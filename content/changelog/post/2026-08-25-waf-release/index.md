---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2026-08-25 · Changelog
  head_html: <title>WAF Release - 2026-08-25 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2026-08-25 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/#page","headline":"WAF Release - 2026-08-25 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-25-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-08-25-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 25, 2026</time><h2 id="post-title">WAF Release - 2026-08-25</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release moves four new detections from Log to Block, merges the XSS, HTML Injection - Script Tag - Beta rule into the original rule, and adds a Generic Rules - Remote Code Execution rule in Block mode.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Four new detections move from Log to Block: HTTP/2 Request Smuggling - Request Body Anomaly and XSS - JavaScript Event Handler Coercion across Headers, Body, and URI.</p>
</li>
<li>
<p>The XSS, HTML Injection - Script Tag - Beta rule is merged into the original rule.</p>
</li>
<li>
<p>A Generic Rules - Remote Code Execution detection is added in Block mode.</p>
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
				<code class="nb-rule-id" title="a80f214f0947435dabb2ba2d1489d892">1489d892</code>
</td>
<td>N/A</td>
<td>HTTP/2 Request Smuggling - Request Body Anomaly</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58a184412d2b4113bca6379b20646260">20646260</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e79cb939d6aa41db984e6db3d706d517">d706d517</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - Body</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7e3249c7a5d8469697478746660886c8">660886c8</code>
</td>
<td>N/A</td>
<td>XSS - JavaScript Event Handler Coercion - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d34bc5db8cbc4e18a44ed115c293b926">c293b926</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Script Tag - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "XSS, HTML Injection - Script Tag" (ID:{" "}<code class="nb-rule-id" title="9c8dda9708cc4452ac76e7be7b58420b">7b58420b</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>
</td>
<td>N/A</td>
<td>Generic Rules - Remote Code Execution</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div></article></div>
