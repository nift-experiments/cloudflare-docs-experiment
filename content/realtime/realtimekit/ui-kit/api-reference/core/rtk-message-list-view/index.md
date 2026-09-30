<p>A component which renders list of messages.</p>
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
<td><code>estimateItemSize</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Estimated height of an item</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>loadMore</code></td>
<td><code>(lastMessage: Message)</code></td>
<td>✅</td>
<td>-</td>
<td>Function to load more messages. Messages returned from this will be prepended</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>Message[]</code></td>
<td>✅</td>
<td>-</td>
<td>Messages to render</td>
</tr>
<tr>
<td><code>renderer</code></td>
<td><code>(message: Message, index: number)</code></td>
<td>✅</td>
<td>-</td>
<td>Render function of the message</td>
</tr>
<tr>
<td><code>visibleItemsCount</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Maximum visible messages</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-message-list-view&gt;&lt;/rtk-message-list-view&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-message-list-view&gt;&#10;&lt;/rtk-message-list-view&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-message-list-view&quot;);&#10;&#10;  el.estimateItemSize= 42;&#10;  el.messages= [];&#10;&lt;/script&gt;&#10;</code></pre>
