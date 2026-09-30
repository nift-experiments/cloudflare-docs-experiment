---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/
  description: API reference for RtkEventSelfListener component (iOS Library)
  full_title: RtkEventSelfListener · Cloudflare Realtime docs
  head_html: <title>RtkEventSelfListener · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkEventSelfListener component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/index.md"><meta property="og:title" content="RtkEventSelfListener · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkEventSelfListener component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/#page","headline":"RtkEventSelfListener \u00b7 Cloudflare Realtime docs","description":"API reference for RtkEventSelfListener component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-event-self-listener/
  schema: 1
---
<p>A helper class that wraps self-participant and meeting event listeners with closure-based callbacks.
Provides methods for toggling audio and video, observing state changes, and checking device permissions.</p>
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
<td><code>rtkClient</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit client instance</td>
</tr>
<tr>
<td><code>identifier</code></td>
<td><code>String</code></td>
<td>❌</td>
<td><code>&quot;Default&quot;</code></td>
<td>A unique identifier for this listener instance</td>
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
<td><code>toggleLocalAudio(completion:)</code></td>
<td><code>Void</code></td>
<td>Toggles the local microphone on or off</td>
</tr>
<tr>
<td><code>toggleLocalVideo(completion:)</code></td>
<td><code>Void</code></td>
<td>Toggles the local camera on or off</td>
</tr>
<tr>
<td><code>observeSelfVideo(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for local video state changes</td>
</tr>
<tr>
<td><code>observeSelfAudio(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for local audio state changes</td>
</tr>
<tr>
<td><code>observeSelfRemoved(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for when the local participant is removed</td>
</tr>
<tr>
<td><code>observeSelfMeetingEndForAll(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for when the meeting ends for all participants</td>
</tr>
<tr>
<td><code>observeWebinarStageStatus(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for webinar stage status changes</td>
</tr>
<tr>
<td><code>observeRequestToJoinStage(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for stage join request events</td>
</tr>
<tr>
<td><code>observeSelfPermissionChanged(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for permission changes on the local participant</td>
</tr>
<tr>
<td><code>observeMeetingReconnectionState(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for meeting reconnection state changes</td>
</tr>
<tr>
<td><code>isCameraPermissionGranted()</code></td>
<td><code>Bool</code></td>
<td>Returns whether camera permission is granted</td>
</tr>
<tr>
<td><code>isMicrophonePermissionGranted()</code></td>
<td><code>Bool</code></td>
<td>Returns whether microphone permission is granted</td>
</tr>
<tr>
<td><code>clean()</code></td>
<td><code>Void</code></td>
<td>Removes all registered listeners and cleans up resources</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let listener = RtkEventSelfListener(rtkClient: rtkClient)&#10;&#10;listener.observeSelfAudio { isEnabled in&#10;    print(&quot;Audio enabled: \(isEnabled)&quot;)&#10;}&#10;&#10;listener.observeSelfVideo { isEnabled in&#10;    print(&quot;Video enabled: \(isEnabled)&quot;)&#10;}&#10;</code></pre>
<h3 id="toggle-audio-and-video">Toggle audio and video</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let listener = RtkEventSelfListener(rtkClient: rtkClient)&#10;&#10;listener.toggleLocalAudio { success in&#10;    print(&quot;Audio toggled: \(success)&quot;)&#10;}&#10;&#10;listener.toggleLocalVideo { success in&#10;    print(&quot;Video toggled: \(success)&quot;)&#10;}&#10;</code></pre>
<h3 id="observe-meeting-end">Observe meeting end</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let listener = RtkEventSelfListener(&#10;    rtkClient: rtkClient,&#10;    identifier: &quot;MeetingObserver&quot;&#10;)&#10;&#10;listener.observeSelfRemoved {&#10;    print(&quot;Removed from meeting&quot;)&#10;}&#10;&#10;listener.observeSelfMeetingEndForAll {&#10;    print(&quot;Meeting ended for all&quot;)&#10;}&#10;</code></pre>
