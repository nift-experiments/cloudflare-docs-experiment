<p>@deprecated Use <code>rtk-chat-messages-ui-paginated</code> instead.</p>
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
<td><code>canPinMessages</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Can current user pin/unpin messages</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>messages</code></td>
<td><code>Chat[]</code></td>
<td>✅</td>
<td>-</td>
<td>Chat Messages</td>
</tr>
<tr>
<td><code>selectedGroup</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Selected group key</td>
</tr>
<tr>
<td><code>selfUserId</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>User ID of self user</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size1</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
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
<pre><code class="language-html">&lt;rtk-chat-messages-ui&gt;&lt;/rtk-chat-messages-ui&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-chat-messages-ui&#10; selectedGroup=&quot;example&quot;&gt;&#10;&lt;/rtk-chat-messages-ui&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-chat-messages-ui&quot;);&#10;&#10;  el.canPinMessages= true;&#10;  el.messages= [];&#10;&lt;/script&gt;&#10;</code></pre>
