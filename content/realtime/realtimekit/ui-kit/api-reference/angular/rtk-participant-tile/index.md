<p>A component which plays a participants video and allows for placement
of components like <code>rtk-name-tag</code>, <code>rtk-audio-visualizer</code> or any other component.</p>
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
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>createDefaultConfig()</code></td>
<td>Config object</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>isPreview</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether tile is used for preview</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting object</td>
</tr>
<tr>
<td><code>nameTagPosition</code></td>
<td><code>| 'bottom-left'     | 'bottom-right'     | 'bottom-center'     | 'top-left'     | 'top-right'     | 'top-center'</code></td>
<td>✅</td>
<td>-</td>
<td>Position of name tag</td>
</tr>
<tr>
<td><code>participant</code></td>
<td><code>Peer</code></td>
<td>✅</td>
<td>-</td>
<td>Participant object</td>
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
<td>States object</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>'solid' | 'gradient'</code></td>
<td>✅</td>
<td>-</td>
<td>Variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-participant-tile&gt;&lt;/rtk-participant-tile&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-participant-tile&#10; [isPreview]=&quot;true&quot;&#10; [meeting]=&quot;meeting&quot;&#10; [nameTagPosition]=&quot;| &#x27;bottom-left&#x27;&#10;    | &#x27;bottom-right&#x27;&#10;    | &#x27;bottom-center&#x27;&#10;    | &#x27;top-left&#x27;&#10;    | &#x27;top-right&#x27;&#10;    | &#x27;top-center&#x27;&quot;&gt;&#10;&lt;/rtk-participant-tile&gt;&#10;</code></pre>
