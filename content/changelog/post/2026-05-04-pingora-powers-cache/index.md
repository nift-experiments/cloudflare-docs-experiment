---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/
  description: New updates and improvements at Cloudflare.
  full_title: Pingora now powers Cloudflare's cache · Changelog
  head_html: <title>Pingora now powers Cloudflare&#x27;s cache · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Pingora now powers Cloudflare&#x27;s cache · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/#page","headline":"Pingora now powers Cloudflare's cache \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-04-pingora-powers-cache/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-04-pingora-powers-cache/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 4, 2026</time><h2 id="post-title">Pingora now powers Cloudflare's cache</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Cloudflare's cache now runs on a new proxy built on <a href="https://github.com/cloudflare/pingora">Pingora</a>, the Rust-based framework that already serves a significant portion of Cloudflare's network traffic. The new proxy is faster, more memory-safe, and designed to evolve our cache architecture. It delivers immediate performance improvements and enables new caching capabilities.</p>
<h4 id="what-this-brings">What this brings</h4>
<ul>
<li><strong>Lower latency</strong>: The new proxy reduces per-request overhead through improved connection reuse.</li>
<li><strong>Reduced cache MISSes</strong>: Enhanced cache retention improves origin offload.</li>
<li><strong>Better RFC compliance</strong>: Caching behavior more closely follows HTTP caching standards.</li>
<li><strong>Foundation for future features</strong>: The new architecture enables upcoming improvements to cache functionality and efficiency.</li>
</ul>
<h4 id="new-features">New features</h4>
<ul>
<li><strong>Asynchronous <code>stale-while-revalidate</code></strong>: Every request returns stale content immediately while revalidation happens in the background, instead of the first request after expiry blocking on the origin. Refer to the <a href="/changelog/post/2026-02-26-async-stale-while-revalidate/">asynchronous <code>stale-while-revalidate</code> changelog</a> for details.</li>
<li><strong>Unbuffered bypass by default</strong>: Responses that bypass cache are streamed directly to the client without buffering, reducing time-to-first-byte for uncacheable content.</li>
</ul>
<h4 id="behavioral-changes">Behavioral changes</h4>
<p>The new architecture introduces the following behavioral changes to improve RFC compliance and correctness:</p>
<ul>
<li><strong><code>Vary: *</code> results in cache bypass</strong>: According to <a href="https://httpwg.org/specs/rfc9110.html#field.vary">RFC 9110 Section 12.5.5</a>, a <code>Vary</code> header value of <code>*</code> indicates the response varies on factors beyond request headers and must not be served from cache. Cloudflare now bypasses cache for these responses instead of storing them.</li>
<li><strong><code>Set-Cookie</code> stripped on MISS and EXPIRED</strong>: For cacheable assets, <code>Set-Cookie</code> is now stripped on MISS and EXPIRED responses, not only on HITs.</li>
<li><strong>Floating-point TTL values</strong>: Floating-point time-to-live values (for example, <code>max-age=1.5</code>) are rounded down to the nearest integer instead of being rejected as invalid.</li>
</ul>
<h4 id="what-s-next">What's next</h4>
<p>A deeper look at the new cache proxy is coming soon to the <a href="https://blog.cloudflare.com/">Cloudflare blog</a>. For background on the underlying framework, read:</p>
<ul>
<li><a href="https://blog.cloudflare.com/pingora-open-source/">Open sourcing Pingora: our Rust framework for building programmable network services</a></li>
<li><a href="https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/">How we built Pingora, the proxy that connects Cloudflare to the Internet</a></li>
</ul>
</div></article></div>
