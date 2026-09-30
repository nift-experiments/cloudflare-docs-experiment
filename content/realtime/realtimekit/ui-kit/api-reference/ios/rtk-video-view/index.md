---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/
  description: API reference for RtkVideoView component (iOS Library)
  full_title: RtkVideoView · Cloudflare Realtime docs
  head_html: <title>RtkVideoView · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkVideoView component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/index.md"><meta property="og:title" content="RtkVideoView · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkVideoView component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/#page","headline":"RtkVideoView \u00b7 Cloudflare Realtime docs","description":"API reference for RtkVideoView component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-view/
  schema: 1
---
<p>Renders a participant's video stream.
Supports self-preview, remote participant video, and screen share rendering.</p>
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
<td><code>participant</code></td>
<td><code>RtkMeetingParticipant</code></td>
<td>✅</td>
<td>-</td>
<td>The participant whose video to render</td>
</tr>
<tr>
<td><code>showSelfPreview</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether to show the local camera preview</td>
</tr>
<tr>
<td><code>showScreenShare</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether to show the screen share stream instead of camera</td>
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
<td><code>reattachRenderer()</code></td>
<td><code>Void</code></td>
<td>Reattaches the video renderer to the participant stream</td>
</tr>
<tr>
<td><code>prepareForReuse()</code></td>
<td><code>Void</code></td>
<td>Prepares the view for reuse in a collection or table view</td>
</tr>
<tr>
<td><code>clean()</code></td>
<td><code>Void</code></td>
<td>Releases the video renderer and cleans up resources</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let videoView = RtkVideoView(participant: participant)&#10;view.addSubview(videoView)&#10;</code></pre>
<h3 id="self-preview">Self-preview</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let previewView = RtkVideoView(&#10;    participant: localParticipant,&#10;    showSelfPreview: true&#10;)&#10;view.addSubview(previewView)&#10;</code></pre>
<h3 id="screen-share">Screen share</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let screenShareView = RtkVideoView(&#10;    participant: participant,&#10;    showScreenShare: true&#10;)&#10;view.addSubview(screenShareView)&#10;</code></pre>
