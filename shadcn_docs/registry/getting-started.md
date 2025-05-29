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