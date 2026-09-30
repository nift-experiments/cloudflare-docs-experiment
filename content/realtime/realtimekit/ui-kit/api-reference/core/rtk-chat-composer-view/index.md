<p>A component which renders a chat composer</p>
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
<td><code>canSendFiles</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether user can send file messages</td>
</tr>
<tr>
<td><code>canSendTextMessage</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether user can send text messages</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>inputTextPlaceholder</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Placeholder for text input</td>
</tr>
<tr>
<td><code>isEditing</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Sets composer to edit mode</td>
</tr>
<tr>
<td><code>maxLength</code></td>
<td><code>number</code></td>
<td>✅</td>
<td>-</td>
<td>Max length for text input</td>
</tr>
<tr>
<td><code>message</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Message to be pre-populated</td>
</tr>
<tr>
<td><code>quotedMessage</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Quote message to be displayed</td>
</tr>
<tr>
<td><code>rateLimits</code></td>
<td><code>{ period: number; maxInvocations: number; }</code></td>
<td>✅</td>
<td>-</td>
<td>Rate limits</td>
</tr>
<tr>
<td><code>storageKey</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Key for storing message in localStorage</td>
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
<pre><code class="language-html">&lt;rtk-chat-composer-view&gt;&lt;/rtk-chat-composer-view&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-chat-composer-view&#10; inputTextPlaceholder=&quot;example&quot;&gt;&#10;&lt;/rtk-chat-composer-view&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-chat-composer-view&quot;);&#10;&#10;  el.canSendFiles= true;&#10;  el.canSendTextMessage= true;&#10;&lt;/script&gt;&#10;</code></pre>
