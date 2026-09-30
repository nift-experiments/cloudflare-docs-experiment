<h1 id="changelog">Changelog</h1>

<h2 id="hostname-routing-is-now-generally-available-with-a-new-public-ip-range-for-initial-resolved-ips"><a href="/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/">Hostname routing is now generally available, with a new public IP range for initial resolved IPs</a></h2>
<p><em>2026-08-11</em></p>
<p><a href="https://blog.cloudflare.com/tunnel-hostname-routing/">Hostname routing</a> is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:</p>
<ul>
<li><strong>Cloudflare Tunnel</strong>: route a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> (for example, <code>wiki.internal.local</code>) to a private application behind your tunnel, or a <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> (for example, <code>bank.example.com</code>) to egress through a specific tunnel and anchor traffic to a dedicated exit node.</li>
<li><strong>Cloudflare Mesh</strong>: attract a <a href="/mesh/features/routes/#hostname-routes">private or public hostname's traffic</a> to a Mesh node.</li>
</ul>
<p>Alongside GA, the default IPv4 range used for <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/17760.md")</div> (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p><strong>Why this is changing:</strong> Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restrictions block background requests to CGNAT addresses (<code>100.64.0.0/10</code>), which included the previous initial resolved IP default (<code>100.80.0.0/16</code>). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.</p>
<p><strong>What is affected:</strong> Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">Private</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public</a> hostname routing for Cloudflare Tunnel</li>
<li><a href="/mesh/features/routes/#hostname-routes">Hostname routes</a> for Cloudflare Mesh</li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access private applications</a> on non-HTTPS ports</li>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Egress policy host selectors</a> (Domain, Host, Application, and Content Categories)</li>
</ul>
<p>You can check your account's current range, or configure a custom range, at any time from <strong>Networking</strong> &gt; <strong>IP addresses</strong> &gt; <strong>Address space</strong> &gt; <strong>Custom IPs</strong>, or using the <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/#(resource)%20zero_trust.networks.subnets.initial_resolved_ip">Initial Resolved IP Subnet API</a>.</p>
<div class="nb-dash-button"></div>
<p>For full instructions, refer to <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">Configure initial resolved IPs</a>. The IPv6 range (<code>2606:4700:0cf1:4000::/64</code>) is unchanged and is not affected by this restriction.</p>
<p>The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">Automatically managed ranges</a> for details.</p>
<p>If you were relying on a Chrome Enterprise policy workaround (such as <code>LocalNetworkAccessRestrictionsTemporaryOptOut</code>) while your account was still on the legacy CGNAT-based range, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames">Google Chrome restricts access to private hostnames</a> for next steps.</p>


<h2 id="stream-live-logs-from-cloudflare-tunnel-in-the-dashboard"><a href="/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/">Stream live logs from Cloudflare Tunnel in the dashboard</a></h2>
<p><em>2026-08-10</em></p>
<p>Real-time Tunnel log streaming is now available in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong>. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-live-logs-core-dashboard.gif" alt="Stream live logs from a tunnel in the Cloudflare dashboard" /></p>
<p>In the tunnel detail view, a new <strong>Live logs</strong> tab lets you:</p>
<ul>
<li><strong>Stream logs from single or multiple connectors</strong> — In <a href="/tunnel/configuration/#replicas-and-high-availability">highly available</a> deployments with multiple <code>cloudflared</code> replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.</li>
<li><strong>Filter by log level, event type, and HTTP method</strong> — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or <code>cloudflared</code> internal), at any log level.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/tunnel/observability/#remote-log-streaming">Tunnel observability</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a>.</p>


<h2 id="turnstile-spin-is-now-generally-available"><a href="/changelog/post/2026-08-10-turnstile-spin-ga/">Turnstile Spin is now generally available</a></h2>
<p><em>2026-08-10</em></p>
<p><a href="/turnstile/spin/">Turnstile Spin</a> is now generally available with three setup paths for creating a Turnstile widget and wiring canonical server-side siteverify into your existing backend. Start in the dashboard, with Wrangler, or from your AI coding agent. All three paths create the same widget. You can complete the integration by hand or have your agent embed the widget, wire siteverify, and validate it.</p>
<h4 id="2026-08-10-turnstile-spin-ga-server-side-verification">Server-side verification</h4>
<p>Turnstile setup has two parts: embed the widget in your frontend, then call siteverify from your backend. Without the second part, the widget appears on the page but does not protect the request.</p>
<ul>
<li>The skill includes insertion snippets for Next.js (App Router and Pages Router), Astro, SvelteKit, Hugo, and vanilla HTML. For other frameworks, the agent proposes a generic pattern and asks you to confirm it first.</li>
<li>The Turnstile dashboard flags existing widgets with no matching siteverify traffic. Select <strong>Fix with Spin</strong> to copy a prompt that guides your agent through wiring siteverify into your backend.</li>
<li>Before finishing, the agent runs a real Turnstile token through your protected endpoint, checks that it passes, then replays the token to confirm the endpoint rejects it on the second try. If a check fails, the agent stops and shows you where.</li>
</ul>
<h4 id="2026-08-10-turnstile-spin-ga-run-spin">Run Spin</h4>
<p>You can run Spin three ways:</p>
<ul>
<li>In the <strong>Turnstile dashboard</strong>, select <strong>Set up with Spin</strong>, enter your domains, then select <strong>Set up</strong>. Spin creates the widget and returns the sitekey, secret, and a prompt for your agent.</li>
<li>From the <code>Wrangler CLI</code>, run <a href="/turnstile/spin/#set-up-from-the-wrangler-cli"><code>wrangler turnstile widget create</code></a>. Wrangler prints the sitekey and secret. You wire the frontend and siteverify by hand.</li>
<li>From your <strong>AI coding agent</strong>, paste the <a href="/turnstile/spin/#set-up-from-an-ai-coding-agent">Spin prompt</a> into Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot Chat. Your agent fetches the skill, creates the widget, then embeds it and wires siteverify.</li>
</ul>
<p>To get started, refer to the <a href="/turnstile/spin/">Turnstile Spin documentation</a>.</p>


<h2 id="workers-ai-and-ai-gateway-unify-model-access-and-billing"><a href="/changelog/post/2026-08-07-workers-ai-unified-billing/">Workers AI and AI Gateway unify model access and billing</a></h2>
<p><em>2026-08-07</em></p>
<p>Workers AI and AI Gateway now provide a unified path for accessing models and managing inference traffic. Use the same AI binding and REST API to call models hosted on Workers AI or by supported third-party providers, with AI Gateway providing observability, logging, caching, security, and billing controls.</p>
<h4 id="2026-08-07-workers-ai-unified-billing-unified-entrypoints-and-observability">Unified entrypoints and observability</h4>
<p>The <a href="/ai-gateway/usage/worker-binding-methods/">AI binding</a> supports both Workers AI and third-party models through <code>env.AI.run()</code>. The <a href="/ai-gateway/usage/rest-api/">REST API</a> provides shared <code>/ai/</code> endpoints with Cloudflare authentication across providers.</p>
<p>Route a Workers AI request through AI Gateway by specifying a gateway ID. Use <code>default</code> to automatically create a gateway on the first authenticated request, or specify an existing gateway to separate applications and workloads:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17687.md")</div>
<p>Requests routed through AI Gateway can be logged and included in analytics for request volume, errors, latency, token usage, and costs. You can also configure controls such as caching, rate limiting, and request retries on the gateway.</p>
<h4 id="2026-08-07-workers-ai-unified-billing-unified-billing-and-higher-rate-limits">Unified billing and higher rate limits</h4>
<p>You can now use prepaid <a href="/ai-gateway/features/unified-billing/">AI Gateway credits</a> to pay for Workers AI inference. This provides one credit balance for Workers AI and supported third-party model providers. To use credits for Workers AI, set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>. Workers AI requests routed through that gateway deduct from your credit balance in real time.</p>
<p>Prepaid credits also provide access to the following Workers AI frontier models without requiring the Workers Paid plan. Each frontier Workers AI model has a rate limit of 50 requests per minute per account, per model when billed with AI Gateway credits, compared to 20 requests per minute through standard Workers AI billing:</p>
<ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a></li>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a></li>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a></li>
</ul>
<p>These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.</p>
<p>For details, refer to <a href="/workers-ai/platform/limits/">Workers AI limits</a>, <a href="/workers-ai/platform/pricing/">Workers AI pricing</a>, <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, and the <a href="/ai/models/">AI Gateway model catalog</a>.</p>


<h2 id="mysql-support-in-hyperdrive-is-now-generally-available"><a href="/changelog/post/2026-08-07-hyperdrive-mysql-ga/">MySQL support in Hyperdrive is now generally available</a></h2>
<p><em>2026-08-07</em></p>
<p>Support for MySQL in Hyperdrive is now generally available. You can connect to any MySQL database from your Workers using Hyperdrive.</p>
<p>Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.</p>
<p>You can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, with no code changes required. MySQL support is available at the same <a href="/hyperdrive/platform/pricing/">pricing</a> as Postgres.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17733.md")</div>
<p>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a> and <a href="/hyperdrive/get-started/">get started building Workers that connect to MySQL with Hyperdrive</a>.</p>


<h2 id="restart-a-hyperdrive-configuration-from-the-dashboard"><a href="/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/">Restart a Hyperdrive configuration from the dashboard</a></h2>
<p><em>2026-08-07</em></p>
<p>You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.</p>
<p>Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.</p>
<p>To restart, select your Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to the <strong>Settings</strong> tab, and select <strong>Restart</strong> under <strong>Danger zone</strong>. Restarting requires the <a href="/fundamentals/manage-members/roles/"><strong>Hyperdrive Admin</strong> role</a>. After a restart, the <strong>Settings</strong> tab shows when the configuration was last manually restarted.</p>
<p><img src="/assets/upstream/images/hyperdrive/dashboard-restart-danger-zone.png" alt="The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions." /></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17734.md")</aside>
<p>For more information, refer to <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>


<h2 id="sandbox-sdk-1-0-preview-on-next"><a href="/changelog/post/2026-08-07-sandbox-sdk-1-0-preview/">Sandbox SDK 1.0 preview on @next</a></h2>
<p><em>2026-08-07</em></p>
<p><strong>Sandbox SDK 1.0</strong> is available to preview under the npm <code>@next</code> tag. For existing applications, the current stable package remains published on the 0.12.x line.</p>
<p>Sandbox SDK first shipped to provide a rich library for running untrusted and agent-driven work on <a href="/containers/">Cloudflare Containers</a>. Since then, both Sandbox and Containers have matured. This preview is a thinner SDK built on a richer Cloudflare Containers foundation.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="2026-08-07-sandbox-sdk-1-0-preview-what-this-preview-is">What this preview is</h4>
<ul>
<li><strong>A single execution interface</strong> — <code>sandbox.exec()</code> takes an argument list, returns when the process <strong>starts</strong>, and gives you a handle for output, logs, waits, and signals. Both short commands and long-running services use the same API.</li>
<li><strong>Removed session execution</strong> — the SDK no longer maintains shell state between executions. Each launch is independent. Pass <code>cwd</code> and <code>env</code> when you need them, or put multi-step shell syntax in one explicit shell command.</li>
<li><strong>RPC as the only transport</strong> — the SDK talks to the container exclusively over RPC. Remove <code>SANDBOX_TRANSPORT</code>, <code>transport</code> on <code>getSandbox()</code>, and <code>setTransport()</code>.</li>
<li><strong>Improved PTY and terminal interface</strong> — interactive PTYs use <code>createTerminal</code> / <code>connect</code>, not the older session-shaped helpers.</li>
<li><strong>Code interpreter as an extension</strong> — configure the code interpreter on your <code>Sandbox</code> subclass so you only ship what you need.</li>
</ul>
<p>Start new projects on <code>@next</code>. Migrate existing apps when you can so you are ready when 1.0 becomes stable. Deploy the Worker package and container image from the <strong>same</strong> <code>@next</code> line.</p>
<p>Coding agents: install <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a> (<a href="/agent-setup/">Agent setup</a>). Use <strong><code>sandbox-next</code></strong> for <code>@next</code> (recommended for new projects), <strong><code>sandbox-stable</code></strong> for the current stable package, and <strong><code>sandbox-migrate-to-next</code></strong> when you are ready to port. Stable-package deprecated-API cleanup is in the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation guide</a>.</p>
<p>The main <a href="/sandbox/">Sandbox documentation</a> still describes today's stable package. Preview docs:</p>
<ul>
<li><a href="/sandbox/1-0-preview/">1.0 preview</a></li>
<li><a href="/sandbox/1-0-preview/get-started/">Get started</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Processes</a> · <a href="/sandbox/1-0-preview/terminals/">Terminals</a> · <a href="/sandbox/1-0-preview/errors/">Errors</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
</ul>
<p>The self-deployed Sandbox bridge is not currently part of this preview. We are working on bringing it in line with the latest code. Until then, use the <a href="/sandbox/bridge/">stable bridge</a> with the matching stable package and container image.</p>
<h4 id="2026-08-07-sandbox-sdk-1-0-preview-timeline-for-1-0">Timeline for 1.0</h4>
<p>Further Cloudflare Containers features will let us keep reducing the size of the Sandbox SDK. We aim to ship Sandbox SDK 1.0 once those are in. In the meantime we continue to support and maintain the 1.0 preview (<code>@next</code>) alongside the current stable release.</p>


<h2 id="ai-search-makes-it-easier-to-build-a-search-engine-for-your-data"><a href="/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/">AI Search makes it easier to build a search engine for your data</a></h2>
<p><em>2026-08-06</em></p>
<p><a href="/ai-search/">AI Search</a> gets you from a data source to a working search endpoint quickly. This release adds what you need to put that endpoint in front of real users: your own domain, authentication, and one endpoint across several instances. It also adds crawling for sites without a complete sitemap, so your index covers everything you want it to find.</p>
<p>Each of the following is a new option. The previous behavior is still the default, so nothing changes until you change it.</p>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-serve-search-from-your-own-domain">Serve search from your own domain</h4>
<p>A <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a> is a URL that a site or app can query directly, with no authentication in front of it. By default that URL is a generated hostname on <code>search.ai.cloudflare.com</code>. You can now serve the same endpoint from a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a>, a hostname in a zone that you own:</p>
<pre><code class="language-txt">https://search.example.com/search&#10;</code></pre>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-restrict-who-can-query-your-content">Restrict who can query your content</h4>
<p>Once your endpoint is on your own domain, you can put <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a> in front of it. For example, you usually want to give <code>/mcp</code> to specific agents rather than to anyone who finds the URL. Agents authenticate with an Access service token, and people who open the endpoint in a browser sign in through your identity provider.</p>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-search-several-instances-from-one-url">Search several instances from one URL</h4>
<p>A namespace can expose its own <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">public endpoint</a> with <code>/search</code>, <code>/chat/completions</code>, and <code>/mcp</code> paths that fan out across the instances you choose:</p>
<pre><code class="language-bash">curl https://ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com/search \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;content&quot;: &quot;How do I configure AI Search?&quot;, &quot;role&quot;: &quot;user&quot; }],&#10;    &quot;ai_search_options&quot;: { &quot;instance_ids&quot;: [&quot;docs&quot;, &quot;support&quot;] }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-index-your-sites-without-a-sitemap">Index your sites without a sitemap</h4>
<p>Website data sources support a new <code>discover</code> <a href="/ai-search/configuration/data-source/website/parse-types/">parse type</a>. It starts at the source URL and collects pages from both your sitemaps and the links it finds while crawling:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source&quot;: &quot;example.com&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_type&quot;: &quot;discover&quot;,&#10;        &quot;discover_options&quot;: { &quot;source&quot;: &quot;links&quot;, &quot;limit&quot;: 5000, &quot;depth&quot;: 3 }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>To learn more, refer to the <a href="/ai-search/">AI Search documentation</a>.</p>


<h2 id="introducing-kitesurf-an-agent-first-browser-on-browser-run"><a href="/changelog/post/2026-08-06-kitesurf/">Introducing Kitesurf, an agent-first browser on Browser Run</a></h2>
<p><em>2026-08-06</em></p>
<p><a href="/browser-run/kitesurf/">Kitesurf</a> is Cloudflare's new stateless, highly scalable browser that runs entirely on top of <a href="/workers/">Workers</a> and is designed for AI agents. It is available for free while in beta.</p>
<p>Compared to Chromium, Kitesurf uses 3–7× less CPU and memory for common agentic tasks like screenshots and HTML extraction, so you can run more sessions and scale better for bursty, AI-driven workloads.</p>
<p>Your existing clients already work. To opt in, add the <code>browser=kitesurf</code> parameter to any Browser Run <a href="/browser-run/cdp/">CDP</a> or <a href="/browser-run/quick-actions/">Quick Action</a> endpoint:</p>
<pre><code class="language-sh">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-run/screenshot?browser=kitesurf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<p>You can also explore Kitesurf without writing any code in the <a href="https://kitesurf.cloudflare.app/">public playground</a>.</p>
<p>For more information, refer to the <a href="/browser-run/kitesurf/">Kitesurf documentation</a> and the <a href="https://blog.cloudflare.com/kitesurf">blog announcement</a>.</p>


<h2 id="track-ai-spend-and-catch-anomalous-usage-with-user-insights"><a href="/changelog/post/2026-08-05-user-insights/">Track AI spend and catch anomalous usage with User Insights</a></h2>
<p><em>2026-08-05T12:00:00-08:00</em></p>
<p>AI Gateway now includes User Insights, a dashboard that gives you two things at once: clear visibility into how much your organization spends on AI, and a security signal that surfaces users whose usage suddenly looks abnormal. It works on the traffic already flowing through your gateway, so there is no additional setup.</p>
<p>On the spend side, User Insights shows organization-wide totals for cost, requests, tokens, and adoption, and lets you drill into an individual user to see their spend, top models and providers, cache hit rate, and more. To attribute usage to individual users, add a user identifier with custom metadata or put your gateway behind Cloudflare Access.</p>
<p>On the security side, User Insights baselines each user's normal usage from their 95th percentile (p95) session cost over the last 30 days, then flags sessions that exceed both that baseline and an organization-level threshold. A sudden jump above a user's own pattern is often the first sign of a compromised credential or a misbehaving agent, so you can investigate before it shows up on your bill.</p>
<p>User Insights is available to all AI Gateway customers at no additional cost.</p>


<h2 id="identity-aware-controls-are-now-available-in-ai-gateway"><a href="/changelog/post/2026-08-05-access-user-id-metadata/">Identity-aware controls are now available in AI Gateway</a></h2>
<p><em>2026-08-05</em></p>
<p>AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:</p>
<ul>
<li><strong>Protect your gateway endpoint.</strong> Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.</li>
<li><strong>Identity-aware controls.</strong> When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.</li>
</ul>
<p>With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as <code>cf.user_id</code>.</p>
<p>For setup instructions, refer to <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>.</p>


<h2 id="agent-traces-for-think-flue-and-ai-sdk-instrumented-by-agents-sdk"><a href="/changelog/post/2026-08-04-agent-tracing/">Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK</a></h2>
<p><em>2026-08-04</em></p>
<p>Agent tracing is now available for applications built with the Agents SDK. Traces show each agent turn alongside model calls, tool runs, approvals, token usage, and Workers runtime operations.</p>
<p>Turn on Workers tracing in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17683.md")</div>
<p>Think and Flue applications emit agent traces automatically. For direct AI SDK calls, wrap the AI SDK namespace once. <code>wrapAISDK()</code> supports AI SDK v6 and v7. This AI SDK v7 example also supplies the agent identity:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17684.md")</div>
<p>Message and tool payload recording is off by default. Turn it on only when the payloads are safe to store:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17685.md")</div>
<p>Open the <a href="https://dash.cloudflare.com/?to=/:account/agents"><strong>Agents</strong> tab</a> in the Cloudflare dashboard to inspect sessions, replay conversations, and view trace waterfalls. For advanced setup, privacy controls, and trace structure, refer to <a href="/agents/runtime/operations/observability/tracing/">Agent tracing</a>.</p>


<h2 id="build-and-deploy-artifacts-repos-on-every-push"><a href="/changelog/post/2026-08-04-build-and-deploy-on-push/">Build and deploy Artifacts repos on every push</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now run your CI/CD pipeline on your <a href="/artifacts/">Artifacts</a> repo by defining a CI <a href="/workflows/">Workflow</a> with the <a href="https://github.com/cloudflare/ci">CI SDK</a>, automatically triggered on Artifacts push events.</p>
<p>This allows you to:</p>
<ul>
<li>Automatically build and deploy application code stored in Artifacts.</li>
<li>Run linting, type checking, tests, and other checks on every push.</li>
<li>Reuse dependencies when the lockfile (i.e. <code>pnpm-lock.yaml</code>) has not changed.</li>
<li>Stop deployment when a check or build fails.</li>
<li>Restrict API token access to the deployment step.</li>
<li>Deploy the output to a <a href="/workers/">Worker</a> or a <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> User Worker.</li>
</ul>
<p>Define your CI steps with <code>@cloudflare/ci</code>. Each <code>ci.runner()</code> spins up an isolated sandbox, and the <code>cache</code> option reuses installed dependencies across each sandboxed step in your CI job.</p>
<p>Point <code>cache.inputs</code> at your lockfile (i.e. <code>pnpm-lock.yaml</code>, <code>bun.lock</code>), and the install step only runs again when that lockfile changes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17690.md")</div>
<p>To start the Workflow automatically after each push, add a <code>cf.artifacts.repo.pushed</code> trigger to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17691.md")</div>
<p>To learn more, refer to <a href="/artifacts/guides/build-and-deploy-on-push/">Build and deploy Artifacts repos</a>.</p>


<h2 id="vectorize-indexes-now-support-up-to-20-million-vectors"><a href="/changelog/post/2026-08-04-index-capacity-20-million/">Vectorize indexes now support up to 20 million vectors</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now store up to 20 million vectors in a single Vectorize index, doubling the previous limit of 10 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>


<h2 id="ai-agents-can-debug-workers-with-local-tracing"><a href="/changelog/post/2026-08-04-local-tracing/">AI agents can debug Workers with local tracing</a></h2>
<p><em>2026-08-04</em></p>
<p><code>wrangler dev</code> and <code>vite dev</code> automatically capture structured OpenTelemetry traces and correlated console logs during local Worker invocations.</p>
<h4 id="2026-08-04-local-tracing-debug-with-ai-agents">Debug with AI agents</h4>
<p>When the tooling detects an AI agent session, it prints a terminal hint pointing to the <a href="/workers/local-development/local-explorer/#api">Local Explorer API</a> at <code>/cdn-cgi/local/explorer/api</code>. The API serves an OpenAPI schema and exposes a read-only observability query endpoint for discovering telemetry, querying traces and logs, and inspecting binding state.</p>
<p>The agent can identify the exact failing operation, fix the code, rerun the request, and verify the result. This debug loop requires no deployment or temporary logs.</p>
<h4 id="2026-08-04-local-tracing-inspect-traces-in-local-explorer">Inspect traces in Local Explorer</h4>
<p>Humans can inspect the same <a href="/workers/observability/traces/">traces</a> and correlated console logs in the Local Explorer browser UI. Each trace shows spans, timing, attributes, and errors.</p>
<p><img src="/assets/upstream/images/workers/observability/local-trace-failed-request.png" alt="Local Explorer showing a failed Worker trace with spans, timing, and errors" /></p>
<p>Automatic spans cover handler calls, outbound <code>fetch()</code> calls, and binding calls. Custom spans appear alongside these automatic spans.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>


<h2 id="node-js-compatibility-is-now-enabled-by-default"><a href="/changelog/post/2026-08-04-nodejs-compat-default/">Node.js compatibility is now enabled by default</a></h2>
<p><em>2026-08-04</em></p>
<p>Workers now enable the <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> compatibility
flags by default for <a href="/workers/configuration/compatibility-dates/">compatibility dates</a>
of <code>2026-08-04</code> or later. These flags are not used for these compatibility
dates because the compatibility date enables the same behavior.</p>
<p>This means all <a href="/workers/runtime-apis/nodejs/">Node.js built-in APIs</a> supported
by the Workers runtime are available by default, including <code>node:crypto</code>,
<code>node:buffer</code>, <code>node:stream</code>, <code>node:net</code>, <code>node:dns</code>, <code>node:fs</code>, <code>node:http</code>,
and more. npm packages that depend on these APIs will work without additional
configuration.</p>
<p>Workers using an earlier compatibility date are not affected. They can still
opt in by adding <code>nodejs_compat</code> to <code>compatibility_flags</code>.</p>
<p>New projects do not need to add either flag. Existing projects can update their
compatibility date without removing them. Wrangler, Miniflare, the Cloudflare
Vite plugin, and Vitest Pool Workers ignore these redundant flags when starting
the runtime.</p>
<p>To turn off Node.js compatibility completely, remove any <code>nodejs_compat</code> and
<code>nodejs_compat_v2</code> flags. Then add both of the following flags:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17813.md")</div>
<p>For more information, refer to the <a href="/workers/runtime-apis/nodejs/">Node.js compatibility documentation</a>.</p>


<h2 id="log-in-to-wrangler-without-a-local-callback-server"><a href="/changelog/post/2026-08-04-wrangler-login-device-flow/">Log in to Wrangler without a local callback server</a></h2>
<p><em>2026-08-04</em></p>
<p><code>wrangler login</code> now supports the <a href="https://www.rfc-editor.org/rfc/rfc8628">OAuth 2.0 Device Authorization Grant</a>. Pass <code>--device</code> to authenticate without starting a temporary callback server on <code>localhost:8976</code>:</p>
<pre><code class="language-sh">npx wrangler login --device&#10;</code></pre>
<p>Wrangler prints a verification URL and a short user code, opens the URL in your default browser with the code already filled in, and polls Cloudflare for an access token while you approve the request:</p>
<pre><code class="language-sh"> ⛅️ wrangler 4.119.0&#10;────────────────────&#10;Attempting to login via OAuth Device Authorization Grant...&#10;To authorize Wrangler, please visit:&#10;&#10;  https://dash.cloudflare.com/oauth2/device&#10;&#10;and enter the code:&#10;&#10;  jPqK6Qvs&#10;&#10;You have 5 minutes to approve this request.&#10;&#10;Opening a link in your default browser: https://dash.cloudflare.com/oauth2/device?user_code=jPqK6Qvs&#10;Successfully logged in.&#10;</code></pre>
<p>The default login flow needs your browser to reach <code>localhost:8976</code>, which is not always possible from containers, remote SSH sessions, or GitHub Codespaces. Previously these environments required forwarding ports or fetching the callback URL with <code>curl</code> from a second terminal session. Because <code>--device</code> has no callback server, those workarounds are no longer necessary.</p>
<p>Since the plain verification URL and user code are both printed to the terminal, you can also approve the request from a phone or another machine. Pass <code>--browser=false</code> to stop Wrangler from opening a browser at all.</p>
<p>Available in Wrangler version 4.119.0 or later. For more information, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a>.</p>


<h2 id="preview-cloudflare-computer-agent-runtime"><a href="/changelog/post/2026-08-03-cloudflare-computer/">Preview: @cloudflare/computer agent runtime</a></h2>
<p><em>2026-08-03</em></p>
<p>We're releasing an early preview of <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code></a>, an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.</p>
<p><code>@cloudflare/computer</code> provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.</p>
<p>Install the package via npm:</p>
<pre><code class="language-sh">npm install @cloudflare/computer&#10;</code></pre>
<p>Instantiate a <code>Workspace</code> inside any Durable Object to give your agent a filesystem and execution runtime:</p>
<pre><code class="language-ts">import { Workspace } from &quot;@cloudflare/computer&quot;;&#10;&#10;export class Agent {&#10;	workspace = new Workspace({&#10;		storage: this.ctx.storage,&#10;	});&#10;}&#10;</code></pre>
<p>Several execution backends are included or you can write your own:</p>
<ul>
<li><strong>Isolate runtime</strong> — fast, horizontally scalable execution via <code>just-bash</code> and Dynamic Workers, ideal for file manipulation and data processing.</li>
<li><strong>Container runtime</strong> — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.</li>
</ul>
<p>The AI SDK-compatible toolkit provides common agent tools (<code>read</code>, <code>write</code>, <code>edit</code>, <code>ls</code>, <code>exec</code>) and guides the model to choose the appropriate backend for each task.</p>
<p>For more examples, including a step-by-step tutorial, visit the <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code> repository</a>.</p>
<p>Read the announcement blog post for more details: <a href="https://blog.cloudflare.com/cloudflare-computer/">Your agent needs a computer, not a container</a>.</p>


<h2 id="billing-is-now-enabled-for-pipelines"><a href="/changelog/post/2026-08-03-pipelines-billing-enabled/">Billing is now enabled for Pipelines</a></h2>
<p><em>2026-08-03</em></p>
<p>Billing is now enabled for <a href="/pipelines/">Cloudflare Pipelines</a> on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.</p>
<p>Pipelines charges based on two usage dimensions. Ingress into a Pipeline stream remains free regardless of volume:</p>
<ul>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks (egress)</strong>: $0.03 / GB for JSON output, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Paid plans include 50 GB / month for both SQL transforms and sinks. Standard <a href="/r2/pricing/">R2 storage and operations</a> charges apply for data written to R2 buckets, and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply when writing to Iceberg tables.</p>
<p>For example, a pipeline that ingests 500 GB of event data per month, uses a SQL transform to filter and reshape it, and writes 300 GB to an R2 Data Catalog Iceberg table would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Streams</td>
<td>500 GB</td>
<td>Unlimited</td>
<td>0 GB</td>
<td>$0.00</td>
</tr>
<tr>
<td>SQL transforms</td>
<td>500 GB</td>
<td>50 GB</td>
<td>450 GB</td>
<td>$18.00</td>
</tr>
<tr>
<td>Sinks (Iceberg)</td>
<td>300 GB</td>
<td>50 GB</td>
<td>250 GB</td>
<td>$15.00</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$33.00</strong></td>
</tr>
</tbody>
</table>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>


<h2 id="billing-is-now-enabled-for-r2-data-catalog"><a href="/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/">Billing is now enabled for R2 Data Catalog</a></h2>
<p><em>2026-08-03</em></p>
<p>Billing is now enabled for <a href="/r2-data-catalog/">R2 Data Catalog</a> on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.</p>
<p>R2 Data Catalog charges based on two dimensions, in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>:</p>
<ul>
<li><strong>Catalog operations</strong>: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction</strong>: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a> is turned on for a table.</li>
</ul>
<p>Each dimension includes a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.</p>
<p>For example, a single Iceberg table with 50 GB of data, 500,000 catalog operations per month, and compaction turned on that processes 20 GB across 200,000 files would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Catalog operations</td>
<td>500,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Compaction (data processed)</td>
<td>20 GB</td>
<td>10 GB</td>
<td>10 GB</td>
<td>$0.05</td>
</tr>
<tr>
<td>Compaction (objects)</td>
<td>200,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td><strong>Total (Data Catalog)</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$0.05</strong></td>
</tr>
</tbody>
</table>
<p>Standard R2 storage charges ($0.015 / GB-month) apply separately for the 50 GB of data stored.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>


<h2 id="billing-is-now-enabled-for-r2-sql"><a href="/changelog/post/2026-08-03-r2-sql-billing-enabled/">Billing is now enabled for R2 SQL</a></h2>
<p><em>2026-08-03</em></p>
<p>Billing is now enabled for <a href="/r2-sql/">R2 SQL</a> on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.</p>
<p>R2 SQL charges based on a single dimension:</p>
<ul>
<li><strong>Data scanned</strong>: $0.0025 / GB ($2.50 / TB) of compressed data read from R2 to execute your query.</li>
</ul>
<p>All plans include 10 GB of data scanned per month. Each query is billed for a minimum of 10 MB of data scanned. R2 SQL pricing is additive to standard <a href="/r2/pricing/">R2 storage and operations</a> and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges. R2 does not charge for egress, so there is no additional data transfer cost.</p>
<p>For example, a user who stores 500 GB of Parquet data in R2 Data Catalog and runs queries that scan a total of 50 GB of compressed data during the month would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>R2 storage</td>
<td>500 GB-month</td>
<td>10 GB-month</td>
<td>490 GB-month</td>
<td>$7.35</td>
</tr>
<tr>
<td>R2 SQL (data scanned)</td>
<td>50 GB</td>
<td>10 GB</td>
<td>40 GB</td>
<td>$0.10</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$7.45</strong></td>
</tr>
</tbody>
</table>
<p>For full pricing details and billing examples, refer to <a href="/r2-sql/platform/pricing/">R2 SQL pricing</a>.</p>


<h2 id="python-and-javascript-workers-can-now-call-each-other-via-rpc"><a href="/changelog/post/2026-08-03-python-javascript-rpc/">Python and JavaScript Workers can now call each other via RPC</a></h2>
<p><em>2026-08-03</em></p>
<p>You can now call methods between Python and JavaScript Workers using <a href="/workers/runtime-apis/rpc/">Workers RPC</a>. This works through <a href="/workers/runtime-apis/bindings/service-bindings/rpc/">Service bindings</a> without extra dependencies, schema definitions, or serialization code.</p>
<p>Cross-language RPC calls behave like ordinary function calls. Exceptions propagate to the call site. You can pass <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured cloneable types</a> as parameters or return values, and Pyodide Foreign Function Interface (FFI) automatically converts types between languages.</p>
<h4 id="2026-08-03-python-javascript-rpc-call-a-typescript-worker-from-python">Call a TypeScript Worker from Python</h4>
<p>Define a method in a TypeScript Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17809.md")</div>
<p>Call it from a Python Worker through a Service binding:</p>
<pre><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;	async def fetch(self, request):&#10;		rpc = self.env.RPC&#10;		result = await rpc.add(42, 144)&#10;		return Response.json({&quot;result&quot;: result})&#10;</code></pre>
<p>Configure the Service binding in the Python Worker's Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17810.md")</div>
<h4 id="2026-08-03-python-javascript-rpc-call-a-python-worker-from-javascript">Call a Python Worker from JavaScript</h4>
<p>Define a method in a Python Worker:</p>
<pre><code class="language-python">from workers import WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;	async def highlight_code(self, code: str, language: str) -&gt; dict:&#10;		from pygments.formatters import HtmlFormatter&#10;		from pygments import highlight&#10;		from pygments.lexers import get_lexer_by_name&#10;&#10;		lexer = get_lexer_by_name(language, stripall=True)&#10;		formatter = HtmlFormatter(linenos=True, cssclass=&quot;highlight&quot;, style=&quot;monokai&quot;)&#10;		highlighted_html = highlight(code, lexer, formatter)&#10;		css = formatter.get_style_defs(&quot;.highlight&quot;)&#10;&#10;		return {&#10;			&quot;html&quot;: highlighted_html,&#10;			&quot;css&quot;: css&#10;		}&#10;</code></pre>
<p>Call it from a JavaScript Worker through a Service binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17811.md")</div>
<p>Configure the Service binding in the JavaScript Worker's Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17812.md")</div>
<p>For more details on the announcement, read the <a href="https://blog.cloudflare.com/python-workers-rpc/">blog post</a>.</p>
<p>For more information, refer to the <a href="/workers/runtime-apis/rpc/">Workers RPC documentation</a> and the <a href="/workers/languages/python/">Python Workers overview</a>.</p>


<h2 id="browser-run-adds-a-playground-to-the-cloudflare-dashboard"><a href="/changelog/post/2026-07-31-br-dashboard-playground/">Browser Run adds a Playground to the Cloudflare dashboard</a></h2>
<p><em>2026-07-31</em></p>
<p><a href="/browser-run/">Browser Run</a> now includes a Playground in the Cloudflare dashboard. Use it to try Quick Actions against a live browser without creating a Worker, installing an SDK, or deploying code first.</p>
<p>The Playground helps you test a target URL or raw HTML input, tune viewport and page-load settings, preview the output, and copy working code for the same request.</p>
<p><img src="/images/browser-run/playground.png" alt="Browser Run Playground in the Cloudflare dashboard showing a generated screenshot preview and output settings" /></p>
<p>With the Playground, you can:</p>
<ul>
<li>Capture visuals as <a href="/browser-run/quick-actions/screenshot-endpoint/">screenshots</a> or <a href="/browser-run/quick-actions/pdf-endpoint/">PDFs</a>.</li>
<li>Generate multiple output formats in one request with the <a href="/browser-run/quick-actions/snapshot/">snapshot endpoint</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/content-endpoint/">HTML</a>, <a href="/browser-run/quick-actions/markdown-endpoint/">Markdown</a>, <a href="/browser-run/quick-actions/links-endpoint/">links</a>, or <a href="/browser-run/quick-actions/scrape-endpoint/">scraped data</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/json-endpoint/">structured data with AI</a> using a prompt and optional JSON Schema.</li>
</ul>
<p>You can also configure desktop, laptop, tablet, mobile, or custom viewport sizes, set browser scale, choose page-load conditions, set timeouts, and wait for selectors before running a request.</p>
<p>Select <strong>Show Code</strong> to generate the same request as cURL, TypeScript SDK, Python, or Workers Binding code. For example, a screenshot request can be copied as a Workers Binding call:</p>
<pre><code class="language-ts">interface Env {&#10;	BROWSER: BrowserRun;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		return await env.BROWSER.quickAction(&quot;screenshot&quot;, {&#10;			url: &quot;https://developers.cloudflare.com&quot;,&#10;			viewport: {&#10;				width: 1920,&#10;				height: 1080,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Requests made in the Playground incur <a href="/browser-run/pricing/">Browser Run charges</a>. AI extraction also incurs Workers AI charges.</p>
<p>To try the Playground, go to <strong>Browser Run</strong> in the Cloudflare dashboard and select <strong>Playground</strong>.</p>
<div class="nb-dash-button"></div>
<p>For more information, refer to the <a href="/browser-run/quick-actions/">Quick Actions documentation</a>.</p>


<h2 id="rotate-stream-broadcast-keys-for-live-inputs"><a href="/changelog/post/2026-07-30-rotate-stream-broadcast-keys/">Rotate Stream broadcast keys for live inputs</a></h2>
<p><em>2026-07-31</em></p>
<p>You can now rotate the broadcast credentials for a Stream live input without changing the live input identifier.</p>
<p>Use key rotation when live input credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys revokes the old credentials, disconnects broadcasts using stale credentials, and returns refreshed credentials in the API response.</p>
<p>To rotate keys for a live input, make a <code>POST</code> request to the <code>rotate_keys</code> endpoint:</p>
<pre><code class="language-bash">curl --request POST \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/rotate_keys \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Live input responses now also include <code>keysRotatedAt</code>, which indicates when the live input keys were last rotated. This field is omitted for live inputs whose keys have never been rotated.</p>
<p>For endpoint details, refer to <a href="/api/resources/stream/subresources/live_inputs/methods/rotate_keys/">Rotate keys for a live input</a>. For usage guidance, refer to <a href="/stream/stream-live/start-stream-live/#manage-live-inputs">Manage live inputs</a>.</p>


<h2 id="inspect-worker-startup-performance-with-wrangler"><a href="/changelog/post/2026-07-31-wrangler-startup-profile-summary/">Inspect Worker startup performance with Wrangler</a></h2>
<p><em>2026-07-31</em></p>
<p><code>wrangler check startup</code> now reports your Worker's raw and compressed bundle sizes. It also summarizes local CPU activity during startup directly in your terminal.</p>
<p>Large bundles and costly startup work can introduce cold-start latency, so use this command to find code and large dependencies that slow your Worker before it handles requests.</p>
<p>The summary includes sampled, active, garbage collection, and idle time. Wrangler continues to save a <code>.cpuprofile</code> file for detailed flamegraph analysis in Chrome DevTools or VS Code.</p>
<pre><code class="language-bash">⛅️ wrangler 4.116.0&#10;───────────────────────────────────────────────&#10;├ Building your Worker&#10;│ Worker Built! 🎉&#10;│&#10;├ Analysing&#10;│ Startup phase analysed&#10;│&#10;│ Bundle: 7171.25 KiB / gzip: 2197.00 KiB&#10;│&#10;│ Local startup profile:&#10;│   Profile window: 70.3 ms&#10;│   Sampled time: 70.3 ms&#10;│   Active: 38.5 ms (including 3.7 ms garbage collection)&#10;│   Idle: 31.8 ms&#10;│   Samples: 36&#10;│&#10;│ CPU Profile has been written to worker-startup.cpuprofile. Load it into the Chrome DevTools profiler (or directly in VSCode) to view a flamegraph.&#10;│&#10;│ Note that the CPU Profile was measured on your Worker running locally on your machine, which has a different CPU than when your Worker runs on Cloudflare.&#10;│&#10;│ As such, CPU Profile can be used to understand where time is spent at startup, but the overall startup time in the profile should not be expected to exactly match what your Worker&#x27;s startup time will be when deploying to Cloudflare.&#10;</code></pre>
<p>The profile runs locally, so its duration will differ from startup time on Cloudflare. For authoritative startup time, deploy your Worker or upload a version.</p>
<p>Available in Wrangler version 4.116.0 or later. For more information, refer to <a href="/workers/wrangler/commands/workers/#startup"><code>wrangler check startup</code></a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/2/">Previous</a><span>Page 3 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/4/">Next</a></nav>
