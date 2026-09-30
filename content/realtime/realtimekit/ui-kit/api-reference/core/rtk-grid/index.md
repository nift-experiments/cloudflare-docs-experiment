<p>The main grid component which abstracts all the grid handling logic and renders it for you.</p>
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
<td><code>aspectRatio</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>The aspect ratio of each participant</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>createDefaultConfig()</code></td>
<td>Config object</td>
</tr>
<tr>
<td><code>gap</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Gap between participants</td>
</tr>
<tr>
<td><code>gridSize</code></td>
<td><code>GridSize</code></td>
<td>✅</td>
<td>-</td>
<td>Grid size</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>layout</code></td>
<td><code>GridLayout</code></td>
<td>✅</td>
<td>-</td>
<td>Grid Layout</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting object</td>
</tr>
<tr>
<td><code>overrides</code></td>
<td><code>any</code></td>
<td>✅</td>
<td>-</td>
<td>@deprecated</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>states</code></td>
<td><code>States</code></td>
<td>✅</td>
<td>-</td>
<td>States</td>
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
<pre><code class="language-html">&lt;rtk-grid&gt;&lt;/rtk-grid&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-grid&#10; aspectRatio=&quot;example&quot;&#10; gridSize=&quot;md&quot;&gt;&#10;&lt;/rtk-grid&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-grid&quot;);&#10;&#10;  el.gap= 42;&#10;&lt;/script&gt;&#10;</code></pre>
