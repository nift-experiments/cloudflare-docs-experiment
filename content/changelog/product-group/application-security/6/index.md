---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/application-security/6/
  description: '2025-10-06'
  full_title: Application security changelog - page 6 | Cloudflare Docs
  head_html: <title>Application security changelog - page 6 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-10-06"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/application-security/6/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Application security changelog - page 6"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-10-06"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/application-security/6/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/application-security/6/#page","headline":"Application security changelog - page 6 | Cloudflare Docs","description":"2025-10-06","url":"https://developers.cloudflare.com/changelog/product-group/application-security/6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/application-security/6/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

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


<h2 id="connect-and-secure-any-private-or-public-app-by-hostname-not-ip-with-hostname-routing-for-cloudflare-tunnel"><a href="/changelog/post/2025-09-18-tunnel-hostname-routing/">Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel</a></h2>
<p><em>2025-09-18</em></p>
<p>You can now route private traffic to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is <strong>free for all Cloudflare One customers</strong>.</p>
<p>Previously, Tunnel routes could only be defined by IP address or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">CIDR range</a>. This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/tunnel-hostname-routing.webp" alt="Hostname-based routing in Cloudflare Tunnel" /></p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Hostname &amp; Domain Routing</strong>: Create routes for individual hostnames (e.g., <code>payroll.acme.local</code>) or entire domains (e.g., <code>*.acme.local</code>) and direct their traffic to a specific Tunnel.</li>
<li><strong>Simplified Zero Trust Policies</strong>: Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.</li>
<li><strong>Precise Egress Control</strong>: Route traffic for public hostnames (e.g., <code>bank.example.com</code>) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.</li>
<li><strong>No More IP Lists</strong>: This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.</li>
</ul>
<p>Get started in the Tunnels section of the Zero Trust dashboard with your first <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> or <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> route.</p>
<p>Learn more in our <a href="https://blog.cloudflare.com/tunnel-hostname-routing/">blog post</a>.</p>


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


<h2 id="cloudflare-tunnel-and-networks-api-will-no-longer-return-deleted-resources-by-default-starting-december-1-2025"><a href="/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/">Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</a></h2>
<p><em>2025-09-02</em></p>
<p>Starting <strong>December 1, 2025</strong>, list endpoints for the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.</p>
<p>No action is required if you already explicitly set <code>is_deleted=false</code> or if you only need to list active resources.</p>
<p>This change affects the following API endpoints:</p>
<ul>
<li>List all tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/methods/list/"><code>GET /accounts/{account_id}/tunnels</code></a></li>
<li>List <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels</a>: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a></li>
<li>List <a href="/mesh/">WARP Connector</a> tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a></li>
<li>List tunnel routes: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/"><code>GET /accounts/{account_id}/teamnet/routes</code></a></li>
<li>List subnets: <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/"><code>GET /accounts/{account_id}/zerotrust/subnets</code></a></li>
<li>List virtual networks: <a href="/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/"><code>GET /accounts/{account_id}/teamnet/virtual_networks</code></a></li>
</ul>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-what-is-changing">What is changing?</h4>
<p>The default behavior of the <code>is_deleted</code> query parameter will be updated.</p>
<table>
<thead>
<tr>
<th align="left">Scenario</th>
<th align="left">Previous behavior (before December 1, 2025)</th>
<th align="left">New behavior (from December 1, 2025)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>is_deleted</code> parameter is omitted</td>
<td align="left">Returns <strong>active &amp; deleted</strong> tunnels, routes, subnets and virtual networks</td>
<td align="left">Returns <strong>only active</strong> tunnels, routes, subnets and virtual networks</td>
</tr>
</tbody>
</table>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-action-required">Action required</h4>
<p>If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the <code>is_deleted</code> parameter before <strong>December 1, 2025</strong>.</p>
<p>To get a list of only deleted resources, you must now explicitly add the <code>is_deleted=true</code> query parameter to your request:</p>
<pre tabindex="0"><code class="language-bash">&#35; Example: Get ONLY deleted Tunnels&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Example: Get ONLY deleted Virtual Networks&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using <code>is_deleted=false</code>) and one to get deleted items (<code>is_deleted=true</code>).</p>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-why-we-re-making-this-change">Why we’re making this change</h4>
This update is based on user feedback and aims to:
* **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
* **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
* **Improve performance:** For most users, the default query result will now be smaller and more relevant.
<p>To learn more, please visit the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> documentation.</p>


<h2 id="waf-release-2025-09-01"><a href="/changelog/post/2025-09-01-waf-release/">WAF Release - 2025-09-01</a></h2>
<p><em>2025-09-01</em></p>
<p><strong>This week's update</strong></p>
<p>This week, a critical vulnerability was disclosed in Fortinet FortiWeb (versions 7.6.3 and below, versions 7.4.7 and below, versions 7.2.10 and below, and versions 7.0.10 and below), linked to improper parameter handling that could allow unauthorized access.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Fortinet FortiWeb (CVE-2025-52970): A vulnerability may allow an unauthenticated remote attacker with access to non-public information to log in as any existing user on the device via a specially crafted request.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation could allow an unauthenticated attacker to impersonate any existing user on the device, potentially enabling them to modify system settings or exfiltrate sensitive information, posing a serious security risk. Upgrading to the latest vendor-released version is strongly recommended.</p>
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
        <code class="nb-rule-id" title="636b145a49a84946b990d4fac49b7cf8">c49b7cf8</code>
</td>
<td>100586</td>
<td>Fortinet FortiWeb - Auth Bypass - CVE:CVE-2025-52970</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b5ef1ace353841a0856b5e07790c9dde">790c9dde</code>
</td>
<td>100136C</td>
<td>XSS - JavaScript - Headers and Body</td>
<td>N/A</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-08-29-emergency"><a href="/changelog/post/2025-08-29-emergency-waf-release/">WAF Release - 2025-08-29 - Emergency</a></h2>
<p><em>2025-08-29</em></p>
<p><strong>This week's update</strong></p>
<p>This week, new critical vulnerabilities were disclosed in Next.js’s image optimization functionality, exposing a broad range of production environments to risks of data exposure and cache manipulation.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2025-55173: Arbitrary file download from the server via image optimization.</p>
</li>
<li>
<p>CVE-2025-57752: Cache poisoning leading to unauthorized data disclosure.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation could expose sensitive files, leak user or backend data, and undermine application trust. Given Next.js’s wide use, immediate patching and cache hardening are strongly advised.</p>
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
        <code class="nb-rule-id" title="ea55f8aac44246cc9b827eea9ff4bfe3">9ff4bfe3</code>
</td>
<td>100613</td>
<td>Next.js - Dangerous File Download - CVE:CVE-2025-55173</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e2b2d77a79cc4a76bf7ba53d69b9ea7d">69b9ea7d</code>
</td>
<td>100616</td>
<td>Next.js - Information Disclosure - CVE:CVE-2025-57752</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
</tbody>
</table>


<h2 id="manage-and-deploy-your-ai-provider-keys-through-bring-your-own-key-byok-with-ai-gateway-now-powered-by-cloudflare-secrets-store"><a href="/changelog/post/2025-08-25-secrets-store-ai-gateway/">Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</a></h2>
<p><em>2025-08-25T11:00:00+00:00</em></p>
<p>Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through <a href="https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Key</a>. Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.</p>
<p>You can now create a secret directly from your AI Gateway <a href="http://dash.cloudflare.com/?to=/:account/ai-gateway">in the dashboard</a> by navigating into your gateway -&gt; <strong>Provider Keys</strong> -&gt; <strong>Add</strong>.</p>
<p><img src="/assets/upstream/images/ssl/add-secret-ai-gateway.png" alt="Import repo or choose template" /></p>
<p>You can also create your secret with the newly available <strong>ai_gateway</strong> scope via <a href="https://developers.cloudflare.com/workers/wrangler/commands/">wrangler</a>, the <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">Secrets Store dashboard</a>, or the <a href="https://developers.cloudflare.com/api/resources/secrets_store/">API</a>.</p>
<p>Then, pass the key in the request header using its Secrets Store reference:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic/v1/messages \&#10; &#45;-header &#x27;cf-aig-authorization: ANTHROPIC_KEY_1 \&#10; &#45;-header &#x27;anthropic-version: 2023-06-01&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-data  &#x27;{&quot;model&quot;: &quot;claude-3-opus-20240229&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Or, using Javascript:</p>
<pre tabindex="0"><code>import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;&#10;const anthropic = new Anthropic({&#10; apiKey: &quot;ANTHROPIC_KEY_1&quot;,&#10; baseURL: &quot;https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic&quot;,&#10;});&#10;&#10;&#10;const message = await anthropic.messages.create({&#10; model: &#x27;claude-3-opus-20240229&#x27;,&#10; messages: [{role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot;}],&#10; max_tokens: 1024&#10;});&#10;</code></pre>
<p>For more information, check out the <a href="https://blog.cloudflare.com/ai-gateway-aug-2025-refresh">blog</a>!</p>


<h2 id="waf-release-2025-08-25"><a href="/changelog/post/2025-08-25-waf-release/">WAF Release - 2025-08-25</a></h2>
<p><em>2025-08-25</em></p>
<p><strong>This week's update</strong></p>
<p>This week, critical vulnerabilities were disclosed that impact widely used open-source infrastructure, creating high-risk scenarios for code execution and operational disruption.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Apache HTTP Server – Code Execution (CVE-2024-38474): A flaw in Apache HTTP Server allows attackers to achieve remote code execution, enabling full compromise of affected servers. This vulnerability threatens the confidentiality, integrity, and availability of critical web services.</p>
</li>
<li>
<p>Laravel (CVE-2024-55661): A security flaw in Laravel introduces the potential for remote code execution under specific conditions. Exploitation could provide attackers with unauthorized access to application logic and sensitive backend data.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities pose severe risks to enterprise environments and open-source ecosystems. Remote code execution enables attackers to gain deep system access, steal data, disrupt services, and establish persistent footholds for broader intrusions. Given the widespread deployment of Apache HTTP Server and Laravel in production systems, timely patching and mitigation are critical.</p>
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
        <code class="nb-rule-id" title="c550282a0f7343ca887bdab528050359">28050359</code>
</td>
<td>100822_BETA</td>
<td>WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058</td>
<td>N/A</td>
<td>Disabled</td>
<td>This was merged in to the original rule "WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058" (ID: <code class="nb-rule-id" title="9b5c5e13d2ca4253a89769f2194f7b2d">194f7b2d</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="456b1e8f827b4ed89fb4a54b3bdcdbad">3bdcdbad</code>
</td>
<td>100831</td>
<td>Apache HTTP Server - Code Execution - CVE:CVE-2024-38474</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7dcc01e1dd074e42a26c8ca002eaac5b">02eaac5b</code>
</td>
<td>100846</td>
<td>Laravel - Remote Code Execution - CVE:CVE-2024-55661</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-08-22"><a href="/changelog/post/2025-08-22-waf-release/">WAF Release - 2025-08-22</a></h2>
<p><em>2025-08-22</em></p>
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
        <code class="nb-rule-id" title="0f3b6b9377334707b604be925fcca5c8">5fcca5c8</code>
</td>
<td>100850</td>
<td>Command Injection - Generic 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="36b0532eb3c941449afed2d3744305c4">744305c4</code>
</td>
<td>100851</td>
<td>Remote Code Execution - Java Deserialization</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5d3c0d0958d14512bd2a7d902b083459">2b083459</code>
</td>
<td>100852</td>
<td>Command Injection - Generic 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6e2f7a696ea74c979e7d069cefb7e5b9">efb7e5b9</code>
</td>
<td>100853</td>
<td>Remote Code Execution - Common Bash Bypass Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="735666d7268545a5ae6cfd0b78513ad7">78513ad7</code>
</td>
<td>100854</td>
<td>XSS - Generic JavaScript</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="82780ba6f5df49dcb8d09af0e9a5daac">e9a5daac</code>
</td>
<td>100855</td>
<td>Command Injection - Generic 4</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8e305924a7dc4f91a2de931a480f6093">480f6093</code>
</td>
<td>100856</td>
<td>PHP Object Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1d34e0d05c10473ca824e66fd4ae0a33">d4ae0a33</code>
</td>
<td>100857</td>
<td>Generic - Parameter Fuzzing</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b517e4b79d7a47fbb61f447b1121ee45">1121ee45</code>
</td>
<td>100858</td>
<td>Code Injection - Generic 4</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1f9accf629dc42cb84a7a14420de01e3">20de01e3</code>
</td>
<td>100859</td>
<td>SQLi - UNION - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e95939eacf7c4484b47101d5c0177e21">c0177e21</code>
</td>
<td>100860</td>
<td>Command Injection - Generic 5</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7b426e6f456043f4a21c162085f4d7b3">85f4d7b3</code>
</td>
<td>100861</td>
<td>Command Execution - Generic</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5fac82bd1c03463fb600cfa83fa8ee7f">3fa8ee7f</code>
</td>
<td>100862</td>
<td>GraphQL Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab2cb1f2e2ad4da6a2685b1dc7a41d4b">c7a41d4b</code>
</td>
<td>100863</td>
<td>Command Injection - Generic 6</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="549b4fe1564a448d848365d565e3c165">65e3c165</code>
</td>
<td>100864</td>
<td>Code Injection - Generic 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8ef3c3f91eef46919cc9cb6d161aafdc">161aafdc</code>
</td>
<td>100865</td>
<td>PHP Object Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="57e8ba867e6240d2af8ea0611cc3c3f8">1cc3c3f8</code>
</td>
<td>100866</td>
<td>SQLi - LIKE 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a967a167874b42b6898be46e48ac2221">48ac2221</code>
</td>
<td>100867</td>
<td>SQLi - DROP - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cf79a868cc934bcc92b86ff01f4eec13">1f4eec13</code>
</td>
<td>100868</td>
<td>Code Injection - Generic 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="97a52405eaae47ae9627dbb22755f99e">2755f99e</code>
</td>
<td>100869</td>
<td>Command Injection - Generic 7</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5b3ce84c099040c6a25cee2d413592e2">413592e2</code>
</td>
<td>100870</td>
<td>Command Injection - Generic 8</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5940a9ace2f04d078e35d435d2dd41b5">d2dd41b5</code>
</td>
<td>100871</td>
<td>SQLi - LIKE 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-08-18"><a href="/changelog/post/2025-08-18-waf-release/">WAF Release - 2025-08-18</a></h2>
<p><em>2025-08-18</em></p>
<p><strong>This week's update</strong></p>
<p>This week, a series of critical vulnerabilities were discovered impacting core enterprise and open-source infrastructure. These flaws present a range of risks, providing attackers with distinct pathways for remote code execution, methods to breach internal network boundaries, and opportunities for critical data exposure and operational disruption.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>SonicWall SMA (CVE-2025-32819, CVE-2025-32820, CVE-2025-32821): A remote authenticated attacker with SSLVPN user privileges can bypass path traversal protections. These vulnerabilities enable a attacker to bypass security checks to read, modify, or delete arbitrary files. An attacker with administrative privileges can escalate this further, using a command injection flaw to upload malicious files, which could ultimately force the appliance to reboot to its factory default settings.</p>
</li>
<li>
<p>Ms-Swift Project (CVE-2025-50460): An unsafe deserialization vulnerability exists in the Ms-Swift project's handling of YAML configuration files. If an attacker can control the content of a configuration file passed to the application, they can embed a malicious payload that will execute arbitrary code and it can be executed during deserialization.</p>
</li>
<li>
<p>Apache Druid (CVE-2023-25194): This vulnerability in Apache Druid allows an attacker to cause the server to connect to a malicious LDAP server. By sending a specially crafted LDAP response, the attacker can trigger an unrestricted deserialization of untrusted data. If specific &quot;gadgets&quot; (classes that can be abused) are present in the server's classpath, this can be escalated to achieve Remote Code Execution (RCE).</p>
</li>
<li>
<p>Tenda AC8v4 (CVE-2025-51087, CVE-2025-51088): Vulnerabilities allow an authenticated attacker to trigger a stack-based buffer overflow. By sending malformed arguments in a request to specific endpoints, an attacker can crash the device or potentially achieve arbitrary code execution.</p>
</li>
<li>
<p>Open WebUI (CVE-2024-7959): This vulnerability allows a user to change the OpenAI URL endpoint to an arbitrary internal network address without proper validation. This flaw can be exploited to access internal services or cloud metadata endpoints, potentially leading to remote command execution if the attacker can retrieve instance secrets or access sensitive internal APIs.</p>
</li>
<li>
<p>BentoML (CVE-2025-54381): The vulnerability exists in the serialization/deserialization handlers for multipart form data and JSON requests, which automatically download files from user-provided URLs without proper validation of internal network addresses. This allows attackers to fetch from unintended internal services, including cloud metadata and localhost.</p>
</li>
<li>
<p>Adobe Experience Manager Forms (CVE-2025-54254): An Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could lead to arbitrary file system read in Adobe AEM (≤6.5.23).</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities affect core infrastructure, from network security appliances like SonicWall to data platforms such as Apache Druid and ML frameworks like BentoML. The code execution and deserialization flaws are particularly severe, offering deep system access that allows attackers to steal data, disrupt services, and establish a foothold for broader intrusions. Simultaneously, SSRF and XXE vulnerabilities undermine network boundaries, exposing sensitive internal data and creating pathways for lateral movement. Beyond data-centric threats, flaws in edge devices like the Tenda router introduce the tangible risk of operational disruption, highlighting a multi-faceted threat to the security and stability of key enterprise systems.</p>
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
        <code class="nb-rule-id" title="326ebb56d46a4c269bb699d3418d9a3b">418d9a3b</code>
</td>
<td>100574</td>
<td>SonicWall SMA - Remote Code Execution - CVE:CVE-2025-32819, CVE:CVE-2025-32820, CVE:CVE-2025-32821</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="69f4f161dec04aca8a73a3231e6fefdb">1e6fefdb</code>
</td>
<td>100576</td>
<td>Ms-Swift Project - Remote Code Execution - CVE:CVE-2025-50460</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d62935357ff846d9adefb58108ac45b3">08ac45b3</code>
</td>
<td>100585</td>
<td>Apache Druid - Remote Code Execution - CVE:CVE-2023-25194</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4f6148a760804bf8ad8ebccfe4855472">e4855472</code>
</td>
<td>100834</td>
<td>Tenda AC8v4 - Auth Bypass - CVE:CVE-2025-51087, CVE:CVE-2025-51088</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1474121b01ba40629f8246f8022ab542">022ab542</code>
</td>
<td>100835</td>
<td>Open WebUI - SSRF - CVE:CVE-2024-7959</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="96abffdb7e224ce69ddf89eb6339f132">6339f132</code>
</td>
<td>100837</td>
<td>SQLi - OOB</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a0b20ec638d14800a1d6827cb83d2625">b83d2625</code>
</td>
<td>100841</td>
<td>BentoML - SSRF - CVE:CVE-2025-54381</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="40fd793035c947c5ac75add1739180d2">739180d2</code>
</td>
<td>100841A</td>
<td>BentoML - SSRF - CVE:CVE-2025-54381 - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="08dcb20b9acf47e3880a0b886ab910c2">6ab910c2</code>
</td>
<td>100841B</td>
<td>BentoML - SSRF - CVE:CVE-2025-54381 - 3</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="309cfb7eeb42482e9ad896f12197ec51">2197ec51</code>
</td>
<td>100845</td>
<td>Adobe Experience Manager Forms - XSS - CVE:CVE-2025-54254</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6e039776c2d6418ab6e8f05196f34ce3">96f34ce3</code>
</td>
<td>100845A</td>
<td>Adobe Experience Manager Forms - XSS - CVE:CVE-2025-54254 - 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="save-time-with-bulk-query-creation-in-brand-protection"><a href="/changelog/post/2025-08-15-brand-protection-bulk-endpoint/">Save time with bulk query creation in Brand Protection</a></h2>
<p><em>2025-08-15</em></p>
<p><a href="/security-center/brand-protection/">Brand Protection</a> detects domains that may be impersonating your brand — from common misspellings (<code>cloudfalre.com</code>) to malicious concatenations (<code>cloudflare-okta.com</code>). Saved search queries run continuously and alert you when suspicious domains appear.</p>
<p>You can now create and save multiple queries in a single step, streamlining setup and management. Available now via the <a href="/api/resources/brand_protection/subresources/queries/methods/bulk/">Brand Protection bulk query creation API</a>.</p>


<h2 id="waf-release-2025-08-11"><a href="/changelog/post/2025-08-11-waf-release/">WAF Release - 2025-08-11</a></h2>
<p><em>2025-08-11</em></p>
<p>This week's update focuses on a wide range of enterprise software, from network infrastructure and security platforms to content management systems and development frameworks. Flaws include unsafe deserialization, OS command injection, SSRF, authentication bypass, and arbitrary file upload — many of which allow unauthenticated remote code execution. Notable risks include Cisco Identity Services Engine and Ivanti EPMM, where successful exploitation could grant attackers full administrative control of core network infrastructure and popular web services such as WordPress, SharePoint, and Ingress-Nginx, where security bypasses and arbitrary file uploads could lead to complete site or server compromise.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Cisco Identity Services Engine (CVE-2025-20281): Insufficient input validation in a specific API of Cisco Identity Services Engine (ISE) and ISE-PIC allows an unauthenticated, remote attacker to execute arbitrary code with root privileges on an affected device.</p>
</li>
<li>
<p>Wazuh Server (CVE-2025-24016): An unsafe deserialization vulnerability in Wazuh Server (versions 4.4.0 to 4.9.0) allows for remote code execution and privilege escalation. By injecting unsanitized data, an attacker can trigger an exception to execute arbitrary code on the server.</p>
</li>
<li>
<p>CrushFTP (CVE-2025-54309): A flaw in AS2 validation within CrushFTP allows remote attackers to gain administrative access via HTTPS on systems not using the DMZ proxy feature. This flaw can lead to unauthorized file access and potential system compromise.</p>
</li>
<li>
<p>Kentico Xperience CMS (CVE-2025-2747, CVE-2025-2748): Vulnerabilities in Kentico Xperience CMS could enable cross-site scripting (XSS), allowing attackers to inject malicious scripts into web pages. Additionally, a flaw could allow unauthenticated attackers to bypass the Staging Sync Server's authentication, potentially leading to administrative control over the CMS.</p>
</li>
<li>
<p>Node.js (CVE-2025-27210): An incomplete fix for a previous vulnerability (CVE-2025-23084) in Node.js affects the <code>path.join()</code> API method on Windows systems. The vulnerability can be triggered using reserved Windows device names such as <code>CON</code>, <code>PRN</code>, or <code>AUX</code>.</p>
</li>
<li>
<p>WordPress:Plugin:Simple File List (CVE-2025-34085, CVE-2020-36847):
This vulnerability in the Simple File List plugin for WordPress allows an unauthenticated remote attacker to upload arbitrary files to a vulnerable site. This can be exploited to achieve remote code execution on the server.<br/>
(Note: CVE-2025-34085 has been rejected as a duplicate.)</p>
</li>
<li>
<p>GeoServer (CVE-2024-29198): A Server-Side Request Forgery (SSRF) vulnerability exists in GeoServer's Demo request endpoint, which can be exploited where the Proxy Base URL has not been configured.</p>
</li>
<li>
<p>Ivanti EPMM (CVE-2025-6771): An OS command injection vulnerability in Ivanti Endpoint Manager Mobile (EPMM) before versions 12.5.0.2, 12.4.0.3, and 12.3.0.3 allows a remote, authenticated attacker with high privileges to execute arbitrary code.</p>
</li>
<li>
<p>Microsoft SharePoint (CVE-2024-38018): This is a remote code execution vulnerability affecting Microsoft SharePoint Server.</p>
</li>
<li>
<p>Manager-IO (CVE-2025-54122): A critical unauthenticated full read Server-Side Request Forgery (SSRF) vulnerability is present in the proxy handler of both Manager Desktop and Server editions up to version 25.7.18.2519. This allows an unauthenticated attacker to bypass network isolation and access internal services.</p>
</li>
<li>
<p>Ingress-Nginx (CVE-2025-1974): A vulnerability in the Ingress-Nginx controller for Kubernetes allows an attacker to bypass access control rules. An unauthenticated attacker with access to the pod network can achieve arbitrary code execution in the context of the ingress-nginx controller.</p>
</li>
<li>
<p>PaperCut NG/MF (CVE-2023-2533): A Cross-Site Request Forgery (CSRF) vulnerability has been identified in PaperCut NG/MF. Under specific conditions, an attacker could exploit this to alter security settings or execute arbitrary code if they can deceive an administrator with an active login session into clicking a malicious link.</p>
</li>
<li>
<p>SonicWall SMA (CVE-2025-40598): This vulnerability could allow an unauthenticated attacker to bypass security controls. This allows a remote, unauthenticated attacker to potentially execute arbitrary JavaScript code.</p>
</li>
<li>
<p>WordPress (CVE-2025-5394): The &quot;Alone – Charity Multipurpose Non-profit WordPress Theme&quot; for WordPress  is vulnerable to arbitrary file uploads. A missing capability check allows unauthenticated attackers to upload ZIP files containing webshells disguised as plugins, leading to remote code execution.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities span a broad range of enterprise technologies, including network access control systems, monitoring platforms, web servers, CMS platforms, cloud services, and collaboration tools. Exploitation techniques range from remote code execution and command injection to authentication bypass, SQL injection, path traversal, and configuration weaknesses.</p>
<p>A critical flaw in perimeter devices like Ivanti EPMM or SonicWall SMA could allow an unauthenticated attacker to gain remote code execution, completely breaching the primary network defense. A separate vulnerability within Cisco's Identity Services Engine could then be exploited to bypass network segmentation, granting an attacker widespread internal access. Insecure deserialization issues in platforms like Wazuh Server and CrushFTP could then be used to run malicious payloads or steal sensitive files from administrative consoles. Weaknesses in web delivery controllers like Ingress-Nginx or popular content management systems such as WordPress, SharePoint, and Kentico Xperience create vectors to bypass security controls, exfiltrate confidential data, or fully compromise servers.</p>
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
        <code class="nb-rule-id" title="ec6480c81253494b947d891e51bc8df1">51bc8df1</code>
</td>
<td>100538</td>
<td>GeoServer - SSRF - CVE:CVE-2024-29198</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b8cb07170b5e4c2b989119cac9e0b290">c9e0b290</code>
</td>
<td>100548</td>
<td>Ivanti EPMM - Remote Code Execution - CVE:CVE-2025-6771</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b3524bf5f5174b65bc892122ad93cda8">ad93cda8</code>
</td>
<td>100550</td>
<td>Microsoft SharePoint - Remote Code Execution - CVE:CVE-2024-38018</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e1369c5d629f4f10a14141381dca5738">1dca5738</code>
</td>
<td>100562</td>
<td>Manager-IO - SSRF - CVE:CVE-2025-54122</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="136f67e2b6a84f15ab9a82a52e9137e1">2e9137e1</code>
</td>
<td>100565</td>
<td>
        Cisco Identity Services Engine - Remote Code Execution -
        CVE:CVE-2025-20281
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ed759f7e44184fa398ef71785d8102e1">5d8102e1</code>
</td>
<td>100567</td>
<td>Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1974</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="71b8e7b646f94d79873213cd99105c43">99105c43</code>
</td>
<td>100569</td>
<td>PaperCut NG/MF - Remote Code Execution - CVE:CVE-2023-2533</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="2450bfbb0cfb4804b109d1c42c81dc88">2c81dc88</code>
</td>
<td>100571</td>
<td>SonicWall SMA - XSS - CVE:CVE-2025-40598</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8ce1903b67e24205a93f5fe6926c96d4">926c96d4</code>
</td>
<td>100573</td>
<td>WordPress - Dangerous File Upload - CVE:CVE-2025-5394</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7fdb3c7bc7b74703aeef4ab240ec2fda">40ec2fda</code>
</td>   
<td>100806</td>      
<td>Wazuh Server - Remote Code Execution - CVE:CVE-2025-24016</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="fe088163f51f4928a3c8d91e2401fa3b">2401fa3b</code>
</td>
<td>100824</td>
<td>CrushFTP - Remote Code Execution - CVE:CVE-2025-54309</td>
<td>Log</td>
<td>Block</td>      
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3638baed75924604987b86d874920ace">74920ace</code>
</td>
<td>100824A</td>
<td>CrushFTP - Remote Code Execution - CVE:CVE-2025-54309 - 2</td>
<td>Log</td>
<td>Block</td>      
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="dda4f95b3a3e4ebb9e194aa5c7e63549">c7e63549</code>
</td>
<td>100825</td>
<td>AMI MegaRAC - Auth Bypass - CVE:CVE-2024-54085</td>
<td>Log</td>
<td>Block</td> 
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7dc07014cefa4ce9adf21da7b79037e6">b79037e6</code>
</td>
<td>100826</td>
<td>Kentico Xperience CMS - Auth Bypass - CVE:CVE-2025-2747</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7c7a0a37e79a4949ba840c9acaf261aa">caf261aa</code>
</td>
<td>100827</td>
<td>Kentico Xperience CMS - XSS - CVE:CVE-2025-2748</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="54dd826f578c483196ce852b6f1c2d12">6f1c2d12</code>
</td>
<td>100828</td>
<td>Node.js - Directory Traversal - CVE:CVE-2025-27210</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a2867f7456c14213a94509a40341fccc">0341fccc</code>
</td>
<td>100829</td>
<td>
        WordPress:Plugin:Simple File List - Remote Code Execution -
        CVE:CVE-2025-34085
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4cdb0e792d1a428a897526624cefeeda">4cefeeda</code>
</td>
<td>100829A</td>
<td>
        WordPress:Plugin:Simple File List - Remote Code Execution -
        CVE:CVE-2025-34085 - 2
</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-08-07-emergency"><a href="/changelog/post/2025-08-07-emergency-waf-release/">WAF Release - 2025-08-07 - Emergency</a></h2>
<p><em>2025-08-07</em></p>
<p>This week’s highlight focuses on two critical vulnerabilities affecting key infrastructure and enterprise content management platforms. Both flaws present significant remote code execution risks that can be exploited with minimal or no user interaction.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Squid (≤6.3) — CVE-2025-54574: A heap buffer overflow occurs when processing Uniform Resource Names (URNs). This vulnerability may allow remote attackers to execute arbitrary code on the server. The issue has been resolved in version 6.4.</p>
</li>
<li>
<p>Adobe AEM (≤6.5.23) — CVE-2025-54253: Due to a misconfiguration, attackers can achieve remote code execution without requiring any user interaction, posing a severe threat to affected deployments.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Both vulnerabilities expose critical attack vectors that can lead to full server compromise. The Squid heap buffer overflow allows remote code execution by crafting malicious URNs, which can lead to server takeover or denial of service. Given Squid’s widespread use as a caching proxy, this flaw could be exploited to disrupt network traffic or gain footholds inside secure environments.</p>
<p>Adobe AEM’s remote code execution vulnerability enables attackers to run arbitrary code on the content management server without any user involvement. This puts sensitive content, application integrity, and the underlying infrastructure at extreme risk. Exploitation could lead to data theft, defacement, or persistent backdoor installation.</p>
<p>These findings reinforce the urgency of updating to the patched versions — Squid 6.4 and Adobe AEM 6.5.24 or later — and reviewing configurations to prevent exploitation.</p>
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
        <code class="nb-rule-id" title="f61ed7c1e7e24c3380289e41ef7e015b">ef7e015b</code>
</td>
<td>100844</td>
<td>Adobe Experience Manager Forms - Remote Code Execution - CVE:CVE-2025-54253</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e76e65f5a3aa43f49e0684a6baec057a">baec057a</code>
</td>
<td>100840</td>
<td>Squid - Buffer Overflow - CVE:CVE-2025-54574</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-08-04"><a href="/changelog/post/2025-08-04-waf-release/">WAF Release - 2025-08-04</a></h2>
<p><em>2025-08-04</em></p>
<p>This week's highlight focuses on a series of significant vulnerabilities identified across widely adopted web platforms, from enterprise-grade CMS to essential backend administration tools. The findings reveal multiple vectors for attack, including critical flaws that allow for full server compromise and others that enable targeted attacks against users.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Sitecore (CVE-2025-34509, CVE-2025-34510, CVE-2025-34511): A hardcoded credential allows remote attackers to access administrative APIs. Once authenticated, they can exploit an additional vulnerability to upload arbitrary files, leading to remote code execution.</p>
</li>
<li>
<p>Grafana (CVE-2025-4123): A cross-site scripting (XSS) vulnerability allows an attacker to redirect users to a malicious website, which can then execute arbitrary JavaScript in the victim's browser.</p>
</li>
<li>
<p>LaRecipe (CVE-2025-53833): Through Server-Side Template Injection, attackers can execute arbitrary commands on the server, potentially access sensitive environment variables, and escalate access depending on server configuration.</p>
</li>
<li>
<p>CentOS WebPanel (CVE-2025-48703): A command injection vulnerability could allow a remote attacker to execute arbitrary commands on the server.</p>
</li>
<li>
<p>WordPress (CVE-2023-5561): This vulnerability allows unauthenticated attackers to determine the email addresses of users who have published public posts on an affected website.</p>
</li>
<li>
<p>WordPress Plugin - WPBookit (CVE-2025-6058): A missing file type validation allows unauthenticated attackers to upload arbitrary files to the server, creating the potential for remote code execution.</p>
</li>
<li>
<p>WordPress Theme - Motors (CVE-2025-4322): Due to improper identity validation, an unauthenticated attacker can change the passwords of arbitrary users, including administrators, to gain access to their accounts.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities pose a multi-layered threat to widely adopted web technologies, ranging from enterprise-grade platforms like Sitecore to everyday solutions such as WordPress, and backend tools like CentOS WebPanel. The most severe risks originate in remote code execution (RCE) flaws found in Sitecore, CentOS WebPanel, LaRecipe, and the WPBookit plugin. These allow attackers to bypass security controls and gain deep access to the server, enabling them to steal sensitive data, deface websites, install persistent malware, or use the compromised server as a launchpad for further attacks.</p>
<p>The privilege escalation vulnerability is the Motors theme, which allows for a complete administrative account takeover on WordPress sites. This effectively hands control of the application to an attacker, who can then manipulate content, exfiltrate user data, and alter site functionality without needing to breach the server itself.</p>
<p>The Grafana cross-site scripting (XSS) flaw can be used to hijack authenticated user sessions or steal credentials, turning a trusted user's browser into an attack vector.</p>
<p>Meanwhile, the information disclosure flaw in WordPress core provides attackers with valid user emails, fueling targeted phishing campaigns that aim to secure the same account access achievable through the other exploits.</p>
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
        <code class="nb-rule-id" title="b8ab4644f8044f3485441ee052f30a13">52f30a13</code>
</td>
<td>100535A</td>
<td>Sitecore - Dangerous File Upload - CVE:CVE-2025-34510, CVE:CVE-2025-34511</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="06d1fe0bd6e44d868e6b910b5045a97f">5045a97f</code>
</td>
<td>100535</td>
<td>Sitecore - Information Disclosure - CVE:CVE-2025-34509</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="f71ce87ea6e54eab999223df579cd3e0">579cd3e0</code>
</td>
<td>100543</td>
<td>Grafana - Directory Traversal - CVE:CVE-2025-4123</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="bba3d37891a440fb8bc95b970cbd9abc">0cbd9abc</code>
</td>
<td>100545</td>
<td>WordPress - Information Disclosure - CVE:CVE-2023-5561</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="28108d25f1cf470c8e7648938f634977">8f634977</code>
</td>
<td>100820</td>
<td>CentOS WebPanel - Remote Code Execution - CVE:CVE-2025-48703</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9d69c796a61444a3aca33dc282ae64c1">82ae64c1</code>
</td>
<td>100821</td>
<td>LaRecipe - SSTI - CVE:CVE-2025-53833</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9b5c5e13d2ca4253a89769f2194f7b2d">194f7b2d</code>
</td>
<td>100822</td>
<td>WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="69d43d704b0641898141a4300bf1b661">0bf1b661</code>
</td>
<td>100823</td>
<td>WordPress:Theme:Motors - Privilege Escalation - CVE:CVE-2025-4322</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="deploy-to-cloudflare-buttons-now-support-worker-environment-variables-secrets-and-secrets-store-secrets"><a href="/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/">Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets</a></h2>
<p><em>2025-07-29T01:00:00+00:00</em></p>
<p>Any template which uses <a href="/workers/configuration/environment-variables/">Worker environment variables</a>, <a href="/workers/configuration/secrets/">secrets</a>, or <a href="/secrets-store/">Secrets Store secrets</a> can now be deployed using a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare button</a>.</p>
<p>Define environment variables and secrets store bindings in your Wrangler configuration file as normal:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17781.md")</div>
<p>Add secrets to a <code>.dev.vars.example</code> or <code>.env.example</code> file:</p>
<pre tabindex="0"><code class="language-ini">COOKIE_SIGNING_KEY=my-secret # comment&#10;</code></pre>
<p>And optionally, you can add a description for these bindings in your template's <code>package.json</code> to help users understand how to configure each value:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;private&quot;: true,&#10;	&quot;cloudflare&quot;: {&#10;		&quot;bindings&quot;: {&#10;			&quot;API_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Select your company&#x27;s API key for connecting to the example service.&quot;&#10;			},&#10;			&quot;COOKIE_SIGNING_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Generate a random string using `openssl rand -hex 32`.&quot;&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in <a href="/workers/platform/deploy-buttons/">our documentation</a>.</p>


<h2 id="waf-release-2025-07-28"><a href="/changelog/post/2025-07-28-waf-release/">WAF Release - 2025-07-28</a></h2>
<p><em>2025-07-28</em></p>
<p>This week’s update spotlights several vulnerabilities across Apache Tomcat, MongoDB, and Fortinet FortiWeb. Several flaws related with a memory leak in Apache Tomcat can lead to a denial-of-service attack. Additionally, a code injection flaw in MongoDB's Mongoose library allows attackers to bypass security controls to access restricted data.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Fortinet FortiWeb (CVE-2025-25257): An improper neutralization of special elements used in a SQL command vulnerability in Fortinet FortiWeb versions allows an unauthenticated attacker to execute unauthorized SQL code or commands.</p>
</li>
<li>
<p>Apache Tomcat (CVE-2025-31650): A improper Input Validation vulnerability in Apache Tomcat that could create memory leak when incorrect error handling for some invalid HTTP priority headers resulted in incomplete clean-up of the failed request.</p>
</li>
<li>
<p>MongoDB (CVE-2024-53900, CVE:CVE-2025-23061): Improper use of <code>$where</code> in match and a nested <code>$where</code> filter with a <code>populate()</code> match in Mongoose can lead to search injection.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities target user-facing components, web application servers, and back-end databases. A SQL injection flaw in Fortinet FortiWeb can lead to data theft or system compromise. A separate issue in Apache Tomcat involves a memory leak from improper input validation, which could be exploited for a denial-of-service (DoS) attack. Finally, a vulnerability in MongoDB's Mongoose library allows attackers to bypass security filters and access unauthorized data through malicious search queries.</p>
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
				<code class="nb-rule-id" title="6ab3bd3b58fb4325ac2d3cc73461ec9e">3461ec9e</code>
</td>
<td>100804</td>
<td>BerriAI - SSRF - CVE:CVE-2024-6587</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e6c4d02f42a4c3ca90649d50cb13e1d">0cb13e1d</code>
</td>
<td>100812</td>
<td>Fortinet FortiWeb - Remote Code Execution - CVE:CVE-2025-25257</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fd360d8fd9994e6bab6fb06067fae7f7">67fae7f7</code>
</td>
<td>100813</td>
<td>Apache Tomcat - DoS - CVE:CVE-2025-31650</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f9e01e28c5d6499cac66364b4b6a5bb1">4b6a5bb1</code>
</td>
<td>100815</td>
<td>MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="700d4fcc7b1f481a80cbeee5688f8e79">688f8e79</code>
</td>
<td>100816</td>
<td>MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-07-21-emergency"><a href="/changelog/post/2025-07-21-emergency/">WAF Release - 2025-07-21 - Emergency</a></h2>
<p><em>2025-07-21</em></p>
<p>This week's update highlights several high-impact vulnerabilities affecting Microsoft SharePoint Server. These flaws, involving unsafe deserialization, allow unauthenticated remote code execution over the network, posing a critical threat to enterprise environments relying on SharePoint for collaboration and document management.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Microsoft SharePoint Server (CVE-2025-53770): A critical vulnerability involving unsafe deserialization of untrusted data, enabling unauthenticated remote code execution over the network. This flaw allows attackers to execute arbitrary code on vulnerable SharePoint servers without user interaction.</li>
<li>Microsoft SharePoint Server (CVE-2025-53771): A closely related deserialization issue that can be exploited by unauthenticated attackers, potentially leading to full system compromise. The vulnerability highlights continued risks around insecure serialization logic in enterprise collaboration platforms.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Together, these vulnerabilities significantly weaken the security posture of on-premise Microsoft SharePoint Server deployments. By enabling remote code execution without authentication, they open the door for attackers to gain persistent access, deploy malware, and move laterally across enterprise environments.</p>
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
					<code class="nb-rule-id" title="34dac2b38b904163bc587cc32168f6f0">2168f6f0</code>
</td>
<td>100817</td>
<td>Microsoft SharePoint - Deserialization - CVE:CVE-2025-53770</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
 					<code class="nb-rule-id" title="d21f327516a145bc9d1b05678de656c4">8de656c4</code>
</td>
<td>100818</td>
<td>Microsoft SharePoint - Deserialization - CVE:CVE-2025-53771</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
<p>For more details, also refer to <a href="https://blog.cloudflare.com/cloudflare-protects-against-critical-sharepoint-vulnerability-cve-2025-53770/">our blog</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-security/5/">Previous</a><span>Page 6 of 9</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-security/7/">Next</a></nav>
