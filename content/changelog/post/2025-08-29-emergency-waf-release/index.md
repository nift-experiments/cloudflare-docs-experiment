<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 29, 2025</time><h2 id="post-title">WAF Release - 2025-08-29 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week, new critical vulnerabilities were disclosed in Next.js’s image optimization functionality, exposing a broad range of production environments to risks of data exposure and cache manipulation.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2025-55173: Arbitrary file download from the server via image optimization.</p>
</li>
<li>
<p>CVE-2025-57752: Cache poisoning leading to unauthorized data disclosure.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation could expose sensitive files, leak user or backend data, and undermine application trust. Given Next.js’s wide use, immediate patching and cache hardening are strongly advised.</p>
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
        <code class="nb-rule-id" title="ea55f8aac44246cc9b827eea9ff4bfe3">9ff4bfe3</code>
</td>
<td>100613</td>
<td>Next.js - Dangerous File Download - CVE:CVE-2025-55173</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e2b2d77a79cc4a76bf7ba53d69b9ea7d">69b9ea7d</code>
</td>
<td>100616</td>
<td>Next.js - Information Disclosure - CVE:CVE-2025-57752</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
</tbody>
</table>
</div></article></div>
