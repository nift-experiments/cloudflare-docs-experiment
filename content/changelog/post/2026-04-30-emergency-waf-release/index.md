<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 30, 2026</time><h2 id="post-title">WAF Release - 2026-04-30 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release introduces a new rule to block a cPanel &amp; WHM Authentication Bypass related to CVE-2026-41940.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-41940: A critical authentication bypass vulnerability in cPanel &amp; WHM allows unauthenticated remote attackers to bypass authentication mechanisms and gain unauthorized administrative access to the web hosting control panel. This vulnerability affects the session validation logic, enabling attackers to craft malicious requests that circumvent normal authentication checks.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation allows unauthenticated attackers to gain administrative control over affected cPanel &amp; WHM installations. This leads to complete server compromise, potential theft or manipulation of hosted data, and significant service disruption across managed environments.</p>
<p>We strongly recommend applying official vendor patches for cPanel &amp; WHM immediately to address the underlying vulnerability.</p>
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
				<code class="nb-rule-id" title="fb29b1b660864285a5ebac86eb2b9e2f">eb2b9e2f</code>
</td>
<td>N/A</td>
<td>cPanel - Auth Bypass - CVE:CVE-2026-41940</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div></article></div>
