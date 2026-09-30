<p>@deprecated <code>rtk-chat-message</code> is deprecated and will be removed soon. Use <code>rtk-message-view</code> instead.</p>
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
<td><code>alignRight</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>aligns message to right</td>
</tr>
<tr>
<td><code>canDelete</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>can delete message</td>
</tr>
<tr>
<td><code>canEdit</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>can edit message</td>
</tr>
<tr>
<td><code>canPin</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>can pin this message</td>
</tr>
<tr>
<td><code>canReply</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>can quote reply this message</td>
</tr>
<tr>
<td><code>child</code></td>
<td><code>HTMLElement</code></td>
<td>✅</td>
<td>-</td>
<td>Child</td>
</tr>
<tr>
<td><code>disableControls</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>disables controls</td>
</tr>
<tr>
<td><code>hideAvatar</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>hides avatar</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>isContinued</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>is continued</td>
</tr>
<tr>
<td><code>isSelf</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>if sender is self</td>
</tr>
<tr>
<td><code>isUnread</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>is unread</td>
</tr>
<tr>
<td><code>leftAlign</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether to left align the chat bubbles</td>
</tr>
<tr>
<td><code>message</code></td>
<td><code>Message</code></td>
<td>✅</td>
<td>-</td>
<td>message item</td>
</tr>
<tr>
<td><code>senderDisplayPicture</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>sender display picture url</td>
</tr>
<tr>
<td><code>size</code></td>
<td><code>Size</code></td>
<td>✅</td>
<td>-</td>
<td>Size</td>
</tr>
<tr>
<td><code>t</code></td>
<td><code>RtkI18n1</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-chat-message&gt;&lt;/rtk-chat-message&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-chat-message&#10; [alignRight]=&quot;true&quot;&#10; [canDelete]=&quot;true&quot;&#10; [canEdit]=&quot;true&quot;&gt;&#10;&lt;/rtk-chat-message&gt;&#10;</code></pre>
