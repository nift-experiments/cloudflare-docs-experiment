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
<td><code>actions</code></td>
<td><code>MessageAction[]</code></td>
<td>✅</td>
<td>-</td>
<td>List of actions to show in menu</td>
</tr>
<tr>
<td><code>authorName</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Author display label</td>
</tr>
<tr>
<td><code>avatarUrl</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Avatar image url</td>
</tr>
<tr>
<td><code>hideAuthorName</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hides author display label</td>
</tr>
<tr>
<td><code>hideAvatar</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hides avatar</td>
</tr>
<tr>
<td><code>hideMetadata</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hides metadata (time)</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>isEdited</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Has the message been edited</td>
</tr>
<tr>
<td><code>isSelf</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Is the message sent by the current user</td>
</tr>
<tr>
<td><code>messageType</code></td>
<td><code>Message['type']</code></td>
<td>✅</td>
<td>-</td>
<td>Type of message</td>
</tr>
<tr>
<td><code>pinned</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Is message pinned</td>
</tr>
<tr>
<td><code>time</code></td>
<td><code>Date</code></td>
<td>✅</td>
<td>-</td>
<td>Time when message was sent</td>
</tr>
<tr>
<td><code>variant</code></td>
<td><code>'plain' | 'bubble'</code></td>
<td>✅</td>
<td>-</td>
<td>Appearance</td>
</tr>
<tr>
<td><code>viewType</code></td>
<td><code>'incoming' | 'outgoing'</code></td>
<td>✅</td>
<td>-</td>
<td>Render</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-message-view&gt;&lt;/rtk-message-view&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-message-view&#10; [actions]=&quot;[]&quot;&#10; authorName=&quot;example&quot;&#10; avatarUrl=&quot;example&quot;&gt;&#10;&lt;/rtk-message-view&gt;&#10;</code></pre>
