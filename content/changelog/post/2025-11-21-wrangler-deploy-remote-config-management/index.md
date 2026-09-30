---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/
  description: New updates and improvements at Cloudflare.
  full_title: Better local deployment flow for Cloudflare Workers · Changelog
  head_html: <title>Better local deployment flow for Cloudflare Workers · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Better local deployment flow for Cloudflare Workers · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/#page","headline":"Better local deployment flow for Cloudflare Workers \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-21-wrangler-deploy-remote-config-management/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 21, 2025</time><h2 id="post-title">Better local deployment flow for Cloudflare Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Until now, if a Worker had been previously deployed via the <a href="https://dash.cloudflare.com">Cloudflare Dashboard</a>, a subsequent deployment done via the Cloudflare Workers CLI, <a href="/workers/wrangler/"><strong>Wrangler</strong></a>
(through the <a href="/workers/wrangler/commands/general/#deploy"><code>deploy</code> command</a>), would allow the user to override the Worker's dashboard settings without providing details on
what dashboard settings would be lost.</p>
<p>Now instead, <code>wrangler deploy</code> presents a helpful representation of the differences between the <a href="/workers/wrangler/configuration/">local configuration</a>
and the remote dashboard settings, and offers to update your local configuration file for you.</p>
<p>See example below showing a before and after for <code>wrangler deploy</code> when a local configuration is expected to override a Worker's dashboard settings:</p>
<div class="nb-example"><h3 class="nb-component-title" id="before">Before</h3>
@markup("md", "content/.markup/bodies/17791.md")</div>
<div class="nb-example"><h3 class="nb-component-title" id="after">After</h3>
@markup("md", "content/.markup/bodies/17792.md")</div>
<p>Also, if instead Wrangler detects that a deployment would override remote dashboard settings but in an additive way, without modifying or removing any of them, it will simply proceed with the deployment without requesting any user interaction.</p>
<p>Update to <a href="/workers/wrangler/">Wrangler</a> v4.50.0 or greater to take advantage of this improved deploy flow.</p>
</div></article></div>
