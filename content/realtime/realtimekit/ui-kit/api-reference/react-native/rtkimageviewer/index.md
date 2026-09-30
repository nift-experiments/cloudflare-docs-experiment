<p>Image viewer with fullscreen toggle and download functionality for chat images.</p>
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
<td><code>image</code></td>
<td><code>any</code></td>
<td>✅</td>
<td>-</td>
<td>The image message object</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>'lg' | 'md' | 'sm' | 'xl'</code></td>
<td>❌</td>
<td>-</td>
<td>Size variant</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Custom icon pack</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td>-</td>
<td>i18n translation function</td>
</tr>
<tr>
<td><code>isContinued</code></td>
<td><code>boolean</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether this message continues from the same sender</td>
</tr>
<tr>
<td><code>_id</code></td>
<td><code>string | number</code></td>
<td>❌</td>
<td>-</td>
<td>Unique identifier for fullscreen tracking</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkImageViewer } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkImageViewer image={imageMessage} /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkImageViewer } from &quot;@cloudflare/realtimekit-react-native-ui&quot;;&#10;&#10;function MyComponent() {&#10;	return &lt;RtkImageViewer image={imageMessage} size=&quot;md&quot; _id=&quot;viewer-1&quot; /&gt;;&#10;}&#10;</code></pre>
