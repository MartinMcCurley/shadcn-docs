# Scroll-area - shadcn/ui

Source: https://ui.shadcn.com/docs/components/scroll-area

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Scroll-area

# Scroll-area

Augments native scroll functionality for custom, cross-browser styling.

[Docs](https://www.radix-ui.com/docs/primitives/components/scroll-area)[API Reference](https://www.radix-ui.com/docs/primitives/components/scroll-area#api-reference)

PreviewCode

Style:

Open in Copy

#### Tags

v1.2.0-beta.50

v1.2.0-beta.49

v1.2.0-beta.48

v1.2.0-beta.47

v1.2.0-beta.46

v1.2.0-beta.45

v1.2.0-beta.44

v1.2.0-beta.43

v1.2.0-beta.42

v1.2.0-beta.41

v1.2.0-beta.40

v1.2.0-beta.39

v1.2.0-beta.38

v1.2.0-beta.37

v1.2.0-beta.36

v1.2.0-beta.35

v1.2.0-beta.34

v1.2.0-beta.33

v1.2.0-beta.32

v1.2.0-beta.31

v1.2.0-beta.30

v1.2.0-beta.29

v1.2.0-beta.28

v1.2.0-beta.27

v1.2.0-beta.26

v1.2.0-beta.25

v1.2.0-beta.24

v1.2.0-beta.23

v1.2.0-beta.22

v1.2.0-beta.21

v1.2.0-beta.20

v1.2.0-beta.19

v1.2.0-beta.18

v1.2.0-beta.17

v1.2.0-beta.16

v1.2.0-beta.15

v1.2.0-beta.14

v1.2.0-beta.13

v1.2.0-beta.12

v1.2.0-beta.11

v1.2.0-beta.10

v1.2.0-beta.9

v1.2.0-beta.8

v1.2.0-beta.7

v1.2.0-beta.6

v1.2.0-beta.5

v1.2.0-beta.4

v1.2.0-beta.3

v1.2.0-beta.2

v1.2.0-beta.1

## Installation

CLIManual

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest add scroll-area

```

Copy

## Usage

```
import { ScrollArea } from "@/components/ui/scroll-area"
```

Copy

```
<ScrollArea className="h-[200px] w-[350px] rounded-md border p-4">
  Jokester began sneaking into the castle in the middle of the night and leaving
  jokes all over the place: under the king's pillow, in his soup, even in the
  royal toilet. The king was furious, but he couldn't seem to stop Jokester. And
  then, one day, the people of the kingdom discovered that the jokes left by
  Jokester were so funny that they couldn't help but laugh. And once they
  started laughing, they couldn't stop.
</ScrollArea>
```

Copy

## Examples

### Horizontal Scrolling

PreviewCode

Style:

Copy

![Photo by Ornella Binni](/_next/image?url=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1465869185982-5a1a7522cbcb%3Fauto%3Dformat%26fit%3Dcrop%26w%3D300%26q%3D80&w=640&q=75)

Photo by Ornella Binni

![Photo by Tom Byrom](/_next/image?url=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1548516173-3cabfa4607e9%3Fauto%3Dformat%26fit%3Dcrop%26w%3D300%26q%3D80&w=640&q=75)

Photo by Tom Byrom

![Photo by Vladimir Malyavko](/_next/image?url=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1494337480532-3725c85fd2ab%3Fauto%3Dformat%26fit%3Dcrop%26w%3D300%26q%3D80&w=640&q=75)

Photo by Vladimir Malyavko

[Resizable](/docs/components/resizable)[Select](/docs/components/select)

On This Page

* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
  + [Horizontal Scrolling](#horizontal-scrolling)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)