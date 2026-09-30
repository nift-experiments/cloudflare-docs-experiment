<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 21, 2026</time><h2 id="post-title">WAF Release - 2026-04-21</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces a new detection for a Remote Code Execution (RCE) vulnerability in Apache ActiveMQ (CVE-2026-34197) and an updated signature for Magento 2 - Unrestricted File Upload. Alongside these detections, we are continuing our work on rule refinements to provide deeper security insights for our customers.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Apache ActiveMQ (CVE-2026-34197): A vulnerability in Apache ActiveMQ allows an unauthenticated, remote attacker to execute arbitrary code. This flaw occurs during the processing of specially crafted network packets, leading to potential full system compromise.</p>
</li>
<li>
<p>Magento 2 - Unrestricted File Upload - 2: This is a follow-up enhancement to our existing protections for Magento and Adobe Commerce.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code or gain full administrative control over affected servers. We strongly recommend applying official vendor patches for Apache ActiveMQ and Magento to address the underlying vulnerabilities.</p>
<p><strong>Continuous Rule Improvements</strong></p>
<p>We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.</p>
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
				<code class="nb-rule-id" title="ff8df24181aa4573a81be531ee159e2e">ee159e2e</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 8 - uri</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. Previous description was "Command Injection - Generic 8 - uri - Beta"</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9429b63c137247faadeb8a29a15308cf">a15308cf</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 8 - body - Beta</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Command Injection - Generic 8 - body" (ID:{" "}
				<code class="nb-rule-id" title="5b3ce84c099040c6a25cee2d413592e2">413592e2</code>). The rule previously known as "Command Injection - Generic 8" is now renamed to "Command Injection - Generic 8 - body".
</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="85aaf5db9e0c4237b87e837e958047ed">958047ed</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"MySQL - SQLi - Executable Comment - Body" (ID:{" "}
				<code class="nb-rule-id" title="8629bb58defe4193ab4d493c7bd2d8fa">7bd2d8fa</code>) The rule previously known as "MySQL - SQLi - Executable Comment" is now renamed to "MySQL - SQLi - Executable Comment - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d19cd574c4644952881a6f3a582cc559">582cc559</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="407f9ec8a17348dfba3b9450a16639d3">a16639d3</code>
</td>
<td>N/A</td>
<td>MySQL - SQLi - Executable Comment - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d07e6dbf15664b99b37b0d2544f24211">44f24211</code>
</td>
<td>N/A</td>
<td>Magento 2 - Unrestricted file upload - 2</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>     
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="26ef21cb197b44fc8a98b7cebf170a17">bf170a17</code>
</td>
<td>N/A</td>
<td>Apache ActiveMQ - Remote Code Execution - CVE:CVE-2026-34197</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7f7bc3d28a8e43bf97bd15d68c2ac1a7">8c2ac1a7</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Sleep Function" (ID:{" "}
				<code class="nb-rule-id" title="2c333735f7b24566b17cb64ef77e8d54">f77e8d54</code>)
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3872e5638bdf4bf0943a80394dacaeb8">4dacaeb8</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>   
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bebce8fadfa94ccab09eb74fed4c9ece">ed4c9ece</code>
</td>
<td>N/A</td>
<td>SQLi - Sleep Function - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7a40eed5a8654a50a2598a821dfa64df">1dfa64df</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - uri</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="15c6b2ce033949b2a1a9f9454c62e2e7">4c62e2e7</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - header</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fc9d800b7a724181af8d5650aab28ea1">aab28ea1</code>
</td>
<td>N/A</td>
<td>SQLi - Probing - body</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Probing" (ID: <code class="nb-rule-id" title="2c20b5e8684043f48620ff77b4026c88">b4026c88</code>)
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="945c5aa9f45141dd872d7ec920999be0">20999be0</code>
</td>
<td>N/A</td>
<td>SQLi - Probing 2 </td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule had duplicate detection logic and has been deprecated.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f1771273700342758e73cf16d7aa0008">d7aa0008</code>
</td>
<td>N/A</td>
<td>SQLi - UNION in MSSQL - Body</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule has been renamed to differentiate from "SQLi - UNION in MSSQL" (ID: <code class="nb-rule-id" title="ef7db598c7654c729d9db56fee5e35fd">ee5e35fd</code>) and contains updated rule logic.
</td>
</tr> 
<tr> 
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3ffd242b4ba242ca965022d3a67d8561">a67d8561</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 3</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This rule had duplicate detection logic and has been deprecated.
</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5e69d599ad634c81abe36a5f0af34bba">0af34bba</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Embed Tag  - URI</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2635275641bf44d4bad6a2e170282f38">70282f38</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Embed Tag - Headers</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b3d033ea9f364574b0a2ec4223f4d718">23f4d718</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - IFrame Tag - Src and Srcdoc Attributes - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="76c37816ef5c4997ab2080a36978def1">6978def1</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Link Tag - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7d6757e8a28f4853a72b4ce6ebd81645">ebd81645</code>
</td>
<td>N/A</td>
<td>XSS, HTML Injection - Link Tag - URI</td>
<td>Disabled</td>
<td>Disabled</td>
<td>
				This is a new detection. 
</td>
</tr>           
</tbody>
</table>
</div></article></div>
