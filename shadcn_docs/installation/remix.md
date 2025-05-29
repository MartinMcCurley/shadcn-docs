# Remix - shadcn/ui

Source: https://ui.shadcn.com/docs/installation/remix

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Remix

# Remix

Install and configure shadcn/ui for Remix.

**Note:** The following guide is for Tailwind v4. If you are using Tailwind
v3, use `shadcn@2.3.0`.

**Note:** This guide is for Remix. For React Router, see the [React Router](/docs/installation/react-router) guide.

### Create project

Start by creating a new Remix project using `create-remix`:

pnpmnpmyarnbun

```
pnpm create remix@latest my-app

```

Copy

### Run the CLI

Run the `shadcn` init command to setup your project:

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest init

```

Copy

### Configure components.json

You will be asked a few questions to configure `components.json`:

```
Which style would you like to use? › New York
Which color would you like to use as base color? › Zinc
Do you want to use CSS variables for colors? › no / yes
```

Copy

### App structure

**Note**: This app structure is only a suggestion. You can place the files wherever you want.

* Place the UI components in the `app/components/ui` folder.
* Your own components can be placed in the `app/components` folder.
* The `app/lib` folder contains all the utility functions. We have a `utils.ts` where we define the `cn` helper.
* The `app/tailwind.css` file contains the global CSS.

### Install Tailwind CSS

pnpmnpmyarnbun

```
pnpm add -D tailwindcss@latest autoprefixer@latest

```

Copy

Then we create a `postcss.config.js` file:

```
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

Copy

And finally we add the following to our `remix.config.js` file:

```
/** @type {import('@remix-run/dev').AppConfig} */
export default {
  ...
  tailwind: true,
  postcss: true,
  ...
};
```

Copy

### Add `tailwind.css` to your app

In your `app/root.tsx` file, import the `tailwind.css` file:

```
import styles from "./tailwind.css?url"

export const links: LinksFunction = () => [
  { rel: "stylesheet", href: styles },
  ...(cssBundleHref ? [{ rel: "stylesheet", href: cssBundleHref }] : []),
]
```

Copy

### That's it

You can now start adding components to your project.

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest add button

```

Copy

The command above will add the `Button` component to your project. You can then import it like this:

```
import { Button } from "~/components/ui/button"

export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

Copy

[React Router](/docs/installation/react-router)[Astro](/docs/installation/astro)

On This Page

* [Create project](#create-project)
* [Run the CLI](#run-the-cli)
* [Configure components.json](#configure-componentsjson)
* [App structure](#app-structure)
* [Install Tailwind CSS](#install-tailwind-css)
* [Add tailwind.css to your app](#add-tailwindcss-to-your-app)
* [That's it](#thats-it)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)