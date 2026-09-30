<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 4, 2026</time><h2 id="post-title">WAF Release - 2026-08-04</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new rules and updates Microsoft SharePoint RCE alongside enhanced SSRF cloud protection rule actions.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-50522: An insecure deserialization vulnerability in Microsoft SharePoint Server. This may allow an unauthenticated attacker to execute arbitrary code using crafted requests.</li>
<li>CVE-2026-66066: An improper input processing vulnerability in Ruby on Rails Active Storage image variant transformations. This may allow an unauthenticated attacker to perform arbitrary file reads and achieve Remote Code Execution (RCE) using maliciously crafted payload requests.</li>
<li>Generic Cloud Protections: Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications.</li>
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
				<code class="nb-rule-id" title="91aee93c31944828bf86f068052b07cf">052b07cf</code>
</td>
<td>N/A</td>
<td>Microsoft SharePoint - Remote Code Execution - CVE:CVE-2026-50522</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89d0243997d24c6ea1d610a23a5b40d6">3a5b40d6</code>
</td>
<td>N/A</td>
<td>Rails - Arbitrary File Read & RCE - CVE:CVE-2026-66066</td>
<td>Block</td>
<td>Block</td>
<td>
				This was labeled as File Upload - RCE.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="98bfd6bb46074d5b8d1c4b39743a63ec">743a63ec</code>
</td>
<td>N/A</td>
<td>SSRF - Local - 2 - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ecd26d61a75e46f6a4449a06ab8af26f">ab8af26f</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - 2 - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="281a1b7086b84db7a695220725ba9d7c">25ba9d7c</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud</td>
<td>Disabled</td>
<td>Block</td>
<td>
				We are changing the action for this rule from Disabled to BLOCK
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="158177dec2504acdba1f2da201a076eb">01a076eb</code>
</td>
<td>N/A</td>
<td>SSRF - Local - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
</tbody>
</table>
</div></article></div>
