<p>A simple grid layout that arranges participant tiles in rows and columns with automatic sizing based on participant count.</p>
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
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit meeting instance</td>
</tr>
<tr>
<td><code>participants</code></td>
<td><code>Peer[]</code></td>
<td>✅</td>
<td>-</td>
<td>Array of participants to display</td>
</tr>
<tr>
<td><code>aspectRatio</code></td>
<td><code>string</code></td>
<td>❌</td>
<td><code>'3:4'</code></td>
<td>Aspect ratio for grid tiles</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>defaultConfig</code></td>
<td>UI configuration object</td>
</tr>
<tr>
<td><code>gap</code></td>
<td><code>number</code></td>
<td>❌</td>
<td><code>8</code></td>
<td>Gap between grid tiles in pixels</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td><code>'sm'</code></td>
<td>Size variant</td>
</tr>
<tr>
<td><code>states</code></td>
<td><code>States</code></td>
<td>❌</td>
<td>-</td>
<td>UI state object</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td>-</td>
<td>i18n translation function</td>
</tr>
<tr>
<td><code>style</code></td>
<td><code>StyleProp&lt;any&gt;</code></td>
<td>❌</td>
<td>-</td>
<td>Custom styles for the grid container</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkSimpleGrid } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkSimpleGrid meeting={meeting} participants={participants} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkSimpleGrid } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkSimpleGrid&#10;			meeting={meeting}&#10;			participants={participants}&#10;			aspectRatio=&quot;16:9&quot;&#10;			gap={12}&#10;			size=&quot;md&quot;&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
