<p>A video tile for a single participant showing their video feed, name tag with audio indicator, avatar (when video is off), and pin indicator.</p>
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
<td><code>participant</code></td>
<td><code>RTKParticipant | RTKSelf</code></td>
<td>✅</td>
<td>-</td>
<td>The participant to render</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>defaultConfig</code></td>
<td>UI configuration object</td>
</tr>
<tr>
<td><code>style</code></td>
<td><code>StyleProp&lt;any&gt;</code></td>
<td>❌</td>
<td>-</td>
<td>Custom styles (typically width/height for grid sizing)</td>
</tr>
<tr>
<td><code>nameTagPosition</code></td>
<td><code>'bottom-center' | 'bottom-left' | 'bottom-right' | 'top-center' | 'top-left' | 'top-right' | 'none'</code></td>
<td>❌</td>
<td><code>'bottom-left'</code></td>
<td>Position of the name tag overlay</td>
</tr>
<tr>
<td><code>isPreview</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether this is a preview tile (setup screen)</td>
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
<td><code>children</code></td>
<td><code>ReactNode</code></td>
<td>❌</td>
<td>-</td>
<td>Additional content to overlay on the tile</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkParticipantTile } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkParticipantTile meeting={meeting} participant={participant} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkParticipantTile } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkParticipantTile&#10;			meeting={meeting}&#10;			participant={participant}&#10;			nameTagPosition=&quot;bottom-left&quot;&#10;			isPreview={false}&#10;			size=&quot;md&quot;&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
