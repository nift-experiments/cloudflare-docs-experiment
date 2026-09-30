<p>A component which renders a file message.</p>
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
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>name</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Name of the file</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Size of the file</td>
</tr>
<tr>
<td><code>url</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Url of the file</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-file-message-view&gt;&lt;/rtk-file-message-view&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-file-message-view&#10; name=&quot;example&quot;&#10; url=&quot;example&quot;&gt;&#10;&lt;/rtk-file-message-view&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-file-message-view&quot;);&#10;&#10;  el.size= 42;&#10;&lt;/script&gt;&#10;</code></pre>
