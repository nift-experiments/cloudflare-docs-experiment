<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 16, 2025</time><h2 id="post-title">WAF Release - 2025-06-16</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s roundup highlights multiple critical vulnerabilities across popular web frameworks, plugins, and enterprise platforms. The focus lies on remote code execution (RCE), server-side request forgery (SSRF), and insecure file upload vectors that enable full system compromise or data exfiltration.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Cisco IOS XE (CVE-2025-20188): Critical RCE vulnerability enabling unauthenticated attackers to execute arbitrary commands on network infrastructure devices, risking total router compromise.</li>
<li>Axios (CVE-2024-39338): SSRF flaw impacting server-side request control, allowing attackers to manipulate internal service requests when misconfigured with unsanitized user input.</li>
<li>vBulletin (CVE-2025-48827, CVE-2025-48828): Two high-impact RCE flaws enabling attackers to remotely execute PHP code, compromising forum installations and underlying web servers.</li>
<li>Invision Community (CVE-2025-47916): A critical RCE vulnerability allowing authenticated attackers to run arbitrary code in community platforms, threatening data and lateral movement risk.</li>
<li>CrushFTP (CVE-2025-32102, CVE-2025-32103): SSRF vulnerabilities in upload endpoint processing permit attackers to pivot internal network scans and abuse internal services.</li>
<li>Roundcube (CVE-2025-49113): RCE via email processing enables attackers to execute code upon viewing a crafted email — particularly dangerous for webmail deployments.</li>
<li>WooCommerce WordPress Plugin (CVE-2025-47577): Dangerous file upload vulnerability permits unauthenticated users to upload executable payloads, leading to full WordPress site takeover.</li>
<li>Cross-Site Scripting (XSS) Detection Improvements: Enhanced detection patterns.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities span core systems — from routers to e-commerce to email. RCE in Cisco IOS XE, Roundcube, and vBulletin poses full system compromise. SSRF in Axios and CrushFTP supports internal pivoting, while WooCommerce’s file upload bug opens doors to mass WordPress exploitation.</p>
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
				<code class="nb-rule-id" title="233bcf0ce50f400989a7e44a35fefd53">35fefd53</code>
</td>
<td>100783</td>
<td>Cisco IOS XE - Remote Code Execution - CVE:CVE-2025-20188</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9284e3b1586341acb4591bfd8332af5d">8332af5d</code>
</td>
<td>100784</td>
<td>Axios - SSRF - CVE:CVE-2024-39338</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2672b175a25548aa8e0107b12e1648d2">2e1648d2</code>
</td>
<td>100785</td>
<td>
				vBulletin - Remote Code Execution - CVE:CVE-2025-48827,
				CVE:CVE-2025-48828
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b77a19fb053744b49eacdab00edcf1ef">0edcf1ef</code>
</td>
<td>100786</td>
<td>Invision Community - Remote Code Execution - CVE:CVE-2025-47916</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="aec2274743064523a9667248d6f5eb48">d6f5eb48</code>
</td>
<td>100791</td>
<td>CrushFTP - SSRF - CVE:CVE-2025-32102, CVE:CVE-2025-32103</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7b80e1f5575d4d99bb7d56ae30baa18a">30baa18a</code>
</td>
<td>100792</td>
<td>Roundcube - Remote Code Execution - CVE:CVE-2025-49113</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="52d76f9394494b0382c7cb00229ba236">229ba236</code>
</td>
<td>100793</td>
<td>XSS - Ontoggle</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d38e657bd43f4d809c28157dfa338296">fa338296</code>
</td>
<td>100794</td>
<td>
				WordPress WooCommerce Plugin - Dangerous File Upload -
				CVE:CVE-2025-47577
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
