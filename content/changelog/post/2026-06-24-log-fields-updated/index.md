---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/
  description: New updates and improvements at Cloudflare.
  full_title: New WebSocket Analytics Logpush dataset and updated fields · Changelog
  head_html: <title>New WebSocket Analytics Logpush dataset and updated fields · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New WebSocket Analytics Logpush dataset and updated fields · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/#page","headline":"New WebSocket Analytics Logpush dataset and updated fields \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-24-log-fields-updated/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-24-log-fields-updated/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 24, 2026</time><h2 id="post-title">New WebSocket Analytics Logpush dataset and updated fields</h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="new-datasets">New datasets</h4>
<ul>
<li><strong>WebSocket Analytics</strong>: A new dataset with fields including <code>BytesReceivedClient</code>, <code>BytesReceivedOrigin</code>, <code>BytesSentClient</code>, <code>BytesSentOrigin</code>, <code>ClientASN</code>, <code>ClientIP</code>, <code>ClientRequestHost</code>, <code>ClientRequestPath</code>, <code>ClientRequestUserAgent</code>, <code>ColoCode</code>, <code>ConnectionCloseReason</code>, <code>ConnectionCloseSource</code>, <code>ConnectionID</code>, <code>ConnectionTransportCloseCode</code>, <code>EdgeEndTimestamp</code>, <code>EdgeStartTimestamp</code>, and <code>RayID</code>.</li>
</ul>
<h4 id="updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>ZoneName</code>. The Firewall events dataset is now also available for <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/">account-scope Logpush</a>, in addition to the existing zone scope.</li>
<li><strong>Email Security Alerts</strong> (added): <code>BCC</code>, <code>DKIMResult</code>, <code>DMARCPolicy</code>, <code>DMARCResult</code>, and <code>SPFResult</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div></article></div>
