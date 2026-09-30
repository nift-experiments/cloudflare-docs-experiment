---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-29-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2025-09-29 · Changelog
  head_html: <title>WAF Release - 2025-09-29 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-29-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2025-09-29 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-29-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-29-waf-release/#page","headline":"WAF Release - 2025-09-29 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-29-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-29-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 29, 2025</time><h2 id="post-title">WAF Release - 2025-09-29</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights four important vendor- and component-specific issues: an authentication bypass in SimpleHelp (CVE-2024-57727), an information-disclosure flaw in Flowise Cloud (CVE-2025-58434), an SSRF in the WordPress plugin Ditty (CVE-2025-8085), and a directory-traversal bug in Vite (CVE-2025-30208). These are paired with improvements to our generic detection coverage (SQLi, SSRF) to raise the baseline and reduce noisy gaps.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>SimpleHelp (CVE-2024-57727): Authentication bypass in SimpleHelp that can allow unauthorized access to management interfaces or sessions.</p>
</li>
<li>
<p>Flowise Cloud (CVE-2025-58434): Information-disclosure vulnerability in Flowise Cloud that may expose sensitive configuration or user data to unauthenticated or low-privileged actors.</p>
</li>
<li>
<p>WordPress:Plugin: Ditty (CVE-2025-8085): SSRF in the Ditty WordPress plugin enabling server-side requests that could reach internal services or cloud metadata endpoints.</p>
</li>
<li>
<p>Vite (CVE-2025-30208): Directory-traversal vulnerability in Vite allowing access to filesystem paths outside the intended web root.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities allow attackers to gain access, escalate privileges, or execute actions that were previously unavailable:</p>
<ul>
<li>
<p>SimpleHelp (CVE-2024-57727): An authentication bypass that can let unauthenticated attackers access management interfaces or hijack sessions — enabling lateral movement, credential theft, or privilege escalation within affected environments.</p>
</li>
<li>
<p>Flowise Cloud (CVE-2025-58434): Information-disclosure flaw that can expose sensitive configuration, tokens, or user data; leaked secrets may be chained into account takeover or privileged access to backend services.</p>
</li>
<li>
<p>WordPress:Plugin: Ditty (CVE-2025-8085): SSRF that enables server-side requests to internal services or cloud metadata endpoints, potentially allowing attackers to retrieve credentials or reach otherwise inaccessible infrastructure, leading to privilege escalation or cloud resource compromise.</p>
</li>
<li>
<p>Vite (CVE-2025-30208): Directory-traversal vulnerability that can expose filesystem contents outside the web root (configuration files, keys, source code), which attackers can use to escalate privileges or further compromise systems.</p>
</li>
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
        <code class="nb-rule-id" title="6fe90532af50427484a5275c8c2e30fb">8c2e30fb</code>
</td>
<td>100717</td>
<td>SimpleHelp - Auth Bypass - CVE:CVE-2024-57727</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged to 100717 in legacy WAF and <code class="nb-rule-id" title="498fcd81a62a4b5ca943e2de958094d3">958094d3</code> in new WAF</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="013ef5de3f074fd5a43cdd70d58b886b">d58b886b</code>
</td>
<td>100775</td>
<td>Flowise Cloud - Information Disclosure - CVE:CVE-2025-58434</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="68fc5c086ccb4b40a35a63b19bce1ff4">9bce1ff4</code>
</td>
<td>100881</td>
<td>WordPress:Plugin:Ditty - SSRF - CVE:CVE-2025-8085</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9e1a56e6b3bc49b187bf6e35ddc329dd">ddc329dd</code>
</td>
<td>100887</td>
<td>Vite - Directory Traversal - CVE:CVE-2025-30208</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
