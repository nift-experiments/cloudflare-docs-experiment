---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/waf/3/
  description: '2025-12-02'
  full_title: waf changelog - page 3 | Cloudflare Docs
  head_html: <title>waf changelog - page 3 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-12-02"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/waf/3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="waf changelog - page 3"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-12-02"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/waf/3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/waf/3/#page","headline":"waf changelog - page 3 | Cloudflare Docs","description":"2025-12-02","url":"https://developers.cloudflare.com/changelog/product/waf/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/waf/3/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="waf-release-2025-12-02-emergency"><a href="/changelog/post/2025-12-02-emergency-waf-release/">WAF Release - 2025-12-02 - Emergency</a></h2>
<p><em>2025-12-02</em></p>
<p>This week's emergency release introduces a new rule to block a critical RCE vulnerability in widely-used web frameworks through unsafe deserialization patterns.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for RCE Generic Framework to block malicious POST requests containing unsafe deserialization patterns. If successfully exploited, this vulnerability allows attackers with network access via HTTP to execute arbitrary code remotely.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Successful exploitation allows unauthenticated attackers to execute arbitrary code remotely through crafted serialization payloads, enabling complete system compromise, data exfiltration, and potential lateral movement within affected environments.</li>
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
				<code class="nb-rule-id" title="33aa8a8a948b48b28d40450c5fb92fba">5fb92fba</code>
</td>
<td>N/A</td>
<td>RCE Generic - Framework</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b5d06e34a814a889bee9a0699702280">99702280</code>
</td>
<td>N/A</td>
<td>RCE Generic - Framework</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-12-01"><a href="/changelog/post/2025-12-01-waf-release/">WAF Release - 2025-12-01</a></h2>
<p><em>2025-12-01</em></p>
<p>This week’s release introduces new detections for remote code execution attempts targeting Monsta FTP (CVE-2025-34299), alongside improvements to an existing XSS detection to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-34299 is a critical remote code execution flaw in Monsta FTP, arising from improper handling of user-supplied parameters within the file-handling interface. Certain builds allow crafted requests to bypass sanitization and reach backend PHP functions that execute arbitrary commands. Attackers can send manipulated parameters through the web panel to trigger command execution within the application’s runtime environment.</li>
</ul>
<p><strong>Impact</strong></p>
<p>If exploited, the vulnerability enables full remote command execution on the underlying server, allowing takeover of the hosting environment, unauthorized file access, and potential lateral movement. As the flaw can be triggered without authentication on exposed Monsta FTP instances, it represents a severe risk for publicly reachable deployments.</p>
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
				<code class="nb-rule-id" title="480da5e7984542a6b8d8d88da4fcc8a8">a4fcc8a8</code>
</td>
<td>N/A</td>
<td>Monsta FTP - Remote Code Execution - CVE:CVE-2025-34299</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2380b125c53d42ac94479c42b7492846">b7492846</code>
</td>
<td>N/A</td>
<td>XSS - JS Context Escape - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "XSS - JS Context Escape" (ID: <code class="nb-rule-id" title="c1ad1bc37caa4cbeb104f44f7a3769d3">7a3769d3</code>)</td>
</tr>  
</tbody>
</table>


<h2 id="waf-release-2025-11-24"><a href="/changelog/post/2025-11-24-waf-release/">WAF Release - 2025-11-24</a></h2>
<p><em>2025-11-24</em></p>
<p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in FortiWeb, linked to CVE-2025-64446, alongside new detection logic expanding protection against PHP Wrapper Injection techniques.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability enables an unauthenticated attacker to bypass access controls by abusing the <code>CGIINFO</code> header. The latest update strengthens detection logic to ensure a reliable identification of crafted requests attempting to exploit this flaw.</p>
<p><strong>Impact</strong></p>
<ul>
<li>FortiWeb (CVE-2025-64446): Exploitation allows a remote unauthenticated adversary to circumvent authentication mechanisms by sending a manipulated <code>CGIINFO</code> header to FortiWeb’s backend CGI handler. Successful exploitation grants unintended access to restricted administrative functionality, potentially enabling configuration tampering or system-level actions.</li>
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
				<code class="nb-rule-id" title="b957ace6e9844bf29244401c4e2e1a2e">4e2e1a2e</code>
</td>
<td>N/A</td>
<td>FortiWeb - Authentication Bypass via CGIINFO Header - CVE:CVE-2025-64446</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e3871391a93248fa98a78e03b6c44ed5">b6c44ed5</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - Body - Beta</td>
<td>Log</td>
<td>Disabled</td>
<td>This rule has been merged into the original rule "PHP Wrapper Injection - Body" (ID:<code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e6b1b66e0e3b46969102baed900f4015">900f4015</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - URI - Beta</td>
<td>Log</td>
<td>Disabled</td>
<td>This rule has been merged into the original rule "PHP Wrapper Injection - URI" (ID:<code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code>)</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-11-21"><a href="/changelog/post/2025-11-21-emergency-waf-release/">WAF Release - 2025-11-21</a></h2>
<p><em>2025-11-21</em></p>
<p>This week’s release introduces a critical detection for CVE-2025-61757, a vulnerability in the Oracle Identity Manager REST WebServices component.</p>
<p><strong>Key Findings</strong></p>
<p>This flaw allows unauthenticated attackers with network access over HTTP to fully compromise the Identity Manager, potentially leading to a complete takeover.</p>
<p><strong>Impact</strong></p>
<p>Oracle Identity Manager (CVE-2025-61757): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.</p>
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
				<code class="nb-rule-id" title="fa584616fe2241608cb8bd1339fdbe7e">39fdbe7e</code>
</td>
<td>N/A</td>
<td>Oracle Identity Manager - Pre-Auth RCE - CVE:CVE-2025-61757</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-11-17"><a href="/changelog/post/2025-11-17-waf-release/">WAF Release - 2025-11-17</a></h2>
<p><em>2025-11-17</em></p>
<p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in DELMIA Apriso, linked to CVE-2025-6205.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to gain privileged access to the application. The latest update provides enhanced detection logic for resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<ul>
<li>DELMIA Apriso (CVE-2025-6205): Exploitation could allow an unauthenticated remote attacker to bypass security checks by sending specially crafted requests to the application's message processor. This enables the creation of arbitrary employee accounts, which can be leveraged to modify system configurations and achieve full system compromise.</li>
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
				<code class="nb-rule-id" title="ec1e2aa190e64e7cb468e16dd256f4bc">d256f4bc</code>
</td>
<td>N/A</td>
<td>DELMIA Apriso - Auth Bypass - CVE:CVE-2025-6205</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code>
</td>
<td>N/A</td>
<td>PHP Wrapper Injection - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-11-10"><a href="/changelog/post/2025-11-10-waf-release/">WAF Release - 2025-11-10</a></h2>
<p><em>2025-11-10</em></p>
<p>This week’s release introduces new detections for Prototype Pollution across three common vectors: URI, Body, and Header/Form.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>These attacks can affect both API and web applications by altering normal behavior or bypassing security controls.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation may allow attackers to change internal logic or cause unexpected behavior in applications using JavaScript or Node.js frameworks. Developers should sanitize input keys and avoid merging untrusted data structures.</p>
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
				<code class="nb-rule-id" title="32405a50728746dd8caa057b606285e6">606285e6</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a7da00c63c4243d2a72456fe4f59ff26">4f59ff26</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="833078bdcfa04bb7aa7b8fb67efbeb39">7efbeb39</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - Header - Form</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>        
</tbody>
</table>


<h2 id="waf-release-2025-11-05-emergency"><a href="/changelog/post/2025-11-05-emergency-waf-release/">WAF Release - 2025-11-05 - Emergency</a></h2>
<p><em>2025-11-05</em></p>
<p>This week’s emergency release introduces a new detection signature that enhances coverage for a critical vulnerability in the React Native Metro Development Server, tracked as CVE-2025-11953.</p>
<p><strong>Key Findings</strong></p>
<p>The Metro Development Server exposes an HTTP endpoint that is vulnerable to OS command injection (CWE-78). An unauthenticated network attacker can send a crafted request to this endpoint and execute arbitrary commands on the host running Metro. The vulnerability affects Metro/cli-server-api builds used by React Native Community CLI in pre-patch development releases.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-11953 may result in remote command execution on developer workstations or CI/build agents, leading to credential and secret exposure, source tampering, and potential lateral movement into internal networks. Administrators and developers are strongly advised to apply the vendor's patches and restrict Metro’s network exposure to reduce this risk.</p>
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
        <code class="nb-rule-id" title="db6b9e1ac1494971ae8c70aac8e30c5b">c8e30c5b</code>
</td>
<td>N/A</td>
<td>React Native Metro - Command Injection - CVE:CVE-2025-11953</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-11-03"><a href="/changelog/post/2025-11-03-waf-release/">WAF Release - 2025-11-03</a></h2>
<p><em>2025-11-03</em></p>
<p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update provides enhanced detection logic for resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.</li>
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
				<code class="nb-rule-id" title="f5295d8333b7428c816654d8cb6d5fe5">cb6d5fe5</code>
</td>
<td>100774C</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236</td>
<td>Log</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-30-emergency"><a href="/changelog/post/2025-10-30-emergency-waf-release/">WAF Release - 2025-10-30 - Emergency</a></h2>
<p><em>2025-10-30</em></p>
<p>This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Oracle E-Business Suite, tracked as CVE-2025-61884.</p>
<p><strong>Key Findings</strong></p>
<p>The flaw is easily exploitable and allows an unauthenticated attacker with network access to compromise Oracle Configurator, which can grant access to sensitive resources and configuration data. The affected versions include 12.2.3 through 12.2.14.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-61884 may result in unauthorized access to critical business data or full exposure of information accessible through Oracle Configurator. Administrators are strongly advised to apply vendor's patches and recommended mitigations to reduce this exposure.</p>
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
        <code class="nb-rule-id" title="2749f13f8cb34a3dbd49c8c48827402f">8827402f</code>
</td>
<td>N/A</td>
<td>Oracle E-Business Suite - SSRF - CVE:CVE-2025-61884</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-24-emergency"><a href="/changelog/post/2025-10-24-emergency-waf-release/">WAF Release - 2025-10-24 - Emergency</a></h2>
<p><em>2025-10-24</em></p>
<p>This week’s release introduces a new detection signature that enhances coverage for a critical vulnerability in Windows Server Update Services (WSUS), tracked as CVE-2025-59287.</p>
<p><strong>Key Findings</strong></p>
<p>The vulnerability allows unauthenticated attackers to potentially achieve remote code execution. The updated detection logic strengthens defenses by improving resilience against exploitation attempts targeting this flaw.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-59287 could enable attackers to hijack sessions, execute arbitrary commands, exfiltrate sensitive data, and disrupt storefront operations. These actions pose significant confidentiality and integrity risks to affected environments. Administrators should apply vendor patches immediately to mitigate exposure.</p>
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
        <code class="nb-rule-id" title="5eaeb5ea6e5a4bce867eb3ffbd72ba08">bd72ba08</code>
</td>
<td>N/A</td>
<td>Windows Server - Deserialization - CVE:CVE-2025-59287</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-23-emergency"><a href="/changelog/post/2025-10-23-emergency-waf-release/">WAF Release - 2025-10-23 - Emergency</a></h2>
<p><em>2025-10-23</em></p>
<p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update enhances detection logic to provide more resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<p>Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.</p>
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
        <code class="nb-rule-id" title="6e04fa2b9eb34fb088034d3fc6ef59a1">c6ef59a1</code>
</td>
<td>N/A</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-20"><a href="/changelog/post/2025-10-20-waf-release/">WAF Release - 2025-10-20</a></h2>
<p><em>2025-10-20</em></p>
<p>This week’s update introduces an enhanced rule that expands detection coverage for a critical vulnerability in Oracle E-Business Suite. It also improves an existing rule to provide more reliable coverage in request processing.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for Oracle E-Business Suite (CVE-2025-61882) to block  unauthenticated attacker's network access via HTTP to compromise Oracle Concurrent Processing. If successfully exploited, this vulnerability may result in remote code execution.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Successful exploitation of CVE-2025-61882 allows unauthenticated attackers to execute arbitrary code remotely by chaining multiple weaknesses, enabling lateral movement into internal services, data exfiltration, and large-scale extortionware deployment within Oracle E-Business Suite environments.</li>
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
				<code class="nb-rule-id" title="933fc13202cd4e8ba498c0f32b4101ab">2b4101ab</code>
</td>
<td>100598A</td>
<td>Remote Code Execution - Common Bash Bypass - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Remote Code Execution - Common Bash Bypass" (ID: <code class="nb-rule-id" title="f8238867ed3e4d3a9a7b731a50cec478">50cec478</code>)</td>
</tr>         
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="185b5df42d1e44e0aeb8f8b8a1118614">a1118614</code>
</td>
<td>100916A</td>
<td>Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882 - 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="646bccf7e9dc46918a4150d6c22b51d3">c22b51d3</code>
</td>
<td>N/A</td>
<td>HTTP Truncated</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="new-detections-released-for-waf-managed-rulesets"><a href="/changelog/post/2025-10-17-emergency-waf-release/">New detections released for WAF managed rulesets</a></h2>
<p><em>2025-10-17</em></p>
<p>This week we introduced several new detections across Cloudflare Managed Rulesets, expanding coverage for high-impact vulnerability classes such as SSRF, SQLi, SSTI, Reverse Shell attempts, and Prototype Pollution. These rules aim to improve protection against attacker-controlled payloads that exploit misconfigurations or unvalidated input in web applications.</p>
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


<h2 id="waf-release-2025-10-13"><a href="/changelog/post/2025-10-13-waf-release/">WAF Release - 2025-10-13</a></h2>
<p><em>2025-10-13</em></p>
<p>This week’s highlights include a new JinJava rule targeting a sandbox-bypass flaw that could allow malicious template input to escape execution controls. The rule improves detection for unsafe template rendering paths.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for JinJava (CVE-2025-59340) to block a sandbox bypass in the template engine that permits attacker-controlled type construction and arbitrary class instantiation; in vulnerable environments this can escalate to remote code execution and full server compromise.</p>
<p><strong>Impact</strong></p>
<ul>
<li>CVE-2025-59340 — Exploitation enables attacker-supplied type descriptors / Jackson <code>ObjectMapper</code> abuse, allowing arbitrary class loading, file/URL access (LFI/SSRF primitives) and, with suitable gadget chains, potential remote code execution and system compromise.</li>
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
				<code class="nb-rule-id" title="b327d6442e2d4848b4aab3cbc04bab5f">c04bab5f</code>
</td>
<td>100892</td>
<td>JinJava - SSTI - CVE:CVE-2025-59340</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-07-emergency"><a href="/changelog/post/2025-10-07-emergency-waf-release/">WAF Release - 2025-10-07 - Emergency</a></h2>
<p><em>2025-10-07</em></p>
<p>This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device.
The initial two rules were made available on September 28, with a third rule added today, October 7, for more robust protection.</p>
<ul>
<li>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.
Administrators are strongly advised to apply vendor updates immediately.</p>
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
        <code class="nb-rule-id" title="12f808a5315441688f3b7c8a3a4d1bd6">3a4d1bd6</code>
</td>
<td>100788B</td>
<td>Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-10-06"><a href="/changelog/post/2025-10-06-waf-release/">WAF Release - 2025-10-06</a></h2>
<p><em>2025-10-06</em></p>
<p>This week’s highlights prioritise an emergency Oracle E-Business Suite RCE rule deployed to block active, high-impact exploitation. Also addressed are high-severity Chaos Mesh controller command-injection flaws that enable unauthenticated in-cluster RCE and potential cluster compromise, plus a form-data multipart boundary issue that permits HTTP Parameter Pollution (HPP). Two new generic SQLi detections were added to catch inline-comment obfuscation and information disclosure techniques.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>New emergency rule released for Oracle E-Business Suite (CVE-2025-61882) addressing an actively exploited remote code execution vulnerability in core business application modules. Immediate mitigation deployed to protect enterprise workloads.</p>
</li>
<li>
<p>Chaos Mesh (CVE-2025-59358,CVE-2025-59359,CVE-2025-59360,CVE-2025-59361): A GraphQL debug endpoint on the Chaos Controller Manager is exposed without authentication; several controller mutations (<code>cleanTcs</code>, <code>killProcesses</code>, <code>cleanIptables</code>) are vulnerable to OS command injection.</p>
</li>
<li>
<p>Form-Data (CVE-2025-7783): Attackers who can observe <code>Math.random()</code> outputs and control request fields in form-data may exploit this flaw to perform HTTP parameter pollution, leading to request tampering or data manipulation.</p>
</li>
<li>
<p>Two new generic SQLi detections added to enhance baseline coverage against inline-comment obfuscation and information disclosure attempts.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<ul>
<li>
<p>CVE-2025-61882 — Oracle E-Business Suite remote code execution (emergency detection): attacker-controlled input can yield full system compromise, data exfiltration, and operational outage; immediate blocking enforced.</p>
</li>
<li>
<p>CVE-2025-59358 / CVE-2025-59359 / CVE-2025-59360 / CVE-2025-59361 — Unauthenticated command-injection in Chaos Mesh controllers allowing remote code execution, cluster compromise, and service disruption (high availability risk).</p>
</li>
<li>
<p>CVE-2025-7783 — Predictable multipart boundaries in form-data enabling HTTP Parameter Pollution; results include request tampering, parameter overwrite, and downstream data integrity loss.</p>
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
        <code class="nb-rule-id" title="0c9bf31ab6fa41fc8f12daaf8650f52f">8650f52f</code>
</td>
<td>100882</td>
<td>Chaos Mesh - Missing Authentication - CVE:CVE-2025-59358</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5d459ed434ed446c9580c73c2b8c3680">2b8c3680</code>
</td>
<td>100883</td>
<td>Chaos Mesh - Command Injection - CVE:CVE-2025-59359</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a2591ba5befa4815a6861aefef859a04">ef859a04</code>
</td>
<td>100884</td>
<td>Chaos Mesh - Command Injection - CVE:CVE-2025-59361</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="05eea4fabf6f4cf3aac1094b961f26a7">961f26a7</code>
</td>
<td>100886</td>
<td>Form-Data - Parameter Pollution - CVE:CVE-2025-7783</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="90514c7810694b188f56979826a4074c">26a4074c</code>
</td>
<td>100888</td>
<td>Chaos Mesh - Command Injection - CVE:CVE-2025-59360</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="42fbc8c09ec84578b9633ffc31101b2f">31101b2f</code>
</td>
<td>100916</td>
<td>Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="badc687a3ba3420a844220b129aa43c3">29aa43c3</code>
</td>
<td>100917</td>
<td>Generic Rules - SQLi - Inline Comment Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="28fa27511f29428899ceb5a273c10b6f">73c10b6f</code>
</td>
<td>100918</td>
<td>Generic Rules - SQLi - Information Disclosure</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>                    
</tbody>
</table>


<h2 id="waf-release-2025-10-03"><a href="/changelog/post/2025-10-03-waf-release/">WAF Release - 2025-10-03</a></h2>
<p><em>2025-10-03</em></p>
<p><strong>Managed Ruleset Updated</strong></p>
<p>This update introduces 21 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.</p>
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
        <code class="nb-rule-id" title="0d02c2fb14eb4cec9c2e2b58d61fac74">d61fac74</code>
</td>
<td>100902</td>
<td>Generic Rules - Command Execution - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c3079865ce9a41368657026b514aeeb8">514aeeb8</code>
</td>
<td>100908</td>
<td>Generic Rules - Command Execution - 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="107ae2922b654bb28df7ca978d46a6f4">8d46a6f4</code>
</td>
<td>100910</td>
<td>Generic Rules - Command Execution - 4</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="68bdb75ae6d24e139a83e5731bd0a329">1bd0a329</code>
</td>
<td>100915</td>
<td>Generic Rules - Command Execution - 5</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ea04bb580f7d400386c7dc1d5e51450a">5e51450a</code>
</td>
<td>100899</td>
<td>Generic Rules - Content-Type Abuse</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="233364f656ff42b8acc41dcd7996012f">7996012f</code>
</td>
<td>100914</td>
<td>Generic Rules - Content-Type Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1aa695281c954513be3d003b93209312">93209312</code>
</td>
<td>100911</td>
<td>Generic Rules - Cookie Header Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d9f9e4f5bf11489da52dccb40f373b3f">0f373b3f</code>
</td>
<td>100905</td>
<td>Generic Rules - NoSQL Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5a1897b714e044a887c0f3f078a0ed04">78a0ed04</code>
</td>
<td>100913</td>
<td>Generic Rules - NoSQL Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4d6fd28df4f1494e95e70d2c5d649624">5d649624</code>
</td>
<td>100907</td>
<td>Generic Rules - Parameter Pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="61181e3af5304f7396c7d01cfd1c674e">fd1c674e</code>
</td>
<td>100906</td>
<td>Generic Rules - PHP Object Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ed5190bfbe1b45a6a645126334c88168">34c88168</code>
</td>
<td>100904</td>
<td>Generic Rules - Prototype Pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3ec33bc5ac77495a9f55020e3ab43f7e">3ab43f7e</code>
</td>
<td>100897</td>
<td>Generic Rules - Prototype Pollution 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c6d752c4909e4b7e8eff6c780d94ee22">0d94ee22</code>
</td>
<td>100903</td>
<td>Generic Rules - Reverse Shell</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="caf37e7800bb4635bcc2eefcd5add8e3">d5add8e3</code>
</td>
<td>100909</td>
<td>Generic Rules - Reverse Shell - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="475d090baead467c88dfabbb565c78b0">565c78b0</code>
</td>
<td>100898</td>
<td>Generic Rules - SSJI NoSQL</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="f4c7f98934264c9c937eec1212b837a0">12b837a0</code>
</td>
<td>100896</td>
<td>Generic Rules - SSRF</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="efd01b814d144e90b36522b311c4fb00">11c4fb00</code>
</td>
<td>100895</td>
<td>Generic Rules - Template Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="00a9a0d663da4add95b863abd3ed0123">d3ed0123</code>
</td>
<td>100895A</td>
<td>Generic Rules - Template Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e58c0fffee4f4374bd37f2577501a1d9">7501a1d9</code>
</td>
<td>100912</td>
<td>Generic Rules - XXE</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab09ba8d00eb4cdbb7a6a65ddc55cdb6">dc55cdb6</code>
</td>
<td>100900</td>
<td>Relative Paths - Anomaly Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-09-29"><a href="/changelog/post/2025-09-29-waf-release/">WAF Release - 2025-09-29</a></h2>
<p><em>2025-09-29</em></p>
<p>This week highlights four important vendor- and component-specific issues: an authentication bypass in SimpleHelp (CVE-2024-57727), an information-disclosure flaw in Flowise Cloud (CVE-2025-58434), an SSRF in the WordPress plugin Ditty (CVE-2025-8085), and a directory-traversal bug in Vite (CVE-2025-30208). These are paired with improvements to our generic detection coverage (SQLi, SSRF) to raise the baseline and reduce noisy gaps.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>SimpleHelp (CVE-2024-57727): Authentication bypass in SimpleHelp that can allow unauthorized access to management interfaces or sessions.</p>
</li>
<li>
<p>Flowise Cloud (CVE-2025-58434): Information-disclosure vulnerability in Flowise Cloud that may expose sensitive configuration or user data to unauthenticated or low-privileged actors.</p>
</li>
<li>
<p>WordPress:Plugin: Ditty (CVE-2025-8085): SSRF in the Ditty WordPress plugin enabling server-side requests that could reach internal services or cloud metadata endpoints.</p>
</li>
<li>
<p>Vite (CVE-2025-30208): Directory-traversal vulnerability in Vite allowing access to filesystem paths outside the intended web root.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities allow attackers to gain access, escalate privileges, or execute actions that were previously unavailable:</p>
<ul>
<li>
<p>SimpleHelp (CVE-2024-57727): An authentication bypass that can let unauthenticated attackers access management interfaces or hijack sessions — enabling lateral movement, credential theft, or privilege escalation within affected environments.</p>
</li>
<li>
<p>Flowise Cloud (CVE-2025-58434): Information-disclosure flaw that can expose sensitive configuration, tokens, or user data; leaked secrets may be chained into account takeover or privileged access to backend services.</p>
</li>
<li>
<p>WordPress:Plugin: Ditty (CVE-2025-8085): SSRF that enables server-side requests to internal services or cloud metadata endpoints, potentially allowing attackers to retrieve credentials or reach otherwise inaccessible infrastructure, leading to privilege escalation or cloud resource compromise.</p>
</li>
<li>
<p>Vite (CVE-2025-30208): Directory-traversal vulnerability that can expose filesystem contents outside the web root (configuration files, keys, source code), which attackers can use to escalate privileges or further compromise systems.</p>
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
        <code class="nb-rule-id" title="6fe90532af50427484a5275c8c2e30fb">8c2e30fb</code>
</td>
<td>100717</td>
<td>SimpleHelp - Auth Bypass - CVE:CVE-2024-57727</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged to 100717 in legacy WAF and <code class="nb-rule-id" title="498fcd81a62a4b5ca943e2de958094d3">958094d3</code> in new WAF</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="013ef5de3f074fd5a43cdd70d58b886b">d58b886b</code>
</td>
<td>100775</td>
<td>Flowise Cloud - Information Disclosure - CVE:CVE-2025-58434</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="68fc5c086ccb4b40a35a63b19bce1ff4">9bce1ff4</code>
</td>
<td>100881</td>
<td>WordPress:Plugin:Ditty - SSRF - CVE:CVE-2025-8085</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9e1a56e6b3bc49b187bf6e35ddc329dd">ddc329dd</code>
</td>
<td>100887</td>
<td>Vite - Directory Traversal - CVE:CVE-2025-30208</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-09-28-emergency"><a href="/changelog/post/2025-09-28-emergency-waf-release/">WAF Release - 2025-09-28 - Emergency</a></h2>
<p><em>2025-09-28</em></p>
<p>This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.</p>
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
        <code class="nb-rule-id" title="a1bef4ada0b146d2862cad439ee0ab84">9ee0ab84</code>
</td>
<td>100788</td>
<td>Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="51de6ce6596a40eb8200452ad30f768e">d30f768e</code>
</td>
<td>100788A</td>
<td>Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-09-26"><a href="/changelog/post/2025-09-26-waf-release/">WAF Release - 2025-09-26</a></h2>
<p><em>2025-09-26</em></p>
<p><strong>Managed Ruleset Updated</strong></p>
<p>This update introduces 11 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.</p>
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
        <code class="nb-rule-id" title="3ffd242b4ba242ca965022d3a67d8561">a67d8561</code>
</td>
<td>100859A</td>
<td>SQLi - UNION - 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="91d9cf56355b4ab88481b2fd4de80468">4de80468</code>
</td>
<td>100889</td>
<td>Command Injection - Generic 9</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c15ca8e8290f485287037665f2be3ddf">f2be3ddf</code>
</td>
<td>100890</td>
<td>Information Disclosure - Common Files - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="56669615f2984c2cac8c608980a252a8">80a252a8</code>
</td>
<td>100891</td>
<td>Anomaly:URL - Relative Paths</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c41789fb6370431d809567d17e7d3865">7e7d3865</code>
</td>
<td>100894</td>
<td>XSS - Inline Function</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b995d0b930604fa6b8d9b2a13792565c">3792565c</code>
</td>
<td>100895</td>
<td>XSS - DOM</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab8277e3f432400bbd9403dd42978e38">42978e38</code>
</td>
<td>100896</td>
<td>SQLi - MSSQL Length Enumeration</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3ec33bc5ac77495a9f55020e3ab43f7e">3ab43f7e</code>
</td>
<td>100897</td>
<td>Generic Rules - Code Injection - 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4375dc90c7af4c55908f6b95c1686741">c1686741</code>
</td>
<td>100898</td>
<td>SQLi - Evasion</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="945c5aa9f45141dd872d7ec920999be0">20999be0</code>
</td>
<td>100899</td>
<td>SQLi - Probing 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="2c20b5e8684043f48620ff77b4026c88">b4026c88</code>
</td>
<td>100900</td>
<td>SQLi - Probing</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-09-24-emergency"><a href="/changelog/post/2025-09-24-emergency-waf-release/">WAF Release - 2025-09-24 - Emergency</a></h2>
<p><em>2025-09-24</em></p>
<p>This week highlights a critical vendor-specific vulnerability: a deserialization flaw in the License Servlet of Fortra’s GoAnywhere MFT. By forging a license response signature, an attacker can trigger deserialization of arbitrary objects, potentially leading to command injection.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>GoAnywhere MFT (CVE-2025-10035): Deserialization vulnerability in the License Servlet that allows attackers with a forged license response signature to deserialize arbitrary objects, potentially resulting in command injection.</li>
</ul>
<p><strong>Impact</strong></p>
<p>GoAnywhere MFT (CVE-2025-10035): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.</p>
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
        <code class="nb-rule-id" title="8fe242c7c0d64d689f4fc9a1e08b39f3">e08b39f3</code>
</td>
<td>100787</td>
<td>Fortra GoAnywhere - Auth Bypass - CVE:CVE-2025-10035</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-09-22"><a href="/changelog/post/2025-09-22-waf-release/">WAF Release - 2025-09-22</a></h2>
<p><em>2025-09-22</em></p>
<p>This week emphasizes two critical vendor-specific vulnerabilities: a full elevation-of-privilege in Microsoft Azure Networking (CVE-2025-54914) and a server-side template injection (SSTI) leading to remote code execution (RCE) in Skyvern (CVE-2025-49619). These are complemented by enhancements in generic detections (SQLi, SSRF) to improve baseline coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Azure (CVE-2025-54914): Vulnerability in Azure Networking allowing elevation of privileges.</p>
</li>
<li>
<p>Skyvern (CVE-2025-49619): Skyvern ≤ 0.1.85 has a server-side template injection (SSTI) vulnerability in its Prompt field (workflow blocks) via Jinja2. Authenticated users with low privileges can get remote code execution (blind).</p>
</li>
<li>
<p>Generic SQLi / SSRF improvements: Expanded rule coverage to detect obfuscated SQL injection patterns and SSRF across host, local, and cloud contexts.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities allow attackers to escalate privileges or execute code under conditions where previously they could not:</p>
<ul>
<li>
<p>Azure CVE-2025-54914 enables an attacker from the network with no credentials to gain high-level access within Azure Networking; could lead to full compromise of networking components.</p>
</li>
<li>
<p>Skyvern CVE-2025-49619 allows authenticated users with minimal privilege to exploit SSTI for remote code execution, undermining isolation of workflow components.</p>
</li>
<li>
<p>The improvements for SQLi and SSRF reduce risk from common injection and request-based attacks.</p>
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
        <code class="nb-rule-id" title="c36a425ae0c94789a9bc34f06a135cbf">6a135cbf</code>
</td>
<td>100146</td>
<td>SSRF - Host - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="dfa84b0aed5a4b45b953a36a57035abf">57035abf</code>
</td>
<td>100146B</td>
<td>SSRF - Local - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="276073e60c7a4b4d91faba1fbbe18d50">bbe18d50</code>
</td>
<td>100146C</td>
<td>SSRF - Cloud - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="78c856218f2d40f4b5988c8c956c1961">956c1961</code>
</td>
<td>100714</td>
<td>Azure - Auth Bypass - CVE:CVE-2025-54914</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9f1c8d4cbf3848dbb940771bc5ced231">c5ced231</code>
</td>
<td>100758</td>
<td>Skyvern - Remote Code Execution - CVE:CVE-2025-49619</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6be7e7829f3b43c688e1ac4284a619a1">84a619a1</code>
</td>
<td>100773</td>
<td>Next.js - SSRF</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="0cc3f50216bf4b448210bcc3983ff2dd">983ff2dd</code>
</td>
<td>100774</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="53bfaeb311a049e3877fa15c0380a1a6">0380a1a6</code>
</td>
<td>100800_BETA</td>
<td>SQLi - Obfuscated Boolean - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule has been merged into the original rule (ID: <code class="nb-rule-id" title="7663ea44178441a0b3205c145563445f">5563445f</code>)</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-09-15"><a href="/changelog/post/2025-09-15-waf-release/">WAF Release - 2025-09-15</a></h2>
<p><em>2025-09-15</em></p>
<p><strong>This week's update</strong></p>
<p>This week's focus highlights newly disclosed vulnerabilities in DevOps tooling, data visualization platforms, and enterprise CMS solutions. These issues include sensitive information disclosure and remote code execution, putting organizations at risk of credential leakage, unauthorized access, and full system compromise.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Argo CD (CVE-2025-55190): Exposure of sensitive information could allow attackers to access credential data stored in configurations, potentially leading to compromise of Kubernetes workloads and secrets.</p>
</li>
<li>
<p>DataEase (CVE-2025-57773): Insufficient input validation enables JNDI injection and insecure deserialization, resulting in remote code execution (RCE). Successful exploitation grants attackers control over the application server.</p>
</li>
<li>
<p>Sitecore (CVE-2025-53694): A sensitive information disclosure flaw allows unauthorized access to confidential information stored in Sitecore deployments, raising the risk of data breaches and privilege escalation.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose organizations to serious risks, including credential theft, unauthorized access, and full system compromise. Argo CD's flaw may expose Kubernetes secrets, DataEase exploitation could give attackers remote execution capabilities, and Sitecore's disclosure issue increases the likelihood of sensitive data leakage and business impact.</p>
<p>Administrators are strongly advised to apply vendor patches immediately, rotate exposed credentials, and review access controls to mitigate these risks.</p>
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
        <code class="nb-rule-id" title="199cce9ab21e40bcb535f01b2ee2085f">2ee2085f</code>
</td>
<td>100646</td>
<td>Argo CD - Information Disclosure - CVE:CVE-2025-55190s</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e513bb21b6a44f9cbfcd2462f5e20788">f5e20788</code>
</td>
<td>100874</td>
<td>DataEase - JNDI injection - CVE:CVE-2025-57773</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="be097f5a71a04f27aa87b60d005a12fd">005a12fd</code>
</td>
<td>100880</td>
<td>Sitecore - Information Disclosure - CVE:CVE-2025-53694</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-09-08"><a href="/changelog/post/2025-09-08-waf-release/">WAF Release - 2025-09-08</a></h2>
<p><em>2025-09-08</em></p>
<p><strong>This week's update</strong></p>
<p>This week’s focus highlights newly disclosed vulnerabilities in web frameworks, enterprise applications, and widely deployed CMS plugins. The vulnerabilities include SSRF, authentication bypass, arbitrary file upload, and remote code execution (RCE), exposing organizations to high-impact risks such as unauthorized access, system compromise, and potential data exposure. In addition, security rule enhancements have been deployed to cover general command injection and server-side injection attacks, further strengthening protections.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Next.js (CVE-2025-57822): Improper handling of redirects in custom middleware can lead to server-side request forgery (SSRF) when user-supplied headers are forwarded. Attackers could exploit this to access internal services or cloud metadata endpoints. The issue has been resolved in versions 14.2.32 and 15.4.7. Developers using custom middleware should upgrade and verify proper redirect handling in <code>next()</code> calls.</p>
</li>
<li>
<p>ScriptCase (CVE-2025-47227, CVE-2025-47228): In the Production Environment extension in Netmake ScriptCase through 9.12.006 (23), two vulnerabilities allow attackers to reset admin accounts and execute system commands, potentially leading to full compromise of affected deployments.</p>
</li>
<li>
<p>Sar2HTML (CVE-2025-34030): In Sar2HTML version 3.2.2 and earlier, insufficient input sanitization of the plot parameter allows remote, unauthenticated attackers to execute arbitrary system commands. Exploitation could compromise the underlying server and its data.</p>
</li>
<li>
<p>Zhiyuan OA (CVE-2025-34040): An arbitrary file upload vulnerability exists in the Zhiyuan OA platform. Improper validation in the <code>wpsAssistServlet</code> interface allows unauthenticated attackers to upload crafted files via path traversal, which can be executed on the web server, leading to remote code execution.</p>
</li>
<li>
<p>WordPress:Plugin:InfiniteWP Client (CVE-2020-8772): A vulnerability in the InfiniteWP Client plugin allows attackers to perform restricted actions and gain administrative control of connected WordPress sites.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities could allow attackers to gain unauthorized access, execute malicious code, or take full control of affected systems. The Next.js SSRF flaw may expose internal services or cloud metadata endpoints to attackers. Exploitations of ScriptCase and Sar2HTML could result in remote code execution, administrative takeover, and full server compromise. In Zhiyuan OA, the arbitrary file upload vulnerability allows attackers to execute malicious code on the web server, potentially exposing sensitive data and applications. The authentication bypass in WordPress InfiniteWP Client enables attackers to gain administrative access, risking data exposure and unauthorized control of connected sites.</p>
<p>Administrators are strongly advised to apply vendor patches immediately, remove unsupported software, and review authentication and access controls to mitigate these risks.</p>
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
        <code class="nb-rule-id" title="7c5812a31fd94996b3299f7e963d7afc">963d7afc</code>
</td>
<td>100007D</td>
<td>Command Injection - Common Attack Commands Args</td>
<td>Log</td>
<td>Block</td>
<td>This rule has been merged into the original rule "Command Injection - Common Attack Commands" (ID: <code class="nb-rule-id" title="89557ce9b26e4d4dbf29e90c28345b9b">28345b9b</code>) for New WAF customers only.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cd528243d6824f7ab56182988230a75b">8230a75b</code>
</td>      
<td>100617</td>
<td>Next.js - SSRF - CVE:CVE-2025-57822</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="503b337dac5c409d8f833a6ba22dabf1">a22dabf1</code>
</td>
<td>100659_BETA</td>
<td>Common Payloads for Server-Side Template Injection - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Common Payloads for Server-Side Template Injection" (ID: <code class="nb-rule-id" title="21c7a963e1b749e7b1753238a28a42c4">a28a42c4</code>)</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6d24266148f24f5e9fa487f8b416b7ca">b416b7ca</code>
</td>
<td>100824B</td>
<td>CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 - 3</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="154b217c43d04f11a13aeff05db1fa6b">5db1fa6b</code>
</td>
<td>100848</td>
<td>ScriptCase - Auth Bypass - CVE:CVE-2025-47227</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cad6f1c8c6d44ef59929e6532c62d330">2c62d330</code>
</td>
<td>100849</td>
<td>ScriptCase - Command Injection - CVE:CVE-2025-47228</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e7464139fd3e44938b56716bef971afd">ef971afd</code>
</td>
<td>100872</td>
<td>WordPress:Plugin:InfiniteWP Client - Missing Authorization - CVE:CVE-2020-8772</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="0181ebb2cc234f2d863412e1bab19b0b">bab19b0b</code>
</td>
<td>100873</td>
<td>Sar2HTML - Command Injection - CVE:CVE-2025-34030</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="34d5c7c7b08b40eaad5b2bb3f24c0fbe">f24c0fbe</code>
</td>
<td>100875</td>
<td>Zhiyuan OA - Remote Code Execution - CVE:CVE-2025-34040</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>    
</tbody>
</table>


<h2 id="waf-release-2025-09-04-emergency"><a href="/changelog/post/2025-09-04-emergency-waf-release/">WAF Release - 2025-09-04 - Emergency</a></h2>
<p><em>2025-09-04</em></p>
<p><strong>This week's update</strong></p>
<p>This week, new critical vulnerabilities were disclosed in Sitecore’s Sitecore Experience Manager (XM), Sitecore Experience Platform (XP), specifically versions 9.0 through 9.3, and 10.0 through 10.4.
These flaws are caused by unsafe data deserialization and code reflection, leaving affected systems at high risk of exploitation.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-53690: Remote Code Execution through Insecure Deserialization</li>
<li>CVE-2025-53691: Remote Code Execution through Insecure Deserialization</li>
<li>CVE-2025-53693: HTML Cache Poisoning through Unsafe Reflections</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation could allow attackers to execute arbitrary code remotely on the affected system and conduct cache poisoning attacks, potentially leading to further compromise. Applying the latest vendor-released solution without delay is strongly recommended.</p>
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
        <code class="nb-rule-id" title="588edc74df1f4609b3c2f7ef0ee2c15e">0ee2c15e</code>
</td>
<td>100878</td>
<td>Sitecore - Remote Code Execution - CVE:CVE-2025-53691</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d1bd7563e6254db48ce703807c5b669c">7c5b669c</code>
</td>
<td>100631</td>
<td>Sitecore - Cache Poisoning - CVE:CVE-2025-53693</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ed94c7ce5301411a94a21a096c410240">6c410240</code>
</td>
<td>100879</td>
<td>Sitecore - Remote Code Execution - CVE:CVE-2025-53690</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
</tbody>
</table>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/waf/2/">Previous</a><span>Page 3 of 5</span><a class="pagination-next" rel="next" href="/changelog/product/waf/4/">Next</a></nav>
