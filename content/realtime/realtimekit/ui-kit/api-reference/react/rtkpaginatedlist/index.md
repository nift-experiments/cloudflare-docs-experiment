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
<td><code>autoScroll</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>auto scroll list to bottom</td>
</tr>
<tr>
<td><code>createNodes</code></td>
<td><code>(data: unknown[])</code></td>
<td>✅</td>
<td>-</td>
<td>Create nodes</td>
</tr>
<tr>
<td><code>emptyListLabel</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>label to show when empty</td>
</tr>
<tr>
<td><code>fetchData</code></td>
<td><code>(timestamp: number, size: number, reversed: boolean)</code></td>
<td>✅</td>
<td>-</td>
<td>Fetch the data</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>pageSize</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Page Size</td>
</tr>
<tr>
<td><code>pagesAllowed</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Number of pages allowed to be shown</td>
</tr>
<tr>
<td><code>rerenderList</code></td>
<td><code>()</code></td>
<td>✅</td>
<td>-</td>
<td>Rerender paginated list</td>
</tr>
<tr>
<td><code>reset</code></td>
<td><code>(timestamp?: number)</code></td>
<td>❌</td>
<td>-</td>
<td>Resets the paginated list to a given timestamp</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkPaginatedList } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkPaginatedList /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkPaginatedList } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkPaginatedList&#10;      autoScroll={true}&#10;      createNodes={[]}&#10;      emptyListLabel=&quot;example&quot;&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
