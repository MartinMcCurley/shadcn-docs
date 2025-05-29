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