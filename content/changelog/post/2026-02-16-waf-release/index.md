<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 16, 2026</time><h2 id="post-title">WAF Release - 2026-02-16</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for CVE-2025-68645 and CVE-2025-31125.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-68645: A Local File Inclusion (LFI) vulnerability in the Webmail Classic UI of Zimbra Collaboration Suite (ZCS) 10.0 and 10.1 allows unauthenticated remote attackers to craft requests to the <code>/h/rest</code> endpoint, improperly influence internal dispatching, and include arbitrary files from the WebRoot directory.</li>
<li>CVE-2025-31125: Vite, the JavaScript frontend tooling framework, exposes content of non-allowed files via <code>?inline&amp;import</code> when its development server is network-exposed, enabling unauthorized attackers to read arbitrary files and potentially leak sensitive information.</li>
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
				<code class="nb-rule-id" title="695d76ff756844d384cab548833761f7">833761f7</code>
</td>
<td>N/A</td>
<td>Zimbra - Local File Inclusion - CVE:CVE-2025-68645</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="38fff9f3deba46a2abc10a8f950ed8c8">950ed8c8</code>
</td>
<td>N/A</td>
<td>Vite - WASM Import Path Traversal - CVE:CVE-2025-31125</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div></article></div>
