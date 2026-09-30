<p>@deprecated . This component is deprecated, please use rtk-chat-composer-view instead.</p>
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
<td><code>prefill</code></td>
<td><code>{     suggestedReplies?: string[];     editMessage?: TextMessage;     replyMessage?: TextMessage;   }</code></td>
<td>❌</td>
<td>-</td>
<td>prefill the composer</td>
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
<pre><code class="language-html">&lt;rtk-chat-composer-ui&gt;&lt;/rtk-chat-composer-ui&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-chat-composer-ui&#10; size=&quot;md&quot;&gt;&#10;&lt;/rtk-chat-composer-ui&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-chat-composer-ui&quot;);&#10;&#10;  el.canSendFiles= true;&#10;  el.canSendTextMessage= true;&#10;&lt;/script&gt;&#10;</code></pre>
