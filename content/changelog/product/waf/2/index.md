---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/waf/2/
  description: '2026-05-07'
  full_title: waf changelog - page 2 | Cloudflare Docs
  head_html: <title>waf changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-05-07"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/waf/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="waf changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-05-07"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/waf/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/waf/2/#page","headline":"waf changelog - page 2 | Cloudflare Docs","description":"2026-05-07","url":"https://developers.cloudflare.com/changelog/product/waf/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/waf/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="waf-release-2026-05-07-emergency"><a href="/changelog/post/2026-05-07-emergency-waf-release/">WAF Release - 2026-05-07 - Emergency</a></h2>
<p><em>2026-05-07</em></p>
<p>This emergency release introduces a new rule to detect Next.js App Router middleware and proxy bypass attempts via segment-prefetch routes (CVE-2026-44575).</p>
<p><strong>Key Findings</strong></p>
<p>CVE-2026-44575: Next.js Middleware / Proxy Bypass in App Router Applications via Segment-Prefetch Routes</p>
<p>Successful exploitation allows unauthenticated attackers to bypass middleware or proxy-based authorization checks in affected Next.js App Router applications. This leads to unauthorized access to protected content, potential exposure of sensitive application data, and compromise of application security boundaries.</p>
<p>We strongly recommend upgrading to Next.js 15.5.16 or 16.2.5 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, enforce authorization in the underlying route or page logic instead of relying solely on middleware.</p>
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
				<code class="nb-rule-id" title="1de95bf6d6374e1099854278e77e4a53">e77e4a53</code>
</td>
<td>N/A</td>
<td>Next.js - Middleware Bypass via Invalid RSC Header - CVE:CVE-2026-44575</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-05-04"><a href="/changelog/post/2026-05-04-waf-release/">WAF Release - 2026-05-04</a></h2>
<p><em>2026-05-04</em></p>
<p>This week's release focuses on new detections to expand coverage across command injection, SQL injection, PHP object injection, remote code execution, and XSS attack vectors.</p>
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


<h2 id="waf-release-2026-04-30-emergency"><a href="/changelog/post/2026-04-30-emergency-waf-release/">WAF Release - 2026-04-30 - Emergency</a></h2>
<p><em>2026-04-30</em></p>
<p>This emergency release introduces a new rule to block a cPanel &amp; WHM Authentication Bypass related to CVE-2026-41940.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-41940: A critical authentication bypass vulnerability in cPanel &amp; WHM allows unauthenticated remote attackers to bypass authentication mechanisms and gain unauthorized administrative access to the web hosting control panel. This vulnerability affects the session validation logic, enabling attackers to craft malicious requests that circumvent normal authentication checks.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation allows unauthenticated attackers to gain administrative control over affected cPanel &amp; WHM installations. This leads to complete server compromise, potential theft or manipulation of hosted data, and significant service disruption across managed environments.</p>
<p>We strongly recommend applying official vendor patches for cPanel &amp; WHM immediately to address the underlying vulnerability.</p>
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
				<code class="nb-rule-id" title="fb29b1b660864285a5ebac86eb2b9e2f">eb2b9e2f</code>
</td>
<td>N/A</td>
<td>cPanel - Auth Bypass - CVE:CVE-2026-41940</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-04-27"><a href="/changelog/post/2026-04-27-waf-release/">WAF Release - 2026-04-27</a></h2>
<p><em>2026-04-27</em></p>
<p>This week's release focuses on new improvements to enhance coverage.</p>
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
				<code class="nb-rule-id" title="d866f980582748568385b94480cec1dd">80cec1dd</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.  This rule is merged into the original rule
				"PostgreSQL - SQLi - COPY - Body (ID:{" "}
				<code class="nb-rule-id" title="705a6b5569d5472596910e3ce7265a4e">e7265a4e</code>). The rule previously known as "PostgreSQL - SQLi - COPY" is now renamed to "PostgreSQL - SQLi - COPY - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="71d133c374d94559aa9fdf042903de89">2903de89</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9f1b1b7fd28a401b9d5c172d1036cfa6">1036cfa6</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8e40416659334b8ba789365755ff389e">55ff389e</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - AND/OR MAKE_SET/ELT - Body" (ID:{" "}
				<code class="nb-rule-id" title="0f41a593c8fe42c38a26f709252d3934">252d3934</code>). The rule previously known as "SQLi - AND/OR MAKE_SET/ELT" is now renamed to "SQLi - AND/OR MAKE_SET/ELT - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1e0d4372ee1e41b9804b2d5c346487f9">346487f9</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d2c961a164a64cf6b871c9511ac6ceca">1ac6ceca</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4dacc0e6f32d4c5da3c2293edd471337">dd471337</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Common Patterns - Body" (ID:{" "}
				<code class="nb-rule-id" title="98f746d07a6d48ab9dae669acb5d0b9b">cb5d0b9b</code>). The rule previously known as "SQLi - Common Patterns" is now renamed to "SQLi - Common Patterns - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="53a374379f2e41e9934791c1975c07b7">975c07b7</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9efedebfc371443f9fe7308605b1b06b">05b1b06b</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d53a791496d64700870334f4dd0ba3c7">dd0ba3c7</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Equation - Body" (ID:{" "}
				<code class="nb-rule-id" title="e7691e1e4f4d4769909f3df6c2eb3e7f">c2eb3e7f</code>). The rule previously known as "SQLi - Equation" is now renamed to "SQLi - Equation - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="46efbd3496e64c3f902ad33d3d1c2384">3d1c2384</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="46b937649a424b7ead90f6d0e1149ea6">e1149ea6</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="04d9182545f54ba8a4fa29fe205adbb0">205adbb0</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - AND/OR Digit Operator Digit - Body" (ID:{" "}
				<code class="nb-rule-id" title="762dd334ed0b4273816e3ff13893c564">3893c564</code>). The rule previously known as "SQLi - AND/OR Digit Operator Digit" is now renamed to "SQLi - AND/OR Digit Operator Digit - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="a24e7c15503948bc8766481aad2abbaa">ad2abbaa</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0c55eb362df64f92a85aa46753acbc0d">53acbc0d</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="18c9879b7e184c559d23c1652b45a97d">2b45a97d</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Benchmark Function - Body" (ID:{" "}
				<code class="nb-rule-id" title="ac4e9ebfb43a4f3998f6072d2ebc44ad">2ebc44ad</code>). The rule previously known as "SQLi - Benchmark Function" is now renamed to "SQLi - Benchmark Function - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2adbc36c52324efcb4681b829889aadc">9889aadc</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="69564af3bc54406080deed72491b28e9">491b28e9</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="94b1646f0b0b46ec9b96f7742aa649de">2aa649de</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Comparison - Body" (ID:{" "}
				<code class="nb-rule-id" title="8166da327a614849bfa29317e7907480">e7907480</code>). The rule previously known as "SQLi - Comparison" is now renamed to "SQLi - Comparison - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="455ce87681bd4200bf53456c39e3e013">39e3e013</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="8152816062ed47f69be0f907f4bdb492">f4bdb492</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="d5afd403a0544248b829fe5da1ff3b34">a1ff3b34</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - Body - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. This rule is merged into the original rule "SQLi - String Concatenation - Headers" (ID:{" "}
				<code class="nb-rule-id" title="3b0c61407d0b4f7d87e516472116d2fe">2116d2fe</code>).The rule previously known as "SQLi - String Concatenation - Headers" is now renamed to "SQLi - String Concatenation - Body". </td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="cb0ec290ee454138abe18b750d0e6c3b">0d0e6c3b</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.(Former Id was{" "}
				<code class="nb-rule-id" title="380099df2bb2469c91ebbb7b846d1940">846d1940</code>)</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="c46d9097c9ef419aa4d9f10626cc211f">26cc211f</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. (Former Id was{" "}
				<code class="nb-rule-id" title="bd19397228404b85aa3797238fae8c84">8fae8c84</code>)</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="6542d36980cf4018b4d5e2bfeacc78ab">eacc78ab</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - SELECT Expression - Body" (ID:{" "}
				<code class="nb-rule-id" title="00da180570d34b5bae2121acd0023a36">d0023a36</code>). The rule previously known as "SQLi - SELECT Expression" is now renamed to "SQLi - SELECT Expression - Body".
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="4073f7b575ff45dfb7621b43630bb223">630bb223</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="2721e3184d50466ea637e9afdcd6efb5">dcd6efb5</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="7ecca84c08aa4aad9b5a7bda18c47cea">18c47cea</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - ORD and ASCII- Body" (ID:{" "}
				<code class="nb-rule-id" title="2fc38b34a9d744d2a3cbcc41d0d207f9">d0d207f9</code>). The rule previously known as "SQLi - ORD and ASCII" is now renamed to "SQLi - ORD and ASCII- Body".
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="f6d10e10c9514eb49dcc2122bdb1618f">bdb1618f</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="60704f5c5513425c94cf77031d0906b6">1d0906b6</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="700613b191d3479ea2782b4e9fe4eff5">9fe4eff5</code>
</td>
<td>N/A</td>
<td>SQLi - Destructive Operations</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>					
</tbody>
</table>


<h2 id="waf-release-2026-04-21"><a href="/changelog/post/2026-04-21-waf-release/">WAF Release - 2026-04-21</a></h2>
<p><em>2026-04-21</em></p>
<p>This week's release introduces a new detection for a Remote Code Execution (RCE) vulnerability in Apache ActiveMQ (CVE-2026-34197) and an updated signature for Magento 2 - Unrestricted File Upload. Alongside these detections, we are continuing our work on rule refinements to provide deeper security insights for our customers.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Apache ActiveMQ (CVE-2026-34197): A vulnerability in Apache ActiveMQ allows an unauthenticated, remote attacker to execute arbitrary code. This flaw occurs during the processing of specially crafted network packets, leading to potential full system compromise.</p>
</li>
<li>
<p>Magento 2 - Unrestricted File Upload - 2: This is a follow-up enhancement to our existing protections for Magento and Adobe Commerce.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code or gain full administrative control over affected servers. We strongly recommend applying official vendor patches for Apache ActiveMQ and Magento to address the underlying vulnerabilities.</p>
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
				<code class="nb-rule-id" title="ff8df24181aa4573a81be531ee159e2e">ee159e2e</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 8 - uri</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. Previous description was "Command Injection - Generic 8 - uri - Beta"</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9429b63c137247faadeb8a29a15308cf">a15308cf</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 8 - body - Beta</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 8 - body" (ID:{" "}
				<code class="nb-rule-id" title="5b3ce84c099040c6a25cee2d413592e2">413592e2</code>). The rule previously known as "Command Injection - Generic 8" is now renamed to "Command Injection - Generic 8 - body".
</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="85aaf5db9e0c4237b87e837e958047ed">958047ed</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"MySQL - SQLi - Executable Comment - Body" (ID:{" "}
				<code class="nb-rule-id" title="8629bb58defe4193ab4d493c7bd2d8fa">7bd2d8fa</code>) The rule previously known as "MySQL - SQLi - Executable Comment" is now renamed to "MySQL - SQLi - Executable Comment - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d19cd574c4644952881a6f3a582cc559">582cc559</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="407f9ec8a17348dfba3b9450a16639d3">a16639d3</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d07e6dbf15664b99b37b0d2544f24211">44f24211</code>
</td>
<td>N/A</td>
<td>Magento 2 - Unrestricted file upload - 2</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>     
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="26ef21cb197b44fc8a98b7cebf170a17">bf170a17</code>
</td>
<td>N/A</td>
<td>Apache ActiveMQ - Remote Code Execution - CVE:CVE-2026-34197</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7f7bc3d28a8e43bf97bd15d68c2ac1a7">8c2ac1a7</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Sleep Function" (ID:{" "}
				<code class="nb-rule-id" title="2c333735f7b24566b17cb64ef77e8d54">f77e8d54</code>)
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3872e5638bdf4bf0943a80394dacaeb8">4dacaeb8</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>   
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bebce8fadfa94ccab09eb74fed4c9ece">ed4c9ece</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7a40eed5a8654a50a2598a821dfa64df">1dfa64df</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - uri</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="15c6b2ce033949b2a1a9f9454c62e2e7">4c62e2e7</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - header</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fc9d800b7a724181af8d5650aab28ea1">aab28ea1</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - body</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Probing" (ID: <code class="nb-rule-id" title="2c20b5e8684043f48620ff77b4026c88">b4026c88</code>)
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="945c5aa9f45141dd872d7ec920999be0">20999be0</code>
</td>
<td>N/A</td>
<td>SQLi - Probing 2 </td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule had duplicate detection logic and has been deprecated.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f1771273700342758e73cf16d7aa0008">d7aa0008</code>
</td>
<td>N/A</td>
<td>SQLi - UNION in MSSQL - Body</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule has been renamed to differentiate from "SQLi - UNION in MSSQL" (ID: <code class="nb-rule-id" title="ef7db598c7654c729d9db56fee5e35fd">ee5e35fd</code>) and contains updated rule logic.
</td>
</tr> 
<tr> 
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3ffd242b4ba242ca965022d3a67d8561">a67d8561</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 3</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule had duplicate detection logic and has been deprecated.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5e69d599ad634c81abe36a5f0af34bba">0af34bba</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Embed Tag  - URI</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2635275641bf44d4bad6a2e170282f38">70282f38</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Embed Tag - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b3d033ea9f364574b0a2ec4223f4d718">23f4d718</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - IFrame Tag - Src and Srcdoc Attributes - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="76c37816ef5c4997ab2080a36978def1">6978def1</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Link Tag - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7d6757e8a28f4853a72b4ce6ebd81645">ebd81645</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Link Tag - URI</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>           
</tbody>
</table>


<h2 id="waf-release-2026-04-15"><a href="/changelog/post/2026-04-15-waf-release/">WAF Release - 2026-04-15</a></h2>
<p><em>2026-04-15</em></p>
<p>This week's release introduces a new detection for a critical Remote Code Execution (RCE) vulnerability in Mesop (CVE-2026-33057), alongside protections for high-impact vulnerabilities in Cisco Secure Firewall Management Center (CVE-2026-20079) and FortiClient EMS (CVE-2026-21643). Additionally, this release includes an update to our existing React Server DoS coverage to address recently identified resource exhaustion vectors (CVE-2026-23869).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Cisco Secure FMC (CVE-2026-20079): A vulnerability in the web-based management interface of Cisco Secure Firewall Management Center (FMC) that allows an unauthenticated, remote attacker to execute arbitrary commands or bypass security filters.</p>
</li>
<li>
<p>FortiClient EMS (CVE-2026-21643): A critical vulnerability in the FortiClient EMS permitting unauthorized access or administrative configuration manipulation via crafted HTTP requests.</p>
</li>
<li>
<p>Mesop (CVE-2026-33057): A vulnerability in the Mesop Python-based UI framework where unauthenticated attackers can execute arbitrary code by sending specially crafted, Base64-encoded payloads in the request body.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, gain administrative control over network management infrastructure, or trigger server-side resource exhaustion. Administrators are strongly encouraged to apply official vendor updates.</p>
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
        <code class="nb-rule-id" title="7767165cda1841b8b6e5abb7aef9415b">aef9415b</code>
</td>
<td>N/A</td>
<td>Cisco Secure FMC - RCE via upgradeReadinessCall - CVE:CVE-2026-20079</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3dd0b2b6f45c4bc08e49bf27ee7be621">ee7be621</code>
</td>
<td>N/A</td>
<td>FortiClient EMS - Pre-Auth SQL Injection - CVE:CVE-2026-21643</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>   
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="0e3a6828906c4b24bad318a9c953a72b">c953a72b</code>
</td>
<td>N/A</td>
<td>Mesop - Remote Code Execution - Base64 Payload - CVE:CVE-2026-33057</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d95aa5410d1b4e98bf7a59d150c08f6f">50c08f6f</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 1 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule has been merged into the original rule "React Server - DOS - CVE:CVE-2026-23864 - 1" (ID: <code class="nb-rule-id" title="aaede80b4d414dc89c443cea61680354">61680354</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7d6757e8a28f4853a72b4ce6ebd81645">ebd81645</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Link Tag - URI (beta)</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5e69d599ad634c81abe36a5f0af34bba">0af34bba</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Embed Tag  - URI (beta)</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="email-obfuscation-decode-script-is-now-non-render-blocking"><a href="/changelog/post/2026-04-14-email-obfuscation-defer/">Email obfuscation decode script is now non-render-blocking</a></h2>
<p><em>2026-04-14</em></p>
<p>The decode script injected by <a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Address Obfuscation</a> now loads with the <code>defer</code> attribute. This means the script no longer blocks page rendering. It downloads in parallel with HTML parsing and executes after the document is fully parsed, before the <code>DOMContentLoaded</code> event.</p>
<p>This improves page loading performance, contributing to better Core Web Vitals, for all zones with Email Address Obfuscation on. No action is required.</p>
<p>If you have custom JavaScript that depends on email addresses being decoded at a specific point during page load, note that the decode script now executes after HTML parsing completes rather than inline during parsing.</p>


<h2 id="waf-release-2026-04-07"><a href="/changelog/post/2026-04-07-waf-release/">WAF Release - 2026-04-07</a></h2>
<p><em>2026-04-07</em></p>
<p>This week's release introduces new detections for a critical Remote Code Execution (RCE) vulnerability in MCP Server (CVE-2026-23744), alongside targeted protection for an authentication bypass vulnerability in SolarWinds products (CVE-2025-40552). Additionally, this release includes a new generic detection rule designed to identify and block Cross-Site Scripting (XSS) injection attempts leveraging &quot;OnEvent&quot; handlers within HTTP cookies.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>MCP Server (CVE-2026-23744): A vulnerability in the Model Context Protocol (MCP) server implementation where malformed input payloads can trigger a memory corruption state, allowing for arbitrary code execution.</p>
</li>
<li>
<p>SolarWinds (CVE-2025-40552): A critical flaw in the authentication module allows unauthenticated attackers to bypass security filters and gain unauthorized access to the management console due to improper identity token validation.</p>
</li>
<li>
<p>XSS OnEvents Cookies: This generic rule identifies malicious event handlers (such as onload or onerror) embedded within HTTP cookie values.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of the MCP Server and SolarWinds vulnerabilities could allow unauthenticated attackers to execute arbitrary code or gain administrative control, leading to a full system takeover. Additionally, the new generic XSS detection prevents attackers from leveraging browser event handlers in cookies to hijack user sessions or execute malicious scripts.</p>
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
				<code class="nb-rule-id" title="73ae1cf103da4bacaa2e1a610aa410af">0aa410af</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a88a85b0cc5a4bc2abead6289131ec2f">9131ec2f</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - Header</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="28518cdc40544979bbd86720551eb9e5">551eb9e5</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1177993d53a1467997002b44d46229eb">d46229eb</code>
</td>
<td>N/A</td>
<td>MCP Server - Remote Code Execution - CVE:CVE-2026-23744</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3d43cdfbc3c14584942f8bc4a864b9c2">a864b9c2</code>
</td>
<td>N/A</td>
<td>XSS - OnEvents - Cookies</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c9dbce2c1da94b24916e37559712a863">9712a863</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="64d812e6d5844d7c9d7a44a440732d48">40732d48</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="50de9369ef7c45928a5dfb34e68a99b5">e68a99b5</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="765ffb5c67b94c9589106c843e8143d2">3e8143d2</code>
</td>
<td>N/A</td>
<td>SQLi - LIKE 3 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5c3dbd4f115e47c781491fcd70e7fb97">70e7fb97</code>
</td>
<td>N/A</td>
<td>SQLi - LIKE 3 - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89fa6027a0334949b1cb2e654c538bd9">4c538bd9</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 2 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="05946b3458364f1b9d4819d561c439c9">61c439c9</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 2 - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b2fe5c2a39df4609b6d39908cf33ea10">cf33ea10</code>
</td>
<td>N/A</td>
<td>SolarWinds - Auth Bypass - CVE:CVE-2025-40552</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-03-30"><a href="/changelog/post/2026-03-30-waf-release/">WAF Release - 2026-03-30</a></h2>
<p><em>2026-03-30</em></p>
<p>This week's release introduces new detections for a critical authentication bypass vulnerability in Fortinet products (CVE-2025-59718), alongside three new generic detection rules designed to identify and block HTTP Parameter Pollution attempts. Additionally, this release includes targeted protection for a high-impact unrestricted file upload vulnerability in Magento and Adobe Commerce.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2025-59718: An improper cryptographic signature verification vulnerability in Fortinet FortiOS, FortiProxy, and FortiSwitchManager. This may allow an unauthenticated attacker to bypass the FortiCloud SSO login authentication using a maliciously crafted SAML message, if that feature is enabled on the device.</p>
</li>
<li>
<p>Magento 2 - Unrestricted File Upload: A critical flaw in Magento and Adobe Commerce allows unauthenticated attackers to bypass security checks and upload malicious files to the server, potentially leading to Remote Code Execution (RCE).</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of the Fortinet and Magento vulnerabilities could allow unauthenticated attackers to gain administrative control or deploy webshells, leading to complete server compromise and data theft.</p>
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
        <code class="nb-rule-id" title="4f7d513cea424c2a853881982f7f95e9">2f7f95e9</code>
</td>
<td>N/A</td>
<td>Generic Rules - Parameter Pollution - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="60d023f3be414d379428add3319731a4">319731a4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Parameter Pollution - Header - Form</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="2dde02d792ad41ec8fd65c2bdef262dd">def262dd</code>
</td>
<td>N/A</td>
<td>Generic Rules - Parameter Pollution - URI</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab8a96ed13034d56a81a79e570a36147">70a36147</code>
</td>
<td>N/A</td>
<td>Magento 2 - Unrestricted file upload</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="0a13a38dd81c44688950444e2ffcca9f">2ffcca9f</code>
</td>
<td>N/A</td>
<td>Fortinet FortiCloud SSO - Authentication Bypass - CVE:CVE-2025-59718</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>    
</tbody>    
</table>


<h2 id="waf-release-2026-03-23"><a href="/changelog/post/2026-03-23-waf-release/">WAF Release - 2026-03-23</a></h2>
<p><em>2026-03-23</em></p>
<p>This week's release focuses on new improvements to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
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
        <code class="nb-rule-id" title="54ad0465c30d4cd2ac7a707197321c6c">97321c6c</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - URI Vector</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b31c34a7b29b4aaf9be6883d1eb7a999">1eb7a999</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - Header Vector</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="155bb67d1061479e995a38510677175f">0677175f</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - Body Vector</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="55fb1c76f0304f6a9d935d03479da68f">479da68f</code>
</td>
<td>N/A</td>
<td>PHP, vBulletin, jQuery File Upload - Code Injection, Dangerous File Upload - CVE:CVE-2018-9206, CVE:CVE-2019-17132 (beta)</td>
<td>Log</td>
<td>Block</td>
<td>This rule has been merged into the original rule "PHP, vBulletin, jQuery File Upload - Code Injection, Dangerous File Upload - CVE:CVE-2018-9206, CVE:CVE-2019-17132" (ID: <code class="nb-rule-id" title="0f2da91cec674eb58006929e824b817c">824b817c</code>)</td>
</tr>
</tbody>    
</table>


<h2 id="waf-release-2026-03-12-emergency"><a href="/changelog/post/2026-03-12-emergency-waf-release/">WAF Release - 2026-03-12 - Emergency</a></h2>
<p><em>2026-03-12</em></p>
<p>This week's release introduces new detections for vulnerabilities in Ivanti Endpoint Manager Mobile (CVE-2026-1281 and CVE-2026-1340), alongside a new generic detection rule designed to identify and block Cross-Site Scripting (XSS) injection attempts within the <code>Content-Security-Policy</code> (CSP) HTTP request header.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-1281 &amp; CVE-2026-1340: Ivanti Endpoint Manager Mobile processes HTTP requests through Apache RevwriteMap directives that pass user-controlled input to Bash scripts (<code>/mi/bin/map-appstore-url</code> and <code>/mi/bin/map-aft-store-url</code>). Bash scripts do not sanitize user input and are vulnerable to shell arithmetic expansion thereby allowing attackers to achieve unauthenticated remote code execution.</li>
<li>Generic XSS in CSP Header: This rule identifies malicious payloads embedded within the request's <code>Content-Security-Policy</code> header. It specifically targets scenarios where web frameworks or applications trust and extract values directly from the CSP header in the incoming request without sufficient validation. Attackers can provide crafted header values to inject scripts or malicious directives that are subsequently processed by the server.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of Ivanti EPMM vulnerability allows unauthenticated remote code execution and generic XSS in CSP header allows attackers to inject malicious scripts during page rendering. In environments using server-side caching, this poisoned XSS content can subsequently be cached and automatically served to all visitors.</p>
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
				<code class="nb-rule-id" title="5ae86a9bda0c41dbb905132f796ea2f6">796ea2f6</code>
</td>
<td>N/A</td>
<td>Ivanti EPMM - Code Injection - CVE:CVE-2026-1281 CVE:CVE-2026-1340</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="35978af68e374a059e397bf5ee964a8c">ee964a8c</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:Content-Security-Policy</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-03-02"><a href="/changelog/post/2026-03-02-waf-release/">WAF Release - 2026-03-02</a></h2>
<p><em>2026-03-02</em></p>
<p>This week's release introduces new detections for vulnerabilities in SmarterTools SmarterMail (CVE-2025-52691 and CVE-2026-23760), alongside improvements to an existing Command Injection (nslookup) detection to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-52691: SmarterTools SmarterMail mail server is vulnerable to Arbitrary File Upload, allowing an unauthenticated attacker to upload files to any location on the mail server, potentially enabling remote code execution.</li>
<li>CVE-2026-23760: SmarterTools SmarterMail versions prior to build 9511 contain an authentication bypass vulnerability in the password reset API permitting unaunthenticated to reset system administrator accounts failing to verify existing password or reset token.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these SmarterMail vulnerabilities could lead to full system compromise or unauthorized administrative access to mail servers. Administrators are strongly encouraged to apply vendor patches without delay.</p>
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
				<code class="nb-rule-id" title="0f282f3c89614779966faf52966ec6b1">966ec6b1</code>
</td>
<td>N/A</td>
<td>SmarterMail - Arbitrary File Upload - CVE-2025-52691</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="35978af68e374a059e397bf5ee964a8c">ee964a8c</code>
</td>
<td>N/A</td>
<td>SmarterMail - Authentication Bypass - CVE-2026-23760</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4bb099bcd71141d4a35c1aa675b64d99">75b64d99</code>
</td>
<td>N/A</td>
<td>Command Injection - Nslookup - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Command Injection - Nslookup" (ID: <code class="nb-rule-id" title="f4a310393c564d50bd585601b090ba9a">b090ba9a</code>)</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-02-16"><a href="/changelog/post/2026-02-16-waf-release/">WAF Release - 2026-02-16</a></h2>
<p><em>2026-02-16</em></p>
<p>This week’s release introduces new detections for CVE-2025-68645 and CVE-2025-31125.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-68645: A Local File Inclusion (LFI) vulnerability in the Webmail Classic UI of Zimbra Collaboration Suite (ZCS) 10.0 and 10.1 allows unauthenticated remote attackers to craft requests to the <code>/h/rest</code> endpoint, improperly influence internal dispatching, and include arbitrary files from the WebRoot directory.</li>
<li>CVE-2025-31125: Vite, the JavaScript frontend tooling framework, exposes content of non-allowed files via <code>?inline&amp;import</code> when its development server is network-exposed, enabling unauthorized attackers to read arbitrary files and potentially leak sensitive information.</li>
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
				<code class="nb-rule-id" title="695d76ff756844d384cab548833761f7">833761f7</code>
</td>
<td>N/A</td>
<td>Zimbra - Local File Inclusion - CVE:CVE-2025-68645</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="38fff9f3deba46a2abc10a8f950ed8c8">950ed8c8</code>
</td>
<td>N/A</td>
<td>Vite - WASM Import Path Traversal - CVE:CVE-2025-31125</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-02-10"><a href="/changelog/post/2026-02-10-waf-release/">WAF Release - 2026-02-10</a></h2>
<p><em>2026-02-10</em></p>
<p>This week’s release changes the rule action from BLOCK to Disabled for Anomaly:Header:User-Agent - Fake Google Bot.</p>
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
        <code class="nb-rule-id" title="ce11be543594412bb4bb92516aa0bef8">6aa0bef8</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:User-Agent - Fake Google Bot</td>
<td>Enabled</td>
<td>Disabled</td>
<td>We are changing the action for this rule from BLOCK to Disabled</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-02-02"><a href="/changelog/post/2026-02-02-waf-release/">WAF Release - 2026-02-02</a></h2>
<p><em>2026-02-02</em></p>
<p>This week’s release introduces new detections for CVE-2025-64459 and CVE-2025-24893.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-64459: Django versions prior to 5.1.14, 5.2.8, and 4.2.26 are vulnerable to SQL injection via crafted dictionaries passed to QuerySet methods and the <code>Q()</code> class.</li>
<li>CVE-2025-24893: XWiki allows unauthenticated remote code execution through crafted requests to the SolrSearch endpoint, affecting the entire installation.</li>
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
        <code class="nb-rule-id" title="7a47683eacce4abd870ab2c630698ff3">30698ff3</code>
</td>
<td>N/A</td>
<td>XWiki - Remote Code Execution - CVE:CVE-2025-24893 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ad5c52f6ca334ef4a844e5e5da8ba7e6">da8ba7e6</code>
</td>
<td>N/A</td>
<td>Django SQLI - CVE:CVE-2025-64459</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8f0d5c98bd24460a9305a1558d667511">8d667511</code>
</td>
<td>N/A</td>
<td>NoSQL, MongoDB - SQLi - Comparison - 2</td>
<td>Block</td>
<td>Block</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-01-26"><a href="/changelog/post/2026-01-26-waf-release/">WAF Release - 2026-01-26</a></h2>
<p><em>2026-01-26</em></p>
<p>This week’s release introduces new detections for denial-of-service attempts targeting React CVE-2026-23864 (<a href="https://www.cve.org/CVERecord?id=CVE-2026-23864">https://www.cve.org/CVERecord?id=CVE-2026-23864</a>).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-23864 (<a href="https://www.cve.org/CVERecord?id=CVE-2026-23864">https://www.cve.org/CVERecord?id=CVE-2026-23864</a>) affects <code>react-server-dom-parcel</code>, <code>react-server-dom-turbopack</code>, and <code>react-server-dom-webpack</code> packages.</li>
<li>Attackers can send crafted HTTP requests to Server Function endpoints, causing server crashes, out-of-memory exceptions, or excessive CPU usage.</li>
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
        <code class="nb-rule-id" title="aaede80b4d414dc89c443cea61680354">61680354</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 1</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3e93c9faaafa447c83a525f2dcdffcf8">dcdffcf8</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="930020d567684f19b05fb35b349edbc6">349edbc6</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 3</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-01-20"><a href="/changelog/post/2026-01-20-waf-release/">WAF Release - 2026-01-20</a></h2>
<p><em>2026-01-20</em></p>
<p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against SQL injection.</li>
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
        <code class="nb-rule-id" title="a291bd530fa346d18cc1ce5a68d90c8f">68d90c8f</code>
</td>
<td>N/A</td>
<td>SQLi - Comment - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Comment" (ID: <code class="nb-rule-id" title="42c424998d2a42c9808ab49c6d8d8fe4">6d8d8fe4</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="da289f9e692e4f5397d915fbfaa045cf">faa045cf</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Comparison" (ID: <code class="nb-rule-id" title="8166da327a614849bfa29317e7907480">e7907480</code>)</td>
</tr>
</tbody>    
</table>


<h2 id="waf-release-2026-01-15"><a href="/changelog/post/2026-01-15-waf-release/">WAF Release - 2026-01-15</a></h2>
<p><em>2026-01-15</em></p>
<p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
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
        <code class="nb-rule-id" title="eb3f44c07266448b9fa54ee7ad7dad3e">ad7dad3e</code>
</td>
<td>N/A</td>
<td>SQLi - String Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - String Function" (ID: <code class="nb-rule-id" title="63e03eecddfc4b3fb0cad587d32b798c">d32b798c</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="adf076af09b2484ca9e7881f9e553ad3">9e553ad3</code>
</td>
<td>N/A</td>
<td>SQLi - Sub Query - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "SQLi - Sub Query" (ID: <code class="nb-rule-id" title="6ec5ecf52c094330aff99a38743e66b1">743e66b1</code>)</td>
</tr>
</tbody>    
</table>


<h2 id="waf-release-2026-01-12"><a href="/changelog/post/2026-01-12-waf-release/">WAF Release - 2026-01-12</a></h2>
<p><em>2026-01-12</em></p>
<p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
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


<h2 id="waf-release-2025-12-18"><a href="/changelog/post/2025-12-18-waf-release/">WAF Release - 2025-12-18</a></h2>
<p><em>2025-12-18</em></p>
<p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
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
        <code class="nb-rule-id" title="6429f7386b1546cf9dfce631be5ec20c">be5ec20c</code>
</td>
<td>N/A</td>
<td>Atlassian Confluence - Code Injection - CVE:CVE-2021-26084 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Atlassian Confluence - Code Injection - CVE:CVE-2021-26084" (ID: <code class="nb-rule-id" title="e8c550810618437c953cf3a969e0b97a">69e0b97a</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9108ddb347b3497e9f9351640d9206e3">0d9206e3</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - Copy - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "PostgreSQL - SQLi - COPY" (ID: <code class="nb-rule-id" title="705a6b5569d5472596910e3ce7265a4e">e7265a4e</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cb687d73cc954092b58b90b00cd00ba7">0cd00ba7</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Body</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="bf30657ffa2a424cbf6570dbcd679ad4">cd679ad4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Header</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6df040f716194070a242967cfd181fb3">fd181fb3</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="39a4fdc37be948709fa7492e7a95bc3a">7a95bc3a</code>
</td>
<td>N/A</td>
<td>SQLi - Tautology - URI - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Tautology - URI" (ID: <code class="nb-rule-id" title="4c580ea1b5174183b7f5e940b3de2e0a">b3de2e0a</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="810e0ffe1dd84e67b159129b432ac90d">432ac90d</code>
</td>
<td>N/A</td>
<td>SQLi - WaitFor Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - WaitFor Function" (ID: <code class="nb-rule-id" title="b16fe708799441dea3049a99d5faba59">d5faba59</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="80690005fef342e0ad6bc9af596c741e">596c741e</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit 2 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - AND/OR Digit Operator Digit" (ID: <code class="nb-rule-id" title="98e7e08ae64247e2801ca4b388d80772">88d80772</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="eaf11ab80b0d491cbb7186f303b2f3fe">03b2f3fe</code>
</td>
<td>N/A</td>
<td>SQLi - Equation 2 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Equation" (ID: <code class="nb-rule-id" title="133c6f83cdf14509a4ca6b82a72a6b3a">a72a6b3a</code>)</td>
</tr>
</tbody>    
</table>


<h2 id="waf-release-2025-12-11-emergency"><a href="/changelog/post/2025-12-11-emergency-waf-release/">WAF Release - 2025-12-11 - Emergency</a></h2>
<p><em>2025-12-11</em></p>
<p>This emergency release introduces rules for CVE-2025-55183 and CVE-2025-55184, targeting server-side function exposure and resource-exhaustion patterns, respectively.</p>
<p><strong>Key Findings</strong></p>
<p>Added coverage for Leaking Server Functions (CVE-2025-55183) and React Function DoS detection (CVE-2025-55184).</p>
<p><strong>Impact</strong></p>
<p>These updates strengthen protection for server-function abuse techniques (CVE-2025-55183, CVE-2025-55184) that may expose internal logic or disrupt application availability.</p>
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
				<code class="nb-rule-id" title="17c5123f1ac049818765ebf2fefb4e9b">fefb4e9b</code>
</td>
<td>N/A</td>
<td>React - Leaking Server Functions - CVE:CVE-2025-55183</td>
<td>N/A</td>
<td>Block</td>
<td>This was labeled as Generic - Server Function Source Code Exposure.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="3114709a3c3b4e3685052c7b251e86aa">251e86aa</code>
</td>
<td>N/A</td>
<td>React - Leaking Server Functions - CVE:CVE-2025-55183</td>
<td>N/A</td>
<td>Block</td>
<td>This was labeled as Generic - Server Function Source Code Exposure.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2694f1610c0b471393b21aef102ec699">102ec699</code>
</td>
<td>N/A</td>
<td>React - DoS - CVE:CVE-2025-55184</td>
<td>N/A</td>
<td>Disabled</td>
<td>This was labeled as Generic – Server Function Resource Exhaustion.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-12-10-emergency"><a href="/changelog/post/2025-12-10-emergency-waf-release/">WAF Release - 2025-12-10 - Emergency</a></h2>
<p><em>2025-12-10</em></p>
<p>This additional week's emergency release introduces improvements to our existing rule for React – Remote Code Execution – CVE-2025-55182 - 2, along with two new generic detections covering server-side function exposure and resource-exhaustion patterns.</p>
<p><strong>Key Findings</strong></p>
<p>Enhanced detection logic for React – RCE – CVE-2025-55182, added Generic – Server Function Source Code Exposure, and added Generic – Server Function Resource Exhaustion.</p>
<p><strong>Impact</strong></p>
<p>These updates strengthen protection against React RCE exploitation attempts and broaden coverage for common server-function abuse techniques that may expose internal logic or disrupt application availability.</p>
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
				<code class="nb-rule-id" title="bc1aee59731c488ca8b5314615fce168">15fce168</code>
</td>
<td>N/A</td>
<td>React - Remote Code Execution - CVE:CVE-2025-55182 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="cbdd3f48396e4b7389d6efd174746aff">74746aff</code>
</td>
<td>N/A</td>
<td>React - Remote Code Execution - CVE:CVE-2025-55182 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="17c5123f1ac049818765ebf2fefb4e9b">fefb4e9b</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Source Code Exposure</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="3114709a3c3b4e3685052c7b251e86aa">251e86aa</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Source Code Exposure</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2694f1610c0b471393b21aef102ec699">102ec699</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Resource Exhaustion</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="increased-waf-payload-limit-for-all-plans"><a href="/changelog/post/2025-12-05-rcs-vuln/">Increased WAF payload limit for all plans</a></h2>
<p><em>2025-12-05</em></p>
<p>Cloudflare WAF now inspects request-payload size of up to 1 MB across all plans to enhance our detection capabilities for React RCE (CVE-2025-55182).</p>
<p><strong>Key Findings</strong></p>
<p>React payloads commonly have a default maximum size of 1 MB. Cloudflare WAF previously inspected up to 128 KB on Enterprise plans, with even lower limits on other plans.</p>
<p><strong>Update:</strong> We later reinstated the maximum request-payload size the Cloudflare WAF inspects. Refer to <a href="/changelog/2025-12-05-waf-max-payload-size-change/">Updating the WAF maximum payload values</a> for details.</p>


<h2 id="updating-the-waf-maximum-payload-values"><a href="/changelog/post/2025-12-05-waf-max-payload-size-change/">Updating the WAF maximum payload values</a></h2>
<p><em>2025-12-05</em></p>
<p>We are reinstating the maximum request-payload size the Cloudflare WAF inspects, with WAF on Enterprise zones inspecting up to 128 KB.</p>
<p><strong>Key Findings</strong></p>
<p>On <a href="/changelog/2025-12-05-rcs-vuln/">December 5, 2025</a>, we initially attempted to increase the maximum WAF payload limit to 1 MB across all plans. However, an automatic rollout for all customers proved impractical because the increase led to a surge in false positives for existing managed rules.</p>
<p>This issue was particularly notable within the Cloudflare Managed Ruleset and the Cloudflare OWASP Core Ruleset, impacting customer traffic.</p>
<p><strong>Impact</strong></p>
<p>Customers on paid plans can increase the limit to 1 MB for any of their zones by contacting Cloudflare Support. Free zones are already protected up to 1 MB and do not require any action.</p>


<h2 id="waf-release-2025-12-03-emergency"><a href="/changelog/post/2025-12-03-emergency-waf-release/">WAF Release - 2025-12-03 - Emergency</a></h2>
<p><em>2025-12-03</em></p>
<p>The WAF rule deployed yesterday to block unsafe deserialization-based RCE has been updated. The rule description now reads “React – RCE – CVE-2025-55182”, explicitly mapping to the recently disclosed React Server Components vulnerability. Detection logic remains unchanged.</p>
<p><strong>Key Findings</strong></p>
<p>Rule description updated to reference React – RCE – CVE-2025-55182 while retaining existing unsafe-deserialization detection.</p>
<p><strong>Impact</strong></p>
<p>Improved classification and traceability with no change to coverage against remote code execution attempts.</p>
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
				<code class="nb-rule-id" title="33aa8a8a948b48b28d40450c5fb92fba">5fb92fba</code>
</td>
<td>N/A</td>
<td>React - RCE - CVE:CVE-2025-55182</td>
<td>N/A</td>
<td>Block</td>
<td>Rule metadata description changed. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b5d06e34a814a889bee9a0699702280">99702280</code>
</td>
<td>N/A</td>
<td>React - RCE - CVE:CVE-2025-55182</td>
<td>N/A</td>
<td>Block</td>
<td>Rule metadata description changed. Detection unchanged.</td>
</tr>
</tbody>
</table>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/waf/">Previous</a><span>Page 2 of 5</span><a class="pagination-next" rel="next" href="/changelog/product/waf/3/">Next</a></nav>
