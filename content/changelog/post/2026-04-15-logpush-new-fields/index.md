---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/
  description: New updates and improvements at Cloudflare.
  full_title: New TenantID and Firewall for AI fields in Logpush datasets · Changelog
  head_html: <title>New TenantID and Firewall for AI fields in Logpush datasets · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New TenantID and Firewall for AI fields in Logpush datasets · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/#page","headline":"New TenantID and Firewall for AI fields in Logpush datasets \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-logpush-new-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-15-logpush-new-fields/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 15, 2026</time><h2 id="post-title">New TenantID and Firewall for AI fields in Logpush datasets</h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has added new fields to multiple <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="tenantid-field">TenantID field</h4>
<p>The following Gateway and Zero Trust datasets now include a <code>TenantID</code> field:</p>
<ul>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#tenantid">Gateway DNS</a></strong>: Identifies the tenant ID of the DNS request, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_http/#tenantid">Gateway HTTP</a></strong>: Identifies the tenant ID of the HTTP request, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_network/#tenantid">Gateway Network</a></strong>: Identifies the tenant ID of the network session, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#tenantid">Zero Trust Network Sessions</a></strong>: Identifies the tenant ID of the network session, if it exists.</li>
</ul>
<h4 id="firewall-for-ai-fields">Firewall for AI fields</h4>
<p>The following datasets now include <a href="/api-shield/security/volumetric-abuse-detection/#firewall-for-ai">Firewall for AI</a> fields:</p>
<ul>
<li>
<p><strong><a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">Firewall Events</a></strong>:</p>
<ul>
<li><code>FirewallForAIInjectionScore</code>: The score indicating the likelihood of a prompt injection attack in the request.</li>
<li><code>FirewallForAIPIICategories</code>: List of PII categories detected in the request.</li>
<li><code>FirewallForAITokenCount</code>: The number of tokens in the request.</li>
<li><code>FirewallForAIUnsafeTopicCategories</code>: List of unsafe topic categories detected in the request.</li>
</ul>
</li>
<li>
<p><strong><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a></strong>:</p>
<ul>
<li><code>FirewallForAIInjectionScore</code>: The score indicating the likelihood of a prompt injection attack in the request.</li>
<li><code>FirewallForAIPIICategories</code>: List of PII categories detected in the request.</li>
<li><code>FirewallForAITokenCount</code>: The number of tokens in the request.</li>
<li><code>FirewallForAIUnsafeTopicCategories</code>: List of unsafe topic categories detected in the request.</li>
</ul>
</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div></article></div>
