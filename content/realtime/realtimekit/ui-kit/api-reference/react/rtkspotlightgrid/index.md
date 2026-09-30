<p>A grid component that renders two lists of participants: <code>pinnedParticipants</code> and <code>participants</code>.
You can customize the layout to a <code>column</code> view, by default is <code>row</code>.</p>
<ul>
<li>Participants from <code>pinnedParticipants[]</code> are rendered inside a larger grid.</li>
<li>Participants from <code>participants[]</code> array are rendered in a smaller grid.</li>
</ul>
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
<pre><code class="language-tsx">import { RtkSpotlightGrid } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkSpotlightGrid /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkSpotlightGrid } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkSpotlightGrid&#10;      aspectRatio=&quot;example&quot;&#10;      gap={42}&#10;      gridSize=&quot;md&quot;&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
