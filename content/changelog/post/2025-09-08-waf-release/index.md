<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 8, 2025</time><h2 id="post-title">WAF Release - 2025-09-08</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
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
</div></article></div>
