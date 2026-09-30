<p>@deprecated <code>rtk-text-message</code> is deprecated and will be removed soon. Use <code>rtk-text-message-view</code> instead.
A component which renders a text message from chat.</p>
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
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>isContinued</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Whether the message is continued by same user</td>
</tr>
<tr>
<td><code>message</code></td>
<td><code>TextMessage</code></td>
<td>✅</td>
<td>-</td>
<td>Text message object</td>
</tr>
<tr>
<td><code>now</code></td>
<td><code>Date</code></td>
<td>✅</td>
<td>-</td>
<td>Date object of now, to calculate distance between dates</td>
</tr>
<tr>
<td><code>showBubble</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>show message in bubble</td>
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
<pre><code class="language-html">&lt;rtk-text-message&gt;&lt;/rtk-text-message&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-text-message&gt;&#10;&lt;/rtk-text-message&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-text-message&quot;);&#10;&#10;  el.isContinued= true;&#10;&lt;/script&gt;&#10;</code></pre>
