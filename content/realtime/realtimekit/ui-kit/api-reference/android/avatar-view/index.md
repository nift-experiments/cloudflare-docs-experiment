<p>Avatar component which renders a participant's profile picture or their initials.</p>
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
<td><code>participant: RtkMeetingParticipant</code></td>
<td>Bind the avatar to a participant</td>
</tr>
<tr>
<td><code>refresh</code></td>
<td>-</td>
<td>Refresh the avatar based on the participant's name</td>
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
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.avatarview.RtkAvatarView&#10;    android:id=&quot;@+id/rtk_avatar&quot;&#10;    android:layout_width=&quot;48dp&quot;&#10;    android:layout_height=&quot;48dp&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val avatar = findViewById&lt;RtkAvatarView&gt;(R.id.rtk_avatar)&#10;avatar.activate(participant)&#10;</code></pre>
