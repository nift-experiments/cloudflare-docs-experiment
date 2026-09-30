<p>Displays a participant's name and an audio indicator.</p>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>activate</code></td>
<td><code>participant: RtkMeetingParticipant, isScreenShare: Boolean</code></td>
<td>Bind the name tag to a participant</td>
</tr>
<tr>
<td><code>setMaxLength</code></td>
<td><code>length: Int</code></td>
<td>Set the maximum length for the displayed name</td>
</tr>
<tr>
<td><code>refresh</code></td>
<td>-</td>
<td>Refresh the name and audio indicator</td>
</tr>
<tr>
<td><code>applyDesignTokens</code></td>
<td><code>designTokens: RtkDesignTokens</code></td>
<td>Apply custom design tokens for theming</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.nametagview.RtkNameTagView&#10;    android:id=&quot;@+id/rtk_name_tag&quot;&#10;    android:layout_width=&quot;wrap_content&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val nameTag = findViewById&lt;RtkNameTagView&gt;(R.id.rtk_name_tag)&#10;nameTag.activate(participant)&#10;</code></pre>
