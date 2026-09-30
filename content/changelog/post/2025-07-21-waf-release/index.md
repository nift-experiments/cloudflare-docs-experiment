<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 21, 2025</time><h2 id="post-title">WAF Release - 2025-07-21</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's update spotlights several critical vulnerabilities across Citrix NetScaler Memory Disclosure, FTP servers and network application. Several flaws enable unauthenticated remote code execution or sensitive data exposure, posing a significant risk to enterprise security.</p>
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
</div></article></div>
