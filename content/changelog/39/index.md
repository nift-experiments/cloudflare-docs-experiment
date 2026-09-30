<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-07-28">Jul 28, 2025</time><div>
<h2 id="post-2025-07-28-waf-release"><a href="/changelog/post/2025-07-28-waf-release/">WAF Release - 2025-07-28</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s update spotlights several vulnerabilities across Apache Tomcat, MongoDB, and Fortinet FortiWeb. Several flaws related with a memory leak in Apache Tomcat can lead to a denial-of-service attack. Additionally, a code injection flaw in MongoDB's Mongoose library allows attackers to bypass security controls to access restricted data.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Fortinet FortiWeb (CVE-2025-25257): An improper neutralization of special elements used in a SQL command vulnerability in Fortinet FortiWeb versions allows an unauthenticated attacker to execute unauthorized SQL code or commands.</p>
</li>
<li>
<p>Apache Tomcat (CVE-2025-31650): A improper Input Validation vulnerability in Apache Tomcat that could create memory leak when incorrect error handling for some invalid HTTP priority headers resulted in incomplete clean-up of the failed request.</p>
</li>
<li>
<p>MongoDB (CVE-2024-53900, CVE:CVE-2025-23061): Improper use of <code>$where</code> in match and a nested <code>$where</code> filter with a <code>populate()</code> match in Mongoose can lead to search injection.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities target user-facing components, web application servers, and back-end databases. A SQL injection flaw in Fortinet FortiWeb can lead to data theft or system compromise. A separate issue in Apache Tomcat involves a memory leak from improper input validation, which could be exploited for a denial-of-service (DoS) attack. Finally, a vulnerability in MongoDB's Mongoose library allows attackers to bypass security filters and access unauthorized data through malicious search queries.</p>
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
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2e6c4d02f42a4c3ca90649d50cb13e1d">0cb13e1d</code>
</td>
<td>100812</td>
<td>Fortinet FortiWeb - Remote Code Execution - CVE:CVE-2025-25257</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fd360d8fd9994e6bab6fb06067fae7f7">67fae7f7</code>
</td>
<td>100813</td>
<td>Apache Tomcat - DoS - CVE:CVE-2025-31650</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f9e01e28c5d6499cac66364b4b6a5bb1">4b6a5bb1</code>
</td>
<td>100815</td>
<td>MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="700d4fcc7b1f481a80cbeee5688f8e79">688f8e79</code>
</td>
<td>100816</td>
<td>MongoDB - Remote Code Execution - CVE:CVE-2024-53900, CVE:CVE-2025-23061</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-24">Jul 24, 2025</time><div>
<h2 id="post-2025-07-24-HTTP-Inspection-on-all-ports"><a href="/changelog/post/2025-07-24-HTTP-Inspection-on-all-ports/">Gateway HTTP Filtering on all ports available in open BETA</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p><a href="/cloudflare-one/traffic-policies/">Gateway</a> can now apply <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP filtering</a> to all proxied HTTP requests, not just traffic on standard HTTP (<code>80</code>) and HTTPS (<code>443</code>) ports. This means all requests can now be filtered by <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">A/V scanning</a>, <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">file sandboxing</a>, <a href="/cloudflare-one/data-loss-prevention/#data-in-transit">Data Loss Prevention (DLP)</a>, and more.</p>
<p>You can turn this <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">setting</a> on by going to <strong>Settings</strong> &gt; <strong>Network</strong> &gt; <strong>Firewall</strong> and choosing  <em>Inspect on all ports</em>.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-Inspection-all-ports.png" alt="HTTP Inspection on all ports setting" /></p>
<p>To learn more, refer to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">Inspect on all ports (Beta)</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-22">Jul 22, 2025</time><div>
<h2 id="post-2025-07-22-br-local-dev"><a href="/changelog/post/2025-07-22-br-local-dev/">Browser Rendering now supports local development</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p>You can now run your Browser Rendering locally using <code>npx wrangler dev</code>, which spins up a browser directly on your machine before deploying to Cloudflare's global network. By running tests locally, you can quickly develop, debug, and test changes without needing to deploy or worry about usage costs.</p>
<p>Get started with this <a href="/browser-run/how-to/deploy-worker/">example guide</a> that shows how to use Cloudflare's <a href="/browser-run/puppeteer/">fork of Puppeteer</a> (you can also use <a href="/browser-run/playwright/">Playwright</a>) to take screenshots of webpages and store the results in <a href="/kv/">Workers KV</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-22">Jul 22, 2025</time><div>
<h2 id="post-2025-07-23-workers-preview-urls"><a href="/changelog/post/2025-07-23-workers-preview-urls/">Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Now, when you connect your Cloudflare Worker to a git repository on GitHub or GitLab, each branch of your repository has its own stable preview URL, that you can use to preview code changes before merging the pull request and deploying to production.</p>
<p>This works the same way that Cloudflare Pages does — every time you create a pull request, you'll automatically get a shareable preview link where you can see your changes running, without affecting production. The link stays the same, even as you add commits to the same branch.
These preview URLs are named after your branch and are posted as a comment to each pull request. The URL stays the same with every commit and always points to the latest version of that branch.</p>
<p><img src="/assets/upstream/images/changelog/workers/preview-urls-comment.png" alt="PR comment preview" /></p>
<h4 id="2025-07-23-workers-preview-urls-preview-url-types">Preview URL types</h4>
<p>Each comment includes <strong>two preview URLs</strong> as shown above:</p>
<ul>
<li><strong>Commit Preview URL</strong>: Unique to the specific version/commit (e.g., <code>&lt;version-prefix&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
<li><strong>Branch Preview URL</strong>: A stable alias based on the branch name (e.g., <code>&lt;branch-name&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
</ul>
<h4 id="2025-07-23-workers-preview-urls-how-it-works">How it works</h4>
<p>When you create a pull request:</p>
<ul>
<li><strong>A preview alias is automatically created</strong> based on the Git branch name (e.g., <code>&lt;branch-name&gt;</code> becomes <code>&lt;branch-name&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
<li><strong>No configuration is needed</strong>, the alias is generated for you</li>
<li><strong>The link stays the same</strong> even as you add commits to the same branch</li>
<li><strong>Preview URLs are posted directly to your pull request as comments</strong> (just like they are in Cloudflare Pages)</li>
</ul>
<h4 id="2025-07-23-workers-preview-urls-custom-alias-name">Custom alias name</h4>
<p>You can also assign a custom preview alias using the <a href="/workers/wrangler/">Wrangler CLI</a>, by passing the <code>--preview-alias</code> flag when <a href="/workers/wrangler/commands/general/#versions-upload">uploading a version</a> of your Worker:</p>
<pre><code class="language-bash">wrangler versions upload --preview-alias staging&#10;</code></pre>
<h4 id="2025-07-23-workers-preview-urls-limitations-while-in-beta">Limitations while in beta</h4>
<ul>
<li>Only available on the <strong>workers.dev</strong> subdomain (custom domains not yet supported)</li>
<li>Requires <strong>Wrangler v4.21.0+</strong></li>
<li>Preview URLs are not generated for Workers that use <a href="/durable-objects/">Durable Objects</a></li>
<li>Not yet supported for <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-22">Jul 22, 2025</time><div>
<h2 id="post-2025-08-15-gemini-application-replaces-bard"><a href="/changelog/post/2025-08-15-gemini-application-replaces-bard/">Google Bard Application replaced by Gemini</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>The <strong>Google Bard</strong> application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the <strong>Gemini</strong> application (ID: 1340).
Any existing Gateway policies that reference the old Google Bard application will no longer function.
To ensure your policies continue to work as intended, you should update them to use the new Gemini application.
We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies.
For more information about application policies, please see the <a href="/cloudflare-one/traffic-policies/application-app-types/">Cloudflare Gateway documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-22">Jul 22, 2025</time><div>
<h2 id="post-2025-07-22-media-transformations-audio-mode"><a href="/changelog/post/2025-07-22-media-transformations-audio-mode/">Audio mode for Media Transformations</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>We now support <code>audio</code> mode! Use this feature to extract audio from a source video, outputting
an M4A file to use in downstream workflows like <a href="/workers-ai/">AI inference</a>, content moderation, or transcription.</p>
<p>For example,</p>
<pre><code class="language-text">https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;https://example.com/cdn-cgi/media/mode=audio,time=3s,duration=60s/&lt;input video with diction&gt;&#10;</code></pre>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-21">Jul 21, 2025</time><div>
<h2 id="post-2025-07-21-virtual-appliance-kvm-proxmox"><a href="/changelog/post/2025-07-21-virtual-appliance-kvm-proxmox/">Virtual Cloudflare One Appliance with KVM support (open beta)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>The KVM-based virtual Cloudflare One Appliance is now in open beta with official support for Proxmox VE.</p>
<p>Customers can deploy the virtual appliance on KVM hypervisors to connect branch or data center networks to Cloudflare WAN without dedicated hardware.</p>
<p>For setup instructions, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a virtual Cloudflare One Appliance</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-21">Jul 21, 2025</time><div>
<h2 id="post-2025-07-21-subaddressing"><a href="/changelog/post/2025-07-21-subaddressing/">Subaddressing support in Email Routing</a></h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>Subaddressing, as defined in <a href="https://www.rfc-editor.org/rfc/rfc5233">RFC 5233</a>, also known as plus addressing, is now supported in Email Routing. This enables using the &quot;+&quot; separator to augment your custom addresses with arbitrary detail information.</p>
<p>Now you can send an email to <code>user+detail@example.com</code> and it will be captured by the <code>user@example.com</code> custom address. The <code>+detail</code> part is ignored by Email Routing, but it can be captured next in the processing chain in the logs, an <a href="/email-service/api/route-emails/email-handler/">Email Worker</a> or an <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">Agent application</a>.</p>
<p>Customers can use this feature to dynamically add context to their emails, such as tracking the source of an email or categorizing emails without needing to create multiple custom addresses.</p>
<p><img src="/assets/upstream/images/changelog/email-service/subaddressing.png" alt="Subaddressing" /></p>
<p>Check our <a href="/email-service/configuration/email-routing-addresses/#subaddressing">Developer Docs</a> to learn how to enable subaddressing in Email Routing.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-21">Jul 21, 2025</time><div>
<h2 id="post-2025-07-21-emergency"><a href="/changelog/post/2025-07-21-emergency/">WAF Release - 2025-07-21 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's update highlights several high-impact vulnerabilities affecting Microsoft SharePoint Server. These flaws, involving unsafe deserialization, allow unauthenticated remote code execution over the network, posing a critical threat to enterprise environments relying on SharePoint for collaboration and document management.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Microsoft SharePoint Server (CVE-2025-53770): A critical vulnerability involving unsafe deserialization of untrusted data, enabling unauthenticated remote code execution over the network. This flaw allows attackers to execute arbitrary code on vulnerable SharePoint servers without user interaction.</li>
<li>Microsoft SharePoint Server (CVE-2025-53771): A closely related deserialization issue that can be exploited by unauthenticated attackers, potentially leading to full system compromise. The vulnerability highlights continued risks around insecure serialization logic in enterprise collaboration platforms.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Together, these vulnerabilities significantly weaken the security posture of on-premise Microsoft SharePoint Server deployments. By enabling remote code execution without authentication, they open the door for attackers to gain persistent access, deploy malware, and move laterally across enterprise environments.</p>
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
					<code class="nb-rule-id" title="34dac2b38b904163bc587cc32168f6f0">2168f6f0</code>
</td>
<td>100817</td>
<td>Microsoft SharePoint - Deserialization - CVE:CVE-2025-53770</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
 					<code class="nb-rule-id" title="d21f327516a145bc9d1b05678de656c4">8de656c4</code>
</td>
<td>100818</td>
<td>Microsoft SharePoint - Deserialization - CVE:CVE-2025-53771</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
<p>For more details, also refer to <a href="https://blog.cloudflare.com/cloudflare-protects-against-critical-sharepoint-vulnerability-cve-2025-53770/">our blog</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-21">Jul 21, 2025</time><div>
<h2 id="post-2025-07-21-waf-release"><a href="/changelog/post/2025-07-21-waf-release/">WAF Release - 2025-07-21</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's update spotlights several critical vulnerabilities across Citrix NetScaler Memory Disclosure, FTP servers and network application. Several flaws enable unauthenticated remote code execution or sensitive data exposure, posing a significant risk to enterprise security.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-18">Jul 18, 2025</time><div>
<h2 id="post-2025-07-18-brand-protection-api"><a href="/changelog/post/2025-07-18-brand-protection-api/">New APIs for Brand Protection setup</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><hr />
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-17">Jul 17, 2025</time><div>
<h2 id="post-2025-07-17-vite-plugin-vite-7-support"><a href="/changelog/post/2025-07-17-vite-plugin-vite-7-support/">The Cloudflare Vite plugin now supports Vite 7</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="https://vite.dev/blog/announcing-vite7">Vite 7</a> is now supported in the Cloudflare Vite plugin.
See the <a href="https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#700-2025-06-24">Vite changelog</a> for a list of changes.</p>
<p>Note that the minimum Node.js versions supported by Vite 7 are 20.19 and 22.12.
We continue to support Vite 6 so you do not need to immediately upgrade.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-17">Jul 17, 2025</time><div>
<h2 id="post-2025-07-17-document-matching"><a href="/changelog/post/2025-07-17-document-matching/">New detection entry type: Document Matching for DLP</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now create <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#document-entries">document-based</a> detection entries in DLP by uploading example documents. Cloudflare will encrypt your documents and create a unique fingerprint of the file. This fingerprint is then used to identify similar documents or snippets within your organization's traffic and stored files.</p>
<p><img src="/assets/upstream/images/changelog/dlp/document-match.png" alt="DLP" /></p>
<p><strong>Key features and benefits:</strong></p>
<ul>
<li>
<p><strong>Upload documents, forms, or templates:</strong> Easily upload .docx and .txt files (up to 10 MB) that contain sensitive information you want to protect.</p>
</li>
<li>
<p><strong>Granular control with similarity percentage:</strong> Define a minimum similarity percentage (0-100%) that a document must meet to trigger a detection, reducing false positives.</p>
</li>
<li>
<p><strong>Comprehensive coverage:</strong> Apply these document-based detection entries in:</p>
<ul>
<li>
<p><strong>Gateway policies:</strong> To inspect network traffic for sensitive documents as they are uploaded or shared.</p>
</li>
<li>
<p><strong>CASB (Cloud Access Security Broker):</strong> To scan files stored in cloud applications for sensitive documents at rest.</p>
</li>
</ul>
</li>
<li>
<p><strong>Identify sensitive data:</strong> This new detection entry type is ideal for identifying sensitive data within completed forms, templates, or even small snippets of a larger document, helping you prevent data exfiltration and ensure compliance.</p>
</li>
</ul>
<p>Once uploaded and processed, you can add this new document entry into a DLP profile and policies to enhance your data protection strategy.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-15">Jul 15, 2025</time><div>
<h2 id="post-2025-07-15-udp-improvements"><a href="/changelog/post/2025-07-15-udp-improvements/">Faster, more reliable UDP traffic for Cloudflare Tunnel</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>Your real-time applications running over <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> are now faster and more reliable. We've completely re-architected the way <code>cloudflared</code> proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.</p>
<p>This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Faster UDP performance</strong>: We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.</li>
<li><strong>Greater reliability for mixed traffic</strong>: UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.</li>
</ul>
<p>Learn more about running <a href="/reference-architecture/architectures/sase/#connecting-applications">TCP or UDP applications</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private networks</a> through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-14">Jul 14, 2025</time><div>
<h2 id="post-2025-07-11-terraform-v5.7.0-provider"><a href="/changelog/post/2025-07-11-terraform-v5.7.0-provider/">Terraform v5.7.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release, with 13.5% of resources impacted. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and relability, including the v5.7 release.</p>
<p>Thank you for continuing to raise issues and please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-changes">Changes</h4>
- Addressed permanent diff bug on Cloudflare Tunnel config
- State is now saved correctly for Zero Trust Access applications
- Exact match is now working as expected within `data.cloudflare_zero_trust_access_applications`
- `cloudflare_zero_trust_access_policy` now supports OIDC claims & diff issues resolved
- Self hosted applications with private IPs no longer require a public domain for `cloudflare_zero_trust_access_application`.
- New resource:
  - `cloudflare_zero_trust_tunnel_warp_connector`
- Other bug fixes
<p>For a more detailed look at all of the changes, see the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.7.0">changelog</a> in GitHub.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-issues-closed">Issues Closed</h4>
- [#5563: cloudflare_logpull_retention is missing import](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5563)
- [#5608: cloudflare_zero_trust_access_policy in 5.5.0 provider gives error upon apply unexpected new value: .app_count: was cty.NumberIntVal(0), but now cty.NumberIntVal(1)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5608)
- [#5612: data.cloudflare_zero_trust_access_applications does not exact match](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5612)
- [#5532: cloudflare_zero_trust_access_identity_provider detects changes on every plan](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5532)
- [#5662: cloudflare_zero_trust_access_policy does not support OIDC claims](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5662)
- [#5565: Running Terraform with the cloudflare_zero_trust_access_policy resource results in updates on every apply, even when no changes are made - breaks idempotency](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5565)
- [#5529: cloudflare_zero_trust_access_application: self hosted applications with private ips require public domain ](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5529)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-upgrading">Upgrading</h4>
<p>We suggest holding on migration to v5 while we work on stabilization of the v5 provider. This will ensure Cloudflare can work ahead and avoid any blocking issues.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the
<a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have
provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which
use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our
<a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-07-11-terraform-v5.7.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-14">Jul 14, 2025</time><div>
<h2 id="post-2025-07-14-waf-release"><a href="/changelog/post/2025-07-14-waf-release/">WAF Release - 2025-07-14</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s vulnerability analysis highlights emerging web application threats that exploit modern JavaScript behavior and SQL parsing ambiguities. Attackers continue to refine techniques such as attribute overloading and obfuscated logic manipulation to evade detection and compromise front-end and back-end systems.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-10">Jul 10, 2025</time><div>
<h2 id="post-2025-07-09-onboarding-resources"><a href="/changelog/post/2025-07-09-onboarding-resources/">New onboarding guides for Zero Trust</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>Use our brand new onboarding experience for Cloudflare Zero Trust. New and returning users can now engage with a <strong>Get Started</strong> tab with walkthroughs for setting up common use cases end-to-end.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/zt-onboarding-guides.png" alt="Zero Trust onboarding guides" /></p>
<p>There are eight brand new onboarding guides in total:</p>
<ul>
<li>Securely access a private network (sets up device client and Tunnel)</li>
<li>Device-to-device / mesh networking (sets up and connects multiple device clients)</li>
<li>Network to network connectivity (sets up and connects multiple WARP Connectors, makes reference to Magic WAN availability for Enterprise)</li>
<li>Secure web traffic (sets up device client, Gateway, pre-reqs, and initial policies)</li>
<li>Secure DNS for networks (sets up a new DNS location and Gateway policies)</li>
<li>Clientless web access (sets up Access to a web app, Tunnel, and public hostname)</li>
<li>Clientless SSH access (all the same + the web SSH experience)</li>
<li>Clientless RDP access (all the same + RDP-in-browser)</li>
</ul>
<p>Each flow walks the user through the steps to configure the essential elements, and provides a “more details” panel with additional contextual information about what the user will accomplish at the end, along with why the steps they take are important.</p>
<p>Try them out now in the <a href="https://one.dash.cloudflare.com/?to=/:account/home">Zero Trust dashboard</a>!</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-09">Jul 9, 2025</time><div>
<h2 id="post-2025-07-09-usage-tracking"><a href="/changelog/post/2025-07-09-usage-tracking/">Usage tracking</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p><a href="/log-explorer/">Log Explorer</a> customers can now monitor their data ingestion volume to keep track of their billing. Monthly usage is displayed at the top of the <a href="/log-explorer/log-search/">Log Search</a> and <a href="/log-explorer/manage-datasets/">Manage Datasets</a> screens in Log Explorer.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/ingested-data.png" alt="Ingested data" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-08">Jul 8, 2025</time><div>
<h2 id="post-2025-07-08-autorag-jobs-view"><a href="/changelog/post/2025-07-08-autorag-jobs-view/">Faster indexing and new Jobs view in AutoRAG</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>You can now expect <strong>3-5× faster indexing</strong> in AutoRAG, and with it, a brand new <strong>Jobs view</strong> to help you monitor indexing progress.</p>
<p>With each AutoRAG, indexing jobs are automatically triggered to sync your data source (i.e. R2 bucket) with your Vectorize index, ensuring new or updated files are reflected in your query results. You can also trigger jobs manually via the <a href="/api/resources/ai-search/subresources/rags/">Sync API</a> or by clicking “Sync index” in the dashboard.</p>
<p>With the new jobs observability, you can now:</p>
<ul>
<li>View the status, job ID, source, start time, duration and last sync time for each indexing job</li>
<li>Inspect real-time logs of job events (e.g. <code>Starting indexing data source...</code>)</li>
<li>See a history of past indexing jobs under the Jobs tab of your AutoRAG</li>
</ul>
<p>This makes it easier to understand what’s happening behind the scenes.</p>
<p><strong>Coming soon:</strong> We’re adding APIs to programmatically check indexing status, making it even easier to integrate AutoRAG into your workflows.</p>
<p>Try it out today on the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-08">Jul 8, 2025</time><div>
<h2 id="post-heic-support"><a href="/changelog/post/heic-support/">HEIC support in Cloudflare Images</a></h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>You can use Images to ingest HEIC images and serve them in supported output formats like AVIF, WebP, JPEG, and PNG.</p>
<p>When inputting a HEIC image, dimension and sizing limits may still apply. Refer to our documentation to see limits for <a href="/images/storage/upload-images/methods/">uploading to Images</a> or <a href="/images/optimization/transformations/overview/">transforming a remote image</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-07">Jul 7, 2025</time><div>
<h2 id="post-2025-07-07-cloudy-summaries-access-gateway"><a href="/changelog/post/2025-07-07-cloudy-summaries-access-gateway/">Cloudy summaries for Access and Gateway Logs</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>Cloudy, Cloudflare's AI Agent, will now automatically summarize your <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access</a> and <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway</a> block logs.</p>
<p>In the log itself, Cloudy will summarize what occurred and why. This will be helpful for quick troubleshooting and issue correlation.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cloudy-explanation.png" alt="Cloudy AI summarizes a log" /></p>
<p>If you have feedback about the Cloudy summary - good or bad - you can provide that right from the summary itself.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-07">Jul 7, 2025</time><div>
<h2 id="post-2025-07-07-dashboard-app-library"><a href="/changelog/post/2025-07-07-dashboard-app-library/">New App Library for Zero Trust Dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>Cloudflare Zero Trust customers can use the App Library to get full visibility over the SaaS applications that they use in their Gateway policies, CASB integrations, and Access for SaaS applications.</p>
<p><strong>App Library</strong>, found under <strong>My Team</strong>, makes information available about all Applications that can be used across the Zero Trust product suite.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/app-library.png" alt="Zero Trust App Library" /></p>
<p>You can use the App Library to see:</p>
<ul>
<li>How Applications are defined</li>
<li>Where they are referenced in policies</li>
<li>Whether they have Access for SaaS configured</li>
<li>Review their CASB findings and integration status.</li>
</ul>
<p>Within individual Applications, you can also track their usage across your organization, and better understand user behavior.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-07">Jul 7, 2025</time><div>
<h2 id="post-2025-07-07-increased-ip-list-limits"><a href="/changelog/post/2025-07-07-increased-ip-list-limits/">Increased IP List Limits for Enterprise Accounts</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>We have significantly increased the limits for <a href="/waf/tools/lists/">IP Lists</a> on Enterprise plans to provide greater flexibility and control:</p>
<ul>
<li><strong>Total number of lists</strong>: Increased from 10 to 1,000.</li>
<li><strong>Total number of list items</strong>: Increased from 10,000 to 500,000.</li>
</ul>
<p>Limits for other list types and plans remain unchanged. For more details, refer to the <a href="/waf/tools/lists/#availability">lists availability</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-07">Jul 7, 2025</time><div>
<h2 id="post-2025-07-07-waf-release"><a href="/changelog/post/2025-07-07-waf-release/">WAF Release - 2025-07-07</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s roundup uncovers critical vulnerabilities affecting enterprise VoIP systems, webmail platforms, and a popular JavaScript framework. The risks range from authentication bypass to remote code execution (RCE) and buffer handling flaws, each offering attackers a path to elevate access or fully compromise systems.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-04">Jul 4, 2025</time><div>
<h2 id="post-2025-07-04-javascript-debug-terminals"><a href="/changelog/post/2025-07-04-javascript-debug-terminals/">Workers now supports JavaScript debug terminals in VSCode, Cursor and Windsurf IDEs</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers now support breakpoint debugging using VSCode's built-in <a href="https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_javascript-debug-terminal">JavaScript Debug Terminals</a>. All you have to do is open a JS debug terminal (<code>Cmd + Shift + P</code> and then type <code>javascript debug</code>) and run <code>wrangler dev</code> (or <code>vite dev</code>) from within the debug terminal. VSCode will automatically connect to your running Worker (even if you're running multiple Workers at once!) and start a debugging session.</p>
<p>In 2023 we announced <a href="https://blog.cloudflare.com/debugging-cloudflare-workers/">breakpoint debugging support</a> for Workers, which meant that you could easily debug your Worker code in Wrangler's built-in devtools (accessible via the <code>[d]</code> hotkey) as well as multiple other devtools clients, <a href="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/">including VSCode</a>. For most developers, breakpoint debugging via VSCode is the most natural flow, but until now it's required <a href="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/#setup-vs-code-to-use-breakpoints">manually configuring a <code>launch.json</code> file</a>, running <code>wrangler dev</code>, and connecting via VSCode's built-in debugger. Now it's much more seamless!</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/38/">Previous</a><span>Page 39 of 50</span><a class="pagination-next" rel="next" href="/changelog/40/">Next</a></nav>
</div>
