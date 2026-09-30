<p>A component which renders a text message from chat.</p>
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
<td><code>isMarkdown</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Renders text as markdown (default = true)</td>
</tr>
<tr>
<td><code>text</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Text message</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-text-message-view&gt;&lt;/rtk-text-message-view&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-text-message-view&#10; text=&quot;example&quot;&gt;&#10;&lt;/rtk-text-message-view&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-text-message-view&quot;);&#10;&#10;  el.isMarkdown= true;&#10;&lt;/script&gt;&#10;</code></pre>
