<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 25, 2025</time><h2 id="post-title">WAF Release - 2025-08-25</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
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
</div></article></div>
