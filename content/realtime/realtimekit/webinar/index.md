---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/webinar/
  description: Set up a RealtimeKit webinar with presenters and viewers, then manage requests to join the stage.
  full_title: Set up a webinar · Cloudflare Realtime docs
  head_html: <title>Set up a webinar · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up a RealtimeKit webinar with presenters and viewers, then manage requests to join the stage."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/webinar/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/webinar/index.md"><meta property="og:title" content="Set up a webinar · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up a RealtimeKit webinar with presenters and viewers, then manage requests to join the stage."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/webinar/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/webinar/#page","headline":"Set up a webinar \u00b7 Cloudflare Realtime docs","description":"Set up a RealtimeKit webinar with presenters and viewers, then manage requests to join the stage.","url":"https://developers.cloudflare.com/realtime/realtimekit/webinar/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/webinar/
  schema: 1
---
<p>In a RealtimeKit webinar, presenters publish audio and video from the <a href="/realtime/realtimekit/concepts/meeting/#stage">stage</a>. Viewers watch and can request to join the stage.</p>
<p>This guide sets up a webinar using the default webinar <a href="/realtime/realtimekit/concepts/preset/">presets</a> and renders it with <a href="/realtime/realtimekit/ui-kit/">RealtimeKit UI Kit</a>. To build a custom interface instead, use <a href="/realtime/realtimekit/core/">RealtimeKit Core SDK</a> with <a href="/realtime/realtimekit/core/stage-management/">stage management</a>.</p>
<h2 id="webinar-roles">Webinar roles</h2>
<p>Every RealtimeKit app includes two default presets for webinars. Assign one of these presets to each participant, modify them, or create your own preset to fit your application.</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Default preset</th>
<th>Stage behavior</th>
<th>Can accept stage requests</th>
</tr>
</thead>
<tbody>
<tr>
<td>Presenter</td>
<td><code>webinar_presenter</code></td>
<td>Can join the stage and publish audio and video</td>
<td>Yes</td>
</tr>
<tr>
<td>Viewer</td>
<td><code>webinar_viewer</code></td>
<td>Can request to join the stage</td>
<td>No</td>
</tr>
</tbody>
</table>
<h2 id="before-you-begin">Before you begin</h2>
<p>Before you set up a webinar, make sure that you have:</p>
<ul>
<li>A <a href="https://dash.cloudflare.com">Cloudflare account</a> with a RealtimeKit app.</li>
<li>An API token with Realtime Admin permissions. Keep it server-side. Do not expose it in frontend code.</li>
<li>A backend that can call the RealtimeKit REST API to create meetings and add participants.</li>
<li>A frontend application ready to integrate <a href="/realtime/realtimekit/ui-kit/">RealtimeKit UI Kit</a>.</li>
</ul>
<p>If you have not completed these requirements, refer to <a href="/realtime/realtimekit/quickstart/">Quickstart</a>.</p>
<h2 id="set-up-a-webinar">Set up a webinar</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11589.md")
</div>
<details class="nb-details"><summary>Configure presets with the API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11590.md")
</div></details>
<h2 id="manage-stage-requests">Manage stage requests</h2>
<p>A viewer whose preset has <strong>Behaviour</strong> set to <strong>Can request to join</strong> can request access to the stage from the UI Kit interface. A presenter whose preset has <strong>Accept Requests</strong> turned on receives the request and can accept or reject it.</p>
<p>Once accepted, the viewer joins the stage and can publish audio and video like a presenter. RealtimeKit UI Kit handles this by default. To build a custom interface, implement the same behavior with the stage management APIs in <a href="/realtime/realtimekit/core/stage-management/">Stage Management</a>.</p>
<h2 id="verify-the-webinar">Verify the webinar</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11591.md")
</div>
<h2 id="pricing">Pricing</h2>
<p>Both presenters and viewers are billed as Audio/Video Participants. For detailed pricing information, refer to <a href="/realtime/realtimekit/pricing/">Pricing</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Customize the webinar interface with a <a href="/realtime/realtimekit/ui-kit/custom-controlbar/">custom control bar</a> or <a href="/realtime/realtimekit/ui-kit/addons/">UI Kit addons</a>.</li>
<li>Review <a href="/realtime/realtimekit/best-practices/video-and-simulcast/#webinar-audience-is-view-only">video and simulcast recommendations</a> for presenter and viewer media quality.</li>
<li><a href="/realtime/realtimekit/recording-guide/">Record the webinar</a> and store the recording in your own storage.</li>
<li>Use <a href="/realtime/realtimekit/webhooks/">webhooks</a> to track webinar lifecycle events in your backend.</li>
</ul>
