---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/
  description: Configure participant roles, permissions, and meeting experience with RealtimeKit presets.
  full_title: Preset · Cloudflare Realtime docs
  head_html: <title>Preset · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure participant roles, permissions, and meeting experience with RealtimeKit presets."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/index.md"><meta property="og:title" content="Preset · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure participant roles, permissions, and meeting experience with RealtimeKit presets."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/#page","headline":"Preset \u00b7 Cloudflare Realtime docs","description":"Configure participant roles, permissions, and meeting experience with RealtimeKit presets.","url":"https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/concepts/preset/
  schema: 1
---
<p>A Preset is a <strong>re-usable configuration</strong> that defines a participant’s experience in a Meeting.
It determines:</p>
<ul>
<li>The meeting type they join (Video, Audio, Webinar, or Livestream <div class="nb-r-t-k-pill"></li>
</ul>
@markup("md", "content/.markup/bodies/12467.md")
</div>)
- Actions they can perform (permissions and controls)
- The UI’s look and feel, including colors and themes, so the experience matches your application's branding.
<p>Presets belong to an App, and they are applied to participants — not to meetings.</p>
<p>You can assign the same Preset to multiple participants when creating them through the Add Participant API. Participants in the same Meeting can have different Presets, allowing each user to have a distinct role and experience.</p>
<p>Example: Large Ed-Tech Classroom</p>
<ul>
<li><strong>Teacher</strong> uses the <code>webinar-host</code> preset — they can share media and access host controls.</li>
<li><strong>Students</strong> use the <code>webinar-participant</code> preset — they cannot share media but can use features like chat.</li>
<li><strong>Teaching</strong> assistant uses the <code>group-call-host</code> preset — they can share media but don’t have full host privileges.</li>
</ul>
<h3 id="create-a-preset">Create a Preset</h3>
<p>A set of default presets are created for you, when you create an app via the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">Cloudflare dashboard</a>.</p>
<p>You can also create a preset using the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">dashboard</a> or the <a href="/api/resources/realtime_kit/subresources/presets/methods/create/">Create Preset API</a>.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/presets \&#10;    &#45;H &#x27;Content-Type: application/json&#x27; \&#10;    &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;    &#45;d &#x27;{&#10;          &quot;config&quot;: {&#10;            ...&lt;preset-configuration-json&gt;&#10;        }&#x27;&#10;</code></pre>
<h3 id="preset-editor">Preset Editor</h3>
<p>We provide a UI-based editor to create and manage the presets in the <a href="https://dash.cloudflare.com/?to=/:account/realtime/kit">Cloudflare dashboard</a>.</p>
<p><img src="/assets/upstream/images/realtime/realtimekit/preset-editor.png" alt="Preset Editor" /></p>
<p>The permissions are divided into the following categories:</p>
<ul>
<li>
<p><strong>Host Controls:</strong> These permissions allow the user to control the meeting, manage participants, and perform administrative actions like kicking users, muting video/audio for others and more.</p>
</li>
<li>
<p><strong>Stage Management:</strong> Large meetings can be configured with a virtual stage. Participants on the stage can share their audio and video, while participants off the stage can view this media and still use features like chat, polls, and plugins.</p>
<pre tabindex="0"><code>  Users can request to join the stage, host can add/remove users from the stage at any point.&#10;  Read more about stage management in [Meetings](/realtime/realtimekit/concepts/meeting#stage).&#10;</code></pre>
</li>
<li>
<p><strong>Chat:</strong> RealtimeKit allows users to send and receive messages in real time. You can also send private messages (visible only to a specific user). You can configure who has access to send &amp; messages and receive various kinds of messages.</p>
</li>
<li>
<p><strong>Polls:</strong> Allows user to configure who can create, view and interact with polls in the meeting.</p>
</li>
<li>
<p><strong>Plugins:</strong> Plugins are interactive real-time applications that run inside the meeting to make collaboration easier. RealtimeKit lets you build your own plugins and also offers built-in options like Whiteboard and Document Sharing.</p>
<pre tabindex="0"><code>  You can control which plugins a participant is allowed to view, open, or close.&#10;</code></pre>
</li>
<li>
<p><strong>Waiting Room:</strong> A waiting room allows participants to join a meeting before they’re admitted, giving hosts control over who enters and when. It helps manage access, reduce interruptions, and ensure the meeting starts smoothly.</p>
<pre tabindex="0"><code>  Hosts can admit or remove participants at any time, and you can configure who should bypass the waiting room automatically.&#10;  Read more about waiting rooms in [Meetings](/realtime/realtimekit/concepts/meeting#waiting-room).&#10;</code></pre>
</li>
<li>
<p><strong>Connected Meetings:</strong> Connected Meetings let you split a main meeting into linked spaces for smaller group discussions or parallel sessions. Permissions determine whether participants can move between connected meetings, return to the parent meeting, or create, update, and delete those meetings.</p>
<pre tabindex="0"><code>  Read more about connected meetings in [Meetings](/realtime/realtimekit/concepts/meeting#connected-meetings).&#10;</code></pre>
</li>
<li>
<p><strong>Miscellaneous:</strong> Miscellaneous permissions let you fine-tune additional aspects of the participant experience that don’t fall under specific categories.</p>
<pre tabindex="0"><code>  These options control capabilities like - editing names, viewing the participant list, syncing tab views, enabling transcriptions, and other supplementary features that enhance how users interact within the meeting.&#10;</code></pre>
</li>
</ul>
<h3 id="where-to-go-next">Where to Go Next</h3>
<p>After learning about Meetings and Sessions, you can explore the following next steps:</p>
<ul>
<li>Add <a href="/realtime/realtimekit/concepts/participant">Participants</a> to a Meeting – Manage who can join, their roles, and the access controls they inherit.</li>
<li>Get started with <a href="/realtime/realtimekit/quickstart/">RealtimeKit SDKs</a> – Integrate RealtimeKit into your web or mobile app with just a few lines of code.</li>
</ul>
