---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2025-07-07 · Changelog
  head_html: <title>WAF Release - 2025-07-07 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2025-07-07 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/#page","headline":"WAF Release - 2025-07-07 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-07-07-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-07-07-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 7, 2025</time><h2 id="post-title">WAF Release - 2025-07-07</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s roundup uncovers critical vulnerabilities affecting enterprise VoIP systems, webmail platforms, and a popular JavaScript framework. The risks range from authentication bypass to remote code execution (RCE) and buffer handling flaws, each offering attackers a path to elevate access or fully compromise systems.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Next.js - Auth Bypass: A newly detected authentication bypass flaw in the Next.js framework allows attackers to access protected routes or APIs without proper authorization, undermining application access controls.</li>
<li>Fortinet FortiVoice (CVE-2025-32756): A buffer error vulnerability in FortiVoice systems that could lead to memory corruption and potential code execution or service disruption in enterprise telephony environments.</li>
<li>Roundcube (CVE-2025-49113): A critical RCE flaw allowing unauthenticated attackers to execute arbitrary PHP code via crafted requests, leading to full compromise of mail servers and user inboxes.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities affect core business infrastructure, from web interfaces to voice communications and email platforms. The Roundcube RCE and FortiVoice buffer flaw offer potential for deep system access, while the Next.js auth bypass undermines trust boundaries in modern web apps.</p>
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
				<code class="nb-rule-id" title="b6558cac8c874bd6878734057eb35ee6">7eb35ee6</code>
</td>
<td>100795</td>
<td>Next.js - Auth Bypass</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58fcf6d9c05d4b7a8f41e0a3c329aeb0">c329aeb0</code>
</td>
<td>100796</td>
<td>Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="34ed0624bc864ea88bbea55bab314023">ab314023</code>
</td>
<td>100797</td>
<td>Roundcube - Remote Code Execution - CVE:CVE-2025-49113</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
