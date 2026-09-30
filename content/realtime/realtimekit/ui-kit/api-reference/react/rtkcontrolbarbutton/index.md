<p>A skeleton component used for composing custom controlbar buttons.</p>
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
<td><code>brandIcon</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether icon requires brand color</td>
</tr>
<tr>
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether button is disabled</td>
</tr>
<tr>
<td><code>icon</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Icon</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>isLoading</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Loading state Ignores current icon and shows a spinner if true</td>
</tr>
<tr>
<td><code>label</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Label of button</td>
</tr>
<tr>
<td><code>showWarning</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to show warning icon</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>ControlBarVariant1</code></td>
<td>✅</td>
<td>-</td>
<td>Variant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkControlbarButton } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkControlbarButton /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkControlbarButton } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkControlbarButton&#10;      brandIcon={true}&#10;      disabled={true}&#10;      icon=&quot;example&quot;&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
