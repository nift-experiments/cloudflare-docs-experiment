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
<td><code>config</code></td>
<td><code>UIConfig1</code></td>
<td>❌</td>
<td><code>createDefaultConfig()</code></td>
<td>Config</td>
</tr>
<tr>
<td><code>hideHeader</code></td>
<td><code>boolean</code></td>
<td>✅</td>
<td>-</td>
<td>Hide Viewer Count Header</td>
</tr>
<tr>
<td><code>iconPack</code></td>
<td><code>IconPack1</code></td>
<td>❌</td>
<td><code>defaultIconPack</code></td>
<td>Icon pack</td>
</tr>
<tr>
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting object</td>
</tr>
<tr>
<td><code>search</code></td>
<td><code>string</code></td>
<td>✅</td>
<td>-</td>
<td>Search</td>
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
<td><code>RtkI18n1</code></td>
<td>❌</td>
<td><code>useLanguage()</code></td>
<td>Language</td>
</tr>
<tr>
<td><code>view</code></td>
<td><code>ParticipantsViewMode</code></td>
<td>✅</td>
<td>-</td>
<td>View mode for participants list</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-html">&lt;rtk-participants-viewer-list&gt;&lt;/rtk-participants-viewer-list&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;rtk-participants-viewer-list&#10; search=&quot;example&quot;&gt;&#10;&lt;/rtk-participants-viewer-list&gt;&#10;</code></pre>
<pre><code class="language-html">&lt;script&gt;&#10;  const el = document.querySelector(&quot;rtk-participants-viewer-list&quot;);&#10;&#10;  el.hideHeader= true;&#10;  el.meeting= meeting&#10;&lt;/script&gt;&#10;</code></pre>
