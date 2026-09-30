<p>The top-level meeting component that orchestrates the entire meeting UI. Manages meeting lifecycle (idle, setup, joined, ended, waiting states), applies design system, handles room join/leave events, and renders the appropriate screen. With this component, you do not have to handle all the states, dialogs, and other smaller bits of managing the application.</p>
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
<td><code>applyDesignSystem</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>true</code></td>
<td>Whether to apply the preset design system colors from the meeting config</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>defaultConfig</code></td>
<td>UI configuration object</td>
</tr>
<tr>
<td><code>iconPackUrl</code></td>
<td><code>string</code></td>
<td>❌</td>
<td><code>''</code></td>
<td>URL to fetch a custom icon pack from</td>
</tr>
<tr>
<td><code>showSetupScreen</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>true</code></td>
<td>Whether to show the setup/preview screen before joining</td>
</tr>
<tr>
<td><code>iOSScreenshareEnabled</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Turn on screenshare on iOS (requires additional native setup)</td>
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
<pre><code class="language-tsx">import { RtkMeeting } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkMeeting meeting={meeting} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkMeeting } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkMeeting&#10;			meeting={meeting}&#10;			applyDesignSystem={true}&#10;			showSetupScreen={true}&#10;			iOSScreenshareEnabled={false}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
