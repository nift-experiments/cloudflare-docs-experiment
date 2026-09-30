<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 22, 2025</time><h2 id="post-title">WAF Release - 2025-09-22</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week emphasizes two critical vendor-specific vulnerabilities: a full elevation-of-privilege in Microsoft Azure Networking (CVE-2025-54914) and a server-side template injection (SSTI) leading to remote code execution (RCE) in Skyvern (CVE-2025-49619). These are complemented by enhancements in generic detections (SQLi, SSRF) to improve baseline coverage.</p>
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
</div></article></div>
