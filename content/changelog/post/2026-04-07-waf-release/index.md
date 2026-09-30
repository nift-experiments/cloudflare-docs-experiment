<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 7, 2026</time><h2 id="post-title">WAF Release - 2026-04-07</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces new detections for a critical Remote Code Execution (RCE) vulnerability in MCP Server (CVE-2026-23744), alongside targeted protection for an authentication bypass vulnerability in SolarWinds products (CVE-2025-40552). Additionally, this release includes a new generic detection rule designed to identify and block Cross-Site Scripting (XSS) injection attempts leveraging &quot;OnEvent&quot; handlers within HTTP cookies.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>MCP Server (CVE-2026-23744): A vulnerability in the Model Context Protocol (MCP) server implementation where malformed input payloads can trigger a memory corruption state, allowing for arbitrary code execution.</p>
</li>
<li>
<p>SolarWinds (CVE-2025-40552): A critical flaw in the authentication module allows unauthenticated attackers to bypass security filters and gain unauthorized access to the management console due to improper identity token validation.</p>
</li>
<li>
<p>XSS OnEvents Cookies: This generic rule identifies malicious event handlers (such as onload or onerror) embedded within HTTP cookie values.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of the MCP Server and SolarWinds vulnerabilities could allow unauthenticated attackers to execute arbitrary code or gain administrative control, leading to a full system takeover. Additionally, the new generic XSS detection prevents attackers from leveraging browser event handlers in cookies to hijack user sessions or execute malicious scripts.</p>
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
				<code class="nb-rule-id" title="73ae1cf103da4bacaa2e1a610aa410af">0aa410af</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a88a85b0cc5a4bc2abead6289131ec2f">9131ec2f</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - Header</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="28518cdc40544979bbd86720551eb9e5">551eb9e5</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1177993d53a1467997002b44d46229eb">d46229eb</code>
</td>
<td>N/A</td>
<td>MCP Server - Remote Code Execution - CVE:CVE-2026-23744</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3d43cdfbc3c14584942f8bc4a864b9c2">a864b9c2</code>
</td>
<td>N/A</td>
<td>XSS - OnEvents - Cookies</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c9dbce2c1da94b24916e37559712a863">9712a863</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="64d812e6d5844d7c9d7a44a440732d48">40732d48</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="50de9369ef7c45928a5dfb34e68a99b5">e68a99b5</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="765ffb5c67b94c9589106c843e8143d2">3e8143d2</code>
</td>
<td>N/A</td>
<td>SQLi - LIKE 3 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5c3dbd4f115e47c781491fcd70e7fb97">70e7fb97</code>
</td>
<td>N/A</td>
<td>SQLi - LIKE 3 - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89fa6027a0334949b1cb2e654c538bd9">4c538bd9</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 2 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="05946b3458364f1b9d4819d561c439c9">61c439c9</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 2 - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b2fe5c2a39df4609b6d39908cf33ea10">cf33ea10</code>
</td>
<td>N/A</td>
<td>SolarWinds - Auth Bypass - CVE:CVE-2025-40552</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div></article></div>
