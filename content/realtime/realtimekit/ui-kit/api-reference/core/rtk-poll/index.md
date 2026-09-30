<p>A poll component.
Shows a poll where a user can vote.</p>
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
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>permissions</code></td>
<td><code>RTKPermissionsPreset</code></td>
<td>✅</td>
<td>-</td>
<td>Permissions Object</td>
</tr>
<tr>
<td><code>poll</code></td>
<td><code>Poll</code></td>
<td>✅</td>
<td>-</td>
<td>Poll</td>
</tr>
<tr>
<td><code>self</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Self ID</td>
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
<pre><code class="language-html">&lt;rtk-poll&gt;&lt;/rtk-poll&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-poll&#10; self=&quot;example&quot;&gt;&#10;&lt;/rtk-poll&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-poll&quot;);&#10;&#10;&lt;/script&gt;&#10;</code></pre>
