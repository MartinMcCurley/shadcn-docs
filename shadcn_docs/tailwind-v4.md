# Tailwind v4 - shadcn/ui

Source: https://ui.shadcn.com/docs/tailwind-v4

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Tailwind v4

# Tailwind v4

How to use shadcn/ui with Tailwind v4 and React 19.

It’s here! Tailwind v4 and React 19. Ready for you to try out. You can start using it today.

[Get Started](#try-it-out)[See Demo](https://v4.shadcn.com)

## What's New

* The CLI can now initialize projects with Tailwind v4.
* Full support for the new `@theme` directive and `@theme inline` option.
* All components are updated for Tailwind v4 and React 19.
* We’ve removed the forwardRefs and adjusted the types.
* Every primitive now has a `data-slot` attribute for styling.
* We've fixed and cleaned up the style of the components.
* We're deprecating the `toast` component in favor of `sonner`.
* Buttons now use the default cursor.
* We're deprecating the `default` style. New projects will use `new-york`.
* HSL colors are now converted to OKLCH.

**Note: this is non-breaking. Your existing apps with Tailwind v3 and React 18 will still work. When you add new components, they'll still be in v3 and React 18 until you upgrade. Only new projects start with Tailwind v4 and React 19.**

## See it Live

I put together a demo with all the updated components here: <https://v4.shadcn.com>

Take a look and test the components. If you find any bugs, please let me know on [GitHub](https://github.com/shadcn-ui/ui).

## Try It Out

You can test Tailwind v4 + React 19 today using the `canary` release of the CLI. See the framework specific guides below for how to get started.

[Next.js

Next.js](/docs/installation/next)[Vite

Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Astro

Astro](/docs/installation/astro)[TanStack Start](/docs/installation/tanstack)[Gatsby

Gatsby](/docs/installation/gatsby)[React

Manual](/docs/installation/manual)

## Upgrade Your Project

**Important:** Before upgrading, please read the [Tailwind v4 Compatibility
Docs](https://tailwindcss.com/docs/compatibility) and make sure your project
is ready for the upgrade. Tailwind v4 uses bleeding-edge browser features and
is designed for modern browsers.

One of the major advantages of using `shadcn/ui` is that the code you end up with is exactly what you'd write yourself. There are no hidden abstractions.

This means when a dependency has a new release, you can just follow the official upgrade paths.

Here's how to upgrade your existing projects (full docs are on the way):

### 1. Follow the Tailwind v4 Upgrade Guide

* Upgrade to Tailwind v4 by following the official upgrade guide: <https://tailwindcss.com/docs/upgrade-guide>
* Use the `@tailwindcss/upgrade@next` codemod to remove deprecated utility classes and update tailwind config.

### 2. Update your CSS variables

The codemod will migrate your CSS variables as references under the `@theme` directive.

```
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.9%;
  }
}

@theme {
  --color-background: hsl(var(--background));
  --color-foreground: hsl(var(--foreground));
}
```

Copy

This works. But to make it easier to work with colors and other variables, we'll need to move the `hsl` wrappers and use `@theme inline`.

Here's how you do it:

1. Move `:root` and `.dark` out of the `@layer` base.
2. Wrap the color values in `hsl()`
3. Add the `inline` option to `@theme` i.e `@theme inline`
4. Remove the `hsl()` wrappers from `@theme`

```
:root {
  --background: hsl(0 0% 100%); // <-- Wrap in hsl
  --foreground: hsl(0 0% 3.9%);
}

.dark {
  --background: hsl(0 0% 3.9%); // <-- Wrap in hsl
  --foreground: hsl(0 0% 98%);
}

@theme inline {
  --color-background: var(--background); // <-- Remove hsl
  --color-foreground: var(--foreground);
}
```

Copy

This change makes it much simpler to access your theme variables in both utility classes and outside of CSS for eg. using color values in JavaScript.

### 3. Update colors for charts

Now that the theme colors come with `hsl()`, you can remove the wrapper in your `chartConfig`:

```
const chartConfig = {
  desktop: {
    label: "Desktop",
-    color: "hsl(var(--chart-1))",
+    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
-   color: "hsl(var(--chart-2))",
+   color: "var(--chart-2)",
  },
} satisfies ChartConfig
```

Copy

### 4. Use new `size-*` utility

The new `size-*` utility (added in Tailwind v3.4), is now fully supported by `tailwind-merge`. You can replace `w-* h-*` with the new `size-*` utility:

```
- w-4 h-4
+ size-4
```

Copy

### 5. Update your dependencies

```
pnpm up "@radix-ui/*" cmdk lucide-react recharts tailwind-merge clsx --latest
```

Copy

### 6. Remove forwardRef

You can use the `remove-forward-ref` codemod to migrate your `forwardRef` to props or manually update the primitives.

For the codemod, see <https://github.com/reactjs/react-codemod#remove-forward-ref>.

If you want to do it manually, here's how to do it step by step:

1. Replace `React.forwardRef<...>` with `React.ComponentProps<...>`
2. Remove `ref={ref}` from the component.
3. Add a `data-slot` attribute. This will come in handy for styling with Tailwind.
4. You can optionally convert to a named function and remove the `displayName`.

#### Before

```
const AccordionItem = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Item>
>(({ className, ...props }, ref) => (
  <AccordionPrimitive.Item
    ref={ref}
    className={cn("border-b last:border-b-0", className)}
    {...props}
  />
))
AccordionItem.displayName = "AccordionItem"
```

Copy

#### After

```
function AccordionItem({
  className,
  ...props
}: React.ComponentProps<typeof AccordionPrimitive.Item>) {
  return (
    <AccordionPrimitive.Item
      data-slot="accordion-item"
      className={cn("border-b last:border-b-0", className)}
      {...props}
    />
  )
}
```

Copy

## Changelog

### March 19, 2025 - Deprecate `tailwindcss-animate`

We've deprecated `tailwindcss-animate` in favor of `tw-animate-css`.

New project will have `tw-animate-css` installed by default.

For existing projects, follow the steps below to migrate.

1. Remove `tailwindcss-animate` from your dependencies.
2. Remove the `@plugin 'tailwindcss-animate'` from your globals.css file.
3. Install `tw-animate-css` as a dev dependency.
4. Add the `@import "tw-animate-css"` to your globals.css file.

```
- @plugin 'tailwindcss-animate';
+ @import "tw-animate-css";
```

Copy

### March 12, 2025 - New Dark Mode Colors

We've revisted the dark mode colors and updated them to be more accessible.

If you're running an existing Tailwind v4 project (**not an upgraded one**[1](#user-content-fn-1)), you can update your components to use the new dark mode colors by re-adding your components using the CLI[2](#user-content-fn-2).

### Commit any changes

**The CLI will overwrite your existing components.** We recommend committing any changes you've made to your components before running the CLI.

```
git add .
git commit -m "..."
```

Copy

### Update components

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest add --all --overwrite

```

Copy

### Update colors

Update the dark mode colors in your `globals.css` file to new OKLCH colors. See the [Base Colors](/docs/theming#base-colors) reference for a list of colors.

### Review changes

Review and re-apply any changes you made to your components.

## Footnotes

1. Upgraded projects are not affected by this change. You can continue using the old dark mode colors. [↩](#user-content-fnref-1)
2. Updating your components will overwrite your existing components. [↩](#user-content-fnref-2)

[Monorepo](/docs/monorepo)[Next.js 15 + React 19](/docs/react-19)

On This Page

* [What's New](#whats-new)
* [See it Live](#see-it-live)
* [Try It Out](#try-it-out)
* [Upgrade Your Project](#upgrade-your-project)
  + [1. Follow the Tailwind v4 Upgrade Guide](#1-follow-the-tailwind-v4-upgrade-guide)
  + [2. Update your CSS variables](#2-update-your-css-variables)
  + [3. Update colors for charts](#3-update-colors-for-charts)
  + [4. Use new size-\* utility](#4-use-new-size--utility)
  + [5. Update your dependencies](#5-update-your-dependencies)
  + [6. Remove forwardRef](#6-remove-forwardref)
* [Changelog](#changelog)
  + [March 19, 2025 - Deprecate tailwindcss-animate](#march-19-2025---deprecate-tailwindcss-animate)
  + [March 12, 2025 - New Dark Mode Colors](#march-12-2025---new-dark-mode-colors)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)