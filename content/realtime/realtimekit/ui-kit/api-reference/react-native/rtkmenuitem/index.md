<p>A pressable menu item within a menu.</p>
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
<td>Menu item content</td>
</tr>
<tr>
<td><code>onClick</code></td>
<td><code>(ev) =&gt; {}</code></td>
<td>❌</td>
<td>-</td>
<td>Press handler callback</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td>-</td>
<td>Size variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkMenuItem } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkMenuItem onClick={() =&gt; ({})}&gt;&#10;			&lt;Text&gt;Option 1&lt;/Text&gt;&#10;		&lt;/RtkMenuItem&gt;&#10;	);&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkMenuItem } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkMenuItem onClick={(ev) =&gt; ({})} size=&quot;md&quot;&gt;&#10;			&lt;Text&gt;Option 1&lt;/Text&gt;&#10;		&lt;/RtkMenuItem&gt;&#10;	);&#10;}&#10;</code></pre>
