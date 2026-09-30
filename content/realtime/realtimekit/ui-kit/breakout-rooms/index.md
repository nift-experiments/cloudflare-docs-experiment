---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/
  description: Create and manage breakout rooms in RealtimeKit meetings for smaller group discussions.
  full_title: Breakout Rooms · Cloudflare Realtime docs
  head_html: <title>Breakout Rooms · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and manage breakout rooms in RealtimeKit meetings for smaller group discussions."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/index.md"><meta property="og:title" content="Breakout Rooms · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and manage breakout rooms in RealtimeKit meetings for smaller group discussions."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/#page","headline":"Breakout Rooms \u00b7 Cloudflare Realtime docs","description":"Create and manage breakout rooms in RealtimeKit meetings for smaller group discussions.","url":"https://developers.cloudflare.com/realtime/realtimekit/ui-kit/breakout-rooms/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/ui-kit/breakout-rooms/
  schema: 1
---
<h3 id="code-examples">Code Examples</h3>
<p>If you prefer to learn by seeing examples, please check out the respective example repositories.</p>
<h4 id="web-examples">Web Examples</h4>
- [Web Components](https://github.com/cloudflare/realtimekit-web-examples/tree/main/html-examples/examples/default-meeting-ui)
- [React](https://github.com/cloudflare/realtimekit-web-examples/tree/main/react-examples/examples/default-meeting-ui)
- [Angular](https://github.com/cloudflare/realtimekit-web-examples/tree/main/angular-examples/examples/default-meeting-ui)
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11778.md")
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
<h3 id="start-breakout-room">Start breakout room</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11779.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11780.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11781.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11782.md")
</div>
<h2 id="integrate-breakout-rooms">Integrate breakout rooms</h2>
<p>After setting up breakout rooms via the API, you need to integrate them into your application using the RealtimeKit SDK.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h3 id="initialize-the-sdk-with-breakout-rooms-support">Initialize the SDK with breakout rooms support</h3>
<p>Initialize the SDK and add an event handler for breakout rooms:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11783.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11784.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11785.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11786.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11787.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11788.md")
</div>
<h3 id="render-the-meeting-ui">Render the meeting UI</h3>
<p>Use the default meeting UI component which includes built-in breakout room support:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11789.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11790.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11791.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11792.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11793.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/11794.md")
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
