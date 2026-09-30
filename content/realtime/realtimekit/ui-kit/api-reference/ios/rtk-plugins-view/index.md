---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/
  description: API reference for RtkPluginsView component (iOS Library)
  full_title: RtkPluginsView · Cloudflare Realtime docs
  head_html: <title>RtkPluginsView · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkPluginsView component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/index.md"><meta property="og:title" content="RtkPluginsView · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkPluginsView component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/#page","headline":"RtkPluginsView \u00b7 Cloudflare Realtime docs","description":"API reference for RtkPluginsView component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-plugins-view/
  schema: 1
---
<p>A composite view for displaying plugins and screen share content.
Includes a tab selector, plugin content area, and a floating active speaker view.</p>
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
<td><code>videoPeerViewModel</code></td>
<td><code>VideoPeerViewModel</code></td>
<td>✅</td>
<td>-</td>
<td>The view model for the active speaker video</td>
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
<td><code>activeListView</code></td>
<td><code>RtkActiveTabSelectorView</code></td>
<td>-</td>
<td>-</td>
<td>The tab selector for switching between plugins and screen shares</td>
</tr>
<tr>
<td><code>pluginVideoView</code></td>
<td><code>UIView</code></td>
<td>-</td>
<td>-</td>
<td>The container view for plugin content</td>
</tr>
<tr>
<td><code>syncButton</code></td>
<td><code>UIButton</code></td>
<td>-</td>
<td>-</td>
<td>Button to sync the plugin view with the presenter</td>
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
<td><code>setButtons(buttons:selectedIndex:clickAction:)</code></td>
<td><code>Void</code></td>
<td>Configures the tab selector buttons with a selection handler</td>
</tr>
<tr>
<td><code>show(pluginView:)</code></td>
<td><code>Void</code></td>
<td>Displays a plugin view in the content area</td>
</tr>
<tr>
<td><code>showVideoView(participant:)</code></td>
<td><code>Void</code></td>
<td>Displays a participant's video in the content area</td>
</tr>
<tr>
<td><code>showPinnedView(participant:)</code></td>
<td><code>Void</code></td>
<td>Displays a pinned participant's video</td>
</tr>
<tr>
<td><code>showActiveSpeakerView(participant:)</code></td>
<td><code>Void</code></td>
<td>Shows the floating active speaker overlay</td>
</tr>
<tr>
<td><code>hideActiveSpeaker()</code></td>
<td><code>Void</code></td>
<td>Hides the floating active speaker overlay</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let viewModel = VideoPeerViewModel(&#10;    meeting: rtkClient,&#10;    participant: participant,&#10;    showSelfPreviewVideo: false&#10;)&#10;let pluginsView = RtkPluginsView(videoPeerViewModel: viewModel)&#10;view.addSubview(pluginsView)&#10;</code></pre>
<h3 id="with-tab-buttons">With tab buttons</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let viewModel = VideoPeerViewModel(&#10;    meeting: rtkClient,&#10;    participant: participant,&#10;    showSelfPreviewVideo: false&#10;)&#10;let pluginsView = RtkPluginsView(videoPeerViewModel: viewModel)&#10;&#10;let buttons = [&#10;    RtkPluginScreenShareTabButton(image: nil, title: &quot;Screen Share&quot;),&#10;    RtkPluginScreenShareTabButton(image: nil, title: &quot;Whiteboard&quot;)&#10;]&#10;pluginsView.setButtons(&#10;    buttons: buttons,&#10;    selectedIndex: 0,&#10;    clickAction: { index in&#10;        print(&quot;Selected tab: \(index)&quot;)&#10;    }&#10;)&#10;view.addSubview(pluginsView)&#10;</code></pre>
