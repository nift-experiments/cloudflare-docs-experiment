---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2025-07-28 · Changelog
  head_html: <title>WAF Release - 2025-07-28 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2025-07-28 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/#page","headline":"WAF Release - 2025-07-28 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-07-28-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-07-28-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 28, 2025</time><h2 id="post-title">WAF Release - 2025-07-28</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s update spotlights several vulnerabilities across Apache Tomcat, MongoDB, and Fortinet FortiWeb. Several flaws related with a memory leak in Apache Tomcat can lead to a denial-of-service attack. Additionally, a code injection flaw in MongoDB's Mongoose library allows attackers to bypass security controls to access restricted data.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Fortinet FortiWeb (CVE-2025-25257): An improper neutralization of special elements used in a SQL command vulnerability in Fortinet FortiWeb versions allows an unauthenticated attacker to execute unauthorized SQL code or commands.</p>
</li>
<li>
<p>Apache Tomcat (CVE-2025-31650): A improper Input Validation vulnerability in Apache Tomcat that could create memory leak when incorrect error handling for some invalid HTTP priority headers resulted in incomplete clean-up of the failed request.</p>
</li>
<li>
<p>MongoDB (CVE-2024-53900, CVE:CVE-2025-23061): Improper use of <code>$where</code> in match and a nested <code>$where</code> filter with a <code>populate()</code> match in Mongoose can lead to search injection.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities target user-facing components, web application servers, and back-end databases. A SQL injection flaw in Fortinet FortiWeb can lead to data theft or system compromise. A separate issue in Apache Tomcat involves a memory leak from improper input validation, which could be exploited for a denial-of-service (DoS) attack. Finally, a vulnerability in MongoDB's Mongoose library allows attackers to bypass security filters and access unauthorized data through malicious search queries.</p>
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
				<code class="nb-rule-id" title="6ab3bd3b58fb4325ac2d3cc73461ec9e">3461ec9e</code>
</td>
<td>100804</td>
<td>BerriAI - SSRF - CVE:CVE-2024-6587</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e6c4d02f42a4c3ca90649d50cb13e1d">0cb13e1d</code>
</td>
<td>100812</td>
<td>Fortinet FortiWeb - Remote Code Execution - CVE:CVE-2025-25257</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fd360d8fd9994e6bab6fb06067fae7f7">67fae7f7</code>
</td>
<td>100813</td>
<td>Apache Tomcat - DoS - CVE:CVE-2025-31650</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f9e01e28c5d6499cac66364b4b6a5bb1">4b6a5bb1</code>
</td>
<td>100815</td>
<td>MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="700d4fcc7b1f481a80cbeee5688f8e79">688f8e79</code>
</td>
<td>100816</td>
<td>MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
