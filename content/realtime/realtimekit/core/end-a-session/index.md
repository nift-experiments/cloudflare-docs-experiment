---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/
  description: End a RealtimeKit session for all participants and stop active recordings.
  full_title: End a session · Cloudflare Realtime docs
  head_html: <title>End a session · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="End a RealtimeKit session for all participants and stop active recordings."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/index.md"><meta property="og:title" content="End a session · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="End a RealtimeKit session for all participants and stop active recordings."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/#page","headline":"End a session \u00b7 Cloudflare Realtime docs","description":"End a RealtimeKit session for all participants and stop active recordings.","url":"https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/end-a-session/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/12329.md")
</aside>
<p>To end the current <a href="/realtime/realtimekit/concepts/meeting/#session/">session</a> for all participants, remove all participants using <code>kickAll()</code>. This stops any ongoing recording for that session and sets the session status to <code>ENDED</code>.</p>
<p>Ending a session is different from leaving a meeting. Leaving disconnects only the current participant. The session remains active if other participants are still present.</p>
<h2 id="steps">Steps</h2>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<ol>
<li>Check that the local participant has permission to remove participants.</li>
</ol>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12330.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12331.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12332.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12333.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12334.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12335.md")
</div>
<ol start="2">
<li>End the session by removing all participants.</li>
</ol>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12336.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12337.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12338.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12339.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12340.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12341.md")
</div>
<ol start="3">
<li>Listen for the session end event.</li>
</ol>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12342.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12343.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12344.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12345.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12346.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12347.md")
</div>
<p>You can also end a session from your backend by removing all participants using the <a href="/api/resources/realtime_kit/subresources/active-session/methods/kick_all_participants/">Kick all participants</a> API.</p>
<h2 id="end-a-session-from-your-backend">End a session from your backend</h2>
<h3 id="remove-all-participants-with-the-api">Remove all participants with the API</h3>
<p>Use the <a href="/api/resources/realtime_kit/subresources/active-session/methods/kick_all_participants/">Kick all participants</a> API method to remove all participants from an active session for a meeting.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="listen-for-session-end-events-with-webhooks">Listen for session end events with webhooks</h3>
<p>Register a webhook that subscribes to <code>meeting.ended</code>. RealtimeKit sends this event when the session ends.
You can use it to trigger backend workflows, such as sending a notification, generating a report, or updating session records in your database.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/realtime/kit/{app_id}/webhooks \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Session ended webhook&quot;,&#10;  &quot;url&quot;: &quot;&lt;YOUR_WEBHOOK_URL&gt;&quot;,&#10;  &quot;events&quot;: [&#10;    &quot;meeting.ended&quot;&#10;  ]&#10;}&#x27;</code></pre>
<h2 id="disable-a-meeting">Disable a meeting</h2>
<p>Ending a session does not disable the meeting. Participants can join the meeting again and start a new session.
To prevent participants from joining again and starting a new session, set the meeting status to <code>INACTIVE</code> using the <a href="/api/resources/realtime_kit/subresources/meetings/methods/update_meeting_by_id/">Update a meeting</a> API.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;status&quot;: &quot;INACTIVE&quot;&#10;}&#x27;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Review how presets control permissions in <a href="/realtime/realtimekit/concepts/preset/">Preset</a>.</li>
<li>Review the possible values of the local participant room state in <a href="/realtime/realtimekit/core/local-participant/#state-properties/">Local Participant</a>.</li>
</ul>
