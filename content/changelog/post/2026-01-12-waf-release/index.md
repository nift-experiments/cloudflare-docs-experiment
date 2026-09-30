---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2026-01-12 · Changelog
  head_html: <title>WAF Release - 2026-01-12 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2026-01-12 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/#page","headline":"WAF Release - 2026-01-12 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-01-12-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-01-12-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 12, 2026</time><h2 id="post-title">WAF Release - 2026-01-12</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against SQL Injection.</li>
</ul>
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
        <code class="nb-rule-id" title="72963b917ef74697b5bde02f48a1841a">48a1841a</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - AND/OR MAKE_SET/ELT" (ID: <code class="nb-rule-id" title="0f41a593c8fe42c38a26f709252d3934">252d3934</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="adf076af09b2484ca9e7881f9e553ad3">9e553ad3</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Benchmark Function" (ID: <code class="nb-rule-id" title="ac4e9ebfb43a4f3998f6072d2ebc44ad">2ebc44ad</code>)</td>
</tr>
</tbody>    
</table>
</div></article></div>
