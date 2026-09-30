---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/
  description: API reference for RtkMoreMenu component (iOS Library)
  full_title: RtkMoreMenu · Cloudflare Realtime docs
  head_html: <title>RtkMoreMenu · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkMoreMenu component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/index.md"><meta property="og:title" content="RtkMoreMenu · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkMoreMenu component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/#page","headline":"RtkMoreMenu \u00b7 Cloudflare Realtime docs","description":"API reference for RtkMoreMenu component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-menu/
  schema: 1
---
<p>A bottom sheet menu that displays meeting action options such as chat, polls, and participant list.</p>
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
<td><code>title</code></td>
<td><code>String?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Optional title displayed at the top of the menu</td>
</tr>
<tr>
<td><code>features</code></td>
<td><code>[MenuType]</code></td>
<td>✅</td>
<td>-</td>
<td>Array of menu items to display</td>
</tr>
<tr>
<td><code>onSelect</code></td>
<td><code>@escaping (MenuType) -&gt; Void</code></td>
<td>✅</td>
<td>-</td>
<td>Closure called when the user selects a menu item</td>
</tr>
</tbody>
</table>
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
<td><code>show(on:)</code></td>
<td><code>Void</code></td>
<td>Presents the menu as a bottom sheet on the specified <code>UIView</code></td>
</tr>
<tr>
<td><code>reload(title:features:)</code></td>
<td><code>Void</code></td>
<td>Reloads the menu with a new title and set of features</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let menu = RtkMoreMenu(&#10;    features: [.chat, .polls, .participants],&#10;    onSelect: { menuType in&#10;        print(&quot;Selected: \(menuType)&quot;)&#10;    }&#10;)&#10;menu.show(on: self.view)&#10;</code></pre>
<h3 id="with-title">With title</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let menu = RtkMoreMenu(&#10;    title: &quot;More Options&quot;,&#10;    features: [.chat, .polls, .participants],&#10;    onSelect: { menuType in&#10;        switch menuType {&#10;        case .chat:&#10;            print(&quot;Open chat&quot;)&#10;        case .polls:&#10;            print(&quot;Open polls&quot;)&#10;        case .participants:&#10;            print(&quot;Open participants&quot;)&#10;        default:&#10;            break&#10;        }&#10;    }&#10;)&#10;menu.show(on: self.view)&#10;</code></pre>
