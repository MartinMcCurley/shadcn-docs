# shadcn - shadcn/ui

Source: https://ui.shadcn.com/docs/cli

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

shadcn

# shadcn

Use the shadcn CLI to add components to your project.

## init

Use the `init` command to initialize configuration and dependencies for a new project.

The `init` command installs dependencies, adds the `cn` util and configures CSS variables for the project.

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest init

```

Copy

### Options

```
Usage: shadcn init [options] [components...]

initialize your project and install dependencies

Arguments:
  components         the components to add or a url to the component.

Options:
  -y, --yes           skip confirmation prompt. (default: true)
  -d, --defaults,     use default configuration. (default: false)
  -f, --force         force overwrite of existing configuration. (default: false)
  -c, --cwd <cwd>     the working directory. defaults to the current directory. (default: "/Users/shadcn/Desktop")
  -s, --silent        mute output. (default: false)
  --src-dir           use the src directory when creating a new project. (default: false)
  --no-src-dir        do not use the src directory when creating a new project.
  --css-variables     use css variables for theming. (default: true)
  --no-css-variables  do not use css variables for theming.
  -h, --help          display help for command
```

Copy

## add

Use the `add` command to add components and dependencies to your project.

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest add [component]

```

Copy

### Options

```
Usage: shadcn add [options] [components...]

add a component to your project

Arguments:
  components         the components to add or a url to the component.

Options:
  -y, --yes           skip confirmation prompt. (default: false)
  -o, --overwrite     overwrite existing files. (default: false)
  -c, --cwd <cwd>     the working directory. defaults to the current directory. (default: "/Users/shadcn/Desktop")
  -a, --all           add all available components (default: false)
  -p, --path <path>   the path to add the component to.
  -s, --silent        mute output. (default: false)
  --src-dir           use the src directory when creating a new project. (default: false)
  --no-src-dir        do not use the src directory when creating a new project.
  --css-variables     use css variables for theming. (default: true)
  --no-css-variables  do not use css variables for theming.
  -h, --help          display help for command
```

Copy

## build

Use the `build` command to generate the registry JSON files.

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest build

```

Copy

This command reads the `registry.json` file and generates the registry JSON files in the `public/r` directory.

### Options

```
Usage: shadcn build [options] [registry]

build components for a shadcn registry

Arguments:
  registry             path to registry.json file (default: "./registry.json")

Options:
  -o, --output <path>  destination directory for json files (default: "./public/r")
  -c, --cwd <cwd>      the working directory. defaults to the current directory. (default:
                       "/Users/shadcn/Code/shadcn/ui/packages/shadcn")
  -h, --help           display help for command
```

Copy

To customize the output directory, use the `--output` option.

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest build --output ./public/registry

```

Copy

[Dark mode](/docs/dark-mode)[Monorepo](/docs/monorepo)

On This Page

* [init](#init)
  + [Options](#options)
* [add](#add)
  + [Options](#options-1)
* [build](#build)
  + [Options](#options-2)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)