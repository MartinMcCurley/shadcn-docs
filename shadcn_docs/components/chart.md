# Chart - shadcn/ui

Source: https://ui.shadcn.com/docs/components/chart

#### Getting Started

[Introduction](/docs)[Installation](/docs/installation)[components.json](/docs/components-json)[Theming](/docs/theming)[Dark mode](/docs/dark-mode)[CLI](/docs/cli)[Monorepo](/docs/monorepo)[Tailwind v4New](/docs/tailwind-v4)[Next.js 15 + React 19](/docs/react-19)[Typography](/docs/components/typography)[Open in v0](/docs/v0)[Blocks](/docs/blocks)[Figma](/docs/figma)[Changelog](/docs/changelog)

#### Installation

[Next.js](/docs/installation/next)[Vite](/docs/installation/vite)[Laravel](/docs/installation/laravel)[React Router](/docs/installation/react-router)[Remix](/docs/installation/remix)[Astro](/docs/installation/astro)[Tanstack Start](/docs/installation/tanstack)[Tanstack Router](/docs/installation/tanstack-router)[Manual](/docs/installation/manual)

#### Components

[Accordion](/docs/components/accordion)[Alert](/docs/components/alert)[Alert Dialog](/docs/components/alert-dialog)[Aspect Ratio](/docs/components/aspect-ratio)[Avatar](/docs/components/avatar)[Badge](/docs/components/badge)[Breadcrumb](/docs/components/breadcrumb)[Button](/docs/components/button)[Calendar](/docs/components/calendar)[Card](/docs/components/card)[Carousel](/docs/components/carousel)[Chart](/docs/components/chart)[Checkbox](/docs/components/checkbox)[Collapsible](/docs/components/collapsible)[Combobox](/docs/components/combobox)[Command](/docs/components/command)[Context Menu](/docs/components/context-menu)[Data Table](/docs/components/data-table)[Date Picker](/docs/components/date-picker)[Dialog](/docs/components/dialog)[Drawer](/docs/components/drawer)[Dropdown Menu](/docs/components/dropdown-menu)[Form](/docs/components/form)[Hover Card](/docs/components/hover-card)[Input](/docs/components/input)[Input OTP](/docs/components/input-otp)[Label](/docs/components/label)[Menubar](/docs/components/menubar)[Navigation Menu](/docs/components/navigation-menu)[Pagination](/docs/components/pagination)[Popover](/docs/components/popover)[Progress](/docs/components/progress)[Radio Group](/docs/components/radio-group)[Resizable](/docs/components/resizable)[Scroll Area](/docs/components/scroll-area)[Select](/docs/components/select)[Separator](/docs/components/separator)[Sheet](/docs/components/sheet)[Sidebar](/docs/components/sidebar)[Skeleton](/docs/components/skeleton)[Slider](/docs/components/slider)[Sonner](/docs/components/sonner)[Switch](/docs/components/switch)[Table](/docs/components/table)[Tabs](/docs/components/tabs)[Textarea](/docs/components/textarea)[Toast](/docs/components/toast)[Toggle](/docs/components/toggle)[Toggle Group](/docs/components/toggle-group)[Tooltip](/docs/components/tooltip)

#### Registry New

[Introduction](/docs/registry)[Getting Started](/docs/registry/getting-started)[Examples](/docs/registry/examples)[Open in v0](/docs/registry/open-in-v0)[FAQ](/docs/registry/faq)[registry.json](/docs/registry/registry-json)[registry-item.json](/docs/registry/registry-item-json)

[Docs](/docs)

Chart

# Chart

Beautiful charts. Built using Recharts. Copy and paste into your apps.

**Note:** If you are using charts with **React 19** or the **Next.js 15**, see the note [here](/docs/react-19#recharts).

Style:

Copy

Bar Chart - Interactive

Showing total visitors for the last 3 months

Desktop24,828Mobile25,010

Introducing **Charts**. A collection of chart components that you can copy and paste into your apps.

Charts are designed to look great out of the box. They work well with the other components and are fully customizable to fit your project.

[Browse the Charts Library](/charts).

## Component

We use [Recharts](https://recharts.org/) under the hood.

We designed the `chart` component with composition in mind. **You build your charts using Recharts components and only bring in custom components, such as `ChartTooltip`, when and where you need it**.

```
import { Bar, BarChart } from "recharts"

import { ChartContainer, ChartTooltipContent } from "@/components/ui/charts"

export function MyChart() {
  return (
    <ChartContainer>
      <BarChart data={data}>
        <Bar dataKey="value" />
        <ChartTooltip content={<ChartTooltipContent />} />
      </BarChart>
    </ChartContainer>
  )
}
```

Copy

We do not wrap Recharts. This means you're not locked into an abstraction. When a new Recharts version is released, you can follow the official upgrade path to upgrade your charts.

**The components are yours**.

## Installation

**Note:** If you are using charts with **React 19** or the **Next.js 15**, see the note [here](/docs/react-19#recharts).

CLIManual

### Run the following command to install `chart.tsx`

pnpmnpmyarnbun

```
pnpm dlx shadcn@latest add chart

```

Copy

### Add the following colors to your CSS file

```
@layer base {
  :root {
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
  }

  .dark {
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
    --chart-3: 30 80% 55%;
    --chart-4: 280 65% 60%;
    --chart-5: 340 75% 55%;
  }
}
```

Copy

## Your First Chart

Let's build your first chart. We'll build a bar chart, add a grid, axis, tooltip and legend.

### Start by defining your data

The following data represents the number of desktop and mobile users for each month.

**Note:** Your data can be in any shape. You are not limited to the shape of the data below. Use the `dataKey` prop to map your data to the chart.

```
const chartData = [
  { month: "January", desktop: 186, mobile: 80 },
  { month: "February", desktop: 305, mobile: 200 },
  { month: "March", desktop: 237, mobile: 120 },
  { month: "April", desktop: 73, mobile: 190 },
  { month: "May", desktop: 209, mobile: 130 },
  { month: "June", desktop: 214, mobile: 140 },
]
```

Copy

### Define your chart config

The chart config holds configuration for the chart. This is where you place human-readable strings, such as labels, icons and color tokens for theming.

```
import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
  mobile: {
    label: "Mobile",
    color: "#60a5fa",
  },
} satisfies ChartConfig
```

Copy

### Build your chart

You can now build your chart using Recharts components.

**Important:** Remember to set a `min-h-[VALUE]` on the `ChartContainer` component. This is required for the chart be responsive.

```
"use client"

import { Bar, BarChart } from "recharts"

import { ChartConfig, ChartContainer } from "@/components/ui/chart"

const chartData = [
  { month: "January", desktop: 186, mobile: 80 },
  { month: "February", desktop: 305, mobile: 200 },
  { month: "March", desktop: 237, mobile: 120 },
  { month: "April", desktop: 73, mobile: 190 },
  { month: "May", desktop: 209, mobile: 130 },
  { month: "June", desktop: 214, mobile: 140 },
]

const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
  mobile: {
    label: "Mobile",
    color: "#60a5fa",
  },
} satisfies ChartConfig

export function Component() {
  return (
    <ChartContainer config={chartConfig} className="min-h-[200px] w-full">
      <BarChart accessibilityLayer data={chartData}>
        <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
        <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
      </BarChart>
    </ChartContainer>
  )
}
```

Copy

Expand

PreviewCode

Style:

Copy

### Add a Grid

Let's add a grid to the chart.

### Import the `CartesianGrid` component.

```
import { Bar, BarChart, CartesianGrid } from "recharts"
```

Copy

### Add the `CartesianGrid` component to your chart.

```
<ChartContainer config={chartConfig} className="min-h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

Copy

PreviewCode

Style:

Copy

### Add an Axis

To add an x-axis to the chart, we'll use the `XAxis` component.

### Import the `XAxis` component.

```
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"
```

Copy

### Add the `XAxis` component to your chart.

```
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

Copy

PreviewCode

Style:

Copy

### Add Tooltip

So far we've only used components from Recharts. They look great out of the box thanks to some customization in the `chart` component.

To add a tooltip, we'll use the custom `ChartTooltip` and `ChartTooltipContent` components from `chart`.

### Import the `ChartTooltip` and `ChartTooltipContent` components.

```
import { ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
```

Copy

### Add the components to your chart.

```
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <ChartTooltip content={<ChartTooltipContent />} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

Copy

PreviewCode

Style:

Copy

Hover to see the tooltips. Easy, right? Two components, and we've got a beautiful tooltip.

### Add Legend

We'll do the same for the legend. We'll use the `ChartLegend` and `ChartLegendContent` components from `chart`.

### Import the `ChartLegend` and `ChartLegendContent` components.

```
import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"
```

Copy

### Add the components to your chart.

```
<ChartContainer config={chartConfig} className="h-[200px] w-full">
  <BarChart accessibilityLayer data={chartData}>
    <CartesianGrid vertical={false} />
    <XAxis
      dataKey="month"
      tickLine={false}
      tickMargin={10}
      axisLine={false}
      tickFormatter={(value) => value.slice(0, 3)}
    />
    <ChartTooltip content={<ChartTooltipContent />} />
    <ChartLegend content={<ChartLegendContent />} />
    <Bar dataKey="desktop" fill="var(--color-desktop)" radius={4} />
    <Bar dataKey="mobile" fill="var(--color-mobile)" radius={4} />
  </BarChart>
</ChartContainer>
```

Copy

PreviewCode

Style:

Copy

Done. You've built your first chart! What's next?

* [Themes and Colors](/docs/components/chart#theming)
* [Tooltip](/docs/components/chart#tooltip)
* [Legend](/docs/components/chart#legend)

## Chart Config

The chart config is where you define the labels, icons and colors for a chart.

It is intentionally decoupled from chart data.

This allows you to share config and color tokens between charts. It can also works independently for cases where your data or color tokens live remotely or in a different format.

```
import { Monitor } from "lucide-react"

import { type ChartConfig } from "@/components/ui/chart"

const chartConfig = {
  desktop: {
    label: "Desktop",
    icon: Monitor,
    // A color like 'hsl(220, 98%, 61%)' or 'var(--color-name)'
    color: "#2563eb",
    // OR a theme object with 'light' and 'dark' keys
    theme: {
      light: "#2563eb",
      dark: "#dc2626",
    },
  },
} satisfies ChartConfig
```

Copy

## Theming

Charts has built-in support for theming. You can use css variables (recommended) or color values in any color format, such as hex, hsl or oklch.

### CSS Variables

### Define your colors in your css file

globals.css

```
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 240 10% 3.9%;
    // ...
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
  }

  .dark: {
    --background: 240 10% 3.9%;
    --foreground: 0 0% 100%;
    // ...
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
  }
}
```

Copy

### Add the color to your `chartConfig`

```
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "hsl(var(--chart-1))",
  },
  mobile: {
    label: "Mobile",
    color: "hsl(var(--chart-2))",
  },
} satisfies ChartConfig
```

Copy

We're wrapping the value in `hsl()` here because we define the colors without color space function.

This is not required. You can use full color values, such as hex, hsl or oklch.

```
--chart-1: oklch(70% 0.227 154.59);
```

Copy

```
color: "var(--chart-1)",
```

Copy

### hex, hsl or oklch

You can also define your colors directly in the chart config. Use the color format you prefer.

```
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
} satisfies ChartConfig
```

Copy

### Using Colors

To use the theme colors in your chart, reference the colors using the format `var(--color-KEY)`.

#### Components

```
<Bar dataKey="desktop" fill="var(--color-desktop)" />
```

Copy

#### Chart Data

```
const chartData = [
  { browser: "chrome", visitors: 275, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]
```

Copy

#### Tailwind

```
<LabelList className="fill-[--color-desktop]" />
```

Copy

## Tooltip

A chart tooltip contains a label, name, indicator and value. You can use a combination of these to customize your tooltip.

Style:

Copy

Label

Page Views

Desktop

186

Mobile

80

Name

Chrome

1,286

Firefox

1,000

Page Views

Desktop

12,486

Indicator

Chrome

1,286

You can turn on/off any of these using the `hideLabel`, `hideIndicator` props and customize the indicator style using the `indicator` prop.

Use `labelKey` and `nameKey` to use a custom key for the tooltip label and name.

Chart comes with the `<ChartTooltip>` and `<ChartTooltipContent>` components. You can use these two components to add custom tooltips to your chart.

```
import { ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
```

Copy

```
<ChartTooltip content={<ChartTooltipContent />} />
```

Copy

### Props

Use the following props to customize the tooltip.

| Prop | Type | Description |
| --- | --- | --- |
| `labelKey` | string | The config or data key to use for the label. |
| `nameKey` | string | The config or data key to use for the name. |
| `indicator` | `dot` `line` or `dashed` | The indicator style for the tooltip. |
| `hideLabel` | boolean | Whether to hide the label. |
| `hideIndicator` | boolean | Whether to hide the indicator. |

### Colors

Colors are automatically referenced from the chart config.

### Custom

To use a custom key for tooltip label and names, use the `labelKey` and `nameKey` props.

```
const chartData = [
  { browser: "chrome", visitors: 187, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]

const chartConfig = {
  visitors: {
    label: "Total Visitors",
  },
  chrome: {
    label: "Chrome",
    color: "hsl(var(--chart-1))",
  },
  safari: {
    label: "Safari",
    color: "hsl(var(--chart-2))",
  },
} satisfies ChartConfig
```

Copy

```
<ChartTooltip
  content={<ChartTooltipContent labelKey="visitors" nameKey="browser" />}
/>
```

Copy

This will use `Total Visitors` for label and `Chrome` and `Safari` for the tooltip names.

## Legend

You can use the custom `<ChartLegend>` and `<ChartLegendContent>` components to add a legend to your chart.

```
import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"
```

Copy

```
<ChartLegend content={<ChartLegendContent />} />
```

Copy

### Colors

Colors are automatically referenced from the chart config.

### Custom

To use a custom key for legend names, use the `nameKey` prop.

```
const chartData = [
  { browser: "chrome", visitors: 187, fill: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, fill: "var(--color-safari)" },
]

const chartConfig = {
  chrome: {
    label: "Chrome",
    color: "hsl(var(--chart-1))",
  },
  safari: {
    label: "Safari",
    color: "hsl(var(--chart-2))",
  },
} satisfies ChartConfig
```

Copy

```
<ChartLegend content={<ChartLegendContent nameKey="browser" />} />
```

Copy

This will use `Chrome` and `Safari` for the legend names.

## Accessibility

You can turn on the `accessibilityLayer` prop to add an accessible layer to your chart.

This prop adds keyboard access and screen reader support to your charts.

```
<LineChart accessibilityLayer />
```

Copy

[Carousel](/docs/components/carousel)[Checkbox](/docs/components/checkbox)

On This Page

* [Component](#component)
* [Installation](#installation)
* [Your First Chart](#your-first-chart)
  + [Add a Grid](#add-a-grid)
  + [Add an Axis](#add-an-axis)
  + [Add Tooltip](#add-tooltip)
  + [Add Legend](#add-legend)
* [Chart Config](#chart-config)
* [Theming](#theming)
  + [CSS Variables](#css-variables)
  + [hex, hsl or oklch](#hex-hsl-or-oklch)
  + [Using Colors](#using-colors)
* [Tooltip](#tooltip)
  + [Props](#props)
  + [Colors](#colors)
  + [Custom](#custom)
* [Legend](#legend)
  + [Colors](#colors-1)
  + [Custom](#custom-1)
* [Accessibility](#accessibility)

Deploy your shadcn/ui app on Vercel

Trusted by OpenAI, Sonos, Chick-fil-A, and more.

Vercel provides tools and infrastructure to deploy apps and features at scale.

Deploy Now[Deploy to Vercel](https://vercel.com/new?utm_source=shadcn_site&utm_medium=web&utm_campaign=docs_cta_deploy_now_callout)