---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/
  description: New updates and improvements at Cloudflare.
  full_title: Announcing Workers VPC Services (Beta) · Changelog
  head_html: <title>Announcing Workers VPC Services (Beta) · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Announcing Workers VPC Services (Beta) · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/#page","headline":"Announcing Workers VPC Services (Beta) \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-25-workers-vpc/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 5, 2025</time><h2 id="post-title">Announcing Workers VPC Services (Beta)</h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p><strong>Workers VPC Services</strong> is now available, enabling your Workers to securely access resources in your private networks, without having to expose them on the public Internet.</p>
<h4 id="what-s-new">What's new</h4>
<ul>
<li><strong>VPC Services</strong>: Create secure connections to internal APIs, databases, and services using familiar Worker binding syntax</li>
<li><strong>Multi-cloud Support</strong>: Connect to resources in private networks in any external cloud (AWS, Azure, GCP, etc.) or on-premise using Cloudflare Tunnels</li>
</ul>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// Perform application logic in Workers here&#10;&#10;		// Sample call to an internal API running on ECS in AWS using the binding&#10;		const response = await env.AWS_VPC_ECS_API.fetch(&quot;https://internal-host.example.com&quot;);&#10;&#10;		// Additional application logic in Workers&#10;		return new Response();&#10;	},&#10;};&#10;</code></pre>
<h4 id="getting-started">Getting started</h4>
<p>Set up a Cloudflare Tunnel, create a VPC Service, add service bindings to your Worker, and access private resources securely. <a href="/workers-vpc/">Refer to the documentation</a> to get started.</p>
</div></article></div>
