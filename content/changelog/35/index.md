<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-25-sso-for-all"><a href="/changelog/post/2025-09-25-sso-for-all/">SSO for all</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Single sign-on (SSO) streamlines the process of logging into Cloudflare for Enterprise customers who manage a custom email domain and manage their own identity provider. Instead of managing a password and two-factor authentication credentials directly for Cloudflare, SSO lets you reuse your existing login infrastructure to seamlessly log in. SSO also provides additional security opportunities such as device health checks which are not available natively within Cloudflare.</p>
<p>Historically, SSO was only available for Enterprise accounts. Today, we are announcing that we are making SSO available to all users for free. We have also added the ability to directly manage SSO configurations using the API. This removes the previous requirement to contact support to configure SSO.</p>
<h4 id="2025-09-25-sso-for-all-for-more-information">For more information</h4>
<ul>
<li><a href="https://blog.cloudflare.com/enterprise-grade-features-for-all/">Every Cloudflare feature, available to all</a></li>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Configure Dashboard SSO</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-25">Sep 25, 2025</time><div>
<h2 id="post-2025-09-25-data-catalog-compaction"><a href="/changelog/post/2025-09-25-data-catalog-compaction/">R2 Data Catalog now supports compaction</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p>You can now enable automatic compaction for <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a> to improve query performance.</p>
<p>Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.</p>
<p>To enable automatic compaction in R2 Data Catalog, find it under <strong>R2 Data Catalog</strong> in your R2 bucket settings in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/r2/compaction.png" alt="compaction-dash" /></p>
<p>Or with <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre><code class="language-bash">npx wrangler r2 bucket catalog compaction enable &lt;BUCKET_NAME&gt;  --target-size 128 --token &lt;API_TOKEN&gt;&#10;</code></pre>
<p>To get started with compaction, check out <a href="/r2-data-catalog/manage-catalogs/">manage catalogs</a>. For best practices and limitations, refer to <a href="/r2-data-catalog/table-maintenance/">about compaction</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-24">Sep 24, 2025</time><div>
<h2 id="post-2025-09-24-emergency-waf-release"><a href="/changelog/post/2025-09-24-emergency-waf-release/">WAF Release - 2025-09-24 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights a critical vendor-specific vulnerability: a deserialization flaw in the License Servlet of Fortra’s GoAnywhere MFT. By forging a license response signature, an attacker can trigger deserialization of arbitrary objects, potentially leading to command injection.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>GoAnywhere MFT (CVE-2025-10035): Deserialization vulnerability in the License Servlet that allows attackers with a forged license response signature to deserialize arbitrary objects, potentially resulting in command injection.</li>
</ul>
<p><strong>Impact</strong></p>
<p>GoAnywhere MFT (CVE-2025-10035): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.</p>
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
        <code class="nb-rule-id" title="8fe242c7c0d64d689f4fc9a1e08b39f3">e08b39f3</code>
</td>
<td>100787</td>
<td>Fortra GoAnywhere - Auth Bypass - CVE:CVE-2025-10035</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-24">Sep 24, 2025</time><div>
<h2 id="post-2025-09-23-invalid-submissions"><a href="/changelog/post/2025-09-23-invalid-submissions/">Invalid Submissions Feedback</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Email security relies on your submissions to continuously improve our detection models. However, we often receive submissions in formats that cannot be ingested, such as incomplete EMLs, screenshots, or text files.</p>
<p>To ensure all customer feedback is actionable, we have launched two new features to manage invalid submissions sent to our team and user <a href="/cloudflare-one/email-security/settings/phish-submissions/submission-addresses/">submission aliases</a>:</p>
<ul>
<li><strong>Email Notifications:</strong> We now automatically notify users by email when they provide an invalid submission, educating them on the correct format. To disable notifications, go to <strong><a href="https://one.dash.cloudflare.com/?to=/:account/email-security/settings">Settings</a></strong> &gt; <strong>Invalid submission emails</strong> and turn the feature off.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/EmailSec-Invalid-Submissions-Toggle.png" alt="EmailSec-Invalid-Submissions-Toggle" /></p>
<ul>
<li><strong>Invalid Submission dashboard:</strong> You can quickly identify which users need education to provide valid submissions so Cloudflare can provide continuous protection.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/email-security/EmailSec-Invalid-Submissions-Dashboard.png" alt="EmailSec-Invalid-Submissions-Dashboard" /></p>
<p>Learn more about this feature on <a href="/cloudflare-one/email-security/submissions/invalid-submissions/">invalid submissions</a>.</p>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-23">Sep 23, 2025</time><div>
<h2 id="post-2025-09-23-wrangler-dev-multi-config-cross-command-support"><a href="/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/">Improved support for running multiple Workers with `wrangler dev`</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can run multiple Workers in a single dev command by passing multiple config files to <code>wrangler dev</code>:</p>
<pre><code class="language-sh">wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc&#10;</code></pre>
<p>Previously, if you ran the command above and then also ran wrangler dev for a different Worker, the Workers running in separate wrangler dev sessions could not communicate with each other. This prevented you from being able to use <a href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> and <a href="https://developers.cloudflare.com/workers/observability/logs/tail-workers/">Tail Workers</a> in local development, when running separate wrangler dev sessions.</p>
<p>Now, the following works as expected:</p>
<pre><code class="language-sh">&#35; Terminal 1: Run your application that includes both Web and API workers&#10;wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc&#10;&#10;&#35; Terminal 2: Run your auth worker separately&#10;wrangler dev --config ./auth/wrangler.jsonc&#10;</code></pre>
<p>These Workers can now communicate with each other across separate dev commands, regardless of your development setup.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		// This service binding call now works across dev commands&#10;		const authorized = await env.AUTH.isAuthorized(request);&#10;&#10;		if (!authorized) {&#10;			return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;		}&#10;&#10;		return new Response(&quot;Hello from API Worker!&quot;, { status: 200 });&#10;	},&#10;};&#10;</code></pre>
<p>Check out the <a href="/workers/local-development/multi-workers">Developing with multiple Workers</a> guide to learn more about the different approaches and when to use each one.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-22">Sep 22, 2025</time><div>
<h2 id="post-2025-09-22-browser-based-rdp-ga"><a href="/changelog/post/2025-09-22-browser-based-rdp-ga/">Access Remote Desktop Protocol (RDP) destinations securely from your browser — now generally available!</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is now generally available for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.</p>
<p>Since we announced our <a href="/changelog/access/#2025-06-30">open beta</a>, we've made a few improvements:</p>
<ul>
<li>Support for targets with IPv6.</li>
<li>Support for <a href="/cloudflare-wan/">Magic WAN</a> and <a href="/mesh/">WARP Connector</a> as on-ramps.</li>
<li>More robust error messaging on the login page to help you if you encounter an issue.</li>
<li>Worldwide keyboard support. Whether your day-to-day is in Portuguese, Chinese, or something in between, your browser-based RDP experience will look and feel exactly like you are using a desktop RDP client.</li>
<li>Cleaned up some other miscellaneous issues, including but not limited to enhanced support for Entra ID accounts and support for usernames with spaces, quotes, and special characters.</li>
</ul>
<p>As a refresher, here are some benefits browser-based RDP provides:</p>
<ul>
<li><strong>Control how users authenticate to internal RDP resources</strong> with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.</li>
<li><strong>Record who is accessing which servers and when</strong> to support regulatory compliance requirements and to gain greater visibility in the event of a security event.</li>
<li><strong>Eliminate the need to install and manage software on user devices</strong>. You will only need a web browser.</li>
<li><strong>Reduce your attack surface</strong> by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/browser-based-rdp-access-app.png" alt="Example of a browser-based RDP Access application" /></p>
<p>To get started, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Connect to RDP in a browser</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-22">Sep 22, 2025</time><div>
<h2 id="post-2025-09-22-waf-release"><a href="/changelog/post/2025-09-22-waf-release/">WAF Release - 2025-09-22</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week emphasizes two critical vendor-specific vulnerabilities: a full elevation-of-privilege in Microsoft Azure Networking (CVE-2025-54914) and a server-side template injection (SSTI) leading to remote code execution (RCE) in Skyvern (CVE-2025-49619). These are complemented by enhancements in generic detections (SQLi, SSRF) to improve baseline coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Azure (CVE-2025-54914): Vulnerability in Azure Networking allowing elevation of privileges.</p>
</li>
<li>
<p>Skyvern (CVE-2025-49619): Skyvern ≤ 0.1.85 has a server-side template injection (SSTI) vulnerability in its Prompt field (workflow blocks) via Jinja2. Authenticated users with low privileges can get remote code execution (blind).</p>
</li>
<li>
<p>Generic SQLi / SSRF improvements: Expanded rule coverage to detect obfuscated SQL injection patterns and SSRF across host, local, and cloud contexts.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities allow attackers to escalate privileges or execute code under conditions where previously they could not:</p>
<ul>
<li>
<p>Azure CVE-2025-54914 enables an attacker from the network with no credentials to gain high-level access within Azure Networking; could lead to full compromise of networking components.</p>
</li>
<li>
<p>Skyvern CVE-2025-49619 allows authenticated users with minimal privilege to exploit SSTI for remote code execution, undermining isolation of workflow components.</p>
</li>
<li>
<p>The improvements for SQLi and SSRF reduce risk from common injection and request-based attacks.</p>
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
        <code class="nb-rule-id" title="c36a425ae0c94789a9bc34f06a135cbf">6a135cbf</code>
</td>
<td>100146</td>
<td>SSRF - Host - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="dfa84b0aed5a4b45b953a36a57035abf">57035abf</code>
</td>
<td>100146B</td>
<td>SSRF - Local - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="276073e60c7a4b4d91faba1fbbe18d50">bbe18d50</code>
</td>
<td>100146C</td>
<td>SSRF - Cloud - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="78c856218f2d40f4b5988c8c956c1961">956c1961</code>
</td>
<td>100714</td>
<td>Azure - Auth Bypass - CVE:CVE-2025-54914</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="9f1c8d4cbf3848dbb940771bc5ced231">c5ced231</code>
</td>
<td>100758</td>
<td>Skyvern - Remote Code Execution - CVE:CVE-2025-49619</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6be7e7829f3b43c688e1ac4284a619a1">84a619a1</code>
</td>
<td>100773</td>
<td>Next.js - SSRF</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="0cc3f50216bf4b448210bcc3983ff2dd">983ff2dd</code>
</td>
<td>100774</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="53bfaeb311a049e3877fa15c0380a1a6">0380a1a6</code>
</td>
<td>100800_BETA</td>
<td>SQLi - Obfuscated Boolean - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule has been merged into the original rule (ID: <code class="nb-rule-id" title="7663ea44178441a0b3205c145563445f">5563445f</code>)</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-19">Sep 19, 2025</time><div>
<h2 id="post-2025-09-19-autorag-metrics"><a href="/changelog/post/2025-09-19-autorag-metrics/">New Metrics View in AutoRAG</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AutoRAG</a> now includes a <strong>Metrics</strong> tab that shows how your data is indexed and searched. Get a clear view of the health of your indexing pipeline, compare usage between <code>ai-search</code> and <code>search</code>, and see which files are retrieved most often.</p>
<p><img src="/assets/upstream/images/ai-search/metrics.png" alt="Metrics" /></p>
<p>You can find these metrics within each AutoRAG instance:</p>
<ul>
<li>Indexing: Track how files are ingested and see status changes over time.</li>
<li>Search breakdown: Compare usage between <code>ai-search</code> and <code>search</code> endpoints.</li>
<li>Top file retrievals: Identify which files are most frequently retrieved in a given period.</li>
</ul>
<p>Try it today in <a href="/ai-search/get-started/">AutoRAG</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-19">Sep 19, 2025</time><div>
<h2 id="post-2025-09-19-ratelimit-workers-ga"><a href="/changelog/post/2025-09-19-ratelimit-workers-ga/">Rate Limiting in Workers is now GA</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/runtime-apis/bindings/rate-limit/">Rate Limiting within Cloudflare Workers</a> is now Generally Available (GA).</p>
<p>The <code>ratelimit</code> binding is now stable and recommended for all production workloads. Existing deployments using the unsafe binding will continue to function to allow for a smooth transition.</p>
<p>For more details, refer to <a href="/workers/runtime-apis/bindings/rate-limit/">Workers Rate Limiting</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-19">Sep 19, 2025</time><div>
<h2 id="post-2025-09-19-workers-rs-panic-recovery"><a href="/changelog/post/2025-09-19-workers-rs-panic-recovery/">Panic Recovery for Rust Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>In <a href="https://github.com/cloudflare/workers-rs">workers-rs</a>, Rust panics were previously non-recoverable. A panic would put the Worker into an invalid state, and further function calls could result in memory overflows or exceptions.</p>
<p>Now, when a panic occurs, in-flight requests will throw 500 errors, but the Worker will automatically and instantly recover for future requests.</p>
<p>This ensures more reliable deployments. Automatic panic recovery is enabled for all new workers-rs deployments as of version 0.6.5, with no configuration required.</p>
<h4 id="2025-09-19-workers-rs-panic-recovery-fixing-rust-panics-with-wasm-bindgen">Fixing Rust Panics with Wasm Bindgen</h4>
<p>Rust Workers are built with Wasm Bindgen, which treats panics as non-recoverable. After a panic, the entire Wasm application is considered to be in an invalid state.</p>
<p>We now attach a default panic handler in Rust:</p>
<pre><code class="language-rust">std::panic::set_hook(Box::new(move |panic_info| {&#10;  hook_impl(panic_info);&#10;}));&#10;</code></pre>
<p>Which is registered by default in the JS initialization:</p>
<pre><code class="language-js">import { setPanicHook } from &quot;./index.js&quot;;&#10;setPanicHook(function (err) {&#10;	console.error(&quot;Panic handler!&quot;, err);&#10;});&#10;</code></pre>
<p>When a panic occurs, we reset the Wasm state to revert the Wasm application to how it was when the application started.</p>
<h4 id="2025-09-19-workers-rs-panic-recovery-resetting-vm-state-in-wasm-bindgen">Resetting VM State in Wasm Bindgen</h4>
<p>We worked upstream on the Wasm Bindgen project to implement a new <a href="https://github.com/wasm-bindgen/wasm-bindgen/pull/4644"><code>--experimental-reset-state-function</code> compilation option</a> which outputs a new <code>__wbg_reset_state</code> function.</p>
<p>This function clears all internal state related to the Wasm VM, and updates all function bindings in place to reference the new WebAssembly instance.</p>
<p>One other necessary change here was associating Wasm-created JS objects with an instance identity. If a JS object created by an earlier instance is then passed into a new instance later on, a new &quot;stale object&quot; error is specially thrown when using this feature.</p>
<h4 id="2025-09-19-workers-rs-panic-recovery-layered-solution">Layered Solution</h4>
<p>Building on this new Wasm Bindgen feature, layered with our new default panic handler, we also added a proxy wrapper to ensure all top-level exported class instantiations (such as for Rust Durable Objects) are tracked and fully reinitialized when resetting the Wasm instance. This was necessary because
the workerd runtime will instantiate exported classes, which would then be associated with the Wasm instance.</p>
<p>This approach now provides full panic recovery for Rust Workers on subsequent requests.</p>
<p>Of course, we never want panics, but when they do happen they are isolated and can be investigated further from the error logs - avoiding broader service disruption.</p>
<h4 id="2025-09-19-workers-rs-panic-recovery-webassembly-exception-handling">WebAssembly Exception Handling</h4>
<p>In the future, full support for recoverable panics could be implemented without needing reinitialization at all, utilizing the <a href="https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md">WebAssembly Exception Handling</a>
proposal, part of the newly announced <a href="https://webassembly.org/news/2025-09-17-wasm-3.0/">WebAssembly 3.0</a> specification. This would allow unwinding panics as normal JS errors, and concurrent requests would no longer fail.</p>
<p><strong>We're making significant improvements to the reliability of <a href="https://github.com/cloudflare/workers-rs">Rust Workers</a>. Join us in <code>#rust-on-workers</code> on the <a href="https://discord.gg/cloudflaredev">Cloudflare Developers Discord</a> to stay updated.</strong></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-18">Sep 18, 2025</time><div>
<h2 id="post-2025-09-18-tunnel-hostname-routing"><a href="/changelog/post/2025-09-18-tunnel-hostname-routing/">Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>You can now route private traffic to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is <strong>free for all Cloudflare One customers</strong>.</p>
<p>Previously, Tunnel routes could only be defined by IP address or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">CIDR range</a>. This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/tunnel-hostname-routing.webp" alt="Hostname-based routing in Cloudflare Tunnel" /></p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Hostname &amp; Domain Routing</strong>: Create routes for individual hostnames (e.g., <code>payroll.acme.local</code>) or entire domains (e.g., <code>*.acme.local</code>) and direct their traffic to a specific Tunnel.</li>
<li><strong>Simplified Zero Trust Policies</strong>: Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.</li>
<li><strong>Precise Egress Control</strong>: Route traffic for public hostnames (e.g., <code>bank.example.com</code>) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.</li>
<li><strong>No More IP Lists</strong>: This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.</li>
</ul>
<p>Get started in the Tunnels section of the Zero Trust dashboard with your first <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> or <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> route.</p>
<p>Learn more in our <a href="https://blog.cloudflare.com/tunnel-hostname-routing/">blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-18">Sep 18, 2025</time><div>
<h2 id="post-2025-09-07-builds-increased-cpu-paid"><a href="/changelog/post/2025-09-07-builds-increased-cpu-paid/">Increased vCPU for Workers Builds on paid plans</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We recently <a href="/changelog/2025-08-04-builds-increased-disk-size/">increased the available disk space</a> from 8 GB to 20 GB for <strong>all</strong> plans. Building on that improvement, we’re now doubling the CPU power available for paid plans — from 2 vCPU to <strong>4 vCPU</strong>.</p>
<p>These changes continue our focus on making <a href="/workers/ci-cd/builds/">Workers Builds</a> faster and more reliable.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Free Plan</th>
<th>Paid Plans</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU</td>
<td>2 vCPU</td>
<td><strong>4 vCPU</strong></td>
</tr>
</tbody>
</table>
<h4 id="2025-09-07-builds-increased-cpu-paid-performance-improvements">Performance Improvements</h4>
- **Fast build times**: Even single-threaded workloads benefit from having more vCPUs 
- **2x faster multi-threaded builds**: Tools like [esbuild](https://esbuild.github.io/) and [webpack](https://webpack.js.org/) can now utilize additional cores, delivering near-linear performance scaling
<p>All other <a href="/workers/ci-cd/builds/limits-and-pricing/">build limits</a> — including memory, build minutes, and timeout remain unchanged.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-17">Sep 17, 2025</time><div>
<h2 id="post-2025-09-17-update-preview-url-setting"><a href="/changelog/post/2025-09-17-update-preview-url-setting/">Preview URLs now default to opt-in</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>To prevent the accidental exposure of applications, we've updated how <a href="/workers/versions-and-deployments/preview-urls/">Worker preview URLs</a> (<code>&lt;PREVIEW&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>) are handled. We made this change to ensure preview URLs are only active when intentionally configured, improving the default security posture of your Workers.</p>
<h4 id="2025-09-17-update-preview-url-setting-one-time-update-for-workers-with-workers-dev-disabled">One-Time Update for Workers with workers.dev Disabled</h4>
We performed a one-time update to disable preview URLs for existing Workers where the [workers.dev subdomain](/workers/configuration/routing/workers-dev/) was also disabled.
<p>Because preview URLs were historically enabled by default, users who had intentionally disabled their workers.dev route may not have realized their Worker was still accessible at a separate preview URL. This update was performed to ensure that using a preview URL is always an intentional, opt-in choice.</p>
<p>If your Worker was affected, its preview URL (<code>&lt;PREVIEW&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>) will now direct to an informational page explaining this change.</p>
<p><strong>How to Re-enable Your Preview URL</strong></p>
<p>If your preview URL was disabled, you can re-enable it <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">via the Cloudflare dashboard</a> by navigating to your Worker's Settings page and toggling on the Preview URL.</p>
<p>Alternatively, you can use Wrangler by adding the <code>preview_urls = true</code> setting to your Wrangler file and redeploying the Worker.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17788.md")</div>
<p><strong>Note:</strong> You can set <code>preview_urls = true</code> with any Wrangler version that supports the preview URL flag (v3.91.0+). However, we recommend updating to v4.34.0 or newer, as this version defaults <code>preview_urls</code> to false, ensuring preview URLs are always enabled by explicit choice.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-16">Sep 16, 2025</time><div>
<h2 id="post-2025-09-16-new-ai-enabled-search-for-zero-trust-dashboard"><a href="/changelog/post/2025-09-16-new-ai-enabled-search-for-zero-trust-dashboard/">New AI-Enabled Search for Zero Trust Dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>Zero Trust Dashboard has a brand new, AI-powered search functionality. You can search your account by resources (applications, policies, device profiles, settings, etc.), pages, products, and more.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/searchexample.png" alt="Example search results in the Zero Trust dashboard" /></p>
<p><strong>Ask Cloudy</strong> — You can also ask Cloudy, our AI agent, questions about Cloudflare Zero Trust. Cloudy is trained on our developer documentation and implementation guides, so it can tell you how to configure functionality, best practices, and can make recommendations.</p>
<p>Cloudy can then stay open with you as you move between pages to build configuration or answer more questions.</p>
<p><strong>Find Recents</strong> — Recent searches and Cloudy questions also have a new tab under Zero Trust Overview.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-16">Sep 16, 2025</time><div>
<h2 id="post-2025-09-16-DNSFW-Analytics-UI"><a href="/changelog/post/2025-09-16-DNSFW-Analytics-UI/">DNS Firewall Analytics — now in the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><h4 id="2025-09-16-DNSFW-Analytics-UI-what-s-new">What's New</h4>
<p>Access <a href="/dns/dns-firewall/analytics/">GraphQL-powered DNS Firewall analytics</a> directly in the Cloudflare dashboard.</p>
<p><img src="/assets/upstream/images/changelog/dns/DNSFW_Analytics_UI.png" alt="DNS Firewall Analytics UI" /></p>
<h4 id="2025-09-16-DNSFW-Analytics-UI-explore-four-interactive-panels">Explore Four Interactive Panels</h4>
<ul>
<li><strong>Query summary</strong>: Describes trends over time, segmented by dimensions.</li>
<li><strong>Query statistics</strong>: Describes totals, cached/uncached queries, and processing/response times.</li>
<li><strong>DNS queries by data center</strong>: Describes global view and the top 10 data centers.</li>
<li><strong>Top query statistics</strong>: Shows a breakdown by key dimensions, with search and expand options (up to top 100 items).</li>
</ul>
<p>Additional features:</p>
<ul>
<li>Apply filters and time ranges once. Changes reflect across all panels.</li>
<li>Filter by dimensions like query name, query type, cluster, data center, protocol (UDP/TCP), IP version, response code/reason, and more.</li>
<li>Access up to 62 days of historical data with flexible intervals.</li>
</ul>
<h4 id="2025-09-16-DNSFW-Analytics-UI-availability">Availability</h4>
<p>Available to all DNS Firewall customers as part of their existing subscription.</p>
<h4 id="2025-09-16-DNSFW-Analytics-UI-where-to-find-it">Where to Find It</h4>
<ul>
<li>In the Cloudflare dashboard, go to the <strong>DNS Firewall</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>Refer to the <a href="/dns/dns-firewall/analytics/">DNS Firewall Analytics</a> to learn more.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-16">Sep 16, 2025</time><div>
<h2 id="post-2025-09-16-remote-bindings-ga"><a href="/changelog/post/2025-09-16-remote-bindings-ga/">Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Three months ago <a href="/changelog/2025-06-18-remote-bindings-beta/">we announced the public beta</a> of <a href="/workers/local-development/#remote-bindings">remote bindings</a> for local development. Now, we're excited to say that it's available for everyone in Wrangler, Vite, and Vitest without using an experimental flag!</p>
<p>With remote bindings, you can now connect to deployed resources like <a href="/r2/">R2 buckets</a> and <a href="/d1/">D1 databases</a> while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.</p>
<h4 id="2025-09-16-remote-bindings-ga-example-configuration">Example configuration</h4>
<p>To enable remote bindings, add <code>&quot;remote&quot; : true</code> to each binding that you want to rely on a remote resource running on Cloudflare:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17787.md")</div>
<p>When remote bindings are configured, your Worker <strong>still executes locally</strong>, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.</p>
<p><strong>You can <a href="/workers/local-development/#remote-bindings">try out remote bindings</a> for local development today with:</strong></p>
<ul>
<li><a href="/workers/wrangler/">Wrangler v4.37.0</a></li>
<li>The <a href="/workers/vite-plugin/">Cloudflare Vite Plugin</a></li>
<li>The <a href="/workers/testing/vitest-integration/">Cloudflare Vitest Plugin</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-15">Sep 15, 2025</time><div>
<h2 id="post-2025-09-15-waf-release"><a href="/changelog/post/2025-09-15-waf-release/">WAF Release - 2025-09-15</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week's focus highlights newly disclosed vulnerabilities in DevOps tooling, data visualization platforms, and enterprise CMS solutions. These issues include sensitive information disclosure and remote code execution, putting organizations at risk of credential leakage, unauthorized access, and full system compromise.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Argo CD (CVE-2025-55190): Exposure of sensitive information could allow attackers to access credential data stored in configurations, potentially leading to compromise of Kubernetes workloads and secrets.</p>
</li>
<li>
<p>DataEase (CVE-2025-57773): Insufficient input validation enables JNDI injection and insecure deserialization, resulting in remote code execution (RCE). Successful exploitation grants attackers control over the application server.</p>
</li>
<li>
<p>Sitecore (CVE-2025-53694): A sensitive information disclosure flaw allows unauthorized access to confidential information stored in Sitecore deployments, raising the risk of data breaches and privilege escalation.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities expose organizations to serious risks, including credential theft, unauthorized access, and full system compromise. Argo CD's flaw may expose Kubernetes secrets, DataEase exploitation could give attackers remote execution capabilities, and Sitecore's disclosure issue increases the likelihood of sensitive data leakage and business impact.</p>
<p>Administrators are strongly advised to apply vendor patches immediately, rotate exposed credentials, and review access controls to mitigate these risks.</p>
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
        <code class="nb-rule-id" title="199cce9ab21e40bcb535f01b2ee2085f">2ee2085f</code>
</td>
<td>100646</td>
<td>Argo CD - Information Disclosure - CVE:CVE-2025-55190s</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e513bb21b6a44f9cbfcd2462f5e20788">f5e20788</code>
</td>
<td>100874</td>
<td>DataEase - JNDI injection - CVE:CVE-2025-57773</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="be097f5a71a04f27aa87b60d005a12fd">005a12fd</code>
</td>
<td>100880</td>
<td>Sitecore - Information Disclosure - CVE:CVE-2025-53694</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-12">Sep 12, 2025</time><div>
<h2 id="post-2025-09-11-regional-email-processing-gia"><a href="/changelog/post/2025-09-11-regional-email-processing-gia/">Regional Email Processing for Germany, India, or Australia</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>We’re excited to announce that Email security customers can now choose their preferred mail processing location directly from the UI when onboarding a domain. This feature is available for the following onboarding methods: <strong>MX</strong>, <strong>BCC</strong>, and <strong>Journaling</strong>.</p>
<h4 id="2025-09-11-regional-email-processing-gia-what-s-new">What’s new</h4>
<p>Customers can now select where their email is processed. The following regions are supported:</p>
<ul>
<li><strong>Germany</strong></li>
<li><strong>India</strong></li>
<li><strong>Australia</strong></li>
</ul>
<p>Global processing remains the default option, providing flexibility to meet both compliance requirements or operational preferences.</p>
<h4 id="2025-09-11-regional-email-processing-gia-how-to-use-it">How to use it</h4>
<p>When onboarding a domain with MX, BCC, or Journaling:</p>
<ol>
<li>Select the desired processing location (Germany, India, or Australia).</li>
<li>The UI will display updated processing addresses specific to that region.</li>
<li>For MX onboarding, if your domain is managed by Cloudflare, you can automatically update MX records directly from the UI.</li>
</ol>
<h4 id="2025-09-11-regional-email-processing-gia-availability">Availability</h4>
<p>This feature is available across these Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<h4 id="2025-09-11-regional-email-processing-gia-what-s-next">What’s next</h4>
<p>We’re expanding the list of processing locations to match our <a href="/data-localization/">Data Localization Suite (DLS)</a> footprint, giving customers the broadest set of regional options in the market without the complexity of self-hosting.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-11">Sep 11, 2025</time><div>
<h2 id="post-2025-09-11-d1-automatic-read-retries"><a href="/changelog/post/2025-09-11-d1-automatic-read-retries/">D1 automatically retries read-only queries</a></h2>
<div class="changelog-badges"><span>d1</span><span>workers</span></div><div class="changelog-body"><p>D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors. You can access the number of execution attempts in the returned <a href="/d1/worker-api/return-object/#d1result">response metadata</a> property <code>total_attempts</code>.</p>
<p>At the moment, only read-only queries are retried, that is, queries containing only the following SQLite keywords: <code>SELECT</code>, <code>EXPLAIN</code>, <code>WITH</code>. Queries containing any <a href="https://sqlite.org/lang_keywords.html">SQLite keyword</a> that leads to database writes are not retried.</p>
<p>The retry success ratio among read-only retryable errors varies from 5% all the way up to 95%, depending on the underlying error and its duration (like network errors or other internal errors).</p>
<p>The retry success ratio among all retryable errors is lower, indicating that there are write-queries that could be retried. Therefore, we recommend D1 users to continue applying <a href="/d1/best-practices/retry-queries/">retries in their own code</a> for queries that are not read-only but are idempotent according to the business logic of the application.</p>
<p><img src="/assets/upstream/images/changelog/d1/d1-auto-retry-success-ratio.png" alt="D1 automatically query retries success ratio" /></p>
<p>D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing changes slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.</p>
<p>The read-only query detection heuristics are simple for now, and there is room for improvement to capture more cases of queries that can be retried, so this is just the beginning.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-11">Sep 11, 2025</time><div>
<h2 id="post-2025-09-11-dns-filtering-for-private-network-onramps"><a href="/changelog/post/2025-09-11-dns-filtering-for-private-network-onramps/">DNS filtering for private network onramps</a></h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-wan</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering">Magic WAN</a> and <a href="/mesh/features/routes/#dns-filtering">WARP Connector</a> users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.</p>
<p>Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including <a href="/cloudflare-one/traffic-policies/resolver-policies/#internal-dns">Internal DNS</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">hostname-based policies</a>.</p>
<p>To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, <code>172.64.36.1</code> and <code>172.64.36.2</code>. Once you configure DNS resolution and filtering, you can use <em>Source Internal IP</em> as a traffic selector in your <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> for routing private DNS traffic to your <a href="/dns/internal-dns/">Internal DNS</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-11">Sep 11, 2025</time><div>
<h2 id="post-2025-09-11-contextual-pivots"><a href="/changelog/post/2025-09-11-contextual-pivots/">Contextual pivots</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Directly from <a href="/log-explorer/log-search/">Log Search</a> results, customers can pivot to other parts of the Cloudflare dashboard to immediately take action as a result of their investigation.</p>
<p>From the <code>http_requests</code> or <code>fw_events</code> dataset results, right click on an IP Address or JA3 Fingerprint to pivot to the Investigate portal to lookup the reputation of an IP address or JA3 fingerprint.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/investigate-ip-address.png" alt="Investigate IP address" /></p>
<p>Easily learn about error codes by linking directly to our documentation from the <strong>EdgeResponseStatus</strong> or <strong>OriginResponseStatus</strong> fields.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/view-documentation.png" alt="View documentation" /></p>
<p>From the <code>gateway_http</code> dataset, click on a <strong>policyid</strong> to link directly to the Zero Trust dashboard to review or make changes to a specific Gateway policy.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/policyid.png" alt="View policy" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-11">Sep 11, 2025</time><div>
<h2 id="post-2025-09-11-new-results-table-view"><a href="/changelog/post/2025-09-11-new-results-table-view/">New results table view</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>The results table view of <strong>Log Search</strong> has been updated with additional functionality and a more streamlined user experience. Users can now easily:</p>
<ul>
<li>Remove/add columns.</li>
<li>Resize columns.</li>
<li>Sort columns.</li>
<li>Copy values from any field.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/log-explorer/new-table.png" alt="New results table view" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-11">Sep 11, 2025</time><div>
<h2 id="post-2025-09-11-increased-version-rollback-limit"><a href="/changelog/post/2025-09-11-increased-version-rollback-limit/">Worker version rollback limit increased from 10 to 100</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The number of recent versions available for a Worker rollback has been increased from 10 to 100.</p>
<p>This allows you to:</p>
<ul>
<li>
<p>Promote any of the 100 most recent versions to be the active deployment.</p>
</li>
<li>
<p>Split traffic using <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployments</a> between your latest code and any of the 100 most recent versions.</p>
</li>
</ul>
<p>You can do this through the Cloudflare dashboard or with <a href="/workers/wrangler/commands/general/#rollback">Wrangler's rollback command</a></p>
<p>Learn more about <a href="/workers/versions-and-deployments/">versioned deployments</a> and <a href="/workers/versions-and-deployments/rollbacks/">rollbacks</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-10">Sep 10, 2025</time><div>
<h2 id="post-2025-09-03-agents-sdk-beta-v5"><a href="/changelog/post/2025-09-03-agents-sdk-beta-v5/">Agents SDK v0.1.0 and workers-ai-provider v2.0.0 with AI SDK v5 support</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v5</a> and introducing automatic message migration that handles all legacy formats transparently.</p>
<p>This release includes improved streaming and tool support, tool confirmation detection (for &quot;human in the loop&quot; systems), enhanced React hooks with automatic tool resolution, improved error handling for streaming responses, and seamless migration utilities that work behind the scenes.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable message handling across SDK versions — all while maintaining backward compatibility.</p>
<p>Additionally, we've updated workers-ai-provider v2.0.0, the official provider for Cloudflare Workers AI models, to be compatible with AI SDK v5.</p>
<h4 id="2025-09-03-agents-sdk-beta-v5-useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v5 capabilities.</p>
<pre><code class="language-ts">// Basic chat setup&#10;const { messages, sendMessage, addToolResult } = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	tools,&#10;});&#10;&#10;// With custom tool confirmation&#10;const chat = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	toolsRequiringConfirmation: [&quot;dangerousOperation&quot;],&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-automatic-tool-resolution">Automatic Tool Resolution</h4>
<p>Tools are automatically categorized based on their configuration:</p>
<pre><code class="language-ts">const tools = {&#10;	// Auto-executes (has execute function)&#10;	getLocalTime: {&#10;		description: &quot;Get current local time&quot;,&#10;		inputSchema: z.object({}),&#10;		execute: async () =&gt; new Date().toLocaleString(),&#10;	},&#10;&#10;	// Requires confirmation (no execute function)&#10;	deleteFile: {&#10;		description: &quot;Delete a file from the system&quot;,&#10;		inputSchema: z.object({&#10;			filename: z.string(),&#10;		}),&#10;	},&#10;&#10;	// Server-executed (no client confirmation)&#10;	analyzeData: {&#10;		description: &quot;Analyze dataset on server&quot;,&#10;		inputSchema: z.object({ data: z.array(z.number()) }),&#10;		serverExecuted: true,&#10;	},&#10;} satisfies Record&lt;string, AITool&gt;;&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-message-handling">Message Handling</h4>
<p>Send messages using the new v5 format with parts array:</p>
<pre><code class="language-ts">// Text message&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [{ type: &quot;text&quot;, text: &quot;Hello, assistant!&quot; }],&#10;});&#10;&#10;// Multi-part message with file&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{ type: &quot;image&quot;, image: imageData },&#10;	],&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>Simplified logic for detecting pending tool confirmations:</p>
<pre><code class="language-ts">const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolResult({&#10;		toolCallId: part.toolCallId,&#10;		tool: getToolName(part),&#10;		output: &quot;User approved the action&quot;,&#10;	});&#10;}&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-automatic-message-migration">Automatic Message Migration</h4>
<p>Seamlessly handle legacy message formats without code changes.</p>
<pre><code class="language-ts">// All these formats are automatically converted:&#10;&#10;// Legacy v4 string content&#10;const legacyMessage = {&#10;	role: &quot;user&quot;,&#10;	content: &quot;Hello world&quot;,&#10;};&#10;&#10;// Legacy v4 with tool calls&#10;const legacyWithTools = {&#10;	role: &quot;assistant&quot;,&#10;	content: &quot;&quot;,&#10;	toolInvocations: [&#10;		{&#10;			toolCallId: &quot;123&quot;,&#10;			toolName: &quot;weather&quot;,&#10;			args: { city: &quot;SF&quot; },&#10;			state: &quot;result&quot;,&#10;			result: &quot;Sunny, 72°F&quot;,&#10;		},&#10;	],&#10;};&#10;&#10;// Automatically becomes v5 format:&#10;// {&#10;//   role: &quot;assistant&quot;,&#10;//   parts: [{&#10;//     type: &quot;tool-call&quot;,&#10;//     toolCallId: &quot;123&quot;,&#10;//     toolName: &quot;weather&quot;,&#10;//     args: { city: &quot;SF&quot; },&#10;//     state: &quot;result&quot;,&#10;//     result: &quot;Sunny, 72°F&quot;&#10;//   }]&#10;// }&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-tool-definition-updates">Tool Definition Updates</h4>
<p>Migrate tool definitions to use the new <code>inputSchema</code> property.</p>
<pre><code class="language-ts">// Before (AI SDK v4)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		parameters: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;&#10;// After (AI SDK v5)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		inputSchema: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-cloudflare-workers-ai-integration">Cloudflare Workers AI Integration</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v2.0.0.</p>
<h4 id="2025-09-03-agents-sdk-beta-v5-model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v2.0.0 - same API, enhanced v5 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v5 file handling with automatic conversion:</p>
<pre><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages,&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-import-updates">Import Updates</h4>
<p>Update your imports to use the new v5 types:</p>
<pre><code class="language-ts">// Before (AI SDK v4)&#10;import type { Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;ai/react&quot;;&#10;&#10;// After (AI SDK v5)&#10;import type { UIMessage } from &quot;ai&quot;;&#10;// or alias for compatibility&#10;import type { UIMessage as Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;@ai-sdk/react&quot;;&#10;</code></pre>
<h4 id="2025-09-03-agents-sdk-beta-v5-resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v5.md">Migration Guide</a> - Comprehensive migration documentation</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-5-0">AI SDK v5 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://github.com/cloudflare/agents-starter/pull/105">An Example PR showing the migration from AI SDK v4 to v5</a></li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="2025-09-03-agents-sdk-beta-v5-feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade process?</li>
<li><strong>Tool confirmation workflow</strong> - Does the new automatic detection work as expected?</li>
<li><strong>Message format handling</strong> - Any edge cases with legacy message conversion?</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-09-10">Sep 10, 2025</time><div>
<h2 id="post-2025-09-10-built-with-cloudflare-button"><a href="/changelog/post/2025-09-10-built-with-cloudflare-button/">Built with Cloudflare button</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've updated our &quot;Built with Cloudflare&quot; button to make it easier to share that you're building on Cloudflare with the world. Embed it in your project's README, blog post, or wherever you want to let people know.</p>
<p><img src="https://workers.cloudflare.com/built-with-cloudflare.svg" alt="Built with Cloudflare" /></p>
<p>Check out the <a href="/workers/platform/built-with-cloudflare">documentation</a> for usage information.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/34/">Previous</a><span>Page 35 of 50</span><a class="pagination-next" rel="next" href="/changelog/36/">Next</a></nav>
</div>
