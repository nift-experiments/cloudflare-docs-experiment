---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/
  description: New updates and improvements at Cloudflare.
  full_title: Improved Payload Logging for WAF Managed Rules · Changelog
  head_html: <title>Improved Payload Logging for WAF Managed Rules · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Improved Payload Logging for WAF Managed Rules · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/#page","headline":"Improved Payload Logging for WAF Managed Rules \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-05-08-improved-payload-logging/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-05-08-improved-payload-logging/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 8, 2025</time><h2 id="post-title">Improved Payload Logging for WAF Managed Rules</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>We have upgraded WAF Payload Logging to enhance rule diagnostics and usability:</p>
<ul>
<li><strong>Targeted logging</strong>: Logs now capture only the specific portions of requests that triggered WAF rules, rather than entire request segments.</li>
<li><strong>Visual highlighting</strong>: Matched content is visually highlighted in the UI for faster identification.</li>
<li><strong>Enhanced context</strong>: Logs now include surrounding context to make diagnostics more effective.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/waf/2025-05-payload-logging-update.png" alt="Log entry showing payload logging details" /></p>
<p>Payload Logging is available to all Enterprise customers. If you have not used Payload Logging before, check how you can <a href="/waf/managed-rules/payload-logging/">get started</a>.</p>
<p><strong>Note:</strong> The structure of the <code>encrypted_matched_data</code> field in Logpush has changed from <code>Map&lt;Field, Value&gt;</code> to <code>Map&lt;Field, {Before: bytes, Content: Value, After: bytes}&gt;</code>. If you rely on this field in your Logpush jobs, you should review and update your processing logic accordingly.</p>
</div></article></div>
