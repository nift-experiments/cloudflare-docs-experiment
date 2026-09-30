<h2 id="2026-07-08">2026-07-08</h2><strong>RealtimeKit React Native UI Kit 2.0.0</strong><p><strong>Compatibility:</strong> Requires <code>@cloudflare/realtimekit-react-native</code> (React Native Core) v2.0.0 or later</p>
<p>This is a major breaking release. Review all breaking changes below before upgrading.</p>
<p><strong>Breaking changes</strong></p>
<ul>
<li>Upgraded to <code>@cloudflare/realtimekit-react-native</code> v2.0.0 and <code>@cloudflare/realtimekit</code> v2.0.0. All <a href="/realtime/realtimekit/release-notes/#2026-06-18-realtimekit-web-core-200">breaking changes from Web Core v2.0.0</a> and <a href="/realtime/realtimekit/release-notes/react-native-core/">React Native Core v2.0.0</a> apply.</li>
<li>Removed the KeepAlive Service from the UI Kit. Background Audio/Video support for Android is now managed by <code>@cloudflare/realtimekit-react-native</code> v2.0.0. Update your integration to use <code>useRealtimeKitClient({ keepAliveService })</code> from the Core SDK.</li>
<li><code>RtkPluginMain</code> now uses <code>plugin.component</code> (an <code>HTMLElement</code>-like object) instead of an iframe. This aligns with the plugin API redesign in Web Core 2.0.0.</li>
<li>RtkMoreMenu is now scrollable rather than a fixed-height container.</li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li><code>Breakout Rooms</code> support:
<ul>
<li>New <code>RtkBreakoutRoomsManager</code> component: full manager UI for creating, assigning participants, and starting or stopping breakout rooms.</li>
<li>New <code>RtkBreakoutRoomsToggle</code> component: control-bar button to open or close the breakout rooms manager.</li>
</ul>
</li>
<li>Connected meeting switching UI: <code>RtkMeeting</code> now handles <code>changingMeeting</code> events and shows a &quot;Joining…&quot; interstitial screen while switching between connected rooms.</li>
<li>New exported types: <code>ConnectedMeeting</code>, <code>ConnectedMeetingParticipant</code>, <code>ConnectedMeetingState</code>, <code>PluginIframe</code>.</li>
<li>New state fields in the <code>States</code> type:
<ul>
<li><code>activeBreakoutRoomsManager</code> — tracks breakout manager open/close state and room-switch destination.</li>
<li><code>activeBreakoutConfirmation</code> — breakout action confirmation dialog state.</li>
</ul>
</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue where the chat sent notification showed up when a message was edited rather than only when a new message was sent.</li>
<li>Fixed an issue where video from web participants did not update on mobile devices while screen sharing or a plugin was active.</li>
<li>Fixed an issue where the screenshare video appeared stretched or distorted in fullscreen when switching between landscape and portrait orientations.</li>
<li>Fixed an issue where host controls disappeared when the host was off stage.</li>
<li>Fixed an issue where the screenshare view shook when the device was held in landscape mode on iOS.</li>
<li>Fixed an issue where the screen orientation did not return to normal after closing a fullscreen plugin on Android.</li>
<li>Fixed an issue where the More menu could not be scrolled when the device was in landscape mode.</li>
<li>Fixed an issue where opening the More menu in landscape mode incorrectly locked the screen orientation.</li>
<li>Fixed inconsistent appearance across button and toggle controls.</li>
<li>Fixed an issue where participant video tiles occasionally showed outdated or frozen video.</li>
<li>Fixed an issue where the &quot;Hide Result&quot; option was not enabled by default when creating a poll.</li>
</ul><h2 id="2026-05-05">2026-05-05</h2><strong>RealtimeKit React Native UI Kit 1.0.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Removed support for <code>@cloudflare/realtimekit-react-native</code> version less than v1.0.0</li>
<li>The Join Stage Confirmation dialog (i.e <code>RtkJoinStage</code>) now opens with Mic/Camera disabled by default.</li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li>Added unread counts for chat and polls in <code>RtkPollsToggle</code>, <code>RtkChatToggle</code>, and <code>RtkMoreToggle</code></li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue where when a meeting host leaves the stage, all plugins and host controls disappear.</li>
</ul><h2 id="2026-03-30">2026-03-30</h2><strong>RealtimeKit React Native UI Kit 0.2.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue where self video is not visible on Setup Screen on initial load (i.e happens with @cloudflare/realtimekit-react-native version v0.3.2)</li>
</ul><h2 id="2025-11-20">2025-11-20</h2><strong>RealtimeKit React Native UI Kit 0.2.0</strong><p><strong>Features</strong></p>
<ul>
<li>Added edit, pin, and delete controls to Chat messages in RtkChat</li>
<li>Added optional background support for audio/video in Android.
Refer to the <a href="https://docs.realtime.cloudflare.com/react-native/quickstart#additional-steps-for-background-audiovideo-support">documentation</a> for implementation details.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed image button in RtkChat opening File Manager instead of Gallery</li>
<li>Fixed app crash on RtkChat auto-scroll when new messages arrive</li>
<li>Fixed chat message display issues</li>
</ul><h2 id="2025-09-14">2025-09-14</h2><strong>RealtimeKit React Native UI Kit 0.1.3</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed duplicate stage toggle pop-ups</li>
<li>Fixed audio switch to earpiece when leaving stage in Webinar</li>
</ul><h2 id="2025-07-08">2025-07-08</h2><strong>RealtimeKit React Native UI Kit 0.1.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed android build failing for New Architecture</li>
<li>Added delete option feature in Polls</li>
<li>Fixed screen being blank when kicked from meeting</li>
<li>Fixed the fullscreen button not clickable in screenshare</li>
<li>Fixed audio selector not visible for webinar viewer</li>
<li>Fixed video incorrectly labeled as being off</li>
</ul><h2 id="2025-06-05">2025-06-05</h2><strong>RealtimeKit React Native UI Kit 0.1.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Documentation improvements</li>
</ul><h2 id="2025-06-04">2025-06-04</h2><strong>RealtimeKit React Native UI Kit 0.1.0</strong><p><strong>Features</strong></p>
<ul>
<li>Initial release</li>
</ul>
