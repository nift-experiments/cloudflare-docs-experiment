---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/
  description: New updates and improvements at Cloudflare.
  full_title: Smart Tiered Cache optimizes Load Balancing Pools · Changelog
  head_html: <title>Smart Tiered Cache optimizes Load Balancing Pools · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Smart Tiered Cache optimizes Load Balancing Pools · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/#page","headline":"Smart Tiered Cache optimizes Load Balancing Pools \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-01-08-smart-tiered-cache-for-load-balancing/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 8, 2025</time><h2 id="post-title">Smart Tiered Cache optimizes Load Balancing Pools</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now achieve higher cache hit rates and reduce origin load when using <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>. Cloudflare automatically selects a single, optimal tiered data center for all origins in your Load Balancing Pool.</p>
<h4 id="how-it-works">How it works</h4>
<p>When you use <a href="/load-balancing/">Load Balancing</a> with <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a>, Cloudflare analyzes performance metrics across your pool's origins and automatically selects the optimal Upper Tier data center for the entire pool. This means:</p>
<ul>
<li><strong>Consistent cache location</strong>: All origins in the pool share the same Upper Tier cache.</li>
<li><strong>Higher HIT rates</strong>: Requests for the same content hit the cache more frequently.</li>
<li><strong>Reduced origin requests</strong>: Fewer requests reach your origin servers.</li>
<li><strong>Improved performance</strong>: Faster response times for cache HITs.</li>
</ul>
<h4 id="example-workflow">Example workflow</h4>
<pre tabindex="0"><code class="language-txt">Load Balancing Pool: api-pool&#10;├── Origin 1: api-1.example.com&#10;├── Origin 2: api-2.example.com&#10;└── Origin 3: api-3.example.com&#10;    ↓&#10;Selected Upper Tier: [Optimal data center based on pool performance]&#10;</code></pre>
<h4 id="get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> on your zone and configure your <a href="/load-balancing/">Load Balancing Pool</a>.</p>
</div></article></div>
