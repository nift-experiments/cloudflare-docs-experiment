---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/
  description: API reference for RtkWaitListParticipantUpdateEventListener component (iOS Library)
  full_title: RtkWaitListParticipantUpdateEventListener · Cloudflare Realtime docs
  head_html: <title>RtkWaitListParticipantUpdateEventListener · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="API reference for RtkWaitListParticipantUpdateEventListener component (iOS Library)"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/index.md"><meta property="og:title" content="RtkWaitListParticipantUpdateEventListener · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="API reference for RtkWaitListParticipantUpdateEventListener component (iOS Library)"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/#page","headline":"RtkWaitListParticipantUpdateEventListener \u00b7 Cloudflare Realtime docs","description":"API reference for RtkWaitListParticipantUpdateEventListener component (iOS Library)","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/api-reference/ios/rtk-wait-list-participant-update-event-listener/
  schema: 1
---
<p>A helper class for listening to waitlist participant events.
Provides callbacks for join, remove, accept, and reject events, and methods for managing waitlist requests.</p>
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
</tbody>
</table>
<h2 id="callback-properties">Callback properties</h2>
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
<td><code>participantJoinedCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Called when a participant joins the waitlist</td>
</tr>
<tr>
<td><code>participantRemovedCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Called when a participant is removed from the waitlist</td>
</tr>
<tr>
<td><code>participantRequestAcceptedCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Called when a waitlist request is accepted</td>
</tr>
<tr>
<td><code>participantRequestRejectCompletion</code></td>
<td><code>(() -&gt; Void)?</code></td>
<td>❌</td>
<td><code>nil</code></td>
<td>Called when a waitlist request is rejected</td>
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
<td><code>acceptWaitingRequest(participant:)</code></td>
<td><code>Void</code></td>
<td>Accepts a participant's waitlist request</td>
</tr>
<tr>
<td><code>rejectWaitingRequest(participant:)</code></td>
<td><code>Void</code></td>
<td>Rejects a participant's waitlist request</td>
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
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let waitlistListener = RtkWaitListParticipantUpdateEventListener(&#10;    rtkClient: rtkClient&#10;)&#10;&#10;waitlistListener.participantJoinedCompletion = {&#10;    print(&quot;New participant in waitlist&quot;)&#10;}&#10;&#10;waitlistListener.participantRemovedCompletion = {&#10;    print(&quot;Participant removed from waitlist&quot;)&#10;}&#10;</code></pre>
<h3 id="accept-or-reject-requests">Accept or reject requests</h3>
<pre tabindex="0"><code class="language-swift">import RealtimeKitUI&#10;&#10;let waitlistListener = RtkWaitListParticipantUpdateEventListener(&#10;    rtkClient: rtkClient&#10;)&#10;&#10;// Accept a waiting participant&#10;waitlistListener.acceptWaitingRequest(participant: waitingParticipant)&#10;&#10;// Reject a waiting participant&#10;waitlistListener.rejectWaitingRequest(participant: waitingParticipant)&#10;</code></pre>
