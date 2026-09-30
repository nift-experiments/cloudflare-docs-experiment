<p>A waiting participant card with accept/reject buttons for waitlist and stage request management.</p>
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
<td><code>Peer</code></td>
<td>✅</td>
<td>-</td>
<td>The waiting participant</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>❌</td>
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
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkParticipantWaiting } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkParticipantWaiting participant={waitingParticipant} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkParticipantWaiting } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkParticipantWaiting&#10;			participant={waitingParticipant}&#10;			meeting={meeting}&#10;			iconPack={customIconPack}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
