#!/usr/bin/env python3
"""
Compile shadcn/ui documentation into consolidated markdown files for LLM consumption.
Usage: python compile_docs.py
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration
SOURCE_DIR = "shadcn_docs"
OUTPUT_DIR = "compiled_docs"
MAX_FILES = 10
MAX_FILE_SIZE = 100000  # ~100KB per file (roughly 25k tokens)

# Define logical groupings for content
CONTENT_GROUPS = {
    "01_getting_started": {
        "description": "Installation, Setup, and Getting Started",
        "patterns": ["installation", "docs.md", "cli.md", "components-json.md"],
        "directories": ["installation"]
    },
    "02_theming_styling": {
        "description": "Theming, Dark Mode, and Styling",
        "patterns": ["theming.md", "dark-mode.md", "tailwind-v4.md"],
        "directories": ["dark-mode"]
    },
    "03_basic_components": {
        "description": "Basic UI Components (Buttons, Inputs, Labels)",
        "patterns": ["button.md", "input.md", "label.md", "textarea.md", "checkbox.md", 
                    "radio-group.md", "switch.md", "slider.md", "progress.md", "badge.md", "avatar.md"]
    },
    "04_layout_components": {
        "description": "Layout and Structure Components",
        "patterns": ["card.md", "separator.md", "aspect-ratio.md", "resizable.md", 
                    "scroll-area.md", "skeleton.md", "tabs.md", "accordion.md", "collapsible.md"]
    },
    "05_navigation_components": {
        "description": "Navigation and Menu Components",
        "patterns": ["navigation-menu.md", "menubar.md", "breadcrumb.md", "pagination.md",
                    "sidebar.md", "command.md"]
    },
    "06_overlay_components": {
        "description": "Dialogs, Modals, and Overlay Components",
        "patterns": ["dialog.md", "alert-dialog.md", "sheet.md", "drawer.md", "popover.md",
                    "hover-card.md", "tooltip.md", "dropdown-menu.md", "context-menu.md"]
    },
    "07_form_components": {
        "description": "Forms and Input Components",
        "patterns": ["form.md", "select.md", "combobox.md", "date-picker.md", "input-otp.md",
                    "toggle.md", "toggle-group.md", "calendar.md"]
    },
    "08_data_components": {
        "description": "Data Display and Tables",
        "patterns": ["table.md", "data-table.md", "chart.md", "typography.md"]
    },
    "09_feedback_components": {
        "description": "Alerts, Toasts, and Feedback",
        "patterns": ["alert.md", "toast.md", "sonner.md", "carousel.md"]
    },
    "10_advanced_features": {
        "description": "Advanced Features and Integrations",
        "patterns": ["blocks.md", "registry.md", "figma.md", "v0.md", "react-19.md", 
                    "monorepo.md", "changelog.md", "components.md"],
        "directories": ["registry"]
    }
}

class DocumentCompiler:
    def __init__(self):
        self.source_path = Path(SOURCE_DIR)
        self.output_path = Path(OUTPUT_DIR)
        self.output_path.mkdir(exist_ok=True)
        
    def get_all_md_files(self) -> List[Path]:
        """Get all markdown files from the source directory."""
        md_files = []
        for root, dirs, files in os.walk(self.source_path):
            for file in files:
                if file.endswith('.md'):
                    md_files.append(Path(root) / file)
        return md_files
    
    def read_file_content(self, file_path: Path) -> str:
        """Read and return file content with metadata."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add file source information
            relative_path = file_path.relative_to(self.source_path)
            header = f"\n\n---\n\n## {relative_path.stem.replace('-', ' ').title()}\n"
            header += f"*Source: {relative_path}*\n\n"
            
            return header + content
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return f"\n\n---\n\n## Error reading {file_path.name}\n\nFile could not be read: {e}\n\n"
    
    def file_matches_group(self, file_path: Path, group_config: Dict) -> bool:
        """Check if a file matches a content group."""
        relative_path = file_path.relative_to(self.source_path)
        file_name = file_path.name
        
        # Check filename patterns
        patterns = group_config.get("patterns", [])
        for pattern in patterns:
            if pattern in file_name:
                return True
        
        # Check directory patterns
        directories = group_config.get("directories", [])
        for directory in directories:
            if str(relative_path).startswith(directory):
                return True
        
        return False
    
    def group_files(self, md_files: List[Path]) -> Dict[str, List[Path]]:
        """Group files according to content categories."""
        grouped_files = {group: [] for group in CONTENT_GROUPS.keys()}
        ungrouped_files = []
        
        for file_path in md_files:
            matched = False
            for group_name, group_config in CONTENT_GROUPS.items():
                if self.file_matches_group(file_path, group_config):
                    grouped_files[group_name].append(file_path)
                    matched = True
                    break
            
            if not matched:
                ungrouped_files.append(file_path)
        
        # Add ungrouped files to the most appropriate category or create overflow
        if ungrouped_files:
            print(f"Warning: {len(ungrouped_files)} files didn't match any group:")
            for f in ungrouped_files:
                print(f"  - {f.relative_to(self.source_path)}")
            # Add to advanced features group
            grouped_files["10_advanced_features"].extend(ungrouped_files)
        
        return grouped_files
    
    def estimate_content_size(self, files: List[Path]) -> int:
        """Estimate the total size of content when combined."""
        total_size = 0
        for file_path in files:
            try:
                total_size += file_path.stat().st_size
            except:
                total_size += 1000  # fallback estimate
        return total_size
    
    def split_large_groups(self, grouped_files: Dict[str, List[Path]]) -> Dict[str, List[Path]]:
        """Split large groups that exceed size limits."""
        final_groups = {}
        
        for group_name, files in grouped_files.items():
            if not files:
                continue
                
            estimated_size = self.estimate_content_size(files)
            
            if estimated_size <= MAX_FILE_SIZE:
                final_groups[group_name] = files
            else:
                # Split into multiple parts
                print(f"Splitting large group {group_name} ({estimated_size} bytes)")
                
                # Sort files by size (largest first) for better distribution
                files_with_size = [(f, f.stat().st_size) for f in files]
                files_with_size.sort(key=lambda x: x[1], reverse=True)
                
                current_group = []
                current_size = 0
                part_num = 1
                
                for file_path, file_size in files_with_size:
                    if current_size + file_size > MAX_FILE_SIZE and current_group:
                        # Save current group and start new one
                        part_name = f"{group_name}_part{part_num}"
                        final_groups[part_name] = current_group
                        current_group = [file_path]
                        current_size = file_size
                        part_num += 1
                    else:
                        current_group.append(file_path)
                        current_size += file_size
                
                # Add remaining files
                if current_group:
                    part_name = f"{group_name}_part{part_num}" if part_num > 1 else group_name
                    final_groups[part_name] = current_group
        
        return final_groups
    
    def compile_group(self, group_name: str, files: List[Path]) -> str:
        """Compile a group of files into a single document."""
        if not files:
            return ""
        
        # Get group description
        base_group = group_name.split('_part')[0]  # Remove part suffix if present
        group_config = CONTENT_GROUPS.get(base_group, {})
        description = group_config.get("description", "Documentation")
        
        # Create header
        content = f"# {description}\n\n"
        content += f"*This document contains {len(files)} files from the shadcn/ui documentation.*\n\n"
        
        # Add table of contents
        content += "## Table of Contents\n\n"
        for file_path in sorted(files):
            title = file_path.stem.replace('-', ' ').title()
            content += f"- [{title}](#{file_path.stem.replace('-', '-').lower()})\n"
        content += "\n"
        
        # Add all file contents
        for file_path in sorted(files):
            file_content = self.read_file_content(file_path)
            content += file_content
        
        return content
    
    def compile_all(self):
        """Main compilation function."""
        print("🔍 Finding all markdown files...")
        md_files = self.get_all_md_files()
        print(f"Found {len(md_files)} markdown files")
        
        print("\n📊 Grouping files by content type...")
        grouped_files = self.group_files(md_files)
        
        # Show grouping results
        for group_name, files in grouped_files.items():
            if files:
                size = self.estimate_content_size(files)
                print(f"  {group_name}: {len(files)} files (~{size//1000}KB)")
        
        print("\n🔧 Splitting large groups if necessary...")
        final_groups = self.split_large_groups(grouped_files)
        
        print(f"\n📝 Compiling into {len(final_groups)} documents...")
        
        # Compile each group
        for group_name, files in final_groups.items():
            if not files:
                continue
                
            print(f"  Compiling {group_name}...")
            content = self.compile_group(group_name, files)
            
            output_file = self.output_path / f"{group_name}.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            size_kb = len(content) // 1000
            print(f"    ✅ {output_file.name} ({size_kb}KB, {len(files)} files)")
        
        print(f"\n🎉 Compilation complete!")
        print(f"📁 Output directory: {self.output_path}")
        print(f"📋 Created {len(final_groups)} compiled documents")
        
        # Summary
        total_files = sum(len(files) for files in final_groups.values())
        print(f"\n📊 Summary:")
        print(f"   Original files: {len(md_files)}")
        print(f"   Compiled files: {len(final_groups)}")
        print(f"   Files processed: {total_files}")

if __name__ == "__main__":
    compiler = DocumentCompiler()
    compiler.compile_all() 