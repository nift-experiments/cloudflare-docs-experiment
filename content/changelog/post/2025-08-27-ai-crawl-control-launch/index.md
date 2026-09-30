---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/
  description: New updates and improvements at Cloudflare.
  full_title: Enhanced crawler insights and custom 402 responses · Changelog
  head_html: <title>Enhanced crawler insights and custom 402 responses · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Enhanced crawler insights and custom 402 responses · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/#page","headline":"Enhanced crawler insights and custom 402 responses \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-27-ai-crawl-control-launch/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-27-ai-crawl-control-launch/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 27, 2025</time><h2 id="post-title">Enhanced crawler insights and custom 402 responses</h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>We improved AI crawler management with detailed analytics and introduced custom HTTP 402 responses for blocked crawlers. AI Audit has been renamed to AI Crawl Control and is now generally available.</p>
<p><strong>Enhanced Crawlers tab:</strong></p>
<ul>
<li>View total allowed and blocked requests for each AI crawler</li>
<li>Trend charts show crawler activity over your selected time range per crawler</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-table.png" alt="Updated AI Crawl Control table showing request counts and trend charts" /></p>
<p><strong>Custom block responses (paid plans):</strong>
You can now return HTTP 402 &quot;Payment Required&quot; responses when blocking AI crawlers, enabling direct communication with crawler operators about licensing terms.</p>
<p>For users on paid plans, when blocking AI crawlers you can configure:</p>
<ul>
<li><strong>Response code:</strong> Choose between 403 Forbidden or 402 Payment Required</li>
<li><strong>Response body:</strong> Add a custom message with your licensing contact information</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-block-response.png" alt="AI Crawl Control block response configuration interface" /></p>
<p>Example 402 response:</p>
<pre tabindex="0"><code class="language-http">HTTP 402 Payment Required&#10;Date: Mon, 24 Aug 2025 12:56:49 GMT&#10;Content-type: application/json&#10;Server: cloudflare&#10;Cf-Ray: 967e8da599d0c3fa-EWR&#10;Cf-Team: 2902f6db750000c3fa1e2ef400000001&#10;&#10;{&#10;  &quot;message&quot;: &quot;Please contact the site owner for access.&quot;&#10;}&#10;</code></pre>
</div></article></div>
