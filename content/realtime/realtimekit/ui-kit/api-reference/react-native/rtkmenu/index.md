<p>A menu container component with placement options.</p>
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
<td>Menu content</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>✅</td>
<td>-</td>
<td>Size variant</td>
</tr>
<tr>
<td><code>placement</code></td>
<td><code>'bottom' | 'bottom-end' | 'bottom-start' | 'left' | 'left-end' | 'left-start' | 'right' | 'right-end' | 'right-start' | 'top' | 'top-end' | 'top-start'</code></td>
<td>✅</td>
<td>-</td>
<td>Menu placement relative to trigger</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkMenu } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkMenu size=&quot;md&quot; placement=&quot;bottom&quot;&gt;&#10;			&lt;Text&gt;Menu content&lt;/Text&gt;&#10;		&lt;/RtkMenu&gt;&#10;	);&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkMenu } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkMenu size=&quot;lg&quot; placement=&quot;bottom-start&quot;&gt;&#10;			&lt;Text&gt;Menu content&lt;/Text&gt;&#10;		&lt;/RtkMenu&gt;&#10;	);&#10;}&#10;</code></pre>
