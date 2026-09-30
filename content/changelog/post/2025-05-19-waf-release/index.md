<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 19, 2025</time><h2 id="post-title">WAF Release - 2025-05-19</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's analysis covers four vulnerabilities, with three rated critical due to their Remote Code Execution (RCE) potential. One targets a high-traffic frontend platform, while another targets a popular content management system. These detections are now part of the Cloudflare Managed Ruleset in <em>Block</em> mode.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Commvault Command Center (CVE-2025-34028) exposes an unauthenticated RCE via insecure command injection paths in the web UI. This is critical due to its use in enterprise backup environments.</li>
<li>BentoML (CVE-2025-27520) reveals an exploitable vector where serialized payloads in model deployment APIs can lead to arbitrary command execution. This targets modern AI/ML infrastructure.</li>
<li>Craft CMS (CVE-2024-56145) allows RCE through template injection in unauthenticated endpoints. It poses a significant risk for content-heavy websites with plugin extensions.</li>
<li>Apache HTTP Server (CVE-2024-38475) discloses sensitive server config data due to misconfigured
<code>mod_proxy</code> behavior. While not RCE, this is useful for pre-attack recon.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These newly detected vulnerabilities introduce critical risk across modern web stacks, AI infrastructure, and content platforms: unauthenticated RCEs in Commvault, BentoML, and Craft CMS enable full system compromise with minimal attacker effort.</p>
<p>Apache HTTPD information leak can support targeted reconnaissance, increasing the success rate of follow-up exploits. Organizations using these platforms should prioritize patching and monitor for indicators of exploitation using updated WAF detection rules.</p>
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
				<code class="nb-rule-id" title="5c3559ad62994e5b932d7d0075129820">75129820</code>
</td>
<td>100745</td>
<td>Apache HTTP Server - Information Disclosure - CVE:CVE-2024-38475</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="28a22a685bba478d99bc904526a517f1">26a517f1</code>
</td>
<td>100747</td>
<td>
				Commvault Command Center - Remote Code Execution - CVE:CVE-2025-34028
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e6bb954d0634e368c49d7d1d7619ccb">d7619ccb</code>
</td>
<td>100749</td>
<td>BentoML - Remote Code Execution - CVE:CVE-2025-27520</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="91250eebec894705b62305b2f15bfda4">f15bfda4</code>
</td>
<td>100753</td>
<td>Craft CMS - Remote Code Execution - CVE:CVE-2024-56145</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
