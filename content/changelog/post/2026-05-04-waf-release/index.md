---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-04-waf-release/
  description: New updates and improvements at Cloudflare.
  full_title: WAF Release - 2026-05-04 · Changelog
  head_html: <title>WAF Release - 2026-05-04 · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-04-waf-release/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="WAF Release - 2026-05-04 · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-04-waf-release/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-04-waf-release/#page","headline":"WAF Release - 2026-05-04 \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-04-waf-release/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-04-waf-release/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 4, 2026</time><h2 id="post-title">WAF Release - 2026-05-04</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on new detections to expand coverage across command injection, SQL injection, PHP object injection, remote code execution, and XSS attack vectors.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<p><strong>Continuous Rule Improvements</strong></p>
<p>We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.</p>
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
				<code class="nb-rule-id" title="607ec27233b54beb8b89386ef0884a68">f0884a68</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Object Tag - Body (beta)</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"XSS, HTML Injection - Object Tag" (ID:{" "}
				<code class="nb-rule-id" title="e9e3ac45a6d842f1a132fbf70c14e284">0c14e284</code>).
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0087c27420c54168a10bc05eff012303">ff012303</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Object Tag - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. The rule previously known as "XSS, HTML
				Injection - Object Tag - Headers (beta)" is now renamed to "XSS, HTML
				Injection - Object Tag - Headers".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="38dc97853ebf40ed9476ec7816f921d9">16f921d9</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Object Tag - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. The rule previously known as "XSS, HTML
				Injection - Object Tag - URI (beta)" is now renamed to "XSS, HTML
				Injection - Object Tag - URI".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="963cb530f72d4c75b2ae7befdc90d21a">dc90d21a</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - Body Vector - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 9 - Body Vector" (ID:{" "}
				<code class="nb-rule-id" title="155bb67d1061479e995a38510677175f">0677175f</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ac1b6dfe22449a798cc7021f8960375">f8960375</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - Header Vector - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 9 - Header Vector" (ID:{" "}
				<code class="nb-rule-id" title="b31c34a7b29b4aaf9be6883d1eb7a999">1eb7a999</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="47a9b66dd73a4a558590c4bdef47a800">ef47a800</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - URI Vector - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 9 - URI Vector" (ID:{" "}
				<code class="nb-rule-id" title="54ad0465c30d4cd2ac7a707197321c6c">97321c6c</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d2ae4a8093f245a1b9de71bbbeebf804">beebf804</code>
</td>
<td>N/A</td>
<td>Command Injection - Sleep - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. The rule previously known as "Command Injection
				- Sleep" is now renamed to "Command Injection - Sleep - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="da91868c0d3d44afb846e7830d257566">0d257566</code>
</td>
<td>N/A</td>
<td>Command Injection - Sleep - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="04863c61e982464b91778f051856fe86">1856fe86</code>
</td>
<td>N/A</td>
<td>Command Injection - Sleep - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9dc1a0b8dbb7425db619309be6e43c37">e6e43c37</code>
</td>
<td>N/A</td>
<td>Fortinet FortiSandbox - Command Injection - CVE:CVE-2026-39808</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b84c10f5a8f84800905932dc88118795">88118795</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Common Bash Bypass - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f496c40011f14bfdb5f55ec79299d53b">9299d53b</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Common Bash Bypass - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a5f75abac2664554a984d061b0bf33f9">b0bf33f9</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Common Bash Bypass - Body - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Remote Code Execution - Common Bash Bypass Body" (ID:{" "}
				<code class="nb-rule-id" title="6e2f7a696ea74c979e7d069cefb7e5b9">efb7e5b9</code>). The rule previously
				known as "Remote Code Execution - Common Bash Bypass Beta" is now
				renamed to "Remote Code Execution - Common Bash Bypass Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bbb31a886ab54f6c8cdd220d33bfe8b9">33bfe8b9</code>
</td>
<td>N/A</td>
<td>PHP Object Injection - 2 - Body - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"PHP Object Injection - 2" (ID:{" "}
				<code class="nb-rule-id" title="8ef3c3f91eef46919cc9cb6d161aafdc">161aafdc</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e199688ab69746c88c33457f29552387">29552387</code>
</td>
<td>N/A</td>
<td>PHP Object Injection - 2 - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="eb33d40e96c54e929af6ed9c8104f4c5">8104f4c5</code>
</td>
<td>N/A</td>
<td>PHP Object Injection - 2 - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="76b15b7b122a4be6a40d8aa96a46201e">6a46201e</code>
</td>
<td>N/A</td>
<td>SQLi - DROP - 2 - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - DROP - 2" (ID:{" "}
				<code class="nb-rule-id" title="a967a167874b42b6898be46e48ac2221">48ac2221</code>)
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e24b2ef4a5c54f97a62db7a68b7f85ee">8b7f85ee</code>
</td>
<td>N/A</td>
<td>SQLi - DROP - 2 - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="51123f35f1d249358aea8fb11546b5f0">1546b5f0</code>
</td>
<td>N/A</td>
<td>SQLi - DROP - 2 - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d86d8873310d41f2877458a91e053dce">1e053dce</code>
</td>
<td>N/A</td>
<td>SmarterMail - Remote Code Execution - CVE:CVE-2026-24423</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="00da180570d34b5bae2121acd0023a36">d0023a36</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - Body</td>
<td>Block</td>
<td>Disabled</td>
<td>Action changed</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c46d9097c9ef419aa4d9f10626cc211f">26cc211f</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - URI</td>
<td>Block</td>
<td>Disabled</td>
<td>Action changed</td>
</tr>
</tbody>
</table>
</div></article></div>
