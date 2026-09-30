<h2 id="2026-09-16">2026-09-16</h2><strong>RealtimeKit Android Core 3.2.0</strong><p><strong>Enhancements</strong></p>
<ul>
<li><strong>Connection and media reliability</strong> — Improved recovery from connection interruptions and screen-share shutdown.</li>
<li><strong>Breakout rooms</strong> — Admins can now join child rooms and reassign participants across rooms. Participant assignment and state handling are also improved.</li>
<li><strong>Polls</strong> — Improved vote acknowledgements and validation for ambiguous options.</li>
<li><strong>API errors</strong> — Improved reporting for authenticated API failures.</li>
</ul><h2 id="2026-07-17">2026-07-17</h2><strong>RealtimeKit Android Core 3.1.0</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Room joins are up to 25% faster under normal network conditions</li>
<li>Improved the initial quality of video received from mobile participants</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed a crash when switching between breakout rooms</li>
<li>When unmuting audio or video, the SDK now requests permission when the corresponding <code>RtkMeetingInfo.enableAudio</code> or <code>RtkMeetingInfo.enableVideo</code> field is <code>false</code>. The UI Kit component is no longer silently disabled.</li>
</ul><h2 id="2026-06-24">2026-06-24</h2><strong>RealtimeKit Android Core 3.0.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Plugins are no longer provided by the server. They must now be declared upfront on the client side by passing a <code>plugins</code> list to <code>RtkMeetingInfo</code>. Any plugin not declared at initialization will not be available in the meeting.
<pre><code class="language-kotlin">val meetingInfo = RtkMeetingInfo(&#10;  authToken = authToken,&#10;  plugins = listOf(&#10;    RtkClientPluginConfig(&#10;      id = &quot;whiteboard&quot;, // Must match the plugin ID used on Web for sync to work&#10;      name = &quot;Whiteboard&quot;,&#10;      icon = &quot;https://example.com/logo.png&quot;,&#10;      url = &quot;https://example.com&quot;,&#10;      permissions = RtkClientPluginPermissions(canActivate = true, canDeactivate = true),&#10;    )&#10;  ),&#10;)&#10;</code></pre>
</li>
<li>Several internal properties have been removed from <code>RtkPlugin</code>: <code>baseURL</code>, <code>config</code>, <code>description</code>, <code>isPrivate</code>, and <code>staggered</code>. Use the new <code>icon</code> and <code>permissions</code> properties instead.</li>
<li>The two-argument <code>subscribe(key, (key, value) → Unit)</code> and <code>unsubscribe(key, (key, value) → Unit)</code> overloads on <code>RtkStore</code> have been removed. Use the single-argument callback variants introduced in 2.1.0.</li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li><strong>AI Transcription</strong> — A new <code>RtkAi</code> class (exposed as <code>client.ai</code>) provides access to real-time transcripts. Implement <code>RtkAiEventListener</code> and register it with <code>addAiEventListener()</code> to receive <code>onTranscript(data: RtkTranscriptionData)</code> callbacks. A <code>transcriptionEnabled</code> permission is available on <code>MiscellaneousPermissions</code>.</li>
<li><strong>Connected Meetings (Breakout Rooms)</strong> — A new <code>RtkConnectedMeetings</code> class (exposed as <code>client.connectedMeetings</code>) enables breakout room workflows. Register an <code>RtkConnectedMeetingsEventListener</code> to handle room transitions and state updates. See the <a href="/realtime/realtimekit/core/breakout-rooms/">Breakout Rooms</a> documentation for a full guide.</li>
<li><strong>Chat: Edit and Delete</strong> — Messages can now be edited and deleted. New methods on <code>RtkChat</code>: <code>editTextMessage()</code>, <code>editImageMessage()</code>, <code>editFileMessage()</code>, and <code>deleteMessage()</code>. <code>RtkChatEventListener</code> gains <code>onMessageEdited()</code> and <code>onMessageDeleted()</code> callbacks. <code>ChatMessage</code> now includes an <code>isEdited</code> flag.</li>
<li><strong>Chat: Fetch and Pagination</strong> — New methods on <code>RtkChat</code> — <code>fetchPublicMessages()</code>, <code>fetchPrivateMessages()</code>, <code>fetchPinnedMessages()</code>, and <code>getMessages()</code> — allow fetching historical messages with cursor-based pagination via <code>FetchMessagesResult(messages, hasMore)</code>.</li>
<li><strong>Client-Declared Plugins</strong> — Plugins are now configured entirely on the client via <code>RtkClientPluginConfig</code> and <code>RtkClientPluginPermissions</code>. <code>RtkPlugin</code> exposes the new <code>icon</code> and <code>permissions</code> properties accordingly.</li>
<li><strong>Targeted Broadcast Messages</strong> — <code>RtkParticipants.broadcastMessage()</code> now accepts an optional <code>targetParticipantIds: List&lt;String&gt;</code> parameter to send a message to a specific subset of participants.</li>
<li><strong>Nullable Store Values</strong> — <code>RtkStore.set()</code> now accepts a nullable <code>value: Any?</code>, allowing keys to be cleared by setting them to <code>null</code>.</li>
<li><strong>Logging Control</strong> — <code>RealtimeKitClient</code> gains <code>enableLogging(enabled: Boolean)</code> and <code>enableLogging(enabled: Boolean, minSeverity: LogSeverity)</code> to control SDK log output at runtime.</li>
<li><strong>Result&lt;S, F&gt; Utility Type</strong> — A new <code>sealed class Result&lt;S, F&gt;</code> with <code>Success</code> and <code>Failure</code> variants is used consistently across new async APIs.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Improved reconnection handling to ensure media recovers gracefully in more scenarios</li>
<li>Improved simulcast tiers to broadcast at a wider range of qualities on higher tiers</li>
<li>Fixed some races in media handling causing mute/unmute operations to rarely result in a crash</li>
<li>Optimized API calls in the room join flow to speed up first join durations</li>
<li>Fixed file and image uploads in chat failing under some conditions</li>
</ul><h2 id="2026-05-08">2026-05-08</h2><strong>RealtimeKit Android Core 2.1.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li><code>RtkParticipants.activeSpeaker</code> → <code>RtkParticipants.lastActiveSpeaker</code>. The old <code>activeSpeaker</code> property is deprecated and will be removed in a future release.</li>
<li><code>RtkSelfParticipant.enableScreenShare()</code> → <code>enableScreenShare(onResult:)</code>. The old no-callback version is deprecated and will be removed in a future release.</li>
<li><code>RtkSelfParticipant.disableScreenShare()</code> → <code>disableScreenShare(onResult:)</code>. The old no-callback version is deprecated and will be removed in a future release.</li>
<li><code>RtkStore.subscribe(key, (key, value) → Unit)</code> → <code>subscribe(key, (value) → Unit)</code>. The old two-argument callback signature is deprecated but remains functional via a backward-compatible shim.</li>
<li><code>RtkStore.unsubscribe(key, (key, value) → Unit)</code> → <code>unsubscribe(key, (value) → Unit)</code>. The old two-argument callback signature is deprecated but remains functional via a backward-compatible shim.</li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li>Added <code>RtkChat.pin()</code> and <code>RtkChat.unpin()</code> methods to pin and unpin chat messages</li>
<li>Added <code>RtkChat.getMessagesByUser()</code> to filter messages by sender and <code>RtkChat.getMessagesByType()</code> to filter messages by type</li>
<li>Added <code>SelfPermissions.canPinMessage()</code> to check whether the local participant has permission to pin messages</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed a memory leak in video rendering caused by <code>SurfaceViewRenderer</code> instances not being released</li>
<li>Fixed recording state getting stuck as &quot;recording&quot; when stopping a recording that was started by another participant</li>
<li>Fixed &quot;ghost&quot; participants appearing on the grid when a user was on the setup screen but had not yet joined the socket room</li>
<li>Fixed webinar host being invisible to other participants when joining late</li>
<li>Fixed recording bots and other hidden participants incorrectly appearing on the participant grid</li>
<li>Fixed waitlisted participants appearing in the participant list before being admitted to the meeting</li>
</ul><h2 id="2026-04-20">2026-04-20</h2><strong>RealtimeKit Android Core 2.0.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Removed Hive SFU support. Only the Cloudflare SFU is supported going forward.</li>
<li>The default base URI is now <code>realtime.cloudflare.com</code>. Calling <code>init()</code> with a <code>dyte.io</code> base domain now fails immediately with <code>MeetingError.InvalidBaseUrl</code></li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Added compatibility with new backend plugins API field naming</li>
<li>Fixed a crash that could occur when accessing the socket controller before <code>init()</code> was called</li>
<li>Fixed auth token not being sent to the callstats collector endpoint</li>
<li>Removed custom ping-pong keepalive logic that was only required for the previous infrastructure</li>
</ul><h2 id="2026-03-06">2026-03-06</h2><strong>RealtimeKit Android Core 1.6.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Avoid crash when using Ktor versions 3.4.0 and above</li>
</ul><h2 id="2026-02-06">2026-02-06</h2><strong>RealtimeKit Android Core 1.6.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed media issues when connection took longer to establish</li>
</ul><h2 id="2026-01-14">2026-01-14</h2><strong>RealtimeKit Android Core 1.6.0</strong><p><strong>Fixes</strong></p>
<ul>
<li>Improved grid transitions by activating consumers in batches for better performance</li>
<li>Moved consumer toggle requests off main thread to prevent UI blocking</li>
<li>Improved video rendering stability with better lifecycle management</li>
<li>Prevented race conditions by canceling reconnection attempts during initialization</li>
</ul><h2 id="2025-12-16">2025-12-16</h2><strong>RealtimeKit Android Core 1.5.7</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed rare crash when toggling audio mute</li>
<li>Off-stage webinar hosts no longer show up on the grid</li>
</ul><h2 id="2025-12-12">2025-12-12</h2><strong>RealtimeKit Android Core 1.5.6</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed deadlocks in webinar join and screenshare enable flows</li>
<li>Fixed an issue with camera not working when moving to settings screen and back</li>
<li>Fixed a rare crash in voice activity detection</li>
</ul><h2 id="2025-12-04">2025-12-04</h2><strong>RealtimeKit Android Core 1.5.5</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed participant tiles not being removed properly when peers left the meeting</li>
</ul><h2 id="2025-11-06">2025-11-06</h2><strong>RealtimeKit Android Core 1.5.4</strong><p><strong>Fixes</strong></p>
<ul>
<li>Internal fixes to reduce telemetry verbosity</li>
</ul><h2 id="2025-10-23">2025-10-23</h2><strong>RealtimeKit Android Core 1.5.3</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed a regression that caused self video to not render if meeting was joined with camera disabled</li>
</ul><h2 id="2025-10-23-1">2025-10-23</h2><strong>RealtimeKit Android Core 1.5.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed unreliable grid behavior with improved refresh logic</li>
</ul><h2 id="2025-10-06">2025-10-06</h2><strong>RealtimeKit Android Core 1.5.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Internal fixes to resolve issues for Flutter platform</li>
</ul><h2 id="2025-09-23">2025-09-23</h2><strong>RealtimeKit Android Core 1.5.0</strong><p><strong>Features</strong></p>
<ul>
<li>Added <code>RtkSelfEventListener#onAudioDeviceChanged</code> method that is invoked when the current audio route is updated</li>
</ul><h2 id="2025-09-18">2025-09-18</h2><strong>RealtimeKit Android Core 1.4.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Speakerphone is now preferred over earpiece as the default audio output</li>
</ul><h2 id="2025-09-18-1">2025-09-18</h2><strong>RealtimeKit Android Core 1.4.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Updated <code>RtkSelfEventListener#onAudioDevicesUpdated</code> method to provide the list of available devices</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed not being able to route audio to Bluetooth devices</li>
</ul><h2 id="2025-09-12">2025-09-12</h2><strong>RealtimeKit Android Core 1.3.4</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed a rare crash during meeting joins in poor network scenarios</li>
</ul><h2 id="2025-09-12-1">2025-09-12</h2><strong>RealtimeKit Android Core 1.3.3</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed pinned peers not being removed from the stage when kicked</li>
<li>Media consumers are now created in parallel, which significantly improved the speed of when users start seeing other people's audio/video after joining a meeting</li>
<li>Native libraries are now 16KB aligned to comply with <a href="https://android-developers.googleblog.com/2025/05/prepare-play-apps-for-devices-with-16kb-page-size.html">Google Play requirements</a></li>
<li>Fixed &quot;Ghost&quot;/Invalid peers that would sometimes show up in long-running meetings</li>
<li>Fixed an issue in webinar meetings where the SDK would fail to produce media after being removed from the stage once</li>
</ul><h2 id="2025-08-13">2025-08-13</h2><strong>RealtimeKit Android Core 1.3.2</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Fixed microphone not working when joining the stage in a webinar</li>
</ul><h2 id="2025-08-13-1">2025-08-13</h2><strong>RealtimeKit Android Core 1.3.1</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Fixed a potential crash in poor network scenarios</li>
</ul><h2 id="2025-08-12">2025-08-12</h2><strong>RealtimeKit Android Core 1.3.0</strong><p><strong>Features</strong></p>
<ul>
<li>Added <code>RtkSelfParticipant#canJoinStage</code> and <code>RtkSelfParticipant#canRequestToJoinStage</code> APIs</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed viewer unable to join stage in a Livestream</li>
<li>Fixed user unable to see existing pinned participant after joining meeting</li>
</ul><h2 id="2025-08-05">2025-08-05</h2><strong>RealtimeKit Android Core 1.2.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Renamed <code>RtkLivestreamData.roomName</code> to <code>RtkLivestreamData.meetingId</code> to match existing API convention</li>
<li>Removed obsolete <code>WaitingRoomPermissions</code> abstraction — all the relevant functionality here is available through <code>HostPermissions</code></li>
<li>VideoDevice gained a <code>cameraType: CameraType</code> parameter</li>
<li><code>VideoDeviceType#displayName</code> is now deprecated, and it's recommended to call <code>VideoDevice#toString</code> instead to get user-facing names for individual <code>VideoDevice</code> instances</li>
<li>Existing APIs related to middlewares were removed and replaced with equivalent counterparts from WebRTC: <code>RtkSelfParticipant#addVideoMiddleware</code>, <code>RtkSelfParticipant#getVideoMiddlewares</code> and <code>RtkSelfParticipant#removeVideoMiddleware</code> were replaced with <code>RealtimeKitMeetingBuilder#setVideoProcessor</code></li>
<li><code>RtkVideoFrame</code> was removed in favor of WebRTC's own <code>VideoFrame</code> class, available as <code>realtimekit.org.webrtc.VideoFrame</code></li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li>Reimplemented middlewares using WebRTC-native primitives to resolve intermittent crashes and other issues, check out the new <a href="https://docs.realtime.cloudflare.com/android-core/video-processing/introduction">Video Processing</a> docs section to learn more</li>
<li><code>VideoDevice</code> now properly labels multiple cameras based on their camera characteristics such as wide-angle and telephoto</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed screen share failing to stop</li>
<li>Silenced log spam from our callstats library</li>
</ul><h2 id="2025-07-02">2025-07-02</h2><strong>RealtimeKit Android Core 1.1.0</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Meeting initialization (<code>meeting.init()</code>) is now ~60% faster</li>
<li>Switched to an updated and <strong>RTK</strong> namespaced WebRTC</li>
<li>Improved Active speaker detection with the updated WebRTC</li>
</ul><h2 id="2025-06-20">2025-06-20</h2><strong>RealtimeKit Android Core 1.0.1</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Renamed RtkMessageType to ChatMessageType</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Silenced logspam from audio activity reporter</li>
<li>Improved speed of joining calls</li>
<li>Auth tokens now automatically trim invalid spaces and newlines</li>
</ul><h2 id="2025-05-26">2025-05-26</h2><strong>RealtimeKit Android Core 1.0.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Removed deprecated <code>channelId</code> field from <code>TextMessage</code></li>
<li>Moved listener types to their respective feature package</li>
<li>Moved public listeners to their respective feature packages</li>
<li>Renamed plugin add-remove listener methods for RtkPluginsEventListener</li>
<li>Moved chat extensions to the <code>chat</code> package</li>
<li>Moved <code>RtkParticipant</code> to the root package</li>
<li>Moved <code>RtkMeetingParticipant</code> to the root package</li>
<li>Moved <code>RtkPluginFile</code> to the plugins package</li>
<li>Moved middlewares to their own package</li>
<li>Moved <code>VideoScaleType</code> to top level <code>media</code> package</li>
<li>Dropped <code>Rtk</code> prefix from audio and video device types</li>
<li>Moved device types to the top level <code>media</code> package</li>
<li>Dropped <code>Rtk</code> prefix from polls types</li>
<li>Replaced all LiveStream references with Livestream</li>
<li>Moved <code>RtkMeetingParticipant</code> to root package</li>
<li>Stripped <code>Rtk</code> prefix from <code>RtkRecordingState</code></li>
<li>Stripped <code>Rtk</code> prefix from chat message types</li>
<li>Removed deprecated RtkLivestream#roomName field</li>
<li>Moved <code>RtkMediaPermission</code> to media package and renamed to <code>MediaPermission</code></li>
<li>Redistributed <code>feat</code> package members</li>
<li>Moved <code>StageStatus</code> class to stage package</li>
<li>Renamed all event listeners to be of the singular <code>*EventListener</code> form</li>
</ul><h2 id="2025-05-16">2025-05-16</h2><strong>RealtimeKit Android Core 0.2.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Internal fixes to release pipeline</li>
</ul><h2 id="2025-05-16-1">2025-05-16</h2><strong>RealtimeKit Android Core 0.2.0</strong><p><strong>Fixes</strong></p>
<ul>
<li>Added audio activity detection for active speaker signaling</li>
</ul><h2 id="2025-05-14">2025-05-14</h2><strong>RealtimeKit Android Core 0.1.0</strong><p><strong>New APIs</strong></p>
<ul>
<li>Initial alpha release</li>
</ul>
