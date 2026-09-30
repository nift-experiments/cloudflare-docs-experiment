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
<td><code>allowDelete</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>allow room delete</td>
</tr>
<tr>
<td><code>assigningParticipants</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Enable updating participants</td>
</tr>
<tr>
<td><code>defaultExpanded</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>display expanded card by default</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>isDragMode</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Drag mode</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting object</td>
</tr>
<tr>
<td><code>mode</code></td>
<td><code>'edit' | 'create'</code></td>
<td>✅</td>
<td>-</td>
<td>Mode in which selector is used</td>
</tr>
<tr>
<td><code>room</code></td>
<td><code>DraftMeeting</code></td>
<td>✅</td>
<td>-</td>
<td>Connected Room Config Object</td>
</tr>
<tr>
<td><code>states</code></td>
<td><code>States</code></td>
<td>✅</td>
<td>-</td>
<td>States object</td>
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
<pre><code class="language-html">&lt;rtk-breakout-room-manager&gt;&lt;/rtk-breakout-room-manager&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-breakout-room-manager&gt;&#10;&lt;/rtk-breakout-room-manager&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-breakout-room-manager&quot;);&#10;&#10;  el.allowDelete= true;&#10;  el.assigningParticipants= true;&#10;  el.defaultExpanded= true;&#10;&lt;/script&gt;&#10;</code></pre>
