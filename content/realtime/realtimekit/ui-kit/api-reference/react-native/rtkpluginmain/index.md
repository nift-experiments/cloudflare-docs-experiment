<p>Renders an active plugin by loading <code>plugin.component.src</code> in a <code>WebView</code>. Includes a header bar with the plugin name, a fullscreen toggle, and an optional close button (shown when <code>plugin.permissions.canDeactivate</code> is <code>true</code>). Pressing close calls <code>plugin.deactivate()</code>.</p>
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
<td><code>plugin</code></td>
<td><code>RTKPlugin</code></td>
<td>✅</td>
<td>-</td>
<td>The plugin to render</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkPluginMain } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkPluginMain meeting={meeting} plugin={activePlugin} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkPluginMain } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkPluginMain&#10;			meeting={meeting}&#10;			plugin={activePlugin}&#10;			iconPack={customIconPack}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
