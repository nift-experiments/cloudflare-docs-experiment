---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2026-06-09 · Changelog
  head_html: <title>WAF Release - 2026-06-09 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2026-06-09 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/#page","headline":"WAF Release - 2026-06-09 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-06-09-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-06-09-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 9, 2026</time><h2 id="post-title">WAF Release - 2026-06-09</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new detections for a critical SQL injection vulnerability in Drupal installations utilizing PostgreSQL (CVE-2026-9082), alongside targeted protection for an unsafe deserialization flaw in the Mirasvit Cache Warmer extension (CVE-2026-45247). Additionally, this release includes coverage for a prototype pollution vector in Axios (CVE-2026-40175) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-9082: A database abstraction vulnerability affects Drupal sites configured with a PostgreSQL backend. Remote, unauthenticated attackers can exploit this flaw via crafted inputs to inject malicious SQL commands and access or manipulate backend data.</p>
</li>
<li>
<p>CVE-2026-45247: A PHP Object Injection vulnerability exists in the Mirasvit Cache Warmer extension for Magento and Adobe Commerce. This flaw stems from unsafe deserialization of untrusted user input, enabling unauthenticated attackers to execute arbitrary code on the hosting server.</p>
</li>
<li>
<p>CVE-2026-40175: A prototype pollution vulnerability affects the Axios HTTP client library. Attackers can exploit this to inject malicious properties into the global JavaScript object prototype, potentially causing application crashes (Denial of Service) or executing unauthorized code depending on the application structure.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, manipulate database contents, or induce application crashes, leading to severe operational disruption or complete server compromise. These newly deployed signatures intercept these advanced malicious payloads at the edge before they can interact with vulnerable software configurations.</p>
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
				<code class="nb-rule-id" title="b4f88cb767874def810edd0b387cf935">387cf935</code>
</td>
<td>N/A</td>
<td>Axios - Prototype Pollution - CVE:CVE-2026-40175</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="098997bb8b5f48abb4039bd6417eb9e0">417eb9e0</code>
</td>
<td>N/A</td>
<td>Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - Body</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8a7650b99ec04a91a19b8295fd3857fd">fd3857fd</code>
</td>
<td>N/A</td>
<td>Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="525c0871787840e6a6193f6caee241d2">aee241d2</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1ec4aeaf7900463397b82b35d8620070">d8620070</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fb74766654c44ff2a5204dc4e0be4d47">e0be4d47</code>
</td>
<td>N/A</td>
<td>Mirasvit Cache Warmer - PHP Object Injection - CVE:CVE-2026-45247</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>
</div></article></div>
