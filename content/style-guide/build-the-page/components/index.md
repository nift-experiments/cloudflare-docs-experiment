---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/
  description: Browse available MDX components for Cloudflare docs.
  full_title: Components · Cloudflare Style Guide
  head_html: <title>Components · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Browse available MDX components for Cloudflare docs."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/index.md"><meta property="og:title" content="Components · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Browse available MDX components for Cloudflare docs."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/#page","headline":"Components \u00b7 Cloudflare Style Guide","description":"Browse available MDX components for Cloudflare docs.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/
  schema: 1
---
<p>When you are <a href="/style-guide/contributions/">contributing to the Cloudflare Docs</a>, you can use our custom components to add additional formatting, such as buttons, tabs, and collapsible sections.</p>
<p>This guide shows you the basics of importing and adding a component to a page. Refer to each component page in this Style Guide to learn the specific props and requirements for each.</p>
<p>Our components are based on <a href="https://docs.astro.build/en/basics/astro-components/">Astro components</a> and are written in <a href="https://docs.astro.build/en/guides/markdown-content/">MDX</a>, an extended version of Markdown. <a href="/style-guide/how-we-docs/our-site/#site-framework">Learn more about the Cloudflare Docs framework</a>.</p>
<h2 id="add-a-component-to-a-page">Add a component to a page</h2>
<p>To add a component to a page:</p>
<ol>
<li>Import the component to the page by adding this text directly below the <a href="/style-guide/build-the-page/frontmatter/">frontmatter</a>:</li>
</ol>
<pre tabindex="0"><code class="language-mdx">import { COMPONENT_NAME } from &quot;~/components&quot;;&#10;&#10;;&#10;</code></pre>
<p>For example, if you were to add <a href="/style-guide/build-the-page/components/dash-button/">the <code>DashButton</code> component</a> to the <a href="/images/get-started/">Images getting started page</a>, the top of the MDX file corresponding to that page would look like the following:</p>
<pre tabindex="0"><code class="language-mdx">&#45;--&#10;pcx_content_type: get-started&#10;title: Getting started&#10; products:&#10;   &#45; images&#10;sidebar:&#10;  order: 2&#10;&#45;--&#10;&#10;import { DashButton } from &quot;~/components&quot;;&#10;&#10;;&#10;</code></pre>
<p>Page-specific wrapper components or one-off components do not need to be added to the barrel — import them via a deep path:</p>
<pre tabindex="0"><code class="language-mdx">import BaseSchemaProperties from &quot;~/components/BaseSchemaProperties.astro&quot;;&#10;</code></pre>
<ol start="2">
<li>Add the component to the page by adding this text anywhere on the page you want the component to appear:</li>
</ol>
<pre tabindex="0"><code class="language-mdx">&lt;COMPONENT_NAME PROP_NAME=&quot;PROP_VALUE&quot; /&gt;&#10;</code></pre>
<p>For example, if you were to add the <code>DashButton</code> component to some steps in the <a href="/images/get-started/">Images getting started page</a>, here is how the MDX file would look:</p>
<pre tabindex="0"><code class="language-mdx">1. In the Cloudflare dashboard, go to the **Transformations** page.&#10;&#10;   &lt;DashButton url=&quot;/?to=/:account/images/transformations&quot; /&gt;&#10;&#10;2. Go to the specific zone where you want to enable transformations.&#10;</code></pre>
<details class="nb-details"><summary>This is how this example would display after it is published:</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14639.md")
</div></details>
<h2 id="choose-the-right-component">Choose the right component</h2>
<p>To choose the right component for your use case, browse this table which contains our most commonly used components and a visual example of each. For full documentation on all available components and their use cases, browse the individual component pages in this Style Guide.</p>
<table>
<thead>
<tr>
<th align="left">Component</th>
<th align="left">Description &amp; visual example</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="/style-guide/build-the-page/components/api-request/"><code>APIRequest</code></a></td>
<td align="left"><p>Styled API request block. Generate executable cURL API commands with the required API token permissions.</p> <span class="nb-example"><h3 class="nb-component-title" id="example">Example</h3></td>
</tr>
</tbody>
</table>
@markup("md", "content/.markup/bodies/14640.md")
</div>                                                                                                                    |
| [`Badge`](/style-guide/build-the-page/components/badges/)                              | <p>Small descriptive pill. Label content with status, version, category, or other short metadata.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/14641.md")
</div>                                                                                                                                       |
| [`DashButton`](/style-guide/build-the-page/components/dash-button/)                    | <p>Dashboard deep-link button. Directly link users from documentation into a specific, relevant section of the Cloudflare Dashboard.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/14642.md")
</div>                                                                                        |
| [`Details`](/style-guide/build-the-page/components/details/)                           | <p>Click-to-expand content block. Hide non-essential, complex, or advanced technical content, allowing users to expand the section when needed.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/14643.md")
</div>                                                                                               |
| [`DirectoryListing`](/style-guide/build-the-page/components/directory-listing)         | <p>Auto-generated sub-page list. Automatically generate a navigable list of links to sub-pages within a specified documentation folder path.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-4">Example</h3>
@markup("md", "content/.markup/bodies/14644.md")
</div>                                                                      |
| [`Feature`](/style-guide/build-the-page/components/feature/)                           | <p>Product feature list item. Highlight a product feature with a description and a direct link button.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-5">Example</h3>
@markup("md", "content/.markup/bodies/14645.md")
</div>                                                                                                                              |
| [`GlossaryTooltip`](/style-guide/build-the-page/components/glossary-tooltip/)          | <p>Hover-activated glossary popup. Provide non-disruptive, hover-activated definitions for technical terms pulled from the documentation glossary.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-6">Example</h3>
@markup("md", "content/.markup/bodies/14646.md")
</div>                                                                           |
| [`LinkCard`](/style-guide/build-the-page/components/link-cards/)                       | <p>Navigational cards. Present related tutorials, concepts, or guides in a visually engaging format.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-7">Example</h3>
@markup("md", "content/.markup/bodies/14647.md")
</div>                                                                                                                              |
| [`PackageManagers`](/style-guide/build-the-page/components/package-managers)           | <p>Command switcher tabs. Display equivalent installation or execution commands for different package managers.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-8">Example</h3>
@markup("md", "content/.markup/bodies/14648.md")
</div>                                                                                                    |
| [`Plan`](/style-guide/build-the-page/components/plan/)                                 | <p>Product plan availability badge. Show the plan required for a product or specific feature.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-9">Example</h3>
@markup("md", "content/.markup/bodies/14649.md")
</div>                                                                                                                                             |
| [`RelatedProduct`](/style-guide/build-the-page/components/related-product/)            | <p>Formatted product reference. Visually highlight and link to a specific, complementary Cloudflare product, also featuring the product's logo.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-10">Example</h3>
@markup("md", "content/.markup/bodies/14650.md")
</div>                                                                       |
| [`ResourcesBySelector`](/style-guide/build-the-page/components/resources-by-selector/) | <p>Filterable code example library. Pull and display lists of code examples and resources based on content type or products.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-11">Example</h3>
@markup("md", "content/.markup/bodies/14651.md")
</div>                                                                                |
| [`Stream`](/style-guide/build-the-page/components/stream/)                             | <p>Embeddable video player. Display a video player optimized for Cloudflare Stream.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-12">Example</h3>
@markup("md", "content/.markup/bodies/14652.md")
</div>                                                                                                                                                             |
| [`Tabs` and `TabItem`](/style-guide/build-the-page/components/tabs/)                   | <p>Switchable content tabs. Allow easy switching between content views for different code languages or configuration methods.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-13">Example</h3>
@markup("md", "content/.markup/bodies/14653.md")
</div>                                                                                                                       |
| [`Type` and `MetaInfo`](/style-guide/build-the-page/components/type-highlighting/)     | <p>Pill-shaped data type badge and metadata annotation about a field or property. `Type` indicates API parameter data types (`String`, `Integer`) and `MetaInfo` indicates metadata constraints (`Required`, `Optional`, `Read-only`).</p> <div class="nb-example"><h3 class="nb-component-title" id="example-14">Example</h3>
@markup("md", "content/.markup/bodies/14654.md")
</div> |
| [`WranglerConfig`](/style-guide/build-the-page/components/wrangler-config/)            | <p>Tabbed Wrangler config display. Show Wrangler configuration files (JSONC and TOML) and bindings with automatic format switching.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-15">Example</h3>
@markup("md", "content/.markup/bodies/14655.md")
</div>                                                                                             |
| [`YouTube`](/style-guide/build-the-page/components/youtube/)                           | <p>Embeddable video player. Embeds a YouTube video player with a specified video ID.</p> <div class="nb-example"><h3 class="nb-component-title" id="example-16">Example</h3>
@markup("md", "content/.markup/bodies/14656.md")
</div>                                                                                                                                                          |
