<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 15, 2026</time><h2 id="post-title">WAF Release - 2026-09-15</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new threat detections to enhance protection against command injection attempts, Server-Side Request Forgery (SSRF) targeting cloud metadata, and information disclosure within version control history.</p>
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
				<code class="nb-rule-id" title="b2170b7b1a2c4b8eba0b498eca453d31">ca453d31</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - 3</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="02c818297e6d42aaa55e67f5e540f17f">e540f17f</code>
</td>
<td>N/A</td>
<td>Version Control - Information Disclosure - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Version Control - Information Disclosure" (ID:{" "}<code class="nb-rule-id" title="23548ee2b36547a1be09bb2c0550c529">0550c529</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="93793848937f4f988f1dfdabba458b4b">ba458b4b</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 10</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>        
</tbody>
</table>
</div></article></div>
