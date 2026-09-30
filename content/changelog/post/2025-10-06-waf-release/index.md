<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 6, 2025</time><h2 id="post-title">WAF Release - 2025-10-06</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s highlights prioritise an emergency Oracle E-Business Suite RCE rule deployed to block active, high-impact exploitation. Also addressed are high-severity Chaos Mesh controller command-injection flaws that enable unauthenticated in-cluster RCE and potential cluster compromise, plus a form-data multipart boundary issue that permits HTTP Parameter Pollution (HPP). Two new generic SQLi detections were added to catch inline-comment obfuscation and information disclosure techniques.</p>
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
</div></article></div>
