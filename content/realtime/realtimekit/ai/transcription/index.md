---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/
  description: Turn on real-time and post-meeting speech-to-text transcription in RealtimeKit.
  full_title: Transcription · Cloudflare Realtime docs
  head_html: <title>Transcription · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Turn on real-time and post-meeting speech-to-text transcription in RealtimeKit."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/index.md"><meta property="og:title" content="Transcription · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Turn on real-time and post-meeting speech-to-text transcription in RealtimeKit."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/#page","headline":"Transcription \u00b7 Cloudflare Realtime docs","description":"Turn on real-time and post-meeting speech-to-text transcription in RealtimeKit.","url":"https://developers.cloudflare.com/realtime/realtimekit/ai/transcription/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ai/transcription/
  schema: 1
---
<p>RealtimeKit provides two transcription modes powered by <a href="/workers-ai/">Cloudflare Workers AI</a>:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Model</th>
<th>Processing time</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#real-time-transcription"><strong>Real-time</strong></a></td>
<td><a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a></td>
<td>During the meeting</td>
<td>Live captions for attendees</td>
</tr>
<tr>
<td><a href="#post-meeting-transcription"><strong>Post-meeting</strong></a></td>
<td><a href="/workers-ai/models/whisper-large-v3-turbo/">Whisper Large v3 Turbo</a></td>
<td>After the meeting ends</td>
<td><a href="#output-formats">Transcript files</a> and <a href="/realtime/realtimekit/webhooks/">webhooks</a></td>
</tr>
</tbody>
</table>
<p>RealtimeKit processes each participant audio stream separately. This helps identify each speaker in the final transcript.</p>
<p>We recommend upgrading to the Workers Paid plan to avoid Workers AI processing limits on the Free plan. Learn more in <a href="#billing-and-free-plan-limits">Billing and Free plan limits</a>.</p>
<h2 id="real-time-transcription">Real-time transcription</h2>
<p>Real-time transcription streams participant audio to <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> on Workers AI and sends <a href="#consume-real-time-transcripts">transcript events</a> to meeting participants during the meeting.</p>
<h3 id="turn-on-real-time-transcription">Turn on real-time transcription</h3>
<p>You can turn on real-time transcription for participants by setting <code>permissions.transcription_enabled: true</code> in the participant's <a href="/realtime/realtimekit/concepts/preset/">preset</a>. This lets you decide which participant audio is transcribed. For example, you can transcribe speaker audio without transcribing audience audio.</p>
<p>To update an existing preset, use the <a href="/api/resources/realtime_kit/subresources/presets/methods/update/">Update a preset API</a>:</p>
<pre tabindex="0"><code class="language-bash">curl -X PATCH &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/presets/$PRESET_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;permissions&quot;: {&#10;      &quot;transcription_enabled&quot;: true&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>To create a preset, refer to the <a href="/api/resources/realtime_kit/subresources/presets/methods/create/">Create a preset API reference</a>.</p>
<p>RealtimeKit transcribes audio only for participants who join with a preset that has <code>permissions.transcription_enabled: true</code>.</p>
<p>During the meeting, RealtimeKit streams transcript updates to the client SDK. To access existing transcripts from <code>meeting.ai.transcripts</code> or listen for new transcript events with <code>meeting.ai.on(&quot;transcript&quot;, ...)</code>, refer to <a href="#consume-real-time-transcripts">Consume real-time transcripts</a>.</p>
<h3 id="configure-transcription-settings">Configure transcription settings</h3>
<p>The preset controls whose audio is transcribed. The meeting configuration controls how RealtimeKit transcribes that audio. Use <code>ai_config.transcription</code> to set the <a href="#real-time-supported-languages">spoken language</a>, boost recognition for custom terms, and control profanity filtering for a specific meeting.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;title&quot;: &quot;Weekly product review&quot;,&#10;    &quot;ai_config&quot;: {&#10;      &quot;transcription&quot;: {&#10;        &quot;language&quot;: &quot;en-US&quot;,&#10;        &quot;keywords&quot;: [&quot;RealtimeKit&quot;, &quot;Cloudflare&quot;],&#10;        &quot;profanity_filter&quot;: false&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>language</code></td>
<td>string</td>
<td><code>en-US</code></td>
<td>Language code for transcription</td>
</tr>
<tr>
<td><code>keywords</code></td>
<td>string[]</td>
<td><code>[]</code></td>
<td>Terms to boost recognition (names, jargon)</td>
</tr>
<tr>
<td><code>profanity_filter</code></td>
<td>boolean</td>
<td><code>false</code></td>
<td>Filter offensive language</td>
</tr>
</tbody>
</table>
<h3 id="real-time-supported-languages">Real-time supported languages</h3>
<p>Real-time transcription is powered by <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> on Workers AI.</p>
<p>Nova-3 on Workers AI supports the following languages for transcription:</p>
<table>
<thead>
<tr>
<th>Language</th>
<th>Code(s)</th>
</tr>
</thead>
<tbody>
<tr>
<td>English</td>
<td><code>en</code>, <code>en-US</code>, <code>en-AU</code>, <code>en-GB</code>, <code>en-IN</code>, <code>en-NZ</code></td>
</tr>
<tr>
<td>Spanish</td>
<td><code>es</code>, <code>es-419</code></td>
</tr>
<tr>
<td>French</td>
<td><code>fr</code>, <code>fr-CA</code></td>
</tr>
<tr>
<td>German</td>
<td><code>de</code>, <code>de-CH</code></td>
</tr>
<tr>
<td>Hindi</td>
<td><code>hi</code></td>
</tr>
<tr>
<td>Russian</td>
<td><code>ru</code></td>
</tr>
<tr>
<td>Portuguese</td>
<td><code>pt</code>, <code>pt-BR</code>, <code>pt-PT</code></td>
</tr>
<tr>
<td>Japanese</td>
<td><code>ja</code></td>
</tr>
<tr>
<td>Italian</td>
<td><code>it</code></td>
</tr>
<tr>
<td>Dutch</td>
<td><code>nl</code></td>
</tr>
</tbody>
</table>
<p>Use <code>multi</code> for automatic multilingual detection across all of the languages listed above.</p>
<p>If no language is specified, the model defaults to <code>en-US</code>. For best accuracy, explicitly set the language code matching your audio.</p>
<h3 id="consume-real-time-transcripts">Consume real-time transcripts</h3>
<p>Real-time transcription sends interim and final transcript updates to the client SDK. Use interim updates for live captions, and use final updates for transcript history or saved UI state.</p>
<h4 id="client-sdk">Client SDK</h4>
<pre tabindex="0"><code class="language-js">// Get transcript entries already received by the client.&#10;const transcripts = meeting.ai.transcripts;&#10;&#10;// Listen for transcript updates during the meeting.&#10;meeting.ai.on(&quot;transcript&quot;, (transcript) =&gt; {&#10;	if (transcript.isPartialTranscript) {&#10;		updateLiveCaption(transcript.peerId, transcript.transcript);&#10;		return;&#10;	}&#10;&#10;	appendFinalTranscript(transcript);&#10;});&#10;</code></pre>
<h4 id="transcript-payload">Transcript payload</h4>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;id&quot;: &quot;1a2b3c4d-5678-90ab-cdef-1234567890ab&quot;,&#10;	&quot;name&quot;: &quot;Alice&quot;,&#10;	&quot;peerId&quot;: &quot;4f5g6h7i-8j9k-0lmn-opqr-1234567890st&quot;,&#10;	&quot;userId&quot;: &quot;uvwxyz-1234-5678-90ab-cdefghijklmn&quot;,&#10;	&quot;customParticipantId&quot;: &quot;abc123xyz&quot;,&#10;	&quot;transcript&quot;: &quot;Hello everyone&quot;,&#10;	&quot;isPartialTranscript&quot;: false,&#10;	&quot;timestamp&quot;: 1716700000000&#10;}&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>Unique transcript entry ID</td>
</tr>
<tr>
<td><code>name</code></td>
<td>Display name of the participant who spoke</td>
</tr>
<tr>
<td><code>peerId</code></td>
<td>Peer ID of the participant who spoke. Changes if they rejoin.</td>
</tr>
<tr>
<td><code>userId</code></td>
<td>Persistent participant ID</td>
</tr>
<tr>
<td><code>customParticipantId</code></td>
<td>Participant identifier set when the participant was added</td>
</tr>
<tr>
<td><code>transcript</code></td>
<td>Transcribed text</td>
</tr>
<tr>
<td><code>isPartialTranscript</code></td>
<td><code>true</code> for interim updates, <code>false</code> for final updates</td>
</tr>
<tr>
<td><code>timestamp</code></td>
<td>Unix epoch timestamp in milliseconds</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="post-meeting-transcription">Post-meeting transcription</h2>
<p>Post-meeting transcription generates a transcript after the meeting ends using <a href="/workers-ai/models/whisper-large-v3-turbo/">Whisper Large v3 Turbo</a> on Workers AI and delivers it through a <a href="/realtime/realtimekit/webhooks/">webhook</a> or <a href="#rest-api">REST API</a>. To identify speakers, RealtimeKit processes each participant's audio separately before creating the <a href="#output-formats">final transcript</a>.</p>
<h3 id="turn-on-post-meeting-transcription">Turn on post-meeting transcription</h3>
<p>You can turn on post-meeting transcription when you create a meeting. Set <code>transcribe_on_end: true</code> to generate a transcript after the meeting ends. To also generate a <a href="/realtime/realtimekit/ai/summary/">summary</a> automatically after the transcript is available, set <code>summarize_on_end: true</code>.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;title&quot;: &quot;Weekly product review&quot;,&#10;    &quot;transcribe_on_end&quot;: true,&#10;    &quot;summarize_on_end&quot;: true,&#10;    &quot;ai_config&quot;: {&#10;      &quot;transcription&quot;: {&#10;        &quot;language&quot;: &quot;en&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Use <code>ai_config.transcription.language</code> to set the transcript language. For supported values, refer to <a href="#post-meeting-supported-languages">Post-meeting supported languages</a>. If <code>transcribe_on_end</code> is not set, RealtimeKit does not generate a post-meeting transcript.</p>
<h3 id="post-meeting-supported-languages">Post-meeting supported languages</h3>
<p>Post-meeting transcription supports <a href="/workers-ai/models/whisper-large-v3-turbo/">Whisper Large v3 Turbo</a> language codes. Omit <code>ai_config.transcription.language</code> to let Whisper detect the spoken language.</p>
<p>Common language codes include:</p>
<table>
<thead>
<tr>
<th>Language</th>
<th>Code</th>
<th>Language</th>
<th>Code</th>
<th>Language</th>
<th>Code</th>
</tr>
</thead>
<tbody>
<tr>
<td>English</td>
<td><code>en</code></td>
<td>Spanish</td>
<td><code>es</code></td>
<td>French</td>
<td><code>fr</code></td>
</tr>
<tr>
<td>German</td>
<td><code>de</code></td>
<td>Hindi</td>
<td><code>hi</code></td>
<td>Portuguese</td>
<td><code>pt</code></td>
</tr>
<tr>
<td>Japanese</td>
<td><code>ja</code></td>
<td>Italian</td>
<td><code>it</code></td>
<td>Dutch</td>
<td><code>nl</code></td>
</tr>
<tr>
<td>Russian</td>
<td><code>ru</code></td>
<td>Chinese</td>
<td><code>zh</code></td>
<td>Cantonese</td>
<td><code>yue</code></td>
</tr>
</tbody>
</table>
<details class="nb-details"><summary>Additional post-meeting language codes</summary><div class="nb-details-body">
@input("content/.markup/bodies/12514.md")
</div></details>
<h3 id="output-formats">Output formats</h3>
<p>Post-meeting transcripts are available in multiple formats. Use CSV or JSON for application workflows, and use SRT or VTT when you need subtitle files.</p>
<table>
<thead>
<tr>
<th>Format</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>CSV</strong></td>
<td>Spreadsheets and data analysis</td>
</tr>
<tr>
<td><strong>JSON</strong></td>
<td>Programmatic access</td>
</tr>
<tr>
<td><strong>SRT</strong></td>
<td>Video subtitle files</td>
</tr>
<tr>
<td><strong>VTT</strong></td>
<td>Web video captions (<code>&lt;track&gt;</code> element)</td>
</tr>
</tbody>
</table>
<h4 id="examples">Examples</h4>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="transcriptFormat"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12518.md")
</div></div>
<h3 id="consume-post-meeting-transcripts">Consume post-meeting transcripts</h3>
<p>After RealtimeKit finishes processing a post-meeting transcript, you can receive the transcript download URL through a webhook or fetch it with the REST API. Use webhooks for asynchronous backend workflows, and use the REST API when you need to retrieve the transcript for a specific session.</p>
<h4 id="webhook">Webhook</h4>
<p>Configure the <code>meeting.transcript</code> event in <a href="/realtime/realtimekit/webhooks/#meetingtranscript">RealtimeKit webhooks</a>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.transcript&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;title&quot;: &quot;Weekly sync&quot;,&#10;		&quot;endedAt&quot;: &quot;2026-06-03T10:30:00.000Z&quot;,&#10;		&quot;createdAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;startedAt&quot;: &quot;2026-06-03T10:00:00.000Z&quot;,&#10;		&quot;status&quot;: &quot;LIVE&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	},&#10;	&quot;transcriptDownloadUrl&quot;: &quot;https://example.com/transcript.csv&quot;,&#10;	&quot;transcriptDownloadUrlExpiry&quot;: &quot;2026-06-10T10:30:00.000Z&quot;&#10;}&#10;</code></pre>
<h4 id="rest-api">REST API</h4>
<p>Refer to <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/">Fetch the complete transcript for a session</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h4 id="transcript-availability">Transcript availability</h4>
<p>Transcripts are available for <strong>7 days</strong> after the meeting ends. Download or copy transcript files before the URL expiry time returned by the webhook or REST API.</p>
<h2 id="billing-and-free-plan-limits">Billing and Free plan limits</h2>
<p>RealtimeKit's default transcription records each participant's audio track and processes it with Workers AI. Workers AI usage is billed to your Cloudflare account using <a href="/workers-ai/platform/pricing/#audio-model-pricing">audio model pricing</a>, which scales by participant audio minutes, not meeting duration.</p>
<p>On the Workers Free plan, Workers AI includes 10,000 Neurons per day. To use more than 10,000 Neurons per day, upgrade to the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>. Workers Paid includes the same 10,000 daily free Neurons, then bills additional usage at <code>$0.011</code> per 1,000 Neurons.</p>
<p>You can upgrade to the Workers Paid plan in the Cloudflare dashboard under <strong>Manage account</strong>.</p>
<p>RealtimeKit transcription uses these Workers AI audio model rates:</p>
<table>
<thead>
<tr>
<th>Transcription mode</th>
<th>Workers AI model</th>
<th>Neurons per audio minute</th>
</tr>
</thead>
<tbody>
<tr>
<td>Post-meeting</td>
<td><code>@cf/openai/whisper-large-v3-turbo</code></td>
<td><code>46.63</code></td>
</tr>
<tr>
<td>Real-time</td>
<td><code>@cf/deepgram/nova-3</code> WebSocket</td>
<td><code>836.36</code></td>
</tr>
</tbody>
</table>
<h2 id="data-processing-and-storage">Data processing and storage</h2>
<p>RealtimeKit transcription is a managed transcription workflow. When transcription is turned on, RealtimeKit processes participant audio with Workers AI and stores <a href="#output-formats">transcript outputs</a> in RealtimeKit-managed storage.</p>
<p>For real-time transcription, RealtimeKit streams audio from participants with transcription turned on to Workers AI and sends transcript updates to meeting participants during the meeting.</p>
<p>For post-meeting transcription, RealtimeKit processes each participant's audio separately after the meeting ends, creates the final transcript files, and makes them available through a webhook or REST API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="storage-for-sensitive-workloads">Storage for sensitive workloads</h3>
@markup("md", "content/.markup/bodies/12513.md")
</aside>
