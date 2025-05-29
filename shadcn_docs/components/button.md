# Button - shadcn/ui

Source: https://ui.shadcn.com/docs/components/button

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Button

# Button

Displays a button or a component that looks like a button.

PreviewCode

Style:

Open in Copy

Button

## Installation

CLIManual

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest add button

```

Copy

## Usage

```
import { Button } from "@/components/ui/button"
```

Copy

```
<Button variant="outline">Button</Button>
```

Copy

## Link

You can use the `buttonVariants` helper to create a link that looks like a button.

```
import { buttonVariants } from "@/components/ui/button"
```

Copy

```
<Link className={buttonVariants({ variant: "outline" })}>Click here</Link>
```

Copy

Alternatively, you can set the `asChild` parameter and nest the link component.

```
<Button asChild>
  <Link href="/login">Login</Link>
</Button>
```

Copy

## Examples

### Primary

PreviewCode

Style:

Open in Copy

Button

### Secondary

PreviewCode

Style:

Open in Copy

Secondary

### Destructive

PreviewCode

Style:

Open in Copy

Destructive

### Outline

PreviewCode

Style:

Open in Copy

Outline

### Ghost

PreviewCode

Style:

Open in Copy

Ghost

### Link

PreviewCode

Style:

Open in Copy

Link

### Icon

PreviewCode

Style:

Open in Copy

### With Icon

PreviewCode

Style:

Open in Copy

Login with Email

### Loading

PreviewCode

Style:

Open in Copy

Please wait

### As Child

PreviewCode

Style:

Open in Copy

[Login](/login)

## Changelog

### 2024-10-16 Classes for icons

Added `gap-2 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0` to the button to automatically style icon inside the button.

Add the following classes to the `cva` call in your `button.tsx` file.

button.tsx

```
const buttonVariants = cva(
  "inline-flex ... gap-2 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0"
)
```

Copy

[Breadcrumb](/docs/components/breadcrumb)[Calendar](/docs/components/calendar)

On This Page

* [Installation](#installation)
* [Usage](#usage)
* [Link](#link)
* [Examples](#examples)
  + [Primary](#primary)
  + [Secondary](#secondary)
  + [Destructive](#destructive)
  + [Outline](#outline)
  + [Ghost](#ghost)
  + [Link](#link-1)
  + [Icon](#icon)
  + [With Icon](#with-icon)
  + [Loading](#loading)
  + [As Child](#as-child)
* [Changelog](#changelog)
  + [2024-10-16 Classes for icons](#2024-10-16-classes-for-icons)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)