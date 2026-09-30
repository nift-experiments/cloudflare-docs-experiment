<p>A modal dialog overlay component with optional close button.</p>
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
<td><code>children</code></td>
<td><code>ReactNode</code></td>
<td>✅</td>
<td>-</td>
<td>Dialog content</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit meeting instance</td>
</tr>
<tr>
<td><code>onRtkDialogClose</code></td>
<td><code>any</code></td>
<td>✅</td>
<td>-</td>
<td>Callback when dialog is closed</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td><code>defaultConfig</code></td>
<td>UI configuration object</td>
</tr>
<tr>
<td><code>hideCloseButton</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Hide the close button</td>
</tr>
<tr>
<td><code>open</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td>-</td>
<td>Whether the dialog is visible</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td>-</td>
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
<pre><code class="language-tsx">import { RtkDialog } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkDialog meeting={meeting} onRtkDialogClose={() =&gt; setOpen(false)}&gt;&#10;			&lt;Text&gt;Dialog content&lt;/Text&gt;&#10;		&lt;/RtkDialog&gt;&#10;	);&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkDialog } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkDialog&#10;			meeting={meeting}&#10;			open={isOpen}&#10;			onRtkDialogClose={() =&gt; setOpen(false)}&#10;			hideCloseButton={false}&#10;			size=&quot;md&quot;&#10;		&gt;&#10;			&lt;Text&gt;Dialog content&lt;/Text&gt;&#10;		&lt;/RtkDialog&gt;&#10;	);&#10;}&#10;</code></pre>
