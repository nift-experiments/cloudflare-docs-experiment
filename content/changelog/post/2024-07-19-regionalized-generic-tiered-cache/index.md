---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/
  description: New updates and improvements at Cloudflare.
  full_title: Regionalized Generic Tiered Cache for higher hit ratios · Changelog
  head_html: <title>Regionalized Generic Tiered Cache for higher hit ratios · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Regionalized Generic Tiered Cache for higher hit ratios · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/#page","headline":"Regionalized Generic Tiered Cache for higher hit ratios \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2024-07-19-regionalized-generic-tiered-cache/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2024-07-19-regionalized-generic-tiered-cache/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 19, 2024</time><h2 id="post-title">Regionalized Generic Tiered Cache for higher hit ratios</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now achieve higher cache hit ratios with <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a>. Regional content hashing routes content consistently to the same upper-tier data centers, eliminating redundant caching and reducing origin load.</p>
<h4 id="how-it-works">How it works</h4>
<p>Regional content hashing groups data centers by region and uses consistent hashing to route content to designated upper-tier caches:</p>
<ul>
<li>Same content always routes to the same upper-tier data center within a region.</li>
<li>Eliminates redundant copies across multiple upper-tier caches.</li>
<li>Increases the likelihood of cache HITs for the same content.</li>
</ul>
<h4 id="example">Example</h4>
<p>A popular image requested from multiple edge locations in a region:</p>
<ul>
<li><strong>Before</strong>: Cached at 3-4 different upper-tier data centers</li>
<li><strong>After</strong>: Cached at 1 designated upper-tier data center</li>
<li><strong>Result</strong>: 3-4x fewer cache MISSes, reducing origin load and improving performance</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/#generic-global-tiered-cache">Generic Global Tiered Cache</a> on your zone.</p>
</div></article></div>
