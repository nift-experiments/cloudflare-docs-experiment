---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/webhooks/
  description: Receive RealtimeKit events in your application through signed HTTP callbacks.
  full_title: Webhooks · Cloudflare Realtime docs
  head_html: <title>Webhooks · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Receive RealtimeKit events in your application through signed HTTP callbacks."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/webhooks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/webhooks/index.md"><meta property="og:title" content="Webhooks · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Receive RealtimeKit events in your application through signed HTTP callbacks."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/webhooks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/webhooks/#page","headline":"Webhooks \u00b7 Cloudflare Realtime docs","description":"Receive RealtimeKit events in your application through signed HTTP callbacks.","url":"https://developers.cloudflare.com/realtime/realtimekit/webhooks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/webhooks/
  schema: 1
---
<p>Webhooks let your backend receive RealtimeKit events as they happen. RealtimeKit sends an HTTP <code>POST</code> request to your configured endpoint with a JSON payload when a subscribed event occurs, such as when a meeting starts, a participant joins, or a recording is uploaded.</p>
<p>Use webhooks for backend workflows that depend on asynchronous events, such as starting post-meeting processing, downloading transcripts, tracking recording status, or updating your own session records.</p>
<h2 id="how-webhooks-work">How webhooks work</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11592.md")
</div>
<p>Webhook events are subscription-only. Your endpoint receives only the events included in the webhook's <code>events</code> array.</p>
<h2 id="create-a-webhook-endpoint">Create a webhook endpoint</h2>
<p>Your webhook endpoint must accept JSON <code>POST</code> requests. The endpoint can handle multiple event types by switching on the <code>event</code> field in the request body.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/11593.md")
</div>
<p>Your endpoint should return a <code>2xx</code> response as soon as it accepts the event. Move slow work, such as downloading files or calling third-party APIs, to a background job.</p>
<h2 id="register-a-webhook">Register a webhook</h2>
<p>Register the publicly accessible endpoint URL using the RealtimeKit <a href="/api/resources/realtime_kit/subresources/webhooks/">Webhooks API</a>:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;name&quot;: &quot;Production webhook&quot;,&#10;    &quot;url&quot;: &quot;https://example.com/webhook&quot;,&#10;    &quot;events&quot;: [&#10;      &quot;meeting.started&quot;,&#10;      &quot;meeting.ended&quot;,&#10;      &quot;meeting.participantJoined&quot;,&#10;      &quot;meeting.participantLeft&quot;,&#10;      &quot;recording.statusUpdate&quot;&#10;    ],&#10;    &quot;enabled&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>You can also manage webhooks from the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">RealtimeKit dashboard</a>.</p>
<h2 id="webhook-headers">Webhook headers</h2>
<p>RealtimeKit includes headers that help you identify, deduplicate, and verify webhook deliveries:</p>
<table>
<thead>
<tr>
<th>Header</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rtk-signature</code></td>
<td>Base64-encoded RSA-SHA256 signature for the request body. Use this header to verify that the request came from RealtimeKit.</td>
</tr>
<tr>
<td><code>rtk-uuid</code></td>
<td>Unique ID for the webhook delivery. Store this value if you need to avoid processing duplicate deliveries.</td>
</tr>
<tr>
<td><code>rtk-webhook-id</code></td>
<td>ID of the webhook configuration that triggered the delivery.</td>
</tr>
</tbody>
</table>
<h2 id="verify-webhook-signatures">Verify webhook signatures</h2>
<p>RealtimeKit signs each webhook request body with RSA-SHA256. Verify the signature before processing the event.</p>
<h3 id="fetch-the-public-key">Fetch the public key</h3>
<p>Fetch the RealtimeKit webhook public key from:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.realtime.cloudflare.com/.well-known/webhooks.json&quot;&#10;</code></pre>
<p>The response includes a PEM-encoded public key:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;data&quot;: {&#10;		&quot;publicKey&quot;: &quot;-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----&quot;&#10;	},&#10;	&quot;message&quot;: &quot;&quot;&#10;}&#10;</code></pre>
<h3 id="verify-the-request-body">Verify the request body</h3>
<p>Verify <code>rtk-signature</code> against the raw request body. Do not reserialize parsed JSON before verification because changes in whitespace or key order can change the signed bytes.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/11594.md")
</div>
<h2 id="retry-behavior">Retry behavior</h2>
<p>RealtimeKit treats any <code>2xx</code> response as a successful delivery.</p>
<p>If your endpoint returns a <code>5xx</code> response or the request fails because of a network error, RealtimeKit retries the delivery. If your endpoint returns a non-<code>2xx</code> response below <code>500</code>, RealtimeKit records the delivery as failed and does not retry it.</p>
<p>After repeated delivery failures, RealtimeKit may temporarily reduce delivery attempts to that webhook URL. Return a <code>2xx</code> response only after your application has accepted the event.</p>
<h2 id="supported-events">Supported events</h2>
<p>RealtimeKit supports these webhook events:</p>
<table>
<thead>
<tr>
<th>Event</th>
<th>Trigger</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>meeting.started</code></td>
<td>The first participant joins a meeting.</td>
</tr>
<tr>
<td><code>meeting.ended</code></td>
<td>The meeting ends because the host ended it or all participants left.</td>
</tr>
<tr>
<td><code>meeting.participantJoined</code></td>
<td>A participant joins a meeting.</td>
</tr>
<tr>
<td><code>meeting.participantLeft</code></td>
<td>A participant leaves a meeting.</td>
</tr>
<tr>
<td><code>meeting.chatSynced</code></td>
<td>The chat export for a completed meeting is available.</td>
</tr>
<tr>
<td><code>recording.statusUpdate</code></td>
<td>A recording changes status.</td>
</tr>
<tr>
<td><code>livestreaming.statusUpdate</code></td>
<td>A livestream changes status.</td>
</tr>
<tr>
<td><code>meeting.transcript</code></td>
<td>The transcript for a completed meeting is available.</td>
</tr>
<tr>
<td><code>meeting.summary</code></td>
<td>The AI-generated summary for a completed meeting is available.</td>
</tr>
</tbody>
</table>
<p>Fetch the current event list with the Webhooks API:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks/all&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h2 id="event-payloads">Event payloads</h2>
<p>All webhook payloads include an <code>event</code> field. The remaining fields depend on the event type.</p>
<h3 id="meeting-started"><code>meeting.started</code></h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.started&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;title&quot;: &quot;Weekly sync&quot;,&#10;		&quot;status&quot;: &quot;LIVE&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;startedAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="meeting-ended"><code>meeting.ended</code></h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.ended&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;title&quot;: &quot;Weekly sync&quot;,&#10;		&quot;status&quot;: &quot;LIVE&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;startedAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;endedAt&quot;: &quot;2026-06-03T10:30:00.000Z&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	},&#10;	&quot;reason&quot;: &quot;ALL_PARTICIPANTS_LEFT&quot;&#10;}&#10;</code></pre>
<p>The <code>reason</code> value can be <code>HOST_ENDED_MEETING</code> or <code>ALL_PARTICIPANTS_LEFT</code>.</p>
<h3 id="meeting-participantjoined"><code>meeting.participantJoined</code></h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.participantJoined&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;title&quot;: &quot;Weekly sync&quot;,&#10;		&quot;status&quot;: &quot;LIVE&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;startedAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	},&#10;	&quot;participant&quot;: {&#10;		&quot;peerId&quot;: &quot;e32fb785-ddd0-4b96-b577-879327c0082f&quot;,&#10;		&quot;userDisplayName&quot;: &quot;Mary Sue&quot;,&#10;		&quot;customParticipantId&quot;: &quot;user-123&quot;,&#10;		&quot;joinedAt&quot;: &quot;2026-06-03T10:05:00.000Z&quot;&#10;	}&#10;}&#10;</code></pre>
<p>Use <code>customParticipantId</code> for your own participant identifier. <code>clientSpecificId</code> is included for compatibility with older integrations.</p>
<h3 id="meeting-participantleft"><code>meeting.participantLeft</code></h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.participantLeft&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;title&quot;: &quot;Weekly sync&quot;,&#10;		&quot;status&quot;: &quot;LIVE&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;startedAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;endedAt&quot;: &quot;2026-06-03T10:30:00.000Z&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	},&#10;	&quot;participant&quot;: {&#10;		&quot;peerId&quot;: &quot;e32fb785-ddd0-4b96-b577-879327c0082f&quot;,&#10;		&quot;userDisplayName&quot;: &quot;Mary Sue&quot;,&#10;		&quot;customParticipantId&quot;: &quot;user-123&quot;,&#10;		&quot;joinedAt&quot;: &quot;2026-06-03T10:05:00.000Z&quot;,&#10;		&quot;leftAt&quot;: &quot;2026-06-03T10:25:00.000Z&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="meeting-chatsynced"><code>meeting.chatSynced</code></h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.chatSynced&quot;,&#10;	&quot;title&quot;: &quot;Weekly sync&quot;,&#10;	&quot;endedAt&quot;: &quot;2026-06-03T10:30:00.000Z&quot;,&#10;	&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;	&quot;meetingId&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;	&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;	&quot;startedAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;	&quot;chatDownloadUrl&quot;: &quot;https://example.com/chat.json&quot;,&#10;	&quot;chatDownloadUrlExpiry&quot;: &quot;2026-06-10T10:30:00.000Z&quot;,&#10;	&quot;organizedBy&quot;: {&#10;		&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;		&quot;name&quot;: &quot;Example organization&quot;&#10;	}&#10;}&#10;</code></pre>
<h3 id="recording-statusupdate"><code>recording.statusUpdate</code></h3>
<p>RealtimeKit sends <code>recording.statusUpdate</code> when a recording moves through its lifecycle. Recording statuses include <code>RECORDING</code>, <code>UPLOADING</code>, <code>UPLOADED</code>, and <code>ERRORED</code>. For more information, refer to <a href="/realtime/realtimekit/recording-guide/monitor-status/">Monitor Recording Status</a>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;recording.statusUpdate&quot;,&#10;	&quot;recording&quot;: {&#10;		&quot;id&quot;: &quot;97cb480d-5840-4528-ace3-919b5e386c68&quot;,&#10;		&quot;recordingId&quot;: &quot;97cb480d-5840-4528-ace3-919b5e386c68&quot;,&#10;		&quot;status&quot;: &quot;UPLOADED&quot;,&#10;		&quot;downloadUrl&quot;: &quot;https://example.com/recording.mp4&quot;,&#10;		&quot;audioDownloadUrl&quot;: &quot;https://example.com/recording.mp3&quot;,&#10;		&quot;downloadUrlExpiry&quot;: &quot;2026-06-10T10:30:00.000Z&quot;,&#10;		&quot;startedTime&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;stoppedTime&quot;: &quot;2026-06-03T10:30:00.000Z&quot;,&#10;		&quot;fileSize&quot;: &quot;2044680&quot;,&#10;		&quot;outputFileName&quot;: &quot;weekly-sync.mp4&quot;,&#10;		&quot;meetingId&quot;: &quot;50c8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;recordingDuration&quot;: 1800,&#10;		&quot;organizationId&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;		&quot;roomUUID&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;&#10;	},&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;title&quot;: &quot;Weekly sync&quot;,&#10;		&quot;status&quot;: &quot;LIVE&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;startedAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;endedAt&quot;: &quot;2026-06-03T10:30:00.000Z&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="livestreaming-statusupdate"><code>livestreaming.statusUpdate</code></h3>
<p>Livestream statuses include <code>LIVE</code>, <code>OFFLINE</code>, and <code>IDLE</code>.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;livestreaming.statusUpdate&quot;,&#10;	&quot;streamId&quot;: &quot;d231d346-c422-43a6-a324-c0d65b79c8a7&quot;,&#10;	&quot;status&quot;: &quot;LIVE&quot;,&#10;	&quot;manualIngest&quot;: false,&#10;	&quot;playbackUrl&quot;: &quot;https://example.com/live.m3u8&quot;,&#10;	&quot;ingestServer&quot;: &quot;rtmps://example.com/live&quot;,&#10;	&quot;streamKey&quot;: &quot;stream-key&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;title&quot;: &quot;Weekly sync&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;status&quot;: &quot;LIVE&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="meeting-transcript"><code>meeting.transcript</code></h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.transcript&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;title&quot;: &quot;Weekly sync&quot;,&#10;		&quot;endedAt&quot;: &quot;2026-06-03T10:30:00.000Z&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;startedAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;status&quot;: &quot;LIVE&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	},&#10;	&quot;transcriptDownloadUrl&quot;: &quot;https://example.com/transcript.csv&quot;,&#10;	&quot;transcriptDownloadUrlExpiry&quot;: &quot;2026-06-10T10:30:00.000Z&quot;&#10;}&#10;</code></pre>
<h3 id="meeting-summary"><code>meeting.summary</code></h3>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.summary&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	},&#10;	&quot;summaryDownloadUrl&quot;: &quot;https://example.com/summary.txt&quot;,&#10;	&quot;summaryDownloadUrlExpiry&quot;: &quot;2026-06-10T10:30:00.000Z&quot;&#10;}&#10;</code></pre>
