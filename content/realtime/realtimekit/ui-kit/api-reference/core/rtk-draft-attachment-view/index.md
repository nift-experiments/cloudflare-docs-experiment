<p>A component which renders the draft attachment to send</p>
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
<td><code>attachment</code></td>
<td><code>{     type: 'image' | 'file';     file: File;   }</code></td>
<td>✅</td>
<td>-</td>
<td>Attachment to display</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n1</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-draft-attachment-view&gt;&lt;/rtk-draft-attachment-view&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-draft-attachment-view&gt;&#10;&lt;/rtk-draft-attachment-view&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-draft-attachment-view&quot;);&#10;&#10;  el.attachment= {};&#10;&lt;/script&gt;&#10;</code></pre>
