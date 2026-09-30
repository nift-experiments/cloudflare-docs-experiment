<p>A themed text input field component.</p>
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
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether the input is disabled</td>
</tr>
<tr>
<td><code>placeholder</code></td>
<td><code>string</code></td>
<td>❌</td>
<td><code>''</code></td>
<td>Placeholder text</td>
</tr>
<tr>
<td><code>type</code></td>
<td><code>string</code></td>
<td>❌</td>
<td><code>'text'</code></td>
<td>Input type</td>
</tr>
<tr>
<td><code>style</code></td>
<td><code>StyleProp&lt;any&gt;</code></td>
<td>❌</td>
<td>-</td>
<td>Custom styles</td>
</tr>
<tr>
<td><code>onChangeText</code></td>
<td><code>(s: string) =&gt; void</code></td>
<td>❌</td>
<td>-</td>
<td>Callback when text changes</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkTextField } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkTextField placeholder=&quot;Enter your name&quot; /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkTextField } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkTextField&#10;			placeholder=&quot;Enter display name&quot;&#10;			onChangeText={(text) =&gt; setName(text)}&#10;			disabled={false}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
