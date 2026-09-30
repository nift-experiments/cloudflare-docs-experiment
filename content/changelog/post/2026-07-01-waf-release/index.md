<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 1, 2026</time><h2 id="post-title">WAF Release - 2026-07-01</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release adds targeted coverage for a path traversal flaw in Fortinet FortiSandbox (CVE-2026-39813) and transitions the Anomaly:Header:User-Agent - Fake Bing or MSN Bot rule action from Block to Disabled.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-39813: A path traversal vulnerability in Fortinet FortiSandbox allows remote, unauthenticated attackers to read arbitrary files from the underlying filesystem due to insufficient validation of user-supplied input paths.</li>
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
				<code class="nb-rule-id" title="32075e19b1494117ac5915e8d84c92c9">d84c92c9</code>
</td>
<td>N/A</td>
<td>Fortinet FortiSandbox - Path Traversal - CVE:CVE-2026-39813</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ae20608d93b94e97988db1bbc12cf9c8">c12cf9c8</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:User-Agent - Fake Bing or MSN Bot</td>
<td>Enabled</td>
<td>Disabled</td>
<td>
				We are changing the action for this rule from BLOCK to Disabled
</td>
</tr>
</tbody>
</table>
</div></article></div>
