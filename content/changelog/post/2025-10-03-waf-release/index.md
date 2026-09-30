<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 3, 2025</time><h2 id="post-title">WAF Release - 2025-10-03</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>Managed Ruleset Updated</strong></p>
<p>This update introduces 21 new detections in the Cloudflare Managed Ruleset (all currently set to Disabled mode to preserve remediation logic and allow quick activation if needed). The rules cover a broad spectrum of threats - SQL injection techniques, command and code injection, information disclosure of common files, URL anomalies, and cross-site scripting.</p>
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
        <code class="nb-rule-id" title="0d02c2fb14eb4cec9c2e2b58d61fac74">d61fac74</code>
</td>
<td>100902</td>
<td>Generic Rules - Command Execution - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c3079865ce9a41368657026b514aeeb8">514aeeb8</code>
</td>
<td>100908</td>
<td>Generic Rules - Command Execution - 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="107ae2922b654bb28df7ca978d46a6f4">8d46a6f4</code>
</td>
<td>100910</td>
<td>Generic Rules - Command Execution - 4</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="68bdb75ae6d24e139a83e5731bd0a329">1bd0a329</code>
</td>
<td>100915</td>
<td>Generic Rules - Command Execution - 5</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ea04bb580f7d400386c7dc1d5e51450a">5e51450a</code>
</td>
<td>100899</td>
<td>Generic Rules - Content-Type Abuse</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="233364f656ff42b8acc41dcd7996012f">7996012f</code>
</td>
<td>100914</td>
<td>Generic Rules - Content-Type Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1aa695281c954513be3d003b93209312">93209312</code>
</td>
<td>100911</td>
<td>Generic Rules - Cookie Header Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d9f9e4f5bf11489da52dccb40f373b3f">0f373b3f</code>
</td>
<td>100905</td>
<td>Generic Rules - NoSQL Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5a1897b714e044a887c0f3f078a0ed04">78a0ed04</code>
</td>
<td>100913</td>
<td>Generic Rules - NoSQL Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4d6fd28df4f1494e95e70d2c5d649624">5d649624</code>
</td>
<td>100907</td>
<td>Generic Rules - Parameter Pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="61181e3af5304f7396c7d01cfd1c674e">fd1c674e</code>
</td>
<td>100906</td>
<td>Generic Rules - PHP Object Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ed5190bfbe1b45a6a645126334c88168">34c88168</code>
</td>
<td>100904</td>
<td>Generic Rules - Prototype Pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="3ec33bc5ac77495a9f55020e3ab43f7e">3ab43f7e</code>
</td>
<td>100897</td>
<td>Generic Rules - Prototype Pollution 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="c6d752c4909e4b7e8eff6c780d94ee22">0d94ee22</code>
</td>
<td>100903</td>
<td>Generic Rules - Reverse Shell</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="caf37e7800bb4635bcc2eefcd5add8e3">d5add8e3</code>
</td>
<td>100909</td>
<td>Generic Rules - Reverse Shell - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="475d090baead467c88dfabbb565c78b0">565c78b0</code>
</td>
<td>100898</td>
<td>Generic Rules - SSJI NoSQL</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="f4c7f98934264c9c937eec1212b837a0">12b837a0</code>
</td>
<td>100896</td>
<td>Generic Rules - SSRF</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="efd01b814d144e90b36522b311c4fb00">11c4fb00</code>
</td>
<td>100895</td>
<td>Generic Rules - Template Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="00a9a0d663da4add95b863abd3ed0123">d3ed0123</code>
</td>
<td>100895A</td>
<td>Generic Rules - Template Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e58c0fffee4f4374bd37f2577501a1d9">7501a1d9</code>
</td>
<td>100912</td>
<td>Generic Rules - XXE</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab09ba8d00eb4cdbb7a6a65ddc55cdb6">dc55cdb6</code>
</td>
<td>100900</td>
<td>Relative Paths - Anomaly Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div></article></div>
