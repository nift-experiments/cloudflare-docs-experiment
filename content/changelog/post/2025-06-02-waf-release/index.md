<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 2, 2025</time><h2 id="post-title">WAF Release - 2025-06-02</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s roundup highlights five high-risk vulnerabilities affecting SD-WAN, load balancers, and AI platforms. Several flaws enable unauthenticated remote code execution or authentication bypass.</p>
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
</div></article></div>
