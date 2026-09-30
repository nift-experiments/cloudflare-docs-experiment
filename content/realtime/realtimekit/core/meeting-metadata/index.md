---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/meeting-metadata/
  description: Access meeting state, type, and connection metadata in the RealtimeKit Core SDK.
  full_title: Meeting Metadata · Cloudflare Realtime docs
  head_html: <title>Meeting Metadata · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Access meeting state, type, and connection metadata in the RealtimeKit Core SDK."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/meeting-metadata/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/meeting-metadata/index.md"><meta property="og:title" content="Meeting Metadata · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access meeting state, type, and connection metadata in the RealtimeKit Core SDK."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/meeting-metadata/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/meeting-metadata/#page","headline":"Meeting Metadata \u00b7 Cloudflare Realtime docs","description":"Access meeting state, type, and connection metadata in the RealtimeKit Core SDK.","url":"https://developers.cloudflare.com/realtime/realtimekit/core/meeting-metadata/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/meeting-metadata/
  schema: 1
---
<p>All metadata pertaining to a meeting is stored in <code>meeting.meta</code>. This includes important information about the meeting state, type, and connections.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h2 id="available-metadata">Available metadata</h2>
<p>Select a framework based on the platform you are building for.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12078.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12079.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12080.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12081.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12082.md")
</div>
<h2 id="access-meeting-metadata">Access meeting metadata</h2>
<p>To access meeting metadata, use the <code>meeting.meta</code> object.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12083.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12084.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12085.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12086.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12087.md")
</div>
<h2 id="connection-events">Connection events</h2>
<p>The <code>meta</code> object also emits events for indicating changes in the connection state of the meeting.</p>
<h3 id="media-connection-updates">Media connection updates</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12088.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12089.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12090.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12091.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12092.md")
</div>
<h3 id="socket-connection-updates">Socket connection updates</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12093.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12094.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12095.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12096.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12097.md")
</div>
<h2 id="next-steps">Next steps</h2>
<p>Explore related topics:</p>
<ul>
<li><a href="/realtime/realtimekit/core/meeting-object-explained/">Meeting Object Explained</a> - Comprehensive meeting object reference</li>
<li><a href="/realtime/realtimekit/concepts/session-lifecycle/">Session Lifecycle</a> - Understanding meeting states and transitions</li>
</ul>
