---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/
  description: Detect and display active speakers in RealtimeKit meetings using the Core SDK.
  full_title: Display active speakers · Cloudflare Realtime docs
  head_html: <title>Display active speakers · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Detect and display active speakers in RealtimeKit meetings using the Core SDK."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/index.md"><meta property="og:title" content="Display active speakers · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Detect and display active speakers in RealtimeKit meetings using the Core SDK."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/#page","headline":"Display active speakers \u00b7 Cloudflare Realtime docs","description":"Detect and display active speakers in RealtimeKit meetings using the Core SDK.","url":"https://developers.cloudflare.com/realtime/realtimekit/core/display-active-speakers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/display-active-speakers/
  schema: 1
---
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<p>RealtimeKit automatically detects and tracks participants who are actively speaking in a meeting. You can display either a single active speaker or multiple active speakers in your application UI, depending on your design requirements.</p>
<p>An active speaker in RealtimeKit is a remote participant with prominent audio activity at any given moment. The SDK maintains two types of data to help you build your UI:</p>
<ul>
<li><strong>Active speaker</strong> — A single remote participant who is currently speaking most prominently.</li>
<li><strong>Active participants</strong> — A set of remote participants with the most prominent audio activity.</li>
</ul>
<p>The SDK automatically updates these properties and subscribes to participant media as speaking activity changes. It prioritizes prominent audio activity, so a participant not currently visible in your UI can replace a visible participant if their audio becomes more active.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12348.md")
</aside>
<p>The maximum number of participants in the <code>active</code> map is one less than the grid size configured in the local participant's <a href="/realtime/realtimekit/concepts/preset/">Preset</a>.
This reserves space for the local participant in your UI. For example, if the grid size is 6, the <code>active</code> map contains a maximum of 5 remote participants.</p>
<h2 id="display-a-single-active-speaker">Display a single active speaker</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12349.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12350.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12351.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12352.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12353.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12354.md")
</div>
<h2 id="display-multiple-active-speakers">Display multiple active speakers</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12355.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12356.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12357.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12358.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12359.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12360.md")
</div>
<h2 id="visualize-audio-activity">Visualize audio activity</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12361.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12362.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12363.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12364.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12365.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12366.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/realtime/realtimekit/core/meeting-object-explained/">Meeting object explained</a> - Understand the meeting object structure and available properties.</li>
<li><a href="/realtime/realtimekit/core/remote-participants/">Remote participant</a> - Learn more about remote participants in a session and how to display their video.</li>
</ul>
