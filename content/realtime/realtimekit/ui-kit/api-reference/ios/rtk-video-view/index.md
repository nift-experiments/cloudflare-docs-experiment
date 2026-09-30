<p>Renders a participant's video stream.
Supports self-preview, remote participant video, and screen share rendering.</p>
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
<td><code>participant</code></td>
<td><code>RtkMeetingParticipant</code></td>
<td>✅</td>
<td>-</td>
<td>The participant whose video to render</td>
</tr>
<tr>
<td><code>showSelfPreview</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether to show the local camera preview</td>
</tr>
<tr>
<td><code>showScreenShare</code></td>
<td><code>Bool</code></td>
<td>❌</td>
<td><code>false</code></td>
<td>Whether to show the screen share stream instead of camera</td>
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
<td><code>reattachRenderer()</code></td>
<td><code>Void</code></td>
<td>Reattaches the video renderer to the participant stream</td>
</tr>
<tr>
<td><code>prepareForReuse()</code></td>
<td><code>Void</code></td>
<td>Prepares the view for reuse in a collection or table view</td>
</tr>
<tr>
<td><code>clean()</code></td>
<td><code>Void</code></td>
<td>Releases the video renderer and cleans up resources</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let videoView = RtkVideoView(participant: participant)&#10;view.addSubview(videoView)&#10;</code></pre>
<h3 id="self-preview">Self-preview</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let previewView = RtkVideoView(&#10;    participant: localParticipant,&#10;    showSelfPreview: true&#10;)&#10;view.addSubview(previewView)&#10;</code></pre>
<h3 id="screen-share">Screen share</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let screenShareView = RtkVideoView(&#10;    participant: participant,&#10;    showScreenShare: true&#10;)&#10;view.addSubview(screenShareView)&#10;</code></pre>
