---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2026-08-11 · Changelog
  head_html: <title>WAF Release - 2026-08-11 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2026-08-11 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/#page","headline":"WAF Release - 2026-08-11 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-11-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-11-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 11, 2026</time><h2 id="post-title">WAF Release - 2026-08-11</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new protection for a remote code execution vulnerability in vBulletin and improves two existing detections.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>A new detection provides protection against vBulletin CVE-2026-61511.</li>
<li>Two existing detections have been improved to strengthen coverage.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2026-61511 may lead to remote code execution on affected vBulletin systems, potentially resulting in unauthorized access, data exposure, service disruption, and broader compromise of the hosting environment. Administrators are strongly encouraged to apply vendor updates and recommended mitigations.</p>
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
				<code class="nb-rule-id" title="1b0775f0f092483387cfb23f94f3006b">94f3006b</code>
</td>
<td>N/A</td>
<td>vBulletin - Remote Code Execution - CVE:CVE-2026-61511</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="784d3824b6cf419db6af0b64098b749e">098b749e</code>
</td>
<td>N/A</td>
<td>Version Control - Information Disclosure - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Version Control - Information Disclosure" (ID: <code class="nb-rule-id" title="23548ee2b36547a1be09bb2c0550c529">0550c529</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a561c9138b46470ca6db96edd56225d8">d56225d8</code>
</td>
<td>N/A</td>
<td>vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132" (ID: <code class="nb-rule-id" title="5137834eb8634842852273a08fe9f1c7">8fe9f1c7</code>)</td>
</tr>
</tbody>
</table>
</div></article></div>
