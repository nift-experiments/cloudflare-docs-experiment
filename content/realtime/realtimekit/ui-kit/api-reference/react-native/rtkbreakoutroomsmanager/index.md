<p>Full-screen modal for managing breakout rooms. Hosts can create rooms, assign participants, rename rooms, shuffle participants randomly, and start, update, or close a breakout session. Participants without alter permissions see a simplified room-switcher view instead.</p>
<p>The component is visibility-controlled by the <code>activeBreakoutRoomsManager</code> field in the UI state. Use <code>RtkBreakoutRoomsToggle</code> to open it, or set the state directly.</p>
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
<tr>
<td><code>states</code></td>
<td><code>States</code></td>
<td>❌</td>
<td>-</td>
<td>UI state object</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkBreakoutRoomsManager } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkBreakoutRoomsManager meeting={meeting} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-custom-icon-pack">With Custom Icon Pack</h3>
<pre><code class="language-tsx">import { RtkBreakoutRoomsManager } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;import { myIconPack } from &quot;./icons&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkBreakoutRoomsManager meeting={meeting} iconPack={myIconPack} /&gt;;&#10;}&#10;</code></pre>
