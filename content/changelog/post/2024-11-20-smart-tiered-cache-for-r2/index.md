---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/
  description: New updates and improvements at Cloudflare.
  full_title: Smart Tiered Cache automatically optimizes R2 caching · Changelog
  head_html: <title>Smart Tiered Cache automatically optimizes R2 caching · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Smart Tiered Cache automatically optimizes R2 caching · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/#page","headline":"Smart Tiered Cache automatically optimizes R2 caching \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2024-11-20-smart-tiered-cache-for-r2/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 20, 2024</time><h2 id="post-title">Smart Tiered Cache automatically optimizes R2 caching</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now reduce latency and lower R2 egress costs automatically when using <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> with <a href="/r2/">R2</a>. Cloudflare intelligently selects a tiered data center close to your R2 bucket location, creating an efficient caching topology without additional configuration.</p>
<h4 id="how-it-works">How it works</h4>
<p>When you enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> for zones using <a href="/r2/">R2</a> as an origin, Cloudflare automatically:</p>
<ol>
<li><strong>Identifies your R2 bucket location</strong>: Determines the geographical region where your R2 bucket is stored.</li>
<li><strong>Selects an optimal Upper Tier</strong>: Chooses a data center close to your bucket as the common Upper Tier cache.</li>
<li><strong>Routes requests efficiently</strong>: All cache misses in edge locations route through this Upper Tier before reaching R2.</li>
</ol>
<h4 id="benefits">Benefits</h4>
<ul>
<li><strong>Automatic optimization</strong>: No manual configuration required.</li>
<li><strong>Lower egress costs</strong>: Fewer requests to R2 reduce egress charges.</li>
<li><strong>Improved hit ratio</strong>: Common Upper Tier increases cache efficiency.</li>
<li><strong>Reduced latency</strong>: Upper Tier proximity to R2 minimizes fetch times.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone using R2 as an origin.</p>
</div></article></div>
