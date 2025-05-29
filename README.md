# Shadcn/UI Documentation Scraper

A robust Python scraper for downloading and converting [shadcn/ui](https://ui.shadcn.com/) documentation to local Markdown files.

## Features

- 🚀 **Robust scraping** with error handling and retry logic
- 📊 **Progress tracking** with resume capability if interrupted
- 🧹 **Content cleaning** removes navigation and unwanted elements
- 📁 **Organized output** maintains the original documentation structure
- 🔄 **Resume capability** - can continue from where it left off
- 📝 **Comprehensive logging** to both console and file
- ⚡ **Polite scraping** with configurable delays between requests

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd shadcn-docs
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Simply run the scraper:

```bash
python scrape_shadcn_docs.py
```

The scraper will:
- Create a `shadcn_docs` folder with all documentation
- Save progress to `scraper_progress.json` for resume capability
- Log all activity to `scraper.log`
- Display progress in the terminal

### Configuration

You can modify these settings at the top of `scrape_shadcn_docs.py`:

- `DELAY`: Time between requests (default: 0.5 seconds)
- `DEPTH_LIMIT`: How deep to crawl (default: 2 levels)
- `TIMEOUT`: Request timeout (default: 15 seconds)
- `OUTDIR`: Output directory name (default: "shadcn_docs")

## Output Structure

The scraper maintains the original documentation structure:

```
shadcn_docs/
├── index.md                    # Main documentation page
├── installation/
│   ├── next.md
│   ├── vite.md
│   └── ...
├── components/
│   ├── accordion.md
│   ├── button.md
│   └── ...
└── ...
```

Each Markdown file includes:
- Clean, formatted content
- Source URL reference
- Proper heading structure

## Features in Detail

### Resume Capability
If the scraper is interrupted (Ctrl+C, network issues, etc.), simply run it again. It will automatically resume from where it left off using the saved progress.

### Error Handling
- Failed URLs are tracked and reported
- Network timeouts are handled gracefully
- Individual page failures don't stop the entire scrape

### Content Cleaning
The scraper automatically removes:
- Navigation menus
- Headers and footers
- Sidebar content
- Advertisements
- Scripts and styles

## Requirements

- Python 3.7+
- See `requirements.txt` for package dependencies

## Author

**Martin McCurley**

## License

This project is for educational and personal use. Please respect the shadcn/ui website's terms of service and rate limits.

## Contributing

Feel free to submit issues and enhancement requests! 