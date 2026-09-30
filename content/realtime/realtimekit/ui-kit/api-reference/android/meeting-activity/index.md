<p>The main meeting activity that manages the full meeting lifecycle. Handles transitions between loading, setup, waiting room, group call, webinar, and error states. This is the activity launched by <code>RealtimeKitUI.startMeeting()</code>.</p>
<h2 id="usage-examples">Usage Examples</h2>
<h3 id="basic-usage">Basic Usage</h3>
<pre><code class="language-kotlin">val meetingInfo = RtkMeetingInfo(authToken = authToken, baseUrl = baseUrl)&#10;val realtimeKitUIInfo = RealtimeKitUIInfo(activity = this, rtkMeetingInfo = meetingInfo)&#10;val realtimeKitUI = RealtimeKitUIBuilder.build(realtimeKitUIInfo)&#10;realtimeKitUI.startMeeting()&#10;</code></pre>
