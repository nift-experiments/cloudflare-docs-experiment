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
<pre><code class="language-tsx">import { RtkBreakoutRoomManager } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return &lt;RtkBreakoutRoomManager /&gt;;&#10;}&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-tsx">import { RtkBreakoutRoomManager } from &#x27;@cloudflare/realtimekit-react-ui&#x27;;&#10;&#10;function MyComponent() {&#10;  return (&#10;    &lt;RtkBreakoutRoomManager&#10;      allowDelete={true}&#10;      assigningParticipants={true}&#10;      defaultExpanded={true}&#10;    /&gt;&#10;  );&#10;}&#10;</code></pre>
