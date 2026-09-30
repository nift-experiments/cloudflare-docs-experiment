---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/
  description: API reference for RtkGrid component (React Native Library)
  full_title: RtkGrid · Cloudflare Realtime docs
  head_html: <title>RtkGrid · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkGrid component (React Native Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/index.md"><meta property="og:title" content="RtkGrid · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkGrid component (React Native Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/#page","headline":"RtkGrid \u00b7 Cloudflare Realtime docs","description":"API reference for RtkGrid component (React Native Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/react-native/rtkgrid/
  schema: 1
---
<p>The main participant grid that automatically switches between simple, mixed, spotlight, and livestream layouts based on meeting state.</p>
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
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit meeting instance</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>defaultConfig</code></td>
<td>UI configuration object</td>
</tr>
<tr>
<td><code>states</code></td>
<td><code>States</code></td>
<td>❌</td>
<td>-</td>
<td>UI state object</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td>-</td>
<td>i18n translation function</td>
</tr>
<tr>
<td><code>aspectRatio</code></td>
<td><code>string</code></td>
<td>❌</td>
<td><code>'3:4'</code></td>
<td>Aspect ratio for grid tiles</td>
</tr>
<tr>
<td><code>gap</code></td>
<td><code>number</code></td>
<td>❌</td>
<td><code>8</code></td>
<td>Gap between grid tiles in pixels</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td><code>'sm'</code></td>
<td>Size variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkGrid } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkGrid meeting={meeting} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkGrid } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkGrid meeting={meeting} aspectRatio=&quot;16:9&quot; gap={12} size=&quot;md&quot; /&gt;;&#10;}&#10;</code></pre>
