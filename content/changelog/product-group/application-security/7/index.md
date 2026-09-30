<h1 id="changelog">Changelog</h1>

<h2 id="waf-release-2025-07-21"><a href="/changelog/post/2025-07-21-waf-release/">WAF Release - 2025-07-21</a></h2>
<p><em>2025-07-21</em></p>
<p>This week's update spotlights several critical vulnerabilities across Citrix NetScaler Memory Disclosure, FTP servers and network application. Several flaws enable unauthenticated remote code execution or sensitive data exposure, posing a significant risk to enterprise security.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Wing FTP Server (CVE-2025-47812): A critical Remote Code Execution (RCE) vulnerability that enables unauthenticated attackers to execute arbitrary code with root/SYSTEM-level privileges by exploiting a Lua injection flaw.</li>
<li>Infoblox NetMRI (CVE-2025-32813): A remote unauthenticated command injection flaw that allows an attacker to execute arbitrary commands, potentially leading to unauthorized access.</li>
<li>Citrix Netscaler ADC (CVE-2025-5777, CVE-2023-4966): A sensitive information disclosure vulnerability, also known as &quot;Citrix Bleed2&quot;, that allows the disclosure of memory and subsequent remote access session hijacking.</li>
<li>Akamai CloudTest (CVE-2025-49493): An XML External Entity (XXE) injection that could lead to read local files on the system by manipulating XML input.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities affect critical enterprise infrastructure, from file transfer services and network management appliances to application delivery controllers. The Wing FTP RCE and Infoblox command injection flaws offer direct paths to deep system compromise, while the Citrix &quot;Bleed2&quot; and Akamai XXE vulnerabilities undermine system integrity by enabling session hijacking and sensitive data theft.</p>
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
				<code class="nb-rule-id" title="6ab3bd3b58fb4325ac2d3cc73461ec9e">3461ec9e</code>
</td>
<td>100804</td>
<td>BerriAI - SSRF - CVE:CVE-2024-6587</td>
<td>Log</td>
<td>Log</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0e17d8761f1a47d5a744a75b5199b58a">5199b58a</code>
</td>
<td>100805</td>
<td>Wing FTP Server - Remote Code Execution - CVE:CVE-2025-47812</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="81ace5a851214a2f9c58a1e7919a91a4">919a91a4</code>
</td>
<td>100807</td>
<td>Infoblox NetMRI - Command Injection - CVE:CVE-2025-32813</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="cd8fa74e8f6f476c9380ae217899130f">7899130f</code>
</td>
<td>100808</td>
<td>Citrix Netscaler ADC - Buffer Error - CVE:CVE-2025-5777</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e012c7bece304a1daf80935ed1cf8e08">d1cf8e08</code>
</td>
<td>100809</td>
<td>Citrix Netscaler ADC - Information Disclosure - CVE:CVE-2023-4966</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5d348a573a834ffd968faffc6e70469f">6e70469f</code>
</td>
<td>100810</td>
<td>Akamai CloudTest - XXE - CVE:CVE-2025-49493</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="new-apis-for-brand-protection-setup"><a href="/changelog/post/2025-07-18-brand-protection-api/">New APIs for Brand Protection setup</a></h2>
<p><em>2025-07-18</em></p>
<hr />
<h4 id="2025-07-18-brand-protection-api-title-new-apis-for-brand-protection-setup-description-you-can-now-use-the-brand-protection-api-endpoints-to-manage-your-brand-protection-queries-date-2025-07-18">title: New APIs for Brand Protection setup
description: You can now use the Brand Protection API endpoints to manage your Brand Protection queries
date: 2025-07-18</h4>
<p>The Brand Protection API is now available, allowing users to create new queries and delete existing ones, fetch matches and more!</p>
<p>What you can do:</p>
<ul>
<li><strong>create new string or logo query</strong></li>
<li><strong>delete string or logo queries</strong></li>
<li><strong>download matches for both logo and string queries</strong></li>
<li><strong>read matches for both logo and string queries</strong></li>
</ul>
<p>Ready to start? Check out the <a href="/api/resources/brand_protection/">Brand Protection API</a> in our documentation.</p>


<h2 id="faster-more-reliable-udp-traffic-for-cloudflare-tunnel"><a href="/changelog/post/2025-07-15-udp-improvements/">Faster, more reliable UDP traffic for Cloudflare Tunnel</a></h2>
<p><em>2025-07-15</em></p>
<p>Your real-time applications running over <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> are now faster and more reliable. We've completely re-architected the way <code>cloudflared</code> proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.</p>
<p>This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Faster UDP performance</strong>: We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.</li>
<li><strong>Greater reliability for mixed traffic</strong>: UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.</li>
</ul>
<p>Learn more about running <a href="/reference-architecture/architectures/sase/#connecting-applications">TCP or UDP applications</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private networks</a> through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>


<h2 id="waf-release-2025-07-14"><a href="/changelog/post/2025-07-14-waf-release/">WAF Release - 2025-07-14</a></h2>
<p><em>2025-07-14</em></p>
<p>This week’s vulnerability analysis highlights emerging web application threats that exploit modern JavaScript behavior and SQL parsing ambiguities. Attackers continue to refine techniques such as attribute overloading and obfuscated logic manipulation to evade detection and compromise front-end and back-end systems.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>XSS – Attribute Overloading: A novel cross-site scripting technique where attackers abuse custom or non-standard HTML attributes to smuggle payloads into the DOM. These payloads evade traditional sanitization logic, especially in frameworks that loosely validate attributes or trust unknown tokens.</li>
<li>XSS – onToggle Event Abuse: Exploits the lesser-used onToggle event (triggered by elements like <code>&lt;details&gt; </code>) to execute arbitrary JavaScript when users interact with UI elements. This vector is often overlooked by static analyzers and can be embedded in seemingly benign components.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities target both user-facing components and back-end databases, introducing potential vectors for credential theft, session hijacking, or full data exfiltration. The XSS variants bypass conventional filters through overlooked HTML behaviors, while the obfuscated SQLi enables attackers to stealthily probe back-end logic, making them especially difficult to detect and block.</p>
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
				<code class="nb-rule-id" title="a8918353372b4191b10684eb2aa3d845">2aa3d845</code>
</td>
<td>100798</td>
<td>XSS - Attribute Overloading</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="31dd299ba375414dac9260c037548d06">37548d06</code>
</td>
<td>100799</td>
<td>XSS - OnToggle</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="increased-ip-list-limits-for-enterprise-accounts"><a href="/changelog/post/2025-07-07-increased-ip-list-limits/">Increased IP List Limits for Enterprise Accounts</a></h2>
<p><em>2025-07-07</em></p>
<p>We have significantly increased the limits for <a href="/waf/tools/lists/">IP Lists</a> on Enterprise plans to provide greater flexibility and control:</p>
<ul>
<li><strong>Total number of lists</strong>: Increased from 10 to 1,000.</li>
<li><strong>Total number of list items</strong>: Increased from 10,000 to 500,000.</li>
</ul>
<p>Limits for other list types and plans remain unchanged. For more details, refer to the <a href="/waf/tools/lists/#availability">lists availability</a>.</p>


<h2 id="waf-release-2025-07-07"><a href="/changelog/post/2025-07-07-waf-release/">WAF Release - 2025-07-07</a></h2>
<p><em>2025-07-07</em></p>
<p>This week’s roundup uncovers critical vulnerabilities affecting enterprise VoIP systems, webmail platforms, and a popular JavaScript framework. The risks range from authentication bypass to remote code execution (RCE) and buffer handling flaws, each offering attackers a path to elevate access or fully compromise systems.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Next.js - Auth Bypass: A newly detected authentication bypass flaw in the Next.js framework allows attackers to access protected routes or APIs without proper authorization, undermining application access controls.</li>
<li>Fortinet FortiVoice (CVE-2025-32756): A buffer error vulnerability in FortiVoice systems that could lead to memory corruption and potential code execution or service disruption in enterprise telephony environments.</li>
<li>Roundcube (CVE-2025-49113): A critical RCE flaw allowing unauthenticated attackers to execute arbitrary PHP code via crafted requests, leading to full compromise of mail servers and user inboxes.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities affect core business infrastructure, from web interfaces to voice communications and email platforms. The Roundcube RCE and FortiVoice buffer flaw offer potential for deep system access, while the Next.js auth bypass undermines trust boundaries in modern web apps.</p>
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
				<code class="nb-rule-id" title="b6558cac8c874bd6878734057eb35ee6">7eb35ee6</code>
</td>
<td>100795</td>
<td>Next.js - Auth Bypass</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58fcf6d9c05d4b7a8f41e0a3c329aeb0">c329aeb0</code>
</td>
<td>100796</td>
<td>Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="34ed0624bc864ea88bbea55bab314023">ab314023</code>
</td>
<td>100797</td>
<td>Roundcube - Remote Code Execution - CVE:CVE-2025-49113</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-06-16"><a href="/changelog/post/2025-06-16-waf-release/">WAF Release - 2025-06-16</a></h2>
<p><em>2025-06-16</em></p>
<p>This week’s roundup highlights multiple critical vulnerabilities across popular web frameworks, plugins, and enterprise platforms. The focus lies on remote code execution (RCE), server-side request forgery (SSRF), and insecure file upload vectors that enable full system compromise or data exfiltration.</p>
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


<h2 id="more-flexible-fallback-handling-custom-errors-now-support-fetching-assets-returned-with-4xx-or-5xx-status-codes"><a href="/changelog/post/2025-06-09-custom-errors-fetch-4xx-5xx-assets/">More flexible fallback handling — Custom Errors now support fetching assets returned with 4xx or 5xx status codes</a></h2>
<p><em>2025-06-09</em></p>
<p><a href="/rules/custom-errors/">Custom Errors</a> can now fetch and store <a href="/rules/custom-errors/create-rules/#create-a-custom-error-asset-dashboard">assets</a> and <a href="/rules/custom-errors/#error-pages">error pages</a> from your origin even if they are served with a 4xx or 5xx HTTP status code — previously, only 200 OK responses were allowed.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>You can now upload error pages and error assets that return error status codes (for example, 403, 500, 502, 503, 504) when fetched.</li>
<li>These assets are stored and minified at the edge, so they can be reused across multiple Custom Error rules without triggering requests to the origin.</li>
</ul>
<p>This is especially useful for retrieving error content or downtime banners from your backend when you can’t override the origin status code.</p>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors</a> documentation.</p>


<h2 id="match-workers-subrequests-by-upstream-zone-cf-worker-upstream-zone-now-supported-in-transform-rules"><a href="/changelog/post/2025-06-09-transform-rule-subrequest-matching/">Match Workers subrequests by upstream zone — cf.worker.upstream_zone now supported in Transform Rules</a></h2>
<p><em>2025-06-09</em></p>
<p>You can now use the <a href="/ruleset-engine/rules-language/fields/reference/cf.worker.upstream_zone/"><code>cf.worker.upstream_zone</code></a> field in <a href="/rules/transform/">Transform Rules</a> to control rule execution based on whether a request originates from <a href="/workers/">Workers</a>, including subrequests issued by Workers in other zones.</p>
<p><img src="/assets/upstream/images/changelog/rules/transform-rule-subrequest-matching.png" alt="Match Workers subrequests by upstream zone in Transform Rules" /></p>
<p><strong>What's new:</strong></p>
<ul>
<li><code>cf.worker.upstream_zone</code> is now supported in Transform Rules expressions.</li>
<li>Skip or apply logic conditionally when handling <a href="/workers/platform/limits/#subrequests">Workers subrequests</a>.</li>
</ul>
<p>For example, to add a header when the subrequest comes from another zone:</p>
<div class="nb-example"><h3 class="nb-component-title" id="2025-06-09-transform-rule-subrequest-matching-example">Example</h3>
@markup("md", "content/.markup/bodies/17746.md")</div>
<p>This gives you more granular control in how you handle incoming requests for your zone.</p>
<p>Learn more in the <a href="/rules/transform/">Transform Rules</a> documentation and <a href="/ruleset-engine/rules-language/fields/reference/">Rules language fields</a> reference.</p>


<h2 id="waf-release-2025-06-09"><a href="/changelog/post/2025-06-09-waf-release/">WAF Release - 2025-06-09</a></h2>
<p><em>2025-06-09</em></p>
<p>This week’s update spotlights four critical vulnerabilities across CMS platforms, VoIP systems, and enterprise applications. Several flaws enable remote code execution or privilege escalation, posing significant enterprise risks.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>WordPress OttoKit Plugin (CVE-2025-27007): Privilege escalation flaw allows unauthenticated attackers to create or elevate user accounts, compromising WordPress administrative control.</li>
<li>SAP NetWeaver (CVE-2025-42999): Remote Code Execution vulnerability enables attackers to execute arbitrary code on SAP NetWeaver systems, threatening core ERP and business operations.</li>
<li>Fortinet FortiVoice (CVE-2025-32756): Buffer error vulnerability may lead to memory corruption and potential code execution, directly impacting enterprise VoIP infrastructure.</li>
<li>Camaleon CMS (CVE-2024-46986): Remote Code Execution vulnerability allows attackers to gain full control over Camaleon CMS installations, exposing hosted content and underlying servers.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities target widely deployed CMS, ERP, and VoIP systems. RCE flaws in SAP NetWeaver and Camaleon CMS allow full takeover of business-critical applications. Privilege escalation in OttoKit exposes WordPress environments to full administrative compromise. FortiVoice buffer handling issues risk destabilizing or fully compromising enterprise telephony systems.</p>
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
				<code class="nb-rule-id" title="4afd50a3ef1948bba87c4e620debd86e">0debd86e</code>
</td>
<td>100769</td>
<td>
				WordPress OttoKit Plugin - Privilege Escalation - CVE:CVE-2025-27007
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="24134c41c3e940daa973b4b95f57b448">5f57b448</code>
</td>
<td>100770</td>
<td>SAP NetWeaver - Remote Code Execution - CVE:CVE-2025-42999</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4f219ac0be3545a5be5f0bf34df8857a">4df8857a</code>
</td>
<td>100779</td>
<td>Fortinet FortiVoice - Buffer Error - CVE:CVE-2025-32756</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bc8dfbe8cbac4c039725ec743b840107">3b840107</code>
</td>
<td>100780</td>
<td>Camaleon CMS - Remote Code Execution - CVE:CVE-2024-46986</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-06-02"><a href="/changelog/post/2025-06-02-waf-release/">WAF Release - 2025-06-02</a></h2>
<p><em>2025-06-02</em></p>
<p>This week’s roundup highlights five high-risk vulnerabilities affecting SD-WAN, load balancers, and AI platforms. Several flaws enable unauthenticated remote code execution or authentication bypass.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Versa Concerto SD-WAN (CVE-2025-34026, CVE-2025-34027): Authentication bypass vulnerabilities allow attackers to gain unauthorized access to SD-WAN management interfaces, compromising network segmentation and control.</li>
<li>Kemp LoadMaster (CVE-2024-7591): Remote Code Execution vulnerability enables attackers to execute arbitrary commands, potentially leading to full device compromise within enterprise load balancing environments.</li>
<li>AnythingLLM (CVE-2024-0759): Server-Side Request Forgery (SSRF) flaw allows external attackers to force the LLM backend to make unauthorized internal network requests, potentially exposing sensitive internal resources.</li>
<li>Anyscale Ray (CVE-2023-48022): Remote Code Execution vulnerability affecting distributed AI workloads, allowing attackers to execute arbitrary code on Ray cluster nodes.</li>
<li>Server-Side Request Forgery (SSRF) - Generic &amp; Obfuscated Payloads: Ongoing advancements in SSRF payload techniques observed, including obfuscation and expanded targeting of cloud metadata services and internal IP ranges.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose critical infrastructure across networking, AI platforms, and SaaS integrations. Unauthenticated RCE and auth bypass flaws in Versa Concerto, Kemp LoadMaster, and Anyscale Ray allow full system compromise. AnythingLLM and SSRF payload variants expand attack surfaces into internal cloud resources, sensitive APIs, and metadata services, increasing risk of privilege escalation, data theft, and persistent access.</p>
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
				<code class="nb-rule-id" title="752cfb5e6f9c46f0953c742139b52f02">39b52f02</code>
</td>
<td>100764</td>
<td>Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34027</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a01171de18034901b48a5549a34edb97">a34edb97</code>
</td>
<td>100765</td>
<td>Versa Concerto SD-WAN - Auth Bypass - CVE:CVE-2025-34026</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="840b35492a7543c18ffe50fc0d99b2db">0d99b2db</code>
</td>
<td>100766</td>
<td>Kemp LoadMaster - Remote Code Execution - CVE:CVE-2024-7591</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="121b7070de3a459dbe80d7ed95aa3a4f">95aa3a4f</code>
</td>
<td>100767</td>
<td>AnythingLLM - SSRF - CVE:CVE-2024-0759</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="215417f989e2485a9c50eca0840a0966">840a0966</code>
</td>
<td>100768</td>
<td>Anyscale Ray - Remote Code Execution - CVE:CVE-2023-48022</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3ed619a17d4141bda3a8c3869d16ee18">9d16ee18</code>
</td>
<td>100781</td>
<td>SSRF - Generic Payloads</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7ce73f6a70be49f8944737465c963d9d">5c963d9d</code>
</td>
<td>100782</td>
<td>SSRF - Obfuscated Payloads</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="fine-tune-image-optimization-webp-now-supported-in-configuration-rules"><a href="/changelog/post/2025-05-30-configuration-rules-webp/">Fine-tune image optimization — WebP now supported in Configuration Rules</a></h2>
<p><em>2025-05-30</em></p>
<p>You can now enable <a href="/images/polish/activate-polish/">Polish</a> with the <code>webp</code> format directly in <a href="/rules/configuration-rules/">Configuration Rules</a>, allowing you to optimize image delivery for specific routes, user agents, or A/B tests — without applying changes zone-wide.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/images/polish/compression/#webp">WebP</a> is now a supported <a href="/rules/configuration-rules/settings/#polish">value</a> in the <strong>Polish</strong> setting for Configuration Rules.</li>
</ul>
<p>This gives you more precise control over how images are compressed and delivered, whether you're targeting modern browsers, running experiments, or tailoring performance by geography or device type.</p>
<p>Learn more in the <a href="/images/polish/">Polish</a> and <a href="/rules/configuration-rules/">Configuration Rules</a> documentation.</p>


<h2 id="updated-attack-score-model"><a href="/changelog/post/2025-05-28-updated-attack-score-model/">Updated attack score model</a></h2>
<p><em>2025-05-28</em></p>
<p>We have deployed an updated attack score model focused on enhancing the detection of multiple false positives (FPs).</p>
<p>As a result of this improvement, some changes in observed attack scores are expected.</p>


<h2 id="increased-limits-for-cloudflare-for-saas-and-secrets-store-free-and-pay-as-you-go-plans"><a href="/changelog/post/2025-05-19-paygo-updates/">Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans</a></h2>
<p><em>2025-05-27T11:00:00+00:00</em></p>
<p>With upgraded limits to <a href="https://www.cloudflare.com/plans/">all free and paid plans</a>, you can now scale more easily with <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> and <a href="https://developers.cloudflare.com/secrets-store/">Secrets Store</a>.</p>
<p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/">limit for custom hostnames</a> on a Cloudflare for SaaS Pay-as-you-go plan has been <strong>raised from 5,000 custom hostnames to 50,000 custom hostnames.</strong></p>
<p>With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. <a href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">Custom origin server</a> is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.</p>
<p>You can enable custom origin server on a per-custom hostname basis <a href="https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/">via the API</a> or the UI:</p>
<p><img src="/assets/upstream/images/ssl/custom-origin-server.png" alt="Import repo or choose template" /></p>
<p>Currently <a href="https://blog.cloudflare.com/secrets-store-beta/">in beta with a Workers integration</a>, <a href="https://developers.cloudflare.com/secrets-store/">Cloudflare Secrets Store</a> allows you to store, manage, and deploy account level secrets from a secure, centralized platform your <a href="https://developers.cloudflare.com/workers/">Cloudflare Workers</a>. Now, you can create and deploy <strong>100 secrets per account</strong>. Try it out <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a>, with <a href="https://developers.cloudflare.com/secrets-store/integrations/workers/">Wrangler</a>, or <a href="https://developers.cloudflare.com/api/resources/secrets_store/">via the API</a> today.</p>


<h2 id="waf-release-2025-05-27"><a href="/changelog/post/2025-05-27-waf-release/">WAF Release - 2025-05-27</a></h2>
<p><em>2025-05-27</em></p>
<p>This week’s roundup covers nine vulnerabilities, including six critical RCEs and one dangerous file upload. Affected platforms span cloud services, CI/CD pipelines, CMSs, and enterprise backup systems. Several are now addressed by updated WAF managed rulesets.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Ingress-Nginx (CVE-2025-1098): Unauthenticated RCE via unsafe annotation handling. Impacts Kubernetes clusters.</li>
<li>GitHub Actions (CVE-2025-30066): RCE through malicious workflow inputs. Targets CI/CD pipelines.</li>
<li>Craft CMS (CVE-2025-32432): Template injection enables unauthenticated RCE. High risk to content-heavy sites.</li>
<li>F5 BIG-IP (CVE-2025-31644): RCE via TMUI exploit, allowing full system compromise.</li>
<li>AJ-Report (CVE-2024-15077): RCE through untrusted template execution. Affects reporting dashboards.</li>
<li>NAKIVO Backup (CVE-2024-48248): RCE via insecure script injection. High-value target for ransomware.</li>
<li>SAP NetWeaver (CVE-2025-31324): Dangerous file upload flaw enables remote shell deployment.</li>
<li>Ivanti EPMM (CVE-2025-4428, 4427): Auth bypass allows full access to mobile device management.</li>
<li>Vercel (CVE-2025-32421): Information leak via misconfigured APIs. Useful for attacker recon.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose critical components across Kubernetes, CI/CD pipelines, and enterprise systems to severe threats including unauthenticated remote code execution, authentication bypass, and information leaks. High-impact flaws in Ingress-Nginx, Craft CMS, F5 BIG-IP, and NAKIVO Backup enable full system compromise, while SAP NetWeaver and AJ-Report allow remote shell deployment and template-based attacks. Ivanti EPMM’s auth bypass further risks unauthorized control over mobile device fleets.</p>
<p>GitHub Actions and Vercel introduce supply chain and reconnaissance risks, allowing malicious workflow inputs and data exposure that aid in targeted exploitation. Organizations should prioritize immediate patching, enhance monitoring, and deploy updated WAF and IDS signatures to defend against likely active exploitation.</p>
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
				<code class="nb-rule-id" title="6a61a14f44af4232a44e45aad127592a">d127592a</code>
</td>
<td>100746</td>
<td>Vercel - Information Disclosure</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bd30b3c43eb44335ab6013c195442495">95442495</code>
</td>
<td>100754</td>
<td>AJ-Report - Remote Code Execution - CVE:CVE-2024-15077</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6a13bd6e5fc94b1d9c97eb87dfee7ae4">dfee7ae4</code>
</td>
<td>100756</td>
<td>NAKIVO Backup - Remote Code Execution - CVE:CVE-2024-48248</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a4af6f2f15c9483fa9eab01d1c52f6d0">1c52f6d0</code>
</td>
<td>100757</td>
<td>Ingress-Nginx - Remote Code Execution - CVE:CVE-2025-1098</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bd30b3c43eb44335ab6013c195442495">95442495</code>
</td>
<td>100759</td>
<td>SAP NetWeaver - Dangerous File Upload - CVE:CVE-2025-31324</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dab2df4f548349e3926fee845366ccc1">5366ccc1</code>
</td>
<td>100760</td>
<td>Craft CMS - Remote Code Execution - CVE:CVE-2025-32432</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb23f172ed64ee08895e161eb40686b">eb40686b</code>
</td>
<td>100761</td>
<td>GitHub Action - Remote Code Execution - CVE:CVE-2025-30066</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="827037f2d5f941789efcba6260fc041c">60fc041c</code>
</td>
<td>100762</td>
<td>Ivanti EPMM - Auth Bypass - CVE:CVE-2025-4428, CVE:CVE-2025-4427</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ddee6d1c4f364768b324609cebafdfe6">ebafdfe6</code>
</td>
<td>100763</td>
<td>F5 Big IP - Remote Code Execution - CVE:CVE-2025-31644</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-05-19"><a href="/changelog/post/2025-05-19-waf-release/">WAF Release - 2025-05-19</a></h2>
<p><em>2025-05-19</em></p>
<p>This week's analysis covers four vulnerabilities, with three rated critical due to their Remote Code Execution (RCE) potential. One targets a high-traffic frontend platform, while another targets a popular content management system. These detections are now part of the Cloudflare Managed Ruleset in <em>Block</em> mode.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Commvault Command Center (CVE-2025-34028) exposes an unauthenticated RCE via insecure command injection paths in the web UI. This is critical due to its use in enterprise backup environments.</li>
<li>BentoML (CVE-2025-27520) reveals an exploitable vector where serialized payloads in model deployment APIs can lead to arbitrary command execution. This targets modern AI/ML infrastructure.</li>
<li>Craft CMS (CVE-2024-56145) allows RCE through template injection in unauthenticated endpoints. It poses a significant risk for content-heavy websites with plugin extensions.</li>
<li>Apache HTTP Server (CVE-2024-38475) discloses sensitive server config data due to misconfigured
<code>mod_proxy</code> behavior. While not RCE, this is useful for pre-attack recon.</li>
</ul>
<p><strong>Impact</strong></p>
<p>These newly detected vulnerabilities introduce critical risk across modern web stacks, AI infrastructure, and content platforms: unauthenticated RCEs in Commvault, BentoML, and Craft CMS enable full system compromise with minimal attacker effort.</p>
<p>Apache HTTPD information leak can support targeted reconnaissance, increasing the success rate of follow-up exploits. Organizations using these platforms should prioritize patching and monitor for indicators of exploitation using updated WAF detection rules.</p>
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
				<code class="nb-rule-id" title="5c3559ad62994e5b932d7d0075129820">75129820</code>
</td>
<td>100745</td>
<td>Apache HTTP Server - Information Disclosure - CVE:CVE-2024-38475</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="28a22a685bba478d99bc904526a517f1">26a517f1</code>
</td>
<td>100747</td>
<td>
				Commvault Command Center - Remote Code Execution - CVE:CVE-2025-34028
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e6bb954d0634e368c49d7d1d7619ccb">d7619ccb</code>
</td>
<td>100749</td>
<td>BentoML - Remote Code Execution - CVE:CVE-2025-27520</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="91250eebec894705b62305b2f15bfda4">f15bfda4</code>
</td>
<td>100753</td>
<td>Craft CMS - Remote Code Execution - CVE:CVE-2024-56145</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="more-ways-to-match-snippets-now-support-custom-lists-bot-score-and-waf-attack-score"><a href="/changelog/post/2025-05-09-snippets-cloud-connector-lists-waf-bot-scores/">More ways to match — Snippets now support Custom Lists, Bot Score, and WAF Attack Score</a></h2>
<p><em>2025-05-09</em></p>
<p>You can now use IP, Autonomous System (AS), and Hostname <a href="/waf/tools/lists/custom-lists/">custom lists</a> to route traffic to <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a>, giving you greater precision and control over how you match and process requests at the edge.</p>
<p>In Snippets, you can now also match on <a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a>, unlocking smarter edge logic for everything from request filtering and mitigation to <a href="/rules/snippets/examples/slow-suspicious-requests/">tarpitting</a> and logging.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><a href="/waf/tools/lists/custom-lists/">Custom lists</a> matching – Snippets and Cloud Connector now support user-created IP, AS, and Hostname lists via dashboard or <a href="/api/resources/rules/subresources/lists/methods/list/">Lists API</a>. Great for shared logic across zones.</li>
<li><a href="/bots/concepts/bot-score/">Bot Score</a> and <a href="/waf/detections/attack-score/">WAF Attack Score</a> – Use Cloudflare’s intelligent traffic signals to detect bots or attacks and take advanced, tailored actions with just a few lines of code.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-lists-scores.png" alt="New fields in Snippets" /></p>
<p>These enhancements unlock new possibilities for building smarter traffic workflows with minimal code and maximum efficiency.</p>
<p>Learn more in the <a href="/rules/snippets/">Snippets</a> and <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


<h2 id="url-scanner-now-supports-geo-specific-scanning"><a href="/changelog/post/2025-05-07-url-scanner-geoegress/">URL Scanner now supports geo-specific scanning</a></h2>
<p><em>2025-05-08</em></p>
<p>Enterprise customers can now choose the geographic location from which a URL scan is performed — either via <a href="/security-center/investigate/">Security Center</a> in the Cloudflare dashboard or via the <a href="/api/resources/url_scanner/subresources/scans/methods/create/">URL Scanner API</a>.</p>
<p>This feature gives security teams greater insight into how a website behaves across different regions, helping uncover targeted, location-specific threats.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li>Location Picker: Select a location for the scan via <strong>Security Center → Investigate</strong> in the dashboard or through the API.</li>
<li>Region-aware scanning: Understand how content changes by location — useful for detecting regionally tailored attacks.</li>
<li>Default behavior: If no location is set, scans default to the user’s current geographic region.</li>
</ul>
<p>Learn more in the <a href="/security-center/">Security Center documentation</a>.</p>


<h2 id="improved-payload-logging-for-waf-managed-rules"><a href="/changelog/post/2025-05-08-improved-payload-logging/">Improved Payload Logging for WAF Managed Rules</a></h2>
<p><em>2025-05-08</em></p>
<p>We have upgraded WAF Payload Logging to enhance rule diagnostics and usability:</p>
<ul>
<li><strong>Targeted logging</strong>: Logs now capture only the specific portions of requests that triggered WAF rules, rather than entire request segments.</li>
<li><strong>Visual highlighting</strong>: Matched content is visually highlighted in the UI for faster identification.</li>
<li><strong>Enhanced context</strong>: Logs now include surrounding context to make diagnostics more effective.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/waf/2025-05-payload-logging-update.png" alt="Log entry showing payload logging details" /></p>
<p>Payload Logging is available to all Enterprise customers. If you have not used Payload Logging before, check how you can <a href="/waf/managed-rules/payload-logging/">get started</a>.</p>
<p><strong>Note:</strong> The structure of the <code>encrypted_matched_data</code> field in Logpush has changed from <code>Map&lt;Field, Value&gt;</code> to <code>Map&lt;Field, {Before: bytes, Content: Value, After: bytes}&gt;</code>. If you rely on this field in your Logpush jobs, you should review and update your processing logic accordingly.</p>


<h2 id="waf-release-2025-05-05"><a href="/changelog/post/2025-05-05-waf-release/">WAF Release - 2025-05-05</a></h2>
<p><em>2025-05-05</em></p>
<p>This week's analysis covers five CVEs with varying impact levels. Four are rated critical, while one is rated high severity. Remote Code Execution vulnerabilities dominate this set.</p>
<p><strong>Key Findings</strong></p>
<p>GFI KerioControl (CVE-2024-52875) contains an unauthenticated Remote Code Execution (RCE) vulnerability that targets firewall appliances. This vulnerability can let attackers gain root level system access, making this CVE particularly attractive for threat actors.</p>
<p>The SonicWall SMA vulnerabilities remain concerning due to their continued exploitation since 2021. These critical vulnerabilities in remote access solutions create dangerous entry points to networks.</p>
<p><strong>Impact</strong></p>
<p>Customers using the Managed Ruleset will receive rule coverage following this week's release. Below is a breakdown of the recommended prioritization based on current exploitation trends:</p>
<ul>
<li>GFI KerioControl (CVE-2024-52875) - Highest priority; unauthenticated RCE</li>
<li>SonicWall SMA (Multiple vulnerabilities) - Critical for network appliances</li>
<li>XWiki (CVE-2025-24893) - High priority for development environments</li>
<li>Langflow (CVE-2025-3248) - Important for AI workflow platforms</li>
<li>MinIO (CVE-2025-31489) - Important for object storage implementations</li>
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
				<code class="nb-rule-id" title="921660147baa48eaa9151077d0b7a392">d0b7a392</code>
</td>
<td>100724</td>
<td>GFI KerioControl - Remote Code Execution - CVE:CVE-2024-52875</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a3900934273b4a488111f810717a9e42">717a9e42</code>
</td>
<td>100748</td>
<td>XWiki - Remote Code Execution - CVE:CVE-2025-24893</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="616ad0e03892473191ca1df4e9cf745d">e9cf745d</code>
</td>
<td>100750</td>
<td>
				SonicWall SMA - Dangerous File Upload - CVE:CVE-2021-20040,
				CVE:CVE-2021-20041, CVE:CVE-2021-20042
</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1a11fbe84b49451193ee1ee6d29da333">d29da333</code>
</td>
<td>100751</td>
<td>Langflow - Remote Code Execution - CVE:CVE-2025-3248</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5eb7ed601e6844828b9bdb05caa7b208">caa7b208</code>
</td>
<td>100752</td>
<td>MinIO - Auth Bypass - CVE:CVE-2025-31489</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2025-04-26-emergency"><a href="/changelog/post/2025-04-26-emergency-waf-release/">WAF Release - 2025-04-26 - Emergency</a></h2>
<p><em>2025-04-26</em></p>
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
				<code class="nb-rule-id" title="54ea354d7f2d43c69b238d1419fcc883">19fcc883</code>
</td>
<td>100755</td>
<td>
				React.js - Router and Remix Vulnerability - CVE:CVE-2025-43864,
				CVE:CVE-2025-43865
</td>
<td>Block</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="custom-errors-are-now-generally-available"><a href="/changelog/post/2025-04-24-custom-errors-ga/">Custom Errors are now Generally Available</a></h2>
<p><em>2025-04-24</em></p>
<p><a href="/rules/custom-errors/">Custom Errors</a> are now generally available for all paid plans — bringing a unified and powerful experience for customizing error responses at both the zone and account levels.</p>
<p>You can now manage <strong>Custom Error Rules</strong>, <strong>Custom Error Assets</strong>, and redesigned <strong>Error Pages</strong> directly from the Cloudflare dashboard. These features let you deliver tailored messaging when errors occur, helping you maintain brand consistency and improve user experience — whether it’s a 404 from your origin or a security challenge from Cloudflare.</p>
<p>What's new:</p>
<ul>
<li><strong>Custom Errors are now GA</strong> – Available on all paid plans and ready for production traffic.</li>
<li><strong>UI for Custom Error Rules and Assets</strong> – Manage your zone-level rules from the Rules &gt; Overview and your zone-level assets from the Rules &gt; Settings tabs.</li>
<li><strong>Define inline content or upload assets</strong> – Create custom responses directly in the rule builder, upload new or reuse previously stored assets.</li>
<li><strong>Refreshed UI and new name for Error Pages</strong> – Formerly known as “Custom Pages,” Error Pages now offer a cleaner, more intuitive experience for both zone and account-level configurations.</li>
<li><strong>Powered by Ruleset Engine</strong> – Custom Error Rules support <a href="/ruleset-engine/rules-language/">conditional logic</a> and override Error Pages for 500 and 1000 class errors, as well as errors originating from your origin or <a href="/ruleset-engine/reference/phases-list/">other Cloudflare products</a>. You can also configure <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> to add, change, or remove HTTP headers from responses returned by Custom Error Rules.</li>
</ul>
<p>Learn more in the <a href="/rules/custom-errors/">Custom Errors documentation</a>.</p>


<h2 id="waf-release-2025-04-22"><a href="/changelog/post/2025-04-22-waf-release/">WAF Release - 2025-04-22</a></h2>
<p><em>2025-04-22</em></p>
<p>Each of this week's rule releases covers a distinct CVE, with half of the rules targeting Remote Code Execution (RCE) attacks. Of the 6 CVEs covered, four were scored as critical, with the other two scored as high.</p>
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


<h2 id="waf-release-2025-04-14"><a href="/changelog/post/2025-04-14-waf-release/">WAF Release - 2025-04-14</a></h2>
<p><em>2025-04-14</em></p>
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
				<code class="nb-rule-id" title="9209bb65527f4c088bca5ffad6b2d36c">d6b2d36c</code>
</td>
<td>100739A</td>
<td>Next.js - Auth Bypass - CVE:CVE-2025-29927 - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>


<h2 id="cloudflare-snippets-are-now-generally-available"><a href="/changelog/post/2025-04-09-snippets-ga/">Cloudflare Snippets are now Generally Available</a></h2>
<p><em>2025-04-09</em></p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-ga.png" alt="Cloudflare Snippets are now GA" /></p>
<p><a href="/rules/snippets/">Cloudflare Snippets</a> are now generally available at no extra cost across all paid plans — giving you a fast, flexible way to programmatically control HTTP traffic using lightweight JavaScript.</p>
<p>You can now use Snippets to modify HTTP requests and responses with confidence, reliability, and scale. Snippets are production-ready and deeply integrated with Cloudflare Rules, making them ideal for everything from quick dynamic header rewrites to advanced routing logic.</p>
<p>What's new:</p>
<ul>
<li><strong>Snippets are now GA</strong> – Available at no extra cost on all Pro, Business, and Enterprise plans.</li>
<li><strong>Ready for production</strong> – Snippets deliver a production-grade experience built for scale.</li>
<li><strong>Part of the Cloudflare Rules platform</strong> – Snippets inherit request modifications from other Cloudflare products and support sequential execution, allowing you to run multiple Snippets on the same request and apply custom modifications step by step.</li>
<li><strong>Trace integration</strong> – Use <a href="/rules/trace-request/">Cloudflare Trace</a> to see which Snippets were triggered on a request — helping you understand traffic flow and debug more effectively.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-ga-trace.gif" alt="Snippets shown in Cloudflare Trace results" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/snippets/">launch blog post</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-security/6/">Previous</a><span>Page 7 of 9</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-security/8/">Next</a></nav>
