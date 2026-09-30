---
cp9:
  canonical: https://developers.cloudflare.com/cache/concepts/cache-behavior/
  description: How Cloudflare handles HEAD requests and Set-Cookie headers.
  full_title: Head Requests and Set-Cookie Headers · Cloudflare Cache (CDN) docs
  head_html: <title>Head Requests and Set-Cookie Headers · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="How Cloudflare handles HEAD requests and Set-Cookie headers."><link rel="canonical" href="https://developers.cloudflare.com/cache/concepts/cache-behavior/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/concepts/cache-behavior/index.md"><meta property="og:title" content="Head Requests and Set-Cookie Headers · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Cloudflare handles HEAD requests and Set-Cookie headers."><meta property="og:url" content="https://developers.cloudflare.com/cache/concepts/cache-behavior/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><meta name="pcx_tags" content="Headers,Cookies"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/concepts/cache-behavior/#page","headline":"Head Requests and Set-Cookie Headers \u00b7 Cloudflare Cache (CDN) docs","description":"How Cloudflare handles HEAD requests and Set-Cookie headers.","url":"https://developers.cloudflare.com/cache/concepts/cache-behavior/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Headers","Cookies"]}</script>
  markdown: true
  noindex: false
  route: /cache/concepts/cache-behavior/
  schema: 1
---
<p>This page describes how Cloudflare's cache system behaves in interaction with:</p>
<ul>
<li><code>HEAD</code> requests</li>
<li><code>Set-Cookie</code> response headers</li>
</ul>
<h2 id="interaction-of-head-requests-with-cache">Interaction of <code>HEAD</code> requests with Cache</h2>
<p>Cloudflare converts <code>HEAD</code> requests to <code>GET</code> requests for <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">cacheable requests</a>.</p>
<p>When you make a <code>HEAD</code> request for a cacheable resource and Cloudflare does not have that resource in the edge cache, a cache miss happens. Cloudflare will send a <code>GET</code> request to your origin, cache the full response and return the response headers only. Make sure the origin server is set up to handle <code>GET</code> requests, even if only <code>HEAD</code> requests are expected, so that compatibility with this behavior is ensured.</p>
<h2 id="interaction-of-set-cookie-response-header-with-cache">Interaction of <code>Set-Cookie</code> response header with Cache</h2>
<p>For non-cacheable requests, <code>Set-Cookie</code> is always preserved. For cacheable requests, there are three possible behaviors:</p>
<ul>
<li>
<p><code>Set-Cookie</code> is returned from origin and the default cache level is used. If <a href="/cache/concepts/cache-control/">origin cache control</a> is not enabled, Cloudflare removes the <code>Set-Cookie</code> and caches the asset. If origin cache control is enabled, Cloudflare does not cache the asset and preserves the <code>Set-Cookie</code>. A cache status of <code>BYPASS</code> is returned.</p>
</li>
<li>
<p><code>Set-Cookie</code> is returned from origin and the cache level is set to <code>Cache Everything</code> in Page Rules, or <code>Eligible for cache</code> in Cache Rules. In this case, Cloudflare preserves the <code>Set-Cookie</code> but does not cache the asset. A cache <code>MISS</code> will be returned every time.</p>
</li>
<li>
<p><code>Set-Cookie</code> is returned from origin, the cache level is set to <code>Cache Everything</code> in Page Rules, or <code>Eligible for cache</code> in Cache Rules, and edge cache TTL is explicitly set using either the &quot;Ignore cache-control header and use this TTL&quot; or &quot;Status code TTL&quot; setting. In this case, Cloudflare removes the <code>Set-Cookie</code> and the asset is cached.</p>
</li>
</ul>
