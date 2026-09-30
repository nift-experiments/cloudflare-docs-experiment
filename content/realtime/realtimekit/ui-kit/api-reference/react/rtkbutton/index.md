<p>A button that follows RTK Design System.</p>
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
<td>✅</td>
<td>-</td>
<td>Where the button is disabled or not</td>
</tr>
<tr>
<td><code>kind</code></td>
<td><code>ButtonKind</code></td>
<td>✅</td>
<td>-</td>
<td>Button type</td>
</tr>
<tr>
<td><code>reverse</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to reverse order of children</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>type</code></td>
<td><code>HTMLButtonElement['type']</code></td>
<td>✅</td>
<td>-</td>
<td>Button type</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>ButtonVariant</code></td>
<td>✅</td>
<td>-</td>
<td>Button variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkButton } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkButton /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkButton } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkButton&#10;      disabled={true}&#10;      kind={buttonkind}&#10;      reverse={true}&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
