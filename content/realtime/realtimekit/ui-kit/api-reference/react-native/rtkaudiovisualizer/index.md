<p>Displays an audio visualizer with animated bars representing a participant's audio levels.</p>
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
<td><code>participant</code></td>
<td><code>Peer | RTKParticipant</code></td>
<td>✅</td>
<td>-</td>
<td>The participant whose audio to visualize</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack for icons</td>
</tr>
<tr>
<td><code>isScreenshare</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether this is a screenshare audio visualizer</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td><code>'sm'</code></td>
<td>Size of the visualizer</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>'bar'</code></td>
<td>❌</td>
<td><code>'bar'</code></td>
<td>Visual variant of the visualizer</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkAudioVisualizer } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkAudioVisualizer participant={participant} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkAudioVisualizer } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkAudioVisualizer participant={participant} size=&quot;md&quot; variant=&quot;bar&quot; /&gt;&#10;	);&#10;}&#10;</code></pre>
