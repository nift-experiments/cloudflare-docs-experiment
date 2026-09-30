<p>A component which lists all participants, with ability to
run privileged actions on each participant according to your permissions.</p>
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
<td><code>meeting</code></td>
<td><code>Meeting</code></td>
<td>✅</td>
<td>-</td>
<td>Meeting object</td>
</tr>
<tr>
<td><code>participantIds</code></td>
<td><code>string[]</code></td>
<td>✅</td>
<td>-</td>
<td>Participant ids</td>
</tr>
<tr>
<td><code>selectedParticipantIds</code></td>
<td><code>string[]</code></td>
<td>✅</td>
<td>-</td>
<td>selected participants</td>
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
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-breakout-room-participants&gt;&lt;/rtk-breakout-room-participants&gt;&#10;</code></pre>
<h3 id="with-properties">With Properties</h3>
<pre><code class="language-html">&lt;!-- component.html --&gt;&#10;&lt;rtk-breakout-room-participants&#10; [meeting]=&quot;meeting&quot;&#10; participantIds=&quot;example&quot;&#10; selectedParticipantIds=&quot;example&quot;&gt;&#10;&lt;/rtk-breakout-room-participants&gt;&#10;</code></pre>
