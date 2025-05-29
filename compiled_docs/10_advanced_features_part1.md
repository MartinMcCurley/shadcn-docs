# Advanced Features and Integrations

*This document contains 8 files from the shadcn/ui documentation.*

## Table of Contents

- [Blocks](#blocks)
- [Changelog](#changelog)
- [Monorepo](#monorepo)
- [React 19](#react-19)
- [Examples](#examples)
- [Faq](#faq)
- [Getting Started](#getting-started)
- [Registry Item Json](#registry-item-json)



---

## Blocks
*Source: blocks.md*

# Add a block - shadcn/ui

Source: https://ui.shadcn.com/docs/blocks

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Add a block

# Add a block

Contribute components to the blocks library.

We are inviting the community to contribute to the [blocks library](/blocks). Share your components and blocks with other developers and help build a library of high-quality, reusable components.

We'd love to see all types of blocks: applications, marketing, products, and more.

## Setup your workspace

### Fork the repository

```
git clone https://github.com/shadcn-ui/ui.git
```

Copy

### Create a new branch

```
git checkout -b username/my-new-block
```

Copy

### Install dependencies

```
pnpm install
```

Copy

### Start the dev server

```
pnpm www:dev
```

Copy

## Add a block

A block can be a single component (eg. a variation of a ui component) or a complex component (eg. a dashboard) with multiple components, hooks, and utils.

### Create a new block

Create a new folder in the `apps/www/registry/new-york/blocks` directory. Make sure the folder is named in kebab-case and under `new-york`.

```
apps
└── www
    └── registry
        └── new-york
            └── blocks
                └── dashboard-01
```

Copy

**Note:** The build script will take care of building the block for the `default` style.

### Add your block files

Add your files to the block folder. Here is an example of a block with a page, components, hooks, and utils.

```
dashboard-01
└── page.tsx
└── components
    └── hello-world.tsx
    └── example-card.tsx
└── hooks
    └── use-hello-world.ts
└── lib
    └── format-date.ts
```

Copy

**Note:** You can start with one file and add more files later.

## Add your block to the registry

### Add your block definition to `registry-blocks.tsx`

To add your block to the registry, you need to add your block definition to `registry-blocks.ts`.

This follows the registry schema at <https://ui.shadcn.com/schema/registry-item.json>.

apps/www/registry/registry-blocks.tsx

```
export const blocks = [
  // ...
  {
    name: "dashboard-01",
    author: "shadcn (https://ui.shadcn.com)",
    title: "Dashboard",
    description: "A simple dashboard with a hello world component.",
    type: "registry:block",
    registryDependencies: ["input", "button", "card"],
    dependencies: ["zod"],
    files: [
      {
        path: "blocks/dashboard-01/page.tsx",
        type: "registry:page",
        target: "app/dashboard/page.tsx",
      },
      {
        path: "blocks/dashboard-01/components/hello-world.tsx",
        type: "registry:component",
      },
      {
        path: "blocks/dashboard-01/components/example-card.tsx",
        type: "registry:component",
      },
      {
        path: "blocks/dashboard-01/hooks/use-hello-world.ts",
        type: "registry:hook",
      },
      {
        path: "blocks/dashboard-01/lib/format-date.ts",
        type: "registry:lib",
      },
    ],
    categories: ["dashboard"],
  },
]
```

Copy

Make sure you add a name, description, type, registryDependencies, dependencies, files, and categories. We'll go over each of these in more detail in the schema docs (coming soon).

### Run the build script

```
pnpm registry:build
```

Copy

**Note:** you do not need to run this script for every change. You only need to run it when you update the block definition.

### View your block

Once the build script is finished, you can view your block at `http://localhost:3333/blocks/[CATEGORY]` or a full screen preview at `http://localhost:3333/view/styles/new-york/dashboard-01`.

![Block preview](/_next/image?url=%2Fimages%2Fblock-preview-light.png&w=3840&q=75)![Block preview](/_next/image?url=%2Fimages%2Fblock-preview-dark.png&w=3840&q=75)

### Build your block

You can now build your block by editing the files in the block folder and viewing the changes in the browser.

If you add more files, make sure to add them to the `files` array in the block definition.

## Publish your block

Once you're ready to publish your block, you can submit a pull request to the main repository.

### Run the build script

```
pnpm registry:build
```

Copy

### Capture a screenshot

```
pnpm registry:capture
```

Copy

**Note:** If you've run the capture script before, you might need to delete the existing screenshots (both light and dark) at `apps/www/public/r/styles/new-york` and run the script again.

### Submit a pull request

Commit your changes and submit a pull request to the main repository.

Your block will be reviewed and merged. Once merged it will be published to the website and available to be installed via the CLI.

## Categories

The `categories` property is used to organize your block in the registry.

### Add a category

If you need to add a new category, you can do so by adding it to the `registryCategories` array in `apps/www/registry/registry-categories.ts`.

apps/www/registry/registry-categories.ts

```
export const registryCategories = [
  // ...
  {
    name: "Input",
    slug: "input",
    hidden: false,
  },
]
```

Copy

## Guidelines

Here are some guidelines to follow when contributing to the blocks library.

* The following properties are required for the block definition: `name`, `description`, `type`, `files`, and `categories`.
* Make sure to list all registry dependencies in `registryDependencies`. A registry dependency is the name of the component in the registry eg. `input`, `button`, `card`, etc.
* Make sure to list all dependencies in `dependencies`. A dependency is the name of the package in the registry eg. `zod`, `sonner`, etc.
* If your block has a page (optional), it should be the first entry in the `files` array and it should have a `target` property. This helps the CLI place the page in the correct location for file-based routing.
* **Imports should always use the `@/registry` path.** eg. `import { Input } from "@/registry/new-york/input"`

[Open in v0](/docs/v0)[Figma](/docs/figma)

On This Page

* [Setup your workspace](#setup-your-workspace)
  + [Fork the repository](#fork-the-repository)
  + [Create a new branch](#create-a-new-branch)
  + [Install dependencies](#install-dependencies)
  + [Start the dev server](#start-the-dev-server)
* [Add a block](#add-a-block)
  + [Create a new block](#create-a-new-block)
  + [Add your block files](#add-your-block-files)
* [Add your block to the registry](#add-your-block-to-the-registry)
  + [Add your block definition to registry-blocks.tsx](#add-your-block-definition-to-registry-blockstsx)
  + [Run the build script](#run-the-build-script)
  + [View your block](#view-your-block)
  + [Build your block](#build-your-block)
* [Publish your block](#publish-your-block)
  + [Run the build script](#run-the-build-script-1)
  + [Capture a screenshot](#capture-a-screenshot)
  + [Submit a pull request](#submit-a-pull-request)
* [Categories](#categories)
  + [Add a category](#add-a-category)
* [Guidelines](#guidelines)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)

---

## Changelog
*Source: changelog.md*

# Changelog - shadcn/ui

Source: https://ui.shadcn.com/docs/changelog

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Changelog

# Changelog

Latest updates and announcements.

## August 2024 - npx shadcn init

The new CLI is now available. It's a complete rewrite with a lot of new features and improvements. You can now install components, themes, hooks, utils and more using `npx shadcn add`.

This is a major step towards distributing code that you and your LLMs can access and use.

1. First up, the cli now has support for all major React framework out of the box. Next.js, Remix, Vite and Laravel. And when you init into a new app, we update your existing Tailwind files instead of overriding.
2. A component now ship its own dependencies. Take the accordion for example, it can define its Tailwind keyframes. When you add it to your project, we’ll update your tailwind.config.ts file accordingly.
3. You can also install remote components using url. `npx shadcn add https://acme.com/registry/navbar.json`.
4. We have also improve the init command. It does framework detection and can even init a brand new Next.js app in one command. `npx shadcn init`.
5. We have created a new schema that you can use to ship your own component registry. And since it has support for urls, you can even use it to distribute private components.
6. And a few more updates like better error handling and monorepo support.

You can try the new cli today.

pnpmnpmyarnbun

```
pnpm dlx shadcn init sidebar-01 login-01

```

Copy

### Update Your Project

To update an existing project to use the new CLI, update your `components.json` file to include import aliases for your **components**, **utils**, **ui**, **lib** and **hooks**.

components.json

```
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "tailwind": {
    // ...
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  }
}
```

Copy

If you're using a different import alias prefix eg `~`, replace `@` with your prefix.

## April 2024 - Introducing Lift Mode

We're introducing a new mode for [Blocks](/blocks) called **Lift Mode**.

Enable Lift Mode to automatically "lift" smaller components from a block template for copy and paste.

[![Lift Mode](/_next/image?url=%2Fimages%2Flift-mode-light.png&w=3840&q=75)![Lift Mode](/_next/image?url=%2Fimages%2Flift-mode-dark.png&w=3840&q=75)View the blocks library](/blocks)

With Lift Mode, you'll be able to copy the smaller components that make up a block template, like cards, buttons, and forms, and paste them directly into your project.

Visit the [Blocks](/blocks) page to try it out.

## March 2024 - Introducing Blocks

One of the most requested features since launch has been layouts: admin dashboards with sidebar, marketing page sections, cards and more.

**Today, we're launching [**Blocks**](/blocks)**.

[![Admin dashboard](/_next/image?url=%2Fimages%2Fdashboard-1.jpg&w=1920&q=75)![Admin dashboard](/_next/image?url=%2Fimages%2Fdashboard-1-dark.jpg&w=1920&q=75)View the blocks library](/blocks)

Blocks are ready-made components that you can use to build your apps. They are fully responsive, accessible, and composable, meaning they are built using the same principles as the rest of the components in shadcn/ui.

We're starting with dashboard layouts and authentication pages, with plans to add more blocks in the coming weeks.

### Open Source

Blocks are open source. You can find the source on GitHub. Use them in your projects, customize them and contribute back.

[![AI Playground](/_next/image?url=%2Fimages%2Fdashboard-2.jpg&w=1920&q=75)![AI Playground](/_next/image?url=%2Fimages%2Fdashboard-2-dark.jpg&w=1920&q=75)View the blocks library](/blocks)

### Request a Block

We're also introducing a "Request a Block" feature. If there's a specific block you'd like to see, simply create a request on GitHub and the community can upvote and build it.

[![Settings Page](/_next/image?url=%2Fimages%2Fdashboard-3.jpg&w=1920&q=75)![Settings Page](/_next/image?url=%2Fimages%2Fdashboard-3-dark.jpg&w=1920&q=75)View the blocks library](/blocks)

### v0

If you have a [v0](https://v0.dev) account, you can use the **Edit in v0** feature to open the code on v0 for prompting and further generation.

That's it. *Looking forward to seeing what you build with Blocks*.

## March 2024 - Breadcrumb and Input OTP

We've added a new Breadcrumb component and an Input OTP component.

### Breadcrumb

An accessible and flexible breadcrumb component. It has support for collapsed items, custom separators, bring-your-own routing `<Link />` and composable with other shadcn/ui components.

PreviewCode

Style:

Copy

[See more examples](/docs/components/breadcrumb)

### Input OTP

A fully featured input OTP component. It has support for numeric and alphanumeric codes, custom length, copy-paste and accessible. Input OTP is built on top of [input-otp](https://github.com/guilhermerodz/input-otp) by [@guilherme\_rodz](https://twitter.com/guilherme_rodz).

PreviewCode

Style:

Copy

[Read the docs](/docs/components/input-otp)

If you have a [v0](https://v0.dev), the new components are available for generation.

## December 2023 - New components, CLI and more

We've added new components to shadcn/ui and made a lot of improvements to the CLI.

Here's a quick overview of what's new:

* [**Carousel**](#carousel) - A carousel component with motion, swipe gestures and keyboard support.
* [**Drawer**](#drawer) - A drawer component that looks amazing on mobile.
* [**Pagination**](#pagination) - A pagination component with page navigation, previous and next buttons.
* [**Resizable**](#resizable) - A resizable component for building resizable panel groups and layouts.
* [**Sonner**](#sonner) - The last toast component you'll ever need.
* [**CLI updates**](#cli-updates) - Support for custom **Tailwind prefix** and `tailwind.config.ts`.

### Carousel

We've added a fully featured carousel component with motion, swipe gestures and keyboard support. Built on top of [Embla Carousel](https://www.embla-carousel.com).

It has support for infinite looping, autoplay, vertical orientation, and more.

PreviewCode

Style:

Copy

1

2

3

4

5

Previous slideNext slide

### Drawer

Oh the drawer component 😍. Built on top of [Vaul](https://github.com/emilkowalski/vaul) by [emilkowalski\_](https://twitter.com/emilkowalski_).

Try opening the following drawer on mobile. It looks amazing!

PreviewCode

Style:

Copy

Open Drawer

### Pagination

We've added a pagination component with page navigation, previous and next buttons. Simple, flexible and works with your framework's `<Link />` component.

PreviewCode

Style:

Copy

### Resizable

Build resizable panel groups and layouts with this `<Resizable />` component.

PreviewCode

Style:

Copy

One

Two

Three

`<Resizable />` is built using [react-resizable-panels](https://github.com/bvaughn/react-resizable-panels) by [bvaughn](https://github.com/bvaughn). It has support for mouse, touch and keyboard.

### Sonner

Another one by [emilkowalski\_](https://twitter.com/emilkowalski_). The last toast component you'll ever need. Sonner is now availabe in shadcn/ui.

PreviewCode

Style:

Copy

Show Toast

### CLI updates

This has been one of the most requested features. You can now configure a custom Tailwind prefix and the cli will automatically prefix your utility classes when adding components.

This means you can now easily add shadcn/ui components to existing projects like Docusaurus, Nextra...etc. A drop-in for your existing design system with no conflict. 🔥

```
<AlertDialog className="tw-grid tw-gap-4 tw-border tw-bg-background tw-shadow-lg" />
```

Copy

It works with `cn`, `cva` and CSS variables.

The cli can now also detect `tailwind.config.ts` and add the TypeScript version of the config for you.

That's it. Happy Holidays.

## July 2023 - JavaScript

This project and the components are written in TypeScript. **We recommend using TypeScript for your project as well**.

However we provide a JavaScript version of the components, available via the [cli](/docs/cli).

```
Would you like to use TypeScript (recommended)? no
```

Copy

To opt-out of TypeScript, you can use the `tsx` flag in your `components.json` file.

components.json

```
{
  "style": "default",
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "src/app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "rsc": false,
  "tsx": false,
  "aliases": {
    "utils": "~/lib/utils",
    "components": "~/components"
  }
}
```

Copy

To configure import aliases, you can use the following `jsconfig.json`:

jsconfig.json

```
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

Copy

## June 2023 - New CLI, Styles and more

I have a lot of updates to share with you today:

* [**New CLI**](#new-cli) - Rewrote the CLI from scratch. You can now add components, dependencies and configure import paths.
* [**Theming**](#theming-with-css-variables-or-tailwind-colors) - Choose between using CSS variables or Tailwind CSS utility classes for theming.
* [**Base color**](#base-color) - Configure the base color for your project. This will be used to generate the default color palette for your components.
* [**React Server Components**](#react-server-components) - Opt out of using React Server Components. The CLI will automatically append or remove the `use client` directive.
* [**Styles**](#styles) - Introducing a new concept called *Style*. A style comes with its own set of components, animations, icons and more.
* [**Exit animations**](#exit-animations) - Added exit animations to all components.
* [**Other updates**](#other-updates) - New `icon` button size, updated `sheet` component and more.
* [**Updating your project**](#updating-your-project) - How to update your project to get the latest changes.

---

### New CLI

I've been working on a new CLI for the past few weeks. It's a complete rewrite. It comes with a lot of new features and improvements.

### `init`

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest init

```

Copy

When you run the `init` command, you will be asked a few questions to configure `components.json`:

```
Which style would you like to use? › Default
Which color would you like to use as base color? › Slate
Where is your global CSS file? › › app/globals.css
Do you want to use CSS variables for colors? › no / yes
Where is your tailwind.config.js located? › tailwind.config.js
Configure the import alias for components: › @/components
Configure the import alias for utils: › @/lib/utils
Are you using React Server Components? › no / yes
```

Copy

This file contains all the information about your components: where to install them, the import paths, how they are styled...etc.

You can use this file to change the import path of a component, set a baseColor or change the styling method.

components.json

```
{
  "style": "default",
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "src/app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "rsc": false,
  "aliases": {
    "utils": "~/lib/utils",
    "components": "~/components"
  }
}
```

Copy

This means you can now use the CLI with any directory structure including `src` and `app` directories.

### `add`

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest add

```

Copy

The `add` command is now much more capable. You can now add UI components but also import more complex components (coming soon).

The CLI will automatically resolve all components and dependencies, format them based on your custom config and add them to your project.

### `diff` (experimental)

pnpmnpmyarnbun

```
pnpm dlx shadcn diff

```

Copy

We're also introducing a new `diff` command to help you keep track of upstream updates.

You can use this command to see what has changed in the upstream repository and update your project accordingly.

Run the `diff` command to get a list of components that have updates available:

pnpmnpmyarnbun

```
pnpm dlx shadcn diff

```

Copy

```
The following components have updates available:
- button
  - /path/to/my-app/components/ui/button.tsx
- toast
  - /path/to/my-app/components/ui/use-toast.ts
  - /path/to/my-app/components/ui/toaster.tsx
```

Copy

Then run `diff [component]` to see the changes:

pnpmnpmyarnbun

```
pnpm dlx shadcn diff alert

```

Copy

```
const alertVariants = cva(
- "relative w-full rounded-lg border",
+ "relative w-full pl-12 rounded-lg border"
)
```

Copy

---

### Theming with CSS Variables or Tailwind Colors

You can choose between using CSS variables or Tailwind CSS utility classes for theming.

When you add new components, the CLI will automatically use the correct theming methods based on your `components.json` configuration.

#### Utility classes

```
<div className="bg-zinc-950 dark:bg-white" />
```

Copy

To use utility classes for theming set `tailwind.cssVariables` to `false` in your `components.json` file.

components.json

```
{
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": false
  }
}
```

Copy

#### CSS Variables

```
<div className="bg-background text-foreground" />
```

Copy

To use CSS variables classes for theming set `tailwind.cssVariables` to `true` in your `components.json` file.

components.json

```
{
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": true
  }
}
```

Copy

---

### Base color

You can now configure the base color for your project. This will be used to generate the default color palette for your components.

components.json

```
{
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "zinc",
    "cssVariables": false
  }
}
```

Copy

Choose between `gray`, `neutral`, `slate`, `stone` or `zinc`.

If you have `cssVariables` set to `true`, we will set the base colors as CSS variables in your `globals.css` file. If you have `cssVariables` set to `false`, we will inline the Tailwind CSS utility classes in your components.

---

### React Server Components

If you're using a framework that does not support React Server Components, you can now opt out by setting `rsc` to `false`. We will automatically append or remove the `use client` directive when adding components.

components.json

```
{
  "rsc": false
}
```

Copy

---

### Styles

We are introducing a new concept called *Style*.

*You can think of style as the visual foundation: shapes, icons, animations & typography.* A style comes with its own set of components, animations, icons and more.

We are shipping two styles: `default` and `new-york` (with more coming soon).

![Default vs New York style](/_next/image?url=%2Fimages%2Fstyle.jpg&w=1920&q=75)

The `default` style is the one you are used to. It's the one we've been using since the beginning of this project. It uses `lucide-react` for icons and `tailwindcss-animate` for animations.

The `new-york` style is a new style. It ships with smaller buttons, cards with shadows and a new set of icons from [Radix Icons](https://icons.radix-ui.com).

When you run the `init` command, you will be asked which style you would like to use. This is saved in your `components.json` file.

components.json

```
{
  "style": "new-york"
}
```

Copy

### Theming

Start with a style as the base then theme using CSS variables or Tailwind CSS utility classes to completely change the look of your components.

![Style with theming](/_next/image?url=%2Fimages%2Fstyle-with-theming.jpg&w=1920&q=75)

---

### Exit animations

I added exit animations to all components. Click on the combobox below to see the subtle exit animation.

PreviewCode

Style:

Copy

Select framework...

The animations can be customized using utility classes.

---

### Other updates

### Button

* Added a new button size `icon`:

PreviewCode

Style:

Copy

### Sheet

* Renamed `position` to `side` to match the other elements.

PreviewCode

Style:

Copy

toprightbottomleft

* Removed the `size` props. Use `className="w-[200px] md:w-[450px]"` for responsive sizing.

---

### Updating your project

Since we follow a copy and paste approach, you will need to manually update your project to get the latest changes.

Note: we are working on a [`diff`](#diff-experimental) command to help you
keep track of upstream updates.

### Add `components.json`

Creating a `components.json` file at the root:

components.json

```
{
  "style": "default",
  "rsc": true,
  "tailwind": {
    "config": "tailwind.config.js",
    "css": "app/globals.css",
    "baseColor": "slate",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils"
  }
}
```

Copy

Update the values for `tailwind.css` and `aliases` to match your project structure.

### Button

Add the `icon` size to the `buttonVariants`:

components/ui/button.tsx

```
const buttonVariants = cva({
  variants: {
    size: {
      default: "h-10 px-4 py-2",
      sm: "h-9 rounded-md px-3",
      lg: "h-11 rounded-md px-8",
      icon: "h-10 w-10",
    },
  },
})
```

Copy

### Sheet

1. Replace the content of `sheet.tsx` with the following:

components/ui/sheet.tsx

```
"use client"

import * as React from "react"
import * as SheetPrimitive from "@radix-ui/react-dialog"
import { cva, type VariantProps } from "class-variance-authority"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const Sheet = SheetPrimitive.Root

const SheetTrigger = SheetPrimitive.Trigger

const SheetClose = SheetPrimitive.Close

const SheetPortal = ({
  className,
  ...props
}: SheetPrimitive.DialogPortalProps) => (
  <SheetPrimitive.Portal className={cn(className)} {...props} />
)
SheetPortal.displayName = SheetPrimitive.Portal.displayName

const SheetOverlay = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Overlay
    className={cn(
      "fixed inset-0 z-50 bg-background/80 backdrop-blur-sm data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
    ref={ref}
  />
))
SheetOverlay.displayName = SheetPrimitive.Overlay.displayName

const sheetVariants = cva(
  "fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:duration-300 data-[state=open]:duration-500",
  {
    variants: {
      side: {
        top: "inset-x-0 top-0 border-b data-[state=closed]:slide-out-to-top data-[state=open]:slide-in-from-top",
        bottom:
          "inset-x-0 bottom-0 border-t data-[state=closed]:slide-out-to-bottom data-[state=open]:slide-in-from-bottom",
        left: "inset-y-0 left-0 h-full w-3/4 border-r data-[state=closed]:slide-out-to-left data-[state=open]:slide-in-from-left sm:max-w-sm",
        right:
          "inset-y-0 right-0 h-full w-3/4  border-l data-[state=closed]:slide-out-to-right data-[state=open]:slide-in-from-right sm:max-w-sm",
      },
    },
    defaultVariants: {
      side: "right",
    },
  }
)

interface SheetContentProps
  extends React.ComponentPropsWithoutRef<typeof SheetPrimitive.Content>,
    VariantProps<typeof sheetVariants> {}

const SheetContent = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Content>,
  SheetContentProps
>(({ side = "right", className, children, ...props }, ref) => (
  <SheetPortal>
    <SheetOverlay />
    <SheetPrimitive.Content
      ref={ref}
      className={cn(sheetVariants({ side }), className)}
      {...props}
    >
      {children}
      <SheetPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-secondary">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </SheetPrimitive.Close>
    </SheetPrimitive.Content>
  </SheetPortal>
))
SheetContent.displayName = SheetPrimitive.Content.displayName

const SheetHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-2 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
SheetHeader.displayName = "SheetHeader"

const SheetFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
SheetFooter.displayName = "SheetFooter"

const SheetTitle = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Title>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold text-foreground", className)}
    {...props}
  />
))
SheetTitle.displayName = SheetPrimitive.Title.displayName

const SheetDescription = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Description>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
SheetDescription.displayName = SheetPrimitive.Description.displayName

export {
  Sheet,
  SheetTrigger,
  SheetClose,
  SheetContent,
  SheetHeader,
  SheetFooter,
  SheetTitle,
  SheetDescription,
}
```

Copy

2. Rename `position` to `side`

```
- <Sheet position="right" />
+ <Sheet side="right" />
```

Copy

### Thank you

I'd like to thank everyone who has been using this project, providing feedback and contributing to it. I really appreciate it. Thank you 🙏

[Figma](/docs/figma)[Next.js](/docs/installation/next)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)

---

## Monorepo
*Source: monorepo.md*

# Monorepo - shadcn/ui

Source: https://ui.shadcn.com/docs/monorepo

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Monorepo

# Monorepo

Using shadcn/ui components and CLI in a monorepo.

Until now, using shadcn/ui in a monorepo was a bit of a pain. You could add
components using the CLI, but you had to manage where the components
were installed and manually fix import paths.

With the new monorepo support in the CLI, we've made it a lot easier to use
shadcn/ui in a monorepo.

The CLI now understands the monorepo structure and will install the components,
dependencies and registry dependencies to the correct paths and handle imports
for you.

## Getting started

### Create a new monorepo project

To create a new monorepo project, run the `init` command. You will be prompted
to select the type of project you are creating.

pnpmnpmyarnbun

```
pnpm dlx shadcn@canary init

```

Copy

Select the `Next.js (Monorepo)` option.

```
? Would you like to start a new project?
    Next.js
❯   Next.js (Monorepo)
```

Copy

This will create a new monorepo project with two workspaces: `web` and `ui`,
and [Turborepo](https://turbo.build/repo/docs) as the build system.

Everything is set up for you, so you can start adding components to your project.

Note: The monorepo uses React 19 and Tailwind CSS v4.

### Add components to your project

To add components to your project, run the `add` command **in the path of your app**.

```
cd apps/web
```

Copy

pnpmnpmyarnbun

```
pnpm dlx shadcn@canary add [COMPONENT]

```

Copy

The CLI will figure out what type of component you are adding and install the
correct files to the correct path.

For example, if you run `npx shadcn@canary add button`, the CLI will install the button component under `packages/ui` and update the import path for components in `apps/web`.

If you run `npx shadcn@canary add login-01`, the CLI will install the `button`, `label`, `input` and `card` components under `packages/ui` and the `login-form` component under `apps/web/components`.

### Importing components

You can import components from the `@workspace/ui` package as follows:

```
import { Button } from "@workspace/ui/components/button"
```

Copy

You can also import hooks and utilities from the `@workspace/ui` package.

```
import { useTheme } from "@workspace/ui/hooks/use-theme"
import { cn } from "@workspace/ui/lib/utils"
```

Copy

## File Structure

When you create a new monorepo project, the CLI will create the following file structure:

```
apps
└── web         # Your app goes here.
    ├── app
    │   └── page.tsx
    ├── components
    │   └── login-form.tsx
    ├── components.json
    └── package.json
packages
└── ui          # Your components and dependencies are installed here.
    ├── src
    │   ├── components
    │   │   └── button.tsx
    │   ├── hooks
    │   ├── lib
    │   │   └── utils.ts
    │   └── styles
    │       └── globals.css
    ├── components.json
    └── package.json
package.json
turbo.json
```

Copy

## Requirements

1. Every workspace must have a `components.json` file. A `package.json` file tells npm how to install the dependencies. A `components.json` file tells the CLI how and where to install components.
2. The `components.json` file must properly define aliases for the workspace. This tells the CLI how to import components, hooks, utilities, etc.

Tailwind CSS v4Tailwind CSS v3

apps/web/components.json

```
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "../../packages/ui/src/styles/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "hooks": "@/hooks",
    "lib": "@/lib",
    "utils": "@workspace/ui/lib/utils",
    "ui": "@workspace/ui/components"
  }
}
```

Copy

packages/ui/components.json

```
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/styles/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@workspace/ui/components",
    "utils": "@workspace/ui/lib/utils",
    "hooks": "@workspace/ui/hooks",
    "lib": "@workspace/ui/lib",
    "ui": "@workspace/ui/components"
  }
}
```

Copy

3. Ensure you have the same `style`, `iconLibrary` and `baseColor` in both `components.json` files.
4. **For Tailwind CSS v4, leave the `tailwind` config empty in the `components.json` file.**

By following these requirements, the CLI will be able to install ui components, blocks, libs and hooks to the correct paths and handle imports for you.

[CLI](/docs/cli)[Tailwind v4](/docs/tailwind-v4)

On This Page

* [Getting started](#getting-started)
  + [Create a new monorepo project](#create-a-new-monorepo-project)
  + [Add components to your project](#add-components-to-your-project)
  + [Importing components](#importing-components)
* [File Structure](#file-structure)
* [Requirements](#requirements)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)

---

## React 19
*Source: react-19.md*

# Next.js 15 + React 19 - shadcn/ui

Source: https://ui.shadcn.com/docs/react-19

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Next.js 15 + React 19

# Next.js 15 + React 19

Using shadcn/ui with Next.js 15 and React 19.

**Update:** We have added full support for React 19 and Tailwind v4 in the
`canary` release. See the docs for [Tailwind v4](/docs/tailwind-v4) for more
information.

**The following guide applies to any framework that supports React 19**. I
titled this page "Next.js 15 + React 19" to help people upgrading to Next.js
15 find it. We are working with package maintainers to help upgrade to React
19.

## TL;DR

If you're using `npm`, you can install shadcn/ui dependencies with a flag. The `shadcn` CLI will prompt you to select a flag when you run it. No flags required for pnpm, bun, or yarn.

See [Upgrade Status](#upgrade-status) for the status of React 19 support for each package.

## What's happening?

React 19 is now [rc](https://www.npmjs.com/package/react?activeTab=versions) and is [tested and supported in the latest Next.js 15 release](https://nextjs.org/blog/next-15#react-19).

To support React 19, package maintainers will need to test and update their packages to include React 19 as a peer dependency. This is [already](https://github.com/radix-ui/primitives/pull/2952) [in](https://github.com/pacocoursey/cmdk/pull/318) [progress](https://github.com/emilkowalski/vaul/pull/498).

```
"peerDependencies": {
-  "react": "^16.8 || ^17.0 || ^18.0",
+  "react": "^16.8 || ^17.0 || ^18.0 || ^19.0",
-  "react-dom": "^16.8 || ^17.0 || ^18.0"
+  "react-dom": "^16.8 || ^17.0 || ^18.0 || ^19.0"
},
```

Copy

You can check if a package lists React 19 as a peer dependency by running
`npm info <package> peerDependencies`.

In the meantime, if you are installing a package that **does not** list React 19 as a peer dependency, you will see an error message like this:

```
npm error code ERESOLVE
npm error ERESOLVE unable to resolve dependency tree
npm error
npm error While resolving: my-app@0.1.0
npm error Found: react@19.0.0-rc-69d4b800-20241021
npm error node_modules/react
npm error   react@"19.0.0-rc-69d4b800-20241021" from the root project
```

Copy

**Note:** This is npm only. PNPM and Bun will only show a silent warning.

## How to fix this

### Solution 1: `--force` or `--legacy-peer-deps`

You can force install a package with the `--force` or the `--legacy-peer-deps` flag.

```
npm i <package> --force

npm i <package> --legacy-peer-deps
```

Copy

This will install the package and ignore the peer dependency warnings.

### What do the `--force` and `--legacy-peer-deps` flag do?

### Solution 2: Use React 18

You can downgrade `react` and `react-dom` to version 18, which is compatible with the package you are installing and upgrade when the dependency is updated.

```
npm i react@18 react-dom@18
```

Copy

Whichever solution you choose, make sure you test your app thoroughly to ensure
there are no regressions.

## Using shadcn/ui on Next.js 15

### Using pnpm, bun, or yarn

Follow the instructions in the [installation guide](/docs/installation/next) to install shadcn/ui. No flags are needed.

### Using npm

When you run `npx shadcn@latest init -d`, you will be prompted to select an option to resolve the peer dependency issues.

```
It looks like you are using React 19.
Some packages may fail to install due to peer dependency issues (see https://ui.shadcn.com/react-19).

? How would you like to proceed? › - Use arrow-keys. Return to submit.
❯   Use --force
    Use --legacy-peer-deps
```

Copy

You can then run the command with the flag you choose.

## Adding components

The process for adding components is the same as above. Select a flag to resolve the peer dependency issues.

**Remember to always test your app after installing new dependencies.**

## Upgrade Status

To make it easy for you track the progress of the upgrade, I've created a table below with React 19 support status for the shadcn/ui dependencies.

* ✅ - Works with React 19 using npm, pnpm, and bun.
* 🚧 - Works with React 19 using pnpm and bun. Requires flag for npm. PR is in progress.

| Package | Status | Note |
| --- | --- | --- |
| [radix-ui](https://www.npmjs.com/package/@radix-ui/react-icons) | ✅ |  |
| [lucide-react](https://www.npmjs.com/package/lucide-react) | ✅ |  |
| [class-variance-authority](https://www.npmjs.com/package/class-variance-authority) | ✅ | Does not list React 19 as a peer dependency. |
| [tailwindcss-animate](https://www.npmjs.com/package/tailwindcss-animate) | ✅ | Does not list React 19 as a peer dependency. |
| [embla-carousel-react](https://www.npmjs.com/package/embla-carousel-react) | ✅ |  |
| [recharts](https://www.npmjs.com/package/recharts) | ✅ | See note [below](#recharts) |
| [react-hook-form](https://www.npmjs.com/package/react-hook-form) | ✅ |  |
| [react-resizable-panels](https://www.npmjs.com/package/react-resizable-panels) | ✅ |  |
| [sonner](https://www.npmjs.com/package/sonner) | ✅ |  |
| [react-day-picker](https://www.npmjs.com/package/react-day-picker) | ✅ | Works with flag for npm. Work to upgrade to v9 in progress. |
| [input-otp](https://www.npmjs.com/package/input-otp) | ✅ |  |
| [vaul](https://www.npmjs.com/package/vaul) | ✅ |  |
| [@radix-ui/react-icons](https://www.npmjs.com/package/@radix-ui/react-icons) | 🚧 | See [PR #194](https://github.com/radix-ui/icons/pull/194) |
| [cmdk](https://www.npmjs.com/package/cmdk) | ✅ |  |

If you have any questions, please [open an issue](https://github.com/shadcn/ui/issues) on GitHub.

## Recharts

To use recharts with React 19, you will need to override the `react-is` dependency.

### Add the following to your `package.json`

package.json

```
"overrides": {
  "react-is": "^19.0.0-rc-69d4b800-20241021"
}
```

Copy

Note: the `react-is` version needs to match the version of React 19 you are using. The above is an example.

### Run `npm install --legacy-peer-deps`

[Tailwind v4](/docs/tailwind-v4)[Typography](/docs/components/typography)

On This Page

* [TL;DR](#tldr)
* [What's happening?](#whats-happening)
* [How to fix this](#how-to-fix-this)
  + [Solution 1: --force or --legacy-peer-deps](#solution-1---force-or---legacy-peer-deps)
  + [Solution 2: Use React 18](#solution-2-use-react-18)
* [Using shadcn/ui on Next.js 15](#using-shadcnui-on-nextjs-15)
  + [Using pnpm, bun, or yarn](#using-pnpm-bun-or-yarn)
  + [Using npm](#using-npm)
* [Adding components](#adding-components)
* [Upgrade Status](#upgrade-status)
* [Recharts](#recharts)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)

---

## Examples
*Source: registry\examples.md*

# Examples - shadcn/ui

Source: https://ui.shadcn.com/docs/registry/examples

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Examples

# Examples

Examples of registry items: styles, components, css vars, etc.

## registry:style

### Custom style that extends shadcn/ui

The following registry item is a custom style that extends shadcn/ui. On `npx shadcn init`, it will:

* Install `@tabler/icons-react` as a dependency.
* Add the `login-01` block and `calendar` component to the project.
* Add the `editor` from a remote registry.
* Set the `font-sans` variable to `Inter, sans-serif`.
* Install a `brand` color in light and dark mode.

example-style.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "example-style",
  "type": "registry:style",
  "dependencies": ["@tabler/icons-react"],
  "registryDependencies": [
    "login-01",
    "calendar",
    "https://example.com/r/editor.json"
  ],
  "cssVars": {
    "theme": {
      "font-sans": "Inter, sans-serif"
    },
    "light": {
      "brand": "20 14.3% 4.1%"
    },
    "dark": {
      "brand": "20 14.3% 4.1%"
    }
  }
}
```

Copy

### Custom style from scratch

The following registry item is a custom style that doesn't extend shadcn/ui. See the `extends: none` field.

It can be used to create a new style from scratch i.e custom components, css vars, dependencies, etc.

On `npx shadcn add`, the following will:

* Install `tailwind-merge` and `clsx` as dependencies.
* Add the `utils` registry item from the shadcn/ui registry.
* Add the `button`, `input`, `label`, and `select` components from a remote registry.
* Install new css vars: `main`, `bg`, `border`, `text`, `ring`.

example-style.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "extends": "none",
  "name": "new-style",
  "type": "registry:style",
  "dependencies": ["tailwind-merge", "clsx"],
  "registryDependencies": [
    "utils",
    "https://example.com/r/button.json",
    "https://example.com/r/input.json",
    "https://example.com/r/label.json",
    "https://example.com/r/select.json"
  ],
  "cssVars": {
    "theme": {
      "font-sans": "Inter, sans-serif",
    }
    "light": {
      "main": "#88aaee",
      "bg": "#dfe5f2",
      "border": "#000",
      "text": "#000",
      "ring": "#000",
    },
    "dark": {
      "main": "#88aaee",
      "bg": "#272933",
      "border": "#000",
      "text": "#e6e6e6",
      "ring": "#fff",
    }
  }
}
```

Copy

## registry:theme

### Custom theme

example-theme.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "light": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.546 0.245 262.881)",
      "primary-foreground": "oklch(0.97 0.014 254.604)",
      "ring": "oklch(0.746 0.16 232.661)",
      "sidebar-primary": "oklch(0.546 0.245 262.881)",
      "sidebar-primary-foreground": "oklch(0.97 0.014 254.604)",
      "sidebar-ring": "oklch(0.746 0.16 232.661)"
    },
    "dark": {
      "background": "oklch(1 0 0)",
      "foreground": "oklch(0.141 0.005 285.823)",
      "primary": "oklch(0.707 0.165 254.624)",
      "primary-foreground": "oklch(0.97 0.014 254.604)",
      "ring": "oklch(0.707 0.165 254.624)",
      "sidebar-primary": "oklch(0.707 0.165 254.624)",
      "sidebar-primary-foreground": "oklch(0.97 0.014 254.604)",
      "sidebar-ring": "oklch(0.707 0.165 254.624)"
    }
  }
}
```

Copy

### Custom colors

The following style will init using shadcn/ui defaults and then add a custom `brand` color.

example-style.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-style",
  "type": "registry:style",
  "cssVars": {
    "light": {
      "brand": "oklch(0.99 0.00 0)"
    },
    "dark": {
      "brand": "oklch(0.14 0.00 286)"
    }
  }
}
```

Copy

## registry:block

### Custom block

This blocks installs the `login-01` block from the shadcn/ui registry.

login-01.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "login-01",
  "type": "registry:block",
  "description": "A simple login form.",
  "registryDependencies": ["button", "card", "input", "label"],
  "files": [
    {
      "path": "blocks/login-01/page.tsx",
      "content": "import { LoginForm } ...",
      "type": "registry:page",
      "target": "app/login/page.tsx"
    },
    {
      "path": "blocks/login-01/components/login-form.tsx",
      "content": "...",
      "type": "registry:component"
    }
  ]
}
```

Copy

### Install a block and override primitives

You can install a block fromt the shadcn/ui registry and override the primitives using your custom ones.

On `npx shadcn add`, the following will:

* Add the `login-01` block from the shadcn/ui registry.
* Override the `button`, `input`, and `label` primitives with the ones from the remote registry.

example-style.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-login",
  "type": "registry:block",
  "registryDependencies": [
    "login-01",
    "https://example.com/r/button.json",
    "https://example.com/r/input.json",
    "https://example.com/r/label.json"
  ]
}
```

Copy

## CSS Variables

### Custom Theme Variables

Add custom theme variables to the `theme` object.

example-theme.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "theme": {
      "font-heading": "Inter, sans-serif",
      "shadow-card": "0 0 0 1px rgba(0, 0, 0, 0.1)"
    }
  }
}
```

Copy

### Override Tailwind CSS variables

example-theme.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-theme",
  "type": "registry:theme",
  "cssVars": {
    "theme": {
      "spacing": "0.2rem",
      "breakpoint-sm": "640px",
      "breakpoint-md": "768px",
      "breakpoint-lg": "1024px",
      "breakpoint-xl": "1280px",
      "breakpoint-2xl": "1536px"
    }
  }
}
```

Copy

## Add custom CSS

### Base styles

example-base.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-style",
  "type": "registry:style",
  "css": {
    "@layer base": {
      "h1": {
        "font-size": "var(--text-2xl)"
      },
      "h2": {
        "font-size": "var(--text-xl)"
      }
    }
  }
}
```

Copy

### Components

example-card.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-card",
  "type": "registry:component",
  "css": {
    "@layer components": {
      "card": {
        "background-color": "var(--color-white)",
        "border-radius": "var(--rounded-lg)",
        "padding": "var(--spacing-6)",
        "box-shadow": "var(--shadow-xl)"
      }
    }
  }
}
```

Copy

## Add custom utilities

### Simple utility

example-component.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "css": {
    "@utility content-auto": {
      "content-visibility": "auto"
    }
  }
}
```

Copy

### Complex utility

example-utility.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "css": {
    "@utility scrollbar-hidden": {
      "scrollbar-hidden": {
        "&::-webkit-scrollbar": {
          "display": "none"
        }
      }
    }
  }
}
```

Copy

### Functional utilities

example-functional.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "css": {
    "@utility tab-*": {
      "tab-size": "var(--tab-size-*)"
    }
  }
}
```

Copy

## Add custom animations

Note: you need to define both `@keyframes` in css and `theme` in cssVars to use animations.

example-component.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "custom-component",
  "type": "registry:component",
  "cssVars": {
    "theme": {
      "--animate-wiggle": "wiggle 1s ease-in-out infinite"
    }
  },
  "css": {
    "@keyframes wiggle": {
      "0%, 100%": {
        "transform": "rotate(-3deg)"
      },
      "50%": {
        "transform": "rotate(3deg)"
      }
    }
  }
}
```

Copy

[Getting Started](/docs/registry/getting-started)[Open in v0](/docs/registry/open-in-v0)

On This Page

* [registry:style](#registrystyle)
  + [Custom style that extends shadcn/ui](#custom-style-that-extends-shadcnui)
  + [Custom style from scratch](#custom-style-from-scratch)
* [registry:theme](#registrytheme)
  + [Custom theme](#custom-theme)
  + [Custom colors](#custom-colors)
* [registry:block](#registryblock)
  + [Custom block](#custom-block)
  + [Install a block and override primitives](#install-a-block-and-override-primitives)
* [CSS Variables](#css-variables)
  + [Custom Theme Variables](#custom-theme-variables)
  + [Override Tailwind CSS variables](#override-tailwind-css-variables)
* [Add custom CSS](#add-custom-css)
  + [Base styles](#base-styles)
  + [Components](#components)
* [Add custom utilities](#add-custom-utilities)
  + [Simple utility](#simple-utility)
  + [Complex utility](#complex-utility)
  + [Functional utilities](#functional-utilities)
* [Add custom animations](#add-custom-animations)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)

---

## Faq
*Source: registry\faq.md*

# FAQ - shadcn/ui

Source: https://ui.shadcn.com/docs/registry/faq

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

FAQ

# FAQ

Frequently asked questions about running a registry.

## Frequently asked questions

### What does a complex component look like?

Here's an example of a complex component that installs a page, two components, a hook, a format-date utils and a config file.

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "title": "Hello World",
  "type": "registry:block",
  "description": "A complex hello world component",
  "files": [
    {
      "path": "registry/new-york/hello-world/page.tsx",
      "type": "registry:page",
      "target": "app/hello/page.tsx"
    },
    {
      "path": "registry/new-york/hello-world/components/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/components/formatted-message.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/hooks/use-hello.ts",
      "type": "registry:hook"
    },
    {
      "path": "registry/new-york/hello-world/lib/format-date.ts",
      "type": "registry:utils"
    },
    {
      "path": "registry/new-york/hello-world/hello.config.ts",
      "type": "registry:file",
      "target": "~/hello.config.ts"
    }
  ]
}
```

Copy

### How do I add a new Tailwind color?

Tailwind CSS v4Tailwind CSS v3

To add a new color you need to add it to `cssVars` under `light` and `dark` keys.

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "title": "Hello World",
  "type": "registry:block",
  "description": "A complex hello world component",
  "files": [
    // ...
  ],
  "cssVars": {
    "light": {
      "brand-background": "20 14.3% 4.1%",
      "brand-accent": "20 14.3% 4.1%"
    },
    "dark": {
      "brand-background": "20 14.3% 4.1%",
      "brand-accent": "20 14.3% 4.1%"
    }
  }
}
```

Copy

The CLI will update the project CSS file. Once updated, the new colors will be available to be used as utility classes: `bg-brand` and `text-brand-accent`.

### How do I add or override a Tailwind theme variable?

Tailwind CSS v4Tailwind CSS v3

To add or override a theme variable you add it to `cssVars.theme` under the key you want to add or override.

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "title": "Hello World",
  "type": "registry:block",
  "description": "A complex hello world component",
  "files": [
    // ...
  ],
  "cssVars": {
    "theme": {
      "text-base": "3rem",
      "ease-in-out": "cubic-bezier(0.4, 0, 0.2, 1)",
      "font-heading": "Poppins, sans-serif"
    }
  }
}
```

Copy

[Open in v0](/docs/registry/open-in-v0)[registry.json](/docs/registry/registry-json)

On This Page

* [Frequently asked questions](#frequently-asked-questions)
  + [What does a complex component look like?](#what-does-a-complex-component-look-like)
  + [How do I add a new Tailwind color?](#how-do-i-add-a-new-tailwind-color)
  + [How do I add or override a Tailwind theme variable?](#how-do-i-add-or-override-a-tailwind-theme-variable)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)

---

## Getting Started
*Source: registry\getting-started.md*

# Getting Started - shadcn/ui

Source: https://ui.shadcn.com/docs/registry/getting-started

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Getting Started

# Getting Started

Learn how to get setup and run your own component registry.

This guide will walk you through the process of setting up your own component registry.

It assumes you already have a project with components and would like to turn it into a registry.

If you're starting a new registry project, you can use the [registry template](https://github.com/shadcn-ui/registry-template) as a starting point. We have already configured it for you.

## registry.json

The `registry.json` file is only required if you're using the `shadcn` CLI to build your registry.

If you're using a different build system, you can skip this step as long as your build system produces valid JSON files that conform to the [registry-item schema specification](/docs/registry/registry-item-json).

### Add a registry.json file

Create a `registry.json` file in the root of your project. Your project can be a Next.js, Remix, Vite, or any other project that supports React.

registry.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    // ...
  ]
}
```

Copy

This `registry.json` file must conform to the [registry schema specification](/docs/registry/registry-json).

## Add a registry item

### Create your component

Add your first component. Here's an example of a simple `<HelloWorld />` component:

registry/new-york/hello-world/hello-world.tsx

```
import { Button } from "@/components/ui/button"

export function HelloWorld() {
  return <Button>Hello World</Button>
}
```

Copy

**Note:** This example places the component in the `registry/new-york`
directory. You can place it anywhere in your project as long as you set the
correct path in the `registry.json` file and you follow the `registry/[NAME]`
directory structure.

```
registry
└── new-york
    └── hello-world
        └── hello-world.tsx
```

Copy

**Important:** If you're placing your component in a custom directory, make
sure it is configured in your `tailwind.config.ts` file.

```
// tailwind.config.ts
export default {
  content: ["./registry/**/*.{js,ts,jsx,tsx}"],
}
```

Copy

### Add your component to the registry

To add your component to the registry, you need to add your component definition to `registry.json`.

registry.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "acme",
  "homepage": "https://acme.com",
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component.",
      "files": [
        {
          "path": "registry/new-york/hello-world/hello-world.tsx",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

Copy

You define your registry item by adding a `name`, `type`, `title`, `description` and `files`.

For every file you add, you must specify the `path` and `type` of the file. The `path` is the relative path to the file from the root of your project. The `type` is the type of the file.

You can read more about the registry item schema and file types in the [registry item schema docs](/docs/registry/registry-item-json).

## Build your registry

### Install the shadcn CLI

Note: the `build` command is currently only available in the `shadcn@canary` version of the CLI.

pnpmnpmyarnbun

```
pnpm add shadcn@canary

```

Copy

### Add a build script

Add a `registry:build` script to your `package.json` file.

package.json

```
{
  "scripts": {
    "registry:build": "shadcn build"
  }
}
```

Copy

### Run the build script

Run the build script to generate the registry JSON files.

pnpmnpmyarnbun

```
pnpm registry:build

```

Copy

**Note:** By default, the build script will generate the registry JSON files
in `public/r` e.g `public/r/hello-world.json`.

You can change the output directory by passing the `--output` option. See the [shadcn build command](/docs/cli#build) for more information.

## Serve your registry

If you're running your registry on Next.js, you can now serve your registry by running the `next` server. The command might differ for other frameworks.

pnpmnpmyarnbun

```
pnpm dev

```

Copy

Your files will now be served at `http://localhost:3000/r/[NAME].json` eg. `http://localhost:3000/r/hello-world.json`.

## Publish your registry

To make your registry available to other developers, you can publish it by deploying your project to a public URL.

## Adding Auth

The `shadcn` CLI does not offer a built-in way to add auth to your registry. We recommend handling authorization on your registry server.

A common simple approach is to use a `token` query parameter to authenticate requests to your registry. e.g. `http://localhost:3000/r/hello-world.json?token=[SECURE_TOKEN_HERE]`.

Use the secure token to authenticate requests and return a 401 Unauthorized response if the token is invalid. Both the `shadcn` CLI and `Open in v0` will handle the 401 response and display a message to the user.

**Note:** Make sure to encrypt and expire tokens.

## Guidelines

Here are some guidelines to follow when building components for a registry.

* Place your registry item in the `registry/[STYLE]/[NAME]` directory. I'm using `new-york` as an example. It can be anything you want as long as it's nested under the `registry` directory.
* The following properties are required for the block definition: `name`, `description`, `type` and `files`.
* Make sure to list all registry dependencies in `registryDependencies`. A registry dependency is the name of the component in the registry eg. `input`, `button`, `card`, etc or a URL to a registry item eg. `http://localhost:3000/r/editor.json`.
* Make sure to list all dependencies in `dependencies`. A dependency is the name of the package in the registry eg. `zod`, `sonner`, etc. To set a version, you can use the `name@version` format eg. `zod@^3.20.0`.
* **Imports should always use the `@/registry` path.** eg. `import { HelloWorld } from "@/registry/new-york/hello-world/hello-world"`
* Ideally, place your files within a registry item in `components`, `hooks`, `lib` directories.

## Install using the CLI

To install a registry item using the `shadcn` CLI, use the `add` command followed by the URL of the registry item.

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest add http://localhost:3000/r/hello-world.json

```

Copy

[Introduction](/docs/registry)[Examples](/docs/registry/examples)

On This Page

* [registry.json](#registryjson)
  + [Add a registry.json file](#add-a-registryjson-file)
* [Add a registry item](#add-a-registry-item)
  + [Create your component](#create-your-component)
  + [Add your component to the registry](#add-your-component-to-the-registry)
* [Build your registry](#build-your-registry)
  + [Install the shadcn CLI](#install-the-shadcn-cli)
  + [Add a build script](#add-a-build-script)
  + [Run the build script](#run-the-build-script)
* [Serve your registry](#serve-your-registry)
* [Publish your registry](#publish-your-registry)
* [Adding Auth](#adding-auth)
* [Guidelines](#guidelines)
* [Install using the CLI](#install-using-the-cli)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)

---

## Registry Item Json
*Source: registry\registry-item-json.md*

# registry-item.json - shadcn/ui

Source: https://ui.shadcn.com/docs/registry/registry-item-json

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

registry-item.json

# registry-item.json

Specification for registry items.

The `registry-item.json` schema is used to define your custom registry items.

registry-item.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json",
  "name": "hello-world",
  "type": "registry:block",
  "title": "Hello World",
  "description": "A simple hello world component.",
  "files": [
    {
      "path": "registry/new-york/hello-world/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/use-hello-world.ts",
      "type": "registry:hook"
    }
  ],
  "cssVars": {
    "theme": {
      "font-heading": "Poppins, sans-serif"
    },
    "light": {
      "brand": "20 14.3% 4.1%"
    },
    "dark": {
      "brand": "20 14.3% 4.1%"
    }
  }
}
```

Copy

[See more examples](/docs/registry/examples)

## Definitions

You can see the JSON Schema for `registry-item.json` [here](https://ui.shadcn.com/schema/registry-item.json).

### $schema

The `$schema` property is used to specify the schema for the `registry-item.json` file.

registry-item.json

```
{
  "$schema": "https://ui.shadcn.com/schema/registry-item.json"
}
```

Copy

### name

The name of the item. This is used to identify the item in the registry. It should be unique for your registry.

registry-item.json

```
{
  "name": "hello-world"
}
```

Copy

### title

A human-readable title for your registry item. Keep it short and descriptive.

registry-item.json

```
{
  "title": "Hello World"
}
```

Copy

### description

A description of your registry item. This can be longer and more detailed than the `title`.

registry-item.json

```
{
  "description": "A simple hello world component."
}
```

Copy

### type

The `type` property is used to specify the type of your registry item. This is used to determine the type and target path of the item when resolved for a project.

registry-item.json

```
{
  "type": "registry:block"
}
```

Copy

The following types are supported:

| Type | Description |
| --- | --- |
| `registry:block` | Use for complex components with multiple files. |
| `registry:component` | Use for simple components. |
| `registry:lib` | Use for lib and utils. |
| `registry:hook` | Use for hooks. |
| `registry:ui` | Use for UI components and single-file primitives |
| `registry:page` | Use for page or file-based routes. |
| `registry:file` | Use for miscellaneous files. |
| `registry:style` | Use for registry styles. eg. `new-york` |
| `registry:theme` | Use for themes. |

### author

The `author` property is used to specify the author of the registry item.

It can be unique to the registry item or the same as the author of the registry.

registry-item.json

```
{
  "author": "John Doe <john@doe.com>"
}
```

Copy

### dependencies

The `dependencies` property is used to specify the dependencies of your registry item. This is for `npm` packages.

Use `@version` to specify the version of your registry item.

registry-item.json

```
{
  "dependencies": [
    "@radix-ui/react-accordion",
    "zod",
    "lucide-react",
    "name@1.0.2"
  ]
}
```

Copy

### registryDependencies

Used for registry dependencies. Can be names or URLs. Use the name of the item to reference shadcn/ui components and urls to reference other registries.

* For `shadcn/ui` registry items such as `button`, `input`, `select`, etc use the name eg. `['button', 'input', 'select']`.
* For custom registry items use the URL of the registry item eg. `['https://example.com/r/hello-world.json']`.

registry-item.json

```
{
  "registryDependencies": [
    "button",
    "input",
    "select",
    "https://example.com/r/editor.json"
  ]
}
```

Copy

Note: The CLI will automatically resolve remote registry dependencies.

### files

The `files` property is used to specify the files of your registry item. Each file has a `path`, `type` and `target` (optional) property.

**The `target` property is required for `registry:page` and `registry:file` types.**

registry-item.json

```
{
  "files": [
    {
      "path": "registry/new-york/hello-world/page.tsx",
      "type": "registry:page",
      "target": "app/hello/page.tsx"
    },
    {
      "path": "registry/new-york/hello-world/hello-world.tsx",
      "type": "registry:component"
    },
    {
      "path": "registry/new-york/hello-world/use-hello-world.ts",
      "type": "registry:hook"
    },
    {
      "path": "registry/new-york/hello-world/.env",
      "type": "registry:file",
      "target": "~/.env"
    }
  ]
}
```

Copy

#### path

The `path` property is used to specify the path to the file in your registry. This path is used by the build script to parse, transform and build the registry JSON payload.

#### type

The `type` property is used to specify the type of the file. See the [type](#type) section for more information.

#### target

The `target` property is used to indicate where the file should be placed in a project. This is optional and only required for `registry:page` and `registry:file` types.

By default, the `shadcn` cli will read a project's `components.json` file to determine the target path. For some files, such as routes or config you can specify the target path manually.

Use `~` to refer to the root of the project e.g `~/foo.config.js`.

### tailwind

**DEPRECATED:** Use `cssVars.theme` instead for Tailwind v4 projects.

The `tailwind` property is used for tailwind configuration such as `theme`, `plugins` and `content`.

You can use the `tailwind.config` property to add colors, animations and plugins to your registry item.

registry-item.json

```
{
  "tailwind": {
    "config": {
      "theme": {
        "extend": {
          "colors": {
            "brand": "hsl(var(--brand))"
          },
          "keyframes": {
            "wiggle": {
              "0%, 100%": { "transform": "rotate(-3deg)" },
              "50%": { "transform": "rotate(3deg)" }
            }
          },
          "animation": {
            "wiggle": "wiggle 1s ease-in-out infinite"
          }
        }
      }
    }
  }
}
```

Copy

### cssVars

Use to define CSS variables for your registry item.

registry-item.json

```
{
  "cssVars": {
    "theme": {
      "font-heading": "Poppins, sans-serif"
    },
    "light": {
      "brand": "20 14.3% 4.1%",
      "radius": "0.5rem"
    },
    "dark": {
      "brand": "20 14.3% 4.1%"
    }
  }
}
```

Copy

### css

Use `css` to add new rules to the project's CSS file eg. `@layer base`, `@layer components`, `@utility`, `@keyframes`, etc.

registry-item.json

```
{
  "css": {
    "@layer base": {
      "body": {
        "font-size": "var(--text-base)",
        "line-height": "1.5"
      }
    },
    "@layer components": {
      "button": {
        "background-color": "var(--color-primary)",
        "color": "var(--color-white)"
      }
    },
    "@utility text-magic": {
      "font-size": "var(--text-base)",
      "line-height": "1.5"
    },
    "@keyframes wiggle": {
      "0%, 100%": {
        "transform": "rotate(-3deg)"
      },
      "50%": {
        "transform": "rotate(3deg)"
      }
    }
  }
}
```

Copy

### docs

Use `docs` to show custom documentation or message when installing your registry item via the CLI.

registry-item.json

```
{
  "docs": "Remember to add the FOO_BAR environment variable to your .env file."
}
```

Copy

### categories

Use `categories` to organize your registry item.

registry-item.json

```
{
  "categories": ["sidebar", "dashboard"]
}
```

Copy

### meta

Use `meta` to add additional metadata to your registry item. You can add any key/value pair that you want to be available to the registry item.

registry-item.json

```
{
  "meta": { "foo": "bar" }
}
```

Copy

[registry.json](/docs/registry/registry-json)

On This Page

* [Definitions](#definitions)
  + [$schema](#schema)
  + [name](#name)
  + [title](#title)
  + [description](#description)
  + [type](#type)
  + [author](#author)
  + [dependencies](#dependencies)
  + [registryDependencies](#registrydependencies)
  + [files](#files)
  + [tailwind](#tailwind)
  + [cssVars](#cssvars)
  + [css](#css)
  + [docs](#docs)
  + [categories](#categories)
  + [meta](#meta)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)