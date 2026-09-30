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
<td><code>maxLength</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>max length of text to render as markdown</td>
</tr>
<tr>
<td><code>text</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>raw text to render as markdown</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-markdown-view&gt;&lt;/rtk-markdown-view&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-markdown-view&#10; text=&quot;example&quot;&gt;&#10;&lt;/rtk-markdown-view&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-markdown-view&quot;);&#10;&#10;  el.maxLength= 42;&#10;&lt;/script&gt;&#10;</code></pre>
