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
<td><code>filter</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>File type filter to open file picker with</td>
</tr>
<tr>
<td><code>icon</code></td>
<td><code>keyof IconPack1</code></td>
<td>✅</td>
<td>-</td>
<td>Icon</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>label</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Label for tooltip</td>
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
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-file-picker-button&gt;&lt;/rtk-file-picker-button&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-file-picker-button&#10; filter=&quot;example&quot;&#10; [icon]=&quot;defaultIconPack&quot;&#10; label=&quot;example&quot;&gt;&#10;&lt;/rtk-file-picker-button&gt;&#10;</code></pre>
