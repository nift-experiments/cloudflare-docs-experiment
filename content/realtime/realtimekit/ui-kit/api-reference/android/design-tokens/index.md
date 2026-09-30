---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/
  description: API reference for RtkDesignTokens component (Android Library)
  full_title: RtkDesignTokens · Cloudflare Realtime docs
  head_html: <title>RtkDesignTokens · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkDesignTokens component (Android Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/index.md"><meta property="og:title" content="RtkDesignTokens · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkDesignTokens component (Android Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/#page","headline":"RtkDesignTokens \u00b7 Cloudflare Realtime docs","description":"API reference for RtkDesignTokens component (Android Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/design-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/android/design-tokens/
  schema: 1
---
<p>The top-level design token container for customizing the look and feel of all UI Kit components.</p>
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
<td><code>colors</code></td>
<td><code>RtkColorTokens</code></td>
<td>❌</td>
<td>-</td>
<td>Color theme tokens</td>
</tr>
<tr>
<td><code>borderWidth</code></td>
<td><code>RtkBorderWidthToken</code></td>
<td>❌</td>
<td>-</td>
<td>Border width token</td>
</tr>
<tr>
<td><code>borderRadius</code></td>
<td><code>RtkBorderRadiusToken</code></td>
<td>❌</td>
<td>-</td>
<td>Border radius token</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-kotlin">val designTokens = RtkDesignTokens(&#10;    colors = RtkColorTokens(&#10;        brand = BrandColor(&#10;            shade300 = Color.parseColor(&quot;#497CFD&quot;),&#10;            shade400 = Color.parseColor(&quot;#356EFD&quot;),&#10;            shade500 = Color.parseColor(&quot;#2160FD&quot;),&#10;            shade600 = Color.parseColor(&quot;#0D52FD&quot;),&#10;            shade700 = Color.parseColor(&quot;#0046E5&quot;)&#10;        ),&#10;        background = BackgroundColor(&#10;            shade600 = Color.parseColor(&quot;#2C2C2C&quot;),&#10;            shade700 = Color.parseColor(&quot;#242424&quot;),&#10;            shade800 = Color.parseColor(&quot;#1C1C1C&quot;),&#10;            shade900 = Color.parseColor(&quot;#141414&quot;),&#10;            shade1000 = Color.parseColor(&quot;#0C0C0C&quot;)&#10;        )&#10;    ),&#10;    borderRadius = RtkBorderRadiusToken.Rounded,&#10;    borderWidth = RtkBorderWidthToken.Thin&#10;)&#10;</code></pre>
