---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/
  description: New updates and improvements at Cloudflare.
  full_title: Leaked Credentials Insights in Cloudflare Radar · Changelog
  head_html: <title>Leaked Credentials Insights in Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Leaked Credentials Insights in Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/#page","headline":"Leaked Credentials Insights in Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-03-18-radar-leaked-credentials-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-03-18-radar-leaked-credentials-insights/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 18, 2025</time><h2 id="post-title">Leaked Credentials Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its security insights, providing visibility into aggregate trends in authentication requests,
including the detection of leaked credentials through <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a> scans.</p>
<p>We have now introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/leaked_credentials/subresources/summary/"><code>/leaked_credential_checks/summary/{dimension}</code></a>: Retrieves summaries of HTTP authentication requests distribution across two different dimensions.</li>
<li><a href="/api/resources/radar/subresources/leaked_credentials/subresources/timeseries_groups/"><code>/leaked_credential_checks/timeseries_groups/{dimension}</code></a>: Retrieves timeseries data for HTTP authentication requests distribution across two different dimensions.</li>
</ul>
<p>The following dimensions are available, displaying the distribution of HTTP authentication requests based on:</p>
<ul>
<li><code>compromised</code>: Credential status (clean vs. compromised).</li>
<li><code>bot_class</code>: <a href="/radar/concepts/bot-classes">Bot class</a> (human vs. bot).</li>
</ul>
<p>Dive deeper into leaked credential detection in this <a href="https://blog.cloudflare.com/password-reuse-rampant-half-user-logins-compromised/">blog post</a> and learn more about the expanded Radar security insights in our <a href="https://blog.cloudflare.com/cloudflare-radar-ddos-leaked-credentials-bots">blog post</a>.</p>
</div></article></div>
