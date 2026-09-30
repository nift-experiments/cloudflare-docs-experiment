<p>A switch component which follows RTK Design System.</p>
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
<td><code>checked</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether the switch is enabled/checked</td>
</tr>
<tr>
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether switch is readonly</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>readonly</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether switch is readonly</td>
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
<pre><code class="language-html">&lt;rtk-switch&gt;&lt;/rtk-switch&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-switch&gt;&#10;&lt;/rtk-switch&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-switch&quot;);&#10;&#10;  el.checked= true;&#10;  el.disabled= true;&#10;  el.readonly= true;&#10;&lt;/script&gt;&#10;</code></pre>
