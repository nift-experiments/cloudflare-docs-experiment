<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 10, 2025</time><h2 id="post-title">WAF Release - 2025-12-10 - Emergency</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This additional week's emergency release introduces improvements to our existing rule for React – Remote Code Execution – CVE-2025-55182 - 2, along with two new generic detections covering server-side function exposure and resource-exhaustion patterns.</p>
<p><strong>Key Findings</strong></p>
<p>Enhanced detection logic for React – RCE – CVE-2025-55182, added Generic – Server Function Source Code Exposure, and added Generic – Server Function Resource Exhaustion.</p>
<p><strong>Impact</strong></p>
<p>These updates strengthen protection against React RCE exploitation attempts and broaden coverage for common server-function abuse techniques that may expose internal logic or disrupt application availability.</p>
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
				<code class="nb-rule-id" title="bc1aee59731c488ca8b5314615fce168">15fce168</code>
</td>
<td>N/A</td>
<td>React - Remote Code Execution - CVE:CVE-2025-55182 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="cbdd3f48396e4b7389d6efd174746aff">74746aff</code>
</td>
<td>N/A</td>
<td>React - Remote Code Execution - CVE:CVE-2025-55182 - 2</td>
<td>N/A</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="17c5123f1ac049818765ebf2fefb4e9b">fefb4e9b</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Source Code Exposure</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="3114709a3c3b4e3685052c7b251e86aa">251e86aa</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Source Code Exposure</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2694f1610c0b471393b21aef102ec699">102ec699</code>
</td>
<td>N/A</td>
<td>Generic - Server Function Resource Exhaustion</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div></article></div>
