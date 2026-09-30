<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 2, 2026</time><h2 id="post-title">WAF Release - 2026-02-02</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for CVE-2025-64459 and CVE-2025-24893.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-64459: Django versions prior to 5.1.14, 5.2.8, and 4.2.26 are vulnerable to SQL injection via crafted dictionaries passed to QuerySet methods and the <code>Q()</code> class.</li>
<li>CVE-2025-24893: XWiki allows unauthenticated remote code execution through crafted requests to the SolrSearch endpoint, affecting the entire installation.</li>
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
        <code class="nb-rule-id" title="7a47683eacce4abd870ab2c630698ff3">30698ff3</code>
</td>
<td>N/A</td>
<td>XWiki - Remote Code Execution - CVE:CVE-2025-24893 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ad5c52f6ca334ef4a844e5e5da8ba7e6">da8ba7e6</code>
</td>
<td>N/A</td>
<td>Django SQLI - CVE:CVE-2025-64459</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8f0d5c98bd24460a9305a1558d667511">8d667511</code>
</td>
<td>N/A</td>
<td>NoSQL, MongoDB - SQLi - Comparison - 2</td>
<td>Block</td>
<td>Block</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>
</div></article></div>
