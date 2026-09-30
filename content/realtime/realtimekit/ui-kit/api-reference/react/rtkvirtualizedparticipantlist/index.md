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
<td><code>bufferedItemsCount</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Buffer items to render before and after the visible area</td>
</tr>
<tr>
<td><code>emptyListElement</code></td>
<td><code>HTMLElement</code></td>
<td>✅</td>
<td>-</td>
<td>Element to render if list is empty</td>
</tr>
<tr>
<td><code>itemHeight</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Height of each item in pixels (assumed fixed)</td>
</tr>
<tr>
<td><code>items</code></td>
<td><code>Peer1[]</code></td>
<td>✅</td>
<td>-</td>
<td>Items to be virtualized</td>
</tr>
<tr>
<td><code>renderItem</code></td>
<td><code>(item: Peer1, index: number)</code></td>
<td>✅</td>
<td>-</td>
<td>Function to render each item</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-tsx">import { RtkVirtualizedParticipantList } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkVirtualizedParticipantList /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkVirtualizedParticipantList } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkVirtualizedParticipantList&#10;      bufferedItemsCount={42}&#10;      emptyListElement={htmlelement}&#10;      itemHeight={42}&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
