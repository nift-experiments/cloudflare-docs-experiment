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
<td><code>initialTranscriptions</code></td>
<td><code>Transcript[]</code></td>
<td>✅</td>
<td>-</td>
<td>Initial transcriptions</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting object</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-ai-transcriptions&gt;&lt;/rtk-ai-transcriptions&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-ai-transcriptions&gt;&#10;&lt;/rtk-ai-transcriptions&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-ai-transcriptions&quot;);&#10;&#10;  el.initialTranscriptions= [];&#10;  el.meeting= meeting&#10;&lt;/script&gt;&#10;</code></pre>
