<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 22, 2025</time><h2 id="post-title">WAF Release - 2025-04-22</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>Each of this week's rule releases covers a distinct CVE, with half of the rules targeting Remote Code Execution (RCE) attacks. Of the 6 CVEs covered, four were scored as critical, with the other two scored as high.</p>
<p>When deciding which exploits to tackle, Cloudflare tunes into the attackers' areas of focus. Cloudflare's network intelligence provides a unique lens into attacker activity – for instance, through the volume of blocked requests related with CVE exploits after updating WAF Managed Rules with new detections.</p>
<p>From this week's releases, one indicator that RCE is a &quot;hot topic&quot; attack type is the fact that the Oracle PeopleSoft RCE rule accounts for half of all of the new rule matches. This rule patches CVE-2023-22047, a high-severity vulnerability in the Oracle PeopleSoft suite that allows unauthenticated attackers to access PeopleSoft Enterprise PeopleTools data through remote code execution. This is particularly concerning because of the nature of the data managed by PeopleSoft – this can include payroll records or student profile information. This CVE, along with five others, are addressed with the latest detection update to WAF Managed Rules.</p>
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
				<code class="nb-rule-id" title="faa032d9825e4844a1188f3ba5be3327">a5be3327</code>
</td>
<td>100738</td>
<td>GitLab - Auth Bypass - CVE:CVE-2023-7028</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e96b6d5cdd94f7782b90e266c9531fa">6c9531fa</code>
</td>
<td>100740</td>
<td>Splunk Enterprise - Remote Code Execution - CVE:CVE-2025-20229</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5c9c095bc1e5411195edb893f40bbc2b">f40bbc2b</code>
</td>
<td>100741</td>
<td>Oracle PeopleSoft - Remote Code Execution - CVE:CVE-2023-22047</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1d7a3932296c42fd827055335462167c">5462167c</code>
</td>
<td>100742</td>
<td>CrushFTP - Auth Bypass - CVE:CVE-2025-31161</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb7ed601e6844828b9bdb05caa7b208">caa7b208</code>
</td>
<td>100743</td>
<td>Ivanti - Buffer Error - CVE:CVE-2025-22457</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="410317f1e32b41859fa3214dd52139a8">d52139a8</code>
</td>
<td>100744</td>
<td>
				Oracle Access Manager - Remote Code Execution - CVE:CVE-2021-35587
</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
