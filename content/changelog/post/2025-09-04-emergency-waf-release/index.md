<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 4, 2025</time><h2 id="post-title">WAF Release - 2025-09-04 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week, new critical vulnerabilities were disclosed in Sitecore’s Sitecore Experience Manager (XM), Sitecore Experience Platform (XP), specifically versions 9.0 through 9.3, and 10.0 through 10.4.
These flaws are caused by unsafe data deserialization and code reflection, leaving affected systems at high risk of exploitation.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-53690: Remote Code Execution through Insecure Deserialization</li>
<li>CVE-2025-53691: Remote Code Execution through Insecure Deserialization</li>
<li>CVE-2025-53693: HTML Cache Poisoning through Unsafe Reflections</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation could allow attackers to execute arbitrary code remotely on the affected system and conduct cache poisoning attacks, potentially leading to further compromise. Applying the latest vendor-released solution without delay is strongly recommended.</p>
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
        <code class="nb-rule-id" title="588edc74df1f4609b3c2f7ef0ee2c15e">0ee2c15e</code>
</td>
<td>100878</td>
<td>Sitecore - Remote Code Execution - CVE:CVE-2025-53691</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d1bd7563e6254db48ce703807c5b669c">7c5b669c</code>
</td>
<td>100631</td>
<td>Sitecore - Cache Poisoning - CVE:CVE-2025-53693</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ed94c7ce5301411a94a21a096c410240">6c410240</code>
</td>
<td>100879</td>
<td>Sitecore - Remote Code Execution - CVE:CVE-2025-53690</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection</td>
</tr>
</tbody>
</table>
</div></article></div>
