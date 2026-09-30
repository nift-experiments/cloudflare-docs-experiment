<p>Loading/idle screen displayed while the meeting is initializing, showing a logo and spinner.</p>
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
<td><code>UIConfig</code></td>
<td>✅</td>
<td>-</td>
<td>UI configuration object (used for logo URL)</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkIdleScreen } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkIdleScreen config={config} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import {&#10;	RtkIdleScreen,&#10;	defaultConfig,&#10;} from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkIdleScreen config={defaultConfig} /&gt;;&#10;}&#10;</code></pre>
