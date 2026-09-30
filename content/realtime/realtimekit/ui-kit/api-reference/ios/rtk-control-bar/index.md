---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/
  description: API reference for RtkControlBar component (iOS Library)
  full_title: RtkControlBar · Cloudflare Realtime docs
  head_html: <title>RtkControlBar · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkControlBar component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/index.md"><meta property="og:title" content="RtkControlBar · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkControlBar component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/#page","headline":"RtkControlBar \u00b7 Cloudflare Realtime docs","description":"API reference for RtkControlBar component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/
  schema: 1
---
<p>Base control bar view with a More menu button and an End Call button.
Serves as the foundation for <code>RtkMeetingControlBar</code> and <code>RtkWebinarControlBar</code>.</p>
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
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit client instance</td>
</tr>
<tr>
<td><code>delegate</code></td>
<td><code>RtkTabBarDelegate?</code></td>
<td>✅</td>
<td>-</td>
<td>Delegate for handling tab bar interactions</td>
</tr>
<tr>
<td><code>presentingViewController</code></td>
<td><code>UIViewController</code></td>
<td>✅</td>
<td>-</td>
<td>View controller used for presenting modal screens</td>
</tr>
<tr>
<td><code>appearance</code></td>
<td><code>RtkControlBarAppearance</code></td>
<td>❌</td>
<td><code>RtkControlBarAppearanceModel()</code></td>
<td>Appearance configuration for the control bar</td>
</tr>
<tr>
<td><code>settingViewControllerCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the settings view controller dismisses</td>
</tr>
<tr>
<td><code>onLeaveMeetingCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Closure called when the participant leaves the meeting</td>
</tr>
</tbody>
</table>
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
<td><code>moreButton</code></td>
<td><code>RtkMoreButtonControlBar</code></td>
<td>-</td>
<td>-</td>
<td>The More menu button (read-only)</td>
</tr>
<tr>
<td><code>endCallButton</code></td>
<td><code>RtkEndMeetingControlBarButton</code></td>
<td>-</td>
<td>-</td>
<td>The End Call button</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let controlBar = RtkControlBar(&#10;    meeting: rtkClient,&#10;    delegate: self,&#10;    presentingViewController: self&#10;)&#10;view.addSubview(controlBar)&#10;</code></pre>
<h3 id="with-completion-handlers">With completion handlers</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let controlBar = RtkControlBar(&#10;    meeting: rtkClient,&#10;    delegate: self,&#10;    presentingViewController: self,&#10;    onLeaveMeetingCompletion: {&#10;        self.dismiss(animated: true)&#10;    }&#10;)&#10;view.addSubview(controlBar)&#10;</code></pre>
