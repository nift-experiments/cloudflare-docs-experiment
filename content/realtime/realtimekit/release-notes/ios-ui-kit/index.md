<h2 id="2026-09-16">2026-09-16</h2><strong>RealtimeKit iOS UI Kit 3.2.0</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Aligned the version with <a href="/realtime/realtimekit/release-notes/ios-core/#2026-09-16">RealtimeKit iOS Core v3.2.0</a>. This release has no breaking changes.</li>
</ul><h2 id="2026-07-17">2026-07-17</h2><strong>RealtimeKit iOS UI Kit 3.1.0</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Aligned the version with <a href="/realtime/realtimekit/release-notes/ios-core/#2026-07-17">RealtimeKit iOS Core v3.1.0</a>. This release has no breaking changes.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Audio and video toggle buttons no longer check permissions or disable themselves. The core SDK handles permission requests.</li>
</ul><h2 id="2026-06-30">2026-06-30</h2><strong>RealtimeKit iOS UI Kit 2.0.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2026-06-24">RealtimeKit Core v3.0.0</a>. Plugins must now be declared on the client side when constructing <code>RtkMeetingInfo</code>.</li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li>Added Breakout Rooms support. Participants can be assigned to rooms manually or distributed automatically; hosts can create, rename, and close rooms, move participants between them, and return everyone to the main room. See the Connected Meetings documentation for a full guide.</li>
<li>Added an AI Transcription screen accessible from the More menu. The screen matches web SDK rendering behavior: consecutive utterances from the same speaker are grouped, the list auto-scrolls to the latest transcript, and transcripts can be filtered by participant name or text.</li>
<li>Added edit and delete actions for chat messages. Long-pressing a message opens a context menu with Edit and Delete options. Edited messages display an &quot;edited&quot; indicator.</li>
</ul><h2 id="2026-05-11">2026-05-11</h2><strong>RealtimeKit iOS UI Kit 1.1.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Minimum deployment target raised to iOS 16.0</li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li>Added a &quot;Deny All&quot; button to the waiting room participant list so hosts can reject all pending join requests at once, in both group call and webinar meetings</li>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2026-05-08">RealtimeKit Core v2.1.0</a></li>
</ul><h2 id="2026-04-20">2026-04-20</h2><strong>RealtimeKit iOS UI Kit 1.0.0</strong><p><strong>Breaking changes</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2026-04-20">RealtimeKit Core v2.0.0</a> which removes support for Dyte APIs and SFU.</li>
<li>Minimum deployment target is now iOS 15.6</li>
</ul><h2 id="2026-01-14">2026-01-14</h2><strong>RealtimeKit iOS UI Kit 0.5.7</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2026-01-14">RealtimeKit Core v1.6.0</a></li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed video not resuming when video view returns to foreground</li>
</ul><h2 id="2025-12-16">2025-12-16</h2><strong>RealtimeKit iOS UI Kit 0.5.6</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-12-16">RealtimeKit Core v1.5.7</a></li>
</ul><h2 id="2025-12-12">2025-12-12</h2><strong>RealtimeKit iOS UI Kit 0.5.5</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-12-12">RealtimeKit Core v1.5.6</a></li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Raised minimum deployment target to iOS 15.6</li>
</ul><h2 id="2025-12-04">2025-12-04</h2><strong>RealtimeKit iOS UI Kit 0.5.4</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-12-04">RealtimeKit Core v1.5.5</a></li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Raised iOS deployment target to 15.6</li>
</ul><h2 id="2025-11-06">2025-11-06</h2><strong>RealtimeKit iOS UI Kit 0.5.3</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-11-06">RealtimeKit Core v1.5.4</a></li>
</ul><h2 id="2025-10-23">2025-10-23</h2><strong>RealtimeKit iOS UI Kit 0.5.2</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-10-23">RealtimeKit Core v1.5.3</a></li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed a regression that caused self video to not render if meeting was joined with camera disabled</li>
</ul><h2 id="2025-10-23-1">2025-10-23</h2><strong>RealtimeKit iOS UI Kit 0.5.1</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-10-23">RealtimeKit Core v1.5.2</a></li>
</ul><h2 id="2025-10-06">2025-10-06</h2><strong>RealtimeKit iOS UI Kit 0.5.0</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-10-06">RealtimeKit Core v1.5.1</a></li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Audio device selector now dynamically updates the options list when devices are removed or added</li>
<li>Fixed participant list host actions not working for self</li>
</ul><h2 id="2025-09-12">2025-09-12</h2><strong>RealtimeKit iOS UI Kit 0.4.6</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed a rare crash during meeting joins in poor network scenarios</li>
</ul><h2 id="2025-09-12-1">2025-09-12</h2><strong>RealtimeKit iOS UI Kit 0.4.5</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed pinned peers not being removed from the stage when kicked</li>
<li>Media consumers are now created in parallel, which significantly improved the speed of when users start seeing other people's audio/video after joining a meeting</li>
<li>Fixed &quot;Ghost&quot;/Invalid peers that would sometimes show up in long-running meetings</li>
<li>Fixed an issue in webinar meetings where the SDK would fail to produce media after being removed from the stage once</li>
</ul><h2 id="2025-08-13">2025-08-13</h2><strong>RealtimeKit iOS UI Kit 0.4.4</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-08-13">RealtimeKit Core v1.3.2</a></li>
</ul><h2 id="2025-08-13-1">2025-08-13</h2><strong>RealtimeKit iOS UI Kit 0.4.3</strong><p><strong>Features</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-08-13">RealtimeKit Core v1.3.1</a></li>
</ul><h2 id="2025-08-12">2025-08-12</h2><strong>RealtimeKit iOS UI Kit 0.4.2</strong><p><strong>Features</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-08-12">RealtimeKit Core v1.3.0</a></li>
</ul><h2 id="2025-08-08">2025-08-08</h2><strong>RealtimeKit iOS UI Kit 0.4.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed multiple errors in the SPM package preventing it from being imported by users</li>
</ul><h2 id="2025-08-05">2025-08-05</h2><strong>RealtimeKit iOS UI Kit 0.4.0</strong><p><strong>Features</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-08-05">RealtimeKit Core v1.2.0</a></li>
</ul><h2 id="2025-07-02">2025-07-02</h2><strong>RealtimeKit iOS UI Kit 0.3.0</strong><p><strong>Features</strong></p>
<ul>
<li>Upgraded to <a href="/realtime/realtimekit/release-notes/ios-core/#2025-07-02">RealtimeKit Core v1.1.0</a></li>
</ul>
