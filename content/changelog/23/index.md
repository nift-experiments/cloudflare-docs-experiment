<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-03-16">Mar 16, 2026</time><div>
<h2 id="post-2026-03-15-infinite-paging-investigations"><a href="/changelog/post/2026-03-15-infinite-paging-investigations/">Unlimited result paging in Investigations</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Investigations now support unlimited result paging in both the dashboard and the API, removing the previous 1,000-record cap. Security teams can page through complete result sets when searching across large mail volumes, giving SOC analysts and automated workflows deeper visibility for forensics and threat hunting.</p>
<p>In the dashboard, infinite paging is now supported in the Investigations view. The 1,000-record ceiling has been removed, so you can navigate through the full result set directly in the UI. The <a href="/api/resources/email_security/subresources/investigate/methods/list">Investigations API</a> now returns up to 10,000 records per page (up from 1,000), with no cap on total result volume across pages.</p>
<p>For high-volume use cases, we recommend:</p>
<ul>
<li><strong><a href="/cloudflare-one/insights/logs/logpush/email-security-logs/">Logpush</a> to a SIEM</strong> for full-fidelity datasets and long-term retention.</li>
<li><strong>SOAR playbooks</strong> against the async bulk action API for large-scale remediation. Bulk actions initiated from the dashboard remain capped at 1,000 messages per action.</li>
<li><strong>The Investigations API</strong> for report exports larger than 1,000 results, which is the dashboard download cap.</li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-15">Mar 15, 2026</time><div>
<h2 id="post-2026-03-15-durable-object-id-name"><a href="/changelog/post/2026-03-15-durable-object-id-name/">Access Durable Object name via `ctx.id.name`</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>When your Worker accesses a Durable Object via <code>idFromName()</code> or <code>getByName()</code>, the same name is now available on <code>ctx.id.name</code> inside the object — no need to pass it through method arguments or persist it in storage. This brings the runtime behavior in line with the <a href="/workers/languages/typescript/">Workers runtime types</a>.</p>
<p>This is especially useful for <a href="/durable-objects/api/alarms/">alarms</a>, where there is no calling client to pass the name as an argument. When an alarm handler runs, <code>ctx.id.name</code> will hold the same name the object was originally accessed with.</p>
<pre><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class ChatRoom extends DurableObject {&#10;  async getRoomName() {&#10;    // ctx.id.name returns the name passed to getByName() or idFromName()&#10;    return this.ctx.id.name;&#10;  }&#10;}&#10;&#10;// Worker&#10;export default {&#10;  async fetch(request, env) {&#10;    const stub = env.CHAT_ROOM.getByName(&quot;general&quot;);&#10;    const roomName = await stub.getRoomName();&#10;    return new Response(`Welcome to ${roomName}!`);&#10;  },&#10;};&#10;</code></pre>
<p><code>ctx.id.name</code> is <code>undefined</code> in the following cases:</p>
<ul>
<li>For Durable Objects created with <code>newUniqueId()</code>.</li>
<li>When accessed via <code>idFromString()</code>, even if the ID was originally created from a name.</li>
<li>For <a href="/durable-objects/api/id/#name">names longer than 1,024 bytes</a>.</li>
</ul>
<p>This works the same way in local development with <code>wrangler dev</code> as it does in production. Run <code>npm update wrangler</code> to ensure you are on a version with this support.</p>
<p>For more information, refer to the <a href="/durable-objects/api/id/#name">Durable Object ID documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-12">Mar 12, 2026</time><div>
<h2 id="post-2026-03-12-ssh-support"><a href="/changelog/post/2026-03-12-ssh-support/">SSH into running Container instances</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now SSH into running Container instances using Wrangler. This is useful for debugging, inspecting running processes, or executing one-off commands inside a Container.</p>
<p>To connect, enable <code>wrangler_ssh</code> in your Container configuration and add your <code>ssh-ed25519</code> public key to <code>authorized_keys</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17709.md")</div>
<p>Then connect with:</p>
<pre><code class="language-sh">wrangler containers ssh &lt;INSTANCE_ID&gt;&#10;</code></pre>
<p>You can also run a single command without opening an interactive shell:</p>
<pre><code class="language-sh">wrangler containers ssh &lt;INSTANCE_ID&gt; -- ls -al&#10;</code></pre>
<p>Use <code>wrangler containers instances &lt;APPLICATION&gt;</code> to find the instance ID for a running Container.</p>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-12">Mar 12, 2026</time><div>
<h2 id="post-2026-03-12-wrangler-containers-instances"><a href="/changelog/post/2026-03-12-wrangler-containers-instances/">List Container instances with `wrangler containers instances`</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>A new <a href="/workers/wrangler/commands/containers/#containers-instances"><code>wrangler containers instances</code></a> command lists all instances for a given Container application. This mirrors the instances view in the Cloudflare dashboard.</p>
<p>The command displays each instance's ID, name, state, location, version, and creation time:</p>
<pre><code class="language-sh">wrangler containers instances &lt;APPLICATION_ID&gt;&#10;</code></pre>
<p>Use the <code>--json</code> flag for machine-readable output, which is also the default format in non-interactive environments such as CI pipelines.</p>
<p>For the full list of options, refer to the <a href="/workers/wrangler/commands/containers/#containers-instances"><code>containers instances</code> command reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-12">Mar 12, 2026</time><div>
<h2 id="post-2026-03-12-retry-after-header-for-1xxx-errors"><a href="/changelog/post/2026-03-12-retry-after-header-for-1xxx-errors/">Retry-After HTTP header for retryable 1xxx errors</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare-generated 1xxx error responses now include a standard <code>Retry-After</code> HTTP header when the error is retryable. Agents and HTTP clients can read the recommended wait time from response headers alone — no body parsing required.</p>
<h4 id="2026-03-12-retry-after-header-for-1xxx-errors-changes">Changes</h4>
<p>Seven retryable error codes now emit <code>Retry-After</code>:</p>
<table>
<thead>
<tr>
<th>Error code</th>
<th>Retry-After (seconds)</th>
<th>Error name</th>
</tr>
</thead>
<tbody>
<tr>
<td>1004</td>
<td>120</td>
<td>DNS resolution error</td>
</tr>
<tr>
<td>1005</td>
<td>120</td>
<td>Banned zone</td>
</tr>
<tr>
<td>1015</td>
<td>30</td>
<td>Rate limited</td>
</tr>
<tr>
<td>1033</td>
<td>120</td>
<td>Argo Tunnel error</td>
</tr>
<tr>
<td>1038</td>
<td>60</td>
<td>HTTP headers limit exceeded</td>
</tr>
<tr>
<td>1200</td>
<td>60</td>
<td>Cache connection limit</td>
</tr>
<tr>
<td>1205</td>
<td>5</td>
<td>Too many redirects</td>
</tr>
</tbody>
</table>
<p>The header value matches the existing <code>retry_after</code> body field in JSON and Markdown responses.</p>
<p>If a WAF rate limiting rule has already set a dynamic <code>Retry-After</code> value on the response, that value takes precedence.</p>
<h4 id="2026-03-12-retry-after-header-for-1xxx-errors-availability">Availability</h4>
<p>Available for all zones on all plans.</p>
<h4 id="2026-03-12-retry-after-header-for-1xxx-errors-verify">Verify</h4>
<p>Check for the header on any retryable error:</p>
<pre><code class="language-bash">curl -s --compressed -D - -o /dev/null -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | grep -i retry-after&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9110#section-10.2.3">RFC 9110 section 10.2.3 - Retry-After</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-12">Mar 12, 2026</time><div>
<h2 id="post-2026-03-12-emergency-waf-release"><a href="/changelog/post/2026-03-12-emergency-waf-release/">WAF Release - 2026-03-12 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces new detections for vulnerabilities in Ivanti Endpoint Manager Mobile (CVE-2026-1281 and CVE-2026-1340), alongside a new generic detection rule designed to identify and block Cross-Site Scripting (XSS) injection attempts within the <code>Content-Security-Policy</code> (CSP) HTTP request header.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-1281 &amp; CVE-2026-1340: Ivanti Endpoint Manager Mobile processes HTTP requests through Apache RevwriteMap directives that pass user-controlled input to Bash scripts (<code>/mi/bin/map-appstore-url</code> and <code>/mi/bin/map-aft-store-url</code>). Bash scripts do not sanitize user input and are vulnerable to shell arithmetic expansion thereby allowing attackers to achieve unauthenticated remote code execution.</li>
<li>Generic XSS in CSP Header: This rule identifies malicious payloads embedded within the request's <code>Content-Security-Policy</code> header. It specifically targets scenarios where web frameworks or applications trust and extract values directly from the CSP header in the incoming request without sufficient validation. Attackers can provide crafted header values to inject scripts or malicious directives that are subsequently processed by the server.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of Ivanti EPMM vulnerability allows unauthenticated remote code execution and generic XSS in CSP header allows attackers to inject malicious scripts during page rendering. In environments using server-side caching, this poisoned XSS content can subsequently be cached and automatically served to all visitors.</p>
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
				<code class="nb-rule-id" title="5ae86a9bda0c41dbb905132f796ea2f6">796ea2f6</code>
</td>
<td>N/A</td>
<td>Ivanti EPMM - Code Injection - CVE:CVE-2026-1281 CVE:CVE-2026-1340</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="35978af68e374a059e397bf5ee964a8c">ee964a8c</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:Content-Security-Policy</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-11">Mar 11, 2026</time><div>
<h2 id="post-2026-03-11-json-rfc9457-responses-for-1xxx-errors"><a href="/changelog/post/2026-03-11-json-rfc9457-responses-for-1xxx-errors/">JSON responses and RFC 9457 support for Cloudflare 1xxx errors</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare-generated 1xxx errors now return structured JSON when clients send <code>Accept: application/json</code> or <code>Accept: application/problem+json</code>. JSON responses follow <a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 (Problem Details for HTTP APIs)</a>, so any HTTP client that understands Problem Details can parse the base members without Cloudflare-specific code.</p>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-breaking-change">Breaking change</h4>
<p>The Markdown frontmatter field <code>http_status</code> has been renamed to <code>status</code>. Agents consuming Markdown frontmatter should update parsers accordingly.</p>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-changes">Changes</h4>
<p><strong>JSON format.</strong> Clients sending <code>Accept: application/json</code> or <code>Accept: application/problem+json</code> now receive a structured JSON object with the same operational fields as Markdown frontmatter, plus RFC 9457 standard members.</p>
<p><strong>RFC 9457 standard members (JSON only):</strong></p>
<ul>
<li><code>type</code> — URI pointing to Cloudflare documentation for the specific error code</li>
<li><code>status</code> — HTTP status code (matching the response status)</li>
<li><code>title</code> — short, human-readable summary</li>
<li><code>detail</code> — human-readable explanation specific to this occurrence</li>
<li><code>instance</code> — Ray ID identifying this specific error occurrence</li>
</ul>
<p><strong>Field renames:</strong></p>
<ul>
<li><code>http_status</code> -&gt; <code>status</code> (JSON and Markdown)</li>
<li><code>what_happened</code> -&gt; <code>detail</code> (JSON only — Markdown prose sections are unchanged)</li>
</ul>
<p><strong>Content-Type mirroring.</strong> Clients sending <code>Accept: application/problem+json</code> receive <code>Content-Type: application/problem+json; charset=utf-8</code> back; <code>Accept: application/json</code> receives <code>application/json; charset=utf-8</code>. Same body in both cases.</p>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-negotiation-behavior">Negotiation behavior</h4>
<table>
<thead>
<tr>
<th>Request header sent</th>
<th>Response format</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Accept: application/json</code></td>
<td>JSON (<code>application/json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/problem+json</code></td>
<td>JSON (<code>application/problem+json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/json, text/markdown;q=0.9</code></td>
<td>JSON</td>
</tr>
<tr>
<td><code>Accept: text/markdown</code></td>
<td>Markdown</td>
</tr>
<tr>
<td><code>Accept: text/markdown, application/json</code></td>
<td>Markdown (equal <code>q</code>, first-listed wins)</td>
</tr>
<tr>
<td><code>Accept: */*</code></td>
<td>HTML (default)</td>
</tr>
</tbody>
</table>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-availability">Availability</h4>
<p>Available now for Cloudflare-generated 1xxx errors.</p>
<h4 id="2026-03-11-json-rfc9457-responses-for-1xxx-errors-get-started">Get started</h4>
<pre><code class="language-bash">curl -s --compressed -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | jq .&#10;</code></pre>
<pre><code class="language-bash">curl -s --compressed -H &quot;Accept: application/problem+json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/1015&quot; | jq .&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 — Problem Details for HTTP APIs</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-11">Mar 11, 2026</time><div>
<h2 id="post-2026-03-11-ingest-field-selection"><a href="/changelog/post/2026-03-11-ingest-field-selection/">Ingest field selection for Log Explorer</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Cloudflare Log Explorer now allows you to customize exactly which data fields are ingested and stored when enabling or managing log datasets.</p>
<p>Previously, ingesting logs often meant taking an &quot;all or nothing&quot; approach to data fields. With <strong>Ingest Field Selection</strong>, you can now choose from a list of available and recommended fields for each dataset. This allows you to reduce noise, focus on the metrics that matter most to your security and performance analysis, and manage your data footprint more effectively.</p>
<h4 id="2026-03-11-ingest-field-selection-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Granular control:</strong> Select only the specific fields you need when enabling a new dataset.</li>
<li><strong>Dynamic updates:</strong> Update fields for existing, already enabled logstreams at any time.</li>
<li><strong>Historical consistency:</strong> Even if you disable a field later, you can still query and receive results for that field for the period it was captured.</li>
<li><strong>Data integrity:</strong> Core fields, such as <code>Timestamp</code>, are automatically retained to ensure your logs remain searchable and chronologically accurate.</li>
</ul>
<h4 id="2026-03-11-ingest-field-selection-example-configuration">Example configuration</h4>
<p>When configuring a dataset via the dashboard or API, you can define a specific set of fields. The <code>Timestamp</code> field remains mandatory to ensure data indexability.</p>
<pre><code class="language-json">{&#10;  &quot;dataset&quot;: &quot;firewall_events&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;fields&quot;: [&#10;    &quot;Timestamp&quot;,&#10;    &quot;ClientRequestHost&quot;,&#10;    &quot;ClientIP&quot;,&#10;    &quot;Action&quot;,&#10;    &quot;EdgeResponseStatus&quot;,&#10;    &quot;OriginResponseStatus&quot;&#10;  ]&#10;}&#10;</code></pre>
<p>For more information, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-11">Mar 11, 2026</time><div>
<h2 id="post-2026-03-11-nemotron-3-super-workers-ai"><a href="/changelog/post/2026-03-11-nemotron-3-super-workers-ai/">NVIDIA Nemotron 3 Super now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We're excited to partner with NVIDIA to bring <a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a> to Workers AI. NVIDIA Nemotron 3 Super is a Mixture-of-Experts (MoE) model with a hybrid Mamba-transformer architecture, 120B total parameters, and 12B active parameters per forward pass.</p>
<p>The model is optimized for running many collaborating agents per application. It delivers high accuracy for reasoning, tool calling, and instruction following across complex multi-step tasks.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Hybrid Mamba-transformer architecture</strong> delivers over 50% higher token generation throughput compared to leading open models, reducing latency for real-world applications</li>
<li><strong>Tool calling</strong> support for building AI agents that invoke tools across multiple conversation turns</li>
<li><strong>Multi-Token Prediction (MTP)</strong> accelerates long-form text generation by predicting several future tokens simultaneously in a single forward pass</li>
<li><strong>32,000 token context window</strong> for retaining conversation history and plan states across multi-step agent workflows</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-03-11-nemotron-3-super-workers-ai-prompt-caching">Prompt caching</h4>
@markup("md", "content/.markup/bodies/17818.md")</aside>
<p>Use Nemotron 3 Super through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/nemotron-3-120b-a12b/">Nemotron 3 Super model page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-11">Mar 11, 2026</time><div>
<h2 id="post-2026-03-10-warp-macos-beta"><a href="/changelog/post/2026-03-10-warp-macos-beta/">WARP client for macOS (version 2026.3.566.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the <a href="https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362">Cloudflare Community forum</a> and let us know.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.</li>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.</li>
<li>Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>The client may become stuck in a <code>Connecting</code> state. To resolve this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface. Alternatively, change the client's operation mode.</li>
<li>The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.</li>
<li>Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-11">Mar 11, 2026</time><div>
<h2 id="post-2026-03-10-warp-windows-beta"><a href="/changelog/post/2026-03-10-warp-windows-beta/">WARP client for Windows (version 2026.3.566.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and introduces a brand new visual style for the client interface. The new Cloudflare One Client interface changes connectivity management from a toggle to a button and brings useful connectivity settings to the home screen. The redesign also introduces a collapsible navigation bar. When expanded, more client information can be accessed including connectivity, settings, and device profile information. If you have any feedback or questions, visit the <a href="https://community.cloudflare.com/t/introducing-the-new-cloudflare-one-client-interface/901362">Cloudflare Community forum</a> and let us know.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm to Cubic for improved reliability across platforms.</li>
<li>Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.</li>
<li>Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.</li>
<li>Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.</li>
<li>Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.</li>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed emergency disconnect state from a previous organization incorrectly persisting after switching organizations.</li>
<li>Fixed initiating managed network detection checks when no network is available, which caused device profile flapping.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>The client may unexpectedly terminate during captive portal login. To work around this issue, use a web browser to authenticate with the captive portal and then re-launch the client.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>The client may become stuck in a <code>Connecting</code> state. To resolve this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface. Alternatively, change the client's operation mode.</li>
<li>The client may display an empty white screen upon the device waking from sleep. To resolve this issue, exit and then open the client to re-launch it.</li>
<li>Canceling login during a single MDM configuration setup results in an empty page with no way to resume authentication. To work around this issue, exit and relaunch the client.</li>
<li>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 version KB5062553</a> or higher for resolution.</li>
<li>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.</li>
<li>DNS resolution may be broken when the following conditions are all true:
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.
To work around this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface.</li>
</ul>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-10">Mar 10, 2026</time><div>
<h2 id="post-2026-03-10-audit-logs-v2-ga"><a href="/changelog/post/2026-03-10-audit-logs-v2-ga/">Audit logs (version 2) - General Availability</a></h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>Audit Logs v2 is now generally available to all Cloudflare customers.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/auditlogsv2.gif" alt="Audit Logs v2 GA" /></p>
<p>Audit Logs v2 provides a unified and standardized system for tracking and recording all user and system actions across Cloudflare products. Built on Cloudflare's API Shield / OpenAPI gateway, logs are generated automatically without requiring manual instrumentation from individual product teams, ensuring consistency across ~95% of Cloudflare products.</p>
<p><strong>What's available at GA:</strong></p>
<ul>
<li><strong>Standardized logging</strong> — Audit logs follow a consistent format across all Cloudflare products, making it easier to search, filter, and investigate activity.</li>
<li><strong>Expanded product coverage</strong> — ~95% of Cloudflare products covered, up from ~75% in v1.</li>
<li><strong>Granular filtering</strong> — Filter by actor, action type, action result, resource, raw HTTP method, zone, and more. Over 20 filter parameters available via the API.</li>
<li><strong>Enhanced context</strong> — Each log entry includes authentication method, interface (API or dashboard), Cloudflare Ray ID, and actor token details.</li>
<li><strong>18-month retention</strong> — Logs are retained for 18 months. Full history is accessible via the API or Logpush.</li>
</ul>
<p><strong>Access:</strong></p>
<ul>
<li><strong>Dashboard</strong>: Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>. Audit Logs v2 is shown by default.</li>
<li><strong>API</strong>: <code>GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit</code></li>
<li><strong>Logpush</strong>: Available via the <code>audit_logs_v2</code> account-scoped dataset.</li>
</ul>
<p><strong>Important notes:</strong></p>
<ul>
<li>Approximately 30 days of logs from the Beta period (back to ~February 8, 2026) are available at GA. These Beta logs will expire on ~April 9, 2026. Logs generated after GA will be retained for the full 18 months. Older logs remain available in Audit Logs v1.</li>
<li>The UI query window is limited to 90 days for performance reasons. Use the API or Logpush for access to the full 18-month history.</li>
<li><code>GET</code> requests (view actions) and <code>4xx</code> error responses are not logged at GA. <code>GET</code> logging will be selectively re-enabled for sensitive read operations in a future release.</li>
<li>Audit Logs v1 continues to run in parallel. A deprecation timeline will be communicated separately.</li>
<li>Before and after values — the ability to see what a value changed from and to — is a highly requested feature and is on our roadmap for a post-GA release. In the meantime, we recommend using Audit Logs v1 for before and after values. Audit Logs v1 will continue to run in parallel until this feature is available in v2.</li>
</ul>
<p>For more details, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2 documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-10">Mar 10, 2026</time><div>
<h2 id="post-2026-03-10-br-crawl-endpoint"><a href="/changelog/post/2026-03-10-br-crawl-endpoint/">Crawl entire websites with a single API call using Browser Rendering</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><em>Edit: this post has been edited to clarify crawling behavior with respect to site guidance.</em></p>
<p>You can now crawl an entire website with a single API call using <a href="/browser-run/">Browser Rendering</a>'s new <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a>, available in open beta. Submit a starting URL, and pages are automatically discovered, rendered in a headless browser, and returned in multiple formats, including HTML, Markdown, and structured JSON. The endpoint is a <a href="/bots/concepts/bot/verified-bots/">verified bot (intermediary agent)</a> that respects robots.txt and <a href="https://www.cloudflare.com/ai-crawl-control/">AI Crawl Control</a> by default, making it easy for developers to comply with website rules, and making it less likely for crawlers to ignore web-owner guidance. This is great for training models, building RAG pipelines, and researching or monitoring content across a site.</p>
<p>Crawl jobs run asynchronously. You submit a URL, receive a job ID, and check back for results as pages are processed.</p>
<pre><code class="language-sh">&#35; Initiate a crawl&#10;curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://blog.cloudflare.com/&quot;&#10;  }&#x27;&#10;&#10;&#35; Check results&#10;curl -X GET &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27;&#10;</code></pre>
<p>Key features:</p>
<ul>
<li><strong>Multiple output formats</strong> - Return crawled content as HTML, Markdown, and structured JSON (powered by <a href="/workers-ai/">Workers AI</a>)</li>
<li><strong>Crawl scope controls</strong> - Configure crawl depth, page limits, and wildcard patterns to include or exclude specific URL paths</li>
<li><strong>Automatic page discovery</strong> - Discovers URLs from sitemaps, page links, or both</li>
<li><strong>Incremental crawling</strong> - Use <code>modifiedSince</code> and <code>maxAge</code> to skip pages that haven't changed or were recently fetched, saving time and cost on repeated crawls</li>
<li><strong>Static mode</strong> - Set <code>render: false</code> to fetch static HTML without spinning up a browser, for faster crawling of static sites</li>
<li><strong>Well-behaved bot</strong> - Honors <code>robots.txt</code> directives, including <code>crawl-delay</code></li>
</ul>
<p>Available on both the Workers Free and Paid plans.</p>
<p><strong>Note</strong>: the /crawl endpoint cannot bypass Cloudflare bot detection or captchas, and self-identifies as a bot.</p>
<p>To get started, refer to the <a href="/browser-run/quick-actions/crawl-endpoint/">crawl endpoint documentation</a>.
If you are setting up your own site to be crawled, review the <a href="/browser-run/reference/robots-txt/">robots.txt and sitemaps best practices</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-09">Mar 9, 2026</time><div>
<h2 id="post-2026-03-09-vulnerability-scanner"><a href="/changelog/post/2026-03-09-vulnerability-scanner/">New Vulnerability Scanner for API Shield</a></h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>Introducing Cloudflare's Web and API Vulnerability Scanner (Open Beta)</p>
<p>Cloudflare is launching the <a href="https://blog.cloudflare.com/vulnerability-scanner">Open Beta of the <strong>Web and API Vulnerability Scanner</strong></a> for all <a href="/api-shield/">API Shield</a> customers. This new, stateful Dynamic Application Security Testing (DAST) platform helps teams proactively find logic flaws in their APIs.</p>
<p>The initial release focuses on detecting Broken Object Level Authorization (BOLA) vulnerabilities by building API call graphs to simulate attacker and owner contexts, then testing these contexts by sending real HTTP requests to your APIs.</p>
<p>The scanner is now available via the Cloudflare API. To scan, set up your target environment, owner and attacker credentials, and upload your OpenAPI file with response schemas. The scanner will be available in the Cloudflare dashboard in a future release.</p>
<p><strong>Access</strong>: This feature is only available to API Shield subscribers via the Cloudflare API. We hope you will use the API for programmatic integration into your CI/CD pipelines and security dashboards.</p>
<p><strong>Documentation</strong>: Refer to the <a href="/api-shield/security/vulnerability-scanner/">developer documentation</a> to start scanning your endpoints today.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-09">Mar 9, 2026</time><div>
<h2 id="post-2026-03-09-log-fields-updated"><a href="/changelog/post/2026-03-09-log-fields-updated/">New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has added new fields across multiple <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-03-09-log-fields-updated-new-dataset">New dataset</h4>
<ul>
<li><strong>MCP Portal Logs</strong>: A new dataset with fields including <code>ClientCountry</code>, <code>ClientIP</code>, <code>ColoCode</code>, <code>Datetime</code>, <code>Error</code>, <code>Method</code>, <code>PortalAUD</code>, <code>PortalID</code>, <code>PromptGetName</code>, <code>ResourceReadURI</code>, <code>ServerAUD</code>, <code>ServerID</code>, <code>ServerResponseDurationMs</code>, <code>ServerURL</code>, <code>SessionID</code>, <code>Success</code>, <code>ToolCallName</code>, <code>UserEmail</code>, and <code>UserID</code>.</li>
</ul>
<h4 id="2026-03-09-log-fields-updated-new-fields-in-existing-datasets">New fields in existing datasets</h4>
<ul>
<li><strong>DEX Application Tests</strong>: <code>HTTPRedirectEndMs</code>, <code>HTTPRedirectStartMs</code>, <code>HTTPResponseBody</code>, and <code>HTTPResponseHeaders</code>.</li>
<li><strong>DEX Device State Events</strong>: <code>ExperimentalExtra</code>.</li>
<li><strong>Firewall Events</strong>: <code>FraudUserID</code>.</li>
<li><strong>Gateway HTTP</strong>: <code>AppControlInfo</code> and <code>ApplicationStatuses</code>.</li>
<li><strong>Gateway DNS</strong>: <code>InternalDNSDurationMs</code>.</li>
<li><strong>HTTP Requests</strong>: <code>FraudEmailRisk</code>, <code>FraudUserID</code>, and <code>PayPerCrawlStatus</code>.</li>
<li><strong>Network Analytics Logs</strong>: <code>DNSQueryName</code>, <code>DNSQueryType</code>, and <code>PFPCustomTag</code>.</li>
<li><strong>WARP Toggle Changes</strong>: <code>UserEmail</code>.</li>
<li><strong>WARP Config Changes</strong>: <code>UserEmail</code>.</li>
<li><strong>Zero Trust Network Session Logs</strong>: <code>SNI</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-06">Mar 6, 2026</time><div>
<h2 id="post-2026-03-06-step-context-available"><a href="/changelog/post/2026-03-06-step-context-available/">Workflow steps now expose retry attempt number via step context</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>Cloudflare Workflows allows you to configure specific retry logic for each step in your workflow execution. Now, you can access <strong>which</strong> retry attempt is currently executing for calls to <code>step.do()</code>:</p>
<pre><code class="language-ts">await step.do(&quot;my-step&quot;, async (ctx) =&gt; {&#10;	// ctx.attempt is 1 on first try, 2 on first retry, etc.&#10;	console.log(`Attempt ${ctx.attempt}`);&#10;});&#10;</code></pre>
<p>You can use the step context for improved logging &amp; observability, progressive backoff, or conditional logic in your workflow definition.</p>
<p>Note that the current attempt number is 1-indexed. For more information on retry behavior, refer to <a href="/workflows/build/sleeping-and-retrying/">Sleeping and Retrying</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-06">Mar 6, 2026</time><div>
<h2 id="post-2026-03-06-radar-region-filtering-traffic-volume-navigation"><a href="/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/">Region Filtering, AS Traffic Volume, and Navigation Improvements on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> ships several new features that improve the flexibility and usability of the platform, as well as visibility into what is happening on the Internet.</p>
<h4 id="2026-03-06-radar-region-filtering-traffic-volume-navigation-region-filtering">Region filtering</h4>
<p>All location-aware pages now support filtering by region, including continents, geographic subregions (<a href="https://radar.cloudflare.com/middle-east">Middle East</a>, <a href="https://radar.cloudflare.com/eastern-asia">Eastern Asia</a>, etc.), political regions (<a href="https://radar.cloudflare.com/european-union">EU</a>, <a href="https://radar.cloudflare.com/african-union">African Union</a>), and US Census regions/divisions (for example, <a href="https://radar.cloudflare.com/traffic/us-new-england">New England</a>, <a href="https://radar.cloudflare.com/traffic/us-northeast">US Northeast</a>).</p>
<p><img src="/assets/upstream/images/radar/region-filtering-middle-east.png" alt="Screenshot of region filtering on Radar - Middle east" /></p>
<h4 id="2026-03-06-radar-region-filtering-traffic-volume-navigation-traffic-volume-by-top-autonomous-systems-and-locations">Traffic volume by top autonomous systems and locations</h4>
<p>A new traffic volume view shows the top autonomous systems and countries/territories for a given location. This is useful for quickly determining which network providers in a location may be experiencing connectivity issues, or how traffic is distributed across a region.</p>
<p><img src="/assets/upstream/images/radar/traffic-volume-top-as-us.png" alt="Screenshot of traffic volume by top autonomous systems in US" /></p>
<p>The new AS and location dimensions have also been added to the <a href="https://radar.cloudflare.com/explorer">Data Explorer</a> for the HTTP, DNS, and NetFlows datasets. Combined with other available filters, this provides a powerful tool for generating unique insights.</p>
<p><img src="/assets/upstream/images/radar/data-explorer-top-as-pt.png" alt="Screenshot of AS and location dimensions in Data Explorer" /></p>
<p>Finally, breadcrumb navigation is now available on most pages, allowing easier navigation between parent and related pages.</p>
<p>Check out these features on <a href="https://radar.cloudflare.com">Cloudflare Radar</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-06">Mar 6, 2026</time><div>
<h2 id="post-2026-03-06-realtimekit-multilingual-transcription"><a href="/changelog/post/2026-03-06-realtimekit-multilingual-transcription/">Real-time transcription in RealtimeKit now supports 10 languages with regional variants</a></h2>
<div class="changelog-badges"><span>workers-ai</span><span>realtime</span></div><div class="changelog-body"><p><a href="/realtime/realtimekit/ai/transcription/">Real-time transcription</a> in RealtimeKit now supports 10 languages with regional variants, powered by <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> running on <a href="/workers-ai/">Workers AI</a>.</p>
<p>During a meeting, participant audio is routed through <a href="/ai-gateway/">AI Gateway</a> to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.</p>
<p>Set the language when <a href="/realtime/realtimekit/concepts/meeting/">creating a meeting</a> via <code>ai_config.transcription.language</code>:</p>
<pre><code class="language-json">{&#10;	&quot;ai_config&quot;: {&#10;		&quot;transcription&quot;: {&#10;			&quot;language&quot;: &quot;fr&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like <code>en-AU</code>, <code>en-GB</code>, <code>en-IN</code>, <code>en-NZ</code>, <code>es-419</code>, <code>fr-CA</code>, <code>de-CH</code>, <code>pt-BR</code>, and <code>pt-PT</code>. Use <code>multi</code> for automatic multilingual detection.</p>
<p>If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.</p>
<ul>
<li><a href="/realtime/realtimekit/ai/transcription/">Transcription docs</a></li>
<li><a href="/workers-ai/models/nova-3/">Nova-3 model page</a></li>
<li><a href="/workers-ai/">Workers AI</a></li>
<li><a href="/ai-gateway/">AI Gateway</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-06">Mar 6, 2026</time><div>
<h2 id="post-2026-03-06-brand-protection-dismiss-match"><a href="/changelog/post/2026-03-06-brand-protection-dismiss-match/">Dismiss and filter matches in Brand Protection</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>We have introduced new triage controls to help you manage your Brand Protection results more efficiently. You can now clear out the noise by dismissing matches while maintaining full visibility into your historical decisions.</p>
<h4 id="2026-03-06-brand-protection-dismiss-match-what-s-new">What's new</h4>
<ul>
<li><strong>Dismiss matches</strong>: Users can now mark specific results as dismissed if they are determined to be benign or false positives, removing them from the primary triage view.</li>
<li><strong>Show/Hide toggle</strong>: A new visibility control allows you to instantly switch between viewing only active matches and including previously dismissed ones.</li>
<li><strong>Persistent review states</strong>: Dismissed status is saved across sessions, ensuring that your workspace remains organized and focused on new or high-priority threats.</li>
</ul>
<h4 id="2026-03-06-brand-protection-dismiss-match-key-benefits-of-the-dismiss-match-functionality">Key benefits of the dismiss match functionality:</h4>
<ul>
<li>Reduce alert fatigue by hiding known-safe results, allowing your team to focus exclusively on unreviewed or high-risk infringements.</li>
<li>Auditability and recovery through the visibility toggle, ensuring that no match is ever truly &quot;lost&quot; and can be re-evaluated if a site's content changes.</li>
<li>Improved collaboration as your team members can see which matches have already been vetted and dismissed by others.</li>
</ul>
<p>Ready to clean up your match queue? Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-04">Mar 4, 2026</time><div>
<h2 id="post-2026-03-04-br-rest-api-limit-increase"><a href="/changelog/post/2026-03-04-br-rest-api-limit-increase/">Browser Rendering: 3x higher REST API request rate</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Rendering</a> REST API rate limits for Workers Paid plans have been increased from 3 requests per second (180/min) to <strong>10 requests per second (600/min)</strong>. No action is needed to benefit from the higher limit.</p>
<p><img src="/assets/upstream/images/changelog/browser-run/rest-api-limit-increase.png" alt="Browser Rendering REST API rate limit increased from 3 to 10 requests per second" /></p>
<p>The <a href="/browser-run/quick-actions/">REST API</a> lets you perform common browser tasks with a single API call, and you can now do it at a higher rate.</p>
<ul>
<li><a href="/browser-run/quick-actions/content-endpoint/">/content - Fetch HTML</a></li>
<li><a href="/browser-run/quick-actions/screenshot-endpoint/">/screenshot - Capture screenshot</a></li>
<li><a href="/browser-run/quick-actions/pdf-endpoint/">/pdf - Render PDF</a></li>
<li><a href="/browser-run/quick-actions/markdown-endpoint/">/markdown - Extract Markdown from a webpage</a></li>
<li><a href="/browser-run/quick-actions/snapshot/">/snapshot - Take a webpage snapshot</a></li>
<li><a href="/browser-run/quick-actions/scrape-endpoint/">/scrape - Scrape HTML elements</a></li>
<li><a href="/browser-run/quick-actions/json-endpoint/">/json - Capture structured data using AI</a></li>
<li><a href="/browser-run/quick-actions/links-endpoint/">/links - Retrieve links from a webpage</a></li>
</ul>
<p>If you use the <a href="/browser-run/#integration-methods">Browser Sessions</a> method, increases to concurrent browser and new browser limits are coming soon. Stay tuned.</p>
<p>For full details, refer to the <a href="/browser-run/limits/">Browser Rendering limits page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-04">Mar 4, 2026</time><div>
<h2 id="post-2026-03-04-user-risk-score-access-policies"><a href="/changelog/post/2026-03-04-user-risk-score-access-policies/">User risk score selector in Access policies</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p>You can now use <a href="/cloudflare-one/team-and-resources/users/risk-score/">user risk scores</a> in your <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. The new <strong>User Risk Score</strong> selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.</p>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies">Use risk scores in Access policies</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-04">Mar 4, 2026</time><div>
<h2 id="post-2026-03-04-gateway-authorization-proxy-open-beta"><a href="/changelog/post/2026-03-04-gateway-authorization-proxy-open-beta/">Gateway Authorization Proxy and hosted PAC files (open beta)</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Gateway Authorization Proxy</a> and <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">PAC file hosting</a> are now in open beta for all plan types.</p>
<p>Previously, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">proxy endpoints</a> relied on static source IP addresses to authorize traffic, providing no user-level identity in logs or policies. The new authorization proxy replaces IP-based authorization with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> authentication, verifying who a user is before applying Gateway filtering without installing the WARP client.</p>
<p>This is ideal for environments where you cannot deploy a device client, such as virtual desktops (VDI), mergers and acquisitions, or compliance-restricted endpoints.</p>
<h4 id="2026-03-04-gateway-authorization-proxy-open-beta-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Identity-aware proxy traffic</strong> — Users authenticate through your identity provider (Okta, Microsoft Entra ID, Google Workspace, and others) via Cloudflare Access. Logs now show exactly which user accessed which site, and you can write <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based policies</a> like &quot;only the Finance team can access this accounting tool.&quot;</li>
<li><strong>Multiple identity providers</strong> — Display one or multiple login methods simultaneously, giving flexibility for organizations managing users across different identity systems.</li>
<li><strong>Cloudflare-hosted PAC files</strong> — Create and host <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">PAC files</a> directly in Cloudflare One with pre-configured templates for Okta and Azure, hosted at <code>https://pac.cloudflare-gateway.com/&lt;account-id&gt;/&lt;slug&gt;</code> on Cloudflare's global network.</li>
<li><strong>Simplified billing</strong> — Each user occupies a seat, exactly like they do with the Cloudflare One Client. No new metrics to track.</li>
</ul>
<h4 id="2026-03-04-gateway-authorization-proxy-open-beta-get-started">Get started</h4>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong> &gt; <strong>Proxy endpoints</strong>.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Create an authorization proxy endpoint</a> and configure Access policies.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">Create a hosted PAC file</a> or write your own.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#3b-configure-browser-to-use-pac-file">Configure browsers</a> to use the PAC file URL.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Install the Cloudflare certificate</a> for HTTPS inspection.</li>
</ol>
<p>For more details, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints documentation</a> and the <a href="https://blog.cloudflare.com/gateway-authorization-proxy-identity-aware-policies/">announcement blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-04">Mar 4, 2026</time><div>
<h2 id="post-2026-03-04-new-markdown-conversion-options"><a href="/changelog/post/2026-03-04-new-markdown-conversion-options/">New conversion options for Markdown Conversion</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>You can now customize how the <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service processes different file types by passing a <code>conversionOptions</code> object.</p>
<p>Available options:</p>
<ul>
<li><strong>Images</strong>: Set the language for AI-generated image descriptions</li>
<li><strong>HTML</strong>: Use CSS selectors to extract specific content, or provide a hostname to resolve relative links</li>
<li><strong>PDF</strong>: Exclude metadata from the output</li>
</ul>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17817.md")</div>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;html&quot;: {&quot;cssSelector&quot;: &quot;article.content&quot;}}&#x27;&#10;</code></pre>
<p>For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/">Conversion Options</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-03">Mar 3, 2026</time><div>
<h2 id="post-2026-03-03-step-limits-to-25k"><a href="/changelog/post/2026-03-03-step-limits-to-25k/">Workflows step limit increased to 25,000 steps per instance</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>Each Workflow on Workers Paid now supports 10,000 steps by default, configurable up to 25,000 steps in your <code>wrangler.jsonc</code> file:</p>
<pre><code class="language-json">{&#10;	&quot;workflows&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;my-workflow&quot;,&#10;			&quot;binding&quot;: &quot;MY_WORKFLOW&quot;,&#10;			&quot;class_name&quot;: &quot;MyWorkflow&quot;,&#10;			&quot;limits&quot;: {&#10;				&quot;steps&quot;: 25000&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Previously, each instance was limited to 1,024 steps. Now, Workflows can support more complex, long-running executions without the additional complexity of recursive or child workflow calls.</p>
<p>Note that the maximum persisted state limit per Workflow instance remains <strong>100 MB</strong> for Workers Free and <strong>1 GB</strong> for Workers Paid. Refer to <a href="/workflows/reference/limits/">Workflows limits</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-03">Mar 3, 2026</time><div>
<h2 id="post-2026-03-03-sandbox-watch-file-events"><a href="/changelog/post/2026-03-03-sandbox-watch-file-events/">Real-time file watching in Sandboxes</a></h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p><a href="/sandbox/">Sandboxes</a> now support real-time filesystem watching via <code>sandbox.watch()</code>. The method returns a <a href="https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events">Server-Sent Events</a> stream backed by native inotify, so your Worker receives <code>create</code>, <code>modify</code>, <code>delete</code>, and <code>move</code> events as they happen inside the container.</p>
<h4 id="2026-03-03-sandbox-watch-file-events-sandbox-watch-path-options"><code>sandbox.watch(path, options)</code></h4>
<p>Pass a directory path and optional filters. The returned stream is a standard <code>ReadableStream</code> you can proxy directly to a browser client or consume server-side.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17650.md")</div>
<h4 id="2026-03-03-sandbox-watch-file-events-server-side-consumption-with-parsessestream">Server-side consumption with <code>parseSSEStream</code></h4>
<p>Use <code>parseSSEStream</code> to iterate over events inside a Worker without forwarding them to a client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17651.md")</div>
<p>Each event includes a <code>type</code> field (<code>create</code>, <code>modify</code>, <code>delete</code>, or <code>move</code>) and the affected <code>path</code>. Move events also include a <code>from</code> field with the original path.</p>
<h4 id="2026-03-03-sandbox-watch-file-events-options">Options</h4>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>recursive</code></td>
<td><code>boolean</code></td>
<td>Watch subdirectories. Defaults to <code>false</code>.</td>
</tr>
<tr>
<td><code>include</code></td>
<td><code>string[]</code></td>
<td>Glob patterns to filter events. Omit to receive all events.</td>
</tr>
</tbody>
</table>
<h4 id="2026-03-03-sandbox-watch-file-events-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>
<p>For full API details, refer to the <a href="/sandbox/api/file-watching/">Sandbox file watching reference</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/22/">Previous</a><span>Page 23 of 50</span><a class="pagination-next" rel="next" href="/changelog/24/">Next</a></nav>
</div>
