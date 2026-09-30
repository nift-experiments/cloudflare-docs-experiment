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
<td><code>config</code></td>
<td><code>UIConfig1</code></td>
<td>✅</td>
<td>-</td>
<td>Config</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting | null</code></td>
<td>❌</td>
<td><code>null</code></td>
<td>Meeting</td>
</tr>
<tr>
<td><code>mode</code></td>
<td><code>MeetingMode1</code></td>
<td>✅</td>
<td>-</td>
<td>Fill type</td>
</tr>
<tr>
<td><code>overrides</code></td>
<td><code>Overrides1</code></td>
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
<td><code>t</code></td>
<td><code>RtkI18n1</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language utility</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkUiProvider } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkUiProvider /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkUiProvider } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkUiProvider&#10;      config={defaultUiConfig}&#10;      mode={meeting}&#10;      showSetupScreen={true}&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
