---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/waf/4/
  description: '2025-09-01'
  full_title: waf changelog - page 4 | Cloudflare Docs
  head_html: <title>waf changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-09-01"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/waf/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="waf changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-09-01"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/waf/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/waf/4/#page","headline":"waf changelog - page 4 | Cloudflare Docs","description":"2025-09-01","url":"https://developers.cloudflare.com/changelog/product/waf/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/waf/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

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


<h2 id="waf-release-2025-07-21"><a href="/changelog/post/2025-07-21-waf-release/">WAF Release - 2025-07-21</a></h2>
<p><em>2025-07-21</em></p>
<p>This week's update spotlights several critical vulnerabilities across Citrix NetScaler Memory Disclosure, FTP servers and network application. Several flaws enable unauthenticated remote code execution or sensitive data exposure, posing a significant risk to enterprise security.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Wing FTP Server (CVE-2025-47812): A critical Remote Code Execution (RCE) vulnerability that enables unauthenticated attackers to execute arbitrary code with root/SYSTEM-level privileges by exploiting a Lua injection flaw.</li>
<li>Infoblox NetMRI (CVE-2025-32813): A remote unauthenticated command injection flaw that allows an attacker to execute arbitrary commands, potentially leading to unauthorized access.</li>
<li>Citrix Netscaler ADC (CVE-2025-5777, CVE-2023-4966): A sensitive information disclosure vulnerability, also known as &quot;Citrix Bleed2&quot;, that allows the disclosure of memory and subsequent remote access session hijacking.</li>
<li>Akamai CloudTest (CVE-2025-49493): An XML External Entity (XXE) injection that could lead to read local files on the system by manipulating XML input.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities affect critical enterprise infrastructure, from file transfer services and network management appliances to application delivery controllers. The Wing FTP RCE and Infoblox command injection flaws offer direct paths to deep system compromise, while the Citrix &quot;Bleed2&quot; and Akamai XXE vulnerabilities undermine system integrity by enabling session hijacking and sensitive data theft.</p>
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
<td>Log</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0e17d8761f1a47d5a744a75b5199b58a">5199b58a</code>
</td>
<td>100805</td>
<td>Wing FTP Server - Remote Code Execution - CVE:CVE-2025-47812</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="81ace5a851214a2f9c58a1e7919a91a4">919a91a4</code>
</td>
<td>100807</td>
<td>Infoblox NetMRI - Command Injection - CVE:CVE-2025-32813</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="cd8fa74e8f6f476c9380ae217899130f">7899130f</code>
</td>
<td>100808</td>
<td>Citrix Netscaler ADC - Buffer Error - CVE:CVE-2025-5777</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e012c7bece304a1daf80935ed1cf8e08">d1cf8e08</code>
</td>
<td>100809</td>
<td>Citrix Netscaler ADC - Information Disclosure - CVE:CVE-2023-4966</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5d348a573a834ffd968faffc6e70469f">6e70469f</code>
</td>
<td>100810</td>
<td>Akamai CloudTest - XXE - CVE:CVE-2025-49493</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-07-14"><a href="/changelog/post/2025-07-14-waf-release/">WAF Release - 2025-07-14</a></h2>
<p><em>2025-07-14</em></p>
<p>This week’s vulnerability analysis highlights emerging web application threats that exploit modern JavaScript behavior and SQL parsing ambiguities. Attackers continue to refine techniques such as attribute overloading and obfuscated logic manipulation to evade detection and compromise front-end and back-end systems.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>XSS – Attribute Overloading: A novel cross-site scripting technique where attackers abuse custom or non-standard HTML attributes to smuggle payloads into the DOM. These payloads evade traditional sanitization logic, especially in frameworks that loosely validate attributes or trust unknown tokens.</li>
<li>XSS – onToggle Event Abuse: Exploits the lesser-used onToggle event (triggered by elements like <code>&lt;details&gt; </code>) to execute arbitrary JavaScript when users interact with UI elements. This vector is often overlooked by static analyzers and can be embedded in seemingly benign components.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities target both user-facing components and back-end databases, introducing potential vectors for credential theft, session hijacking, or full data exfiltration. The XSS variants bypass conventional filters through overlooked HTML behaviors, while the obfuscated SQLi enables attackers to stealthily probe back-end logic, making them especially difficult to detect and block.</p>
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
				<code class="nb-rule-id" title="a8918353372b4191b10684eb2aa3d845">2aa3d845</code>
</td>
<td>100798</td>
<td>XSS - Attribute Overloading</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="31dd299ba375414dac9260c037548d06">37548d06</code>
</td>
<td>100799</td>
<td>XSS - OnToggle</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="increased-ip-list-limits-for-enterprise-accounts"><a href="/changelog/post/2025-07-07-increased-ip-list-limits/">Increased IP List Limits for Enterprise Accounts</a></h2>
<p><em>2025-07-07</em></p>
<p>We have significantly increased the limits for <a href="/waf/tools/lists/">IP Lists</a> on Enterprise plans to provide greater flexibility and control:</p>
<ul>
<li><strong>Total number of lists</strong>: Increased from 10 to 1,000.</li>
<li><strong>Total number of list items</strong>: Increased from 10,000 to 500,000.</li>
</ul>
<p>Limits for other list types and plans remain unchanged. For more details, refer to the <a href="/waf/tools/lists/#availability">lists availability</a>.</p>


<h2 id="waf-release-2025-07-07"><a href="/changelog/post/2025-07-07-waf-release/">WAF Release - 2025-07-07</a></h2>
<p><em>2025-07-07</em></p>
<p>This week’s roundup uncovers critical vulnerabilities affecting enterprise VoIP systems, webmail platforms, and a popular JavaScript framework. The risks range from authentication bypass to remote code execution (RCE) and buffer handling flaws, each offering attackers a path to elevate access or fully compromise systems.</p>
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


<h2 id="waf-release-2025-06-16"><a href="/changelog/post/2025-06-16-waf-release/">WAF Release - 2025-06-16</a></h2>
<p><em>2025-06-16</em></p>
<p>This week’s roundup highlights multiple critical vulnerabilities across popular web frameworks, plugins, and enterprise platforms. The focus lies on remote code execution (RCE), server-side request forgery (SSRF), and insecure file upload vectors that enable full system compromise or data exfiltration.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Cisco IOS XE (CVE-2025-20188): Critical RCE vulnerability enabling unauthenticated attackers to execute arbitrary commands on network infrastructure devices, risking total router compromise.</li>
<li>Axios (CVE-2024-39338): SSRF flaw impacting server-side request control, allowing attackers to manipulate internal service requests when misconfigured with unsanitized user input.</li>
<li>vBulletin (CVE-2025-48827, CVE-2025-48828): Two high-impact RCE flaws enabling attackers to remotely execute PHP code, compromising forum installations and underlying web servers.</li>
<li>Invision Community (CVE-2025-47916): A critical RCE vulnerability allowing authenticated attackers to run arbitrary code in community platforms, threatening data and lateral movement risk.</li>
<li>CrushFTP (CVE-2025-32102, CVE-2025-32103): SSRF vulnerabilities in upload endpoint processing permit attackers to pivot internal network scans and abuse internal services.</li>
<li>Roundcube (CVE-2025-49113): RCE via email processing enables attackers to execute code upon viewing a crafted email — particularly dangerous for webmail deployments.</li>
<li>WooCommerce WordPress Plugin (CVE-2025-47577): Dangerous file upload vulnerability permits unauthenticated users to upload executable payloads, leading to full WordPress site takeover.</li>
<li>Cross-Site Scripting (XSS) Detection Improvements: Enhanced detection patterns.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities span core systems — from routers to e-commerce to email. RCE in Cisco IOS XE, Roundcube, and vBulletin poses full system compromise. SSRF in Axios and CrushFTP supports internal pivoting, while WooCommerce’s file upload bug opens doors to mass WordPress exploitation.</p>
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
				<code class="nb-rule-id" title="233bcf0ce50f400989a7e44a35fefd53">35fefd53</code>
</td>
<td>100783</td>
<td>Cisco IOS XE - Remote Code Execution - CVE:CVE-2025-20188</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9284e3b1586341acb4591bfd8332af5d">8332af5d</code>
</td>
<td>100784</td>
<td>Axios - SSRF - CVE:CVE-2024-39338</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2672b175a25548aa8e0107b12e1648d2">2e1648d2</code>
</td>
<td>100785</td>
<td>
				vBulletin - Remote Code Execution - CVE:CVE-2025-48827,
				CVE:CVE-2025-48828
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b77a19fb053744b49eacdab00edcf1ef">0edcf1ef</code>
</td>
<td>100786</td>
<td>Invision Community - Remote Code Execution - CVE:CVE-2025-47916</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="aec2274743064523a9667248d6f5eb48">d6f5eb48</code>
</td>
<td>100791</td>
<td>CrushFTP - SSRF - CVE:CVE-2025-32102, CVE:CVE-2025-32103</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7b80e1f5575d4d99bb7d56ae30baa18a">30baa18a</code>
</td>
<td>100792</td>
<td>Roundcube - Remote Code Execution - CVE:CVE-2025-49113</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="52d76f9394494b0382c7cb00229ba236">229ba236</code>
</td>
<td>100793</td>
<td>XSS - Ontoggle</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d38e657bd43f4d809c28157dfa338296">fa338296</code>
</td>
<td>100794</td>
<td>
				WordPress WooCommerce Plugin - Dangerous File Upload -
				CVE:CVE-2025-47577
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-06-09"><a href="/changelog/post/2025-06-09-waf-release/">WAF Release - 2025-06-09</a></h2>
<p><em>2025-06-09</em></p>
<p>This week’s update spotlights four critical vulnerabilities across CMS platforms, VoIP systems, and enterprise applications. Several flaws enable remote code execution or privilege escalation, posing significant enterprise risks.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>WordPress OttoKit Plugin (CVE-2025-27007): Privilege escalation flaw allows unauthenticated attackers to create or elevate user accounts, compromising WordPress administrative control.</li>
<li>SAP NetWeaver (CVE-2025-42999): Remote Code Execution vulnerability enables attackers to execute arbitrary code on SAP NetWeaver systems, threatening core ERP and business operations.</li>
<li>Fortinet FortiVoice (CVE-2025-32756): Buffer error vulnerability may lead to memory corruption and potential code execution, directly impacting enterprise VoIP infrastructure.</li>
<li>Camaleon CMS (CVE-2024-46986): Remote Code Execution vulnerability allows attackers to gain full control over Camaleon CMS installations, exposing hosted content and underlying servers.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities target widely deployed CMS, ERP, and VoIP systems. RCE flaws in SAP NetWeaver and Camaleon CMS allow full takeover of business-critical applications. Privilege escalation in OttoKit exposes WordPress environments to full administrative compromise. FortiVoice buffer handling issues risk destabilizing or fully compromising enterprise telephony systems.</p>
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
				<code class="nb-rule-id" title="4afd50a3ef1948bba87c4e620debd86e">0debd86e</code>
</td>
<td>100769</td>
<td>
				WordPress OttoKit Plugin - Privilege Escalation - CVE:CVE-2025-27007
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="24134c41c3e940daa973b4b95f57b448">5f57b448</code>
</td>
<td>100770</td>
<td>SAP NetWeaver - Remote Code Execution - CVE:CVE-2025-42999</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4f219ac0be3545a5be5f0bf34df8857a">4df8857a</code>
</td>
<td>100779</td>
<td>Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bc8dfbe8cbac4c039725ec743b840107">3b840107</code>
</td>
<td>100780</td>
<td>Camaleon CMS - Remote Code Execution - CVE:CVE-2024-46986</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-06-02"><a href="/changelog/post/2025-06-02-waf-release/">WAF Release - 2025-06-02</a></h2>
<p><em>2025-06-02</em></p>
<p>This week’s roundup highlights five high-risk vulnerabilities affecting SD-WAN, load balancers, and AI platforms. Several flaws enable unauthenticated remote code execution or authentication bypass.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Versa Concerto SD-WAN (CVE-2025-34026, CVE-2025-34027): Authentication bypass vulnerabilities allow attackers to gain unauthorized access to SD-WAN management interfaces, compromising network segmentation and control.</li>
<li>Kemp LoadMaster (CVE-2024-7591): Remote Code Execution vulnerability enables attackers to execute arbitrary commands, potentially leading to full device compromise within enterprise load balancing environments.</li>
<li>AnythingLLM (CVE-2024-0759): Server-Side Request Forgery (SSRF) flaw allows external attackers to force the LLM backend to make unauthorized internal network requests, potentially exposing sensitive internal resources.</li>
<li>Anyscale Ray (CVE-2023-48022): Remote Code Execution vulnerability affecting distributed AI workloads, allowing attackers to execute arbitrary code on Ray cluster nodes.</li>
<li>Server-Side Request Forgery (SSRF) - Generic &amp; Obfuscated Payloads: Ongoing advancements in SSRF payload techniques observed, including obfuscation and expanded targeting of cloud metadata services and internal IP ranges.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose critical infrastructure across networking, AI platforms, and SaaS integrations. Unauthenticated RCE and auth bypass flaws in Versa Concerto, Kemp LoadMaster, and Anyscale Ray allow full system compromise. AnythingLLM and SSRF payload variants expand attack surfaces into internal cloud resources, sensitive APIs, and metadata services, increasing risk of privilege escalation, data theft, and persistent access.</p>
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
				<code class="nb-rule-id" title="752cfb5e6f9c46f0953c742139b52f02">39b52f02</code>
</td>
<td>100764</td>
<td>Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34027</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a01171de18034901b48a5549a34edb97">a34edb97</code>
</td>
<td>100765</td>
<td>Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34026</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="840b35492a7543c18ffe50fc0d99b2db">0d99b2db</code>
</td>
<td>100766</td>
<td>Kemp LoadMaster - Remote Code Execution - CVE:CVE-2024-7591</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="121b7070de3a459dbe80d7ed95aa3a4f">95aa3a4f</code>
</td>
<td>100767</td>
<td>AnythingLLM - SSRF - CVE:CVE-2024-0759</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="215417f989e2485a9c50eca0840a0966">840a0966</code>
</td>
<td>100768</td>
<td>Anyscale Ray - Remote Code Execution - CVE:CVE-2023-48022</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3ed619a17d4141bda3a8c3869d16ee18">9d16ee18</code>
</td>
<td>100781</td>
<td>SSRF - Generic Payloads</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7ce73f6a70be49f8944737465c963d9d">5c963d9d</code>
</td>
<td>100782</td>
<td>SSRF - Obfuscated Payloads</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="updated-attack-score-model"><a href="/changelog/post/2025-05-28-updated-attack-score-model/">Updated attack score model</a></h2>
<p><em>2025-05-28</em></p>
<p>We have deployed an updated attack score model focused on enhancing the detection of multiple false positives (FPs).</p>
<p>As a result of this improvement, some changes in observed attack scores are expected.</p>


<h2 id="waf-release-2025-05-27"><a href="/changelog/post/2025-05-27-waf-release/">WAF Release - 2025-05-27</a></h2>
<p><em>2025-05-27</em></p>
<p>This week’s roundup covers nine vulnerabilities, including six critical RCEs and one dangerous file upload. Affected platforms span cloud services, CI/CD pipelines, CMSs, and enterprise backup systems. Several are now addressed by updated WAF managed rulesets.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Ingress-Nginx (CVE-2025-1098): Unauthenticated RCE via unsafe annotation handling. Impacts Kubernetes clusters.</li>
<li>GitHub Actions (CVE-2025-30066): RCE through malicious workflow inputs. Targets CI/CD pipelines.</li>
<li>Craft CMS (CVE-2025-32432): Template injection enables unauthenticated RCE. High risk to content-heavy sites.</li>
<li>F5 BIG-IP (CVE-2025-31644): RCE via TMUI exploit, allowing full system compromise.</li>
<li>AJ-Report (CVE-2024-15077): RCE through untrusted template execution. Affects reporting dashboards.</li>
<li>NAKIVO Backup (CVE-2024-48248): RCE via insecure script injection. High-value target for ransomware.</li>
<li>SAP NetWeaver (CVE-2025-31324): Dangerous file upload flaw enables remote shell deployment.</li>
<li>Ivanti EPMM (CVE-2025-4428, 4427): Auth bypass allows full access to mobile device management.</li>
<li>Vercel (CVE-2025-32421): Information leak via misconfigured APIs. Useful for attacker recon.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose critical components across Kubernetes, CI/CD pipelines, and enterprise systems to severe threats including unauthenticated remote code execution, authentication bypass, and information leaks. High-impact flaws in Ingress-Nginx, Craft CMS, F5 BIG-IP, and NAKIVO Backup enable full system compromise, while SAP NetWeaver and AJ-Report allow remote shell deployment and template-based attacks. Ivanti EPMM’s auth bypass further risks unauthorized control over mobile device fleets.</p>
<p>GitHub Actions and Vercel introduce supply chain and reconnaissance risks, allowing malicious workflow inputs and data exposure that aid in targeted exploitation. Organizations should prioritize immediate patching, enhance monitoring, and deploy updated WAF and IDS signatures to defend against likely active exploitation.</p>
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
				<code class="nb-rule-id" title="6a61a14f44af4232a44e45aad127592a">d127592a</code>
</td>
<td>100746</td>
<td>Vercel - Information Disclosure</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bd30b3c43eb44335ab6013c195442495">95442495</code>
</td>
<td>100754</td>
<td>AJ-Report - Remote Code Execution - CVE:CVE-2024-15077</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6a13bd6e5fc94b1d9c97eb87dfee7ae4">dfee7ae4</code>
</td>
<td>100756</td>
<td>NAKIVO Backup - Remote Code Execution - CVE:CVE-2024-48248</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a4af6f2f15c9483fa9eab01d1c52f6d0">1c52f6d0</code>
</td>
<td>100757</td>
<td>Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1098</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bd30b3c43eb44335ab6013c195442495">95442495</code>
</td>
<td>100759</td>
<td>SAP NetWeaver - Dangerous File Upload - CVE:CVE-2025-31324</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dab2df4f548349e3926fee845366ccc1">5366ccc1</code>
</td>
<td>100760</td>
<td>Craft CMS - Remote Code Execution - CVE:CVE-2025-32432</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb23f172ed64ee08895e161eb40686b">eb40686b</code>
</td>
<td>100761</td>
<td>GitHub Action - Remote Code Execution - CVE:CVE-2025-30066</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="827037f2d5f941789efcba6260fc041c">60fc041c</code>
</td>
<td>100762</td>
<td>Ivanti EPMM - Auth Bypass - CVE:CVE-2025-4428, CVE:CVE-2025-4427</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ddee6d1c4f364768b324609cebafdfe6">ebafdfe6</code>
</td>
<td>100763</td>
<td>F5 Big IP - Remote Code Execution - CVE:CVE-2025-31644</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-05-19"><a href="/changelog/post/2025-05-19-waf-release/">WAF Release - 2025-05-19</a></h2>
<p><em>2025-05-19</em></p>
<p>This week's analysis covers four vulnerabilities, with three rated critical due to their Remote Code Execution (RCE) potential. One targets a high-traffic frontend platform, while another targets a popular content management system. These detections are now part of the Cloudflare Managed Ruleset in <em>Block</em> mode.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Commvault Command Center (CVE-2025-34028) exposes an unauthenticated RCE via insecure command injection paths in the web UI. This is critical due to its use in enterprise backup environments.</li>
<li>BentoML (CVE-2025-27520) reveals an exploitable vector where serialized payloads in model deployment APIs can lead to arbitrary command execution. This targets modern AI/ML infrastructure.</li>
<li>Craft CMS (CVE-2024-56145) allows RCE through template injection in unauthenticated endpoints. It poses a significant risk for content-heavy websites with plugin extensions.</li>
<li>Apache HTTP Server (CVE-2024-38475) discloses sensitive server config data due to misconfigured
<code>mod_proxy</code> behavior. While not RCE, this is useful for pre-attack recon.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These newly detected vulnerabilities introduce critical risk across modern web stacks, AI infrastructure, and content platforms: unauthenticated RCEs in Commvault, BentoML, and Craft CMS enable full system compromise with minimal attacker effort.</p>
<p>Apache HTTPD information leak can support targeted reconnaissance, increasing the success rate of follow-up exploits. Organizations using these platforms should prioritize patching and monitor for indicators of exploitation using updated WAF detection rules.</p>
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
				<code class="nb-rule-id" title="5c3559ad62994e5b932d7d0075129820">75129820</code>
</td>
<td>100745</td>
<td>Apache HTTP Server - Information Disclosure - CVE:CVE-2024-38475</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="28a22a685bba478d99bc904526a517f1">26a517f1</code>
</td>
<td>100747</td>
<td>
				Commvault Command Center - Remote Code Execution - CVE:CVE-2025-34028
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e6bb954d0634e368c49d7d1d7619ccb">d7619ccb</code>
</td>
<td>100749</td>
<td>BentoML - Remote Code Execution - CVE:CVE-2025-27520</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="91250eebec894705b62305b2f15bfda4">f15bfda4</code>
</td>
<td>100753</td>
<td>Craft CMS - Remote Code Execution - CVE:CVE-2024-56145</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="improved-payload-logging-for-waf-managed-rules"><a href="/changelog/post/2025-05-08-improved-payload-logging/">Improved Payload Logging for WAF Managed Rules</a></h2>
<p><em>2025-05-08</em></p>
<p>We have upgraded WAF Payload Logging to enhance rule diagnostics and usability:</p>
<ul>
<li><strong>Targeted logging</strong>: Logs now capture only the specific portions of requests that triggered WAF rules, rather than entire request segments.</li>
<li><strong>Visual highlighting</strong>: Matched content is visually highlighted in the UI for faster identification.</li>
<li><strong>Enhanced context</strong>: Logs now include surrounding context to make diagnostics more effective.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/waf/2025-05-payload-logging-update.png" alt="Log entry showing payload logging details" /></p>
<p>Payload Logging is available to all Enterprise customers. If you have not used Payload Logging before, check how you can <a href="/waf/managed-rules/payload-logging/">get started</a>.</p>
<p><strong>Note:</strong> The structure of the <code>encrypted_matched_data</code> field in Logpush has changed from <code>Map&lt;Field, Value&gt;</code> to <code>Map&lt;Field, {Before: bytes, Content: Value, After: bytes}&gt;</code>. If you rely on this field in your Logpush jobs, you should review and update your processing logic accordingly.</p>


<h2 id="waf-release-2025-05-05"><a href="/changelog/post/2025-05-05-waf-release/">WAF Release - 2025-05-05</a></h2>
<p><em>2025-05-05</em></p>
<p>This week's analysis covers five CVEs with varying impact levels. Four are rated critical, while one is rated high severity. Remote Code Execution vulnerabilities dominate this set.</p>
<p><strong>Key Findings</strong></p>
<p>GFI KerioControl (CVE-2024-52875) contains an unauthenticated Remote Code Execution (RCE) vulnerability that targets firewall appliances. This vulnerability can let attackers gain root level system access, making this CVE particularly attractive for threat actors.</p>
<p>The SonicWall SMA vulnerabilities remain concerning due to their continued exploitation since 2021. These critical vulnerabilities in remote access solutions create dangerous entry points to networks.</p>
<p><strong>Impact</strong></p>
<p>Customers using the Managed Ruleset will receive rule coverage following this week's release. Below is a breakdown of the recommended prioritization based on current exploitation trends:</p>
<ul>
<li>GFI KerioControl (CVE-2024-52875) - Highest priority; unauthenticated RCE</li>
<li>SonicWall SMA (Multiple vulnerabilities) - Critical for network appliances</li>
<li>XWiki (CVE-2025-24893) - High priority for development environments</li>
<li>Langflow (CVE-2025-3248) - Important for AI workflow platforms</li>
<li>MinIO (CVE-2025-31489) - Important for object storage implementations</li>
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
				<code class="nb-rule-id" title="921660147baa48eaa9151077d0b7a392">d0b7a392</code>
</td>
<td>100724</td>
<td>GFI KerioControl - Remote Code Execution - CVE:CVE-2024-52875</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a3900934273b4a488111f810717a9e42">717a9e42</code>
</td>
<td>100748</td>
<td>XWiki - Remote Code Execution - CVE:CVE-2025-24893</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="616ad0e03892473191ca1df4e9cf745d">e9cf745d</code>
</td>
<td>100750</td>
<td>
				SonicWall SMA - Dangerous File Upload - CVE:CVE-2021-20040,
				CVE:CVE-2021-20041, CVE:CVE-2021-20042
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1a11fbe84b49451193ee1ee6d29da333">d29da333</code>
</td>
<td>100751</td>
<td>Langflow - Remote Code Execution - CVE:CVE-2025-3248</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb7ed601e6844828b9bdb05caa7b208">caa7b208</code>
</td>
<td>100752</td>
<td>MinIO - Auth Bypass - CVE:CVE-2025-31489</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-04-26-emergency"><a href="/changelog/post/2025-04-26-emergency-waf-release/">WAF Release - 2025-04-26 - Emergency</a></h2>
<p><em>2025-04-26</em></p>
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
				<code class="nb-rule-id" title="54ea354d7f2d43c69b238d1419fcc883">19fcc883</code>
</td>
<td>100755</td>
<td>
				React.js - Router and Remix Vulnerability - CVE:CVE-2025-43864,
				CVE:CVE-2025-43865
</td>
<td>Block</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-04-22"><a href="/changelog/post/2025-04-22-waf-release/">WAF Release - 2025-04-22</a></h2>
<p><em>2025-04-22</em></p>
<p>Each of this week's rule releases covers a distinct CVE, with half of the rules targeting Remote Code Execution (RCE) attacks. Of the 6 CVEs covered, four were scored as critical, with the other two scored as high.</p>
<p>When deciding which exploits to tackle, Cloudflare tunes into the attackers' areas of focus. Cloudflare's network intelligence provides a unique lens into attacker activity – for instance, through the volume of blocked requests related with CVE exploits after updating WAF Managed Rules with new detections.</p>
<p>From this week's releases, one indicator that RCE is a &quot;hot topic&quot; attack type is the fact that the Oracle PeopleSoft RCE rule accounts for half of all of the new rule matches. This rule patches CVE-2023-22047, a high-severity vulnerability in the Oracle PeopleSoft suite that allows unauthenticated attackers to access PeopleSoft Enterprise PeopleTools data through remote code execution. This is particularly concerning because of the nature of the data managed by PeopleSoft – this can include payroll records or student profile information. This CVE, along with five others, are addressed with the latest detection update to WAF Managed Rules.</p>
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
				<code class="nb-rule-id" title="faa032d9825e4844a1188f3ba5be3327">a5be3327</code>
</td>
<td>100738</td>
<td>GitLab - Auth Bypass - CVE:CVE-2023-7028</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e96b6d5cdd94f7782b90e266c9531fa">6c9531fa</code>
</td>
<td>100740</td>
<td>Splunk Enterprise - Remote Code Execution - CVE:CVE-2025-20229</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5c9c095bc1e5411195edb893f40bbc2b">f40bbc2b</code>
</td>
<td>100741</td>
<td>Oracle PeopleSoft - Remote Code Execution - CVE:CVE-2023-22047</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1d7a3932296c42fd827055335462167c">5462167c</code>
</td>
<td>100742</td>
<td>CrushFTP - Auth Bypass - CVE:CVE-2025-31161</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb7ed601e6844828b9bdb05caa7b208">caa7b208</code>
</td>
<td>100743</td>
<td>Ivanti - Buffer Error - CVE:CVE-2025-22457</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="410317f1e32b41859fa3214dd52139a8">d52139a8</code>
</td>
<td>100744</td>
<td>
				Oracle Access Manager - Remote Code Execution - CVE:CVE-2021-35587
</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-04-14"><a href="/changelog/post/2025-04-14-waf-release/">WAF Release - 2025-04-14</a></h2>
<p><em>2025-04-14</em></p>
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
				<code class="nb-rule-id" title="9209bb65527f4c088bca5ffad6b2d36c">d6b2d36c</code>
</td>
<td>100739A</td>
<td>Next.js - Auth Bypass - CVE:CVE-2025-29927 - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/waf/3/">Previous</a><span>Page 4 of 5</span><a class="pagination-next" rel="next" href="/changelog/product/waf/5/">Next</a></nav>
