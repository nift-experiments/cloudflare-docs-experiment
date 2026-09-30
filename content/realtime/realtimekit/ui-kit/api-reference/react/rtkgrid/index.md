---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/
  description: API reference for RtkGrid component (React Library)
  full_title: RtkGrid · Cloudflare Realtime docs
  head_html: <title>RtkGrid · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkGrid component (React Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/index.md"><meta property="og:title" content="RtkGrid · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkGrid component (React Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/#page","headline":"RtkGrid \u00b7 Cloudflare Realtime docs","description":"API reference for RtkGrid component (React Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/react/rtkgrid/
  schema: 1
---
<p>The main grid component which abstracts all the grid handling logic and renders it for you.</p>
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
<td><code>aspectRatio</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>The aspect ratio of each participant</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>createDefaultConfig()</code></td>
<td>Config object</td>
</tr>
<tr>
<td><code>gap</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Gap between participants</td>
</tr>
<tr>
<td><code>gridSize</code></td>
<td><code>GridSize</code></td>
<td>✅</td>
<td>-</td>
<td>Grid size</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>layout</code></td>
<td><code>GridLayout</code></td>
<td>✅</td>
<td>-</td>
<td>Grid Layout</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting object</td>
</tr>
<tr>
<td><code>overrides</code></td>
<td><code>any</code></td>
<td>✅</td>
<td>-</td>
<td>@deprecated</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>states</code></td>
<td><code>States</code></td>
<td>✅</td>
<td>-</td>
<td>States</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkGrid } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkGrid /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkGrid } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkGrid&#10;      aspectRatio=&quot;example&quot;&#10;      gap={42}&#10;      gridSize=&quot;md&quot;&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
