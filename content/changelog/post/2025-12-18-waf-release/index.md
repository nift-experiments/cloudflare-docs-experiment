<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 18, 2025</time><h2 id="post-title">WAF Release - 2025-12-18</h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on improvements to existing detections to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
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
        <code class="nb-rule-id" title="6429f7386b1546cf9dfce631be5ec20c">be5ec20c</code>
</td>
<td>N/A</td>
<td>Atlassian Confluence - Code Injection - CVE:CVE-2021-26084 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Atlassian Confluence - Code Injection - CVE:CVE-2021-26084" (ID: <code class="nb-rule-id" title="e8c550810618437c953cf3a969e0b97a">69e0b97a</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9108ddb347b3497e9f9351640d9206e3">0d9206e3</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - Copy - Beta</td>
<td>Log</td>
<td>Block</td>      
<td>This rule is merged into the original rule "PostgreSQL - SQLi - COPY" (ID: <code class="nb-rule-id" title="705a6b5569d5472596910e3ce7265a4e">e7265a4e</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cb687d73cc954092b58b90b00cd00ba7">0cd00ba7</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Body</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="bf30657ffa2a424cbf6570dbcd679ad4">cd679ad4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Header</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6df040f716194070a242967cfd181fb3">fd181fb3</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="39a4fdc37be948709fa7492e7a95bc3a">7a95bc3a</code>
</td>
<td>N/A</td>
<td>SQLi - Tautology - URI - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Tautology - URI" (ID: <code class="nb-rule-id" title="4c580ea1b5174183b7f5e940b3de2e0a">b3de2e0a</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="810e0ffe1dd84e67b159129b432ac90d">432ac90d</code>
</td>
<td>N/A</td>
<td>SQLi - WaitFor Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - WaitFor Function" (ID: <code class="nb-rule-id" title="b16fe708799441dea3049a99d5faba59">d5faba59</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="80690005fef342e0ad6bc9af596c741e">596c741e</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit 2 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - AND/OR Digit Operator Digit" (ID: <code class="nb-rule-id" title="98e7e08ae64247e2801ca4b388d80772">88d80772</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="eaf11ab80b0d491cbb7186f303b2f3fe">03b2f3fe</code>
</td>
<td>N/A</td>
<td>SQLi - Equation 2 - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "SQLi - Equation" (ID: <code class="nb-rule-id" title="133c6f83cdf14509a4ca6b82a72a6b3a">a72a6b3a</code>)</td>
</tr>
</tbody>    
</table>
</div></article></div>
