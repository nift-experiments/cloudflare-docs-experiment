<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 26, 2026</time><h2 id="post-title">WAF Release - 2026-01-26</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for denial-of-service attempts targeting React CVE-2026-23864 (<a href="https://www.cve.org/CVERecord?id=CVE-2026-23864">https://www.cve.org/CVERecord?id=CVE-2026-23864</a>).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-23864 (<a href="https://www.cve.org/CVERecord?id=CVE-2026-23864">https://www.cve.org/CVERecord?id=CVE-2026-23864</a>) affects <code>react-server-dom-parcel</code>, <code>react-server-dom-turbopack</code>, and <code>react-server-dom-webpack</code> packages.</li>
<li>Attackers can send crafted HTTP requests to Server Function endpoints, causing server crashes, out-of-memory exceptions, or excessive CPU usage.</li>
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
        <code class="nb-rule-id" title="aaede80b4d414dc89c443cea61680354">61680354</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 1</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3e93c9faaafa447c83a525f2dcdffcf8">dcdffcf8</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="930020d567684f19b05fb35b349edbc6">349edbc6</code>
</td>
<td>N/A</td>
<td>React Server - DOS - CVE:CVE-2026-23864 - 3</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div></article></div>
