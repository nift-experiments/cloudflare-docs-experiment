---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ai/summary/
  description: Generate AI-powered meeting summaries from transcript data in RealtimeKit.
  full_title: Summary · Cloudflare Realtime docs
  head_html: <title>Summary · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate AI-powered meeting summaries from transcript data in RealtimeKit."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ai/summary/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ai/summary/index.md"><meta property="og:title" content="Summary · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate AI-powered meeting summaries from transcript data in RealtimeKit."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ai/summary/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/ai/summary/#page","headline":"Summary \u00b7 Cloudflare Realtime docs","description":"Generate AI-powered meeting summaries from transcript data in RealtimeKit.","url":"https://developers.cloudflare.com/realtime/realtimekit/ai/summary/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ai/summary/
  schema: 1
---
<p>RealtimeKit generates AI-powered meeting summaries from transcript data.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12519.md")
</aside>
<h2 id="turn-on-summarization">Turn on summarization</h2>
<p>Set <code>summarize_on_end: true</code> when <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a>. For post-meeting summaries, also set <code>transcribe_on_end: true</code> so RealtimeKit generates the summary automatically after the transcript is available:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;title&quot;: &quot;Product Review&quot;,&#10;    &quot;transcribe_on_end&quot;: true,&#10;    &quot;summarize_on_end&quot;: true,&#10;    &quot;ai_config&quot;: {&#10;      &quot;transcription&quot;: {&#10;        &quot;language&quot;: &quot;en-US&quot;&#10;      },&#10;      &quot;summarization&quot;: {&#10;        &quot;word_limit&quot;: 500,&#10;        &quot;text_format&quot;: &quot;markdown&quot;,&#10;        &quot;summary_type&quot;: &quot;team_meeting&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h2 id="configuration">Configuration</h2>
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
<td><code>word_limit</code></td>
<td>number</td>
<td>500</td>
<td>Summary length (150-1000 words)</td>
</tr>
<tr>
<td><code>text_format</code></td>
<td>string</td>
<td><code>markdown</code></td>
<td>Output format: <code>plain_text</code> or <code>markdown</code></td>
</tr>
<tr>
<td><code>summary_type</code></td>
<td>string</td>
<td><code>general</code></td>
<td>Meeting context for tailored summaries</td>
</tr>
</tbody>
</table>
<h3 id="summary-types">Summary types</h3>
<p>Choose a type that matches your meeting for better results:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>general</code></td>
<td>Any meeting (default)</td>
</tr>
<tr>
<td><code>team_meeting</code></td>
<td>Regular team syncs</td>
</tr>
<tr>
<td><code>daily_standup</code></td>
<td>Agile standups</td>
</tr>
<tr>
<td><code>one_on_one_meeting</code></td>
<td>1:1 meetings</td>
</tr>
<tr>
<td><code>sales_call</code></td>
<td>Customer sales conversations</td>
</tr>
<tr>
<td><code>client_check_in</code></td>
<td>Client status updates</td>
</tr>
<tr>
<td><code>interview</code></td>
<td>Job interviews</td>
</tr>
<tr>
<td><code>lecture</code></td>
<td>Educational content</td>
</tr>
<tr>
<td><code>code_review</code></td>
<td>Technical code reviews</td>
</tr>
</tbody>
</table>
<h2 id="consume-summaries">Consume summaries</h2>
<h3 id="webhook">Webhook</h3>
<p>Configure the <code>meeting.summary</code> event in <a href="/realtime/realtimekit/webhooks/#meetingsummary">RealtimeKit webhooks</a> to receive the summary download URL when it is ready:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;event&quot;: &quot;meeting.summary&quot;,&#10;	&quot;meeting&quot;: {&#10;		&quot;id&quot;: &quot;bbb8940e-1b97-402a-97d6-2708b7feca41&quot;,&#10;		&quot;sessionId&quot;: &quot;05e57591-d89e-45c9-ae44-08dc1eaad0e0&quot;,&#10;		&quot;organizedBy&quot;: {&#10;			&quot;id&quot;: &quot;c94c437b-592a-4a39-b9e2-47ef1451e43b&quot;,&#10;			&quot;name&quot;: &quot;Example organization&quot;&#10;		}&#10;	},&#10;	&quot;summaryDownloadUrl&quot;: &quot;https://example.com/summary.txt&quot;,&#10;	&quot;summaryDownloadUrlExpiry&quot;: &quot;2026-06-10T10:30:00.000Z&quot;&#10;}&#10;</code></pre>
<h3 id="rest-api">REST API</h3>
<h4 id="fetch-summary">Fetch summary</h4>
<p>Refer to <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/">Fetch summary of transcripts for a session</a>.</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h4 id="trigger-manually">Trigger manually</h4>
<p>Use the <a href="/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/">Generate summary of transcripts for the session</a> API if <code>summarize_on_end</code> was not set and you want to generate a summary manually after the transcript is available.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h2 id="example-output">Example output</h2>
<p>With <code>text_format: &quot;markdown&quot;</code> and <code>summary_type: &quot;team_meeting&quot;</code>:</p>
<pre tabindex="0"><code class="language-markdown">&#35;# Meeting Summary&#10;&#10;&#35;## Key Discussion Points&#10;&#10;&#45; Reviewed Q4 roadmap priorities&#10;&#45; Discussed deployment timeline for v2.0&#10;&#45; Identified blockers for the auth migration&#10;&#10;&#35;## Action Items&#10;&#10;&#45; @alice: Update design specs by Friday&#10;&#45; @bob: Schedule security review&#10;&#45; @charlie: Create migration runbook&#10;&#10;&#35;## Decisions Made&#10;&#10;&#45; Approved moving forward with Kubernetes migration&#10;&#45; Delayed analytics dashboard to next sprint&#10;</code></pre>
<h2 id="retention">Retention</h2>
<p>Summaries are stored for <strong>7 days</strong> after the meeting ends.</p>
