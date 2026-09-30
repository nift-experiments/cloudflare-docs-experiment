<p>Displays a participant's avatar image or initials-based fallback avatar.</p>
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
<td><code>RTKParticipant | RTKSelf</code></td>
<td>✅</td>
<td>-</td>
<td>The participant whose avatar to display</td>
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
<td>Size of the avatar</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>'circular' | 'hexagon' | 'square'</code></td>
<td>❌</td>
<td><code>'circular'</code></td>
<td>Shape variant of the avatar</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkAvatar } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkAvatar participant={participant} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkAvatar } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkAvatar participant={participant} size=&quot;lg&quot; variant=&quot;circular&quot; /&gt;;&#10;}&#10;</code></pre>
