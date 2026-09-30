<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 8, 2026</time><h2 id="post-title">WAF Release - 2026-09-08</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release enhances detection logic for existing rules targeting Next.js remote code execution (RCE) vulnerabilities by consolidating active beta rules into baseline signatures.</p>
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
				<code class="nb-rule-id" title="d5d9f863e50b416faf43934dc76ba662">c76ba662</code>
</td>
<td>N/A</td>
<td>Next.js - Image Optimizer Remote Code Execution via Crafted AVIF - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Next.js - Image Optimizer Remote Code Execution via Crafted AVIF" (ID:{" "}<code class="nb-rule-id" title="18b22b0bd423423c945b3a0180256efe">80256efe</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="771ac3761dcd485cb0e91ea0208457cf">208457cf</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - CVE:CVE-2026-75604 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Next.js - Remote Code Execution - CVE:CVE-2026-75604" (ID:{" "}<code class="nb-rule-id" title="2b6b94ec864d47f99630ecf72ca6cce3">2ca6cce3</code>).</td>
</tr>
</tbody>
</table>
</div></article></div>
