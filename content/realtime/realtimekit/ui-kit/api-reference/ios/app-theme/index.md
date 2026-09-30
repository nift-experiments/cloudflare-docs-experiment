---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/
  description: API reference for AppTheme component (iOS Library)
  full_title: AppTheme · Cloudflare Realtime docs
  head_html: <title>AppTheme · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for AppTheme component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/index.md"><meta property="og:title" content="AppTheme · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for AppTheme component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/#page","headline":"AppTheme \u00b7 Cloudflare Realtime docs","description":"API reference for AppTheme component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/app-theme/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/app-theme/
  schema: 1
---
<p>The application theme singleton that provides pre-configured appearance objects for UI components.
Use <code>AppTheme.shared</code> to access default appearances or call <code>setUp(theme:)</code> to apply a custom theme.</p>
<h2 id="access">Access</h2>
<pre tabindex="0"><code class="language-swift">let theme = AppTheme.shared&#10;</code></pre>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Return Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>setUp(theme: AppThemeProtocol)</code></td>
<td><code>Void</code></td>
<td>Applies a custom theme conforming to <code>AppThemeProtocol</code></td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="access-default-theme">Access default theme</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let theme = AppTheme.shared&#10;let titleAppearance = theme.meetingTitleAppearance&#10;let clockAppearance = theme.clockViewAppearance&#10;</code></pre>
<h3 id="apply-a-custom-theme">Apply a custom theme</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;class CustomTheme: AppThemeProtocol {&#10;    // Implement required appearance properties&#10;}&#10;&#10;let customTheme = CustomTheme()&#10;AppTheme.shared.setUp(theme: customTheme)&#10;</code></pre>
