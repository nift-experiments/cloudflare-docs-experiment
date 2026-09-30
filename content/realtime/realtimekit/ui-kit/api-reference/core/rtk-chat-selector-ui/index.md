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
<td><code>groups</code></td>
<td><code>ChatGroup[]</code></td>
<td>✅</td>
<td>-</td>
<td>Participants</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>selectedGroupId</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Selected participant</td>
</tr>
<tr>
<td><code>selfUserId</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Self User ID</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>unreadCounts</code></td>
<td><code>Record&lt;string, number&gt;</code></td>
<td>✅</td>
<td>-</td>
<td>Unread counts</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-chat-selector-ui&gt;&lt;/rtk-chat-selector-ui&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-chat-selector-ui&#10; selectedGroupId=&quot;example&quot;&#10; selfUserId=&quot;example&quot;&gt;&#10;&lt;/rtk-chat-selector-ui&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-chat-selector-ui&quot;);&#10;&#10;  el.groups= [];&#10;&lt;/script&gt;&#10;</code></pre>
