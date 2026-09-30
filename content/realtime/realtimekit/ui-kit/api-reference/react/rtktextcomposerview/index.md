<p>A component which renders a text composer</p>
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
<td>Disable the text input (default = false)</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>keyDownHandler</code></td>
<td><code>(e: KeyboardEvent)</code></td>
<td>✅</td>
<td>-</td>
<td>Keydown event handler function</td>
</tr>
<tr>
<td><code>maxLength</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Max length for text input</td>
</tr>
<tr>
<td><code>placeholder</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Placeholder text</td>
</tr>
<tr>
<td><code>rateLimitBreached</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Boolean to indicate if rate limit is breached</td>
</tr>
<tr>
<td><code>setText</code></td>
<td><code>(text: string, focus?: boolean)</code></td>
<td>❌</td>
<td>-</td>
<td>Sets value of the text input</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n1</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>value</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Default value for text input</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkTextComposerView } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkTextComposerView /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkTextComposerView } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkTextComposerView&#10;      disabled={true}&#10;      keyDownHandler={(e: keyboardevent)}&#10;      maxLength={42}&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
