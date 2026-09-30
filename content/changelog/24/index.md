<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-03-03">Mar 3, 2026</time><div>
<h2 id="post-2026-03-03-radar-network-quality-test"><a href="/changelog/post/2026-03-03-radar-network-quality-test/">Network Quality Test on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes a <a href="https://radar.cloudflare.com/speedtest">Network Quality Test</a> page. The tool measures Internet connection quality and performance, showing connection details such as IP address, server location, network (ASN), and IP version. For more detailed speed test results, the page links to <a href="https://speed.cloudflare.com/">speed.cloudflare.com</a>.</p>
<p><img src="/assets/upstream/images/radar/network-quality-test.png" alt="Screenshot of the Network Quality Test page on Radar" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-02">Mar 2, 2026</time><div>
<h2 id="post-2026-03-02-agents-sdk-v0.7.0"><a href="/changelog/post/2026-03-02-agents-sdk-v0.7.0/">Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> rewrites observability from scratch with <code>diagnostics_channel</code>, adds <code>keepAlive()</code> to prevent Durable Object eviction during long-running work, and introduces <code>waitForMcpConnections</code> so MCP tools are always available when <code>onChatMessage</code> runs.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-observability-rewrite">Observability rewrite</h4>
<p>The previous observability system used <code>console.log()</code> with a custom <code>Observability.emit()</code> interface. v0.7.0 replaces it with structured events published to <a href="/workers/runtime-apis/nodejs/diagnostics-channel/">diagnostics channels</a> — silent by default, zero overhead when nobody is listening.</p>
<p>Every event has a <code>type</code>, <code>payload</code>, and <code>timestamp</code>. Events are routed to seven named channels:</p>
<table>
<thead>
<tr>
<th>Channel</th>
<th>Event types</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agents:state</code></td>
<td><code>state:update</code></td>
</tr>
<tr>
<td><code>agents:rpc</code></td>
<td><code>rpc</code>, <code>rpc:error</code></td>
</tr>
<tr>
<td><code>agents:message</code></td>
<td><code>message:request</code>, <code>message:response</code>, <code>message:clear</code>, <code>message:cancel</code>, <code>message:error</code>, <code>tool:result</code>, <code>tool:approval</code></td>
</tr>
<tr>
<td><code>agents:schedule</code></td>
<td><code>schedule:create</code>, <code>schedule:execute</code>, <code>schedule:cancel</code>, <code>schedule:retry</code>, <code>schedule:error</code>, <code>queue:retry</code>, <code>queue:error</code></td>
</tr>
<tr>
<td><code>agents:lifecycle</code></td>
<td><code>connect</code>, <code>destroy</code></td>
</tr>
<tr>
<td><code>agents:workflow</code></td>
<td><code>workflow:start</code>, <code>workflow:event</code>, <code>workflow:approved</code>, <code>workflow:rejected</code>, <code>workflow:terminated</code>, <code>workflow:paused</code>, <code>workflow:resumed</code>, <code>workflow:restarted</code></td>
</tr>
<tr>
<td><code>agents:mcp</code></td>
<td><code>mcp:client:preconnect</code>, <code>mcp:client:connect</code>, <code>mcp:client:authorize</code>, <code>mcp:client:discover</code></td>
</tr>
</tbody>
</table>
<p>Use the typed <code>subscribe()</code> helper from <code>agents/observability</code> for type-safe access:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17645.md")</div>
<p>In production, all diagnostics channel messages are automatically forwarded to <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> — no subscription code needed in the agent itself:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17646.md")</div>
<p>The custom <code>Observability</code> override interface is still supported for users who need to filter or forward events to external services.</p>
<p>For the full event reference, refer to the <a href="/agents/runtime/operations/observability/diagnostics-channels/">Diagnostics channels documentation</a>.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-keepalive-and-keepalivewhile"><code>keepAlive()</code> and <code>keepAliveWhile()</code></h4>
<p>Durable Objects are evicted after a period of inactivity (typically 70-140 seconds with no incoming requests, WebSocket messages, or alarms). During long-running operations — streaming LLM responses, waiting on external APIs, running multi-step computations — the agent can be evicted mid-flight.</p>
<p><code>keepAlive()</code> prevents this by creating a 30-second heartbeat schedule. The alarm firing resets the inactivity timer. Returns a disposer function that cancels the heartbeat when called.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17647.md")</div>
<p><code>keepAliveWhile()</code> wraps an async function with automatic cleanup — the heartbeat starts before the function runs and stops when it completes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17648.md")</div>
<p>Key details:</p>
<ul>
<li><strong>Multiple concurrent callers</strong> — Each <code>keepAlive()</code> call returns an independent disposer. Disposing one does not affect others.</li>
<li><strong>AIChatAgent built-in</strong> — <code>AIChatAgent</code> automatically calls <code>keepAlive()</code> during streaming responses. You do not need to add it yourself.</li>
<li><strong>Uses the scheduling system</strong> — The heartbeat does not conflict with your own schedules. It shows up in <code>getSchedules()</code> if you need to inspect it.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17644.md")</aside>
<p>For the full API reference and when-to-use guidance, refer to <a href="/agents/runtime/execution/schedule-tasks/#keeping-the-agent-alive">Schedule tasks — Keeping the agent alive</a>.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-waitformcpconnections"><code>waitForMcpConnections</code></h4>
<p><code>AIChatAgent</code> now waits for MCP server connections to settle before calling <code>onChatMessage</code>. This ensures <code>this.mcp.getAITools()</code> returns the full set of tools, especially after Durable Object hibernation when connections are being restored in the background.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17649.md")</div>
<table>
<thead>
<tr>
<th>Value</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>{ timeout: 10_000 }</code></td>
<td>Wait up to 10 seconds (default)</td>
</tr>
<tr>
<td><code>{ timeout: N }</code></td>
<td>Wait up to <code>N</code> milliseconds</td>
</tr>
<tr>
<td><code>true</code></td>
<td>Wait indefinitely until all connections ready</td>
</tr>
<tr>
<td><code>false</code></td>
<td>Do not wait (old behavior before 0.2.0)</td>
</tr>
</tbody>
</table>
<p>For lower-level control, call <code>this.mcp.waitForConnections()</code> directly inside <code>onChatMessage</code> instead.</p>
<h4 id="2026-03-02-agents-sdk-v0.7.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>MCP deduplication by name and URL</strong> — <code>addMcpServer</code> with HTTP transport now deduplicates on both server name and URL. Calling it with the same name but a different URL creates a new connection. URLs are normalized before comparison (trailing slashes, default ports, hostname case).</li>
<li><strong><code>callbackHost</code> optional for non-OAuth servers</strong> — <code>addMcpServer</code> no longer requires <code>callbackHost</code> when connecting to MCP servers that do not use OAuth.</li>
<li><strong>MCP URL security</strong> — Server URLs are validated before connection to prevent SSRF. Private IP ranges, loopback addresses, link-local addresses, and cloud metadata endpoints are blocked.</li>
<li><strong>Custom denial messages</strong> — <code>addToolOutput</code> now supports <code>state: &quot;output-error&quot;</code> with <code>errorText</code> for custom denial messages in human-in-the-loop tool approval flows.</li>
<li><strong><code>requestId</code> in chat options</strong> — <code>onChatMessage</code> options now include a <code>requestId</code> for logging and correlating events.</li>
</ul>
<h4 id="2026-03-02-agents-sdk-v0.7.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-02">Mar 2, 2026</time><div>
<h2 id="post-2026-03-02-default-gateway"><a href="/changelog/post/2026-03-02-default-gateway/">Get started with AI Gateway automatically</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>You can now start using AI Gateway with a single API call — no setup required. Use <code>default</code> as your gateway ID, and AI Gateway creates one for you automatically on the first request.</p>
<p>To try it out, <a href="/fundamentals/api/get-started/create-token/">create an API token</a> with <code>AI Gateway - Read</code>, <code>AI Gateway - Edit</code>, and <code>Workers AI - Read</code> permissions, then run:</p>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/$CLOUDFLARE_ACCOUNT_ID/default/compat/chat/completions \&#10;  &#45;-header &quot;cf-aig-authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>AI Gateway gives you logging, caching, rate limiting, and access to multiple AI providers through a single endpoint. For more information, refer to <a href="/ai-gateway/get-started/">Get started</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-02">Mar 2, 2026</time><div>
<h2 id="post-2026-03-copy-resources-as-json-or-post-requests"><a href="/changelog/post/2026-03-copy-resources-as-json-or-post-requests/">Copy Cloudflare One resources as JSON or POST requests</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span></div><div class="changelog-body"><p>You can now copy Cloudflare One resources as JSON or as a ready-to-use API POST request directly from the dashboard. This makes it simple to transition workflows into API calls, automation scripts, or infrastructure-as-code pipelines.</p>
<p>To use this feature, click the overflow menu (⋮) on any supported resource and select <strong>Copy as JSON</strong> or <strong>Copy as POST request</strong>. The copied output includes only the fields present on your resource, giving you a clean and minimal starting point for your own API calls.</p>
<p>Initially supported resources:</p>
<ul>
<li>Access applications</li>
<li>Access policies</li>
<li>Gateway policies</li>
<li>Resolver policies</li>
<li>Service tokens</li>
<li>Identity providers</li>
</ul>
<p>We will continue to add support for more resources throughout 2026.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-02">Mar 2, 2026</time><div>
<h2 id="post-2026-03-02-waf-release"><a href="/changelog/post/2026-03-02-waf-release/">WAF Release - 2026-03-02</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces new detections for vulnerabilities in SmarterTools SmarterMail (CVE-2025-52691 and CVE-2026-23760), alongside improvements to an existing Command Injection (nslookup) detection to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-52691: SmarterTools SmarterMail mail server is vulnerable to Arbitrary File Upload, allowing an unauthenticated attacker to upload files to any location on the mail server, potentially enabling remote code execution.</li>
<li>CVE-2026-23760: SmarterTools SmarterMail versions prior to build 9511 contain an authentication bypass vulnerability in the password reset API permitting unaunthenticated to reset system administrator accounts failing to verify existing password or reset token.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these SmarterMail vulnerabilities could lead to full system compromise or unauthorized administrative access to mail servers. Administrators are strongly encouraged to apply vendor patches without delay.</p>
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
				<code class="nb-rule-id" title="0f282f3c89614779966faf52966ec6b1">966ec6b1</code>
</td>
<td>N/A</td>
<td>SmarterMail - Arbitrary File Upload - CVE-2025-52691</td>
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
<td>SmarterMail - Authentication Bypass - CVE-2026-23760</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4bb099bcd71141d4a35c1aa675b64d99">75b64d99</code>
</td>
<td>N/A</td>
<td>Command Injection - Nslookup - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Command Injection - Nslookup" (ID: <code class="nb-rule-id" title="f4a310393c564d50bd585601b090ba9a">b090ba9a</code>)</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-01">Mar 1, 2026</time><div>
<h2 id="post-2026-03-01-rdp-clipboard-controls"><a href="/changelog/post/2026-03-01-rdp-clipboard-controls/">Clipboard controls for browser-based RDP</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>You can now configure clipboard controls for browser-based RDP with Cloudflare Access. Clipboard controls allow administrators to restrict whether users can copy or paste text between their local machine and the remote Windows server.</p>
<p><img src="/assets/upstream/images/changelog/access/rdp-clipboard-controls.png" alt="Enable users to copy and paste content from their local machine to remote RDP sessions in the Cloudflare One dashboard" /></p>
<p>This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting clipboard access, you can prevent sensitive data from being transferred out of the remote session to a user's personal device.</p>
<h4 id="2026-03-01-rdp-clipboard-controls-configuration-options">Configuration options</h4>
<p>Clipboard controls are configured per policy within your Access application. For each policy, you can independently allow or deny:</p>
<ul>
<li><strong>Copy from local client to remote RDP session</strong> — Users can copy/paste text from their local machine into the browser-based RDP session.</li>
<li><strong>Copy from remote RDP session to local client</strong> — Users can copy/paste text from the browser-based RDP session to their local machine.</li>
</ul>
<p>By default, both directions are denied for new policies. For existing Access applications created before this feature was available, clipboard access remains enabled to preserve backwards compatibility.</p>
<p>When a user attempts a restricted clipboard action, the clipboard content is replaced with an error message informing them that the action is not allowed.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#clipboard-controls">Clipboard controls for browser-based RDP</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-27">Feb 27, 2026</time><div>
<h2 id="post-2026-02-27-mcp-portal-logpush"><a href="/changelog/post/2026-02-27-mcp-portal-logpush/">Export MCP server portal logs with Logpush</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-02-27-mcp-portal-logpush-availability">Availability</h4>
@markup("md", "content/.markup/bodies/17617.md")</aside>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> now supports <a href="/logs/logpush/">Logpush</a> integration. You can automatically export MCP server portal activity logs to third-party storage destinations or security information and event management (SIEM) tools for analysis and auditing.</p>
<h4 id="2026-02-27-mcp-portal-logpush-available-log-fields">Available log fields</h4>
<p>The MCP server portal logs dataset includes fields such as:</p>
<ul>
<li><code>Datetime</code> — Timestamp of the request</li>
<li><code>PortalID</code> / <code>PortalAUD</code> — Portal identifiers</li>
<li><code>ServerID</code> / <code>ServerURL</code> — Upstream MCP server details</li>
<li><code>Method</code> — JSON-RPC method (for example, <code>tools/call</code>, <code>prompts/get</code>, <code>resources/read</code>)</li>
<li><code>ToolCallName</code> / <code>PromptGetName</code> / <code>ResourceReadURI</code> — Method-specific identifiers</li>
<li><code>UserID</code> / <code>UserEmail</code> — Authenticated user information</li>
<li><code>Success</code> / <code>Error</code> — Request outcome</li>
<li><code>ServerResponseDurationMs</code> — Response time from upstream server</li>
</ul>
<p>For the complete field reference, refer to <a href="/logs/logpush/logpush-job/datasets/account/mcp_portal_logs/">MCP portal logs</a>.</p>
<h4 id="2026-02-27-mcp-portal-logpush-set-up-logpush">Set up Logpush</h4>
<p>To configure Logpush for MCP server portal logs, refer to <a href="/cloudflare-one/insights/logs/logpush/">Logpush integration</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17616.md")</aside>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-27">Feb 27, 2026</time><div>
<h2 id="post-2026-02-27-new-protocol-detection-protocols"><a href="/changelog/post/2026-02-27-new-protocol-detection-protocols/">New protocols added for Gateway Protocol Detection (Beta)</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Gateway <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol Detection</a> now supports seven additional protocols in beta:</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>IMAP</td>
<td>Internet Message Access Protocol — email retrieval</td>
</tr>
<tr>
<td>POP3</td>
<td>Post Office Protocol v3 — email retrieval</td>
</tr>
<tr>
<td>SMTP</td>
<td>Simple Mail Transfer Protocol — email sending</td>
</tr>
<tr>
<td>MYSQL</td>
<td>MySQL database wire protocol</td>
</tr>
<tr>
<td>RSYNC-DAEMON</td>
<td>rsync daemon protocol</td>
</tr>
<tr>
<td>LDAP</td>
<td>Lightweight Directory Access Protocol</td>
</tr>
<tr>
<td>NTP</td>
<td>Network Time Protocol</td>
</tr>
</tbody>
</table>
<p>These protocols join the existing set of detected protocols (HTTP, HTTP2, SSH, TLS, DCERPC, MQTT, and TPKT) and can be used with the <em>Detected Protocol</em> selector in <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a> to identify and filter traffic based on the application-layer protocol, without relying on port-based identification.</p>
<p>If protocol detection is enabled on your account, these protocols will automatically be logged when detected in your Gateway network traffic.</p>
<p>For more information on using Protocol Detection, refer to the <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol detection documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-27">Feb 27, 2026</time><div>
<h2 id="post-2026-02-27-radar-pq-key-transparency"><a href="/changelog/post/2026-02-27-radar-pq-key-transparency/">Post-Quantum Encryption and Key Transparency on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now tracks post-quantum encryption support on origin servers, provides a tool to test any host for post-quantum compatibility, and introduces a Key Transparency dashboard for monitoring end-to-end encrypted messaging audit logs.</p>
<h4 id="2026-02-27-radar-pq-key-transparency-post-quantum-origin-support">Post-quantum origin support</h4>
<p>The new <a href="/api/resources/radar/subresources/post_quantum/"><code>Post-Quantum</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/"><code>/post_quantum/tls/support</code></a> - Tests whether a host supports post-quantum TLS key exchange.</li>
<li><a href="/api/resources/radar/subresources/post_quantum/methods/summary/"><code>/post_quantum/origin/summary/{dimension}</code></a> - Returns origin post-quantum data summarized by key agreement algorithm.</li>
<li><a href="/api/resources/radar/subresources/post_quantum/methods/timeseries_groups/"><code>/post_quantum/origin/timeseries_groups/{dimension}</code></a> - Returns origin post-quantum timeseries data grouped by key agreement algorithm.</li>
</ul>
<p>The new <a href="https://radar.cloudflare.com/post-quantum">Post-Quantum Encryption</a> page shows the share of customer origins supporting <a href="/ssl/post-quantum-cryptography/pqc-support/#x25519mlkem768">X25519MLKEM768</a>, derived from daily automated TLS scans of TLS 1.3-compatible origins. The scanner tests for algorithm support rather than the origin server's configured preference.</p>
<p><img src="/assets/upstream/images/radar/pq-origin-support.png" alt="Screenshot of the origin post-quantum support graph on Radar" /></p>
<p>A host test tool allows checking any publicly accessible website for post-quantum encryption compatibility. Enter a hostname and optional port to see whether the server negotiates a post-quantum key exchange algorithm.</p>
<p><img src="/assets/upstream/images/radar/pq-host-test.png" alt="Screenshot of the post-quantum host test tool on Radar" /></p>
<h4 id="2026-02-27-radar-pq-key-transparency-key-transparency">Key Transparency</h4>
<p>A new <a href="https://radar.cloudflare.com/key-transparency">Key Transparency</a> section displays the audit status of Key Transparency logs for end-to-end encrypted messaging services. The page launches with two monitored logs: WhatsApp and Facebook Messenger Transport.</p>
<p>Each log card shows the current status, last signed epoch, last verified epoch, and the root hash of the Auditable Key Directory tree. The data is also available through the <a href="/key-transparency/api/">Key Transparency Auditor API</a>.</p>
<p><img src="/assets/upstream/images/radar/key-transparency-dashboard.png" alt="Screenshot of the Key Transparency dashboard on Radar" /></p>
<p>Learn more about these features in our <a href="https://blog.cloudflare.com/radar-origin-pq-key-transparency-aspa">blog post</a> and check out the <a href="https://radar.cloudflare.com/post-quantum">Post-Quantum Encryption</a> and <a href="https://radar.cloudflare.com/key-transparency">Key Transparency</a> pages to explore the data.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-26">Feb 26, 2026</time><div>
<h2 id="post-2026-02-26-async-stale-while-revalidate"><a href="/changelog/post/2026-02-26-async-stale-while-revalidate/">Asynchronous stale-while-revalidate</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Cloudflare's <a href="/cache/concepts/cache-control/#revalidation"><code>stale-while-revalidate</code></a> support is now fully asynchronous. Previously, the first request for a stale (expired) asset in cache had to wait for an origin response, after which that visitor received a REVALIDATED or EXPIRED status. Now, the first request after the asset expires triggers revalidation in the background and immediately receives stale content with an UPDATING status. All following requests also receive stale content with an <code>UPDATING</code> status until the origin responds, after which subsequent requests receive fresh content with a <code>HIT</code> status.</p>
<p><code>stale-while-revalidate</code> is a <code>Cache-Control</code> directive set by your origin server that allows Cloudflare to serve an expired cached asset while a fresh copy is fetched from the origin.</p>
<p>Asynchronous revalidation brings:</p>
<ul>
<li><strong>Lower latency</strong>: No visitor is waiting for the origin when the asset is already in cache. Every request is served from cache during revalidation.</li>
<li><strong>Consistent experience</strong>: All visitors receive the same cached response during revalidation.</li>
<li><strong>Reduced error exposure</strong>: The first request is no longer vulnerable to origin timeouts or errors. All visitors receive a cached response while revalidation happens in the background.</li>
</ul>
<h4 id="2026-02-26-async-stale-while-revalidate-availability">Availability</h4>
<p>This change is live for all Free, Pro, and Business zones. Approximately 75% of Enterprise zones have been migrated, with the remaining zones rolling out throughout the quarter.</p>
<h4 id="2026-02-26-async-stale-while-revalidate-get-started">Get started</h4>
<p>To use this feature, make sure your origin includes the <code>stale-while-revalidate</code> directive in the <code>Cache-Control</code> header. Refer to the <a href="/cache/concepts/cache-control/#revalidation">Cache-Control documentation</a> for details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-26">Feb 26, 2026</time><div>
<h2 id="post-2026-02-26-markdown-responses-for-1xxx-errors"><a href="/changelog/post/2026-02-26-markdown-responses-for-1xxx-errors/">Markdown responses for Cloudflare 1xxx errors</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare now returns structured Markdown responses for Cloudflare-generated 1xxx errors when clients send <code>Accept: text/markdown</code>.</p>
<p>Each response includes YAML frontmatter plus guidance sections (<code>What happened</code> / <code>What you should do</code>) so agents can make deterministic retry and escalation decisions without parsing HTML.</p>
<p>In measured 1,015 comparisons, Markdown reduced payload size and token footprint by over 98% versus HTML.</p>
<p>Included frontmatter fields:</p>
<ul>
<li><code>error_code</code>, <code>error_name</code>, <code>error_category</code>, <code>http_status</code></li>
<li><code>ray_id</code>, <code>timestamp</code>, <code>zone</code></li>
<li><code>cloudflare_error</code>, <code>retryable</code>, <code>retry_after</code> (when applicable), <code>owner_action_required</code></li>
</ul>
<p>Default behavior is unchanged: clients that do not explicitly request Markdown continue to receive HTML error pages.</p>
<h4 id="2026-02-26-markdown-responses-for-1xxx-errors-negotiation-behavior">Negotiation behavior</h4>
<p>Cloudflare uses standard HTTP content negotiation on the <code>Accept</code> header.</p>
<ul>
<li><code>Accept: text/markdown</code> -&gt; Markdown</li>
<li><code>Accept: text/markdown, text/html;q=0.9</code> -&gt; Markdown</li>
<li><code>Accept: text/*</code> -&gt; Markdown</li>
<li><code>Accept: */*</code> -&gt; HTML (default browser behavior)</li>
</ul>
<p>When multiple values are present, Cloudflare selects the highest-priority supported media type using <code>q</code> values. If Markdown is not explicitly preferred, HTML is returned.</p>
<h4 id="2026-02-26-markdown-responses-for-1xxx-errors-availability">Availability</h4>
<p>Available now for Cloudflare-generated 1xxx errors.</p>
<h4 id="2026-02-26-markdown-responses-for-1xxx-errors-get-started">Get started</h4>
<pre><code class="language-bash">curl -H &quot;Accept: text/markdown&quot; https://&lt;your-domain&gt;/cdn-cgi/error/1015&#10;</code></pre>
<p>Reference: <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx error documentation</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-25">Feb 25, 2026</time><div>
<h2 id="post-2026-02-25-agents-sdk-v0.6.0"><a href="/changelog/post/2026-02-25-agents-sdk-v0.6.0/">Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> lets you define an Agent and an McpAgent in the same Worker and connect them over RPC — no HTTP, no network overhead. It also makes OAuth opt-in for simple MCP connections, hardens the schema converter for production workloads, and ships a batch of <code>@cloudflare/ai-chat</code> reliability fixes.</p>
<h4 id="2026-02-25-agents-sdk-v0.6.0-rpc-transport-for-mcp">RPC transport for MCP</h4>
<p>You can now connect an Agent to an McpAgent in the same Worker using a Durable Object binding instead of an HTTP URL. The connection stays entirely within the Cloudflare runtime — no network round-trips, no serialization overhead.</p>
<p>Pass the Durable Object namespace directly to <code>addMcpServer</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17642.md")</div>
<p>The <code>addMcpServer</code> method now accepts <code>string | DurableObjectNamespace</code> as the second parameter with full TypeScript overloads, so HTTP and RPC paths are type-safe and cannot be mixed.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Hibernation support</strong> — RPC connections survive Durable Object hibernation automatically. The binding name and props are persisted to storage and restored on wake-up, matching the behavior of HTTP MCP connections.</li>
<li><strong>Deduplication</strong> — Calling <code>addMcpServer</code> with the same server name returns the existing connection instead of creating duplicates. Connection IDs are stable across hibernation restore.</li>
<li><strong>Smaller surface area</strong> — The RPC transport internals have been rewritten and reduced from 609 lines to 245 lines. <code>RPCServerTransport</code> now uses <code>JSONRPCMessageSchema</code> from the MCP SDK for validation instead of hand-written checks.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17641.md")</aside>
<h4 id="2026-02-25-agents-sdk-v0.6.0-optional-oauth-for-mcp-connections">Optional OAuth for MCP connections</h4>
<p><code>addMcpServer()</code> no longer eagerly creates an OAuth provider for every connection. For servers that do not require authentication, a simple call is all you need:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17643.md")</div>
<p>If the server responds with a 401, the SDK throws a clear error: <code>&quot;This MCP server requires OAuth authentication. Provide callbackHost in addMcpServer options to enable the OAuth flow.&quot;</code> The restore-from-storage flow also handles missing callback URLs gracefully, skipping auth provider creation for non-OAuth servers.</p>
<h4 id="2026-02-25-agents-sdk-v0.6.0-hardened-json-schema-to-typescript-converter">Hardened JSON Schema to TypeScript converter</h4>
<p>The schema converter used by <code>generateTypes()</code> and <code>getAITools()</code> now handles edge cases that previously caused crashes in production:</p>
<ul>
<li><strong>Depth and circular reference guards</strong> — Prevents stack overflows on recursive or deeply nested schemas</li>
<li><strong><code>$ref</code> resolution</strong> — Supports internal JSON Pointers (<code>#/definitions/...</code>, <code>#/$defs/...</code>, <code>#</code>)</li>
<li><strong>Tuple support</strong> — <code>prefixItems</code> (JSON Schema 2020-12) and array <code>items</code> (draft-07)</li>
<li><strong>OpenAPI 3.0 <code>nullable: true</code></strong> — Supported across all schema branches</li>
<li><strong>Per-tool error isolation</strong> — One malformed schema cannot crash the full pipeline in <code>generateTypes()</code> or <code>getAITools()</code></li>
<li><strong>Missing <code>inputSchema</code> fallback</strong> — <code>getAITools()</code> falls back to <code>{ type: &quot;object&quot; }</code> instead of throwing</li>
</ul>
<h4 id="2026-02-25-agents-sdk-v0.6.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Tool denial flow</strong> — Denied tool approvals (<code>approved: false</code>) now transition to <code>output-denied</code> with a <code>tool_result</code>, fixing Anthropic provider compatibility. Custom denial messages are supported via <code>state: &quot;output-error&quot;</code> and <code>errorText</code>.</li>
<li><strong>Abort/cancel support</strong> — Streaming responses now properly cancel the reader loop when the abort signal fires and send a done signal to the client.</li>
<li><strong>Duplicate message persistence</strong> — <code>persistMessages()</code> now reconciles assistant messages by content and order, preventing duplicate rows when clients resend full history.</li>
<li><strong><code>requestId</code> in <code>OnChatMessageOptions</code></strong> — Handlers can now send properly-tagged error responses for pre-stream failures.</li>
<li><strong><code>redacted_thinking</code> preservation</strong> — The message sanitizer no longer strips Anthropic <code>redacted_thinking</code> blocks.</li>
<li><strong><code>/get-messages</code> reliability</strong> — Endpoint handling moved from a prototype <code>onRequest()</code> override to a constructor wrapper, so it works even when users override <code>onRequest</code> without calling <code>super.onRequest()</code>.</li>
<li><strong>Client tool APIs undeprecated</strong> — <code>createToolsFromClientSchemas</code>, <code>clientTools</code>, <code>AITool</code>, <code>extractClientToolSchemas</code>, and the <code>tools</code> option on <code>useAgentChat</code> are restored for SDK use cases where tools are defined dynamically at runtime.</li>
<li><strong><code>jsonSchema</code> initialization</strong> — Fixed <code>jsonSchema not initialized</code> error when calling <code>getAITools()</code> in <code>onChatMessage</code>.</li>
</ul>
<h4 id="2026-02-25-agents-sdk-v0.6.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-25">Feb 25, 2026</time><div>
<h2 id="post-2026-02-25-higher-container-resource-limits"><a href="/changelog/post/2026-02-25-higher-container-resource-limits/">Run 15x more Containers with higher resource limits</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now run more <a href="/containers/">Containers</a> concurrently with significantly higher limits on memory, vCPU, and disk.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous Limit</th>
<th>New Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory for concurrent live Container instances</td>
<td>400GiB</td>
<td>6TiB</td>
</tr>
<tr>
<td>vCPU for concurrent live Container instances</td>
<td>100</td>
<td>1,500</td>
</tr>
<tr>
<td>Disk for concurrent live Container instances</td>
<td>2TB</td>
<td>30TB</td>
</tr>
</tbody>
</table>
<p>This 15x increase enables larger-scale workloads on Containers. You can now run 15,000 instances of the <code>lite</code> instance type, 6,000 instances of <code>basic</code>, over 1,500 instances of <code>standard-1</code>, or over 1,000 instances of <code>standard-2</code> concurrently.</p>
<p>Refer to <a href="/containers/platform/limits/">Limits</a> for more details on the available instance types and limits.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-25">Feb 25, 2026</time><div>
<h2 id="post-2026-02-25-radar-aspa-insights"><a href="/changelog/post/2026-02-25-radar-aspa-insights/">RPKI ASPA Deployment Insights on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes <a href="https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/">Autonomous System Provider Authorization (ASPA)</a> deployment insights, providing visibility into the adoption and verification of ASPA objects across the global routing ecosystem.</p>
<h4 id="2026-02-25-radar-aspa-insights-new-api-endpoints">New API endpoints</h4>
<p>The new <a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/"><code>ASPA</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/"><code>/bgp/rpki/aspa/snapshot</code></a> - Retrieves current or historical ASPA objects.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes/"><code>/bgp/rpki/aspa/changes</code></a> - Retrieves changes to ASPA objects over time.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries/"><code>/bgp/rpki/aspa/timeseries</code></a> - Retrieves ASPA object counts over time as a timeseries.</li>
</ul>
<h4 id="2026-02-25-radar-aspa-insights-new-radar-widgets">New Radar widgets</h4>
<p>The <a href="https://radar.cloudflare.com/routing">global routing page</a> now shows the ASPA deployment trend over time by counting daily ASPA objects.</p>
<p><img src="/assets/upstream/images/radar/aspa-global-trend.png" alt="Screenshot of the ASPA deployment trend chart" /></p>
<p>The global routing page also displays the most recent ASPA objects, searchable by ASN or AS name.</p>
<p><img src="/assets/upstream/images/radar/aspa-global-table.png" alt="Screenshot of the ASPA objects table" /></p>
<p>On country and region routing pages, a new widget shows the ASPA deployment rate for ASNs registered in the selected country or region.</p>
<p><img src="/assets/upstream/images/radar/aspa-germany-trend.png" alt="Screenshot of the ASPA deployment trent chart for Germany" /></p>
<p>On AS routing pages, the connectivity table now includes checkmarks for ASPA-verified upstreams. All ASPA upstreams are listed in a dedicated table, and a timeline shows ASPA changes at daily granularity.</p>
<p><img src="/assets/upstream/images/radar/aspa-asn-timeline.png" alt="Screenshot of the ASPA changes timeline on an AS routing page" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/routing">Radar routing page</a> to explore the data.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-25">Feb 25, 2026</time><div>
<h2 id="post-2026-02-13-pywrangler-windows-support"><a href="/changelog/post/2026-02-13-pywrangler-windows-support/">Better Windows support for Python Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler">Pywrangler</a>, the CLI tool for managing Python Workers and packages,
now supports Windows, allowing you to develop and deploy Python Workers from Windows environments.
Previously, Pywrangler was only available on macOS and Linux.</p>
<p>You can install and use Pywrangler on Windows the same way you would on other platforms.
<a href="/workers/languages/python/packages/">Specify your Worker's Python dependencies</a> in your <code>pyproject.toml</code> file,
then use the following commands to develop and deploy:</p>
<pre><code class="language-bash">uvx --from workers-py pywrangler dev&#10;uvx --from workers-py pywrangler deploy&#10;</code></pre>
<p>All existing Pywrangler functionality, including package management, local development, and deployment, works on Windows without any additional configuration.</p>
<h4 id="2026-02-13-pywrangler-windows-support-requirements">Requirements</h4>
<p>This feature requires the following minimum versions:</p>
<ul>
<li><code>wrangler</code> &gt;= 4.64.0</li>
<li><code>workers-py</code> &gt;= 1.72.0</li>
<li><code>uv</code> &gt;= 0.29.8</li>
</ul>
<p>To upgrade <code>workers-py</code> (which includes Pywrangler) in your project, run:</p>
<pre><code class="language-bash">uv tool upgrade workers-py&#10;</code></pre>
<p>To upgrade <code>wrangler</code>, run:</p>
<pre><code class="language-bash">npm install -g wrangler@latest&#10;</code></pre>
<p>To upgrade <code>uv</code>, run:</p>
<pre><code class="language-bash">uv self update&#10;</code></pre>
<p>To get started with Python Workers on Windows, refer to the <a href="/workers/languages/python/packages/">Python packages documentation</a> for full details on Pywrangler.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-25">Feb 25, 2026</time><div>
<h2 id="post-2026-02-24-observability-query-language"><a href="/changelog/post/2026-02-24-observability-query-language/">Write structured queries to filter and search your Workers logs and traces</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/observability/">Workers Observability</a> now includes a query language that lets you write structured queries directly in the search bar to filter your logs and traces. The search bar doubles as a free text search box — type any term to search across all metadata and attributes, or write field-level queries for precise filtering.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-02-24-query-language.png" alt="Workers Observability search bar with autocomplete suggestions and Query Builder sidebar filters" /></p>
<p>Queries written in the search bar sync with the <a href="/workers/observability/">Query Builder</a> sidebar, so you can write a query by hand and then refine it visually, or build filters in the Query Builder and see the corresponding query syntax. The search bar provides autocomplete suggestions for metadata fields and operators as you type.</p>
<p>The query language supports:</p>
<ul>
<li><strong>Free text search</strong> — search everywhere with a keyword like <code>error</code>, or match an exact phrase with <code>&quot;exact phrase&quot;</code></li>
<li><strong>Field queries</strong> — filter by specific fields using comparison operators (for example, <code>status = 500</code> or <code>$workers.wallTimeMs &gt; 100</code>)</li>
<li><strong>Operators</strong> — <code>=</code>, <code>!=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code>, <code>&lt;=</code>, and <code>:</code> (contains)</li>
<li><strong>Functions</strong> — <code>contains(field, value)</code>, <code>startsWith(field, prefix)</code>, <code>regex(field, pattern)</code>, and <code>exists(field)</code></li>
<li><strong>Boolean logic</strong> — add conditions with <code>AND</code>, <code>OR</code>, and <code>NOT</code></li>
</ul>
<p>Select the help icon next to the search bar to view the full syntax reference, including all supported operators, functions, and keyboard shortcuts.</p>
<p>Go to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> to try the query language.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-25">Feb 25, 2026</time><div>
<h2 id="post-2026-02-25-wrangler-autoconfig-ga"><a href="/changelog/post/2026-02-25-wrangler-autoconfig-ga/">No config? No problem. Just `wrangler deploy`</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now deploy any existing project to Cloudflare Workers — even without a Wrangler configuration file — and <code>wrangler deploy</code> will <em>just work</em>.</p>
<p>Starting with Wrangler <strong>4.68.0</strong>, running <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> <a href="/workers/framework-guides/automatic-configuration/">automatically configures your project</a> by detecting your framework, installing required adapters, and deploying it to Cloudflare Workers.</p>
<h4 id="2026-02-25-wrangler-autoconfig-ga-using-wrangler-locally">Using Wrangler locally</h4>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>When you run <code>wrangler deploy</code> in a project without a configuration file, Wrangler:</p>
<ol>
<li>Detects your framework from <code>package.json</code></li>
<li>Prompts you to confirm the detected settings</li>
<li>Installs any required adapters</li>
<li>Generates a <code>wrangler.jsonc</code> <a href="/workers/wrangler/configuration/">configuration file</a></li>
<li>Deploys your project to Cloudflare Workers</li>
</ol>
<p>You can also use <a href="/workers/wrangler/commands/general/#setup"><code>wrangler setup</code></a> to configure without deploying, or pass <a href="/workers/wrangler/commands/general/#deploy"><code>--yes</code></a> to skip prompts.</p>
<h4 id="2026-02-25-wrangler-autoconfig-ga-using-the-cloudflare-dashboard">Using the Cloudflare dashboard</h4>
<p><img src="/assets/upstream/images/workers/ci-cd/builds/automatic-pr.png" alt="Automatic configuration pull request created by Workers Builds" /></p>
<p>When you connect a repository through the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create">Workers dashboard</a>, a <a href="/workers/ci-cd/builds/automatic-prs/">pull request is generated</a> for you with all necessary files, and a <a href="/workers/versions-and-deployments/preview-urls/">preview deployment</a> to check before merging.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17800.md")</aside>
<h4 id="2026-02-25-wrangler-autoconfig-ga-background">Background</h4>
<p>In December 2025, we <a href="/changelog/2025-12-16-wrangler-autoconfig/">introduced automatic configuration</a> as an experimental feature. It is now generally available and the default behavior.</p>
<p>If you have questions or run into issues, join the <a href="https://github.com/cloudflare/workers-sdk/discussions/11667">GitHub discussion</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-24">Feb 24, 2026</time><div>
<h2 id="post-2026-02-24-deleteall-deletes-alarms"><a href="/changelog/post/2026-02-24-deleteall-deletes-alarms/">deleteAll() now deletes Durable Object alarm</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p><code>deleteAll()</code> now deletes a Durable Object alarm in addition to stored data for Workers with a compatibility date of <code>2026-02-24</code> or later. This change simplifies clearing a Durable Object's storage with a single API call.</p>
<p>Previously, <code>deleteAll()</code> only deleted user-stored data for an object. Alarm usage stores metadata in an object's storage, which required a separate <code>deleteAlarm()</code> call to fully clean up all storage for an object. The <code>deleteAll()</code> change applies to both KV-backed and SQLite-backed Durable Objects.</p>
<pre><code class="language-js">// Before: two API calls required to clear all storage&#10;await this.ctx.storage.deleteAlarm();&#10;await this.ctx.storage.deleteAll();&#10;&#10;// Now: a single call clears both data and the alarm&#10;await this.ctx.storage.deleteAll();&#10;</code></pre>
<p>For more information, refer to the <a href="/durable-objects/api/sqlite-storage-api/#deleteall">Storage API documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-24">Feb 24, 2026</time><div>
<h2 id="post-2026-02-24-typed-bindings-setup-improvements-error-metrics"><a href="/changelog/post/2026-02-24-typed-bindings-setup-improvements-error-metrics/">Dropped event metrics, typed Pipelines bindings, and improved setup</a></h2>
<div class="changelog-badges"><span>pipelines</span><span>workers</span></div><div class="changelog-body"><p><a href="/pipelines/">Cloudflare Pipelines</a> ingests streaming data via <a href="/workers/">Workers</a> or HTTP endpoints, transforms it with SQL, and writes it to <a href="/r2/">R2</a> as Apache Iceberg tables. Today we're shipping three improvements to help you understand why streaming events get dropped, catch data quality issues early, and set up Pipelines faster.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-dropped-event-metrics">Dropped event metrics</h4>
<p>When <a href="/pipelines/streams/">stream</a> events don't match the expected schema, Pipelines accepts them during ingestion but drops them when attempting to deliver them to the <a href="/pipelines/sinks/">sink</a>. To help you identify the root cause of these issues, we are introducing a new dashboard and metrics that surface dropped events with detailed error messages.</p>
<p><img src="/assets/upstream/images/pipelines/pipelines-error-log-dash.png" alt="The Errors tab in the Cloudflare dashboard showing deserialization errors grouped by type with individual error details" /></p>
<p>Dropped events can also be queried programmatically via the new <code>pipelinesUserErrorsAdaptiveGroups</code> GraphQL dataset. The dataset breaks down failures by specific error type (<code>missing_field</code>, <code>type_mismatch</code>, <code>parse_failure</code>, or <code>null_value</code>) so you can trace issues back to the source.</p>
<pre><code class="language-graphql">query GetPipelineUserErrors(&#10;	$accountTag: String!&#10;	$pipelineId: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			pipelinesUserErrorsAdaptiveGroups(&#10;				limit: 100&#10;				filter: {&#10;					pipelineId: $pipelineId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					errorFamily&#10;					errorType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>For the full list of dimensions, error types, and additional query examples, refer to <a href="/pipelines/observability/metrics/#user-error-metrics">User error metrics</a>.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-typed-pipelines-bindings">Typed Pipelines bindings</h4>
<p>Sending data to a Pipeline from a Worker previously used a generic <code>Pipeline&lt;PipelineRecord&gt;</code> type, which meant schema mismatches (wrong field names, incorrect types) were only caught at runtime as dropped events.</p>
<p>Running <code>wrangler types</code> now generates schema-specific TypeScript types for your <a href="/pipelines/streams/writing-to-streams/#send-via-workers">Pipeline bindings</a>. TypeScript catches missing required fields and incorrect field types at compile time, before your code is deployed.</p>
<pre><code class="language-ts">declare namespace Cloudflare {&#10;	type EcommerceStreamRecord = {&#10;		user_id: string;&#10;		event_type: string;&#10;		product_id?: string;&#10;		amount?: number;&#10;	};&#10;	interface Env {&#10;		STREAM: import(&quot;cloudflare:pipelines&quot;).Pipeline&lt;Cloudflare.EcommerceStreamRecord&gt;;&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/pipelines/streams/writing-to-streams/#typed-pipeline-bindings">Typed Pipeline bindings</a>.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-improved-pipelines-setup">Improved Pipelines setup</h4>
<p>Setting up a new Pipeline previously required multiple manual steps: creating an R2 bucket, enabling R2 Data Catalog, generating an API token, and configuring format, compression, and rolling policies individually.</p>
<p>The <code>wrangler pipelines setup</code> command now offers a <strong>Simple</strong> setup mode that applies recommended defaults and automatically creates the <a href="/r2/buckets/">R2 bucket</a> and enables <a href="/r2-data-catalog/">R2 Data Catalog</a> if they do not already exist. Validation errors during setup prompt you to retry inline rather than restarting the entire process.</p>
<p>For a full walkthrough, refer to the <a href="/pipelines/getting-started/">Getting started guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-24">Feb 24, 2026</time><div>
<h2 id="post-2026-02-24-disable-live-inputs"><a href="/changelog/post/2026-02-24-disable-live-inputs/">Stream live inputs can now be disabled and enabled</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now disable a live input to reject incoming RTMPS and SRT
connections. When a live input is disabled, any broadcast attempts will fail to
connect.</p>
<p>This gives you more control over your live inputs:</p>
<ul>
<li>Temporarily pause an input without deleting it</li>
<li>Programmatically end creator broadcasts</li>
<li>Prevent new broadcasts from starting on a specific input</li>
</ul>
<p>To disable a live input via the API, set the <code>enabled</code> property to <code>false</code>:</p>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: false}&#x27;&#10;</code></pre>
<p>You can also disable or enable a live input from the <strong>Live inputs</strong> list page
or the live input detail page in the Dashboard.</p>
<p>All existing live inputs remain enabled by default. For more information, refer
to <a href="/stream/stream-live/start-stream-live/">Start a live stream</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-24">Feb 24, 2026</time><div>
<h2 id="post-2026-02-24-warp-linux-ga"><a href="/changelog/post/2026-02-24-warp-linux-ga/">WARP client for Linux (version 2026.1.150.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
<li>Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.</li>
<li>Fixed issues causing DNS requests to fail with clients in Traffic and DNS mode or DNS only mode.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-24">Feb 24, 2026</time><div>
<h2 id="post-2026-02-24-warp-macos-ga"><a href="/changelog/post/2026-02-24-warp-macos-ga/">WARP client for macOS (version 2026.1.150.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
<li>Fixed an issue with DNS server configuration failures that caused tunnel connection delays.</li>
<li>Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.</li>
<li>Fixed an issue causing DNS requests to fail with clients in Traffic and DNS mode.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-24">Feb 24, 2026</time><div>
<h2 id="post-2026-02-24-warp-windows-ga"><a href="/changelog/post/2026-02-24-warp-windows-ga/">WARP client for Windows (version 2026.1.150.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improvements to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multi-user mode</a>. Fixed an issue where when switching from a pre-login registration to a user registration, Mobile Device Management (MDM) configuration association could be lost.</li>
<li>Added a new feature to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#netbios-over-tcpip">manage NetBIOS over TCP/IP</a> functionality on the Windows client. NetBIOS over TCP/IP on the Windows client is now disabled by default and can be enabled in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile settings</a>.</li>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for the Windows <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/client-certificate/">client certificate posture check</a> to ensure logged results are from checks that run once users log in.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
<li>Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.</li>
<li>Fixed an issue causing DNS requests to fail with clients in Traffic and DNS mode.</li>
<li>Improved service shutdown behavior in cases where the daemon is unresponsive.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while WARP is connected.</li>
</ul>
<p>To work around this issue, reconnect the WARP client by toggling off and back on.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-23">Feb 23, 2026</time><div>
<h2 id="post-2026-02-23-sandbox-backup-restore-api"><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore API for Sandbox SDK</a></h2>
<div class="changelog-badges"><span>agents</span><span>r2</span><span>containers</span></div><div class="changelog-body"><p><a href="/sandbox/">Sandboxes</a> now support <code>createBackup()</code> and <code>restoreBackup()</code> methods for creating and restoring point-in-time snapshots of directories.</p>
<p>This allows you to restore environments quickly. For instance, in order to develop in a sandbox, you may need to include a user's codebase and run a build step.
Unfortunately <code>git clone</code> and <code>npm install</code> can take minutes, and you don't want to run these steps every time the user starts their sandbox.</p>
<p>Now, after the initial setup, you can just call <code>createBackup()</code>, then <code>restoreBackup()</code> the next time this environment is needed. This makes it practical to pick up exactly
where a user left off, even after days of inactivity, without repeating expensive setup steps.</p>
<pre><code class="language-ts">const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;&#10;// Make non-trivial changes to the file system&#10;await sandbox.gitCheckout(endUserRepo, { targetDir: &quot;/workspace&quot; });&#10;await sandbox.exec(&quot;npm install&quot;, { cwd: &quot;/workspace&quot; });&#10;&#10;// Create a point-in-time backup of the directory&#10;const backup = await sandbox.createBackup({ dir: &quot;/workspace&quot; });&#10;&#10;// Store the handle for later use&#10;await env.KV.put(`backup:${userId}`, JSON.stringify(backup));&#10;&#10;// ... in a future session...&#10;&#10;// Restore instead of re-cloning and reinstalling&#10;await sandbox.restoreBackup(backup);&#10;</code></pre>
<p>Backups are stored in <a href="/r2">R2</a> and can take advantage of <a href="/sandbox/guides/backup-restore/#configure-r2-lifecycle-rules-for-automatic-cleanup">R2 object lifecycle rules</a> to ensure they do not persist forever.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Persist and reuse across sandbox sessions</strong> — Easily store backup handles in KV, D1, or Durable Object storage for use in subsequent sessions</li>
<li><strong>Usable across multiple instances</strong> — Fork a backup across many sandboxes for parallel work</li>
<li><strong>Named backups</strong> — Provide optional human-readable labels for easier management</li>
<li><strong>TTLs</strong> — Set time-to-live durations so backups are automatically removed from storage once they are no longer needed</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17640.md")</aside>
<p>To get started, refer to the <a href="/sandbox/guides/backup-restore/">backup and restore guide</a> for setup instructions and usage patterns, or the <a href="/sandbox/api/backups/">Backups API reference</a> for full method documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-23">Feb 23, 2026</time><div>
<h2 id="post-2026-02-23-hyperdrive-stable-functions-uncacheable"><a href="/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/">Hyperdrive no longer caches queries using STABLE PostgreSQL functions</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now treats queries containing PostgreSQL <code>STABLE</code> functions as uncacheable, in addition to <code>VOLATILE</code> functions.</p>
<p>Previously, only functions <a href="https://www.postgresql.org/docs/current/xfunc-volatility.html">that PostgreSQL categorizes</a> as <code>VOLATILE</code> (for example, <code>RANDOM()</code>, <code>LASTVAL()</code>) were detected as uncacheable. <code>STABLE</code> functions (for example, <code>NOW()</code>, <code>CURRENT_TIMESTAMP</code>, <code>CURRENT_DATE</code>) were incorrectly allowed to be cached.</p>
<p>Because <code>STABLE</code> functions can return different results across different SQL statements within the same transaction, caching their results could serve stale or incorrect data. This change aligns Hyperdrive's caching behavior with PostgreSQL's function volatility semantics.</p>
<p>If your queries use <code>STABLE</code> functions, and you were relying on them being cached, move the function call to your application code and pass the result as a query parameter. For example, instead of <code>WHERE created_at &gt; NOW()</code>, compute the timestamp in your Worker and pass it as <code>WHERE created_at &gt; $1</code>.</p>
<p>Hyperdrive uses text-based pattern matching to detect uncacheable functions. References to function names like <code>NOW()</code> in SQL comments also cause the query to be marked as uncacheable.</p>
<p>For more information, refer to <a href="/hyperdrive/concepts/query-caching/">Query caching</a> and <a href="/hyperdrive/observability/troubleshooting/">Troubleshoot and debug</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/23/">Previous</a><span>Page 24 of 50</span><a class="pagination-next" rel="next" href="/changelog/25/">Next</a></nav>
</div>
