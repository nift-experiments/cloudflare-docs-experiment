---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/
  description: New updates and improvements at Cloudflare.
  full_title: Log Explorer adds 14 new datasets · Changelog
  head_html: <title>Log Explorer adds 14 new datasets · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Log Explorer adds 14 new datasets · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/#page","headline":"Log Explorer adds 14 new datasets \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-11-13-new-datasets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-11-13-new-datasets/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 13, 2025</time><h2 id="post-title">Log Explorer adds 14 new datasets</h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>We've significantly enhanced Log Explorer by adding support for 14 additional Cloudflare product datasets.</p>
<p>This expansion enables Operations and Security Engineers to gain deeper visibility and telemetry across a wider range of Cloudflare services. By integrating these new datasets, users can now access full context to efficiently investigate security incidents, troubleshoot application performance issues, and correlate logged events across different layers (like application and network) within a single interface. This capability is crucial for a complete and cohesive understanding of event flows across your Cloudflare environment.</p>
<p>The newly supported datasets include:</p>
<h4 id="zone-level">Zone Level</h4>
<ul>
<li><code>Dns_logs</code></li>
<li><code>Nel_reports</code></li>
<li><code>Page_shield_events</code></li>
<li><code>Spectrum_events</code></li>
<li><code>Zaraz_events</code></li>
</ul>
<h4 id="account-level">Account Level</h4>
<ul>
<li><code>Audit Logs</code></li>
<li><code>Audit_logs_v2</code></li>
<li><code>Biso_user_actions</code></li>
<li><code>DNS firewall logs</code></li>
<li><code>Email_security_alerts</code></li>
<li><code>Magic Firewall IDS</code></li>
<li><code>Network Analytics</code></li>
<li><code>Sinkhole HTTP</code></li>
<li><code>ipsec_logs</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17736.md")</aside>
<h4 id="example-correlating-logs">Example: Correlating logs</h4>
<p>You can now use Log Explorer to query and filter with each of these datasets. For example, you can identify an IP address exhibiting suspicious behavior in the <code>FW_event</code> logs, and then instantly pivot to the <code>Network Analytics</code> logs or <code>Access</code> logs to see its network-level traffic profile or if it bypassed a corporate policy.</p>
<p>To learn more and get started, refer to the <a href="/log-explorer/">Log Explorer documentation</a> and the <a href="/logs/">Cloudflare Logs documentation</a>.</p>
</div></article></div>
