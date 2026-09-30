<p>A single component which renders an entire meeting UI.
It loads your preset and renders the UI based on it.
With this component, you don't have to handle all the states,
dialogs and other smaller bits of managing the application.</p>
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
<td><code>applyDesignSystem</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to apply the design system on the document root from config</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>✅</td>
<td>-</td>
<td>UI Config</td>
</tr>
<tr>
<td><code>gridLayout</code></td>
<td><code>GridLayout1</code></td>
<td>✅</td>
<td>-</td>
<td>Grid layout</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>leaveOnUnmount</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether participant should leave when this component gets unmounted</td>
</tr>
<tr>
<td><code>loadConfigFromPreset</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to load config from preset</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting object</td>
</tr>
<tr>
<td><code>mode</code></td>
<td><code>MeetingMode</code></td>
<td>✅</td>
<td>-</td>
<td>Fill type</td>
</tr>
<tr>
<td><code>overrides</code></td>
<td><code>Overrides</code></td>
<td>❌</td>
<td><code>defaultOverrides</code></td>
<td>UI Kit Overrides</td>
</tr>
<tr>
<td><code>showSetupScreen</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to show setup screen or not</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
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
<pre><code class="language-tsx">import { RtkMeeting } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkMeeting /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkMeeting } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkMeeting&#10;      applyDesignSystem={true}&#10;      config={defaultUiConfig}&#10;      gridLayout={gridlayout1}&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
