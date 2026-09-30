<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 3, 2025</time><h2 id="post-title">WAF Release - 2025-12-03 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>The WAF rule deployed yesterday to block unsafe deserialization-based RCE has been updated. The rule description now reads “React – RCE – CVE-2025-55182”, explicitly mapping to the recently disclosed React Server Components vulnerability. Detection logic remains unchanged.</p>
<p><strong>Key Findings</strong></p>
<p>Rule description updated to reference React – RCE – CVE-2025-55182 while retaining existing unsafe-deserialization detection.</p>
<p><strong>Impact</strong></p>
<p>Improved classification and traceability with no change to coverage against remote code execution attempts.</p>
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
				<code class="nb-rule-id" title="33aa8a8a948b48b28d40450c5fb92fba">5fb92fba</code>
</td>
<td>N/A</td>
<td>React - RCE - CVE:CVE-2025-55182</td>
<td>N/A</td>
<td>Block</td>
<td>Rule metadata description changed. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="2b5d06e34a814a889bee9a0699702280">99702280</code>
</td>
<td>N/A</td>
<td>React - RCE - CVE:CVE-2025-55182</td>
<td>N/A</td>
<td>Block</td>
<td>Rule metadata description changed. Detection unchanged.</td>
</tr>
</tbody>
</table>
</div></article></div>
