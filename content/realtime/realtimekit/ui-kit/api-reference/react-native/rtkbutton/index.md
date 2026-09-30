<p>A general-purpose button component with multiple variants and sizes.</p>
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
<td>❌</td>
<td>-</td>
<td>Button content/label</td>
</tr>
<tr>
<td><code>onClick</code></td>
<td><code>any</code></td>
<td>✅</td>
<td>-</td>
<td>Press handler callback</td>
</tr>
<tr>
<td><code>kind</code></td>
<td><code>'button' | 'icon' | 'wide'</code></td>
<td>❌</td>
<td><code>'button'</code></td>
<td>Button kind</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>'danger' | 'ghost' | 'primary' | 'secondary'</code></td>
<td>❌</td>
<td>-</td>
<td>Visual style variant</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td>-</td>
<td>Button size</td>
</tr>
<tr>
<td><code>reverse</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Reverse the button content order</td>
</tr>
<tr>
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td>-</td>
<td>Whether the button is disabled</td>
</tr>
<tr>
<td><code>style</code></td>
<td><code>StyleProp&lt;any&gt;</code></td>
<td>❌</td>
<td>-</td>
<td>Custom React Native styles</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkButton } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkButton onClick={() =&gt; console.log(&quot;pressed&quot;)}&gt;Press Me&lt;/RtkButton&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkButton } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkButton&#10;			onClick={() =&gt; console.log(&quot;pressed&quot;)}&#10;			variant=&quot;primary&quot;&#10;			size=&quot;md&quot;&#10;			kind=&quot;wide&quot;&#10;		&gt;&#10;			Join Meeting&#10;		&lt;/RtkButton&gt;&#10;	);&#10;}&#10;</code></pre>
