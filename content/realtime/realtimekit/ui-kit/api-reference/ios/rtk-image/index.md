---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/
  description: API reference for RtkImage component (iOS Library)
  full_title: RtkImage · Cloudflare Realtime docs
  head_html: <title>RtkImage · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkImage component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/index.md"><meta property="og:title" content="RtkImage · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkImage component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/#page","headline":"RtkImage \u00b7 Cloudflare Realtime docs","description":"API reference for RtkImage component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/
  schema: 1
---
<p>A struct that wraps a <code>UIImage</code> or a <code>URL</code> for image content.
Used throughout the UI Kit for icons, avatars, and custom images.</p>
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
<td><code>image</code></td>
<td><code>UIImage?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>A local UIImage to display</td>
</tr>
<tr>
<td><code>url</code></td>
<td><code>URL?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>A remote URL to load the image from</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="with-a-local-image">With a local image</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let rtkImage = RtkImage(image: UIImage(systemName: &quot;mic&quot;))&#10;</code></pre>
<h3 id="with-a-remote-url">With a remote URL</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let rtkImage = RtkImage(url: URL(string: &quot;https://example.com/avatar.png&quot;))&#10;</code></pre>
