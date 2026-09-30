---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/
  description: New updates and improvements at Cloudflare.
  full_title: Filter Workers' public Internet traffic using Gateway policies · Changelog
  head_html: <title>Filter Workers&#x27; public Internet traffic using Gateway policies · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Filter Workers&#x27; public Internet traffic using Gateway policies · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/#page","headline":"Filter Workers' public Internet traffic using Gateway policies \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-05-gateway-egress/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-05-gateway-egress/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 5, 2026</time><h2 id="post-title">Filter Workers' public Internet traffic using Gateway policies</h2>
<div class="changelog-badges"><span>gateway</span><span>mesh</span><span>workers-vpc</span></div><div class="changelog-body"><p>Workers using a <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> binding with <code>network_id: &quot;cf1:network&quot;</code> now egress to public Internet destinations through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>. This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.</p>
<div class="nb-interactive-component" data-cf-component="WorkersVPCEgressDiagram"></div>
<p>What you get by default:</p>
<ul>
<li><strong>Visibility.</strong> Worker egress shows up in Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> logs alongside your other traffic, so you can audit what your Workers are calling and when.</li>
<li><strong>Enforcement.</strong> Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17825.md")</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17826.md")</div>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>. For policy authoring, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway traffic policies</a>.</p>
</div></article></div>
