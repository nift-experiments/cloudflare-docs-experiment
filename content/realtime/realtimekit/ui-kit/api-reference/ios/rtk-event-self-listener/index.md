<p>A helper class that wraps self-participant and meeting event listeners with closure-based callbacks.
Provides methods for toggling audio and video, observing state changes, and checking device permissions.</p>
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
<td><code>identifier</code></td>
<td><code>String</code></td>
<td>❌</td>
<td><code>&quot;Default&quot;</code></td>
<td>A unique identifier for this listener instance</td>
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
<td><code>toggleLocalAudio(completion:)</code></td>
<td><code>Void</code></td>
<td>Toggles the local microphone on or off</td>
</tr>
<tr>
<td><code>toggleLocalVideo(completion:)</code></td>
<td><code>Void</code></td>
<td>Toggles the local camera on or off</td>
</tr>
<tr>
<td><code>observeSelfVideo(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for local video state changes</td>
</tr>
<tr>
<td><code>observeSelfAudio(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for local audio state changes</td>
</tr>
<tr>
<td><code>observeSelfRemoved(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for when the local participant is removed</td>
</tr>
<tr>
<td><code>observeSelfMeetingEndForAll(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for when the meeting ends for all participants</td>
</tr>
<tr>
<td><code>observeWebinarStageStatus(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for webinar stage status changes</td>
</tr>
<tr>
<td><code>observeRequestToJoinStage(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for stage join request events</td>
</tr>
<tr>
<td><code>observeSelfPermissionChanged(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for permission changes on the local participant</td>
</tr>
<tr>
<td><code>observeMeetingReconnectionState(update:)</code></td>
<td><code>Void</code></td>
<td>Registers a callback for meeting reconnection state changes</td>
</tr>
<tr>
<td><code>isCameraPermissionGranted()</code></td>
<td><code>Bool</code></td>
<td>Returns whether camera permission is granted</td>
</tr>
<tr>
<td><code>isMicrophonePermissionGranted()</code></td>
<td><code>Bool</code></td>
<td>Returns whether microphone permission is granted</td>
</tr>
<tr>
<td><code>clean()</code></td>
<td><code>Void</code></td>
<td>Removes all registered listeners and cleans up resources</td>
</tr>
</tbody>
</table>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let listener = RtkEventSelfListener(rtkClient: rtkClient)&#10;&#10;listener.observeSelfAudio { isEnabled in&#10;    print(&quot;Audio enabled: \(isEnabled)&quot;)&#10;}&#10;&#10;listener.observeSelfVideo { isEnabled in&#10;    print(&quot;Video enabled: \(isEnabled)&quot;)&#10;}&#10;</code></pre>
<h3 id="toggle-audio-and-video">Toggle audio and video</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let listener = RtkEventSelfListener(rtkClient: rtkClient)&#10;&#10;listener.toggleLocalAudio { success in&#10;    print(&quot;Audio toggled: \(success)&quot;)&#10;}&#10;&#10;listener.toggleLocalVideo { success in&#10;    print(&quot;Video toggled: \(success)&quot;)&#10;}&#10;</code></pre>
<h3 id="observe-meeting-end">Observe meeting end</h3>
<pre><code class="language-swift">import RealtimeKitUI&#10;&#10;let listener = RtkEventSelfListener(&#10;    rtkClient: rtkClient,&#10;    identifier: &quot;MeetingObserver&quot;&#10;)&#10;&#10;listener.observeSelfRemoved {&#10;    print(&quot;Removed from meeting&quot;)&#10;}&#10;&#10;listener.observeSelfMeetingEndForAll {&#10;    print(&quot;Meeting ended for all&quot;)&#10;}&#10;</code></pre>
