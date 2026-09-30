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
<pre><code class="language-json">{&#10;	&quot;title&quot;: &quot;Team Standup&quot;,&#10;	&quot;transcribe_on_end&quot;: true,&#10;	&quot;summarize_on_end&quot;: true,&#10;	&quot;ai_config&quot;: {&#10;		&quot;transcription&quot;: {&#10;			&quot;language&quot;: &quot;en&quot;&#10;		},&#10;		&quot;summarization&quot;: {&#10;			&quot;word_limit&quot;: 500,&#10;			&quot;text_format&quot;: &quot;markdown&quot;,&#10;			&quot;summary_type&quot;: &quot;team_meeting&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use <code>transcribe_on_end</code> for post-meeting transcripts. Use <code>summarize_on_end</code> for AI-generated summaries. For real-time transcription, make sure participants have <code>transcription_enabled: true</code> in their <a href="/realtime/realtimekit/concepts/preset/">preset</a>.</p>
<h2 id="storage-and-retention">Storage and retention</h2>
<ul>
<li>Transcripts and summaries are stored for <strong>7 days</strong> after the meeting ends</li>
<li>Files are stored in R2 with presigned URLs for secure access</li>
<li>Delivered via <a href="/realtime/realtimekit/webhooks/">webhooks</a> or REST API</li>
</ul>
