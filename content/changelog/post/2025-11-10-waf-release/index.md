<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 10, 2025</time><h2 id="post-title">WAF Release - 2025-11-10</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for Prototype Pollution across three common vectors: URI, Body, and Header/Form.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>These attacks can affect both API and web applications by altering normal behavior or bypassing security controls.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation may allow attackers to change internal logic or cause unexpected behavior in applications using JavaScript or Node.js frameworks. Developers should sanitize input keys and avoid merging untrusted data structures.</p>
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
				<code class="nb-rule-id" title="32405a50728746dd8caa057b606285e6">606285e6</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a7da00c63c4243d2a72456fe4f59ff26">4f59ff26</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="833078bdcfa04bb7aa7b8fb67efbeb39">7efbeb39</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - Header - Form</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>        
</tbody>
</table>
</div></article></div>
