<p>A complete participant tile view that displays video, avatar, name tag, and pin indicator.
Combines <code>RtkVideoView</code>, <code>RtkAvatarView</code>, and <code>RtkMeetingNameTag</code> into a single composable view.</p>
<h2 id="initializer-parameters">Initializer parameters</h2>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rtkClient</code></td>
<td><code>RealtimeKitClient</code></td>
<td>✅</td>
<td>-</td>
<td>The RealtimeKit client instance</td>
</tr>
<tr>
<td><code>participant</code></td>
<td><code>RtkMeetingParticipant</code></td>
<td>✅</td>
<td>-</td>
<td>The participant to display</td>
</tr>
<tr>
<td><code>isForLocalUser</code></td>
<td><code>Bool</code></td>
<td>✅</td>
<td>-</td>
<td>Whether this tile represents the local user</td>
</tr>
<tr>
<td><code>showScreenShareVideoView</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether to show the screen share video instead of camera video</td>
</tr>
</tbody>
</table>
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
<td><code>nameTag</code></td>
<td><code>RtkMeetingNameTag!</code></td>
<td>-</td>
<td>-</td>
<td>The name tag view displayed on the tile</td>
</tr>
<tr>
<td><code>viewModel</code></td>
<td><code>VideoPeerViewModel</code></td>
<td>-</td>
<td>-</td>
<td>The view model managing participant data (read-only)</td>
</tr>
</tbody>
</table>
<h2 id="methods">Methods</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Return Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pinView(show: Bool)</code></td>
<td><code>Void</code></td>
<td>Shows or hides the pin indicator on the tile</td>
</tr>
<tr>
<td><code>refreshVideo()</code></td>
<td><code>Void</code></td>
<td>Refreshes the video renderer for the participant</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let tileView = RtkParticipantTileView(&#10;    rtkClient: rtkClient,&#10;    participant: participant,&#10;    isForLocalUser: false&#10;)&#10;view.addSubview(tileView)&#10;</code></pre>
<h3 id="local-user-tile-with-screen-share">Local user tile with screen share</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let localTile = RtkParticipantTileView(&#10;    rtkClient: rtkClient,&#10;    participant: localParticipant,&#10;    isForLocalUser: true,&#10;    showScreenShareVideoView: true&#10;)&#10;view.addSubview(localTile)&#10;</code></pre>
