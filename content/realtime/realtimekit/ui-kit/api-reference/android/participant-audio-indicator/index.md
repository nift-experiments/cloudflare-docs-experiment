<p>An audio visualizer component which visualizes a participant's audio.</p>
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
<td>Bind the indicator to a participant</td>
</tr>
<tr>
<td><code>refresh</code></td>
<td>-</td>
<td>Force a refresh of the audio indicator state</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.RtkParticipantAudioIndicator&#10;    android:id=&quot;@+id/audio_indicator&quot;&#10;    android:layout_width=&quot;wrap_content&quot;&#10;    android:layout_height=&quot;wrap_content&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val audioIndicator = findViewById&lt;RtkParticipantAudioIndicator&gt;(R.id.audio_indicator)&#10;audioIndicator.activate(participant)&#10;</code></pre>
