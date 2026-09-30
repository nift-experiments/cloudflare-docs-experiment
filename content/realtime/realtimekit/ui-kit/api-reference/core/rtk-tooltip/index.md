<p>Tooltip component which follows RTK Design System.</p>
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
<td><code>delay</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Delay before showing the tooltip</td>
</tr>
<tr>
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Disabled</td>
</tr>
<tr>
<td><code>kind</code></td>
<td><code>TooltipKind</code></td>
<td>✅</td>
<td>-</td>
<td>Tooltip kind</td>
</tr>
<tr>
<td><code>label</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Tooltip label</td>
</tr>
<tr>
<td><code>open</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Open</td>
</tr>
<tr>
<td><code>placement</code></td>
<td><code>Placement</code></td>
<td>✅</td>
<td>-</td>
<td>Placement of menu</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>TooltipVariant</code></td>
<td>✅</td>
<td>-</td>
<td>Tooltip variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-tooltip&gt;&lt;/rtk-tooltip&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-tooltip&gt;&#10;&lt;/rtk-tooltip&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-tooltip&quot;);&#10;&#10;  el.delay= 42;&#10;  el.disabled= true;&#10;&lt;/script&gt;&#10;</code></pre>
