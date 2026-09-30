---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2025-12-11 - Emergency · Changelog
  head_html: <title>WAF Release - 2025-12-11 - Emergency · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2025-12-11 - Emergency · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/#page","headline":"WAF Release - 2025-12-11 - Emergency \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-12-11-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-12-11-emergency-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 11, 2025</time><h2 id="post-title">WAF Release - 2025-12-11 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release introduces rules for CVE-2025-55183 and CVE-2025-55184, targeting server-side function exposure and resource-exhaustion patterns, respectively.</p>
<p><strong>Key Findings</strong></p>
<p>Added coverage for Leaking Server Functions (CVE-2025-55183) and React Function DoS detection (CVE-2025-55184).</p>
<p><strong>Impact</strong></p>
<p>These updates strengthen protection for server-function abuse techniques (CVE-2025-55183, CVE-2025-55184) that may expose internal logic or disrupt application availability.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="17c5123f1ac049818765ebf2fefb4e9b">fefb4e9b</code>
</td>
<td>N/A</td>
<td>React - Leaking Server Functions - CVE:CVE-2025-55183</td>
<td>N/A</td>
<td>Block</td>
<td>This was labeled as Generic - Server Function Source Code Exposure.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="3114709a3c3b4e3685052c7b251e86aa">251e86aa</code>
</td>
<td>N/A</td>
<td>React - Leaking Server Functions - CVE:CVE-2025-55183</td>
<td>N/A</td>
<td>Block</td>
<td>This was labeled as Generic - Server Function Source Code Exposure.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2694f1610c0b471393b21aef102ec699">102ec699</code>
</td>
<td>N/A</td>
<td>React - DoS - CVE:CVE-2025-55184</td>
<td>N/A</td>
<td>Disabled</td>
<td>This was labeled as Generic – Server Function Resource Exhaustion.</td>
</tr>
</tbody>
</table>
</div></article></div>
