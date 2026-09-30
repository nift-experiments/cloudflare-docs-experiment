---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/application-security/3/
  description: '2026-05-07'
  full_title: Application security changelog - page 3 | Cloudflare Docs
  head_html: <title>Application security changelog - page 3 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-05-07"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/application-security/3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Application security changelog - page 3"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-05-07"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/application-security/3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/application-security/3/#page","headline":"Application security changelog - page 3 | Cloudflare Docs","description":"2026-05-07","url":"https://developers.cloudflare.com/changelog/product-group/application-security/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/application-security/3/
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


<h2 id="taxii-support-added-to-threat-events-api"><a href="/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/">TAXII support added to Threat Events API</a></h2>
<p><em>2026-05-06</em></p>
<p>The Cloudforce One Threat Events API now supports <a href="https://www.cloudflare.com/en-gb/learning/security/what-is-stix-and-taxii/"><strong>TAXII</strong></a> as an output format, enabling standardized, automated sharing of cyber threat intelligence with your existing security stack.</p>
<h4 id="2026-05-06-TAXII-support-for-threat-events-api-why-this-matters">Why this matters</h4>
<ul>
<li>You can now ingest Cloudforce One threat data directly into your SIEM, TIP or SOAR tools that prefer TAXII-formatted streams without needing custom translation scripts.</li>
<li>By supporting the TAXII format parameter in our API, security teams can automate the synchronization of indicator data, reducing the manual overhead of updating blocklists and detection rules.</li>
<li>This alignment with industry standards ensures that your threat data remains consistent across different security ecosystems and partner integrations.</li>
</ul>
<h4 id="2026-05-06-TAXII-support-for-threat-events-api-how-to-use-it">How to use it</h4>
<p>When calling the Threat Events API, you can now specify <code>taxii</code> in the <code>format</code> query parameter:</p>
<p><code>GET /accounts/{account_id}/cloudforce_one/threat_events?format=taxii</code></p>
<p>You can find the updated documentation in the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list#%28resource%29%20cloudforce_one.threat_events%20%3E%20%28method%29%20list%20%3E%20%28params%29%20default%20%3E%20%28param%29%20format%20%3E%20%28schema%29">Cloudflare API Reference</a>.</p>


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


<h2 id="unified-workspace-for-brand-protection"><a href="/changelog/post/2026-04-27-unified-workspace-brand-protection/">Unified workspace for Brand Protection</a></h2>
<p><em>2026-04-27</em></p>
<p>We have introduced a unified investigation workspace within Brand Protection to help analysts manage complex brand portfolios. Instead of jumping between individual queries, you can now consolidate your workflow into a single, cohesive view.</p>
<h4 id="2026-04-27-unified-workspace-brand-protection-what-s-new">What's new</h4>
<ul>
<li>You can now elect multiple saved queries from your dashboard to generate a consolidated &quot;Combined Matches&quot; view. This allows you to triage results from different brand queries in one unified table</li>
<li>You can open query extended views in distinct tabs within the Brand Protection dashboard. This enables you to maintain multiple investigation contexts simultaneously and switch between them without losing your place.</li>
<li>You can reset your workspace using the new &quot;Clear Selection&quot; action, making it easier to pivot between different investigation sets.</li>
</ul>
<h4 id="2026-04-27-unified-workspace-brand-protection-key-benefits">Key benefits</h4>
<ul>
<li>Eliminate fragmented workflows by viewing all matches across different query buckets in a single table, reducing the need to click through dozens of individual query pages</li>
<li>Correlate related campaigns by seeing similar domains or infrastructure patterns that appear across multiple saved queries</li>
</ul>
<p>Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


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


<h2 id="archive-and-audit-security-action-items"><a href="/changelog/post/2026-04-27-archive-and-audit-security-action-items/">Archive and audit security action items</a></h2>
<p><em>2026-04-20</em></p>
<h4 id="2026-04-27-archive-and-audit-security-action-items-archive-and-audit-security-action-items">Archive and audit security action items</h4>
<p>Introducing enhanced archiving capabilities for security action items within the Security Overview dashboard. This update allows security teams to maintain a cleaner workspace by removing resolved, accepted, or irrelevant items from their active list while maintaining a clear paper trail for compliance.</p>
<hr />
<h4 id="2026-04-27-archive-and-audit-security-action-items-why-this-matters">Why this matters</h4>
<p>Managing a high volume of security insights can be overwhelming. Previously, users lacked a structured way to dismiss items without losing the context of why they were ignored.</p>
<p>With these new archiving options—<strong>False Positive</strong>, <strong>Accept Risk</strong>, and <strong>Other</strong>—you can now suppress items indefinitely with required rationale text for risk-based decisions. This ensures that your team remains focused on critical, actionable vulnerabilities while preserving institutional knowledge for audits.</p>
<h4 id="2026-04-27-archive-and-audit-security-action-items-key-features">Key features</h4>
<ul>
<li><strong>Structured Archiving:</strong> Choose from specific categories to define why an action item is being moved.</li>
<li><strong>Required Rationale:</strong> For &quot;Accept Risk&quot; and &quot;Other&quot; categories, users must provide documentation, ensuring accountability for security decisions.</li>
<li><strong>Audit Log Transparency:</strong> New API endpoints allow you to programmatically retrieve the history of status changes and rationale for any insight at the account or zone level.</li>
<li><strong>Reversible Actions:</strong> Any archived item can be moved back to the active list at any time if the security context changes.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17753.md")</aside>
<hr />
<h4 id="2026-04-27-archive-and-audit-security-action-items-example-retrieve-audit-logs-via-api">Example: Retrieve audit logs via API</h4>
<p>To review the history and rationale of a specific archived issue at the account level, you can use the following API command:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){account_id}/insights/{insight_id}/audit-log&quot; \&#10;     &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot;&#10;</code></pre>


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


<h2 id="real-time-alerts-and-daily-digests-for-threat-events"><a href="/changelog/post/2026-04-08-threat-events-notification/">Real-time alerts and daily digests for Threat Events</a></h2>
<p><em>2026-04-08</em></p>
<p>You can now automate your threat monitoring by setting up custom alerts in your saved views. Instead of manually checking the dashboard for updates, you can subscribe to notifications that trigger whenever new data matches your specific filter sets, like new activity associated to a particular threat actor or spikes in activity within your industry.</p>
<h4 id="2026-04-08-threat-events-notification-stay-ahead-of-emerging-threats">Stay ahead of emerging threats</h4>
<p>By linking your saved views to the Cloudflare Notifications Center, you can ensure the right information reaches your team at the right time.</p>
<ul>
<li>
<p><strong>Immediate Alerts</strong>: receive real-time notifications the moment a critical event is detected that matches your saved criteria. This is essential for high-priority monitoring, such as tracking active campaigns from specific APT groups.</p>
</li>
<li>
<p><strong>Daily Digests</strong>: opt for a summarized report delivered once a day. This is ideal for maintaining situational awareness of broader trends, like regional activity shifts or industry-wide threat landscapes, without cluttering your inbox.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/threat-events-notifications.png" alt="Threat Events notifications" /></p>
<h4 id="2026-04-08-threat-events-notification-how-to-get-started">How to get started</h4>
<p>To set up an alert, go to <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Threat Events</strong>. From there:</p>
<ol>
<li>Choose your datasets and apply your desired filters and select <strong>Save View</strong> (or select an existing one).</li>
<li>Open the <strong>Manage Saved Views</strong> menu.</li>
<li>Select <strong>Add Alert</strong> next to your chosen view to configure your notification preferences in the Cloudflare dashboard.</li>
</ol>
<p>For more technical details on configuring notifications, refer to the <a href="/security-center/cloudforce-one/">Threat Events documentation</a>.</p>


<h2 id="manage-mtls-and-byo-ca-certificates-from-the-cloudflare-dashboard"><a href="/changelog/post/2026-04-07-mtls-byoca-dashboard/">Manage mTLS and BYO CA certificates from the Cloudflare dashboard</a></h2>
<p><em>2026-04-07</em></p>
<p>You can now manage mutual TLS (mTLS) and Bring Your Own Certificate Authority
(BYO CA) configurations directly from the Cloudflare dashboard — no API required.</p>
<p>Previously, these advanced workflows required the Cloudflare API. The following
are now available in the dashboard:</p>
<ul>
<li><strong>AOP certificate management</strong> — Upload and manage your own
certificate authorities for <a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls (AOP)</a>
directly from the dashboard.</li>
<li><strong>BYO Client mTLS certificate management</strong> — Upload and manage your own CA
certificates for <a href="/ssl/client-certificates/byo-ca/">client mTLS enforcement</a>
without needing API access.</li>
<li><strong>CDN hostname to client mTLS certificate mapping</strong> — Associate client mTLS
certificates with specific hostnames directly from the dashboard.</li>
</ul>


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


<h2 id="new-quic-rtt-and-delivery-rate-fields"><a href="/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/">New QUIC RTT and delivery rate fields</a></h2>
<p><em>2026-04-01</em></p>
<p>Two new fields are now available in rule expressions that surface Layer 4 transport telemetry from the client connection. Together with the existing <a href="/ruleset-engine/rules-language/fields/reference/"><code>cf.timings.client_tcp_rtt_msec</code></a> field, these fields give you a complete picture of connection quality for both TCP and QUIC traffic — enabling transport-aware rules without requiring any client-side changes.</p>
<p>Previously, QUIC RTT and delivery rate data was only available via the <code>Server-Timing: cfL4</code> response header. These new fields make the same data available directly in rule expressions, so you can use them in Transform Rules, WAF Custom Rules, and other phases that support dynamic fields.</p>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.client_quic_rtt_msec</code></td>
<td>Integer</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only populated for QUIC (HTTP/3) connections. Returns <code>0</code> for TCP connections.</td>
</tr>
<tr>
<td><code>cf.edge.l4.delivery_rate</code></td>
<td>Integer</td>
<td>The most recent data delivery rate estimate for the client connection, in bytes per second. Returns <code>0</code> when L4 statistics are not available for the request.</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-route-slow-connections-to-a-lightweight-origin">Example: Route slow connections to a lightweight origin</h4>
<p>Use a request header transform rule to tag requests from high-latency connections, so your origin can serve a lighter page variant:</p>
<p><strong>Rule expression:</strong></p>
<pre tabindex="0"><code class="language-txt">cf.timings.client_tcp_rtt_msec &gt; 200 or cf.timings.client_quic_rtt_msec &gt; 200&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>X-High-Latency</code></td>
<td><code>true</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-quic-rtt-delivery-rate-fields-example-match-low-bandwidth-connections">Example: Match low-bandwidth connections</h4>
<pre tabindex="0"><code class="language-txt">cf.edge.l4.delivery_rate &gt; 0 and cf.edge.l4.delivery_rate &lt; 100000&#10;</code></pre>
<p>For more information, refer to <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a> and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


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


<h2 id="new-mtls-certificate-fields-for-transform-rules"><a href="/changelog/post/2026-03-25-rfc9440-mtls-fields/">New mTLS certificate fields for Transform Rules</a></h2>
<p><em>2026-03-25</em></p>
<p>Cloudflare now exposes four new fields in the Transform Rules phase that encode client certificate data in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format. Previously, forwarding client certificate information to your origin required custom parsing of PEM-encoded fields or non-standard HTTP header formats. These new fields produce output in the standardized <code>Client-Cert</code> and <code>Client-Cert-Chain</code> header format defined by RFC 9440, so your origin can consume them directly without any additional decoding logic.</p>
<p>Each certificate is DER-encoded, Base64-encoded, and wrapped in colons. For example, <code>:MIIDsT...Vw==:</code>. A chain of intermediates is expressed as a comma-separated list of such values.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format. Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted. In practice this will almost always be <code>false</code>.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediate certificates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>cf.tls_client_auth.cert_chain_rfc9440_too_large</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted.</td>
</tr>
</tbody>
</table>
<p>The chain encoding follows the same ordering as the TLS handshake: the certificate closest to the leaf appears first, working up toward the trust anchor. The root certificate is not included.</p>
<h4 id="2026-03-25-rfc9440-mtls-fields-example-forwarding-client-certificate-headers-to-your-origin-server">Example: Forwarding client certificate headers to your origin server</h4>
<p>Add a request header transform rule to set the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> headers on requests forwarded to your origin server. For example, to forward headers for verified, non-revoked certificates:</p>
<p><strong>Rule expression:</strong></p>
<pre tabindex="0"><code class="language-txt">cf.tls_client_auth.cert_verified and not cf.tls_client_auth.cert_revoked&#10;</code></pre>
<p><strong>Header modifications:</strong></p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Header name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Set</td>
<td><code>Client-Cert</code></td>
<td><code>cf.tls_client_auth.cert_rfc9440</code></td>
</tr>
<tr>
<td>Set</td>
<td><code>Client-Cert-Chain</code></td>
<td><code>cf.tls_client_auth.cert_chain_rfc9440</code></td>
</tr>
</tbody>
</table>
<p>To get the most out of these fields, upload your client CA certificate to Cloudflare so that Cloudflare validates the client certificate at the edge and populates <code>cf.tls_client_auth.cert_verified</code> and <code>cf.tls_client_auth.cert_revoked</code>.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-03-25-rfc9440-mtls-fields-prevent-header-injection">Prevent header injection</h4>
@markup("md", "content/.markup/bodies/17749.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>, <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>, and the <a href="/ruleset-engine/rules-language/fields/reference/">fields reference</a>.</p>


<h2 id="web-assets-fields-now-available-in-graphql-analytics-api"><a href="/changelog/post/2026-03-23-web-assets-graphql-fields/">Web Assets fields now available in GraphQL Analytics API</a></h2>
<p><em>2026-03-23</em></p>
<p>Two new fields are now available in the <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code> <a href="/analytics/graphql-api/">GraphQL Analytics API</a> datasets:</p>
<ul>
<li><code>webAssetsOperationId</code> — the ID of the <a href="/api-shield/management-and-monitoring/">saved endpoint</a> that matched the incoming request.</li>
<li><code>webAssetsLabelsManaged</code> — the <a href="/api-shield/management-and-monitoring/endpoint-labels/#managed-labels">managed labels</a> mapped to the matched operation at the time of the request (for example, <code>cf-llm</code>, <code>cf-log-in</code>). At most 10 labels are returned per request.</li>
</ul>
<p>Both fields are empty when no operation matched. <code>webAssetsLabelsManaged</code> is also empty when no managed labels are assigned to the matched operation.</p>
<p>These fields allow you to determine, per request, which Web Assets operation was matched and which managed labels were active. This is useful for troubleshooting downstream security detection verdicts — for example, understanding why <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> did or did not flag a request.</p>
<p>Refer to <a href="/api-shield/management-and-monitoring/endpoint-labels/#analytics">Endpoint labeling service</a> for GraphQL query examples.</p>


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


<h2 id="stream-logs-from-multiple-replicas-of-cloudflare-tunnel-simultaneously"><a href="/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/">Stream logs from multiple replicas of Cloudflare Tunnel simultaneously</a></h2>
<p><em>2026-03-20</em></p>
<p>In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> of that tunnel and supports streaming logs from multiple replicas at once.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-multiconn.gif" alt="View replicas and stream logs from multiple connectors" /></p>
<p>Previously, you could only stream logs from one replica at a time. With this update:</p>
<ul>
<li><strong>Replicas on the tunnel overview</strong> — All active replicas for the selected tunnel now appear on that tunnel's overview page under <strong>Connectors</strong>. Select any replica to stream its logs.</li>
<li><strong>Multi-connector log streaming</strong> — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Networks</strong> &gt; <strong>Connectors</strong> &gt; <strong>Cloudflare Tunnels</strong>. Select <strong>View logs</strong> next to the tunnel you want to monitor.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/">Deploy replicas</a>.</p>


<h2 id="manage-cloudflare-tunnels-with-wrangler"><a href="/changelog/post/2026-03-19-wrangler-tunnel-commands/">Manage Cloudflare Tunnels with Wrangler</a></h2>
<p><em>2026-03-19</em></p>
<p>You can now manage <a href="/tunnel/">Cloudflare Tunnels</a> directly from <a href="/workers/wrangler/">Wrangler</a>, the CLI for the Cloudflare Developer Platform. The new <a href="/workers/wrangler/commands/tunnel/"><code>wrangler tunnel</code></a> commands let you create, run, and manage tunnels without leaving your terminal.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/wrangler-tunnel.gif" alt="Wrangler tunnel commands demo" /></p>
<p>Available commands:</p>
<ul>
<li><code>wrangler tunnel create</code> — Create a new remotely managed tunnel.</li>
<li><code>wrangler tunnel list</code> — List all tunnels in your account.</li>
<li><code>wrangler tunnel info</code> — Display details about a specific tunnel.</li>
<li><code>wrangler tunnel delete</code> — Delete a tunnel.</li>
<li><code>wrangler tunnel run</code> — Run a tunnel using the cloudflared daemon.</li>
<li><code>wrangler tunnel quick-start</code> — Start a free, temporary tunnel without an account using <a href="/tunnel/get-started/#quick-tunnels-development">Quick Tunnels</a>.</li>
</ul>
<p>Wrangler handles downloading and managing the <a href="/tunnel/downloads/">cloudflared</a> binary automatically. On first use, you will be prompted to download <code>cloudflared</code> to a local cache directory.</p>
<p>These commands are currently experimental and may change without notice.</p>
<p>To get started, refer to the <a href="/workers/wrangler/commands/tunnel/">Wrangler tunnel commands documentation</a>.</p>


<h2 id="worker-execution-timing-field-now-available-in-rules"><a href="/changelog/post/2026-03-18-worker-timing-field/">Worker execution timing field now available in Rules</a></h2>
<p><em>2026-03-18</em></p>
<p>The <code>cf.timings.worker_msec</code> field is now available in the Ruleset Engine. This field reports the wall-clock time that a Cloudflare Worker spent handling a request, measured in milliseconds.</p>
<p>You can use this field to identify slow Worker executions, detect performance regressions, or build rules that respond differently based on Worker processing time, such as logging requests that exceed a latency threshold.</p>
<h4 id="2026-03-18-worker-timing-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.worker_msec</code></td>
<td>Integer</td>
<td>The time spent executing a Cloudflare Worker in milliseconds. Returns <code>0</code> if no Worker was invoked.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre tabindex="0"><code>cf.timings.worker_msec &gt; 500&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/">Fields reference</a>.</p>


<h2 id="real-time-logo-match-preview"><a href="/changelog/post/2026-03-18-brand-protection-logo-match-preview/">Real-time logo match preview</a></h2>
<p><em>2026-03-18</em></p>
<p>We are introducing <strong>Logo Match Preview</strong>, bringing the same pre-save visibility to visual assets that was previously only available for string-based queries. This update allows you to fine-tune your brand detection strategy before committing to a live monitor.</p>
<h4 id="2026-03-18-brand-protection-logo-match-preview-what-s-new">What’s new:</h4>
<ul>
<li>Upload your brand logo and immediately see a sample of potential matches from recently detected sites before finalizing the query</li>
<li>Adjust your similarity score (from 75% to 100%) and watch the results refresh in real-time to find the balance between broad detection and noise reduction</li>
<li>Review the specific logos triggered by your current settings to ensure your query is capturing the right level of brand infringement</li>
</ul>
<p>If you are ready to test your brand assets, go to the <a href="https://developers.cloudflare.com/security-center/brand-protection/">Brand Protection dashboard</a> to try the new preview tool.</p>


<h2 id="new-security-overview-ui"><a href="/changelog/post/2026-03-17-new-security-overview-ui/">New Security Overview UI</a></h2>
<p><em>2026-03-17</em></p>
<p>The Security Overview has been updated to provide Application Security customers with more actionable insights and a clearer view of their security posture.</p>
<p>Key improvements include:</p>
<ul>
<li><strong>Criticality for all Insights</strong>: Every insight now includes a criticality rating, allowing you to prioritize the most impactful security action items first.</li>
<li><strong>Detection Tools Section</strong>: A new section displays the security detection tools available to you, indicating which are currently enabled and which can be activated to strengthen your defenses.</li>
<li><strong>Industry Peer Comparison</strong> (Enterprise customers): A new module from Security Reports benchmarks your security posture against industry peers, highlighting relative strengths and areas for improvement.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-overview/overview-ui.png" alt="New Security Overview UI" /></p>
<p>For more information, refer to <a href="/security/overview/">Security Overview</a>.</p>


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


<h2 id="new-vulnerability-scanner-for-api-shield"><a href="/changelog/post/2026-03-09-vulnerability-scanner/">New Vulnerability Scanner for API Shield</a></h2>
<p><em>2026-03-09</em></p>
<p>Introducing Cloudflare's Web and API Vulnerability Scanner (Open Beta)</p>
<p>Cloudflare is launching the <a href="https://blog.cloudflare.com/vulnerability-scanner">Open Beta of the <strong>Web and API Vulnerability Scanner</strong></a> for all <a href="/api-shield/">API Shield</a> customers. This new, stateful Dynamic Application Security Testing (DAST) platform helps teams proactively find logic flaws in their APIs.</p>
<p>The initial release focuses on detecting Broken Object Level Authorization (BOLA) vulnerabilities by building API call graphs to simulate attacker and owner contexts, then testing these contexts by sending real HTTP requests to your APIs.</p>
<p>The scanner is now available via the Cloudflare API. To scan, set up your target environment, owner and attacker credentials, and upload your OpenAPI file with response schemas. The scanner will be available in the Cloudflare dashboard in a future release.</p>
<p><strong>Access</strong>: This feature is only available to API Shield subscribers via the Cloudflare API. We hope you will use the API for programmatic integration into your CI/CD pipelines and security dashboards.</p>
<p><strong>Documentation</strong>: Refer to the <a href="/api-shield/security/vulnerability-scanner/">developer documentation</a> to start scanning your endpoints today.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-security/2/">Previous</a><span>Page 3 of 9</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-security/4/">Next</a></nav>
