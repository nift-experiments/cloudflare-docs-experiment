---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/
  description: API reference for RtkButton component (iOS Library)
  full_title: RtkButton · Cloudflare Realtime docs
  head_html: <title>RtkButton · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkButton component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/index.md"><meta property="og:title" content="RtkButton · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkButton component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/#page","headline":"RtkButton \u00b7 Cloudflare Realtime docs","description":"API reference for RtkButton component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/
  schema: 1
---
<p>A versatile button that follows the RTK Design System.
Supports multiple styles, states, and sizes.</p>
<h2 id="initializer-parameters">Initializer parameters</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>style</code></td>
<td><code>Style</code></td>
<td>❌</td>
<td><code>.solid</code></td>
<td>The button style (solid, line, icon-left, and others)</td>
</tr>
<tr>
<td><code>rtkButtonState</code></td>
<td><code>States</code></td>
<td>❌</td>
<td><code>.active</code></td>
<td>The initial state of the button</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>❌</td>
<td><code>.large</code></td>
<td>The size of the button</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkButtonAppearance</code></td>
<td>❌</td>
<td>-</td>
<td>Appearance configuration for colors and fonts</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let button = RtkButton()&#10;button.setTitle(&quot;Join&quot;, for: .normal)&#10;view.addSubview(button)&#10;</code></pre>
<h3 id="with-custom-style">With custom style</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let button = RtkButton(&#10;    style: .line,&#10;    rtkButtonState: .active,&#10;    size: .large&#10;)&#10;button.setTitle(&quot;Cancel&quot;, for: .normal)&#10;view.addSubview(button)&#10;</code></pre>
