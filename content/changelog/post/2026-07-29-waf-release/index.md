<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 29, 2026</time><h2 id="post-title">WAF Release - 2026-07-29</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new rules and updates existing threat signatures to provide targeted protections for vulnerabilities in Nuxt Server Island components and Alibaba Fastjson deserialization routines, alongside enhanced protections for cloud metadata Server-Side Request Forgery (SSRF) and obfuscated command injection attempts.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Nuxt Server Island - RCE(GHSA-9473-5f9j-94wq): An unauthenticated vulnerability in Nuxt Server Islands where remote attackers can supply arbitrary component names or props to endpoints. Manipulating these parameters allows unauthenticated component Remote Code Execution (RCE) on the server.</p>
</li>
<li>
<p>Alibaba Fastjson JSONType Remote Code Execution: A unauthenticated remote code execution vulnerability in Alibaba Fastjson (≤ 1.2.83) during JSON deserialization. Under default configurations, attackers can execute arbitrary system commands, bypassing traditional classpath and gadget-based defenses.</p>
</li>
<li>
<p>Generic Protections (SSRF &amp; Command Injection): Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications, alongside new rules targeting obfuscated command injection patterns across request parameters.</p>
</li>
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
				<code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is an improved detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="95a84ab1645a49c685648c17761e7a4c">761e7a4c</code>
</td>
<td>N/A</td>
<td>Command Injection - Obfuscation</td>
<td>Log</td>
<td>Block</td>            
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58df9693db4d454a8764fcda7347c892">7347c892</code>
</td>
<td>N/A</td>
<td>Alibaba Fastjson JSONType Remote Code Execution - Body</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6159ead63d284147943dc5a18ec012ea">8ec012ea</code>
</td>
<td>N/A</td>
<td>Nuxt Server Island - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.This was labeled as Generic Rules - RCE.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dcf635ab2e744e1a994443973590a4ad">3590a4ad</code>
</td>
<td>N/A</td>
<td>Generic Rules - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d3852d0891634686a46114069c6dff1c">9c6dff1c</code>
</td>
<td>N/A</td>
<td>Generic Rules - XSS</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89d0243997d24c6ea1d610a23a5b40d6">3a5b40d6</code>
</td>
<td>N/A</td>
<td>File Upload - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ad9f2049b094c608be0f8adcfe1a93c">cfe1a93c</code>
</td>
<td>N/A</td>
<td>Generic Rules - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="5bdf578fff504b8cbe3b7f699ab5ed95">9ab5ed95</code>
</td>
<td>N/A</td>
<td>Generic Rules - XSS</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="7ecac499d14a4750aa58c1e21b7f9c67">1b7f9c67</code>
</td>
<td>N/A</td>
<td>File Upload - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>
</div></article></div>
