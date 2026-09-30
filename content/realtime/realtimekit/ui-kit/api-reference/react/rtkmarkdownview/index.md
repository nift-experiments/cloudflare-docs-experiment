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
<td><code>maxLength</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>max length of text to render as markdown</td>
</tr>
<tr>
<td><code>text</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>raw text to render as markdown</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkMarkdownView } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkMarkdownView /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkMarkdownView } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkMarkdownView&#10;      maxLength={42}&#10;      text=&quot;example&quot;&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
