---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/breakout-rooms/
  description: Create and manage breakout rooms to split participants into smaller groups in RealtimeKit.
  full_title: Breakout Rooms · Cloudflare Realtime docs
  head_html: <title>Breakout Rooms · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage breakout rooms to split participants into smaller groups in RealtimeKit."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/breakout-rooms/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/breakout-rooms/index.md"><meta property="og:title" content="Breakout Rooms · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage breakout rooms to split participants into smaller groups in RealtimeKit."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/breakout-rooms/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Content"><meta name="algolia_content_type" content="Content"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/breakout-rooms/#page","headline":"Breakout Rooms \u00b7 Cloudflare Realtime docs","description":"Create and manage breakout rooms to split participants into smaller groups in RealtimeKit.","url":"https://developers.cloudflare.com/realtime/realtimekit/core/breakout-rooms/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/breakout-rooms/
  schema: 1
---
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12424.md")
</aside>
<p>Breakout rooms allow participants of a meeting to split into smaller groups for targeted discussions and collaboration. With the rise of remote work and online learning, breakout rooms have become an essential tool for enhancing engagement and building community in virtual settings. They are an ideal choice for workshops, online classrooms, or when you need to speak privately with select participants outside the main meeting.</p>
<p>In RealtimeKit, breakout rooms are created as a separate meeting. Each breakout room is an independent meeting and can be managed like any other RealtimeKit meeting. RealtimeKit provides a set of SDK APIs to create, manage, and switch between breakout rooms.</p>
<h2 id="key-features">Key features</h2>
<p>The following are some of the key features of RealtimeKit's breakout rooms:</p>
<ul>
<li>Manage permissions and privileges of hosts and participants using presets</li>
<li>Hosts can create breakout rooms, assign participants, start and close the breakout rooms, and switch between rooms</li>
<li>Participants can start and stop video, interact with other participants using chat and polls, and mute/unmute audio</li>
<li>Record all breakout sessions individually like any other RealtimeKit meeting</li>
</ul>
<h2 id="roles-in-a-breakout-room">Roles in a breakout room</h2>
<p>Roles in the breakout room are managed by presets.</p>
<h3 id="host">Host</h3>
<p>Hosts can create breakout rooms, assign participants, start and close the breakout rooms, and switch between rooms.</p>
<h3 id="participants">Participants</h3>
<p>As a participant in a breakout room, you can:</p>
<ul>
<li><strong>Switch to Parent Meeting</strong> - Switch back to the main meeting (if you have the required permissions)</li>
<li><strong>Switch Connected Meetings</strong> - Move from the main meeting to smaller, focused discussion groups (breakout rooms) for collaboration</li>
<li><strong>Collaborate</strong> - Use tools such as chat and polls during breakout sessions</li>
</ul>
<h2 id="audio-and-video">Audio and video</h2>
<p>Each breakout room functions as an independent meeting. When you switch to a breakout room from the main meeting, it automatically switches to the audio and video of the breakout session. You can mute or unmute your audio and start or stop your video at any time during the breakout session, just as you can in the main meeting.</p>
<p>When the breakout session ends, your audio and video automatically switch back to the main meeting.</p>
<ul>
<li>If your video was turned on during a breakout session, it will remain on when you return to the main session</li>
<li>If your microphone was on during a breakout session, it will stay on when you return to the main session</li>
</ul>
<h2 id="recording-breakout-sessions">Recording breakout sessions</h2>
<p>Each breakout session is a separate session. Each breakout session's recording is stored and managed separately, just like any other RealtimeKit meeting. For more information, refer to <a href="/realtime/realtimekit/recording-guide/">Recording</a>.</p>
<h2 id="breakout-rooms-management">Breakout rooms management</h2>
<p>Breakout rooms allow the participants to split into separate sessions. The host can create breakout rooms, assign participants, start and close the breakout rooms.</p>
<h3 id="create-presets">Create presets</h3>
<p>A preset is a set of permissions and UI configurations that are applied to hosts and participants. They determine the look, feel, and behavior of the breakout room.</p>
<p>For breakout rooms, you must provide the following permissions for hosts and participants in Connected Meetings:</p>
<h4 id="host-1">Host</h4>
<p>The host preset should have <strong>Full Access</strong> permission in Connected Meetings. This allows the host to:</p>
<ul>
<li>Create breakout rooms</li>
<li>Assign participants to rooms</li>
<li>Start and close breakout rooms</li>
<li>Switch between rooms</li>
</ul>
<h4 id="participants-1">Participants</h4>
<p>You can choose to provide the following permissions to participants:</p>
<ul>
<li><strong>Switch Connected Meetings</strong> - Allows participants to move between breakout rooms</li>
<li><strong>Switch to Parent Meeting</strong> - Allows participants to return to the main meeting</li>
</ul>
<h3 id="save-the-preset">Save the preset</h3>
<ol>
<li>Once you have made all the changes to your preset, click <strong>Save</strong></li>
<li>Enter a name for your preset and click <strong>Save</strong></li>
<li>Your preset is listed - click <strong>Edit</strong> to make any changes</li>
</ol>
<h3 id="create-a-meeting">Create a meeting</h3>
<p>Create a RealtimeKit meeting using the <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">Create meeting API</a>. This API returns a unique identifier for your meeting.</p>
<h3 id="add-participants">Add participants</h3>
<p>After creating the meeting, add each participant using the <a href="/api/resources/realtime_kit/subresources/meetings/methods/add_participant/">Add participant API</a>. The <code>presetName</code> created earlier must be passed in the body of the Add Participant API request.</p>
<h3 id="validate-permissions">Validate permissions</h3>
<p>Before creating breakout rooms, validate the permissions of the current participant to ensure that the participant has the required permissions to create breakout rooms. Incorrect permissions can lead to errors being thrown.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12425.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12426.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12427.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12428.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12429.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12430.md")
</div>
<h3 id="create-breakout-rooms">Create breakout rooms</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12431.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12432.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12433.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12434.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12435.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12436.md")
</div>
<h3 id="retrieve-list-of-breakout-rooms-and-their-participants">Retrieve list of breakout rooms and their participants</h3>
<p>If there are more than one host in the room creating breakouts, you can retrieve consolidated list of breakout rooms using the following API.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12437.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12438.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12439.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12440.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12441.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12442.md")
</div>
<h3 id="move-participants-to-breakout-rooms">Move participants to breakout rooms</h3>
<p>Once you have created breakout rooms, assign participants to the rooms.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12443.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12444.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12445.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12446.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12447.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12448.md")
</div>
<h3 id="move-participants-with-a-specific-preset-to-breakout-rooms">Move participants, with a specific preset, to breakout rooms</h3>
<p>Once you have created breakout rooms, assign participants to the rooms.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12449.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12450.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12451.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12452.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12453.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12454.md")
</div>
<h3 id="move-local-participant-to-breakout-room">Move local participant to breakout room</h3>
<p>To move the local participant to a different breakout room or back to the parent meeting, use the same API as for moving other participants, but pass the local participant's ID. The local participant must have the appropriate permissions: <code>canSwitchConnectedMeetings</code> to switch between breakout rooms, or <code>canSwitchToParentMeeting</code> to return to the parent meeting, if the request was originated by the non-host local participant.</p>
<h3 id="handle-breakout-room-events">Handle breakout room events</h3>
<p>If a participant has been moved to a breakout room, the <code>changingMeeting</code> event is triggered, followed by the <code>meetingChanged</code> event. These events are also triggered when a participant switches between the main meeting and breakout rooms. Participants will autojoin the breakout room if they are assigned to it. You won't have to join meeting explicitly.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12455.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12456.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12457.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12458.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12459.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12460.md")
</div>
<h3 id="close-breakout-rooms">Close breakout rooms</h3>
<p>You can close/delete the breakout rooms. This will force participants in those meetings to come to the main room.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12461.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12462.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12463.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12464.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12465.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12466.md")
</div>
<h2 id="next-steps">Next steps</h2>
<p>You have successfully integrated breakout rooms into your RealtimeKit application. Participants can now:</p>
<ul>
<li>Join the main meeting</li>
<li>Be assigned to breakout rooms by the host</li>
<li>Switch between the main meeting and breakout rooms</li>
<li>Collaborate in smaller focused groups</li>
</ul>
<p>For more advanced customization, explore the following:</p>
<ul>
<li><a href="/realtime/realtimekit/ui-kit/component-library/">UI Kit Components Library</a> - Browse available components</li>
<li><a href="/realtime/realtimekit/ui-kit/state-management/">UI Kit States</a> - Learn how components synchronize</li>
<li><a href="/realtime/realtimekit/ui-kit/build-your-own-ui/">Build Your Own UI</a> - Create custom meeting interfaces</li>
</ul>
