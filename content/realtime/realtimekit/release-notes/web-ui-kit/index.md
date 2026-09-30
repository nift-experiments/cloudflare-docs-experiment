<h2 id="2026-08-24">2026-08-24</h2><strong>RealtimeKit Web UI Kit 2.0.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Restored Safari 16.x compatibility by incorporating an <a href="https://github.com/stenciljs/core/pull/6236">upstream Stencil fix</a>.</li>
<li>Fixed <code>rtk-idle-screen</code> incorrectly displaying non-fatal <code>preJoinError</code> events, such as declining to share media, as fatal errors.</li>
<li>Starting a recording while one is already in progress now displays a specific message instead of a generic internal error.</li>
</ul>
<p><strong>New localization keys</strong></p>
<ul>
<li><code>recording.error.already_recording</code> — &quot;A recording is already in progress.&quot;</li>
</ul><h2 id="2026-07-17">2026-07-17</h2><strong>RealtimeKit Web UI Kit 2.0.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>The <code>joinError</code> state has been superseded by <code>preJoinError</code> to cover all errors that occur before or during joining the meeting. Refer to <a href="/realtime/realtimekit/ui-kit/state-management/">State management</a> for details on UI Kit states.</li>
<li>The <code>rtk-idle-screen</code> now displays user-friendly error messages instead of just an infinite loader, helping customers identify issues and retry.</li>
<li>Fixed errors thrown by the Core SDK not being captured and shown properly by the UI Kit.</li>
</ul>
<p><strong>New localization keys</strong></p>
<ul>
<li><code>init.auth_error</code> — &quot;We couldn't verify your access to this meeting. The meeting may have ended, or you may not have permission to join.&quot;</li>
<li><code>init.network_error</code> — &quot;We couldn't connect to the meeting. Please try again, and if the problem continues, check your internet connection.&quot;</li>
<li><code>init.browser_error</code> — &quot;Your browser is not supported. Please try a different or updated browser.&quot;</li>
<li><code>init.default_error</code> — &quot;Something went wrong while connecting to the meeting. Please try again.&quot;</li>
<li><code>join.network_error</code> — &quot;We couldn't connect to the meeting. Please check your internet connection and try again.&quot;</li>
<li><code>join.media_error</code> — &quot;We're having trouble connecting to the meeting. Please try again, and if the problem continues, try using a different network.&quot;</li>
<li><code>join.media_firewall_error</code> — &quot;Your network may be blocking this connection. Try using a different network, or contact your network administrator for help.&quot;</li>
<li><code>join.default_error</code> — &quot;Something went wrong while joining the meeting. Please try again.&quot;</li>
<li><code>join.error_code</code> — &quot;Error code&quot;</li>
</ul><h2 id="2026-06-18">2026-06-18</h2><strong>RealtimeKit Web UI Kit 2.0.0</strong><p><strong>Compatibility:</strong> Requires RealtimeKit Web Core 2.0.0 or later.</p>
<p>This is a major breaking release to align with the Core SDK v2.0.0 plugin redesign and removal of deprecated APIs.</p>
<p><strong>Plugin components — redesigned</strong></p>
<p>The <code>rtk-plugin-main</code> and <code>rtk-plugins</code> components have been updated for the new plugin model.</p>
<p>Key changes:</p>
<ul>
<li><code>rtk-plugin-main</code> no longer renders an <code>&lt;iframe&gt;</code>. Instead, it uses a <code>&lt;slot&gt;</code> to project the <code>plugin.component</code> (any <code>HTMLElement</code>) you provide in the plugin config.</li>
<li>Plugin permission checks now use <code>plugin.permissions.canActivate</code> and <code>plugin.permissions.canDeactivate</code> instead of the old <code>meeting.self.permissions.plugins.canStart</code> / <code>canClose</code>.</li>
<li>Plugin list (<code>rtk-plugins</code>) now shows <code>plugin.icon</code> instead of <code>plugin.picture</code>.</li>
<li>Added an empty state message (&quot;No plugins available&quot;) when no plugins are registered.</li>
<li>Removed iframe interaction checks (<code>canInteractWithPlugin</code>, <code>viewModeEnabled</code>) and the <code>block-inputs</code> overlay. These are no longer applicable without iframes.</li>
</ul>
<p><strong>Removed deprecated API usages</strong></p>
<ul>
<li><code>meeting.leaveRoom()</code> — use <code>meeting.leave()</code>.</li>
<li><code>meeting.connectedMeetings.supportsConnectedMeetings</code> — removed. Breakout room checks use <code>meeting.connectedMeetings.isActive</code> and permission checks directly.</li>
<li><code>participant.clientSpecificId</code> — use <code>participant.customParticipantId</code>.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>AI Transcriptions UI: Rewrote the search UI for transcriptions. Search now covers both participant names and transcript content. Added dedicated search placeholder and &quot;no results&quot; states.</li>
<li>AI Transcriptions header: Fixed typo &quot;MeetingAI&quot; to &quot;Meeting AI&quot;.</li>
<li>Chat message spacing: Reduced line height in <code>rtk-message-view</code> for better vertical spacing.</li>
<li>Audio track handling: <code>RTKAudio.addTrack()</code> now removes any existing track with the same ID before adding, preventing stale tracks from accumulating (fixes double audio on reconnect).</li>
</ul>
<p><strong>New localization keys</strong></p>
<ul>
<li><code>plugins.empty</code> — &quot;No plugins available&quot;</li>
<li><code>ai.transcriptions.search_placeholder</code> — &quot;Search by participant name or transcript&quot;</li>
<li><code>ai.transcriptions.no_transcripts_found</code> — &quot;No transcripts found. Try searching for a different participant or transcript.&quot;</li>
<li><code>ai.transcriptions.no_transcripts_yet</code> — &quot;No transcripts yet.&quot;</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed abrupt disconnection screen appearing incorrectly during media reconnection.</li>
<li>Fixed missing audio after reconnection due to stale tracks not being replaced.</li>
</ul><h2 id="2026-05-28">2026-05-28</h2><strong>RealtimeKit Web UI Kit 1.2.0</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit Web Core 1.5.1 or later.</p>
<p><strong>Features</strong></p>
<ul>
<li>When a user fails to join a meeting, <code>rtk-idle-screen</code> and <code>rtk-setup-screen</code> now display a troubleshooting link to help resolve common connection issues such as firewall restrictions and permission errors.</li>
<li>If the meeting preset allows transcripts, the transcription panel is now shown by default without requiring manual activation.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>Raw SDK error codes and messages are no longer shown to end users on join failure. Error messages are now mapped to clear, user-friendly, localized text with a small reference code (for example, <code>Error code: 0002</code>) for support and debugging.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Corrected several typos and spacing issues in the default language pack.</li>
</ul><h2 id="2026-03-31">2026-03-31</h2><strong>RealtimeKit Web UI Kit 1.1.2</strong><p><strong>Enhancements</strong></p>
<ul>
<li>AI sidebar component now uses <code>activeSidebar</code> state instead of <code>activeAI</code> state, streamlining all sidebar components under a single state.</li>
</ul><h2 id="2026-03-10">2026-03-10</h2><strong>RealtimeKit Web UI Kit 1.1.1</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit Web Core 1.2.5 or later.</p>
<p><strong>Enhancements</strong></p>
<ul>
<li>Improved error handling for room join failures to display actionable error messages instead of showing an infinite loader.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Corrected typos in UI strings:
<ul>
<li><code>occured</code> → <code>occurred</code></li>
<li><code>On you device</code> → <code>On your device</code></li>
<li><code>Grant acess</code> → <code>Grant access</code></li>
</ul>
</li>
<li>Fixed default language pack keys:
<ul>
<li><code>ai.chat.summerise</code> → <code>ai.chat.summarize</code></li>
<li><code>date.yesteday</code> → <code>date.yesterday</code></li>
</ul>
</li>
</ul><h2 id="2026-01-30">2026-01-30</h2><strong>RealtimeKit Web UI Kit 1.1.0</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit Web Core 1.2.4 or later.</p>
<p><strong>Features</strong></p>
<ul>
<li>Chat message operations (edit, delete, pin) are now available to all participants.</li>
<li>Chat pagination with infinite scroll for improved performance in meetings with high message volume.</li>
<li>Pinned messages are now displayed in a dedicated view for easy access.</li>
<li>Added <code>overrides</code> prop support on <code>rtk-meeting</code> and <code>rtk-ui-provider</code> for easier UI customization. Available overrides include:
<ul>
<li><code>disablePrivateChat</code> - Disable private chat functionality.</li>
<li><code>disableEmojiPicker</code> - Hide emoji picker in chat component.</li>
</ul>
<pre><code class="language-tsx">&lt;RtkMeeting meeting={meeting} overrides={{&#10;  disablePrivateChat: true,&#10;  disableEmojiPicker: true&#10;}} /&gt;&#10;</code></pre>
</li>
</ul>
<p><strong>New components</strong></p>
<ul>
<li><code>rtk-chat-header</code> - Header component with pinned messages and private chat selector.</li>
<li><code>rtk-pinned-message-selector</code> - Displays all pinned messages with paginated infinite scroll.</li>
<li><code>rtk-chat-selector</code> - Switch between public chat and private chats with specific participants.</li>
</ul>
<p><strong>Component enhancements</strong></p>
<ul>
<li><code>rtk-chat-composer-view</code> now accepts <code>isSending</code> prop to display sender messages on the right and other messages on the left with different colors.</li>
<li><code>rtk-chat-messages-ui-paginated</code> now accepts <code>privateChatRecipient</code> prop for displaying paginated private chat messages.</li>
<li><code>rtk-chat-messages-ui-paginated</code> now emits <code>editMessage</code>, <code>deleteMessage</code>, and <code>pinMessage</code> events for message operations.</li>
<li><code>rtk-menu-item</code> and <code>rtk-menu-list</code> now accept <code>menuVariant</code> prop for different color schemes based on user actions.</li>
<li><code>rtk-message-view</code> now accepts <code>isEdited</code>, <code>isSelf</code>, <code>messageType</code>, and <code>pinned</code> props for appropriate message rendering.</li>
<li>Added automatic scrolling to new messages.</li>
</ul>
<p><strong>Breaking changes</strong></p>
<p>Removed non-operational chat channel components to streamline the SDK. <code>rtk-chat</code> remains fully operational.</p>
<ul>
<li>Removed <code>rtk-channel-creator</code>.</li>
<li>Removed <code>rtk-channel-header</code>.</li>
<li>Removed <code>rtk-channel-details</code>.</li>
<li>Removed <code>rtk-channel-selector-ui</code>.</li>
<li>Removed <code>rtk-channel-selector-view</code>.</li>
<li><code>rtk-chat-composer-ui</code> no longer accepts <code>channelId</code> prop.</li>
<li><code>rtk-chat</code> no longer accepts <code>disablePrivateChat</code> prop. Use preset configuration instead, or pass as override:
<pre><code class="language-tsx">&lt;RtkMeeting meeting={meeting} overrides={{disablePrivateChat: true}} /&gt;&#10;</code></pre>
</li>
</ul>
<p><strong>Deprecations</strong></p>
<ul>
<li><code>rtk-chat-composer-ui</code> is deprecated due to scalability limitations and lack of pagination support.</li>
</ul>
<p><strong>Removed localization keys</strong></p>
<ul>
<li><code>ai.chat.summarise</code></li>
<li><code>ai.chat.agenda</code></li>
<li><code>chat.new_channel</code></li>
<li><code>chat.channel_name</code></li>
<li><code>chat.channel_members</code></li>
</ul>
<p><strong>Renamed localization keys</strong></p>
<ul>
<li><code>chat.empty_channel</code> → <code>chat.empty_chat</code></li>
</ul>
<p><strong>Known limitations</strong></p>
<ul>
<li>Total message count for public and private chats is not currently displayed.</li>
</ul><h2 id="2025-12-17">2025-12-17</h2><strong>RealtimeKit Web UI Kit 1.0.8</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed iOS issue where the chat compose view would zoom when typing a message.</li>
</ul><h2 id="2025-11-18">2025-11-18</h2><strong>RealtimeKit Web UI Kit 1.0.7</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed alignment issues with unread chat message count, unread polls count, and pending participant stage request count.</li>
<li>Resolved issue where action toggles were incorrectly displayed in participant video preview in the settings component.</li>
</ul><h2 id="2025-10-30">2025-10-30</h2><strong>RealtimeKit Web UI Kit 1.0.6</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue where <code>rtk-debugger</code> displayed audio and video bitrate as <code>0</code>.</li>
<li>Resolved menu visibility for the last participant when the participants list is long.</li>
<li>Fixed <code>rtk-polls</code> not rendering when props were provided after initial mount.</li>
<li>Improved <code>rtk-participant-tile</code> audio visualizer appearance when muted (no longer shows as a single dot).</li>
<li>Prevented large notifications from overflowing their container.</li>
<li>Fixed a memory leak in the <code>mediaConnectionUpdate</code> event listener.</li>
<li>Corrected <code>rtk-ui-provider</code> prop passing to children during consecutive meetings on the same page.</li>
</ul>
<p><strong>New localization keys</strong></p>
<ul>
<li><code>network.troubleshoot</code> — &quot;Troubleshoot your connection&quot;</li>
</ul><h2 id="2025-08-14">2025-08-14</h2><strong>RealtimeKit Web UI Kit 1.0.5</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed Safari CSS issues where the <code>rtk-settings</code> component was not visible and the Audio Playback modal was not taking the proper height.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>Livestream viewer now has a seeker and DVR functionality.</li>
</ul><h2 id="2025-07-17">2025-07-17</h2><strong>RealtimeKit Web UI Kit 1.0.4</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed Angular integration issues.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>Added support for multiple meetings on the same page in RealtimeKit.</li>
<li>Enhanced the <code>rtk-ui-provider</code> component to serve as a parent component for sharing common props (<code>meeting</code>, <code>config</code>, <code>iconPack</code>) with all child components.</li>
</ul><h2 id="2025-07-08">2025-07-08</h2><strong>RealtimeKit Web UI Kit 1.0.3</strong><p><strong>Fixes</strong></p>
<ul>
<li>Resolved <code>TypeError</code> that occurred for meetings without titles.</li>
<li>Implemented minor UI improvements for chat components.</li>
</ul>
<p><strong>Features</strong></p>
<ul>
<li>Made Livestream feature available to all beta users.</li>
</ul><h2 id="2025-07-02">2025-07-02</h2><strong>RealtimeKit Web UI Kit 1.0.2</strong><p><strong>Performance</strong></p>
<ul>
<li>Fixed dependency issues to enhance performance and Angular integration.</li>
</ul><h2 id="2025-06-30">2025-06-30</h2><strong>RealtimeKit Web UI Kit 1.0.1</strong><p><strong>Deprecated API</strong></p>
<ul>
<li>Discontinued Vue UI support.</li>
</ul><h2 id="2025-05-29">2025-05-29</h2><strong>RealtimeKit Web UI Kit 1.0.0</strong><p><strong>Features</strong></p>
<ul>
<li>Initial release of Cloudflare RealtimeKit with support for group calls, webinars, livestreaming, polls, and chat.</li>
</ul>
