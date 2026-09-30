<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 17, 2026</time><h2 id="post-title">WAF Release - 2026-07-17 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release adds a new managed rule to block active exploitation of a critical remote code execution (RCE) and SQL injection (SQLi) vulnerability found in popular web frameworks.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Generic Frameworks - Unauthenticated RCE: Attackers can execute arbitrary system commands with web server privileges by sending malicious input containing invalid path sequences during request processing.</p>
</li>
<li>
<p>Generic Frameworks - SQLi: Attackers can execute unauthorized database queries due to a failure to sanitize input values within request parameters.</p>
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
				<code class="nb-rule-id" title="7dfb2bd4708d4b88b9911dc0550664b6">550664b6</code>
</td>
<td>N/A</td>
<td>Generic Rules - Unauthenticated RCE</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c060d3a371549219ee290d7ed933fcc">ed933fcc</code>
</td>
<td>N/A</td>
<td>Generic Rules - SQLi </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="ebd3f2df15c74ddcbf6220c9b5ec246a">b5ec246a</code>
</td>
<td>N/A</td>
<td>Generic Rules - Unauthenticated RCE </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="db003b39b7774859a8d588ce33697a1a">33697a1a</code>
</td>
<td>N/A</td>
<td>Generic Rules - SQLi </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>        
</tbody>
</table>
</div></article></div>
