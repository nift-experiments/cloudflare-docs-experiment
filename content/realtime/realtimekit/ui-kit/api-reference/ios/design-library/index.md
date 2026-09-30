---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/
  description: API reference for DesignLibrary component (iOS Library)
  full_title: DesignLibrary · Cloudflare Realtime docs
  head_html: <title>DesignLibrary · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for DesignLibrary component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/index.md"><meta property="og:title" content="DesignLibrary · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for DesignLibrary component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/#page","headline":"DesignLibrary \u00b7 Cloudflare Realtime docs","description":"API reference for DesignLibrary component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/design-library/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/design-library/
  schema: 1
---
<p>The central design token library providing color, spacing, border width, and border radius tokens.
Access through the <code>DesignLibrary.shared</code> singleton.</p>
<h2 id="access">Access</h2>
<pre tabindex="0"><code class="language-swift">let designLibrary = DesignLibrary.shared&#10;</code></pre>
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
<td><code>color</code></td>
<td><code>ColorTokens</code></td>
<td>-</td>
<td>-</td>
<td>Color tokens for backgrounds, text, and brand colors</td>
</tr>
<tr>
<td><code>space</code></td>
<td><code>SpaceToken</code></td>
<td>-</td>
<td>-</td>
<td>Spacing tokens for margins and padding</td>
</tr>
<tr>
<td><code>borderSize</code></td>
<td><code>BorderWidthToken</code></td>
<td>-</td>
<td>-</td>
<td>Border width tokens</td>
</tr>
<tr>
<td><code>borderRadius</code></td>
<td><code>BorderRadiusToken</code></td>
<td>-</td>
<td>-</td>
<td>Border radius tokens for corner rounding</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="access-design-tokens">Access design tokens</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let designLibrary = DesignLibrary.shared&#10;&#10;// Access color tokens&#10;let backgroundColor = designLibrary.color.background&#10;let textColor = designLibrary.color.text&#10;&#10;// Access spacing tokens&#10;let padding = designLibrary.space.space4&#10;&#10;// Access border tokens&#10;let borderWidth = designLibrary.borderSize.thin&#10;let cornerRadius = designLibrary.borderRadius.rounded&#10;</code></pre>
