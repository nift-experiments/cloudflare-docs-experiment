---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/
  description: API reference for rtk-tooltip component (Web Components (HTML) Library)
  full_title: rtk-tooltip · Cloudflare Realtime docs
  head_html: <title>rtk-tooltip · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for rtk-tooltip component (Web Components (HTML) Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/index.md"><meta property="og:title" content="rtk-tooltip · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for rtk-tooltip component (Web Components (HTML) Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/#page","headline":"rtk-tooltip \u00b7 Cloudflare Realtime docs","description":"API reference for rtk-tooltip component (Web Components (HTML) Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/core/rtk-tooltip/
  schema: 1
---
<p>Tooltip component which follows RTK Design System.</p>
<h2 id="properties">Properties</h2>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>delay</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Delay before showing the tooltip</td>
</tr>
<tr>
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Disabled</td>
</tr>
<tr>
<td><code>kind</code></td>
<td><code>TooltipKind</code></td>
<td>✅</td>
<td>-</td>
<td>Tooltip kind</td>
</tr>
<tr>
<td><code>label</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Tooltip label</td>
</tr>
<tr>
<td><code>open</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Open</td>
</tr>
<tr>
<td><code>placement</code></td>
<td><code>Placement</code></td>
<td>✅</td>
<td>-</td>
<td>Placement of menu</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>TooltipVariant</code></td>
<td>✅</td>
<td>-</td>
<td>Tooltip variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-html">&lt;rtk-tooltip&gt;&lt;/rtk-tooltip&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-html">&lt;rtk-tooltip&gt;&#10;&lt;/rtk-tooltip&gt;&#10;</code></pre>
<pre tabindex="0"><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-tooltip&quot;);&#10;&#10;  el.delay= 42;&#10;  el.disabled= true;&#10;&lt;/script&gt;&#10;</code></pre>
