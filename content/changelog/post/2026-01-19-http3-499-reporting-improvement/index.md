---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/
  description: New updates and improvements at Cloudflare.
  full_title: Enhanced HTTP/3 request cancellation visibility · Changelog
  head_html: <title>Enhanced HTTP/3 request cancellation visibility · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Enhanced HTTP/3 request cancellation visibility · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/#page","headline":"Enhanced HTTP/3 request cancellation visibility \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-19-http3-499-reporting-improvement/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-19-http3-499-reporting-improvement/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 19, 2026</time><h2 id="post-title">Enhanced HTTP/3 request cancellation visibility</h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><h4 id="enhanced-http-3-request-cancellation-visibility">Enhanced HTTP/3 request cancellation visibility</h4>
<p>Cloudflare now provides more accurate visibility into HTTP/3 client request cancellations, giving you better insight into real client behavior and reducing unnecessary load on your origins.</p>
<p>Previously, when an HTTP/3 client cancelled a request, the cancellation was not always actioned immediately. This meant requests could continue through the CDN — potentially all the way to your origin — even after the client had abandoned them. In these cases, logs would show the upstream response status (such as <code>200</code> or a timeout-related code) rather than reflecting the client cancellation.</p>
<p>Now, Cloudflare terminates cancelled HTTP/3 requests immediately and accurately logs them with a <code>499</code> status code.</p>
<hr />
<h4 id="better-observability-for-client-behavior">Better observability for client behavior</h4>
<p>When HTTP/3 clients cancel requests, Cloudflare now immediately reflects this in your logs with a <code>499</code> status code. This gives you:</p>
<ul>
<li><strong>More accurate traffic analysis</strong>: Understand exactly when and how often clients cancel requests.</li>
<li><strong>Clearer debugging</strong>: Distinguish between true errors and intentional client cancellations.</li>
<li><strong>Better availability metrics</strong>: Separate client-initiated cancellations from server-side issues.</li>
</ul>
<hr />
<h4 id="reduced-origin-load">Reduced origin load</h4>
<p>Cloudflare now terminates cancelled requests faster, which means:</p>
<ul>
<li><strong>Less wasted compute</strong>: Your origin no longer processes requests that clients have already abandoned.</li>
<li><strong>Lower bandwidth usage</strong>: Responses are no longer generated and transmitted for cancelled requests.</li>
<li><strong>Improved efficiency</strong>: Resources are freed up to handle active requests.</li>
</ul>
<hr />
<h4 id="what-to-expect-in-your-logs">What to expect in your logs</h4>
<p>You may notice an increase in <code>499</code> status codes for HTTP/3 traffic. For HTTP/3, a <code>499</code> indicates the client <a href="https://datatracker.ietf.org/doc/html/rfc9114#section-4.1.1">cancelled the request stream</a> before receiving a complete response — the underlying connection may remain open. This is a normal part of web traffic.</p>
<p><strong>Tip</strong>: If you use <code>499</code> codes in availability calculations, consider whether client-initiated cancellations should be excluded from error rates. These typically represent normal user behavior — such as closing a browser, navigating away from a page, mobile network drops, or cancelling a download — rather than service issues.</p>
<hr />
<p>For more information, refer to <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-499/">Error 499</a>.</p>
</div></article></div>
