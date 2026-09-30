<p>A horizontal list container for menu items.</p>
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
<td>Menu list content</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import {&#10;	RtkMenuList,&#10;	RtkMenuItem,&#10;} from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkMenuList&gt;&#10;			&lt;RtkMenuItem onClick={() =&gt; {}}&gt;&#10;				&lt;Text&gt;Item 1&lt;/Text&gt;&#10;			&lt;/RtkMenuItem&gt;&#10;			&lt;RtkMenuItem onClick={() =&gt; {}}&gt;&#10;				&lt;Text&gt;Item 2&lt;/Text&gt;&#10;			&lt;/RtkMenuItem&gt;&#10;		&lt;/RtkMenuList&gt;&#10;	);&#10;}&#10;</code></pre>
