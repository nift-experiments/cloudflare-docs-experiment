---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/
  description: New updates and improvements at Cloudflare.
  full_title: Hostname routing for Cloudflare Mesh · Changelog
  head_html: <title>Hostname routing for Cloudflare Mesh · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Hostname routing for Cloudflare Mesh · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/#page","headline":"Hostname routing for Cloudflare Mesh \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-07-02-mesh-hostname-routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-07-02-mesh-hostname-routing/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 2, 2026</time><h2 id="post-title">Hostname routing for Cloudflare Mesh</h2>
<div class="changelog-badges"><span>mesh</span><span>cloudflare-one</span></div><div class="changelog-body"><p>You can now add <a href="/mesh/features/routes/#hostname-routes">hostname routes</a> to a Cloudflare Mesh node, in addition to CIDR routes.</p>
<div class="nb-interactive-component" data-cf-component="MeshHostnameRoutingDiagram"></div>
<p>Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:</p>
<ul>
<li><strong>Private hostname</strong> (for example, <code>wiki.internal.local</code>) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.</li>
<li><strong>Public hostname</strong> (for example, <code>www.example.com</code>) — route that hostname's traffic through the node and egress via the node's public IP.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For setup steps, prerequisites, and DNS options, refer to <a href="/mesh/features/routes/#hostname-routes">Hostname routes</a>.</p>
</div></article></div>
