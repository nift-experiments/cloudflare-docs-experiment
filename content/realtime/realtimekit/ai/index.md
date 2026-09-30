---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ai/
  description: Add AI-powered transcription and summarization to RealtimeKit meetings.
  full_title: AI · Cloudflare Realtime docs
  head_html: <title>AI · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Add AI-powered transcription and summarization to RealtimeKit meetings."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ai/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ai/index.md"><meta property="og:title" content="AI · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add AI-powered transcription and summarization to RealtimeKit meetings."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ai/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ai/#page","headline":"AI \u00b7 Cloudflare Realtime docs","description":"Add AI-powered transcription and summarization to RealtimeKit meetings.","url":"https://developers.cloudflare.com/realtime/realtimekit/ai/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ai/
  schema: 1
---
<p>RealtimeKit provides AI-powered features using Cloudflare's AI infrastructure to enhance your meetings with transcription and summarization capabilities.</p>
<ul class="directory-listing"><li><a href="/realtime/realtimekit/ai/transcription/">Transcription</a></li><li><a href="/realtime/realtimekit/ai/summary/">Summary</a></li></ul>
<h2 id="available-features">Available features</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/realtime/realtimekit/ai/transcription/">Transcription</a></td>
<td>Real-time and post-meeting speech-to-text</td>
</tr>
<tr>
<td><a href="/realtime/realtimekit/ai/summary/">Summary</a></td>
<td>AI-generated meeting summaries</td>
</tr>
</tbody>
</table>
<h2 id="quick-start">Quick start</h2>
<p>Turn on post-meeting transcription and automatic summaries when creating a meeting:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;title&quot;: &quot;Team Standup&quot;,&#10;	&quot;transcribe_on_end&quot;: true,&#10;	&quot;summarize_on_end&quot;: true,&#10;	&quot;ai_config&quot;: {&#10;		&quot;transcription&quot;: {&#10;			&quot;language&quot;: &quot;en&quot;&#10;		},&#10;		&quot;summarization&quot;: {&#10;			&quot;word_limit&quot;: 500,&#10;			&quot;text_format&quot;: &quot;markdown&quot;,&#10;			&quot;summary_type&quot;: &quot;team_meeting&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use <code>transcribe_on_end</code> for post-meeting transcripts. Use <code>summarize_on_end</code> for AI-generated summaries. For real-time transcription, make sure participants have <code>transcription_enabled: true</code> in their <a href="/realtime/realtimekit/concepts/preset/">preset</a>.</p>
<h2 id="storage-and-retention">Storage and retention</h2>
<ul>
<li>Transcripts and summaries are stored for <strong>7 days</strong> after the meeting ends</li>
<li>Files are stored in R2 with presigned URLs for secure access</li>
<li>Delivered via <a href="/realtime/realtimekit/webhooks/">webhooks</a> or REST API</li>
</ul>
