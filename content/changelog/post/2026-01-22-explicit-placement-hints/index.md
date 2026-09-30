---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/
  description: New updates and improvements at Cloudflare.
  full_title: New Placement Hints for Workers · Changelog
  head_html: <title>New Placement Hints for Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New Placement Hints for Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/#page","headline":"New Placement Hints for Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-22-explicit-placement-hints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-22-explicit-placement-hints/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 22, 2026</time><h2 id="post-title">New Placement Hints for Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now configure Workers to run close to infrastructure in legacy cloud regions to minimize latency to existing services and databases. This is most useful when your Worker makes multiple round trips.</p>
<p>To <a href="/workers/configuration/placement/#configure-explicit-placement-hints">set a placement hint</a>, set the <code>placement.region</code> property in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17793.md")</div>
<p>Placement hints support Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure region identifiers. Workers run in the <a href="https://www.cloudflare.com/network/">Cloudflare data center</a> with the lowest latency to the specified cloud region.</p>
<p>If your existing infrastructure is not in these cloud providers, expose it to placement probes with <code>placement.host</code> for layer 4 checks or <code>placement.hostname</code> for layer 7 checks. These probes are designed to locate single-homed infrastructure and are not suitable for anycasted or multicasted resources.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17794.md")</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17795.md")</div>
<p>This is an extension of <a href="/workers/configuration/placement/#enable-smart-placement">Smart Placement</a>, which automatically places your Workers closer to back-end APIs based on measured latency. When you do not know the location of your back-end APIs or have multiple back-end APIs, set <code>mode: &quot;smart&quot;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17796.md")</div>
</div></article></div>
