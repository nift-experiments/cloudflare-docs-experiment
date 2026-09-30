---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/waf/
  description: '2026-09-15'
  full_title: waf changelog | Cloudflare Docs
  head_html: <title>waf changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-15"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/waf/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="waf changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-15"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/waf/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/waf/#page","headline":"waf changelog | Cloudflare Docs","description":"2026-09-15","url":"https://developers.cloudflare.com/changelog/product/waf/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/waf/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="waf-release-2026-09-15"><a href="/changelog/post/2026-09-15-waf-release/">WAF Release - 2026-09-15</a></h2>
<p><em>2026-09-15</em></p>
<p>This release introduces new threat detections to enhance protection against command injection attempts, Server-Side Request Forgery (SSRF) targeting cloud metadata, and information disclosure within version control history.</p>
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
				<code class="nb-rule-id" title="b2170b7b1a2c4b8eba0b498eca453d31">ca453d31</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - 3</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="02c818297e6d42aaa55e67f5e540f17f">e540f17f</code>
</td>
<td>N/A</td>
<td>Version Control - Information Disclosure - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Version Control - Information Disclosure" (ID:{" "}<code class="nb-rule-id" title="23548ee2b36547a1be09bb2c0550c529">0550c529</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="93793848937f4f988f1dfdabba458b4b">ba458b4b</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 10</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>        
</tbody>
</table>


<h2 id="waf-release-scheduled-changes-for-2026-09-22"><a href="/changelog/post/scheduled-waf-release/">WAF Release - Scheduled changes for 2026-09-22</a></h2>
<p><em>2026-09-15</em></p>
<table style="width: 100%">
<thead>
<tr>
<th>Announcement Date</th>
<th>Release Date</th>
<th>Release Behavior</th>
<th>Legacy Rule ID</th>
<th>Rule ID</th>
<th>Description</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="40b93de7a8f848709c4ec3e60f0313d6">0f0313d6</code>
</td>
<td>SSRF - Block jar HTTP loopback payload</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="ca05d6c847834f75a317c33b5f21b651">5f21b651</code>
</td>
<td>SSRF - Cloud,Link-Local non-standard IP notation</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="48dfa3e5bef84063914edfe175cd912a">75cd912a</code>
</td>
<td>SSRF - Local non-standard IP notation</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="cd1de1fd21c443508f9073f2a1ba83f6">a1ba83f6</code>
</td>
<td>SSTI - Jinja Dangerous Globals Chain</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-09-10-emergency"><a href="/changelog/post/2026-09-10-emergency-waf-release/">WAF Release - 2026-09-10 - Emergency</a></h2>
<p><em>2026-09-10</em></p>
<p>This update provides immediate defense against a high-severity, actively exploited zero-day vulnerability targeting Adobe Commerce and Magento Open Source storefronts.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Adobe Commerce and Magento RCE (CVE-2026-75650 / &quot;StyleSmuggler&quot;): Unauthenticated Remote Code Execution (RCE) vulnerability caused by improper neutralization of special elements in the platform's template engine. Unauthenticated attackers can inject arbitrary PHP payloads through style properties to execute system commands and deploy persistent malware.</li>
</ul>
<p><strong>Impact</strong></p>
<p>This emergency rule provides immediate edge-level mitigation and virtual patching, origin applications must be urgently updated. We strongly recommend to apply the hotfix outlined in Adobe Security Bulletin <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146">APSB26-146</a> and immediately rotate all potentially exposed encryption keys, integration tokens, and system credentials, as patching alone does not remediate an existing compromise.</p>
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
				<code class="nb-rule-id" title="f9a3026b0fdc4d63b7338346440f5c55">440f5c55</code>
</td>
<td>N/A</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2026-75650</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-09-08"><a href="/changelog/post/2026-09-08-waf-release/">WAF Release - 2026-09-08</a></h2>
<p><em>2026-09-08</em></p>
<p>This release enhances detection logic for existing rules targeting Next.js remote code execution (RCE) vulnerabilities by consolidating active beta rules into baseline signatures.</p>
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
				<code class="nb-rule-id" title="d5d9f863e50b416faf43934dc76ba662">c76ba662</code>
</td>
<td>N/A</td>
<td>Next.js - Image Optimizer Remote Code Execution via Crafted AVIF - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Next.js - Image Optimizer Remote Code Execution via Crafted AVIF" (ID:{" "}<code class="nb-rule-id" title="18b22b0bd423423c945b3a0180256efe">80256efe</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="771ac3761dcd485cb0e91ea0208457cf">208457cf</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2026-75604 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Next.js - Remote Code Execution - CVE:CVE-2026-75604" (ID:{" "}<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>).</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-09-01"><a href="/changelog/post/2026-09-01-waf-release/">WAF Release - 2026-09-01</a></h2>
<p><em>2026-09-01</em></p>
<p>This release introduces a new threat detection to enhance protection against SQL injection (SQLi) attempts exploiting complex query syntax.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>SQLi Protection: Improved coverage for SQL injection patterns involving WHERE comparisons combined with WITH clauses.</li>
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
				<code class="nb-rule-id" title="d2d75b2f0614405f9fab0354bcfa0966">bcfa0966</code>
</td>
<td>N/A</td>
<td>SQLi - WHERE Comparison With WITH Clause</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-08-26-emergency"><a href="/changelog/post/2026-08-26-emergency-waf-release/">WAF Release - 2026-08-26 - Emergency</a></h2>
<p><em>2026-08-26</em></p>
<p>This emergency release updates an existing Next.js remote code execution rule to identify CVE-2026-75604 and adds a new rule for remote code execution in the Next.js Image Optimizer via crafted AVIF images.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-75604 affects Windows-hosted Next.js applications using both the Pages Router and App Router without Cache Components and can lead to unauthenticated remote code execution.</p>
</li>
<li>
<p>GHSA-2xp9-vwfh-vxw4 affects the Next.js Image Optimizer and can lead to unauthenticated remote code execution when it optimizes an attacker-controlled AVIF image.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Next.js recommends updating to version 16.3.3 or 15.5.24 to address these vulnerabilities.</p>
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
				<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2026-75604</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="18b22b0bd423423c945b3a0180256efe">80256efe</code>
</td>
<td>N/A</td>
<td>Next.js - Image Optimizer Remote Code Execution via Crafted AVIF</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-08-25"><a href="/changelog/post/2026-08-25-waf-release/">WAF Release - 2026-08-25</a></h2>
<p><em>2026-08-25</em></p>
<p>This release moves four new detections from Log to Block, merges the XSS, HTML Injection - Script Tag - Beta rule into the original rule, and adds a Generic Rules - Remote Code Execution rule in Block mode.</p>
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


<h2 id="leaked-credentials-detection-now-scans-authorization-headers"><a href="/changelog/post/2026-08-20-leaked-credentials-authorization-header/">Leaked credentials detection now scans Authorization headers</a></h2>
<p><em>2026-08-20</em></p>
<p><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a> now scans the <code>Authorization</code> request header for Basic Authentication credentials. Previously, the detection only inspected request bodies, query strings, and headers for well-known web applications or custom detection locations, which meant credentials sent through HTTP Basic Authentication were not covered by default.</p>
<p>This new default scan location decodes the <code>Authorization: Basic &lt;credentials&gt;</code> header and compares the extracted username and password against Cloudflare's database of leaked credentials, the same way as other default scan locations. Matches populate the existing <a href="/waf/detections/leaked-credentials/#leaked-credentials-fields">leaked credentials fields</a>, such as <code>cf.waf.credential_check.password_leaked</code>, and trigger the <a href="/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header"><code>Exposed-Credential-Check</code> managed transform header</a> if configured, so you can reuse existing <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a> without changes.</p>
<p>This change was applied automatically for zones with leaked credentials detection enabled. No configuration changes are required.</p>
<p>For more information, refer to <a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a>.</p>


<h2 id="waf-release-2026-08-17"><a href="/changelog/post/2026-08-17-waf-release/">WAF Release - 2026-08-17</a></h2>
<p><em>2026-08-17</em></p>
<p>This release updates WordPress remote code execution rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify CVE-2026-65640.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-65640: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.</li>
</ul>
<p><strong>Impact</strong></p>
<p>The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.</p>
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
				<code class="nb-rule-id" title="dcf635ab2e744e1a994443973590a4ad">3590a4ad</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-65640</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ad9f2049b094c608be0f8adcfe1a93c">cfe1a93c</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-65640</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-08-11"><a href="/changelog/post/2026-08-11-waf-release/">WAF Release - 2026-08-11</a></h2>
<p><em>2026-08-11</em></p>
<p>This release introduces new protection for a remote code execution vulnerability in vBulletin and improves two existing detections.</p>
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


<h2 id="waf-release-2026-08-07"><a href="/changelog/post/2026-08-07-waf-release/">WAF Release - 2026-08-07</a></h2>
<p><em>2026-08-07</em></p>
<p>This release updates WordPress XSS rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify XSS2Shell (CVE-2026-64638). It also disables the Command Injection - Obfuscation rule.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-64638: A pre-authentication reflected cross-site scripting vulnerability affecting the WordPress login screen. Exploitation requires social engineering and explicit interaction by the target user. Under additional conditions, it may be escalated to remote code execution.</li>
</ul>
<p><strong>Impact</strong></p>
<p>The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.</p>
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
				<code class="nb-rule-id" title="d3852d0891634686a46114069c6dff1c">9c6dff1c</code>
</td>
<td>N/A</td>
<td>Wordpress - XSS - CVE:CVE-2026-64638</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="5bdf578fff504b8cbe3b7f699ab5ed95">9ab5ed95</code>
</td>
<td>N/A</td>
<td>Wordpress - XSS - CVE:CVE-2026-64638</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="95a84ab1645a49c685648c17761e7a4c">761e7a4c</code>
</td>
<td>N/A</td>
<td>Command Injection - Obfuscation</td>
<td>Block</td>
<td>Disabled</td>
<td>Detection logic has been deprecated</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-08-04"><a href="/changelog/post/2026-08-04-waf-release/">WAF Release - 2026-08-04</a></h2>
<p><em>2026-08-04</em></p>
<p>This release introduces new rules and updates Microsoft SharePoint RCE alongside enhanced SSRF cloud protection rule actions.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-50522: An insecure deserialization vulnerability in Microsoft SharePoint Server. This may allow an unauthenticated attacker to execute arbitrary code using crafted requests.</li>
<li>CVE-2026-66066: An improper input processing vulnerability in Ruby on Rails Active Storage image variant transformations. This may allow an unauthenticated attacker to perform arbitrary file reads and achieve Remote Code Execution (RCE) using maliciously crafted payload requests.</li>
<li>Generic Cloud Protections: Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications.</li>
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
				<code class="nb-rule-id" title="91aee93c31944828bf86f068052b07cf">052b07cf</code>
</td>
<td>N/A</td>
<td>Microsoft SharePoint - Remote Code Execution - CVE:CVE-2026-50522</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89d0243997d24c6ea1d610a23a5b40d6">3a5b40d6</code>
</td>
<td>N/A</td>
<td>Rails - Arbitrary File Read & RCE - CVE:CVE-2026-66066</td>
<td>Block</td>
<td>Block</td>
<td>
				This was labeled as File Upload - RCE.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="98bfd6bb46074d5b8d1c4b39743a63ec">743a63ec</code>
</td>
<td>N/A</td>
<td>SSRF - Local - 2 - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ecd26d61a75e46f6a4449a06ab8af26f">ab8af26f</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - 2 - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="281a1b7086b84db7a695220725ba9d7c">25ba9d7c</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud</td>
<td>Disabled</td>
<td>Block</td>
<td>
				We are changing the action for this rule from Disabled to BLOCK
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="158177dec2504acdba1f2da201a076eb">01a076eb</code>
</td>
<td>N/A</td>
<td>SSRF - Local - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-07-29"><a href="/changelog/post/2026-07-29-waf-release/">WAF Release - 2026-07-29</a></h2>
<p><em>2026-07-29</em></p>
<p>This release introduces new rules and updates existing threat signatures to provide targeted protections for vulnerabilities in Nuxt Server Island components and Alibaba Fastjson deserialization routines, alongside enhanced protections for cloud metadata Server-Side Request Forgery (SSRF) and obfuscated command injection attempts.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Nuxt Server Island - RCE(GHSA-9473-5f9j-94wq): An unauthenticated vulnerability in Nuxt Server Islands where remote attackers can supply arbitrary component names or props to endpoints. Manipulating these parameters allows unauthenticated component Remote Code Execution (RCE) on the server.</p>
</li>
<li>
<p>Alibaba Fastjson JSONType Remote Code Execution: A unauthenticated remote code execution vulnerability in Alibaba Fastjson (≤ 1.2.83) during JSON deserialization. Under default configurations, attackers can execute arbitrary system commands, bypassing traditional classpath and gadget-based defenses.</p>
</li>
<li>
<p>Generic Protections (SSRF &amp; Command Injection): Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications, alongside new rules targeting obfuscated command injection patterns across request parameters.</p>
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
				<code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is an improved detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="95a84ab1645a49c685648c17761e7a4c">761e7a4c</code>
</td>
<td>N/A</td>
<td>Command Injection - Obfuscation</td>
<td>Log</td>
<td>Block</td>            
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58df9693db4d454a8764fcda7347c892">7347c892</code>
</td>
<td>N/A</td>
<td>Alibaba Fastjson JSONType Remote Code Execution - Body</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6159ead63d284147943dc5a18ec012ea">8ec012ea</code>
</td>
<td>N/A</td>
<td>Nuxt Server Island - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.This was labeled as Generic Rules - RCE.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dcf635ab2e744e1a994443973590a4ad">3590a4ad</code>
</td>
<td>N/A</td>
<td>Generic Rules - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d3852d0891634686a46114069c6dff1c">9c6dff1c</code>
</td>
<td>N/A</td>
<td>Generic Rules - XSS</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89d0243997d24c6ea1d610a23a5b40d6">3a5b40d6</code>
</td>
<td>N/A</td>
<td>File Upload - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ad9f2049b094c608be0f8adcfe1a93c">cfe1a93c</code>
</td>
<td>N/A</td>
<td>Generic Rules - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="5bdf578fff504b8cbe3b7f699ab5ed95">9ab5ed95</code>
</td>
<td>N/A</td>
<td>Generic Rules - XSS</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="7ecac499d14a4750aa58c1e21b7f9c67">1b7f9c67</code>
</td>
<td>N/A</td>
<td>File Upload - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-07-21"><a href="/changelog/post/2026-07-21-waf-release/">WAF Release - 2026-07-21</a></h2>
<p><em>2026-07-21</em></p>
<p>This release introduces new rules for vulnerabilities in Adobe ColdFusion, Next.js, WordPress alongside updates to existing rules thereby providing enhanced generic protections against Server-Side Request Forgery (SSRF), Local File Inclusion (LFI), and Cross-Site Scripting (XSS).</p>
<p><strong>WAF and framework adapter mitigations for Next.js vulnerabilities</strong></p>
<p>Multiple <a href="https://nextjs.org/blog/july-2026-security-release">security vulnerabilities</a> were disclosed and patched by the Next.js team through July 2026 security release. These include denial of service, middleware and proxy bypass, server-side request forgery, information disclosure, and cache poisoning across a range of severities.</p>
<p>Several of the disclosed vulnerabilities are not possible to block at WAF layer,we strongly recommend updating your application and its dependencies immediately. Patched versions are available through v16.2.11 (Active LTS) and v15.5.21 (Maintenance LTS) to address these issues.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Advisory</th>
<th>CVE</th>
<th>Severity</th>
<th>Issue</th>
<th>WAF Coverage</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-m99w-x7hq-7vfj">Denial of Service in App Router using Server Actions</a></td>
<td>CVE-2026-64641</td>
<td>High</td>
<td>
				Crafted requests targeting Next.js applications using App Router with at least one Server Action can lead to excessive CPU usage. The CPU usage blocks processing of further requests in the same process, leading to Denial of Service.
</td>
<td>
				WAF rule Next.js - DoS - CVE-2026-64641 (<code class="nb-rule-id" title="b013b67c357547b4b866234390dcdb0a">90dcdb0a</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-6gpp-xcg3-4w24">Middleware / Proxy bypass in App Router applications using Turbopack and single locale</a></td>
<td>CVE-2026-64642</td>
<td>High</td>
<td>
				Next.js applications using App Router built with Turbopack and a single entry in config.i18n.locales are vulnerable to a middleware/proxy bypass. Accordingly, any authentication or security checks that a middleware/proxy may perform are bypassed.
</td>
<td>
				This is a middleware bypass that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-p9j2-gv94-2wf4">Server-Side Request Forgery in rewrites via attacker-controlled destination hostname</a></td>
<td>CVE-2026-64645</td>
<td>High</td>
<td>
				A rewrites() or redirects() rule that builds its external destination hostname from request-controlled input can be pointed at an arbitrary hostname, regardless of the rule's hostname suffix. For rewrites, this behavior enables Server-Side Request Forgery (SSRF); for redirects, Open Redirect can be achieved.
</td>
<td>
				Existing SSRF rules provide adequate coverage for this vulnerability, no tailored WAF rule was developed.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-89xv-2m56-2m9x">Server-Side Request Forgery in Server Actions on custom servers</a></td>
<td>CVE-2026-64649</td>
<td>High</td>
<td>
				When a Server Action forwards or redirects a request, an attacker can cause the server to send that outbound request to a malicious host (Server-Side Request Forgery). This requires the attacker’s request to control Host-associated headers.
</td>
<td>
				WAF rule Next.js - SSRF - CVE-2026-64649 (<code class="nb-rule-id" title="7fe6d6f3df774ae2a0011f20930091a3">930091a3</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-q8wf-6r8g-63ch">Denial of Service in the Image Optimization API using SVGs</a></td>
<td>CVE-2026-64644</td>
<td>Medium</td>
<td>
				When self-hosting Next.js with the default image loader, the Image Optimization API can optimize remotely hosted images if configured (not enabled by default). If those images contain malicious content, the images can cause CPU exhaustion in the /_next/image endpoint.
</td>
<td>
				Malicious request is unfortunately indistinguishable from a legitimate image optimization request, so no WAF rule has been created to address this vulnerability.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4c39-4ccg-62r3">Unbounded Server Action payload in Edge runtime</a></td>
<td>CVE-2026-64646</td>
<td>Medium</td>
<td>
				A crafted request can lead to memory consumption on Server Actions in the Edge runtime. Next.js applications which use App Router and have at least one Server Action are affected.
</td>
<td>
				Unfortunately there is no one size fits all rule that can be deployed through WAF in lieu of custom bodySizeLimit configurations, so no WAF rule has been created to address this vulnerability.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-955p-x3mx-jcvp">Unauthenticated disclosure of internal Server Function endpoints</a></td>
<td>CVE-2026-64643</td>
<td>Medium</td>
<td>
				In Next.js applications using App Router, Server Actions (use server) or use cache endpoint IDs can be globally disclosed. An attacker can use this for reconnaissance and as part of a broader attack chain.
</td>
<td>
				WAF rule Next.js - Information Disclosure - CVE-2026-64643 (<code class="nb-rule-id" title="6c4135d4d9d745e4866ad83672952826">72952826</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-68g3-v927-f742">Cache confusion of response bodies for requests with bodies</a></td>
<td>CVE-2026-64648</td>
<td>Medium</td>
<td>
				A server-side fetch with a request body may return a cached response body from a different request to the same URL but different body. This only applies for fetch calls of the shape fetch(new Request(init), aDifferentInit)
</td>
<td>
				This is an application logic bug that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4633-3j49-mh5q">Cache confusion of response bodies for requests with bodies containing invalid UTF-8 byte sequences</a></td>
<td>CVE-2026-64647</td>
<td>Medium</td>
<td>
				A server-side fetch with a request body may return a cached response body from a different request to the same URL but different body. This only applies when receiving request bodies which contain invalid UTF-8 characters.
</td>
<td>
				This is an application logic bug that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
</tbody>
</table>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-48276: A path traversal vulnerability in Adobe ColdFusion file upload mechanisms allows unauthenticated attackers to write or upload files to arbitrary locations outside designated directories on the origin server.</p>
</li>
<li>
<p>CVE-2026-48282: A path traversal vulnerability in Adobe ColdFusion enables unauthenticated attackers to manipulate directory sequences and access restricted system files on the host filesystem.</p>
</li>
<li>
<p>CVE-2026-60137: An unauthenticated SQL injection vulnerability affecting WordPress. Threat actors exploit unsanitized input parameters to execute arbitrary SQL queries, leading to unauthorized database access, record manipulation, or data exfiltration.</p>
</li>
<li>
<p>CVE-2026-63030: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.</p>
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
				<code class="nb-rule-id" title="7fbdc9407bdb4a4eae2b3d91215e7d31">215e7d31</code>
</td>
<td>N/A</td>
<td>SSRF - Restricted Protocol</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ca512d240d848d6a0c7ef42a935ee5d">a935ee5d</code>
</td>
<td>N/A</td>
<td>SSRF - Obfuscated Host</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a3fb0870c38440d8a9a0eba81b0230ac">1b0230ac</code>
</td>
<td>N/A</td>
<td>LFI - Path Traversal</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="452a04be3f73458c863d8dae61349c8b">61349c8b</code>
</td>
<td>N/A</td>
<td>Adobe ColdFusion - File Upload Path Traversal - CVE:CVE-2026-48276</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a53a3fb491c64d74908081ee9cb61eac">9cb61eac</code>
</td>
<td>N/A</td>
<td>Adobe ColdFusion - Path Traversal - CVE:CVE-2026-48282</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d8b63828c2344d919b94d2594ac5e21f">4ac5e21f</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="264a83a764be428ca41d516ff31f5559">f31f5559</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4ba21a60837244029183b782987984fd">987984fd</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c060d3a371549219ee290d7ed933fcc">ed933fcc</code>
</td>
<td>N/A</td>
<td>Wordpress - SQL Injection - CVE:CVE-2026-60137</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - SQLi.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7dfb2bd4708d4b88b9911dc0550664b6">550664b6</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-63030</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Unauthenticated RCE.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="db003b39b7774859a8d588ce33697a1a">33697a1a</code>
</td>
<td>N/A</td>
<td>Wordpress - SQL Injection - CVE:CVE-2026-60137</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - SQLi.
</td>
</tr>	
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="ebd3f2df15c74ddcbf6220c9b5ec246a">b5ec246a</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-63030</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Unauthenticated RCE.
</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6c4135d4d9d745e4866ad83672952826">72952826</code>
</td>
<td>N/A</td>
<td>Next.js - Information Disclosure - CVE-2026-64643</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Information Disclosure.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7fe6d6f3df774ae2a0011f20930091a3">930091a3</code>
</td>
<td>N/A</td>
<td>Next.js - SSRF - CVE-2026-64649</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Auth Bypass - 2.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c4ca56c0a6a348299d5a93e663167195">63167195</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - Cache Components</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - RCE.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b013b67c357547b4b866234390dcdb0a">90dcdb0a</code>
</td>
<td>N/A</td>
<td>Next.js - DoS - CVE-2026-64641</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - DoS.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="aa21c9b8b97743bfb217748b2049a60c">2049a60c</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Body - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e7ee67e824844754b513cdf3836855a4">836855a4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Header - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5f2a6681a2b94442b23816286d060a0d">6d060a0d</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - URI - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-07-17-emergency"><a href="/changelog/post/2026-07-17-emergency-waf-release/">WAF Release - 2026-07-17 - Emergency</a></h2>
<p><em>2026-07-17</em></p>
<p>This emergency release adds a new managed rule to block active exploitation of a critical remote code execution (RCE) and SQL injection (SQLi) vulnerability found in popular web frameworks.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Generic Frameworks - Unauthenticated RCE: Attackers can execute arbitrary system commands with web server privileges by sending malicious input containing invalid path sequences during request processing.</p>
</li>
<li>
<p>Generic Frameworks - SQLi: Attackers can execute unauthorized database queries due to a failure to sanitize input values within request parameters.</p>
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
				<code class="nb-rule-id" title="7dfb2bd4708d4b88b9911dc0550664b6">550664b6</code>
</td>
<td>N/A</td>
<td>Generic Rules - Unauthenticated RCE</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c060d3a371549219ee290d7ed933fcc">ed933fcc</code>
</td>
<td>N/A</td>
<td>Generic Rules - SQLi </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="ebd3f2df15c74ddcbf6220c9b5ec246a">b5ec246a</code>
</td>
<td>N/A</td>
<td>Generic Rules - Unauthenticated RCE </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="db003b39b7774859a8d588ce33697a1a">33697a1a</code>
</td>
<td>N/A</td>
<td>Generic Rules - SQLi </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>        
</tbody>
</table>


<h2 id="waf-release-2026-07-14"><a href="/changelog/post/2026-07-14-waf-release/">WAF Release - 2026-07-14</a></h2>
<p><em>2026-07-14</em></p>
<p>This release introduces new rules targeting critical infrastructure vulnerabilities. These include an unauthenticated memory disclosure flaw in Citrix NetScaler ADC and Gateway (CVE-2026-8451) and a high-severity pre-authentication remote code execution (RCE) vulnerability in Progress Kemp LoadMaster (CVE-2026-8037).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-8451: An insufficient input validation vulnerability affects Citrix NetScaler ADC and NetScaler Gateway appliances configured as a SAML Identity Provider (IdP). Remote, unauthenticated attackers can exploit this flaw by sending malformed requests to trigger a memory overread, allowing them to leak chunks of sensitive data from adjacent appliance memory.</p>
</li>
<li>
<p>CVE-2026-8037: A critical OS command injection vulnerability in Progress Kemp LoadMaster load balancers allows unauthenticated remote attackers to achieve remote code execution (RCE).</p>
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
				<code class="nb-rule-id" title="78826e3223b94da493a2ade876973ac4">76973ac4</code>
</td>
<td>N/A</td>
<td>Citrix Netscaler ADC - Insufficient Input Validation - CVE:CVE-2026-8451</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6b64d216620449fbb273d07910233f36">10233f36</code>
</td>
<td>N/A</td>
<td>Progress Kemp LoadMaster - Remote Code Execution - CVE:CVE-2026-8037</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>		
</tbody>
</table>


<h2 id="waf-release-2026-07-01"><a href="/changelog/post/2026-07-01-waf-release/">WAF Release - 2026-07-01</a></h2>
<p><em>2026-07-01</em></p>
<p>This release adds targeted coverage for a path traversal flaw in Fortinet FortiSandbox (CVE-2026-39813) and transitions the Anomaly:Header:User-Agent - Fake Bing or MSN Bot rule action from Block to Disabled.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-39813: A path traversal vulnerability in Fortinet FortiSandbox allows remote, unauthenticated attackers to read arbitrary files from the underlying filesystem due to insufficient validation of user-supplied input paths.</li>
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
				<code class="nb-rule-id" title="32075e19b1494117ac5915e8d84c92c9">d84c92c9</code>
</td>
<td>N/A</td>
<td>Fortinet FortiSandbox - Path Traversal - CVE:CVE-2026-39813</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ae20608d93b94e97988db1bbc12cf9c8">c12cf9c8</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:User-Agent - Fake Bing or MSN Bot</td>
<td>Enabled</td>
<td>Disabled</td>
<td>
				We are changing the action for this rule from BLOCK to Disabled
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-06-23"><a href="/changelog/post/2026-06-23-waf-release/">WAF Release - 2026-06-23</a></h2>
<p><em>2026-06-23</em></p>
<p>This week's release introduces new managed protection to address a critical pre-authentication OS command injection vulnerability in Ivanti Sentry (CVE-2026-10520).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-10520: An OS command injection vulnerability in Ivanti Sentry allows remote, unauthenticated attackers to execute arbitrary system commands with root privileges. The flaw stems from improper sanitization of input strings parsed during internal configuration handling.</li>
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
				<code class="nb-rule-id" title="500a90789f874345b60b0de7242fdf83">242fdf83</code>
</td>
<td>N/A</td>
<td>Ivanti Sentry - Command Injection - CVE:CVE-2026-10520</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>		
</tbody>
</table>


<h2 id="use-cloudforce-one-threat-intelligence-in-waf-rules"><a href="/changelog/post/2026-06-15-threat-intelligence-fields/">Use Cloudforce One threat intelligence in WAF rules</a></h2>
<p><em>2026-06-15</em></p>
<p>You can now match incoming requests against Cloudforce One threat intelligence in your WAF rules. A new detection looks up the client IP address of each request against the threat intelligence database. If the IP was involved in threat activity in the past seven days, Cloudflare populates <code>cf.intel.ip.*</code> fields that you can use in <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a>.</p>
<p>The detection populates the following fields. Use the <a href="/ruleset-engine/rules-language/functions/#any"><code>any()</code></a> function with the <code>[*]</code> wildcard to match array values:</p>
<ul>
<li><code>cf.intel.ip.datasets</code> — the dataset that flagged the IP address (<code>ddos</code> or <code>waf</code>).</li>
<li><code>cf.intel.ip.target_industries</code> — industries the IP address has targeted.</li>
<li><code>cf.intel.ip.attacker_names</code> — known threat actors associated with the IP address.</li>
<li><code>cf.intel.ip.attacker_countries</code> — source countries of the threat activity.</li>
<li><code>cf.intel.ip.target_countries</code> — countries the IP address has targeted.</li>
</ul>
<p>For example, the following custom rule expression blocks requests from IP addresses associated with DDoS activity that have targeted France:</p>
<pre tabindex="0"><code class="language-txt">any(cf.intel.ip.target_countries[*] == &quot;FR&quot;) and any(cf.intel.ip.datasets[*] == &quot;ddos&quot;)&#10;</code></pre>
<p>These fields work with the Cloudflare API and Terraform. Matches are logged in <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</p>
<p>The threat intelligence detection is available to customers with an active <a href="/security-center/cloudforce-one/">Cloudforce One</a> subscription. For more information, refer to <a href="/waf/detections/threat-intelligence/">Threat intelligence</a>.</p>


<h2 id="waf-release-2026-06-15"><a href="/changelog/post/2026-06-15-waf-release/">WAF Release - 2026-06-15</a></h2>
<p><em>2026-06-15</em></p>
<p>This week's release introduces new managed protection to address a critical SQL injection vulnerability in Ghost CMS (CVE-2026-26980) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic. These rules protect affected installations from unauthorized data exfiltration at the network edge.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-26980: A blind SQL injection vulnerability in the Ghost CMS Content API (versions 3.24.0 to 6.19.0) allows unauthenticated remote attackers to inject malicious SQL commands via query parameters due to improper input validation.</li>
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
				<code class="nb-rule-id" title="439c4ef64b32447989bdf412b4c29bc6">b4c29bc6</code>
</td>
<td>N/A</td>
<td>Ghost CMS - SQLi - CVE:CVE-2026-26980</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6c64b68ef5ed45e7a622cdaab56f403f">b56f403f</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>		
</tbody>
</table>


<h2 id="waf-release-2026-06-09"><a href="/changelog/post/2026-06-09-waf-release/">WAF Release - 2026-06-09</a></h2>
<p><em>2026-06-09</em></p>
<p>This release introduces new detections for a critical SQL injection vulnerability in Drupal installations utilizing PostgreSQL (CVE-2026-9082), alongside targeted protection for an unsafe deserialization flaw in the Mirasvit Cache Warmer extension (CVE-2026-45247). Additionally, this release includes coverage for a prototype pollution vector in Axios (CVE-2026-40175) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic.</p>
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


<h2 id="waf-release-2026-05-20"><a href="/changelog/post/2026-05-20-waf-release/">WAF Release - 2026-05-20</a></h2>
<p><em>2026-05-20</em></p>
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
				<code class="nb-rule-id" title="bcdcec3ea63a480896513dc39e9c068d">9e9c068d</code>
</td>
<td>N/A</td>
<td>Sitecore - Cache Poisoning - CVE:CVE-2025-53693 Beta</td>
<td>N/A</td>
<td>Block</td>
<td>
				This rule is merged into the original rule "Sitecore - Cache Poisoning - CVE:CVE-2025-53693" (ID:{" "}
				<code class="nb-rule-id" title="d1bd7563e6254db48ce703807c5b669c">7c5b669c</code>).
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-05-15-emergency"><a href="/changelog/post/2026-05-15-emergency-waf-release/">WAF Release - 2026-05-15 - Emergency</a></h2>
<p><em>2026-05-15</em></p>
<p>This emergency release introduces two new rules to detect nginx heap buffer overflow and heap spray exploitation attempts targeting the rewrite module's <code>is_args</code> stale-state bug (CVE-2026-42945).</p>
<p><strong>Key Findings</strong></p>
<p>CVE-2026-42945: nginx Heap Buffer Overflow via Stale <code>is_args</code> in Rewrite Module</p>
<p>Successful exploitation allows remote attackers to trigger a heap buffer overflow in nginx's rewrite module by sending crafted URIs containing escapable characters. A length/copy pass mismatch in <code>ngx_http_script_copy_capture_code()</code> causes the copy pass to write escaped data into an undersized buffer, leading to heap corruption. This enables denial of service (worker process crash) and, with heap feng shui techniques, potential remote code execution.</p>
<p>We strongly recommend upgrading to nginx 1.30.1 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, avoid <code>rewrite</code> directives with <code>?</code> in the replacement string followed by <code>set</code> or <code>if</code> referencing capture groups.</p>
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
				<code class="nb-rule-id" title="2013e3e58efe4b79a26e214f7e52be73">7e52be73</code>
</td>
<td>N/A</td>
<td>nginx - Remote Code Execution - Buffer Overread - CVE:CVE-2026-42945</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="68226e83a4d14ee9a9c878469df0ee6c">9df0ee6c</code>
</td>
<td>N/A</td>
<td>nginx - Remote Code Execution - Heap Spray - CVE:CVE-2026-42945</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-05-11"><a href="/changelog/post/2026-05-11-waf-release/">WAF Release - 2026-05-11</a></h2>
<p><em>2026-05-11</em></p>
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
				<code class="nb-rule-id" title="23ac4a9e53f94467ba470c9468b3c389">68b3c389</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Java Deserialization - Body - Beta</td>
<td>Block</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Remote Code Execution - Java Deserialization" (ID:{" "}
				<code class="nb-rule-id" title="36b0532eb3c941449afed2d3744305c4">744305c4</code>).
</td>
</tr>
</tbody>
</table>


<h2 id="waf-and-framework-adapter-mitigations-for-react-and-next-js-vulnerabilities"><a href="/changelog/post/2026-05-06-react-nextjs-vulnerabilities/">WAF and framework adapter mitigations for React and Next.js vulnerabilities</a></h2>
<p><em>2026-05-07 12:00:00 UTC</em></p>
<p>Multiple security vulnerabilities were disclosed by the React team and Vercel affecting React Server Components and Next.js. These include denial of service, middleware and proxy bypass, server-side request forgery, cross-site scripting, and cache poisoning issues across a range of severity levels.</p>
<p><strong>We strongly recommend updating your application and its dependencies immediately.</strong> Patched versions are available for React (<code>react-server-dom-webpack</code>, <code>react-server-dom-parcel</code>, and <code>react-server-dom-turbopack</code> <code>19.0.6</code>, <code>19.1.7</code>, and <code>19.2.6</code>) and Next.js (<code>15.5.16</code> and <code>16.2.5</code>).</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-waf-protections">WAF protections</h4>
<p>Cloudflare WAF rules deployed in response to prior React Server Component CVEs (<a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a> and <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a>) already provide coverage for the newly disclosed denial-of-service vulnerabilities. These rules are enabled by default with a Block action for all customers using the Cloudflare Managed Ruleset, including Free plan customers using the Free Managed Ruleset.</p>
<table>
<thead>
<tr>
<th>Ruleset</th>
<th>Rule description</th>
<th>Rule ID</th>
<th>Default action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a></td>
<td><code>2694f1610c0b471393b21aef102ec699</code></td>
<td>Block</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a></td>
<td><code>aaede80b4d414dc89c443cea61680354</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>The existing rules detect the underlying attack patterns generically. As a result, they apply to the new <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> denial-of-service vulnerability in Server Components and the corresponding Next.js advisory <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>.</p>
<p>Cloudflare is investigating whether WAF rules can be safely and effectively deployed for three of the high-severity advisories: <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>, <a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a>, and <a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a>. If it is possible to create a managed WAF rule that mitigates these CVEs and does not potentially break application behavior, Cloudflare will add additional managed WAF rules. These rules will be announced through the <a href="/waf/change-log/changelog/">WAF changelog</a>. Because these vulnerabilities were shared with Cloudflare with minimal advance notice, we are still investigating what WAF mitigations are possible.</p>
<p>Several of the disclosed vulnerabilities are not possible to block in WAF. We strongly recommend updating your applications so they are not purely reliant on WAF mitigations.</p>
<p>Customers on Pro, Business, or Enterprise plans should ensure that <a href="/waf/get-started/#1-deploy-the-cloudflare-managed-ruleset">Managed Rules are enabled</a>.</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-next-js-adapters">Next.js adapters</h4>
<p><strong>Vinext:</strong> <a href="https://github.com/cloudflare/vinext">Vinext</a> is a Vite plugin that reimplements the Next.js API surface. Vinext's latest release is not vulnerable to any of the disclosed CVEs. Vinext's architecture differs from stock Next.js in ways that sidestep the affected code paths. For example, it does not implement the PPR resume protocol, does not expose Pages Router data-route endpoints, and strips internal headers such as <code>x-nextjs-data</code> at request boundaries. As an extra layer of defense, we added a React <code>19.2.6</code> or later requirement when running <code>vinext init</code> (<a href="https://github.com/cloudflare/vinext/pull/1118">PR #1118</a>, <a href="https://github.com/cloudflare/vinext/pull/1112">PR #1112</a>) to prevent accidentally running a vulnerable version of React with Vinext.</p>
<p><strong>OpenNext on Cloudflare:</strong> OpenNext is an adapter that lets you deploy Next.js apps to the Cloudflare Workers platform. OpenNext itself is not directly vulnerable to the React denial-of-service CVE, but users must update the Next.js version in their application. The OpenNext team has updated the adapter to further harden against these vectors and released a new version of the Cloudflare adapter. Test fixtures and examples have been updated to use patched versions (<a href="https://github.com/opennextjs/opennextjs-cloudflare/pull/1255">PR #1255</a>).</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-summary-of-disclosed-vulnerabilities">Summary of disclosed vulnerabilities</h4>
<table>
<thead>
<tr>
<th>Advisory</th>
<th>Severity</th>
<th>Issue</th>
<th>WAF status</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a></td>
<td>High</td>
<td>Denial of service in Server Components</td>
<td><strong>WAF rules in place:</strong> <code>2694f1610c0b471393b21aef102ec699</code>, <code>aaede80b4d414dc89c443cea61680354</code><br/>Cloudflare is investigating additional managed WAF coverage</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a></td>
<td>High</td>
<td>Middleware bypass via segment-prefetch routes</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a></td>
<td>High</td>
<td>Denial of service via connection exhaustion in Cache Components</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv"><code>GHSA-492v-c6pp-mqqv</code></a></td>
<td>High</td>
<td>Middleware bypass via dynamic route parameter injection</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r"><code>GHSA-c4j6-fc7j-m34r</code></a></td>
<td>High</td>
<td>SSRF via WebSocket upgrades</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5"><code>GHSA-36qx-fr4f-26g5</code></a></td>
<td>High</td>
<td>Middleware bypass in Pages Router i18n</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q"><code>GHSA-ffhc-5mcf-pf4q</code></a></td>
<td>Moderate</td>
<td>XSS via CSP nonces</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h"><code>GHSA-gx5p-jg67-6x7h</code></a></td>
<td>Moderate</td>
<td>XSS in <code>beforeInteractive</code> scripts</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh"><code>GHSA-h64f-5h5j-jqjh</code></a></td>
<td>Moderate</td>
<td>Denial of service in Image Optimization API</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7"><code>GHSA-wfc6-r584-vfw7</code></a></td>
<td>Moderate</td>
<td>Cache poisoning in RSC responses</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949"><code>GHSA-vfv6-92ff-j949</code></a></td>
<td>Low</td>
<td>Cache poisoning via RSC cache-busting collisions</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq"><code>GHSA-3g8h-86w9-wvmq</code></a></td>
<td>Low</td>
<td>Middleware redirect cache poisoning</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
</tbody>
</table>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 5</span><a class="pagination-next" rel="next" href="/changelog/product/waf/2/">Next</a></nav>
