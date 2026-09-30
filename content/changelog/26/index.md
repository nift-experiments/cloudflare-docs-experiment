---
cp9:
  canonical: https://developers.cloudflare.com/changelog/26/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 26 | Cloudflare Docs
  head_html: <title>Changelog - page 26 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/26/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 26"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/26/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/26/#page","headline":"Changelog - page 26 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/26/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/26/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-02-12">Feb 12, 2026</time><div>
<h2 id="post-2026-02-12-terraform-v5.17.0-provider"><a href="/changelog/post/2026-02-12-terraform-v5.17.0-provider/">Terraform v5.17.0 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>In January 2025, we announced the launch of the new Terraform v5 Provider. We
greatly appreciate the proactive engagement and valuable feedback from the
Cloudflare community following the v5 release. In response, we have established
a consistent and rapid <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> for releasing targeted improvements,
demonstrating our commitment to stability and reliability.</p>
<p>With the help of the community, we have a growing number of resources that we
have marked as <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">stable</a>, with that list continuing to grow with every release.
The most used <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">resources</a> are on track to be stable by the end of March 2026,
when we will also be releasing a new migration tool to help you migrate from v4
to v5 with ease.</p>
<p>This release brings new capabilities for AI Search, enhanced Workers Script
placement controls, and numerous bug fixes based on community feedback. We also
begun laying foundational work for improving the v4 to v5 migration process.
Stay tuned for more details as we approach the March 2026 release timeline.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and
help us build products that reflect your needs.</p>
<h4 id="2026-02-12-terraform-v5.17.0-provider-features">Features</h4>
<ul>
<li><strong>ai_search_instance:</strong> add data source for querying AI Search instances</li>
<li><strong>ai_search_token:</strong> add data source for querying AI Search tokens</li>
<li><strong>account:</strong> add support for tenant unit management with new <code>unit</code> field</li>
<li><strong>account:</strong> add automatic mapping from <code>managed_by.parent_org_id</code> to <code>unit.id</code></li>
<li><strong>authenticated_origin_pulls_certificate:</strong> add data source for querying authenticated origin pull certificates</li>
<li><strong>authenticated_origin_pulls_hostname_certificate:</strong> add data source for querying hostname-specific authenticated origin pull certificates</li>
<li><strong>authenticated_origin_pulls_settings:</strong> add data source for querying authenticated origin pull settings</li>
<li><strong>workers_kv:</strong> add <code>value</code> field to data source to retrieve KV values directly</li>
<li><strong>workers_script:</strong> add <code>script</code> field to data source to retrieve script content</li>
<li><strong>workers_script:</strong> add support for <code>simple</code> rate limit binding</li>
<li><strong>workers_script:</strong> add support for targeted placement mode with <code>placement.target</code> array for specifying placement targets (region, hostname, host)</li>
<li><strong>workers_script:</strong> add <code>placement_mode</code> and <code>placement_status</code> computed fields</li>
<li><strong>zero_trust_dex_test:</strong> add data source with filter support for finding specific tests</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> add <code>enabled_entries</code> field for flexible entry management</li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account:</strong> map <code>managed_by.parent_org_id</code> to <code>unit.id</code> in unmarshall and add acceptance tests</li>
<li><strong>authenticated_origin_pulls_certificate:</strong> add certificate normalization to prevent drift</li>
<li><strong>authenticated_origin_pulls:</strong> handle array response and implement full lifecycle</li>
<li><strong>authenticated_origin_pulls_hostname_certificate:</strong> fix resource and tests</li>
<li><strong>cloudforce_one_request_message:</strong> use correct <code>request_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>dns_zone_transfers_incoming:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>dns_zone_transfers_outgoing:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>email_routing_settings:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>hyperdrive_config:</strong> add proper handling for write-only fields to prevent state drift</li>
<li><strong>hyperdrive_config:</strong> add normalization for empty <code>mtls</code> objects to prevent unnecessary diffs</li>
<li><strong>magic_network_monitoring_rule:</strong> use correct <code>account_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>mtls_certificates:</strong> fix resource and test</li>
<li><strong>pages_project:</strong> revert build_config to computed optional</li>
<li><strong>stream_key:</strong> use correct <code>account_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>total_tls:</strong> use upsert pattern for singleton zone setting</li>
<li><strong>waiting_room_rules:</strong> use correct <code>waiting_room_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>workers_script:</strong> add support for placement mode/status</li>
<li><strong>zero_trust_access_application:</strong> update v4 version on migration tests</li>
<li><strong>zero_trust_device_posture_rule:</strong> update tests to match API</li>
<li><strong>zero_trust_dlp_integration_entry:</strong> use correct <code>entry_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>zero_trust_dlp_predefined_entry:</strong> use correct <code>entry_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>zero_trust_organization:</strong> fix plan issues</li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-chores">Chores</h4>
<ul>
<li>add state upgraders to 95+ resources to lay the foundation for replacing Grit
(still under active development)</li>
<li><strong>certificate_pack:</strong> add state migration handler for SDKv2 to Framework conversion</li>
<li><strong>custom_hostname_fallback_origin:</strong> add comprehensive lifecycle test and migration support</li>
<li><strong>dns_record:</strong> add state migration handler for SDKv2 to Framework conversion</li>
<li><strong>leaked_credential_check:</strong> add import functionality and tests</li>
<li><strong>load_balancer_pool:</strong> add state migration handler with detection for v4 vs v5 format</li>
<li><strong>pages_project:</strong> add state migration handlers</li>
<li><strong>tiered_cache:</strong> add state migration handlers</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> deprecate <code>entries</code> field in favor of <code>enabled_entries</code></li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-11">Feb 11, 2026</time><div>
<h2 id="post-2026-02-11-appliance-post-quantum-encryption"><a href="/changelog/post/2026-02-11-appliance-post-quantum-encryption/">Post-quantum encryption support for Cloudflare One Appliance</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Cloudflare One Appliance version 2026.2.0 adds <a href="/ssl/post-quantum-cryptography/">post-quantum encryption</a> support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.</p>
<p>This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-11">Feb 11, 2026</time><div>
<h2 id="post-2026-02-11-subrequests-limit"><a href="/changelog/post/2026-02-11-subrequests-limit/">Workers are no longer limited to 1000 subrequests</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers no longer have a limit of 1000 subrequests per invocation, allowing you to make more <code>fetch()</code> calls or requests
to Cloudflare services on every incoming request. This is especially important for long-running Workers requests, such as
open websockets on <a href="/durable-objects">Durable Objects</a> or long-running <a href="/workflows">Workflows</a>, as these could often exceed this limit and error.</p>
<p>By default, Workers on paid plans are now limited to 10,000 subrequests per invocation, but this
limit can be increased up to 10 million by setting the new <code>subrequests</code> limit in your Wrangler configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17797.md")</div>
<p>Workers on the free plan remain limited to 50 external subrequests and 1000 subrequests to Cloudflare services per invocation.</p>
<p>To protect against runaway code or unexpected costs, you can also set a lower limit for both subrequests and CPU usage.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17798.md")</div>
<p>For more information, refer to the <a href="/workers/wrangler/configuration/#limits">Wrangler configuration documentation for limits</a> and <a href="/workers/platform/limits/#subrequests">subrequest limits</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-11">Feb 11, 2026</time><div>
<h2 id="post-2026-02-11-vite-plugin-child-environments"><a href="/changelog/post/2026-02-11-vite-plugin-child-environments/">Improved React Server Components support in the Cloudflare Vite plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The Cloudflare Vite plugin now integrates seamlessly <a href="https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc">@vitejs/plugin-rsc</a>, the official Vite plugin for <a href="https://react.dev/reference/rsc/server-components">React Server Components</a>.</p>
<p>A <code>childEnvironments</code> option has been added to the plugin config to enable using multiple environments within a single Worker.
The parent environment can then import modules from a child environment in order to access a separate module graph.
For a typical RSC use case, the plugin might be configured as in the following example:</p>
<pre tabindex="0"><code class="language-ts">export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			viteEnvironment: {&#10;				name: &quot;rsc&quot;,&#10;				childEnvironments: [&quot;ssr&quot;],&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p><code>@vitejs/plugin-rsc</code> provides the lower level functionality that frameworks, such as <a href="https://reactrouter.com/how-to/react-server-components">React Router</a>, build upon.
The GitHub repository includes a <a href="https://github.com/vitejs/vite-plugin-react/tree/f066114c3e6bf18f5209ff3d3ef6bf1ab46d3866/packages/plugin-rsc/examples/starter-cf-single">basic Cloudflare example</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-10">Feb 10, 2026</time><div>
<h2 id="post-2026-02-10-waf-release"><a href="/changelog/post/2026-02-10-waf-release/">WAF Release - 2026-02-10</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release changes the rule action from BLOCK to Disabled for Anomaly:Header:User-Agent - Fake Google Bot.</p>
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
        <code class="nb-rule-id" title="ce11be543594412bb4bb92516aa0bef8">6aa0bef8</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:User-Agent - Fake Google Bot</td>
<td>Enabled</td>
<td>Disabled</td>
<td>We are changing the action for this rule from BLOCK to Disabled</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-09">Feb 9, 2026</time><div>
<h2 id="post-2026-02-09-agents-sdk-v0.4.0"><a href="/changelog/post/2026-02-09-agents-sdk-v0.4.0/">Agents SDK v0.4.0: Readonly connections, MCP security improvements, x402 v2 migration, and custom MCP OAuth providers</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings readonly connections, MCP protocol and security improvements, x402 payment protocol v2 migration, and the ability to customize OAuth for MCP server connections.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-readonly-connections">Readonly connections</h4>
<p>Agents can now restrict WebSocket clients to read-only access, preventing them from modifying agent state. This is useful for dashboards, spectator views, or any scenario where clients should observe but not mutate.</p>
<p>New hooks: <code>shouldConnectionBeReadonly</code>, <code>setConnectionReadonly</code>, <code>isConnectionReadonly</code>. Readonly connections block both client-side <code>setState()</code> and mutating <code>@callable()</code> methods, and the readonly flag survives hibernation.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17630.md")</div>
<h4 id="2026-02-09-agents-sdk-v0.4.0-custom-mcp-oauth-providers">Custom MCP OAuth providers</h4>
<p>The new <code>createMcpOAuthProvider</code> method on the <code>Agent</code> class allows subclasses to override the default OAuth provider used when connecting to MCP servers. This enables custom authentication strategies such as pre-registered client credentials or mTLS, beyond the built-in dynamic client registration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17631.md")</div>
<h4 id="2026-02-09-agents-sdk-v0.4.0-mcp-sdk-upgrade-to-1-26-0">MCP SDK upgrade to 1.26.0</h4>
<p>Upgraded the MCP SDK to 1.26.0 to prevent cross-client response leakage. Stateless MCP Servers should now create a new <code>McpServer</code> instance per request instead of sharing a single instance. A guard is added in this version of the MCP SDK which will prevent connection to a Server instance that has already been connected to a transport. Developers will need to modify their code if they declare their <code>McpServer</code> instance as a global variable.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-mcp-oauth-callback-url-security-fix">MCP OAuth callback URL security fix</h4>
<p>Added <code>callbackPath</code> option to <code>addMcpServer</code> to prevent instance name leakage in MCP OAuth callback URLs. When <code>sendIdentityOnConnect</code> is <code>false</code>, <code>callbackPath</code> is now required — the default callback URL would expose the instance name, undermining the security intent. Also fixes callback request detection to match via the <code>state</code> parameter instead of a loose <code>/callback</code> URL substring check, enabling custom callback paths.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-deprecate-onstateupdate-in-favor-of-onstatechanged">Deprecate <code>onStateUpdate</code> in favor of <code>onStateChanged</code></h4>
<p><code>onStateChanged</code> is a drop-in rename of <code>onStateUpdate</code> (same signature, same behavior). <code>onStateUpdate</code> still works but emits a one-time console warning per class. <code>validateStateChange</code> rejections now propagate a <code>CF_AGENT_STATE_ERROR</code> message back to the client.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-x402-v2-migration">x402 v2 migration</h4>
<p>Migrated the x402 MCP payment integration from the legacy <code>x402</code> package to <code>@x402/core</code> and <code>@x402/evm</code> v2.</p>
<p><strong>Breaking changes for x402 users:</strong></p>
<ul>
<li>Peer dependencies changed: replace <code>x402</code> with <code>@x402/core</code> and <code>@x402/evm</code></li>
<li><code>PaymentRequirements</code> type now uses v2 fields (e.g. <code>amount</code> instead of <code>maxAmountRequired</code>)</li>
<li><code>X402ClientConfig.account</code> type changed from <code>viem.Account</code> to <code>ClientEvmSigner</code> (structurally compatible with <code>privateKeyToAccount()</code>)</li>
</ul>
<pre tabindex="0"><code class="language-bash">npm uninstall x402&#10;npm install @x402/core @x402/evm&#10;</code></pre>
<p>Network identifiers now accept both legacy names and CAIP-2 format:</p>
<pre tabindex="0"><code class="language-ts">// Legacy name (auto-converted)&#10;{&#10;	network: &quot;base-sepolia&quot;,&#10;}&#10;&#10;// CAIP-2 format (preferred)&#10;{&#10;	network: &quot;eip155:84532&quot;,&#10;}&#10;</code></pre>
<p><strong>Other x402 changes:</strong></p>
<ul>
<li><code>X402ClientConfig.network</code> is now optional — the client auto-selects from available payment requirements</li>
<li>Server-side lazy initialization: facilitator connection is deferred until the first paid tool invocation</li>
<li>Payment tokens support both v2 (<code>PAYMENT-SIGNATURE</code>) and v1 (<code>X-PAYMENT</code>) HTTP headers</li>
<li>Added <code>normalizeNetwork</code> export for converting legacy network names to CAIP-2 format</li>
<li>Re-exports <code>PaymentRequirements</code>, <code>PaymentRequired</code>, <code>Network</code>, <code>FacilitatorConfig</code>, and <code>ClientEvmSigner</code> from <code>agents/x402</code></li>
</ul>
<h4 id="2026-02-09-agents-sdk-v0.4.0-other-improvements">Other improvements</h4>
<ul>
<li>Fix <code>useAgent</code> and <code>AgentClient</code> crashing when using <code>basePath</code> routing</li>
<li>CORS handling delegated to partyserver's native support (simpler, more reliable)</li>
<li>Client-side <code>onStateUpdateError</code> callback for handling rejected state updates</li>
</ul>
<h4 id="2026-02-09-agents-sdk-v0.4.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-09">Feb 9, 2026</time><div>
<h2 id="post-2026-02-09-pty-terminal-support"><a href="/changelog/post/2026-02-09-pty-terminal-support/">Interactive browser terminals in Sandboxes</a></h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p>The <a href="https://github.com/cloudflare/sandbox-sdk">Sandbox SDK</a> now supports PTY (pseudo-terminal) passthrough, enabling browser-based terminal UIs to connect to sandbox shells via WebSocket.</p>
<h4 id="2026-02-09-pty-terminal-support-sandbox-terminal-request"><code>sandbox.terminal(request)</code></h4>
<p>The new <code>terminal()</code> method proxies a WebSocket upgrade to the container's PTY endpoint, with output buffering for replay on reconnect.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17632.md")</div>
<h4 id="2026-02-09-pty-terminal-support-multiple-terminals-per-sandbox">Multiple terminals per sandbox</h4>
<p>Each session can have its own terminal with an isolated working directory and environment, so users can run separate shells side-by-side in the same container.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17633.md")</div>
<h4 id="2026-02-09-pty-terminal-support-xterm-js-addon">xterm.js addon</h4>
<p>The new <code>@cloudflare/sandbox/xterm</code> export provides a <code>SandboxAddon</code> for <a href="https://xtermjs.org/">xterm.js</a> with automatic reconnection (exponential backoff + jitter), buffered output replay, and resize forwarding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17634.md")</div>
<h4 id="2026-02-09-pty-terminal-support-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-09">Feb 9, 2026</time><div>
<h2 id="post-2026-02-09-analytics-enhancements"><a href="/changelog/post/2026-02-09-analytics-enhancements/">Analytics enhancements</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control metrics have been enhanced with new views, improved filtering, and better data visualization.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-path-patterns.png" alt="AI Crawl Control path patterns" /></p>
<p><strong>Path pattern grouping</strong></p>
<ul>
<li>In the <strong>Metrics</strong> tab &gt; <strong>Most popular paths</strong> table, use the new <strong>Patterns</strong> tab that groups requests by URI pattern (<code>/blog/*</code>, <code>/api/v1/*</code>, <code>/docs/*</code>) to identify which site areas crawlers target most. Refer to the screenshot above.</li>
</ul>
<p><strong>Enhanced referral analytics</strong></p>
<ul>
<li>Destination patterns show which site areas receive AI-driven referral traffic.</li>
<li>In the <strong>Metrics</strong> tab, a new <strong>Referrals over time</strong> chart shows trends by operator or source.</li>
</ul>
<p><strong>Data transfer metrics</strong></p>
<ul>
<li>In the <strong>Metrics</strong> tab &gt; <strong>Allowed requests over time</strong> chart, toggle <strong>Bytes</strong> to show bandwidth consumption.</li>
<li>In the <strong>Crawlers</strong> tab, a new <strong>Bytes Transferred</strong> column shows bandwidth per crawler.</li>
</ul>
<p><strong>Image exports</strong></p>
<ul>
<li>Export charts and tables as images for reports and presentations.</li>
</ul>
<p>Learn more about <a href="/ai-crawl-control/features/analyze-ai-traffic/">analyzing AI traffic</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-09">Feb 9, 2026</time><div>
<h2 id="post-2026-02-09-indexing-improvements"><a href="/changelog/post/2026-02-09-indexing-improvements/">AI Search now with more granular controls over indexing</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>Get your content updates into <a href="/ai-search/">AI Search</a> faster and avoid a full rescan when you do not need it.</p>
<h4 id="2026-02-09-indexing-improvements-reindex-individual-files-without-a-full-sync">Reindex individual files without a full sync</h4>
<p>Updated a file or need to retry one that errored? When you know exactly which file changed, you can now <a href="/ai-search/configuration/indexing/syncing/#controls">reindex it directly</a> instead of rescanning your entire data source.</p>
<p>Go to <strong>Overview</strong> &gt; <strong>Indexed Items</strong> and select the sync icon next to any file to reindex it immediately.</p>
<p><img src="/assets/upstream/images/ai-search/individual-file-indexing.png" alt="Sync individual files from Indexed Items" /></p>
<h4 id="2026-02-09-indexing-improvements-crawl-only-the-sitemap-you-need">Crawl only the sitemap you need</h4>
<p>By default, AI Search crawls all sitemaps listed in your <code>robots.txt</code>, up to the <a href="/ai-search/platform/limits-pricing/#limits">maximum files per index limit</a>. If your site has multiple sitemaps but you only want to index a specific set, you can now <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">specify a single sitemap URL</a> to limit what the crawler visits.</p>
<p>For example, if your <code>robots.txt</code> lists both <code>blog-sitemap.xml</code> and <code>docs-sitemap.xml</code>, you can specify just <code>https://example.com/docs-sitemap.xml</code> to index only your documentation.</p>
<p>Configure your selection anytime in <strong>Settings</strong> &gt; <strong>Parsing options</strong> &gt; <strong>Specific sitemaps</strong>, then trigger a sync to apply the changes.</p>
<p><img src="/assets/upstream/images/ai-search/specify-sitemap.png" alt="Specify a sitemap in Parsinh options" /></p>
<p>Learn more about <a href="/ai-search/configuration/indexing/syncing/#controls">indexing controls</a> and <a href="/ai-search/configuration/data-source/website/parse-types/#specific-sitemap">website crawling configuration</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-09">Feb 9, 2026</time><div>
<h2 id="post-2026-02-09-tabs-and-pivots"><a href="/changelog/post/2026-02-09-tabs-and-pivots/">Tabs and pivots</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Log Explorer now supports multiple concurrent queries with the new Tabs feature. Work with multiple queries simultaneously and pivot between datasets to investigate malicious activity more effectively.</p>
<h4 id="2026-02-09-tabs-and-pivots-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Multiple tabs:</strong> Open and switch between multiple query tabs to compare results across different datasets.</li>
<li><strong>Quick filtering:</strong> Select the filter button from query results to add a value as a filter to your current query.</li>
<li><strong>Pivot to new tab:</strong> Use Cmd + click on the filter button to start a new query tab with that filter applied.</li>
<li><strong>Preserved progress:</strong> Your query progress is preserved on each tab if you navigate away and return.</li>
</ul>
<p>For more information, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-09">Feb 9, 2026</time><div>
<h2 id="post-2026-02-09-approximate-aggregation-functions"><a href="/changelog/post/2026-02-09-approximate-aggregation-functions/">R2 SQL now supports approximate aggregation functions</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>R2 SQL now supports five approximate aggregation functions for fast analysis of large datasets. These functions trade minor precision for improved performance on high-cardinality data.</p>
<h4 id="2026-02-09-approximate-aggregation-functions-new-functions">New functions</h4>
<ul>
<li><code>APPROX_PERCENTILE_CONT(column, percentile)</code> — Returns the approximate value at a given percentile (0.0 to 1.0). Works on integer and decimal columns.</li>
<li><code>APPROX_PERCENTILE_CONT_WITH_WEIGHT(column, weight, percentile)</code> — Weighted percentile calculation where each row contributes proportionally to its weight column value.</li>
<li><code>APPROX_MEDIAN(column)</code> — Returns the approximate median. Equivalent to <code>APPROX_PERCENTILE_CONT(column, 0.5)</code>.</li>
<li><code>APPROX_DISTINCT(column)</code> — Returns the approximate number of distinct values. Works on any column type.</li>
<li><code>APPROX_TOP_K(column, k)</code> — Returns the <code>k</code> most frequent values with their counts as a JSON array.</li>
</ul>
<p>All functions support <code>WHERE</code> filters. All except <code>APPROX_TOP_K</code> support <code>GROUP BY</code>.</p>
<h4 id="2026-02-09-approximate-aggregation-functions-examples">Examples</h4>
<pre tabindex="0"><code class="language-sql">&#45;- Percentile analysis on revenue data&#10;SELECT approx_percentile_cont(total_amount, 0.25),&#10;       approx_percentile_cont(total_amount, 0.5),&#10;       approx_percentile_cont(total_amount, 0.75)&#10;FROM my_namespace.sales_data&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Median per department&#10;SELECT department, approx_median(total_amount)&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Approximate distinct customers by region&#10;SELECT region, approx_distinct(customer_id)&#10;FROM my_namespace.sales_data&#10;GROUP BY region&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Top 5 most frequent departments&#10;SELECT approx_top_k(department, 5)&#10;FROM my_namespace.sales_data&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Combine approximate and standard aggregations&#10;SELECT COUNT(*),&#10;       AVG(total_amount),&#10;       approx_percentile_cont(total_amount, 0.5),&#10;       approx_distinct(customer_id)&#10;FROM my_namespace.sales_data&#10;WHERE region = &#x27;North&#x27;&#10;</code></pre>
<p>For the full syntax and additional examples, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-06">Feb 6, 2026</time><div>
<h2 id="post-2026-02-06-observability-ui-refresh"><a href="/changelog/post/2026-02-06-observability-ui-refresh/">Visualize data, share links, and create exports with the new Workers Observability dashboard</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> has some major updates to make it easier to debug your application's issues and share findings with your team.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-01-22-events_share_obs_wobs.png" alt="Workers Observability dashboard showing events view with event details and share options" /></p>
<p>You can now:</p>
<ul>
<li><strong>Create visualizations</strong> — Build charts from your Worker data directly in a Worker's Observability tab</li>
<li><strong>Export data as JSON or CSV</strong> — Download logs and traces for offline analysis or to share with teammates</li>
<li><strong>Share events and traces</strong> — Generate direct URLs to specific events, invocations, and traces that open standalone pages with full context</li>
<li><strong>Customize table columns</strong> — Improved field picker to add, remove, and reorder columns in the events table</li>
<li><strong>Expandable event details</strong> — Expand events inline to view full details without leaving the table</li>
<li><strong>Keyboard shortcuts</strong> — Navigate the dashboard with hotkey support</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-01-22-vis_qb_wobs.png" alt="Workers Observability dashboard showing a P99 CPU time visualization grouped by outcome" /></p>
<p>These updates are now live in the Cloudflare dashboard, both in a Worker's Observability tab and in the account-level Observability dashboard for a unified experience. To get started, go to <strong>Workers &amp; Pages</strong> &gt; select your Worker &gt; <strong>Observability</strong>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-04">Feb 4, 2026</time><div>
<h2 id="post-2026-02-09-reference-documentation"><a href="/changelog/post/2026-02-09-reference-documentation/">New reference documentation</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>New reference documentation is now available for AI Crawl Control:</p>
<ul>
<li><strong><a href="/ai-crawl-control/reference/graphql-api/">GraphQL API reference</a></strong> — Query examples for crawler requests, top paths, referral traffic, and data transfer. Includes key filters for detection IDs, user agents, and referrer domains.</li>
<li><strong><a href="/ai-crawl-control/reference/bots/">Bot reference</a></strong> — Detection IDs and user agents for major AI crawlers from OpenAI, Anthropic, Google, Meta, and others.</li>
<li><strong><a href="/ai-crawl-control/reference/worker-templates/">Worker templates</a></strong> — Deploy the x402 Payment-Gated Proxy to monetize crawler access or charge bots while letting humans through free.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-04">Feb 4, 2026</time><div>
<h2 id="post-2026-02-04-queues-free-plan"><a href="/changelog/post/2026-02-04-queues-free-plan/">Cloudflare Queues now available on Workers Free plan</a></h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p><a href="/queues">Cloudflare Queues</a> is now part of the Workers free plan, offering guaranteed message delivery across up to <strong>10,000 queues</strong> to either <a href="/workers">Cloudflare Workers</a> or <a href="/queues/configuration/pull-consumers">HTTP pull consumers</a>. Every Cloudflare account now includes <strong>10,000 operations per day</strong> across reads, writes, and deletes. For more details on how each operation is defined, refer to <a href="https://developers.cloudflare.com/workers/platform/pricing/#queues">Queues pricing</a>.</p>
<p>All features of the existing Queues functionality are available on the free plan, including unlimited <a href="/queues/event-subscriptions/">event subscriptions</a>. Note that the maximum retention period on the free tier, however, is 24 hours rather than 14 days.</p>
<p>If you are new to Cloudflare Queues, follow <a href="https://developers.cloudflare.com/queues/get-started/">this guide</a> or try one of our <a href="/queues/tutorials/">tutorials</a> to get started.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-04">Feb 4, 2026</time><div>
<h2 id="post-2026-02-03-workflows-visualizer"><a href="/changelog/post/2026-02-03-workflows-visualizer/">Visualize your Workflows in the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>Cloudflare Workflows now automatically generates visual diagrams from your code</p>
<p>Your Workflow is parsed to provide a visual map of the Workflow structure, allowing you to:</p>
<ul>
<li>Understand how steps connect and execute</li>
<li>Visualize loops and nested logic</li>
<li>Follow branching paths for conditional logic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workflows/2026-02-03-workflows-diagram.png" alt="Example diagram" /></p>
<p>You can collapse loops and nested logic to see the high-level flow, or expand them to see every step.</p>
<p>Workflow diagrams are available in beta for all JavaScript and TypeScript Workflows. Find your Workflows in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a> to see their diagrams.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-03">Feb 3, 2026</time><div>
<h2 id="post-2026-02-03-agents-workflows-integration"><a href="/changelog/post/2026-02-03-agents-workflows-integration/">Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()</a></h2>
<div class="changelog-badges"><span>agents</span><span>workflows</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings first-class support for <a href="/workflows/">Cloudflare Workflows</a>, synchronous state management, and new scheduling capabilities.</p>
<h4 id="2026-02-03-agents-workflows-integration-cloudflare-workflows-integration">Cloudflare Workflows integration</h4>
<p>Agents excel at real-time communication and state management. Workflows excel at durable execution. Together, they enable powerful patterns where Agents handle WebSocket connections while Workflows handle long-running tasks, retries, and human-in-the-loop flows.</p>
<p>Use the new <code>AgentWorkflow</code> class to define workflows with typed access to your Agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17624.md")</div>
<p>Start workflows from your Agent with <code>runWorkflow()</code> and handle lifecycle events:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17625.md")</div>
<p>Key workflow methods on your Agent:</p>
<ul>
<li><code>runWorkflow(workflowName, params, options?)</code> — Start a workflow with optional metadata</li>
<li><code>getWorkflow(workflowId)</code> / <code>getWorkflows(criteria?)</code> — Query workflows with cursor-based pagination</li>
<li><code>approveWorkflow(workflowId)</code> / <code>rejectWorkflow(workflowId)</code> — Human-in-the-loop approval flows</li>
<li><code>pauseWorkflow()</code>, <code>resumeWorkflow()</code>, <code>terminateWorkflow()</code> — Workflow control</li>
</ul>
<h4 id="2026-02-03-agents-workflows-integration-synchronous-setstate">Synchronous setState()</h4>
<p>State updates are now synchronous with a new <code>validateStateChange()</code> validation hook:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17626.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-scheduleevery-for-recurring-tasks">scheduleEvery() for recurring tasks</h4>
<p>The new <code>scheduleEvery()</code> method enables fixed-interval recurring tasks with built-in overlap prevention:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17627.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-callable-system-improvements">Callable system improvements</h4>
<ul>
<li><strong>Client-side RPC timeout</strong> — Set timeouts on callable method invocations</li>
<li><strong><code>StreamingResponse.error(message)</code></strong> — Graceful stream error signaling</li>
<li><strong><code>getCallableMethods()</code></strong> — Introspection API for discovering callable methods</li>
<li><strong>Connection close handling</strong> — Pending calls are automatically rejected on disconnect</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17628.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-email-and-routing-enhancements">Email and routing enhancements</h4>
<p><strong>Secure email reply routing</strong> — Email replies are now secured with HMAC-SHA256 signed headers, preventing unauthorized routing of emails to agent instances.</p>
<p><strong>Routing improvements:</strong></p>
<ul>
<li><code>basePath</code> option to bypass default URL construction for custom routing</li>
<li>Server-sent identity — Agents send <code>name</code> and <code>agent</code> type on connect</li>
<li>New <code>onIdentity</code> and <code>onIdentityChange</code> callbacks on the client</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17629.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest&#10;</code></pre>
<p>For the complete Workflows API reference and patterns, see <a href="/agents/runtime/execution/run-workflows/">Run Workflows</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-03">Feb 3, 2026</time><div>
<h2 id="post-2026-02-03-r2-local-uploads"><a href="/changelog/post/2026-02-03-r2-local-uploads/">Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p><a href="/r2/buckets/local-uploads/">Local Uploads</a> is now available in open beta. Enable it on your <a href="/r2/">R2</a> bucket to improve upload performance when clients upload data from a different region than your bucket. With Local Uploads enabled, object data is written to storage infrastructure near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains strongly consistent throughout. Refer to <a href="/r2/how-r2-works/">How R2 works</a> for details on how data is written to your bucket.</p>
<p>In our tests, we observed <strong>up to 75% reduction in Time to Last Byte (TTLB)</strong> for upload requests when Local Uploads is enabled.</p>
<p><img src="/assets/upstream/images/r2/local-uploads-latency.png" alt="Local Uploads latency comparison showing p50 TTLB dropping from around 2 seconds to 500ms after enabling Local Uploads" /></p>
<p>This feature is ideal when:</p>
<ul>
<li>Your users are globally distributed</li>
<li>Upload performance and reliability is critical to your application</li>
<li>You want to optimize write performance without changing your bucket's primary location</li>
</ul>
<p>To enable Local Uploads on your bucket, find <strong>Local Uploads</strong> in your bucket settings in the <a href="https://dash.cloudflare.com/?to=/:account/r2/overview">Cloudflare Dashboard</a>, or run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket local-uploads enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>Enabling Local Uploads on a bucket is seamless: existing uploads will complete as expected and there’s no interruption to traffic. There is no additional cost to enable Local Uploads. Upload requests incur the standard <a href="/r2/pricing/">Class A operation costs</a> same as upload requests made without Local Uploads.</p>
<p>For more information, refer to <a href="/r2/buckets/local-uploads/">Local Uploads</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-03">Feb 3, 2026</time><div>
<h2 id="post-2026-02-03-threat-actor-name-mapping"><a href="/changelog/post/2026-02-03-threat-actor-name-mapping/">Threat actor identification with "also known as" aliases</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>Identifying threat actors can be challenging, because naming conventions often vary across the security industry. To simplify your research, <strong>Cloudflare Threat Events</strong> now include an <strong>Also known as</strong> field, providing a list of common aliases and industry-standard names for the groups we track.</p>
<p>This new field is available in both the Cloudflare dashboard and via the API. In the dashboard, you can view these aliases by expanding the event details side panel (under the <strong>Attacker</strong> field) or by adding it as a column in your configurable table view.</p>
<h4 id="2026-02-03-threat-actor-name-mapping-key-benefits">Key benefits</h4>
<ul>
<li>Easily map Cloudflare-tracked actors to the naming conventions used by other vendors without manual cross-referencing.</li>
<li>Quickly identify if a detected threat actor matches a group your team is already monitoring via other intelligence feeds.</li>
</ul>
<p>For more information on how to access this data, refer to the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/">Threat Events API documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-02-02">Feb 2, 2026</time><div>
<h2 id="post-2026-02-02-improved-accessibility-search-for-monitoring"><a href="/changelog/post/2026-02-02-improved-accessibility-search-for-monitoring/">Improved Accessibility and Search for Monitoring</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>We have updated the Monitoring page to provide a more streamlined and insightful experience for administrators, improving both data visualization and dashboard accessibility.</p>
<ul>
<li><strong>Enhanced Visual Layout</strong>: Optimized contrast and the introduction of stacked bar charts for clearer data visualization and trend analysis.
<img src="/assets/upstream/images/changelog/email-security/monitoring-bar-charts.png" alt="visual-example" /></li>
<li><strong>Improved Accessibility &amp; Usability</strong>:
<ul>
<li><strong>Widget Search</strong>: Added search functionality to multiple widgets, including Policies, Submitters, and Impersonation.</li>
<li><strong>Actionable UI</strong>: All available actions are now accessible via dedicated buttons.</li>
<li><strong>State Indicators</strong>: Improved UI states to clearly communicate loading, empty datasets, and error conditions.
<img src="/assets/upstream/images/changelog/email-security/monitoring-buttons.png" alt="buttons-example" /></li>
</ul>
</li>
<li><strong>Granular Data Breakdowns</strong>: New views for dispositions by month, malicious email details, link actions, and impersonations.
<img src="/assets/upstream/images/changelog/email-security/monitoring-monthly-dispositions.png" alt="monthly-example" /></li>
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
<time datetime="2026-02-02">Feb 2, 2026</time><div>
<h2 id="post-2026-02-02-waf-release"><a href="/changelog/post/2026-02-02-waf-release/">WAF Release - 2026-02-02</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for CVE-2025-64459 and CVE-2025-24893.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2025-64459: Django versions prior to 5.1.14, 5.2.8, and 4.2.26 are vulnerable to SQL injection via crafted dictionaries passed to QuerySet methods and the <code>Q()</code> class.</li>
<li>CVE-2025-24893: XWiki allows unauthenticated remote code execution through crafted requests to the SolrSearch endpoint, affecting the entire installation.</li>
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
        <code class="nb-rule-id" title="7a47683eacce4abd870ab2c630698ff3">30698ff3</code>
</td>
<td>N/A</td>
<td>XWiki - Remote Code Execution - CVE:CVE-2025-24893 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ad5c52f6ca334ef4a844e5e5da8ba7e6">da8ba7e6</code>
</td>
<td>N/A</td>
<td>Django SQLI - CVE:CVE-2025-64459</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8f0d5c98bd24460a9305a1558d667511">8d667511</code>
</td>
<td>N/A</td>
<td>NoSQL, MongoDB - SQLi - Comparison - 2</td>
<td>Block</td>
<td>Block</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-30">Jan 30, 2026</time><div>
<h2 id="post-2026-01-30-kv-reduced-minimum-cachettl"><a href="/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/">Reduced minimum cache TTL for Workers KV to 30 seconds</a></h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>The minimum <code>cacheTtl</code> parameter for Workers KV has been reduced from 60 seconds to 30 seconds. This change applies to both <code>get()</code> and <code>getWithMetadata()</code> methods.</p>
<p>This reduction allows you to maintain more up-to-date cached data and have finer-grained control over cache behavior. Applications requiring faster data refresh rates can now configure cache durations as low as 30 seconds instead of the previous 60-second minimum.</p>
<p>The <code>cacheTtl</code> parameter defines how long a KV result is cached at the global network location it is accessed from:</p>
<pre tabindex="0"><code class="language-js">// Read with custom cache TTL&#10;const value = await env.NAMESPACE.get(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds (previously 60)&#10;});&#10;&#10;// getWithMetadata also supports the reduced cache TTL&#10;const valueWithMetadata = await env.NAMESPACE.getWithMetadata(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds&#10;});&#10;</code></pre>
<p>The default cache TTL remains unchanged at 60 seconds. Upgrade to the latest version of Wrangler to be able to use 30 seconds <code>cacheTtl</code>.</p>
<p>This change affects all KV read operations using the binding API. For more information, consult the <a href="/kv/api/read-key-value-pairs/#cachettl-parameter">Workers KV cache TTL documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-30">Jan 30, 2026</time><div>
<h2 id="post-2026-01-30-bgp-over-tunnels"><a href="/changelog/post/2026-01-30-bgp-over-tunnels/">BGP over GRE and IPsec tunnels</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span><span>magic-transit</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using IPsec and GRE tunnel on-ramps (beta).</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via IPsec and GRE tunnel on-ramps.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>For configuration details, refer to:</p>
<ul>
<li><a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Configure BGP routes for Magic WAN</a></li>
<li><a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Configure BGP routes for Magic Transit</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-28">Jan 28, 2026</time><div>
<h2 id="post-2026-01-28-flux-2-klein-9b-workers-ai"><a href="/changelog/post/2026-01-28-flux-2-klein-9b-workers-ai/">Launching FLUX.2 [klein] 9B on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We have partnered with Black Forest Labs (BFL) again to bring their optimized FLUX.2 [klein] 9B model to Workers AI. This distilled model offers enhanced quality compared to the 4B variant, while maintaining cost-effective pricing. With a fixed 4-step inference process, Klein 9B is ideal for rapid prototyping and real-time applications where both speed and quality matter.</p>
<p>Read the <a href="https://bfl.ai/blog">BFL blog</a> to learn more about the model itself, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-klein-9b/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-01-28-flux-2-klein-9b-workers-ai-workers-ai-platform-specifics">Workers AI platform specifics</h4>
<p>The model hosted on Workers AI is optimized for speed with a <strong>fixed 4-step inference process</strong> and supports up to 4 image inputs. Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted. Like FLUX.2 [dev] and FLUX.2 [klein] 4B, this image model uses multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre tabindex="0"><code class="language-javascript">const form = new FormData();&#10;form.append(&quot;prompt&quot;, &quot;a sunset with a dog&quot;);&#10;form.append(&quot;width&quot;, &quot;1024&quot;);&#10;form.append(&quot;height&quot;, &quot;1024&quot;);&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-9b&quot;, {&#10;	multipart: {&#10;		body: formStream,&#10;		contentType: formContentType,&#10;	},&#10;});&#10;</code></pre>
<p>The parameters you can send to the model are detailed here:</p>
<details>
  <summary>JSON Schema for Model</summary>
**Required Parameters**
<ul>
<li><code>prompt</code> (string) - Text description of the image to generate</li>
</ul>
<p><strong>Optional Parameters</strong></p>
<ul>
<li><code>input_image_0</code> (string) - Binary image</li>
<li><code>input_image_1</code> (string) - Binary image</li>
<li><code>input_image_2</code> (string) - Binary image</li>
<li><code>input_image_3</code> (string) - Binary image</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
<p><strong>Note:</strong> Since this is a distilled model, the <code>steps</code> parameter is fixed at 4 and cannot be adjusted.</p>
</details>
<h4 id="2026-01-28-flux-2-klein-9b-workers-ai-multi-reference-images">Multi-reference images</h4>
<p>The FLUX.2 klein-9b model supports generating images based on reference images, just like FLUX.2 [dev] and FLUX.2 [klein] 4B. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generated images. You would use it with the same multipart form data structure, with the input images in binary. The model supports up to 4 input images.</p>
<p>For the prompt, you can reference the images based on the index, like <code>take the subject of image 1 and style it like image 0</code> or even use natural language like <code>place the dog beside the woman</code>.</p>
<p>You must name the input parameter as <code>input_image_0</code>, <code>input_image_1</code>, <code>input_image_2</code>, <code>input_image_3</code> for it to work correctly. All input images must be smaller than 512x512.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-klein-9b&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=take the subject of image 1 and style it like image 0&#x27; \&#10;  &#45;-form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png \&#10;  &#45;-form input_image_1=@/Users/johndoe/Desktop/me.png \&#10;  &#45;-form width=1024 \&#10;  &#45;-form height=1024&#10;</code></pre>
<p>Through Workers AI Binding:</p>
<pre tabindex="0"><code class="language-javascript">//helper function to convert ReadableStream to Blob&#10;async function streamToBlob(stream: ReadableStream, contentType: string): Promise&lt;Blob&gt; {&#10;  const reader = stream.getReader();&#10;  const chunks = [];&#10;&#10;  while (true) {&#10;    const { done, value } = await reader.read();&#10;    if (done) break;&#10;    chunks.push(value);&#10;  }&#10;&#10;  return new Blob(chunks, { type: contentType });&#10;}&#10;&#10;const image0 = await fetch(&quot;http://image-url&quot;);&#10;const image1 = await fetch(&quot;http://image-url&quot;);&#10;const form = new FormData();&#10;&#10;const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);&#10;const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);&#10;form.append(&#x27;input_image_0&#x27;, image_blob0)&#10;form.append(&#x27;input_image_1&#x27;, image_blob1)&#10;form.append(&#x27;prompt&#x27;, &#x27;take the subject of image 1 and style it like image 0&#x27;)&#10;&#10;// FormData doesn&#x27;t expose its serialized body or boundary. Passing it to a&#10;// Request (or Response) constructor serializes it and generates the Content-Type&#10;// header with the boundary, which is required for the server to parse the multipart fields.&#10;const formResponse = new Response(form);&#10;const formStream = formResponse.body;&#10;const formContentType = formResponse.headers.get(&#x27;content-type&#x27;);&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-klein-9b&quot;, {&#10;    multipart: {&#10;        body: formStream,&#10;        contentType: formContentType&#10;    }&#10;})&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-28">Jan 28, 2026</time><div>
<h2 id="post-2026-01-27-warp-macos-beta"><a href="/changelog/post/2026-01-27-warp-macos-beta/">WARP client for macOS (version 2026.1.89.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-01-28">Jan 28, 2026</time><div>
<h2 id="post-2026-01-27-warp-windows-beta"><a href="/changelog/post/2026-01-27-warp-windows-beta/">WARP client for Windows (version 2026.1.89.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improvements to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multi-user mode</a>. Fixed an issue where when switching from a pre-login registration to a user registration, Mobile Device Management (MDM) configuration association could be lost.</li>
<li>Added a new feature to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#netbios-over-tcpip">manage NetBIOS over TCP/IP</a> functionality on the Windows client. NetBIOS over TCP/IP on the Windows client is now disabled by default and can be enabled in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile settings</a>.</li>
<li>Fixed an issue causing failure of the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion">local network exclusion</a> feature when configured with a timeout of <code>0</code>.</li>
<li>Improvement for the Windows <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/client-certificate/">client certificate posture check</a> to ensure logged results are from checks that run once users log in.</li>
<li>Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.</li>
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
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/25/">Previous</a><span>Page 26 of 50</span><a class="pagination-next" rel="next" href="/changelog/27/">Next</a></nav>
</div>
