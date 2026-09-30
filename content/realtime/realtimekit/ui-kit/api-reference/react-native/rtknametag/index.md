<p>Displays a participant's name with optional child content (such as an audio visualizer icon). Used as an overlay on participant tiles.</p>
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
<td>The participant to display the name for</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>❌</td>
<td>-</td>
<td>The RealtimeKit meeting instance (used to identify self)</td>
</tr>
<tr>
<td><code>isScreenshare</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether this is a screenshare name tag</td>
</tr>
<tr>
<td><code>maxLength</code></td>
<td><code>number</code></td>
<td>❌</td>
<td><code>20</code></td>
<td>Maximum width offset for the name tag</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td><code>'sm'</code></td>
<td>Text size</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td>-</td>
<td>i18n translation function</td>
</tr>
<tr>
<td><code>children</code></td>
<td><code>ReactNode</code></td>
<td>❌</td>
<td>-</td>
<td>Content to render before the name</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkNameTag } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkNameTag participant={participant} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkNameTag } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkNameTag&#10;			participant={participant}&#10;			meeting={meeting}&#10;			size=&quot;md&quot;&#10;			maxLength={25}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
