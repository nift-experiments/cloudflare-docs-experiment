---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/
  description: New updates and improvements at Cloudflare.
  full_title: Increased HTTP header size limit to 128 KB · Changelog
  head_html: <title>Increased HTTP header size limit to 128 KB · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Increased HTTP header size limit to 128 KB · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/#page","headline":"Increased HTTP header size limit to 128 KB \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-16-header-limit-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-16-header-limit-increase/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 16, 2025</time><h2 id="post-title">Increased HTTP header size limit to 128 KB</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><h4 id="cdn-now-supports-128-kb-request-and-response-headers">CDN now supports 128 KB request and response headers 🚀</h4>
<p>We're excited to announce a significant increase in the maximum header size supported by Cloudflare's Content Delivery Network (CDN). Cloudflare now supports up to <strong>128 KB</strong> for both <strong>request and response headers</strong>.</p>
<p>Previously, customers were limited to a total of 32 KB for request or response headers, with a maximum of 16 KB per individual header. Larger headers could cause requests to fail with <code>HTTP 413</code> (Request Header Fields Too Large) errors.</p>
<hr />
<h4 id="what-s-new">What's new?</h4>
<ul>
<li><strong>Support for large headers:</strong> You can now utilize much larger headers, whether as a single large header up to 128 KB or split over multiple headers.</li>
<li><strong>Reduces <code>413</code> and <code>520</code> HTTP errors:</strong> This change drastically reduces the likelihood of customers encountering <code>HTTP 413</code> errors from large request headers or <code>HTTP 520</code> errors caused by oversized response headers, improving the overall reliability of your web applications.</li>
<li><strong>Enhanced functionality:</strong> This is especially beneficial for applications that rely on:
<ul>
<li>A large number of cookies.</li>
<li>Large Content-Security-Policy (CSP) response headers.</li>
<li>Advanced use cases with Cloudflare Workers that generate large response headers.</li>
</ul>
</li>
</ul>
<p>This enhancement improves compatibility with Cloudflare's CDN, enabling more use cases that previously failed due to header size limits.</p>
<hr />
<p>To learn more and get started, refer to the <a href="/fundamentals/reference/connection-limits/#request-limits">Cloudflare Fundamentals documentation</a>.</p>
</div></article></div>
