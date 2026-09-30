---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/
  description: Record separate audio tracks for selected RealtimeKit participants and download per-participant WebM files.
  full_title: Track recording · Cloudflare Realtime docs
  head_html: <title>Track recording · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Record separate audio tracks for selected RealtimeKit participants and download per-participant WebM files."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/index.md"><meta property="og:title" content="Track recording · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Record separate audio tracks for selected RealtimeKit participants and download per-participant WebM files."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/#page","headline":"Track recording \u00b7 Cloudflare Realtime docs","description":"Record separate audio tracks for selected RealtimeKit participants and download per-participant WebM files.","url":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/track-recording/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/recording-guide/track-recording/
  schema: 1
---
<p>Track recording lets you record participant audio as separate WebM files instead of one composite meeting recording. Use it when you need speaker-level control over what you store, process, or review.</p>
<p>With track recording, you can record specific participant tracks by passing <code>user_ids</code>, which is useful for content-sensitive or regulated workflows where recording every participant is unnecessary. If you do not provide <code>user_ids</code>, RealtimeKit will record all participant audio tracks as separate WebM files by default.</p>
<p>To pass <code>user_ids</code> for specific participant track recording, use the following minimum SDK versions:</p>
<ul>
<li>Web Core: <code>@cloudflare/realtimekit</code> version <code>1.4.0</code> or later</li>
<li>Web UI Kit: <code>@cloudflare/realtimekit-ui</code>, <code>@cloudflare/realtimekit-react-ui</code>, or <code>@cloudflare/realtimekit-angular-ui</code> version <code>1.1.2</code> or later</li>
<li>Android Core or iOS Core: version <code>2.0.0</code> or later</li>
<li>Android UI Kit or iOS UI Kit: version <code>1.1.0</code> or later</li>
</ul>
<p>Track recording creates one file per recorded participant.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11808.md")
</aside>
<h2 id="availability-and-limits">Availability and limits</h2>
<p>Track recording has the following requirements and limits:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Active meeting</td>
<td>The meeting must have an active live session.</td>
</tr>
<tr>
<td>Media kind</td>
<td>Only <code>audio</code> layers are recorded.</td>
</tr>
<tr>
<td>Participant selection</td>
<td>Pass up to 100 values in <code>user_ids</code>.</td>
</tr>
<tr>
<td>Storage</td>
<td>Files are uploaded to RealtimeKit's managed R2 bucket with zero-egress fees.</td>
</tr>
<tr>
<td>File retention</td>
<td>RealtimeKit bucket download URLs expire after seven days.</td>
</tr>
</tbody>
</table>
<h2 id="start-track-recording">Start track recording</h2>
<h3 id="record-specific-participants">Record specific participants</h3>
<p>To record separate audio tracks for specific participants, call <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_track_recording/"><code>POST /recordings/track</code></a> with the meeting ID and the participant <code>user_ids</code>.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings/track \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;  &quot;user_ids&quot;: [&quot;user-123&quot;, &quot;user-456&quot;]&#10;}&#x27;&#10;</code></pre>
<p>RealtimeKit records current and future participants whose <code>user_id</code> matches the allowlist. Participants whose <code>user_id</code> is not listed are not recorded.</p>
<h3 id="record-all-participants-as-separate-tracks">Record all participants as separate tracks</h3>
<p>Omit <code>user_ids</code> to record separate audio tracks for all participants in the live meeting. RealtimeKit creates one WebM file for each recorded participant.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings/track \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;&#10;}&#x27;&#10;</code></pre>
<p>The response includes a recording ID. Use this ID to stop or fetch the recording.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;data&quot;: {&#10;		&quot;recording&quot;: {&#10;			&quot;id&quot;: &quot;fff40c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;			&quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;			&quot;status&quot;: &quot;INVOKED&quot;,&#10;			&quot;type&quot;: &quot;TRACK&quot;,&#10;			&quot;output_file_name&quot;: &quot;{{file_name_prefix}}_{{user_id}}_{{peer_id}}_{{stream_kind}}_{{media_kind}}_{{date_time}}.webm&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="customize-file-names-with-prefixes">Customize file names with prefixes</h2>
<p>Use <code>layers.default.file_name_prefix</code> to prefix every generated track recording file.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;	&quot;layers&quot;: {&#10;		&quot;default&quot;: {&#10;			&quot;media_kind&quot;: &quot;audio&quot;,&#10;			&quot;file_name_prefix&quot;: &quot;speaker&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>If you omit <code>layers</code>, RealtimeKit uses <code>default</code> as the file name prefix.</p>
<h2 id="stop-track-recording">Stop track recording</h2>
<p>Use the <a href="/api/resources/realtime_kit/subresources/recordings/methods/pause_resume_stop_recording/">recording update endpoint</a> to stop a track recording.</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings/&lt;recording_id&gt; \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;action&quot;: &quot;stop&quot;&#10;}&#x27;&#10;</code></pre>
<p>Track recording also stops when the meeting session ends.</p>
<p>After track recording stops, RealtimeKit uploads the per-participant WebM files and moves the recording to <code>UPLOADED</code>.</p>
<h2 id="download-track-files">Download track files</h2>
<p>Track recording uses the same recording status lifecycle as composite recording. To monitor status, refer to <a href="/realtime/realtimekit/recording-guide/monitor-status/">Monitor Recording Status</a>.</p>
<p>When the recording reaches <code>UPLOADED</code>, fetch the recording details or listen for the <code>recording.statusUpdate</code> webhook. For track recordings, <code>download_url</code> contains per-participant WebM file URLs grouped by layer.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;download_url&quot;: [&#10;		{&#10;			&quot;layer_name&quot;: &quot;default&quot;,&#10;			&quot;download_urls&quot;: {&#10;				&quot;speaker_user-123_peer-456_peer_audio_1760000000000.webm&quot;: {&#10;					&quot;download_url&quot;: &quot;https://example.com/presigned-url&quot;&#10;				}&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>File names use this format:</p>
<pre tabindex="0"><code class="language-txt">{{file_name_prefix}}_{{user_id}}_{{peer_id}}_{{stream_kind}}_{{media_kind}}_{{date_time}}.webm&#10;</code></pre>
<p>The <code>date_time</code> value is the Unix timestamp in milliseconds when the file was generated.</p>
