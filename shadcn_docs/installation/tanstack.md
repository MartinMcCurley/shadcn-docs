# TanStack Start - shadcn/ui

Source: https://ui.shadcn.com/docs/installation/tanstack

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

TanStack Start

# TanStack Start

Install and configure shadcn/ui for TanStack Start.

### Create project

Start by creating a new TanStack Start project by following the [Build a Project from Scratch](https://tanstack.com/start/latest/docs/framework/react/build-from-scratch) guide on the TanStack Start website.

**Do not add Tailwind yet. We'll install Tailwind v4 in the next step.**

### Add Tailwind

Install `tailwindcss` and its dependencies.

pnpmnpmyarnbun

```
pnpm add tailwindcss @tailwindcss/postcss postcss

```

Copy

### Create postcss.config.ts

Create a `postcss.config.ts` file at the root of your project.

postcss.config.ts

```
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
}
```

Copy

### Create `app/styles/app.css`

Create an `app.css` file in the `app/styles` directory and import `tailwindcss`

app/styles/app.css

```
@import "tailwindcss" source("../");
```

Copy

### Import `app.css`

app/routes/\_\_root.tsx

```
import type { ReactNode } from "react"
import { Outlet, createRootRoute } from "@tanstack/react-router"
import { Meta, Scripts } from "@tanstack/start"

import appCss from "@/styles/app.css?url"

export const Route = createRootRoute({
  head: () => ({
    meta: [
      {
        charSet: "utf-8",
      },
      {
        name: "viewport",
        content: "width=device-width, initial-scale=1",
      },
      {
        title: "TanStack Start Starter",
      },
    ],
    links: [
      {
        rel: "stylesheet",
        href: appCss,
      },
    ],
  }),
  component: RootComponent,
})
```

Copy

### Edit tsconfig.json file

Add the following code to the `tsconfig.json` file to resolve paths.

tsconfig.json

```
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "moduleResolution": "Bundler",
    "module": "ESNext",
    "target": "ES2022",
    "skipLibCheck": true,
    "strictNullChecks": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./app/*"]
    }
  }
}
```

Copy

### Run the CLI

Run the `shadcn` init command to setup your project:

pnpmnpmyarnbun

```
pnpm dlx shadcn@canary init

```

Copy

This will create a `components.json` file in the root of your project and configure CSS variables inside `app/styles/app.css`.

### That's it

You can now start adding components to your project.

pnpmnpmyarnbun

```
pnpm dlx shadcn@canary add button

```

Copy

The command above will add the `Button` component to your project. You can then import it like this:

app/routes/index.tsx

```
import { Button } from "@/components/ui/button"

function Home() {
  const router = useRouter()
  const state = Route.useLoaderData()

  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

Copy

[Astro](/docs/installation/astro)[Tanstack Router](/docs/installation/tanstack-router)

On This Page

* [Create project](#create-project)
* [Add Tailwind](#add-tailwind)
* [Create postcss.config.ts](#create-postcssconfigts)
* [Create app/styles/app.css](#create-appstylesappcss)
* [Import app.css](#import-appcss)
* [Edit tsconfig.json file](#edit-tsconfigjson-file)
* [Run the CLI](#run-the-cli)
* [That's it](#thats-it)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)