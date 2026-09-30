<p>A reusable button for the control bar with icon, label, loading state, and warning indicator support.</p>
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
<td><code>label</code></td>
<td><code>string</code></td>
<td>✅</td>
<td><code>' '</code></td>
<td>Button label text</td>
</tr>
<tr>
<td><code>icon</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>SVG icon string</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
<tr>
<td><code>isLoading</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Show loading spinner instead of icon</td>
</tr>
<tr>
<td><code>disabled</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether the button is disabled</td>
</tr>
<tr>
<td><code>onClick</code></td>
<td><code>() =&gt; void</code></td>
<td>❌</td>
<td>-</td>
<td>Press handler callback</td>
</tr>
<tr>
<td><code>showWarning</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Show warning indicator</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>'button' | 'horizontal'</code></td>
<td>❌</td>
<td><code>'button'</code></td>
<td>Layout variant</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td><code>'sm'</code></td>
<td>Icon size</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkControlbarButton } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkControlbarButton label=&quot;Mute&quot; icon={muteIcon} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkControlbarButton } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkControlbarButton&#10;			label=&quot;Mute&quot;&#10;			icon={muteIcon}&#10;			variant=&quot;horizontal&quot;&#10;			size=&quot;md&quot;&#10;			onClick={() =&gt; console.log(&quot;pressed&quot;)}&#10;		/&gt;&#10;	);&#10;}&#10;</code></pre>
