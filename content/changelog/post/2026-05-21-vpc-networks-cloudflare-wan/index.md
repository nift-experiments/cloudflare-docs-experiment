---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/
  description: New updates and improvements at Cloudflare.
  full_title: Reach Cloudflare WAN destinations from Workers VPC · Changelog
  head_html: <title>Reach Cloudflare WAN destinations from Workers VPC · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Reach Cloudflare WAN destinations from Workers VPC · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/#page","headline":"Reach Cloudflare WAN destinations from Workers VPC \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-21-vpc-networks-cloudflare-wan/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 21, 2026</time><h2 id="post-title">Reach Cloudflare WAN destinations from Workers VPC</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p>You can now use <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings with <code>network_id: &quot;cf1:network&quot;</code> to reach your full private network from Workers, including:</p>
<ul>
<li><a href="/mesh/">Cloudflare Mesh</a> nodes and client devices</li>
<li>Subnet routes and hostname routes announced through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or Cloudflare Mesh</li>
<li>Destinations connected through <a href="/cloudflare-wan/">Cloudflare WAN</a> on-ramps — GRE, IPsec, and CNI</li>
</ul>
<p>This means a single VPC Network binding can route Worker requests to private services regardless of how those services are connected to Cloudflare: through a Cloudflare Tunnel from a cloud VPC, a Mesh node on a private subnet, or a Cloudflare WAN on-ramp from your data center or branch site.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17824.md")</div>
<p>At runtime, the URL you pass to <code>fetch()</code> determines the destination:</p>
<pre tabindex="0"><code class="language-js">// Reach a service behind a Cloudflare WAN IPsec on-ramp&#10;const response = await env.PRIVATE_NETWORK.fetch(&quot;http://10.50.0.100:8080/api&quot;);&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17823.md")</aside>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>.</p>
</div></article></div>
