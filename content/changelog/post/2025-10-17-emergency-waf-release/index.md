---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-10-17-emergency-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: New detections released for WAF managed rulesets · Changelog
  head_html: <title>New detections released for WAF managed rulesets · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-10-17-emergency-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New detections released for WAF managed rulesets · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-10-17-emergency-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-17-emergency-waf-release/#page","headline":"New detections released for WAF managed rulesets \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-10-17-emergency-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-10-17-emergency-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 17, 2025</time><h2 id="post-title">New detections released for WAF managed rulesets</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week we introduced several new detections across Cloudflare Managed Rulesets, expanding coverage for high-impact vulnerability classes such as SSRF, SQLi, SSTI, Reverse Shell attempts, and Prototype Pollution. These rules aim to improve protection against attacker-controlled payloads that exploit misconfigurations or unvalidated input in web applications.</p>
<p><strong>Key Findings</strong></p>
<p>New detections added for multiple exploit categories:</p>
<p>SSRF (Server-Side Request Forgery) — new rules targeting both local and cloud metadata abuse patterns (Beta).</p>
<p>SQL Injection (SQLi) — rules for common patterns, sleep/time-based injections, and string/wait function exploitation across headers and URIs.</p>
<p>SSTI (Server-Side Template Injection) — arithmetic-based probe detections introduced across URI, header, and body fields.</p>
<p>Reverse Shell and XXE payloads — enhanced heuristics for command execution and XML external entity misuse.</p>
<p>Prototype Pollution — new Beta rule identifying common JSON payload structures used in object prototype poisoning.</p>
<p>PHP Wrapper Injection and HTTP Parameter Pollution detections — to catch path traversal and multi-parameter manipulation attempts.</p>
<p>Anomaly Header Checks — detecting CRLF injection attempts in header names.</p>
<p><strong>Impact</strong></p>
<p>These updates help detect multi-vector payloads that blend SSRF + RCE or SQLi + SSTI attacks, especially in cloud-hosted applications with exposed metadata endpoints or unsafe template rendering.</p>
<p>Prototype Pollution and HTTP parameter pollution rules address emerging JavaScript supply-chain exploitation patterns increasingly seen in real-world incidents.</p>
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
<td><code class="nb-rule-id" title="72f0ff933fb0492eb71cda50589f2a1d">589f2a1d</code></td>
<td>N/A</td>
<td>Anomaly:Header - name - CR, LF</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="5d0377e4435f467488614170132fab7e">132fab7e</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="54e32f7f802c4a699182e8921a027008">1a027008</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - Header</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="7cbda8dbafbc465d9b64a8f2958d0486">958d0486</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="b9f3420674cf481da32333dc8e0cf7ad">8e0cf7ad</code></td>
<td>N/A</td>
<td>Generic Rules - XXE - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="ad55483512f0440b81426acdbf8aab5e">bf8aab5e</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - Common Patterns - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="849c0618d1674f1c92ba6f9b2e466337">2e466337</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - Sleep Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="1b4db4c4bd0649c095c27c6cb686ab47">b686ab47</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - String Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="fa2055b84af94ba4b925f834b0633709">b0633709</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - WaitFor Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="158177dec2504acdba1f2da201a076eb">01a076eb</code></td>
<td>N/A</td>
<td>SSRF - Local - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="98bfd6bb46074d5b8d1c4b39743a63ec">743a63ec</code></td>
<td>N/A</td>
<td>SSRF - Local - 2 - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code></td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="ecd26d61a75e46f6a4449a06ab8af26f">ab8af26f</code></td>
<td>N/A</td>
<td>SSRF - Cloud - 2 - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="c16f4e133c4541f293142d02e6e8dc5b">e6e8dc5b</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="f4fd9904e7624666b8c49cd62550d794">2550d794</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - Header</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="5c0875604f774c36a4f9b69c659d12a6">659d12a6</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code></td>
<td>N/A</td>
<td>PHP Wrapper Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code></td>
<td>N/A</td>
<td>PHP Wrapper Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="cb67fe56a84747b8b64277dc091e296d">091e296d</code></td>
<td>N/A</td>
<td>HTTP parameter pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="443b54d984944cd69043805ee34214ef">e34214ef</code></td>
<td>N/A</td>
<td>Prototype Pollution - Common Payloads - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
