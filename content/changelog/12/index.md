---
cp9:
  canonical: https://developers.cloudflare.com/changelog/12/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 12 | Cloudflare Docs
  head_html: <title>Changelog - page 12 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/12/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 12"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/12/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/12/#page","headline":"Changelog - page 12 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/12/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/12/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-06-16">Jun 16, 2026</time><div>
<h2 id="post-2026-06-16-glm-5.2-workers-ai"><a href="/changelog/post/2026-06-16-glm-5.2-workers-ai/">Introducing GLM-5.2 on Workers AI</a></h2>
<div class="changelog-badges"><span>workers</span><span>agents</span><span>workers-ai</span></div><div class="changelog-body"><p>We are excited to announce <strong>GLM-5.2</strong> on Workers AI, Z.ai's flagship agentic coding model.</p>
<p><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a> is a text generation model built for agentic coding workflows. With function calling and reasoning support, it can handle long codebases, multi-step planning, and tool-augmented agents.</p>
<p><strong>Key features and use cases:</strong></p>
<ul>
<li><strong>Agentic coding</strong>: Designed for autonomous coding tasks, long-horizon planning, and complex software engineering workflows</li>
<li><strong>Large context window</strong>: GLM-5.2 supports up to a 1,048,576 token context window. Workers AI is launching the model with a 262,144 token context window and plans to increase this in the future</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns</li>
<li><strong>Reasoning</strong>: Tackles complex problem-solving and step-by-step reasoning tasks</li>
</ul>
<p>Use GLM-5.2 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-5.2/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-16">Jun 16, 2026</time><div>
<h2 id="post-2026-06-16-tcp-connect-vpc-networks"><a href="/changelog/post/2026-06-16-tcp-connect-vpc-networks/">TCP connections via connect() over VPC Networks</a></h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p><a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings now support the <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> Socket API for raw TCP connections to private destinations, in addition to HTTP traffic via <code>fetch()</code>.</p>
<p>This means Workers can now open TCP sockets to any private service reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp — Redis, Memcached, MQTT, custom binary protocols, or any other TCP-based service.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17828.md")</div>
<p>At runtime, use <code>connect()</code> on the binding to open a TCP socket to a private destination:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request: Request, env: Env) {&#10;		// Open a TCP connection to a private Redis instance&#10;		const socket = await env.PRIVATE_NETWORK.connect(&quot;10.0.1.50:6379&quot;);&#10;&#10;		// Write a Redis PING command&#10;		const writer = socket.writable.getWriter();&#10;		await writer.write(new TextEncoder().encode(&quot;PING\r\n&quot;));&#10;		await writer.close();&#10;&#10;		return new Response(socket.readable);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17827.md")</aside>
<p>For more details, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> and the <a href="/workers-vpc/api/">Workers Binding API</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-15">Jun 15, 2026</time><div>
<h2 id="post-2026-06-15-threat-intelligence-fields"><a href="/changelog/post/2026-06-15-threat-intelligence-fields/">Use Cloudforce One threat intelligence in WAF rules</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>You can now match incoming requests against Cloudforce One threat intelligence in your WAF rules. A new detection looks up the client IP address of each request against the threat intelligence database. If the IP was involved in threat activity in the past seven days, Cloudflare populates <code>cf.intel.ip.*</code> fields that you can use in <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a>.</p>
<p>The detection populates the following fields. Use the <a href="/ruleset-engine/rules-language/functions/#any"><code>any()</code></a> function with the <code>[*]</code> wildcard to match array values:</p>
<ul>
<li><code>cf.intel.ip.datasets</code> — the dataset that flagged the IP address (<code>ddos</code> or <code>waf</code>).</li>
<li><code>cf.intel.ip.target_industries</code> — industries the IP address has targeted.</li>
<li><code>cf.intel.ip.attacker_names</code> — known threat actors associated with the IP address.</li>
<li><code>cf.intel.ip.attacker_countries</code> — source countries of the threat activity.</li>
<li><code>cf.intel.ip.target_countries</code> — countries the IP address has targeted.</li>
</ul>
<p>For example, the following custom rule expression blocks requests from IP addresses associated with DDoS activity that have targeted France:</p>
<pre tabindex="0"><code class="language-txt">any(cf.intel.ip.target_countries[*] == &quot;FR&quot;) and any(cf.intel.ip.datasets[*] == &quot;ddos&quot;)&#10;</code></pre>
<p>These fields work with the Cloudflare API and Terraform. Matches are logged in <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</p>
<p>The threat intelligence detection is available to customers with an active <a href="/security-center/cloudforce-one/">Cloudforce One</a> subscription. For more information, refer to <a href="/waf/detections/threat-intelligence/">Threat intelligence</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-15">Jun 15, 2026</time><div>
<h2 id="post-2026-06-15-waf-release"><a href="/changelog/post/2026-06-15-waf-release/">WAF Release - 2026-06-15</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces new managed protection to address a critical SQL injection vulnerability in Ghost CMS (CVE-2026-26980) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic. These rules protect affected installations from unauthorized data exfiltration at the network edge.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-26980: A blind SQL injection vulnerability in the Ghost CMS Content API (versions 3.24.0 to 6.19.0) allows unauthenticated remote attackers to inject malicious SQL commands via query parameters due to improper input validation.</li>
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
				<code class="nb-rule-id" title="439c4ef64b32447989bdf412b4c29bc6">b4c29bc6</code>
</td>
<td>N/A</td>
<td>Ghost CMS - SQLi - CVE:CVE-2026-26980</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6c64b68ef5ed45e7a622cdaab56f403f">b56f403f</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>		
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-12">Jun 12, 2026</time><div>
<h2 id="post-2026-06-12-user-agent-logging"><a href="/changelog/post/2026-06-12-user-agent-logging/">View the user agent of requests in AI Gateway logs</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway logs now capture the user agent of the client that made each request, making it easier to identify which SDK, library, or application sent the traffic flowing through your gateway. For example, you can tell apart requests coming from <code>openai-python</code> versus a custom application or a Cloudflare Worker.</p>
<p>The user agent appears alongside the other details in each log entry, and you can filter logs by user agent (equals, does not equal, or contains) in the dashboard.</p>
<p>For more information, refer to <a href="/ai-gateway/observability/logging/">Logging</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-12">Jun 12, 2026</time><div>
<h2 id="post-2026-06-12-durable-objects-metrics-filter-by-id-name"><a href="/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/">Filter Durable Objects metrics by object ID or name</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>You can now filter the <strong>Metrics</strong> tab for a Durable Objects namespace by an individual Durable Object's <a href="/durable-objects/api/id/">ID</a> or <a href="/durable-objects/api/id/#name">name</a> in the Cloudflare dashboard. Previously, metrics charts only showed aggregate, namespace-level data, making it difficult to isolate the behavior of a specific object.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-metrics-dashboard.png" alt="The Durable Objects Metrics tab filtered to a single object by ID, showing per-object requests and errors by invocation status." /></p>
<p>Start typing an ID or name into the filter and select a match from the autocomplete dropdown. The autocomplete only shows objects with invocations during the selected time range, so an object that does not appear has not been invoked in that window. This does not necessarily mean the object has been deleted. Every chart on the page updates to reflect only the selected object. This makes it easier to identify and investigate a single Durable Object when debugging a high-traffic object, an error spike, or unexpected storage usage. Clear the filter to return to namespace-level metrics.</p>
<p>Metrics are powered by the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, so standard analytics behavior such as ingestion delay and <a href="/analytics/faq/graphql-api-inconsistent-results/">sampling</a> applies.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/">Metrics and analytics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-12">Jun 12, 2026</time><div>
<h2 id="post-2026-06-12-terraform-v5.20.0-provider"><a href="/changelog/post/2026-06-12-terraform-v5.20.0-provider/">Terraform v5.20.0 now available</a></h2>
<div class="changelog-badges"><span>terraform</span></div><div class="changelog-body"><p>Cloudflare's Terraform v5 Provider makes it easy for developers to manage their Cloudflare infrastructure using a configuration as code approach. It releases every <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 weeks</a> to ensure that you can always manage the latest features in the platform. This week, we launched Terraform v5.20.0, which adds 24 new resources, bumps the underlying Go SDK to cloudflare-go v7, and includes a range of bug fixes and state upgraders based on community feedback.</p>
<h4 id="2026-06-12-terraform-v5.20.0-provider-new-resources">New resources</h4>
<ul>
<li><strong>cloudflare_ai_search_namespace:</strong> Manage AI Search namespaces</li>
<li><strong>cloudflare_custom_csr:</strong> Manage custom certificate signing requests</li>
<li><strong>cloudflare_dls_prefix_binding:</strong> Manage DLS regional service prefix bindings</li>
<li><strong>cloudflare_flagship_app:</strong> Manage Flagship feature flag apps</li>
<li><strong>cloudflare_flagship_flag:</strong> Manage Flagship feature flags</li>
<li><strong>cloudflare_google_tag_gateway:</strong> Manage Google Tag Gateway</li>
<li><strong>cloudflare_load_balancer_monitor_group:</strong> Manage load balancer monitor groups</li>
<li><strong>cloudflare_oauth_client:</strong> Manage IAM OAuth clients</li>
<li><strong>cloudflare_origin_cloud_region:</strong> Manage origin cloud regions (v2 endpoints)</li>
<li><strong>cloudflare_secrets_store:</strong> Manage Secrets Store instances</li>
<li><strong>cloudflare_secrets_store_secret:</strong> Manage Secrets Store secrets</li>
<li><strong>cloudflare_share:</strong> Manage resource shares</li>
<li><strong>cloudflare_share_recipient:</strong> Manage share recipients</li>
<li><strong>cloudflare_share_resource:</strong> Manage shared resources</li>
<li><strong>cloudflare_zero_trust_device_deployment_groups:</strong> Manage Zero Trust device deployment groups</li>
<li><strong>cloudflare_zero_trust_dlp_data_class:</strong> Manage DLP data classes</li>
<li><strong>cloudflare_zero_trust_dlp_data_tag:</strong> Manage DLP data tags</li>
<li><strong>cloudflare_zero_trust_dlp_data_tag_category:</strong> Manage DLP data tag categories</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_group:</strong> Manage DLP sensitivity groups</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_level:</strong> Manage DLP sensitivity levels</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_level_order:</strong> Manage DLP sensitivity level ordering</li>
<li><strong>cloudflare_zero_trust_resource_library_application:</strong> Manage Zero Trust resource library applications</li>
<li><strong>cloudflare_zero_trust_resource_library_category:</strong> Manage Zero Trust resource library categories</li>
<li><strong>cloudflare_zero_trust_tunnel_warp_connector_config:</strong> Manage WARP connector tunnel configurations</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-features">Features</h4>
<ul>
<li><strong>cache:</strong> add create (POST) method for smart_tiered_cache</li>
<li><strong>cache:</strong> update OPCR config to v2 endpoints</li>
<li><strong>dlp:</strong> promote classification Stainless config to main</li>
<li><strong>dlp:</strong> add custom prompt topics endpoint</li>
<li><strong>email_security_block_sender:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>email_security_impersonation_registry:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>email_security_trusted_domains:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>snippets:</strong> add Terraform <code>id_property</code> annotations for snippet and snippet_rules</li>
<li>bump Go SDK to cloudflare-go v7</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>account_member:</strong> missing upgrade path from v5.0–v5.15</li>
<li><strong>authenticated_origin_pulls_settings:</strong> nil pointer panic</li>
<li><strong>bot_management:</strong> restore <code>content_bots_protection</code> handling in model.go</li>
<li><strong>dns_record:</strong> prevent FQDN normalization from swallowing name shortening changes</li>
<li><strong>list:</strong> nullify empty nested objects to prevent inconsistent result after apply</li>
<li><strong>load_balancer_pool:</strong> accept early-v5 object-shape state at schema_version=0</li>
<li><strong>load_balancer_pool:</strong> add <code>UseStateForUnknown</code> for <code>load_shedding</code> attribute to prevent drift</li>
<li><strong>r2_custom_domain:</strong> restore degraded-response handling in resource.go</li>
<li><strong>regional_hostname:</strong> update cloudflare-go imports from v6 to v7</li>
<li><strong>secrets_store:</strong> fix model/schema parity and guard acceptance tests</li>
<li><strong>spectrum_application:</strong> accept early-v5 object-shape state at schema_version=0</li>
<li><strong>worker:</strong> preserve <code>observability.traces.propagation_policy</code> across reads</li>
<li><strong>worker:</strong> add <code>propagation_policy</code> to observability defaults</li>
<li><strong>worker_version:</strong> restore handwritten D1 <code>database_id</code> handling</li>
<li><strong>workers_custom_domain:</strong> missing <code>CertId</code> field in state migration</li>
<li><strong>workers_script:</strong> restore annotations Read workaround stripped by codegen</li>
<li><strong>zero_trust_access_identity_provider:</strong> change <code>read_only</code> from computed to optional</li>
<li><strong>zero_trust_access_identity_provider:</strong> add <code>UseStateForUnknown</code> to SAML-only config fields</li>
<li><strong>zero_trust_access_identity_provider:</strong> use <code>UseNonNullStateForUnknown</code> on scim_config fields</li>
<li><strong>zero_trust_access_policy:</strong> populate <code>account_id</code> when migrating zone-scoped v4 state</li>
<li><strong>zero_trust_access_policy:</strong> missing <code>common_names</code> transform in migration</li>
<li>gracefully handle nil pointer dereference when config has <code>attributes_flat</code> during migration</li>
<li>set initial schema version to 500 for all new resources</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-refactors">Refactors</h4>
<p>Extracted <code>MoveState</code> nil guard into shared helper</p>
<h4 id="2026-06-12-terraform-v5.20.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Version 5 Migration Guide](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-12">Jun 12, 2026</time><div>
<h2 id="post-2026-06-12-kimi-k2-7-code-workers-ai"><a href="/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/">Moonshot AI Kimi K2.7 Code now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a> is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.</p>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-improved-coding-and-agent-performance">Improved coding and agent performance</h4>
<p>K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:</p>
<ul>
<li><strong>+21.8%</strong> on Kimi Code Bench v2</li>
<li><strong>+11.0%</strong> on Program Bench</li>
<li><strong>+31.5%</strong> on MLS Bench Lite</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-reasoning-efficiency">Reasoning efficiency</h4>
<p>K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.</p>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with improved instruction following and higher end-to-end coding task success rates</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth via <code>chat_template_kwargs.thinking</code></li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Structured outputs</strong> with JSON schema support</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-differences-from-kimi-k2-6">Differences from Kimi K2.6</h4>
<p>If you are migrating from Kimi K2.6, note the following:</p>
<ul>
<li>K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency</li>
<li>Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)</li>
<li>API usage is identical — no parameter changes required</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.7 Code through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.7-code/">Kimi K2.7 Code model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-11">Jun 11, 2026</time><div>
<h2 id="post-2026-06-11-browser-run-snapshot-formats"><a href="/changelog/post/2026-06-11-browser-run-snapshot-formats/">New formats parameter for the Browser Run /snapshot endpoint</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a>'s <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> endpoint</a> now supports a <code>formats</code> parameter that lets you return multiple page formats in a single API call. Previously, <code>/snapshot</code> returned only HTML content and a screenshot. You can now also include Markdown and the accessibility tree in the same response.</p>
<p>These formats are particularly useful for AI agent workflows:</p>
<ul>
<li>Markdown provides a token-efficient representation of page content that LLMs can process directly, without parsing HTML markup.</li>
<li>The accessibility tree provides a structured representation of a page's elements, including roles, labels, and hierarchy, helping LLMs understand page structure and navigate its contents.</li>
</ul>
<p>The following example returns a screenshot, Markdown, and the accessibility tree in one call:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17699.md")
</div></div>
<p>You must request at least two formats. If you only need one, use the respective single-format endpoint such as <a href="/browser-run/quick-actions/screenshot-endpoint/"><code>/screenshot</code></a> or <a href="/browser-run/quick-actions/markdown-endpoint/"><code>/markdown</code></a>.</p>
<p>Refer to the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> documentation</a> for the full list of accepted values.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-11">Jun 11, 2026</time><div>
<h2 id="post-2026-06-11-custom-ai-prompt-topics"><a href="/changelog/post/2026-06-11-custom-ai-prompt-topics/">Define custom topics for AI prompt protection</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now define custom topics for AI prompt protection. Predefined <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a> cover common content and intent categories such as PII, source code, and jailbreak attempts. Custom topics let you detect unique or proprietary concepts that are not included in predefined categories.</p>
<p>You describe a custom topic in natural language, and Cloudflare DLP detects whether a prompt matches that topic based on context rather than specific keywords. For example, a topic that describes confidential merger discussions matches a prompt that paraphrases the deal, even when the prompt never uses the word merger or names the companies involved. To detect literal values such as internal codenames or product identifiers, use a <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets">custom wordlist or pattern entry</a> instead.</p>
<p>Custom topics run through the same <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">application granular controls</a> path as predefined AI prompt topics. Custom topics are available for ChatGPT, Google Gemini, Perplexity, and Claude.</p>
<h4 id="2026-06-11-custom-ai-prompt-topics-create-a-custom-ai-prompt-topic">Create a custom AI prompt topic</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>Select <strong>AI prompt topics</strong>, then select <strong>Custom Prompt Topic</strong>.</li>
<li>Describe the topic in natural language. Be specific about the concept you want to detect. For example, describe unreleased product roadmap details or confidential customer contract terms.</li>
<li>Add this detection entry to an existing DLP profile, or <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">create a new DLP profile</a>.</li>
<li>Use the profile in a Gateway HTTP policy to log or block prompts that match the topic.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17715.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-11">Jun 11, 2026</time><div>
<h2 id="post-2026-06-11-dynamic-workers-count"><a href="/changelog/post/2026-06-11-dynamic-workers-count/">Track Dynamic Workers usage from the dashboard and GraphQL API</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/changelog/dynamic-workers-count.png" alt="Dynamic Workers usage on the Workers overview page" /></p>
<p>Customers can now view the number of <a href="/dynamic-workers/">Dynamic Workers</a> invoked during their billing period from the Workers overview page in the Cloudflare dashboard.</p>
<p>This count reflects the number of Dynamic Workers that Cloudflare would bill for during the selected billing period. Dynamic Workers usage data only goes back to June 1, 2026.</p>
<p>You can also query this count through the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> by using <code>workersInvocationsByOwnerAndScriptGroups</code> and selecting <code>distinctDynamicWorkerCount</code>:</p>
<pre tabindex="0"><code class="language-graphql">query getDynamicWorkersCount(&#10;	$accountTag: string!&#10;	$filter: AccountWorkersInvocationsByOwnerAndScriptGroupsFilter_InputObject&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			workersInvocationsByOwnerAndScriptGroups(limit: 10000, filter: $filter) {&#10;				uniq {&#10;					distinctDynamicWorkerCount&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use variables to set the account and billing-period date range:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;	&quot;filter&quot;: {&#10;		&quot;date_geq&quot;: &quot;2026-06-01&quot;,&#10;		&quot;date_leq&quot;: &quot;2026-06-30&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/dynamic-workers/pricing/">Dynamic Workers pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-10">Jun 10, 2026</time><div>
<h2 id="post-2026-06-10-ai-search-namespace-wrangler-commands"><a href="/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/">Manage AI Search namespaces with Wrangler CLI</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports namespace-level Wrangler commands, making it easier to manage <a href="/ai-search/concepts/namespaces/">namespaces</a> from your terminal, scripts, and agent workflows.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search namespace list</code></td>
<td>List AI Search namespaces</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace create</code></td>
<td>Create a new AI Search namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace get</code></td>
<td>Get details for a namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace update</code></td>
<td>Update a namespace description</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace delete</code></td>
<td>Delete an AI Search namespace</td>
</tr>
</tbody>
</table>
<p>Create a namespace for a new application or tenant directly from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search namespace create docs-production --description &quot;Production documentation search&quot;&#10;</code></pre>
<p>List namespaces with pagination or filter by name or description:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search namespace list --search docs --page 1 --per-page 10&#10;</code></pre>
<p>Use <code>--json</code> with <code>list</code>, <code>create</code>, <code>get</code>, and <code>update</code> to return structured output that automation and AI agents can parse directly.</p>
<p>Instance-level commands also now support a <code>--namespace</code> flag, so you can interact with instances inside a specific namespace from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search list --namespace docs-production&#10;</code></pre>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-10">Jun 10, 2026</time><div>
<h2 id="post-2026-06-10-account-level-record-quota"><a href="/changelog/post/2026-06-10-account-level-record-quota/">Account-level DNS records quota</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Cloudflare now enforces DNS records quotas at the account level for Enterprise accounts. Instead of a per-zone limit, these accounts have a quota on the total number of records across all of their zones, letting you distribute records across your zones however you like — regardless of each zone's plan. Public and internal zones are counted separately, each with a default quota of 1,000,000 records.</p>
<p>Accounts without an account-level quota are unaffected: existing per-zone quotas behave exactly as before.</p>
<p>For more details, refer to <a href="/dns/manage-dns-records/#dns-records-quota">DNS records quota</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-10">Jun 10, 2026</time><div>
<h2 id="post-2026-06-10-api-reference"><a href="/changelog/post/2026-06-10-api-reference/">Flagship API reference now available</a></h2>
<div class="changelog-badges"><span>flagship</span></div><div class="changelog-body"><p>The <strong><a href="/api/resources/flagship/">Flagship API reference</a></strong> is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard.</p>
<p>For example, create a new boolean flag with the API:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/flags \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;key&quot;: &quot;new-checkout&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;default_variation&quot;: &quot;off&quot;,&#10;    &quot;variations&quot;: {&#10;      &quot;off&quot;: false,&#10;      &quot;on&quot;: true&#10;    },&#10;    &quot;rules&quot;: []&#10;  }&#x27;&#10;</code></pre>
<p>To create an API token, go to <a href="https://dash.cloudflare.com/?to=/:account/api-tokens">Account API Tokens</a> in the Cloudflare dashboard and search for Flagship.</p>
<p>The API reference includes endpoints for Flagship apps, flags, changelog entries, and flag evaluation. Agents can also use the <a href="https://github.com/cloudflare/skills/tree/main/skills/cloudflare/references/flagship">Flagship reference in the Cloudflare skill</a> to create and manage Flagship resources.</p>
<p>Refer to the <a href="/flagship/">Flagship documentation</a> to learn more about evaluating feature flags from your applications.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-10">Jun 10, 2026</time><div>
<h2 id="post-2026-06-10-hosted-images-binding"><a href="/changelog/post/2026-06-10-hosted-images-binding/">Manage hosted images with the Images binding</a></h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.</p>
<p>The <code>env.IMAGES.hosted</code> namespace supports the following storage and management operations:</p>
<ul>
<li><a href="/images/storage/binding/#uploadimage-options"><code>.upload(image, options)</code></a> — Upload a new image to your account.</li>
<li><a href="/images/storage/binding/#listoptions"><code>.list(options)</code></a> — List images with pagination.</li>
<li><a href="/images/storage/binding/#imageimageiddetails"><code>.image(imageId).details()</code></a> — Get image metadata.</li>
<li><a href="/images/storage/binding/#imageimageidbytes"><code>.image(imageId).bytes()</code></a> — Stream the original image bytes.</li>
<li><a href="/images/storage/binding/#imageimageidupdateoptions"><code>.image(imageId).update(options)</code></a> — Update metadata or access controls.</li>
<li><a href="/images/storage/binding/#imageimageiddelete"><code>.image(imageId).delete()</code></a> — Delete an image.</li>
</ul>
<p>For example, you can upload an image from a request body and return its metadata:</p>
<pre tabindex="0"><code class="language-ts">const image = await env.IMAGES.hosted.upload(request.body, {&#10;	filename: &quot;upload.jpg&quot;,&#10;	metadata: { source: &quot;worker&quot; },&#10;});&#10;&#10;return Response.json(image);&#10;</code></pre>
<p>Or retrieve and serve the original bytes of a hosted image:</p>
<pre tabindex="0"><code class="language-ts">const bytes = await env.IMAGES.hosted.image(&quot;IMAGE_ID&quot;).bytes();&#10;return new Response(bytes);&#10;</code></pre>
<p>For more information, refer to the <a href="/images/storage/binding/">Images binding</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-10">Jun 10, 2026</time><div>
<h2 id="post-2026-06-08-brand-protection-cease-and-desist-letters"><a href="/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/">Automated Cease and Desist templates for Brand Protection</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p><strong>TL;DR:</strong> Brand Protection now features an <strong>Automated Cease &amp; Desist (C&amp;D)</strong> workflow. When you discover an infringing domain hosted outside of Cloudflare, you can instantly generate, review, and download a custom-branded, pre-filled legal notice in seconds.</p>
<h4 id="2026-06-08-brand-protection-cease-and-desist-letters-why-this-matters">Why this matters</h4>
This update introduces a major shift from pure detection to actionable enforcement, eliminating the manual burden for your Trust & Safety and Legal teams:
<ul>
<li><strong>Instant WHOIS and Recipient Lookup:</strong> We automatically scrape registrar data and WHOIS contact information (such as the registrant or registrar abuse email) behind the scenes, highlighting exactly where your notice needs to be sent</li>
<li><strong>Smart Template Automation:</strong> We pre-fill your custom-branded templates with essential metadata, including the infringing domain, registrar name, and discovery date.</li>
<li><strong>Tailored Enforcement Tones:</strong> Choose from three default layout strategies depending on the severity of the infrastructure match:
<ul>
<li><em>Exact Match:</em> A formal demand for identical trademark infringements</li>
<li><em>Similar Match:</em> A standard notice optimized for typosquatting (one-character distance matches)</li>
<li><em>Friendly Tone:</em> An amicable initial outreach for potential unintentional or accidental infringements</li>
</ul>
</li>
<li><strong>Full Editing Control:</strong> Before creating the final PDF, a real-time review screen allows you to fine-tune the messaging, modify placeholders, and ensure your text aligns perfectly with internal legal standards</li>
</ul>
<h4 id="2026-06-08-brand-protection-cease-and-desist-letters-how-it-works">How it works</h4>
When reviewing a malicious domain match inside your dashboard, your enforcement path splits depending on where the attacker is located:
<ol>
<li><strong>On the Cloudflare Network:</strong> If the domain uses Cloudflare’s network or registrar, trigger our existing integrated abuse reporting flow with one click.</li>
<li><strong>Hosted Elsewhere:</strong> If the domain is hosted on an external provider, click the <strong>Generate C&amp;D Letter</strong> option to launch the new document builder, pick your template, verify the auto-populated recipient data, and download your finalized PDF.</li>
</ol>
<p>You can manage your templates and enforce matches by going to the <strong>Cloudflare Dashboard &gt; Application Security &gt; Brand Protection</strong> and selecting your detected Brand Protection matches.
For more information, read the <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>
<blockquote>
<p><strong>Note:</strong> Cloudflare does not represent you and cannot provide you with legal advice. Only you can decide whether your rights have been infringed, whether a cease and desist letter is appropriate, and what that letter should say.</p>
</blockquote>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-09">Jun 9, 2026</time><div>
<h2 id="post-2026-06-09-deprecating-sandbox-sdk-features"><a href="/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/">Deprecating Sandbox SDK features</a></h2>
<div class="changelog-badges"><span>sandbox</span></div><div class="changelog-body"><aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-06-09-deprecating-sandbox-sdk-features-sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h4>
@markup("md", "content/.markup/bodies/17752.md")</aside>
<p>Today we are announcing the deprecation of several features from the Sandbox SDK. The SDK has grown and matured substantially since it first launched. As agent workflows have developed, we have shipped many new features and experiments so developers can easily integrate secure, isolated code execution into their workflows.</p>
<p>We want the SDK to continue providing a stable foundation for agentic workflows while we iterate quickly on the codebase. These deprecated features have either been superseded by newer capabilities or seen low adoption. Do not build new work on them. Migrate using the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration guide</a>, or move to the <a href="/sandbox/1-0-preview/">Sandbox SDK 1.0 preview</a> when you can.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-http-and-websocket-transports">HTTP and WebSocket transports</h4>
<p>In April 2026, we released the new RPC transport and deprecated the WebSocket transport. This setting governs how the sandbox container talks to the Workers ecosystem. The RPC transport removes the limitations of both the HTTP and WebSocket transports. As of this announcement, RPC is the recommended default. HTTP and WebSocket transports are deprecated and will not ship in future Sandbox SDK majors.</p>
<p>To migrate, update the <code>SANDBOX_TRANSPORT</code> variable to <code>rpc</code> or set the <code>transport</code> option when calling <code>getSandbox()</code>. For more information, refer to the <a href="/sandbox/configuration/transport/">transport configuration documentation</a>.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-desktop">Desktop</h4>
<p>The desktop feature ran a full Linux desktop inside the sandbox (display server, desktop environment, and VNC/noVNC) so agents and apps could drive a GUI with screenshots, mouse, and keyboard — the same <em>computer-use</em> shape other sandbox products expose for UI automation. Adoption stayed low, and we removed it in <code>0.10.2</code>. If you need that capability again, you can build it on top of the sandbox with <a href="/sandbox/1-0-preview/extensions/">extensions</a> rather than a built-in <code>sandbox.desktop</code> API.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-expose-ports">Expose ports</h4>
<p>We recently released support for Cloudflare Tunnel in the Sandbox SDK. This provides a robust API for exposing services running in your sandbox to the public internet. It fixes issues many were facing with local development and deployment to <code>workers.dev</code> domains. To migrate from <code>exposePort()</code> to tunnels, refer to the <a href="/sandbox/api/tunnels/">tunnels API documentation</a> and the <a href="/sandbox/guides/expose-services/">expose services guide</a>.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-default-sessions">Default sessions</h4>
<p>By default, the <code>exec()</code> method in the Sandbox SDK maintains a default session across all calls, so a <code>cd</code> in one call is honored in the next. This convenience helped developers writing <code>exec</code> statements by hand, but confused agents and caused hard-to-trace bugs. As of <code>0.10.3</code>, we have introduced the <a href="/sandbox/configuration/sandbox-options/"><code>enableDefaultSession</code></a> flag on the <code>getSandbox()</code> interface to turn this off. Default sessions as a concept — and the flag — will be removed in an upcoming release.</p>
<p>We recommend setting <code>enableDefaultSession: false</code> today and using the <a href="/sandbox/api/sessions/"><code>sandbox.createSession()</code> API</a> when you need the previous behavior.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-other-changes">Other changes</h4>
<p>We are also consolidating all APIs that buffer data to support streaming by default. This includes <a href="/sandbox/api/files/"><code>readFile</code>, <code>writeFile</code></a>, and <a href="/sandbox/api/commands/"><code>exec</code></a>. The stream equivalents will be removed.</p>
<p>We are exploring moving non-core features like the <a href="/sandbox/guides/code-execution/">code interpreter</a>, <a href="/sandbox/api/terminal/">terminal</a>, and <a href="/sandbox/guides/git-workflows/">git APIs</a> into helpers. These features will retain their existing APIs, so migration should be simple.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-next-steps">Next steps</h4>
<p>If you use any of these features on the <strong>current stable</strong> package, refer to the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration guide</a>. Coding agents can use the <strong><code>sandbox-stable</code></strong> skill for stable-package work and that guide for cleanup (<a href="/agent-setup/">Agent setup</a> · <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a>).</p>
<p>If you are moving to <strong>Sandbox SDK 1.0</strong> (<code>@next</code>), use the <a href="/sandbox/1-0-preview/">1.0 preview</a> and <a href="/sandbox/1-0-preview/migrate/">Migrate</a> guides instead — or the <strong><code>sandbox-migrate-to-next</code></strong> skill after installing Cloudflare Skills. New projects should prefer <strong><code>sandbox-next</code></strong> on <code>@next</code>.</p>
<p>For any questions, ask in the <a href="https://discord.gg/cloudflaredev">Cloudflare Developers Discord</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-09">Jun 9, 2026</time><div>
<h2 id="post-2026-06-09-waf-release"><a href="/changelog/post/2026-06-09-waf-release/">WAF Release - 2026-06-09</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new detections for a critical SQL injection vulnerability in Drupal installations utilizing PostgreSQL (CVE-2026-9082), alongside targeted protection for an unsafe deserialization flaw in the Mirasvit Cache Warmer extension (CVE-2026-45247). Additionally, this release includes coverage for a prototype pollution vector in Axios (CVE-2026-40175) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-9082: A database abstraction vulnerability affects Drupal sites configured with a PostgreSQL backend. Remote, unauthenticated attackers can exploit this flaw via crafted inputs to inject malicious SQL commands and access or manipulate backend data.</p>
</li>
<li>
<p>CVE-2026-45247: A PHP Object Injection vulnerability exists in the Mirasvit Cache Warmer extension for Magento and Adobe Commerce. This flaw stems from unsafe deserialization of untrusted user input, enabling unauthenticated attackers to execute arbitrary code on the hosting server.</p>
</li>
<li>
<p>CVE-2026-40175: A prototype pollution vulnerability affects the Axios HTTP client library. Attackers can exploit this to inject malicious properties into the global JavaScript object prototype, potentially causing application crashes (Denial of Service) or executing unauthorized code depending on the application structure.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, manipulate database contents, or induce application crashes, leading to severe operational disruption or complete server compromise. These newly deployed signatures intercept these advanced malicious payloads at the edge before they can interact with vulnerable software configurations.</p>
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
				<code class="nb-rule-id" title="b4f88cb767874def810edd0b387cf935">387cf935</code>
</td>
<td>N/A</td>
<td>Axios - Prototype Pollution - CVE:CVE-2026-40175</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="098997bb8b5f48abb4039bd6417eb9e0">417eb9e0</code>
</td>
<td>N/A</td>
<td>Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - Body</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8a7650b99ec04a91a19b8295fd3857fd">fd3857fd</code>
</td>
<td>N/A</td>
<td>Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="525c0871787840e6a6193f6caee241d2">aee241d2</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1ec4aeaf7900463397b82b35d8620070">d8620070</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fb74766654c44ff2a5204dc4e0be4d47">e0be4d47</code>
</td>
<td>N/A</td>
<td>Mirasvit Cache Warmer - PHP Object Injection - CVE:CVE-2026-45247</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-08">Jun 8, 2026</time><div>
<h2 id="post-2026-06-08-smtp-submission"><a href="/changelog/post/2026-06-08-smtp-submission/">Authenticated SMTP submission now available in beta</a></h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>You can now send emails through <strong>Cloudflare Email Service</strong> using authenticated <a href="/email-service/api/send-emails/smtp/">SMTP submission</a> on <code>smtp.mx.cloudflare.net:465</code>. SMTP joins the <a href="/email-service/api/send-emails/rest-api/">REST API</a> and the <a href="/email-service/api/send-emails/workers-api/">Workers binding</a> as a third way to send transactional email — useful for existing applications that already speak SMTP and language-native SMTP libraries (Nodemailer, <code>smtplib</code>, PHPMailer, JavaMail).</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td><code>smtp.mx.cloudflare.net</code></td>
</tr>
<tr>
<td>Port</td>
<td><code>465</code> (implicit TLS)</td>
</tr>
<tr>
<td>AUTH</td>
<td><code>PLAIN</code> or <code>LOGIN</code></td>
</tr>
<tr>
<td>Username</td>
<td><code>api_token</code></td>
</tr>
<tr>
<td>Password</td>
<td>A Cloudflare API token (account-owned or user-owned) with <strong>Email Sending: Edit</strong></td>
</tr>
</tbody>
</table>
<p>Submissions enter the same delivery pipeline as the REST API and Workers binding: identical <a href="/email-service/platform/limits/">limits</a>, automatic DKIM and ARC signing, and shared dashboard logs.</p>
<p>Send your first email with a single command:</p>
<pre tabindex="0"><code class="language-sh">curl --ssl-reqd \&#10;  &#45;-url &quot;smtps://smtp.mx.cloudflare.net:465&quot; \&#10;  &#45;-user &quot;api_token:&lt;API_TOKEN&gt;&quot; \&#10;  &#45;-mail-from &quot;welcome@yourdomain.com&quot; \&#10;  &#45;-mail-rcpt &quot;user@example.com&quot; \&#10;  &#45;-upload-file mail.txt&#10;</code></pre>
<p>Refer to the <a href="/email-service/api/send-emails/smtp/">SMTP reference</a> for authentication details, response codes, and language-specific examples.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-08">Jun 8, 2026</time><div>
<h2 id="post-2026-06-05-union-intersect-except-select-distinct"><a href="/changelog/post/2026-06-05-union-intersect-except-select-distinct/">R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p><a href="/r2-sql/">R2 SQL</a> now supports set operations (<code>UNION</code>, <code>INTERSECT</code>, <code>EXCEPT</code>) and <code>SELECT DISTINCT</code>, expanding the range of analytical queries you can run directly on <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<h4 id="2026-06-05-union-intersect-except-select-distinct-set-operations">Set operations</h4>
<p>Combine the results of multiple <code>SELECT</code> statements:</p>
<ul>
<li><strong><code>UNION</code></strong> — returns all rows from both queries, removing duplicates</li>
<li><strong><code>UNION ALL</code></strong> — returns all rows from both queries, including duplicates</li>
<li><strong><code>INTERSECT</code></strong> — returns only rows that appear in both queries</li>
<li><strong><code>EXCEPT</code></strong> — returns rows from the first query that do not appear in the second</li>
</ul>
<pre tabindex="0"><code class="language-sql">&#45;- Find zones that had either firewall blocks OR high-risk requests&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;UNION&#10;SELECT zone_id FROM my_namespace.http_requests WHERE risk_score &gt; 0.8&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Find zones with both firewall blocks AND high traffic&#10;SELECT zone_id FROM my_namespace.firewall_events WHERE action = &#x27;block&#x27;&#10;INTERSECT&#10;SELECT zone_id FROM my_namespace.http_requests&#10;GROUP BY zone_id&#10;HAVING COUNT(*) &gt; 10000&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Find enterprise zones that have not been compacted&#10;SELECT zone_id FROM my_namespace.zones WHERE plan = &#x27;enterprise&#x27;&#10;EXCEPT&#10;SELECT zone_id FROM my_namespace.compaction_history&#10;</code></pre>
<h4 id="2026-06-05-union-intersect-except-select-distinct-select-distinct">Select distinct</h4>
<p>Eliminate duplicate rows from query results:</p>
<pre tabindex="0"><code class="language-sql">SELECT DISTINCT region, department&#10;FROM my_namespace.sales_data&#10;WHERE total_amount &gt; 1000&#10;ORDER BY region, department&#10;LIMIT 100&#10;</code></pre>
<p>For large datasets where approximate results are acceptable, <code>approx_distinct()</code> remains a faster alternative for counting unique values.</p>
<p>For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For performance guidance, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-08">Jun 8, 2026</time><div>
<h2 id="post-2026-06-08-realtimekit-post-meeting-transcription-ga"><a href="/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/">Post-meeting transcriptions are now Generally Available in RealtimeKit</a></h2>
<div class="changelog-badges"><span>realtime</span></div><div class="changelog-body"><p><a href="/realtime/realtimekit/">RealtimeKit</a> lets you build products where people meet over live audio and video — such as HealthTech, EdTech, proctoring, and other real-time platforms — on Cloudflare's <a href="/realtime/sfu/calls-vs-sfus/">global WebRTC infrastructure</a>.</p>
<p><a href="/realtime/realtimekit/ai/transcription/#post-meeting-transcription">Post-meeting transcription</a> is now Generally Available, so completed RealtimeKit meetings can automatically produce full transcript files after they end. Those transcripts can also power <a href="/realtime/realtimekit/ai/summary/">AI-generated summaries</a> for meeting notes, review workflows, and follow-up tasks after the transcript is available.</p>
<p>Post-meeting transcription is a managed service powered by <a href="/workers-ai/">Workers AI</a> using <a href="/workers-ai/models/whisper-large-v3-turbo/">Whisper Large v3 Turbo</a>. RealtimeKit handles transcription processing and can return transcript and summary files through <a href="/realtime/realtimekit/webhooks/">webhooks</a> or the REST API, so you do not need to run your own transcription infrastructure.</p>
<h4 id="2026-06-08-realtimekit-post-meeting-transcription-ga-generate-transcripts-and-summaries">Generate transcripts and summaries</h4>
<p>To generate a transcript after a meeting ends, set <code>transcribe_on_end: true</code> when <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a>. To also generate an AI summary automatically after the transcript is available, set <code>summarize_on_end: true</code>:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;title&quot;: &quot;Weekly product review&quot;,&#10;    &quot;transcribe_on_end&quot;: true,&#10;    &quot;summarize_on_end&quot;: true,&#10;    &quot;ai_config&quot;: {&#10;      &quot;transcription&quot;: {&#10;        &quot;language&quot;: &quot;en&quot;&#10;      },&#10;      &quot;summarization&quot;: {&#10;        &quot;word_limit&quot;: 500,&#10;        &quot;text_format&quot;: &quot;markdown&quot;,&#10;        &quot;summary_type&quot;: &quot;team_meeting&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-06-08-realtimekit-post-meeting-transcription-ga-consume-results">Consume results</h4>
<p>When RealtimeKit finishes processing a meeting, it creates download URLs for the transcript and, if <code>summarize_on_end</code> is set, the summary. You can receive those URLs automatically with <a href="/realtime/realtimekit/webhooks/">webhooks</a>, or fetch them later for a specific session with the <a href="/realtime/realtimekit/ai/summary/#rest-api">REST API</a>.</p>
<p>To receive results as soon as they are ready, configure the <code>meeting.transcript</code> and <code>meeting.summary</code> webhook events:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;name&quot;: &quot;AI results webhook&quot;,&#10;    &quot;url&quot;: &quot;https://example.com/webhook&quot;,&#10;    &quot;events&quot;: [&quot;meeting.transcript&quot;, &quot;meeting.summary&quot;],&#10;    &quot;enabled&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>To fetch results later, call the <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/">transcript</a> or <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/">summary</a> endpoint for the session:</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Use the <a href="/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/">Generate summary of transcripts for the session</a> API only if <code>summarize_on_end</code> was not set and you want to generate a summary manually after the transcript is available:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Post-meeting transcription supports <a href="/realtime/realtimekit/ai/transcription/#output-formats">CSV, JSON, SRT, and VTT transcript outputs</a>, <a href="/realtime/realtimekit/ai/transcription/#post-meeting-supported-languages">automatic language detection and Whisper language codes</a>. RealtimeKit also supports <a href="/realtime/realtimekit/ai/transcription/#real-time-transcription">real-time transcription</a> with <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> for live captions, in-meeting accessibility, and real-time note-taking.</p>
<p>Learn more in the <a href="/realtime/realtimekit/ai/transcription/">RealtimeKit transcription docs</a> and <a href="/realtime/realtimekit/ai/summary/">summary docs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-08">Jun 8, 2026</time><div>
<h2 id="post-2026-06-08-create-waf-rules-from-threat-events"><a href="/changelog/post/2026-06-08-create-waf-rules-from-threat-events/">Create WAF rules directly from Threat Events saved views</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>Cloudforce One users can now turn <a href="/security-center/cloudforce-one/#analyze-threat-events">Threat Events indicators</a> into active defense. With this update, users can instantly generate a WAF rule that matches the dynamic list of IP addresses returned by any of their <strong>Saved Views</strong>.</p>
<h4 id="2026-06-08-create-waf-rules-from-threat-events-why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is immediately actionable. Previously, blocking threat actors required manually extracting indicators from threat events and copying them into your firewall rules.
This new integration bridges the gap between threat discovery and threat mitigation:</p>
<ul>
<li>When you identify an active threat pattern - such as an ongoing campaign targeting a specific industry, or using a known indicator type - you can pivot from investigation to mitigation in a single click.</li>
<li>Instead of writing complex, static IP rules, this functionality allows you to leverage the specific filtering logic you have already defined and saved within your Threat Events ecosystem.</li>
<li>Automating the generation of the WAF rule expression from your threat views eliminates manual copying errors, ensuring that the right malicious infrastructure is blocked instantly.</li>
</ul>
<h4 id="2026-06-08-create-waf-rules-from-threat-events-how-to-use-it">How to use it</h4>
<p>You can implement these rules through both the dashboard UI and via the API / Terraform.</p>
<p>Go to <strong>Cloudflare Dashboard</strong> &gt; <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Manage Views</strong>, select your desired view, and select <strong>Create WAF Rule</strong>.</p>
<p>This will automatically pre-populate the <a href="/firewall/cf-dashboard/create-edit-delete-rules/">WAF rule builder</a> with the matching threat event IP indicators.</p>
<p>You can also automate this workflow by utilizing the <a href="/firewall/api/cf-firewall-rules/"><strong>WAF Rule Builder API</strong></a> alongside your <a href="/firewall/api/cf-firewall-rules/">Threat Events saved views endpoints</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-08">Jun 8, 2026</time><div>
<h2 id="post-2026-06-08-threat-actor-profiles"><a href="/changelog/post/2026-06-08-threat-actor-profiles/">Introducing Threat Actor Profiles in Threat Events</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p><strong>TL;DR:</strong> We’ve launched <strong>Threat Actor Profiles</strong> directly inside the Threat Events dashboard. You can now immediately pivot from a generic alert or blocked event to a profile that unmasks the &quot;Who, Why, and How&quot; behind a threat event.</p>
<h4 id="2026-06-08-threat-actor-profiles-why-this-matters">Why this matters</h4>
Security teams often suffer from a visibility gap. When an attack is blocked, it's difficult to know if it was a random automated bot or a sophisticated advanced persistent threat (APT) campaign specifically targeting your industry. Finding out usually means leaving your security dashboard to hunt through external OSINT feeds or static, out-of-date threat reports.
Threat Actor Profiles solve this by sharing Cloudforce One’s deep adversary research directly inside your workflow:
* Cloudflare sees the traffic in real-time across approximately 20% of the web. This means actor profiles display active malicious infrastructure the moment it touches our global edge.
* Every profile provides clear strategic and tactical modules including alternative aliases, origin tracking, historical threat event volume, and MITRE ATT&CK mapping detailing the adversary's technical methods.
* You can search the dedicated threat actor directory or click an actor's name inside any threat event to view all details and related events to the specific threat actor.
<h4 id="2026-06-08-threat-actor-profiles-how-to-use-it">How to use it</h4>
Adversary tracking is now available in the Cloudflare Dashbboard and ready to be included in your daily investigation workflow:
* Click on the **Threat Actor** name in the Threat Events table to open their full identity profile and review their aliases and attack stats.
* Navigate to **Cloudflare Dashboard > Application Security > Threat Intelligence** to explore the new **Threat Actors** tab. Here, you can browse a card-based directory of all established entities tracked by Cloudforce One.
<p>Learn more in the <a href="https://developers.cloudflare.com/security-center/cloudforce-one/#identify-the-adversary">Cloudforce One documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-05">Jun 5, 2026</time><div>
<h2 id="post-2026-06-05-saga-rollbacks"><a href="/changelog/post/2026-06-05-saga-rollbacks/">Rollback support now available in Workflows</a></h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> now supports saga-style rollbacks,  allowing you to add compensating logic to each <code>step.do()</code> in case of downstream failures. If the instance fails, the rollback handlers will execute in reverse <code>step-start</code> order.</p>
<p>This is useful for multi-step operations that touch external systems, such as inventory reservations, payment authorization, ticket creation, or infrastructure provisioning. Instead of writing all cleanup logic in a top-level <code>catch</code>, you can keep each compensating action next to the step it undoes.</p>
<p>Rollback handlers support their own retry and timeout configuration, and Workflows now exposes rollback outcomes in instance status responses. Workflows analytics also emits rollback lifecycle events, making it easier to distinguish a forward execution failure from a rollback failure when debugging production workflows.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17832.md")</div>
<p>Refer to <a href="/workflows/build/workers-api/#rollback-options">rollback options</a> to learn more.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-05">Jun 5, 2026</time><div>
<h2 id="post-2026-06-05-spend-limits"><a href="/changelog/post/2026-06-05-spend-limits/">Control AI costs with spend limits</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway now supports spend limits — cost-based budgets that track cumulative dollar spend and block requests when the budget is exceeded. Unlike rate limiting, which caps the number of requests, spend limits track actual cost based on token usage and model pricing.</p>
<p>You can scope limits by model, provider, or custom metadata dimensions. For example, give each user a $200/day budget, cap total gateway spend at $10,000/day, or limit a specific model to $50/day per user. Each rule uses a configurable time window with fixed or sliding enforcement.</p>
<p>Spend limits work with both <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> and <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK</a> requests for models with known pricing.</p>
<p>For more details, refer to the <a href="/ai-gateway/features/spend-limits/">Spend limits documentation</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/11/">Previous</a><span>Page 12 of 50</span><a class="pagination-next" rel="next" href="/changelog/13/">Next</a></nav>
</div>
