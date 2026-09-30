<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 5, 2025</time><h2 id="post-title">WAF Release - 2025-05-05</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's analysis covers five CVEs with varying impact levels. Four are rated critical, while one is rated high severity. Remote Code Execution vulnerabilities dominate this set.</p>
<p><strong>Key Findings</strong></p>
<p>GFI KerioControl (CVE-2024-52875) contains an unauthenticated Remote Code Execution (RCE) vulnerability that targets firewall appliances. This vulnerability can let attackers gain root level system access, making this CVE particularly attractive for threat actors.</p>
<p>The SonicWall SMA vulnerabilities remain concerning due to their continued exploitation since 2021. These critical vulnerabilities in remote access solutions create dangerous entry points to networks.</p>
<p><strong>Impact</strong></p>
<p>Customers using the Managed Ruleset will receive rule coverage following this week's release. Below is a breakdown of the recommended prioritization based on current exploitation trends:</p>
<ul>
<li>GFI KerioControl (CVE-2024-52875) - Highest priority; unauthenticated RCE</li>
<li>SonicWall SMA (Multiple vulnerabilities) - Critical for network appliances</li>
<li>XWiki (CVE-2025-24893) - High priority for development environments</li>
<li>Langflow (CVE-2025-3248) - Important for AI workflow platforms</li>
<li>MinIO (CVE-2025-31489) - Important for object storage implementations</li>
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
				<code class="nb-rule-id" title="921660147baa48eaa9151077d0b7a392">d0b7a392</code>
</td>
<td>100724</td>
<td>GFI KerioControl - Remote Code Execution - CVE:CVE-2024-52875</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a3900934273b4a488111f810717a9e42">717a9e42</code>
</td>
<td>100748</td>
<td>XWiki - Remote Code Execution - CVE:CVE-2025-24893</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="616ad0e03892473191ca1df4e9cf745d">e9cf745d</code>
</td>
<td>100750</td>
<td>
				SonicWall SMA - Dangerous File Upload - CVE:CVE-2021-20040,
				CVE:CVE-2021-20041, CVE:CVE-2021-20042
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1a11fbe84b49451193ee1ee6d29da333">d29da333</code>
</td>
<td>100751</td>
<td>Langflow - Remote Code Execution - CVE:CVE-2025-3248</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb7ed601e6844828b9bdb05caa7b208">caa7b208</code>
</td>
<td>100752</td>
<td>MinIO - Auth Bypass - CVE:CVE-2025-31489</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
