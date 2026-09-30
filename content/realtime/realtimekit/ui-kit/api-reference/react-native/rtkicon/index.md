<p>Renders an SVG icon from an icon string, applying the current theme text color.</p>
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
<td><code>icon</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>SVG icon string to render</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkIcon } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkIcon icon={svgIconString} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import {&#10;	RtkIcon,&#10;	defaultIconPack,&#10;} from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkIcon icon={defaultIconPack.mic_on} /&gt;;&#10;}&#10;</code></pre>
