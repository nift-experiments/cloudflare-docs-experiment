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
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-message-list-view&gt;&lt;/rtk-message-list-view&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-message-list-view&#10; estimateItemSize=&quot;42&quot;&#10; [loadMore]=&quot;(lastmessage: message)&quot;&#10; [messages]=&quot;[]&quot;&gt;&#10;&lt;/rtk-message-list-view&gt;&#10;</code></pre>
