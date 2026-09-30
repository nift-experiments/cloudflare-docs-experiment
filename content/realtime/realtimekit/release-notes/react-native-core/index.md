<h2 id="2026-07-08">2026-07-08</h2><strong>RealtimeKit React Native Core 2.0.0</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit React Native UI Kit 2.0.0 or later.</p>
<p>This is a major breaking release. Review all breaking changes below before upgrading.</p>
<p><strong>Breaking changes</strong></p>
<ul>
<li>Upgraded to <code>@cloudflare/realtimekit</code> v2.0.0.<br />
All <a href="/realtime/realtimekit/release-notes/#2026-06-18-realtimekit-web-core-200">breaking changes from Web Core v2.0.0</a> apply, including the complete redesign of the plugin API and removal of all deprecated APIs.</li>
<li>Requires React Native 0.84 or above and React 19 or above.</li>
<li>Requires Expo 56 or above (for Expo users).</li>
<li>Requires iOS 15.1 or above.</li>
<li>Requires @cloudflare/react-native-webrtc v137.0.1 or above.</li>
<li>Removed <code>RealtimeKitCore</code> import in iOS Screenshare setup and added a Podfile installer script to automatically add references to the Screenshare related files. Refer documentation for <a href="/realtime/realtimekit/core/local-participant/#screen-share-setup-ios">iOS Screenshare setup</a>.</li>
<li><code>initClient</code> return type changed from <code>Promise&lt;RealtimeKitClient&gt;</code> to <code>Promise&lt;RealtimeKitClient | undefined&gt;</code>. Code that assumes <code>initClient</code> always returns a defined value must add a null check.</li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li><code>Connected Meetings</code> support: the <code>useRealtimeKitClient</code> hook now automatically listens to <code>connectedMeetings.meetingChanged</code> and hot-swaps the active client when switching between connected or breakout meetings.</li>
<li><code>Background support</code> for Android (enabled by default):
<ul>
<li>New exported type <code>KeepAliveServiceConfig</code> to configure the Android meeting foreground service notification (title, body text, enable/disable).</li>
<li>New <code>useRealtimeKitClient({ keepAliveService })</code> option to customize or disable the Android foreground notification.</li>
<li>New <code>useRealtimeKitClient({ resetOnLeave })</code> option to reset client state on room leave.</li>
</ul>
</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue where the microphone did not work after being toggled if audio permission had not been granted before joining the meeting.</li>
<li>Fixed an issue where the in-call notification on Android persisted after the meeting ended.</li>
<li>Fixed an issue where screen sharing failed on the first attempt on Android 14 and above.</li>
<li>Fixed an issue where stopping screen sharing did not properly clean up event listeners, which could cause screen sharing to malfunction in subsequent sessions.</li>
</ul><h2 id="2026-06-18">2026-06-18</h2><strong>RealtimeKit React Native Core 1.1.0</strong><p><strong>Features</strong></p>
<ul>
<li>Added a dedicated error code <code>0014</code> for media (WebRTC) connection failures during room join, making it easier to distinguish media failures from socket and signaling failures.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>Init and join failures from <code>initMeeting()</code> and <code>meeting.join()</code> now surface specific error codes and descriptive messages instead of generic errors.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue where <code>ClientError</code> objects were wrapped inside each other when the SDK retried failed API requests, causing nested error messages and duplicate <code>onError</code> callbacks.</li>
</ul><h2 id="2026-05-05">2026-05-05</h2><strong>RealtimeKit React Native Core 1.0.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Removed Hive SFU support. Only the Cloudflare SFU is supported going forward.</li>
<li>The default base URI is now <code>realtime.cloudflare.com</code>. Calling <code>initMeeting()</code> with baseURI parameter set to a <code>dyte.io</code> base domain now throws an Error.</li>
<li><code>RealtimeKitClientOptions</code> is renamed to <code>RTKClientOptions</code>.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue where sometimes after rejoining a meeting &amp; upon stopping iOS screenshare, the app freezes.</li>
</ul><h2 id="2026-03-30">2026-03-30</h2><strong>RealtimeKit React Native Core 0.3.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed the issue when leaving &amp; rejoining a meeting causes the local media to stop working</li>
<li>Fixed iOS screenshare stops broadcasting on Web when calling <code>meeting.self.disableScreenShare()</code> but not clicking on 'Stop' on iOS Picker View.</li>
</ul><h2 id="2025-11-20">2025-11-20</h2><strong>RealtimeKit React Native Core 0.3.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed bluetooth not showing in list/dropdown after rejoining meeting</li>
<li>Fixed mobile active speaker not working after rejoining meeting</li>
</ul><h2 id="2025-11-02">2025-11-02</h2><strong>RealtimeKit React Native Core 0.3.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Starting from version v0.3.0, SDK now supports only React Native 0.77 and above.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed 16KB page support in Android &gt;=15</li>
<li>Fixed foreground service failed to stop errors in Android</li>
<li>Fixed bluetooth issues in iOS Devices</li>
<li>Fixed android build issues due to deprecated jCenter in React Native 0.80 or higher</li>
</ul><h2 id="2025-10-06">2025-10-06</h2><strong>RealtimeKit React Native Core 0.2.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed can't install multiple apps with expo sdk</li>
<li>Fixed screenshare for Android in Expo with New Architecture enabled</li>
<li>Fixed remote audio/video not working in group calls</li>
</ul><h2 id="2025-09-14">2025-09-14</h2><strong>RealtimeKit React Native Core 0.2.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Adding a <code>blob_provider_authority</code> string resource is now mandatory.
Refer to the installation instructions for more details.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed audio switch to earpiece when leaving stage in Webinar</li>
<li>Fixed types for useRealtimeKitClient options</li>
<li>Fixed screenshare for Android in Expo</li>
</ul><h2 id="2025-08-05">2025-08-05</h2><strong>RealtimeKit React Native Core 0.1.3</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed active speaker not working</li>
</ul><h2 id="2025-07-08">2025-07-08</h2><strong>RealtimeKit React Native Core 0.1.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed screenshare not working for Android 13 and later</li>
<li>Fixed audio device switching not working</li>
<li>Minor performance improvements</li>
</ul><h2 id="2025-06-05">2025-06-05</h2><strong>RealtimeKit React Native Core 0.1.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Documentation improvements</li>
</ul><h2 id="2025-05-29">2025-05-29</h2><strong>RealtimeKit React Native Core 0.1.0</strong><p><strong>Features</strong></p>
<ul>
<li>Initial release</li>
</ul>
