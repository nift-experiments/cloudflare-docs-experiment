<p>A grid component which handles screenshares, plugins and participants.</p>
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
<td>Aspect Ratio of participant tile  Format: <code>width:height</code></td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>createDefaultConfig()</code></td>
<td>UI Config</td>
</tr>
<tr>
<td><code>gap</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Gap between participant tiles</td>
</tr>
<tr>
<td><code>gridSize</code></td>
<td><code>GridSize1</code></td>
<td>✅</td>
<td>-</td>
<td>Grid size</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon Pack</td>
</tr>
<tr>
<td><code>layout</code></td>
<td><code>GridLayout1</code></td>
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
<td><code>participants</code></td>
<td><code>Peer[]</code></td>
<td>✅</td>
<td>-</td>
<td>Participants</td>
</tr>
<tr>
<td><code>pinnedParticipants</code></td>
<td><code>Peer[]</code></td>
<td>✅</td>
<td>-</td>
<td>Pinned Participants</td>
</tr>
<tr>
<td><code>plugins</code></td>
<td><code>RTKPlugin[]</code></td>
<td>✅</td>
<td>-</td>
<td>Active Plugins</td>
</tr>
<tr>
<td><code>screenShareParticipants</code></td>
<td><code>Peer[]</code></td>
<td>✅</td>
<td>-</td>
<td>Screenshare Participants</td>
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
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-mixed-grid&gt;&lt;/rtk-mixed-grid&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-mixed-grid&#10; aspectRatio=&quot;example&quot;&#10; gap=&quot;42&quot;&#10; gridSize=&quot;md&quot;&gt;&#10;&lt;/rtk-mixed-grid&gt;&#10;</code></pre>
