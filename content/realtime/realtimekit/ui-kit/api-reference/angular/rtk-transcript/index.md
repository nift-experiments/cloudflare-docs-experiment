<p>A component which shows a transcript.
You need to remove the element after you receive the
<code>rtkTranscriptDismiss</code> event.</p>
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
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>transcript</code></td>
<td><code>Transcript &amp; { renderedId?: string }</code></td>
<td>❌</td>
<td>-</td>
<td>Message</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-transcript&gt;&lt;/rtk-transcript&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-transcript&#10; [t]=&quot;rtki18n&quot;&#10; transcript=&quot;example&quot;&gt;&#10;&lt;/rtk-transcript&gt;&#10;</code></pre>
