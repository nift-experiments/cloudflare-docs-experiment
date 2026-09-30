---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/
  description: New updates and improvements at Cloudflare.
  full_title: Automatic Return Routing (Beta) · Changelog
  head_html: <title>Automatic Return Routing (Beta) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Automatic Return Routing (Beta) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/#page","headline":"Automatic Return Routing (Beta) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-06-automatic-return-routing-beta/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 6, 2025</time><h2 id="post-title">Automatic Return Routing (Beta)</h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Magic WAN now supports Automatic Return Routing (ARR), allowing customers to configure Magic on-ramps (IPsec/GRE/CNI) to learn the return path for traffic flows without requiring static routes.</p>
<p>Key benefits:</p>
<ul>
<li><strong>Route-less mode</strong>: Static or dynamic routes are optional when using ARR.</li>
<li><strong>Overlapping IP space support</strong>: Traffic originating from customer sites can use overlapping private IP ranges.</li>
<li><strong>Symmetric routing</strong>: Return traffic is guaranteed to use the same connection as the original on-ramp.</li>
</ul>
<p>This feature is currently in beta and requires the new Unified Routing mode (beta).</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-automatic-return-routing-beta">Configure Automatic Return Routing</a>.</p>
</div></article></div>
