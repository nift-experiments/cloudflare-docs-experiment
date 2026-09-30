---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2026-09-10 - Emergency · Changelog
  head_html: <title>WAF Release - 2026-09-10 - Emergency · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2026-09-10 - Emergency · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/#page","headline":"WAF Release - 2026-09-10 - Emergency \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-09-10-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-09-10-emergency-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 10, 2026</time><h2 id="post-title">WAF Release - 2026-09-10 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This update provides immediate defense against a high-severity, actively exploited zero-day vulnerability targeting Adobe Commerce and Magento Open Source storefronts.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Adobe Commerce and Magento RCE (CVE-2026-75650 / &quot;StyleSmuggler&quot;): Unauthenticated Remote Code Execution (RCE) vulnerability caused by improper neutralization of special elements in the platform's template engine. Unauthenticated attackers can inject arbitrary PHP payloads through style properties to execute system commands and deploy persistent malware.</li>
</ul>
<p><strong>Impact</strong></p>
<p>This emergency rule provides immediate edge-level mitigation and virtual patching, origin applications must be urgently updated. We strongly recommend to apply the hotfix outlined in Adobe Security Bulletin <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146">APSB26-146</a> and immediately rotate all potentially exposed encryption keys, integration tokens, and system credentials, as patching alone does not remediate an existing compromise.</p>
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
				<code class="nb-rule-id" title="f9a3026b0fdc4d63b7338346440f5c55">440f5c55</code>
</td>
<td>N/A</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2026-75650</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>
</div></article></div>
