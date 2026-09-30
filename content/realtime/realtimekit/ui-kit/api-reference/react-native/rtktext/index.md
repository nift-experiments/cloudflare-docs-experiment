<p>Themed text component that applies the design system's colors, font family, and font size.</p>
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
<td>Text content</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'sm' | 'md' | 'lg' | 'xl'</code></td>
<td>❌</td>
<td><code>'md'</code></td>
<td>Font size (sm=14, md=16, lg=18, xl=20)</td>
</tr>
<tr>
<td><code>fontWeight</code></td>
<td><code>'normal' | 'bold' | '100' | '200' | '300' | '400' | '500' | '600' | '700' | '800' | '900'</code></td>
<td>❌</td>
<td><code>'normal'</code></td>
<td>Font weight</td>
</tr>
<tr>
<td><code>style</code></td>
<td><code>StyleProp&lt;TextStyle&gt;</code></td>
<td>❌</td>
<td><code>\{\}</code></td>
<td>Custom text styles</td>
</tr>
<tr>
<td><code>onBrand</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Use brand text color instead of default text color</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkText } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkText&gt;Hello World&lt;/RtkText&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkText } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkText size=&quot;lg&quot; fontWeight=&quot;bold&quot; onBrand={true}&gt;&#10;			Meeting Title&#10;		&lt;/RtkText&gt;&#10;	);&#10;}&#10;</code></pre>
