<p>Renders a file message in chat with file name, size, extension, and download button.</p>
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
<td><code>message</code></td>
<td><code>Message</code></td>
<td>✅</td>
<td>-</td>
<td>The chat message object</td>
</tr>
<tr>
<td><code>isContinued</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether this message continues from the same sender</td>
</tr>
<tr>
<td><code>now</code></td>
<td><code>Date</code></td>
<td>❌</td>
<td><code>new Date()</code></td>
<td>Current time for relative timestamps</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkFileMessage } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkFileMessage message={message} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkFileMessage } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return (&#10;		&lt;RtkFileMessage message={message} isContinued={true} now={new Date()} /&gt;&#10;	);&#10;}&#10;</code></pre>
