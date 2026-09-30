---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/
  description: API reference for RtkScreenshareView component (React Native Library)
  full_title: RtkScreenshareView · Cloudflare Realtime docs
  head_html: <title>RtkScreenshareView · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkScreenshareView component (React Native Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/index.md"><meta property="og:title" content="RtkScreenshareView · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkScreenshareView component (React Native Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/#page","headline":"RtkScreenshareView \u00b7 Cloudflare Realtime docs","description":"API reference for RtkScreenshareView component (React Native Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/react-native/rtkscreenshareview/
  schema: 1
---
<p>Renders a participant's screen share with fullscreen toggle, name tag, and audio indicator.</p>
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
<td><code>participant</code></td>
<td><code>RTKParticipant</code></td>
<td>✅</td>
<td>-</td>
<td>The participant sharing their screen</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit meeting instance</td>
</tr>
<tr>
<td><code>hideFullScreenButton</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Hide the fullscreen toggle button</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
<tr>
<td><code>nameTagPosition</code></td>
<td><code>'bottom-center' | 'bottom-left' | 'bottom-right' | 'top-center' | 'top-left' | 'top-right'</code></td>
<td>❌</td>
<td><code>'bottom-left'</code></td>
<td>Position of the name tag overlay</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td><code>'sm'</code></td>
<td>Size variant</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>'gradient' | 'solid'</code></td>
<td>❌</td>
<td><code>'solid'</code></td>
<td>Visual style variant</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td>-</td>
<td>i18n translation function</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkScreenshareView } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkScreenshareView participant={participant} meeting={meeting} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkScreenshareView } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkScreenshareView&#10;			participant={participant}&#10;			meeting={meeting}&#10;			nameTagPosition=&quot;bottom-left&quot;&#10;			variant=&quot;solid&quot;&#10;			size=&quot;md&quot;&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
