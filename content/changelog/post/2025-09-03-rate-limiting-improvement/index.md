---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/
  description: New updates and improvements at Cloudflare.
  full_title: Introducing new headers for rate limiting on Cloudflare's API · Changelog
  head_html: <title>Introducing new headers for rate limiting on Cloudflare&#x27;s API · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Introducing new headers for rate limiting on Cloudflare&#x27;s API · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/#page","headline":"Introducing new headers for rate limiting on Cloudflare's API \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-03-rate-limiting-improvement/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-03-rate-limiting-improvement/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 3, 2025</time><h2 id="post-title">Introducing new headers for rate limiting on Cloudflare's API</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare's API now supports rate limiting headers using the pattern developed by the <a href="https://ietf-wg-httpapi.github.io/ratelimit-headers/draft-ietf-httpapi-ratelimit-headers.html">IETF draft on rate limiting</a>. This allows API consumers to know how many more calls are left until the rate limit is reached, as well as how long you will need to wait until more capacity is available.</p>
<p>Our SDKs automatically work with these new headers, backing off when rate limits are approached. There is no action required for users of the latest Cloudflare SDKs to take advantage of this.</p>
<p>As always, if you need any help with rate limits, please contact Support.</p>
<h4 id="changes">Changes</h4>
<h4 id="new-headers">New Headers</h4>
<p><strong>Headers that are always returned:</strong></p>
<ul>
<li><code>Ratelimit</code>: List of service limit items, composed of the limit name, the remaining quota (<code>r</code>) and the time next window resets (<code>t</code>). For example: <code>&quot;default&quot;;r=50;t=30</code></li>
<li><code>Ratelimit-Policy</code>: List of quota policy items, composed of the policy name, the total quota (<code>q</code>) and the time window the quota applies to (<code>w</code>). For example: <code>&quot;burst&quot;;q=100;w=60</code></li>
</ul>
<p><strong>Returned only when a rate limit has been reached (error code: 429):</strong></p>
<ul>
<li>Retry-After: Number of Seconds until more capacity is available, rounded up</li>
</ul>
<h4 id="sdk-back-offs">SDK Back offs</h4>
- All of Cloudflare's latest SDKs will automatically respond to the headers, instituting a backoff when limits are approached. 
<h4 id="graphql-and-edge-apis">GraphQL and Edge APIs</h4>
These new headers and back offs are only available for Cloudflare REST APIs, and will not affect GraphQL. 
<h4 id="for-more-information">For more information</h4>
* [Rate limits at Cloudflare](https://developers.cloudflare.com/fundamentals/api/reference/limits/)
</div></article></div>
