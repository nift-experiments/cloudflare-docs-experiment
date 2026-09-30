---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/
  description: API reference for RtkMeetingHeaderView component (iOS Library)
  full_title: RtkMeetingHeaderView · Cloudflare Realtime docs
  head_html: <title>RtkMeetingHeaderView · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkMeetingHeaderView component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/index.md"><meta property="og:title" content="RtkMeetingHeaderView · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkMeetingHeaderView component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/#page","headline":"RtkMeetingHeaderView \u00b7 Cloudflare Realtime docs","description":"API reference for RtkMeetingHeaderView component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-meeting-header-view/
  schema: 1
---
<p>Meeting header view that displays the meeting title, participant count, elapsed time clock, recording indicator, and camera switch button.</p>
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
<td>The RealtimeKit client instance for the active meeting</td>
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
<td><code>setContentTop(offset: CGFloat)</code></td>
<td><code>Void</code></td>
<td>Sets the top content offset for the header layout</td>
</tr>
<tr>
<td><code>refreshNextPreviousButtonState()</code></td>
<td><code>Void</code></td>
<td>Refreshes the enabled state of next and previous page buttons</td>
</tr>
<tr>
<td><code>setClicks(nextButton:previousButton:)</code></td>
<td><code>Void</code></td>
<td>Assigns tap handlers for the next and previous page buttons</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let headerView = RtkMeetingHeaderView(meeting: rtkClient)&#10;view.addSubview(headerView)&#10;</code></pre>
<h3 id="with-page-navigation">With page navigation</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let headerView = RtkMeetingHeaderView(meeting: rtkClient)&#10;headerView.setClicks(&#10;    nextButton: { print(&quot;Next page&quot;) },&#10;    previousButton: { print(&quot;Previous page&quot;) }&#10;)&#10;headerView.refreshNextPreviousButtonState()&#10;view.addSubview(headerView)&#10;</code></pre>
