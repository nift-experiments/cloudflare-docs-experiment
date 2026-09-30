---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/
  description: API reference for RtkControlbar component (React Library)
  full_title: RtkControlbar · Cloudflare Realtime docs
  head_html: <title>RtkControlbar · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkControlbar component (React Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/index.md"><meta property="og:title" content="RtkControlbar · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkControlbar component (React Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/#page","headline":"RtkControlbar \u00b7 Cloudflare Realtime docs","description":"API reference for RtkControlbar component (React Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/
  schema: 1
---
<p>Controlbar component provides you with various designs as variants.</p>
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
<td><code>config</code></td>
<td><code>UIConfig1</code></td>
<td>❌</td>
<td><code>createDefaultConfig()</code></td>
<td>Config</td>
</tr>
<tr>
<td><code>disableRender</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to render the default UI</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon Pack</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting</td>
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
<tr>
<td><code>variant</code></td>
<td><code>'solid' | 'boxed'</code></td>
<td>✅</td>
<td>-</td>
<td>Variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkControlbar } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkControlbar /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkControlbar } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkControlbar&#10;      disableRender={true}&#10;      meeting={meeting}&#10;      size=&quot;md&quot;&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
