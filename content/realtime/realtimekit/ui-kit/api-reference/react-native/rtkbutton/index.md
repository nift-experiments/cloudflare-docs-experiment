---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/
  description: API reference for RtkButton component (React Native Library)
  full_title: RtkButton · Cloudflare Realtime docs
  head_html: <title>RtkButton · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkButton component (React Native Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/index.md"><meta property="og:title" content="RtkButton · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkButton component (React Native Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/#page","headline":"RtkButton \u00b7 Cloudflare Realtime docs","description":"API reference for RtkButton component (React Native Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/react-native/rtkbutton/
  schema: 1
---
<p>A general-purpose button component with multiple variants and sizes.</p>
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
<td><code>children</code></td>
<td><code>ReactNode</code></td>
<td>❌</td>
<td>-</td>
<td>Button content/label</td>
</tr>
<tr>
<td><code>onClick</code></td>
<td><code>any</code></td>
<td>✅</td>
<td>-</td>
<td>Press handler callback</td>
</tr>
<tr>
<td><code>kind</code></td>
<td><code>'button' | 'icon' | 'wide'</code></td>
<td>❌</td>
<td><code>'button'</code></td>
<td>Button kind</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>'danger' | 'ghost' | 'primary' | 'secondary'</code></td>
<td>❌</td>
<td>-</td>
<td>Visual style variant</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td>-</td>
<td>Button size</td>
</tr>
<tr>
<td><code>reverse</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Reverse the button content order</td>
</tr>
<tr>
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td>-</td>
<td>Whether the button is disabled</td>
</tr>
<tr>
<td><code>style</code></td>
<td><code>StyleProp&lt;any&gt;</code></td>
<td>❌</td>
<td>-</td>
<td>Custom React Native styles</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkButton } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkButton onClick={() =&gt; console.log(&quot;pressed&quot;)}&gt;Press Me&lt;/RtkButton&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre tabindex="0"><code class="language-tsx">import { RtkButton } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkButton&#10;			onClick={() =&gt; console.log(&quot;pressed&quot;)}&#10;			variant=&quot;primary&quot;&#10;			size=&quot;md&quot;&#10;			kind=&quot;wide&quot;&#10;		&gt;&#10;			Join Meeting&#10;		&lt;/RtkButton&gt;&#10;	);&#10;}&#10;</code></pre>
