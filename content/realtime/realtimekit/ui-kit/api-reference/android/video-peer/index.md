<p>A view that renders a participant's video stream with an avatar fallback when video is disabled.</p>
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
<td><code>refresh</code></td>
<td><code>participant: RtkMeetingParticipant, isScreenShare: Boolean</code></td>
<td>Update the view with the participant data</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkVideoPeer&#10;    android:id=&quot;@+id/rtk_video_peer&quot;&#10;    android:layout_width=&quot;match_parent&quot;&#10;    android:layout_height=&quot;200dp&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val videoPeer = findViewById&lt;RtkVideoPeer&gt;(R.id.rtk_video_peer)&#10;videoPeer.refresh(participant, isScreenShare = false)&#10;</code></pre>
