<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 11, 2026</time><h2 id="post-title">WAF Release - 2026-08-11</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new protection for a remote code execution vulnerability in vBulletin and improves two existing detections.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>A new detection provides protection against vBulletin CVE-2026-61511.</li>
<li>Two existing detections have been improved to strengthen coverage.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2026-61511 may lead to remote code execution on affected vBulletin systems, potentially resulting in unauthorized access, data exposure, service disruption, and broader compromise of the hosting environment. Administrators are strongly encouraged to apply vendor updates and recommended mitigations.</p>
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
				<code class="nb-rule-id" title="1b0775f0f092483387cfb23f94f3006b">94f3006b</code>
</td>
<td>N/A</td>
<td>vBulletin - Remote Code Execution - CVE:CVE-2026-61511</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="784d3824b6cf419db6af0b64098b749e">098b749e</code>
</td>
<td>N/A</td>
<td>Version Control - Information Disclosure - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Version Control - Information Disclosure" (ID: <code class="nb-rule-id" title="23548ee2b36547a1be09bb2c0550c529">0550c529</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a561c9138b46470ca6db96edd56225d8">d56225d8</code>
</td>
<td>N/A</td>
<td>vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "vBulletin - Code Injection - Invalid image format - CVE:CVE-2019-17132" (ID: <code class="nb-rule-id" title="5137834eb8634842852273a08fe9f1c7">8fe9f1c7</code>)</td>
</tr>
</tbody>
</table>
</div></article></div>
