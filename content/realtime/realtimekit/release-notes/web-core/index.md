---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-core/
  description: Release notes and changelog for the RealtimeKit Web Core SDK.
  full_title: Web Core SDK · Cloudflare Realtime docs
  head_html: <title>Web Core SDK · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Release notes and changelog for the RealtimeKit Web Core SDK."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-core/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-core/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-core/index.xml"><meta property="og:title" content="Web Core SDK · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Release notes and changelog for the RealtimeKit Web Core SDK."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-core/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-core/#page","headline":"Web Core SDK \u00b7 Cloudflare Realtime docs","description":"Release notes and changelog for the RealtimeKit Web Core SDK.","url":"https://developers.cloudflare.com/realtime/realtimekit/release-notes/web-core/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/release-notes/web-core/
  schema: 1
---
<h2 id="2026-08-24">2026-08-24</h2><strong>RealtimeKit Web Core 2.0.2</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Generated API documentation now identifies class names correctly, providing more accurate type suggestions for TypeScript users.</li>
<li>Starting a recording that is already in progress now returns error code <code>1005</code> instead of the generic error code <code>1000</code>. If your <a href="/realtime/realtimekit/core/#advanced-options"><code>onError</code> callback</a> handles error code <code>1000</code> for this case, update it to handle <code>1005</code>.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed a Babel transpilation error that could occur when consuming ES2015 builds containing <code>RequestError</code>.</li>
<li>Fixed session recovery after SFU timeouts. Participants can now continue hearing and seeing others after a transient SFU API timeout.</li>
<li>Fixed bulk media consumer creation batching to support participant grids with up to 100 participants per page, increased from 24 per page.</li>
</ul><h2 id="2026-07-17">2026-07-17</h2><strong>RealtimeKit Web Core 2.0.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed ES5 builds containing <code>VERSION_PLACEHOLDER</code> in the bundle instead of the actual SDK version.</li>
<li>Fixed SDK initialization failure when the initial socket connection attempt failed, which also prevented plugin store creation. The SDK now retries store creation based on the socket connection state.</li>
</ul><h2 id="2026-06-18">2026-06-18</h2><strong>RealtimeKit Web Core 2.0.0</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit Web UI Kit 2.0.0 or later.</p>
<p>This is a major breaking release. Several deprecated APIs have been removed and the plugin APIs have been completely redesigned. Review the migration guide below carefully before upgrading.</p>
<p><strong>Plugin APIs — complete redesign</strong></p>
<p>Plugins are no longer fetched from the server automatically. You now provide plugin configurations at SDK init time via <code>defaults.plugins</code>.</p>
<p>Before (v1.x):</p>
<pre tabindex="0"><code class="language-ts">// plugins were loaded via API in SDK internally&#10;const meeting = await RealtimeKitClient.init({&#10;  authToken,&#10;});&#10;<p>// Server-hosted plugins were auto-populated&#10;const plugin = meeting.plugins.all.get(pluginId);</p>&#10;<p>// Plugin rendered in an iframe managed by the SDK&#10;plugin.addPluginView(iframeElement, 'plugin-main');</p>&#10;<p>// Permissions checked via meeting.self.permissions.plugins.canStart / canClose&#10;</code></pre></p>
<p>After (v2.0):</p>
<p>A plugin component is any <code>HTMLElement</code>. You can use a custom element, a framework component mounted to a container, or an iframe. The following example embeds a collaborative text editor as a plugin:</p>
<pre tabindex="0"><code class="language-ts">const editor = document.createElement('iframe');&#10;editor.src = 'https://rustpad.io/#WKLJaD';&#10;editor.style.width = '100%';&#10;editor.style.height = '100%';&#10;editor.style.border = 'none';&#10;<p>const meeting = await RealtimeKitClient.init({&#10;authToken,&#10;defaults: {&#10;plugins: [&#10;{&#10;id: 'collaborative-editor', // SDK prefixes this with {meetingId}: to create the namespaced plugin.id&#10;name: 'Collaborative Editor',&#10;icon: 'https://example.com/editor.png',&#10;permissions: {&#10;canActivate: true,&#10;canDeactivate: true,&#10;},&#10;component: editor,&#10;},&#10;],&#10;},&#10;});</p>&#10;<p>// Plugin is registered and available&#10;const plugin = meeting.plugins.all.get(pluginId);</p>&#10;<p>// Activate — state is synced across all participants&#10;await plugin.activate();&#10;</code></pre></p>
<p>For a complete guide on building custom plugins, refer to <a href="/realtime/realtimekit/custom-plugins/build-your-own-plugins/">Build your own plugins</a>. If you need to record plugin content, you must build a <a href="/realtime/realtimekit/recording-guide/create-record-app-using-sdks/">custom recording app</a>.</p>
<p>Key changes:</p>
<ul>
<li>New type exports: <code>ClientPluginConfig</code>, <code>ClientPluginPermissions</code>.</li>
<li>Plugin <code>id</code> is now namespaced: the SDK prefixes your provided <code>id</code> with <code>{meetingId}:</code> to create the internal <code>pluginId</code>.</li>
<li>Plugin activation and deactivation state is now synced via a collaborative store (<code>__rtk_plugins__</code>) instead of dedicated socket messages.</li>
<li>Plugins now have a <code>component</code> property (any <code>HTMLElement</code>) instead of iframe-based rendering via <code>addPluginView</code>.</li>
<li>Per-plugin permissions (<code>plugin.permissions.canActivate</code> / <code>plugin.permissions.canDeactivate</code>) replace the old global <code>meeting.self.permissions.plugins.canStart</code> / <code>meeting.self.permissions.plugins.canClose</code>.</li>
</ul>
<p>Removed plugin APIs:</p>
<ul>
<li><code>plugin.addPluginView(iframe, viewId)</code> — pass an <code>HTMLElement</code> as <code>component</code> in <code>ClientPluginConfig</code> instead.</li>
<li><code>plugin.removePluginView(viewId)</code> — handled automatically by the UI Kit.</li>
<li><code>plugin.enable()</code> — use <code>plugin.activate()</code>.</li>
<li><code>plugin.disable()</code> — use <code>plugin.deactivate()</code>.</li>
<li><code>plugin.sendIframeEvent()</code> — removed. Communicate directly with your component.</li>
<li><code>plugin.baseURL</code> — removed. Plugins are no longer server-hosted.</li>
<li><code>plugin.picture</code> — use <code>plugin.icon</code>.</li>
<li><code>plugin.description</code>, <code>plugin.organizationId</code>, <code>plugin.tags</code>, <code>plugin.type</code>, <code>plugin.staggered</code>, <code>plugin.private</code>, <code>plugin.published</code>, <code>plugin.createdAt</code>, <code>plugin.updatedAt</code> — removed. No longer applicable.</li>
<li><code>plugin.config</code> (PluginConfig) — removed. No plugin manifest concept.</li>
<li><code>meeting.self.permissions.plugins.canStart</code> — use <code>plugin.permissions.canActivate</code>.</li>
<li><code>meeting.self.permissions.plugins.canClose</code> — use <code>plugin.permissions.canDeactivate</code>.</li>
<li><code>modules.devTools.plugins</code> (local dev plugin config) — use <code>defaults.plugins</code> with a <code>component</code> pointing to your local element.</li>
</ul>
<p><strong>Removed deprecated APIs</strong></p>
<p>Client:</p>
<ul>
<li><code>meeting.joinRoom()</code> — use <code>meeting.join()</code>.</li>
<li><code>meeting.leaveRoom()</code> — use <code>meeting.leave()</code>.</li>
</ul>
<p>Chat:</p>
<ul>
<li><code>meeting.chat.getMessagesByUser(userId)</code> — use <code>meeting.chat.fetchPublicMessages()</code> with appropriate filters.</li>
<li><code>meeting.chat.getMessagesByType(type)</code> — use <code>meeting.chat.fetchPublicMessages()</code> with appropriate filters.</li>
<li><code>meeting.chat.getMessages(timestamp, size, reversed)</code> — use <code>meeting.chat.fetchPublicMessages()</code> or <code>meeting.chat.fetchPrivateMessages()</code>.</li>
<li><code>meeting.chat.searchMessages(query, filters)</code> — use <code>meeting.chat.fetchPublicMessages()</code> or <code>meeting.chat.fetchPrivateMessages()</code>.</li>
<li><code>meeting.chat.pinned</code> (getter) — use <code>meeting.chat.fetchPinnedMessages()</code>.</li>
</ul>
<p>Permissions (<code>meeting.self.permissions</code>):</p>
<ul>
<li><code>permissions.produceVideo</code> — use <code>permissions.canProduceVideo</code>.</li>
<li><code>permissions.produceAudio</code> — use <code>permissions.canProduceAudio</code>.</li>
<li><code>permissions.produceScreenshare</code> — use <code>permissions.canProduceScreenshare</code>.</li>
<li><code>permissions.waitingRoomType</code> — use <code>permissions.waitingRoomBehaviour</code>.</li>
<li><code>permissions.canChangeParticipantRole</code> — use <code>permissions.canChangeParticipantPermissions</code>.</li>
<li><code>permissions.canChangeTheme</code> — removed (always returned <code>false</code>).</li>
<li><code>permissions.canPresent</code> — check individual <code>canProduceAudio</code>, <code>canProduceVideo</code>, <code>canProduceScreenshare</code>.</li>
<li><code>permissions.requestProduce</code> — check individual media permissions for <code>CAN_REQUEST</code> values.</li>
<li><code>permissions.acceptPresentRequests</code> — use <code>permissions.acceptStageRequests</code>.</li>
<li><code>permissions.maxScreenShareCount</code> — use <code>meeting.self.config.maxScreenShareCount</code>.</li>
<li><code>PermissionPreset.fromResponse()</code> — use <code>PermissionPreset.init()</code>.</li>
<li><code>PermissionPreset.default()</code> — use <code>PermissionPreset.init()</code>.</li>
</ul>
<p>Participants:</p>
<ul>
<li><code>meeting.participants.disableAudio(participantId)</code> — use <code>meeting.participants.joined.get(participantId).disableAudio()</code>.</li>
<li><code>meeting.participants.disableVideo(participantId)</code> — use <code>meeting.participants.joined.get(participantId).disableVideo()</code>.</li>
<li><code>meeting.participants.kick(participantId)</code> — call kick on the participant directly.</li>
<li><code>participant.clientSpecificId</code> — use <code>participant.customParticipantId</code>.</li>
</ul>
<p>Connected Meetings:</p>
<ul>
<li><code>meeting.connectedMeetings.supportsConnectedMeetings</code> — removed. Permission checks are now granular via <code>meeting.self.permissions.connectedMeetings</code>.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>Faster reconnection: Socket-only disconnects (where WebRTC transports remain healthy) now skip full transport re-setup. Producers are re-registered and existing consumers are remapped, significantly reducing reconnection time.</li>
<li>Participants stay visible during reconnection: Participant tiles remain in the grid during a socket blip instead of disappearing and reappearing, providing a seamless experience.</li>
<li>Double audio fix: Fixed an issue where other participants could hear double audio from a reconnected participant, caused by stale producers not being cleaned up.</li>
<li>Socket reconnection resilience: Socket now supports up to 50 reconnection attempts with exponential backoff and jitter (up from 10), providing up to approximately four minutes of retry coverage when the internet is down.</li>
<li>Store improvements: <code>StoreManager</code> now supports <code>refresh(name)</code> to re-fetch store data from the server, and reserved store names (<code>__rtk_plugins__</code>) are protected from user creation.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed socket failing to reconnect if left disconnected for 30 seconds.</li>
</ul><h2 id="2026-05-28">2026-05-28</h2><strong>RealtimeKit Web Core 1.5.1</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit Web UI Kit 1.2.0 or later.</p>
<p><strong>Features</strong></p>
<ul>
<li>Added a dedicated error code <code>0014</code> for media (WebRTC) connection failures during room join, making it easier to distinguish media failures from socket and signaling failures.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>Init and join failures from <code>Client.init()</code> and <code>meeting.join()</code> now surface specific error codes and descriptive messages instead of generic or stacked errors.</li>
<li>Telemetry logs are now compressed using gzip when the browser supports the <code>CompressionStream</code> API, achieving approximately a 10:1 compression ratio. Older browsers and React Native fall back to uncompressed JSON with smaller batch sizes.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed a regex-based issue where the Safari video middleware flag was incorrectly removed, potentially breaking video processing on Safari.</li>
<li>Fixed an issue where <code>ClientError</code> objects were wrapped inside each other when the SDK retried failed API requests. This caused nested error messages, duplicate <code>onError</code> callbacks, and redundant <code>window</code> error events.</li>
</ul>
<p><strong>Removed APIs</strong></p>
<ul>
<li>Removed the third-party flag service. <code>meeting.__internals__.features</code> is now deprecated and will be removed in a future release.</li>
</ul><h2 id="2026-04-20">2026-04-20</h2><strong>RealtimeKit Web Core 1.4.0</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit Android Core 2.0.0+ and RealtimeKit iOS Core 2.0.0+.</p>
<p><strong>Features</strong></p>
<ul>
<li>Added <code>meeting.__internals__.authToken</code> to expose authentication token, enabling better integration between Web Core and UI Kit for future features and enhancements.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Proactively fixed an issue where participants with simulcast turned on would not be able to turn on their camera or microphone due to SDP failures in Chrome version 148+.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>SDK now uses <code>*.realtime.cloudflare.com</code> base URI internally instead of the legacy <code>dyte.io</code> base URI.</li>
<li>Refactored error handling to properly catch and display error codes for SDK initialization failures, room join failures, and other errors.</li>
</ul><h2 id="2026-03-31">2026-03-31</h2><strong>RealtimeKit Web Core 1.3.0</strong><p><strong>Features</strong></p>
<ul>
<li>Simulcast support is now available to all RealtimeKit clients. Configure it per participant in Preset via the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">RealtimeKit dashboard</a>, <a href="https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/create">Preset API</a> using the <code>config.media.video.simulcast</code> field, or while <a href="/realtime/realtimekit/core/">initializing the SDK</a>.</li>
<li>Added 4K UHD video support in media production (configurable in Preset and API). Falls back to the maximum supported resolution if the camera does not support 4K.</li>
</ul><h2 id="2026-03-10">2026-03-10</h2><strong>RealtimeKit Web Core 1.2.5</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit Web UI Kit 1.1.1 or later.</p>
<p><strong>Enhancements</strong></p>
<ul>
<li>Implemented retry limits for ICE connection failures to prevent indefinite connection attempts and improve reliability.</li>
<li>Improved error handling for room join operations to provide more descriptive and actionable error messages.</li>
<li>Room join errors are now thrown consistently when network connectivity is blocked by firewalls or when TURN servers are unreachable.</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue in Connected Meetings where peer IDs were not regenerated when switching between rooms. Peer IDs are now correctly assigned per room session.</li>
</ul><h2 id="2026-01-30">2026-01-30</h2><strong>RealtimeKit Web Core 1.2.4</strong><p><strong>Compatibility:</strong> Works best with RealtimeKit Web UI Kit 1.1.0 or later.</p>
<p><strong>New APIs</strong></p>
<p>Added chat pagination support with the following methods:</p>
<ul>
<li><code>meeting.chat.fetchPinnedMessages</code> - Fetch pinned messages from server.</li>
<li><code>meeting.chat.fetchPublicMessages</code> - Fetch public messages from server.</li>
<li><code>meeting.chat.fetchPrivateMessages</code> - Fetch private messages from server.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>Added JSDoc comments to all public-facing methods and classes for improved developer suggestions.</li>
<li>Chat message operations (edit, delete, pin) are now available to all RealtimeKit clients without additional configuration.</li>
<li><code>pinMessage</code> and <code>unpinMessage</code> events on <code>meeting.chat</code> now emit reliably.</li>
<li>Message pinning (<code>meeting.chat.pin</code> and <code>meeting.chat.unpin</code>) is now available to all participants.</li>
</ul>
<p><strong>Removed APIs</strong></p>
<p>Removed non-operational chat channel APIs to streamline the RealtimeKit SDK. Meeting chat (<code>meeting.chat</code>) remains fully operational.</p>
<ul>
<li>Removed <code>meeting.self.permissions.chatChannel</code>.</li>
<li>Removed <code>meeting.self.permissions.chatMessage</code>. Use <code>meeting.self.permissions.chatPublic</code> and <code>meeting.self.permissions.chatPrivate</code> instead.</li>
<li>Removed <code>meeting.chat.channels</code>.</li>
<li>Removed <code>meeting.chat.sendMessageToChannel</code>.</li>
<li>Removed <code>meeting.chat.markLastReadMessage</code>.</li>
<li>Removed events: <code>channelMessageUpdate</code>, <code>channelCreate</code>, and <code>channelUpdate</code> from <code>meeting.chat</code>.</li>
</ul>
<p><strong>API changes</strong></p>
<ul>
<li>The following methods no longer accept a third optional <code>channelId</code> parameter:
<ul>
<li><code>meeting.chat.editTextMessage(messageId, message)</code></li>
<li><code>meeting.chat.editImageMessage(messageId, imageFile)</code></li>
<li><code>meeting.chat.editFileMessage(messageId, file)</code></li>
<li><code>meeting.chat.editMessage(messageId, messagePayload)</code></li>
<li><code>meeting.chat.deleteMessage(messageId)</code></li>
</ul>
</li>
</ul>
<p><strong>Deprecations</strong></p>
<p>The following methods are deprecated due to scalability limitations (limited to 1,000 recent messages):</p>
<ul>
<li><code>meeting.chat.messages</code> - Only fetches recent messages and new messages after joining.</li>
<li><code>meeting.chat.getMessagesByUser</code> - Use new fetch methods for scalable message retrieval.</li>
<li><code>meeting.chat.getMessagesByType</code> - Use new fetch methods for scalable message retrieval.</li>
<li><code>meeting.chat.getMessages</code> - Use <code>meeting.chat.fetchPublicMessages</code> or <code>meeting.chat.fetchPrivateMessages</code> instead.</li>
<li><code>meeting.chat.pinned</code> - Use <code>meeting.chat.fetchPinnedMessages</code> instead.</li>
<li><code>meeting.chat.searchMessages</code> - Use <code>meeting.chat.fetchPublicMessages</code> or <code>meeting.chat.fetchPrivateMessages</code> instead.</li>
</ul>
<p><strong>Known limitations</strong></p>
<ul>
<li>Pinned messages are not supported for private chats.</li>
</ul><h2 id="2026-01-05">2026-01-05</h2><strong>RealtimeKit Web Core 1.2.3</strong><p><strong>Fixes</strong></p>
<ul>
<li>
<p>Fixed an issue where users who joined a meeting with audio and video disabled and then initiated tab screen sharing would experience SDP corruption upon stopping the screen share, preventing subsequent actions such as enabling audio or video.</p>
<p>Error thrown:</p>
<pre tabindex="0"><code class="language-text">InvalidAccessError: Failed to execute 'setRemoteDescription' on 'RTCPeerConnection': Failed to set remote answer sdp: Failed to set remote audio description send parameters for m-section with mid='&lt;N&gt;'&#10;</code></pre>
</li>
<li>
<p>Fixed an issue where awaiting <code>RealtimeKitClient.initMedia</code> did not return media tracks</p>
<p>Example usage:</p>
<pre tabindex="0"><code class="language-ts">const media = await RealtimeKitClient.initMedia({&#10;  video : true,&#10;  audio: true,&#10;});&#10;<p>const { videoTrack, audioTrack } = media;&#10;</code></pre></p>
</li>
<li>
<p>Fixed an issue where an undefined variable caused <code>TypeError: Cannot read properties of undefined (reading 'getValue')</code> in media retrieval due to a race condition.</p>
</li>
</ul><h2 id="2025-12-17">2025-12-17</h2><strong>RealtimeKit Web Core 1.2.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed an issue where camera switching between front and rear cameras was not working on Android devices</li>
<li>Fixed device selection logic to prioritize media devices more effectively</li>
<li>Added PIP support for <a href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/addons/#reactions-1">Reactions</a></li>
</ul><h2 id="2025-11-18">2025-11-18</h2><strong>RealtimeKit Web Core 1.2.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Resolved an issue preventing default media device selection.</li>
<li>Fixed SDK bundle to include <code>browser.js</code> instead of incorrectly shipping <code>index.iife.js</code> in 1.2.0.</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>External media devices are now prioritized over internal devices when no preferred device is set.</li>
</ul><h2 id="2025-10-30">2025-10-30</h2><strong>RealtimeKit Web Core 1.2.0</strong><p><strong>Features</strong></p>
<ul>
<li>
<p>Added support for configuring simulcast via <code>initMeeting</code>:</p>
<pre tabindex="0"><code class="language-ts">initMeeting({&#10;  overrides: {&#10;    simulcastConfig: {&#10;      disable: false,&#10;      encodings: [{ scaleResolutionDownBy: 2 }],&#10;    },&#10;  },&#10;});&#10;</code></pre>
</li>
</ul>
<p><strong>Fixes</strong></p>
<ul>
<li>Resolved an issue where remote participants' video feeds were not visible during grid pagination in certain edge cases.</li>
<li>Fixed a bug preventing participants from switching microphones if the first listed microphone was non-functional.</li>
</ul>
<p><strong>Breaking changes</strong></p>
<ul>
<li>Legacy media engine support has been removed. If your organization was created before March 1, 2025 and you are upgrading to this SDK version or later, you may experience recording issues. Contact support to migrate to the new Cloudflare SFU media engine to ensure continued recording functionality.</li>
</ul><h2 id="2025-08-26">2025-08-26</h2><strong>RealtimeKit Web Core 1.1.7</strong><p><strong>Fixes</strong></p>
<ul>
<li>Prevented speaker change events from being emitted when the active speaker does not change.</li>
<li>Addressed a behavioral change in microphone switching on recent versions of Google Chrome.</li>
<li>Added <code>deviceInfo</code> logs to improve debugging capabilities for React Native.</li>
<li>Fixed an issue that queued multiple media consumers for the same peer, optimizing resource usage.</li>
</ul><h2 id="2025-08-14">2025-08-14</h2><strong>RealtimeKit Web Core 1.1.6</strong><p><strong>Enhancements</strong></p>
<ul>
<li>Internal changes to make debugging of media consumption issues easier and faster.</li>
</ul><h2 id="2025-08-04">2025-08-04</h2><strong>RealtimeKit Web Core 1.1.5</strong><p><strong>Fixes</strong></p>
<ul>
<li>Improved React Native support for <code>AudioActivityReporter</code> with proper audio sampling.</li>
<li>Resolved issue preventing users from creating polls.</li>
<li>Fixed issue where leaving a meeting took more than 20 seconds.</li>
</ul><h2 id="2025-07-17">2025-07-17</h2><strong>RealtimeKit Web Core 1.1.4</strong><p><strong>Fixes</strong></p>
<ul>
<li>Livestream feature is now available to all beta users.</li>
<li>Fixed Livestream stage functionality where hosts were not consuming peer videos upon participants' stage join.</li>
<li>Resolved issues with viewer joins and leaves in Livestream stage.</li>
</ul><h2 id="2025-07-08">2025-07-08</h2><strong>RealtimeKit Web Core 1.1.3</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed issue where users could not enable video mid-meeting if they joined without video initially.</li>
</ul><h2 id="2025-07-02">2025-07-02</h2><strong>RealtimeKit Web Core 1.1.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Fixed edge case in large meetings where existing participants could not hear or see newly joined users.</li>
</ul><h2 id="2025-06-30">2025-06-30</h2><strong>RealtimeKit Web Core 1.1.0–1.1.1</strong><p><strong>Features</strong></p>
<ul>
<li>Added methods to toggle self tile visibility.</li>
<li>Introduced broadcast functionality across connected meetings (breakout rooms).</li>
</ul>
<p><strong>New API</strong></p>
<ul>
<li>
<p>Broadcast messages across meetings:</p>
<pre tabindex="0"><code class="language-ts">meeting.participants.broadcastMessage(&quot;&lt;message_type&gt;&quot;, { message: &quot;Hi&quot; }, {&#10;  meetingIds: [&quot;&lt;connected_meeting_id&gt;&quot;],&#10;});&#10;</code></pre>
</li>
</ul>
<p><strong>Enhancements</strong></p>
<ul>
<li>Reduced time to display videos of newly joined participants when joining in bulk.</li>
<li>Added support for multiple meetings on the same page in RealtimeKit Core SDK.</li>
</ul><h2 id="2025-06-17">2025-06-17</h2><strong>RealtimeKit Web Core 1.0.2</strong><p><strong>Fixes</strong></p>
<ul>
<li>Enhanced error handling for media operations.</li>
<li>Fixed issue where active participants with audio or video were not appearing in the active participant list.</li>
</ul><h2 id="2025-05-29">2025-05-29</h2><strong>RealtimeKit Web Core 1.0.1</strong><p><strong>Fixes</strong></p>
<ul>
<li>Resolved initial setup issues with Cloudflare RealtimeKit integration.</li>
<li>Fixed meeting join and media connectivity issues.</li>
<li>Enhanced media track handling.</li>
</ul><h2 id="2025-05-29-1">2025-05-29</h2><strong>RealtimeKit Web Core 1.0.0</strong><p><strong>Features</strong></p>
<ul>
<li>Initial release of Cloudflare RealtimeKit with support for group calls, webinars, livestreaming, polls, and chat.</li>
</ul>
