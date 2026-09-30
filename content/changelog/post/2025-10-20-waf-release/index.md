<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 20, 2025</time><h2 id="post-title">WAF Release - 2025-10-20</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s update introduces an enhanced rule that expands detection coverage for a critical vulnerability in Oracle E-Business Suite. It also improves an existing rule to provide more reliable coverage in request processing.</p>
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
</div></article></div>
