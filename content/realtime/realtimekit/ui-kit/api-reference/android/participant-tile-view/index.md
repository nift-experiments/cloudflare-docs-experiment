<p>A component which plays a participant's video and allows for placement of components like name tag and avatar.</p>
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
<td><code>rtk_ptv_nameTagPosition</code></td>
<td><code>BOTTOM_LEFT | TOP_CENTER</code></td>
<td>❌</td>
<td><code>BOTTOM_LEFT</code></td>
<td>Position of the name tag</td>
</tr>
<tr>
<td><code>cardBackgroundColor</code></td>
<td><code>color</code></td>
<td>❌</td>
<td>-</td>
<td>Background color of the tile</td>
</tr>
<tr>
<td><code>cardCornerRadius</code></td>
<td><code>dimension</code></td>
<td>❌</td>
<td>-</td>
<td>Corner radius of the tile</td>
</tr>
</tbody>
</table>
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
<td>Bind the tile to a specific participant</td>
</tr>
<tr>
<td><code>refreshParticipantName</code></td>
<td>-</td>
<td>Refresh the name tag and avatar</td>
</tr>
<tr>
<td><code>refreshParticipantVideo</code></td>
<td>-</td>
<td>Refresh the video view state</td>
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
<pre><code class="language-xml">&lt;com.cloudflare.realtimekit.ui.view.participanttile.RtkParticipantTileView&#10;    android:id=&quot;@+id/rtk_participant_tile&quot;&#10;    android:layout_width=&quot;match_parent&quot;&#10;    android:layout_height=&quot;200dp&quot;&#10;    app:rtk_ptv_nameTagPosition=&quot;BOTTOM_LEFT&quot; /&gt;&#10;</code></pre>
<h3 id="with-methods">With Methods</h3>
<pre><code class="language-kotlin">val tile = findViewById&lt;RtkParticipantTileView&gt;(R.id.rtk_participant_tile)&#10;tile.activate(participant)&#10;</code></pre>
