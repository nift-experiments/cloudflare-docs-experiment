<p>Displays a logo from a URL (SVG format) in the meeting header.</p>
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
<td><code>any</code></td>
<td>❌</td>
<td>-</td>
<td>The RealtimeKit meeting instance</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>UIConfig</code></td>
<td>❌</td>
<td>-</td>
<td>UI configuration object</td>
</tr>
<tr>
<td><code>logoUrl</code></td>
<td><code>string</code></td>
<td>❌</td>
<td>-</td>
<td>URL of the logo SVG to display</td>
</tr>
<tr>
<td><code>style</code></td>
<td><code>StyleProps</code></td>
<td>❌</td>
<td>-</td>
<td>Style object with width/height for the logo</td>
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
<pre><code class="language-tsx">import { RtkLogo } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkLogo logoUrl=&quot;https://example.com/logo.svg&quot; /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkLogo } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkLogo&#10;			logoUrl=&quot;https://example.com/logo.svg&quot;&#10;			style={{ width: 120, height: 40 }}&#10;			config={customConfig}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
