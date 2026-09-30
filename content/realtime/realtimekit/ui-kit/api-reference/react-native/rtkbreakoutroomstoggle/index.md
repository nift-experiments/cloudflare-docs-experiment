<p>Control bar button that opens and closes the <code>RtkBreakoutRoomsManager</code>. Automatically hides if the local participant has neither <code>canAlterConnectedMeetings</code> nor <code>canSwitchConnectedMeetings</code> permission.</p>
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
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td>-</td>
<td>Icon size</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td>-</td>
<td>i18n translation function</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkBreakoutRoomsToggle } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkBreakoutRoomsToggle meeting={meeting} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-size">With Size</h3>
<pre><code class="language-tsx">import { RtkBreakoutRoomsToggle } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkBreakoutRoomsToggle meeting={meeting} size=&quot;md&quot; /&gt;;&#10;}&#10;</code></pre>
