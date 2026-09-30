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
<pre><code class="language-html">&lt;rtk-virtualized-participant-list&gt;&lt;/rtk-virtualized-participant-list&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-virtualized-participant-list&gt;&#10;&lt;/rtk-virtualized-participant-list&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-virtualized-participant-list&quot;);&#10;&#10;  el.bufferedItemsCount= 42;&#10;  el.itemHeight= 42;&#10;&lt;/script&gt;&#10;</code></pre>
