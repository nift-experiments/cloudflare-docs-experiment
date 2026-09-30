---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2025-10-24 - Emergency · Changelog
  head_html: <title>WAF Release - 2025-10-24 - Emergency · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2025-10-24 - Emergency · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/#page","headline":"WAF Release - 2025-10-24 - Emergency \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-24-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-24-emergency-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 24, 2025</time><h2 id="post-title">WAF Release - 2025-10-24 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Windows Server Update Services (WSUS), tracked as CVE-2025-59287.</p>
<p><strong>Key Findings</strong></p>
<p>The vulnerability allows unauthenticated attackers to potentially achieve remote code execution. The updated detection logic strengthens defenses by improving resilience against exploitation attempts targeting this flaw.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-59287 could enable attackers to hijack sessions, execute arbitrary commands, exfiltrate sensitive data, and disrupt storefront operations. These actions pose significant confidentiality and integrity risks to affected environments. Administrators should apply vendor patches immediately to mitigate exposure.</p>
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
        <code class="nb-rule-id" title="5eaeb5ea6e5a4bce867eb3ffbd72ba08">bd72ba08</code>
</td>
<td>N/A</td>
<td>Windows Server - Deserialization - CVE:CVE-2025-59287</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
