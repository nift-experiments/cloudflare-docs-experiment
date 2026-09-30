---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers/5/
  description: '2026-02-11'
  full_title: workers changelog - page 5 | Cloudflare Docs
  head_html: <title>workers changelog - page 5 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-02-11"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers/5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers changelog - page 5"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-02-11"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers/5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers/5/#page","headline":"workers changelog - page 5 | Cloudflare Docs","description":"2026-02-11","url":"https://developers.cloudflare.com/changelog/product/workers/5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers/5/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="improved-react-server-components-support-in-the-cloudflare-vite-plugin"><a href="/changelog/post/2026-02-11-vite-plugin-child-environments/">Improved React Server Components support in the Cloudflare Vite plugin</a></h2>
<p><em>2026-02-11</em></p>
<p>The Cloudflare Vite plugin now integrates seamlessly <a href="https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc">@vitejs/plugin-rsc</a>, the official Vite plugin for <a href="https://react.dev/reference/rsc/server-components">React Server Components</a>.</p>
<p>A <code>childEnvironments</code> option has been added to the plugin config to enable using multiple environments within a single Worker.
The parent environment can then import modules from a child environment in order to access a separate module graph.
For a typical RSC use case, the plugin might be configured as in the following example:</p>
<pre tabindex="0"><code class="language-ts">export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			viteEnvironment: {&#10;				name: &quot;rsc&quot;,&#10;				childEnvironments: [&quot;ssr&quot;],&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p><code>@vitejs/plugin-rsc</code> provides the lower level functionality that frameworks, such as <a href="https://reactrouter.com/how-to/react-server-components">React Router</a>, build upon.
The GitHub repository includes a <a href="https://github.com/vitejs/vite-plugin-react/tree/f066114c3e6bf18f5209ff3d3ef6bf1ab46d3866/packages/plugin-rsc/examples/starter-cf-single">basic Cloudflare example</a>.</p>


<h2 id="agents-sdk-v0-4-0-readonly-connections-mcp-security-improvements-x402-v2-migration-and-custom-mcp-oauth-providers"><a href="/changelog/post/2026-02-09-agents-sdk-v0.4.0/">Agents SDK v0.4.0: Readonly connections, MCP security improvements, x402 v2 migration, and custom MCP OAuth providers</a></h2>
<p><em>2026-02-09</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings readonly connections, MCP protocol and security improvements, x402 payment protocol v2 migration, and the ability to customize OAuth for MCP server connections.</p>
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


<h2 id="visualize-data-share-links-and-create-exports-with-the-new-workers-observability-dashboard"><a href="/changelog/post/2026-02-06-observability-ui-refresh/">Visualize data, share links, and create exports with the new Workers Observability dashboard</a></h2>
<p><em>2026-02-06</em></p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> has some major updates to make it easier to debug your application's issues and share findings with your team.</p>
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


<h2 id="visualize-your-workflows-in-the-cloudflare-dashboard"><a href="/changelog/post/2026-02-03-workflows-visualizer/">Visualize your Workflows in the Cloudflare dashboard</a></h2>
<p><em>2026-02-04</em></p>
<p>Cloudflare Workflows now automatically generates visual diagrams from your code</p>
<p>Your Workflow is parsed to provide a visual map of the Workflow structure, allowing you to:</p>
<ul>
<li>Understand how steps connect and execute</li>
<li>Visualize loops and nested logic</li>
<li>Follow branching paths for conditional logic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workflows/2026-02-03-workflows-diagram.png" alt="Example diagram" /></p>
<p>You can collapse loops and nested logic to see the high-level flow, or expand them to see every step.</p>
<p>Workflow diagrams are available in beta for all JavaScript and TypeScript Workflows. Find your Workflows in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a> to see their diagrams.</p>


<h2 id="new-placement-hints-for-workers"><a href="/changelog/post/2026-01-22-explicit-placement-hints/">New Placement Hints for Workers</a></h2>
<p><em>2026-01-22</em></p>
<p>You can now configure Workers to run close to infrastructure in legacy cloud regions to minimize latency to existing services and databases. This is most useful when your Worker makes multiple round trips.</p>
<p>To <a href="/workers/configuration/placement/#configure-explicit-placement-hints">set a placement hint</a>, set the <code>placement.region</code> property in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17793.md")</div>
<p>Placement hints support Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure region identifiers. Workers run in the <a href="https://www.cloudflare.com/network/">Cloudflare data center</a> with the lowest latency to the specified cloud region.</p>
<p>If your existing infrastructure is not in these cloud providers, expose it to placement probes with <code>placement.host</code> for layer 4 checks or <code>placement.hostname</code> for layer 7 checks. These probes are designed to locate single-homed infrastructure and are not suitable for anycasted or multicasted resources.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17794.md")</div>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17795.md")</div>
<p>This is an extension of <a href="/workers/configuration/placement/#enable-smart-placement">Smart Placement</a>, which automatically places your Workers closer to back-end APIs based on measured latency. When you do not know the location of your back-end APIs or have multiple back-end APIs, set <code>mode: &quot;smart&quot;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17796.md")</div>


<h2 id="use-auxiliary-workers-alongside-full-stack-frameworks"><a href="/changelog/post/2026-01-20-auxiliary-workers/">Use auxiliary Workers alongside full-stack frameworks</a></h2>
<p><em>2026-01-20</em></p>
<p>Auxiliary Workers are now fully supported when using full-stack frameworks, such as <a href="/workers/framework-guides/web-apps/react-router/">React Router</a> and <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start</a>, that integrate with the <a href="/workers/vite-plugin/reference/api/">Cloudflare Vite plugin</a>.
They are included alongside the framework's build output in the build output directory.
Note that this feature requires Vite 7 or above.</p>
<p>Auxiliary Workers are additional Workers that can be called via <a href="/workers/runtime-apis/bindings/service-bindings/">service bindings</a> from your main (entry) Worker.
They are defined in the plugin config, as in the example below:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		tanstackStart(),&#10;		cloudflare({&#10;			viteEnvironment: { name: &quot;ssr&quot; },&#10;			auxiliaryWorkers: [{ configPath: &quot;./wrangler.aux.jsonc&quot; }],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>See the Vite plugin <a href="/workers/vite-plugin/reference/api/">API docs</a> for more info.</p>


<h2 id="import-sql-files-as-additional-modules-by-default"><a href="/changelog/post/2026-01-20-sql-module-rule/">Import SQL files as additional modules by default</a></h2>
<p><em>2026-01-20</em></p>
<p>The <code>.sql</code> file extension is now automatically configured to be importable in your Worker code when using <a href="/workers/wrangler/bundling/#including-non-javascript-modules">Wrangler</a> or the <a href="/workers/vite-plugin/reference/non-javascript-modules/">Cloudflare Vite plugin</a>.
This is particular useful for importing migrations in Durable Objects and means you no longer need to configure custom rules when using <a href="https://orm.drizzle.team/docs/connect-cloudflare-do">Drizzle</a>.</p>
<p>SQL files are imported as JavaScript strings:</p>
<pre tabindex="0"><code class="language-ts">// `example` will be a JavaScript string&#10;import example from &quot;./example.sql&quot;;&#10;</code></pre>


<h2 id="wrangler-types-now-generates-types-for-all-environments"><a href="/changelog/post/2026-01-13-wrangler-types-multi-environment/">`wrangler types` now generates types for all environments</a></h2>
<p><em>2026-01-13</em></p>
<p>The <code>wrangler types</code> command now generates TypeScript types for bindings from <strong>all environments</strong> defined in your Wrangler configuration file by default.</p>
<p>Previously, <code>wrangler types</code> only generated types for bindings in the top-level configuration (or a single environment when using the <code>--env</code> flag). This meant that if you had environment-specific bindings — for example, a KV namespace only in production or an R2 bucket only in staging — those bindings would be missing from your generated types, causing TypeScript errors when accessing them.</p>
<p>Now, running <code>wrangler types</code> collects bindings from all environments and includes them in the generated <code>Env</code> type. This ensures your types are complete regardless of which environment you deploy to.</p>
<h4 id="2026-01-13-wrangler-types-multi-environment-generating-types-for-a-specific-environment">Generating types for a specific environment</h4>
<p>If you want the previous behavior of generating types for only a specific environment, you can use the <code>--env</code> flag:</p>
<pre tabindex="0"><code class="language-sh">wrangler types --env production&#10;</code></pre>
<p>Learn more about <a href="/workers/wrangler/commands/general/#types">generating types for your Worker</a> in the Wrangler documentation.</p>


<h2 id="validate-your-generated-types-with-wrangler-types-check"><a href="/changelog/post/2026-01-11-wrangler-types-check/">Validate your generated types with `wrangler types --check`</a></h2>
<p><em>2026-01-12</em></p>
<p>Wrangler now supports a <code>--check</code> flag for the <code>wrangler types</code> command. This flag validates that your generated types are up to date without writing any changes to disk.</p>
<p>This is useful in CI/CD pipelines where you want to ensure that developers have regenerated their types after making changes to their Wrangler configuration. If the types are out of date, the command will exit with a non-zero status code.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler types --check&#10;</code></pre>
<p>If your types are up to date, the command will succeed silently. If they are out of date, you'll see an error message indicating which files need to be regenerated.</p>
<p>For more information, see the <a href="/workers/wrangler/commands/general/#types">Wrangler types documentation</a>.</p>


<h2 id="get-notified-when-your-workers-builds-succeed-or-fail"><a href="/changelog/post/2025-12-11-builds-event-subscriptions/">Get notified when your Workers builds succeed or fail</a></h2>
<p><em>2026-01-09</em></p>
<p>You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using <a href="/queues/event-subscriptions/">Event Subscriptions</a>.</p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> publishes events to a <a href="/queues/">Queue</a> that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.</p>
<p>You can deploy <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template">this Worker</a> to your own Cloudflare account to send build notifications to Slack:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The template includes:</p>
<ul>
<li>Build status with Preview/Live URLs for successful deployments</li>
<li>Inline error messages for failed builds</li>
<li>Branch, commit hash, and author name</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/builds-notifications-slack.png" alt="Slack notifications showing build events" /></p>
<p>For setup instructions, refer to the <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme">template README</a> or the <a href="/queues/event-subscriptions/manage-event-subscriptions/">Event Subscriptions documentation</a>.</p>


<h2 id="shell-tab-completions-for-wrangler-cli"><a href="/changelog/post/2026-01-09-wrangler-tab-completion/">Shell tab completions for Wrangler CLI</a></h2>
<p><em>2026-01-09</em></p>
<p>Wrangler now includes built-in shell tab completion support, making it faster and easier to navigate commands without memorizing every option. Press Tab as you type to autocomplete commands, subcommands, flags, and even option values like log levels.</p>
<p>Tab completions are supported for Bash, Zsh, Fish, and PowerShell.</p>
<h4 id="2026-01-09-wrangler-tab-completion-setup">Setup</h4>
<p>Generate the completion script for your shell and add it to your configuration file:</p>
<pre tabindex="0"><code class="language-sh">&#35; Bash&#10;wrangler complete bash &gt;&gt; ~/.bashrc&#10;&#10;&#35; Zsh&#10;wrangler complete zsh &gt;&gt; ~/.zshrc&#10;&#10;&#35; Fish&#10;wrangler complete fish &gt;&gt; ~/.config/fish/config.fish&#10;&#10;&#35; PowerShell&#10;wrangler complete powershell &gt;&gt; $PROFILE&#10;</code></pre>
<p>After adding the script, restart your terminal or source your configuration file for the changes to take effect. Then you can simply press Tab to see available completions:</p>
<pre tabindex="0"><code class="language-sh">wrangler d&lt;TAB&gt;          # completes to &#x27;deploy&#x27;, &#x27;dev&#x27;, &#x27;d1&#x27;, etc.&#10;wrangler kv &lt;TAB&gt;        # shows subcommands: namespace, key, bulk&#10;</code></pre>
<p>Tab completions are dynamically generated from Wrangler's command registry, so they stay up-to-date as new commands and options are added. This feature is powered by <a href="https://github.com/bombshell-dev/tab/"><code>@bomb.sh/tab</code></a>.</p>
<p>See the <a href="/workers/wrangler/commands/general/#complete"><code>wrangler complete</code> documentation</a> for more details.</p>


<h2 id="workers-analytics-engine-sql-now-supports-filtering-using-having-and-like"><a href="/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/">Workers Analytics Engine SQL now supports filtering using HAVING and LIKE</a></h2>
<p><em>2026-01-07</em></p>
<p>You can now use the <code>HAVING</code> clause and <code>LIKE</code> pattern matching operators in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a>.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale and query your data through a simple SQL API.</p>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-filtering-using-having">Filtering using <code>HAVING</code></h4>
<p>The <code>HAVING</code> clause complements the <code>WHERE</code> clause by enabling you to filter groups based on aggregate values. While <code>WHERE</code> filters rows before aggregation, <code>HAVING</code> filters groups after aggregation is complete.</p>
<p>You can use <code>HAVING</code> to filter groups where the average exceeds a threshold:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;    blob1 AS probe_name,&#10;    avg(double1) AS average_temp&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING average_temp &gt; 10&#10;</code></pre>
<p>You can also filter groups based on aggregates such as the number of items in the group:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;    blob1 AS probe_name,&#10;    count() AS num_readings&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING num_readings &gt; 100&#10;</code></pre>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-pattern-matching-using-like">Pattern matching using <code>LIKE</code></h4>
<p>The new pattern matching operators enable you to search for strings that match specific patterns using wildcard characters:</p>
<ul>
<li><code>LIKE</code> - case-sensitive pattern matching</li>
<li><code>NOT LIKE</code> - case-sensitive pattern exclusion</li>
<li><code>ILIKE</code> - case-insensitive pattern matching</li>
<li><code>NOT ILIKE</code> - case-insensitive pattern exclusion</li>
</ul>
<p>Pattern matching supports two wildcard characters: <code>%</code> (matches zero or more characters) and <code>_</code> (matches exactly one character).</p>
<p>You can match strings starting with a prefix:</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM logs&#10;WHERE blob1 LIKE &#x27;error%&#x27;&#10;</code></pre>
<p>You can also match file extensions (case-insensitive):</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM requests&#10;WHERE blob2 ILIKE &#x27;%.jpg&#x27;&#10;</code></pre>
<p>Another example is excluding strings containing specific text:</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM events&#10;WHERE blob3 NOT ILIKE &#x27;%debug%&#x27;&#10;</code></pre>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-ready-to-get-started">Ready to get started?</h4>
<p>Learn more about the <a href="/analytics/analytics-engine/sql-reference/statements/#having-clause"><code>HAVING</code> clause</a> or <a href="/analytics/analytics-engine/sql-reference/operators/#pattern-matching-operators">pattern matching operators</a> in the Workers Analytics Engine SQL reference documentation.</p>


<h2 id="build-microfrontend-applications-on-workers"><a href="/changelog/post/2026-01-01-microfrontends/">Build microfrontend applications on Workers</a></h2>
<p><em>2026-01-01</em></p>
<p>You can now deploy microfrontends to Cloudflare, splitting a single application into smaller, independently deployable units that render as one cohesive application. This lets different teams using different frameworks develop, test, and deploy each microfrontend without coordinating releases.</p>
<p>Microfrontends solve several challenges for large-scale applications:</p>
<ul>
<li><strong>Independent deployments</strong>: Teams deploy updates on their own schedule without redeploying the entire application</li>
<li><strong>Framework flexibility</strong>: Build multi-framework applications (for example, Astro, Remix, and Next.js in one app)</li>
<li><strong>Gradual migration</strong>: Migrate from a monolith to a distributed architecture incrementally</li>
</ul>
<p>Create a microfrontend project:</p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This template automatically creates a router worker with pre-configured routing logic, and lets you configure <a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a> to Workers you have already deployed to your Cloudflare account. The router Worker analyzes incoming requests, matches them against configured routes, and forwards requests to the appropriate microfrontend via service bindings. The router automatically rewrites HTML, CSS, and headers to ensure assets load correctly from each microfrontend's mount path. The router includes advanced features like preloading for faster navigation between microfrontends, smooth page transitions using the View Transitions API, and automatic path rewriting for assets, redirects, and cookies.</p>
<p>Each microfrontend can be a full-framework application, a static site with Workers Static Assets, or any other Worker-based application.</p>
<p>Get started with the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe">microfrontends template</a>, or read the <a href="/workers/framework-guides/web-apps/microfrontends/">microfrontends documentation</a> for implementation details.</p>


<h2 id="agents-sdk-v0-3-0-workers-ai-provider-v3-0-0-and-ai-gateway-provider-v3-0-0-with-ai-sdk-v6-support"><a href="/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/">Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support</a></h2>
<p><em>2025-12-22</em></p>
<p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> v0.3.0 bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v6</a> and introducing the unified tool pattern, dynamic tool approval, and enhanced React hooks with improved tool handling.</p>
<p>This release includes improved streaming and tool support, dynamic tool approval (for &quot;human in the loop&quot; systems), enhanced React hooks with <code>onToolCall</code> callback, improved error handling for streaming responses, and seamless migration from v5 patterns.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable tool execution and approval workflows.</p>
<p>Additionally, we've updated <strong>workers-ai-provider v3.0.0</strong>, the official provider for Cloudflare Workers AI models, and <strong>ai-gateway-provider v3.0.0</strong>, the provider for Cloudflare AI Gateway, to be compatible with AI SDK v6.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-agents-sdk-v0-3-0">Agents SDK v0.3.0</h4>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-unified-tool-pattern">Unified Tool Pattern</h4>
<p>AI SDK v6 introduces a unified tool pattern where all tools are defined on the server using the <code>tool()</code> function. This replaces the previous client-side <code>AITool</code> pattern.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-server-side-tool-definition">Server-Side Tool Definition</h4>
<pre tabindex="0"><code class="language-ts">import { tool } from &quot;ai&quot;;&#10;import { z } from &quot;zod&quot;;&#10;&#10;// Server: Define ALL tools on the server&#10;const tools = {&#10;	// Server-executed tool&#10;	getWeather: tool({&#10;		description: &quot;Get weather for a city&quot;,&#10;		inputSchema: z.object({ city: z.string() }),&#10;		execute: async ({ city }) =&gt; fetchWeather(city)&#10;	}),&#10;&#10;	// Client-executed tool (no execute = client handles via onToolCall)&#10;	getLocation: tool({&#10;		description: &quot;Get user location from browser&quot;,&#10;		inputSchema: z.object({})&#10;		// No execute function&#10;	}),&#10;&#10;	// Tool requiring approval (dynamic based on input)&#10;	processPayment: tool({&#10;		description: &quot;Process a payment&quot;,&#10;		inputSchema: z.object({ amount: z.number() }),&#10;		needsApproval: async ({ amount }) =&gt; amount &gt; 100,&#10;		execute: async ({ amount }) =&gt; charge(amount)&#10;	})&#10;};&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-client-side-tool-handling">Client-Side Tool Handling</h4>
<pre tabindex="0"><code class="language-ts">// Client: Handle client-side tools via onToolCall callback&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;const { messages, sendMessage, addToolOutput } = useAgentChat({&#10;	agent,&#10;	onToolCall: async ({ toolCall, addToolOutput }) =&gt; {&#10;		if (toolCall.toolName === &quot;getLocation&quot;) {&#10;			const position = await new Promise((resolve, reject) =&gt; {&#10;				navigator.geolocation.getCurrentPosition(resolve, reject);&#10;			});&#10;			addToolOutput({&#10;				toolCallId: toolCall.toolCallId,&#10;				output: {&#10;					lat: position.coords.latitude,&#10;					lng: position.coords.longitude&#10;				}&#10;			});&#10;		}&#10;	}&#10;});&#10;</code></pre>
<p><strong>Key benefits of the unified tool pattern:</strong></p>
<ul>
<li><strong>Server-defined tools</strong>: All tools are defined in one place on the server</li>
<li><strong>Dynamic approval</strong>: Use <code>needsApproval</code> to conditionally require user confirmation</li>
<li><strong>Cleaner client code</strong>: Use <code>onToolCall</code> callback instead of managing tool configs</li>
<li><strong>Type safety</strong>: Full TypeScript support with proper tool typing</li>
</ul>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v6 capabilities.</p>
<pre tabindex="0"><code class="language-ts">// Basic chat setup with onToolCall&#10;const { messages, sendMessage, addToolOutput } = useAgentChat({&#10;	agent,&#10;	onToolCall: async ({ toolCall, addToolOutput }) =&gt; {&#10;		// Handle client-side tool execution&#10;		await addToolOutput({&#10;			toolCallId: toolCall.toolCallId,&#10;			output: { result: &quot;success&quot; }&#10;		});&#10;	}&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-dynamic-tool-approval">Dynamic Tool Approval</h4>
<p>Use <code>needsApproval</code> on server tools to conditionally require user confirmation:</p>
<pre tabindex="0"><code class="language-ts">const paymentTool = tool({&#10;	description: &quot;Process a payment&quot;,&#10;	inputSchema: z.object({&#10;		amount: z.number(),&#10;		recipient: z.string()&#10;	}),&#10;	needsApproval: async ({ amount }) =&gt; amount &gt; 1000,&#10;	execute: async ({ amount, recipient }) =&gt; {&#10;		return await processPayment(amount, recipient);&#10;	}&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>The <code>isToolUIPart</code> and <code>getToolName</code> functions now check both static and dynamic tool parts:</p>
<pre tabindex="0"><code class="language-ts">import { isToolUIPart, getToolName } from &quot;ai&quot;;&#10;&#10;const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolOutput({&#10;		toolCallId: part.toolCallId,&#10;		output: &quot;User approved the action&quot;&#10;	});&#10;}&#10;</code></pre>
<p>If you need the v5 behavior (static-only checks), use the new functions:</p>
<pre tabindex="0"><code class="language-ts">import { isStaticToolUIPart, getStaticToolName } from &quot;ai&quot;;&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-converttomodelmessages-is-now-async">convertToModelMessages() is now async</h4>
<p>The <code>convertToModelMessages()</code> function is now asynchronous. Update all calls to await the result:</p>
<pre tabindex="0"><code class="language-ts">import { convertToModelMessages } from &quot;ai&quot;;&#10;&#10;const result = streamText({&#10;	messages: await convertToModelMessages(this.messages),&#10;	model: openai(&quot;gpt-4o&quot;)&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-modelmessage-type">ModelMessage type</h4>
<p>The <code>CoreMessage</code> type has been removed. Use <code>ModelMessage</code> instead:</p>
<pre tabindex="0"><code class="language-ts">import { convertToModelMessages, type ModelMessage } from &quot;ai&quot;;&#10;&#10;const modelMessages: ModelMessage[] = await convertToModelMessages(messages);&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-generateobject-mode-option-removed">generateObject mode option removed</h4>
<p>The <code>mode</code> option for <code>generateObject</code> has been removed:</p>
<pre tabindex="0"><code class="language-ts">// Before (v5)&#10;const result = await generateObject({&#10;	mode: &quot;json&quot;,&#10;	model,&#10;	schema,&#10;	prompt&#10;});&#10;&#10;// After (v6)&#10;const result = await generateObject({&#10;	model,&#10;	schema,&#10;	prompt&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-structured-output-with-generatetext">Structured Output with generateText</h4>
<p>While <code>generateObject</code> and <code>streamObject</code> are still functional, the recommended approach is to use <code>generateText</code>/<code>streamText</code> with the <code>Output.object()</code> helper:</p>
<pre tabindex="0"><code class="language-ts">import { generateText, Output, stepCountIs } from &quot;ai&quot;;&#10;&#10;const { output } = await generateText({&#10;	model: openai(&quot;gpt-4&quot;),&#10;	output: Output.object({&#10;		schema: z.object({ name: z.string() })&#10;	}),&#10;	stopWhen: stepCountIs(2),&#10;	prompt: &quot;Generate a name&quot;&#10;});&#10;</code></pre>
<blockquote>
<p><strong>Note</strong>: When using structured output with <code>generateText</code>, you must configure multiple steps with <code>stopWhen</code> because generating the structured output is itself a step.</p>
</blockquote>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-workers-ai-provider-v3-0-0">workers-ai-provider v3.0.0</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v3.0.0 with AI SDK v6 support.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre tabindex="0"><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v3.0.0 - enhanced v6 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v6 file handling with automatic conversion:</p>
<pre tabindex="0"><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre tabindex="0"><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages: await convertToModelMessages(messages),&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-ai-gateway-provider-v3-0-0">ai-gateway-provider v3.0.0</h4>
<p>The ai-gateway-provider v3.0.0 now supports AI SDK v6, enabling you to use Cloudflare AI Gateway with multiple AI providers including Anthropic, Azure, AWS Bedrock, Google Vertex, and Perplexity.</p>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-ai-gateway-setup">AI Gateway Setup</h4>
<p>Use Cloudflare AI Gateway to add analytics, caching, and rate limiting to your AI applications:</p>
<pre tabindex="0"><code class="language-ts">import { createAIGateway } from &quot;ai-gateway-provider&quot;;&#10;&#10;// Create AI Gateway provider (v3.0.0 - enhanced v6 internals)&#10;const model = createAIGateway({&#10;	gatewayUrl: &quot;https://gateway.ai.cloudflare.com/v1/your-account-id/gateway&quot;,&#10;	headers: {&#10;		&quot;Authorization&quot;: `Bearer ${env.AI_GATEWAY_TOKEN}`&#10;	}&#10;})({&#10;	provider: &quot;openai&quot;,&#10;	model: &quot;gpt-4o&quot;&#10;});&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-migration-from-v5">Migration from v5</h4>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-deprecated-apis">Deprecated APIs</h4>
<p>The following APIs are deprecated in favor of the unified tool pattern:</p>
<table>
<thead>
<tr>
<th>Deprecated</th>
<th>Replacement</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AITool</code> type</td>
<td>Use AI SDK's <code>tool()</code> function on server</td>
</tr>
<tr>
<td><code>extractClientToolSchemas()</code></td>
<td>Define tools on server, no client schemas needed</td>
</tr>
<tr>
<td><code>createToolsFromClientSchemas()</code></td>
<td>Define tools on server with <code>tool()</code></td>
</tr>
<tr>
<td><code>toolsRequiringConfirmation</code> option</td>
<td>Use <code>needsApproval</code> on server tools</td>
</tr>
<tr>
<td><code>experimental_automaticToolResolution</code></td>
<td>Use <code>onToolCall</code> callback</td>
</tr>
<tr>
<td><code>tools</code> option in <code>useAgentChat</code></td>
<td>Use <code>onToolCall</code> for client-side execution</td>
</tr>
<tr>
<td><code>addToolResult()</code></td>
<td>Use <code>addToolOutput()</code></td>
</tr>
</tbody>
</table>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-breaking-changes-summary">Breaking Changes Summary</h4>
<ol>
<li><strong>Unified Tool Pattern</strong>: All tools must be defined on the server using <code>tool()</code></li>
<li><strong><code>convertToModelMessages()</code> is async</strong>: Add <code>await</code> to all calls</li>
<li><strong><code>CoreMessage</code> removed</strong>: Use <code>ModelMessage</code> instead</li>
<li><strong><code>generateObject</code> mode removed</strong>: Remove <code>mode</code> option</li>
<li><strong><code>isToolUIPart</code> behavior changed</strong>: Now checks both static and dynamic tool parts</li>
</ol>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-installation">Installation</h4>
<p>Update your dependencies to use the latest versions:</p>
<pre tabindex="0"><code class="language-bash">npm install agents@^0.3.0 workers-ai-provider@^3.0.0 ai-gateway-provider@^3.0.0 ai@^6.0.0 @ai-sdk/react@^3.0.0 @ai-sdk/openai@^3.0.0&#10;</code></pre>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v6.md">Migration Guide</a> - Comprehensive migration documentation from v5 to v6</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-6-0">AI SDK v6 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://vercel.com/blog/ai-sdk-6">AI SDK v6 Announcement</a> - Learn about new features in v6</li>
<li><a href="https://sdk.vercel.ai/docs">AI SDK Documentation</a> - Complete AI SDK reference</li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="2025-12-22-agents-sdk-ai-sdk-v6-feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade from v5 to v6?</li>
<li><strong>Unified tool pattern</strong> - How does the new server-defined tool pattern work for you?</li>
<li><strong>Dynamic tool approval</strong> - Does the <code>needsApproval</code> feature meet your needs?</li>
<li><strong>AI Gateway integration</strong> - How well does the new provider work with your setup?</li>
</ul>


<h2 id="static-prerendering-support-for-tanstack-start"><a href="/changelog/post/2025-12-19-tanstack-start-prerendering/">Static prerendering support for TanStack Start</a></h2>
<p><em>2025-12-19</em></p>
<p><a href="https://tanstack.com/start/">TanStack Start</a> apps can now prerender routes to static HTML at build time with access to build time environment variables
and bindings,  and serve them as <a href="/workers/static-assets/">static assets</a>. To enable prerendering, configure the <code>prerender</code> option of the TanStack Start plugin in your Vite config:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;&#10;export default defineConfig({&#10;  plugins: [&#10;    cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }),&#10;    tanstackStart({&#10;      prerender: {&#10;        enabled: true,&#10;      },&#10;    }),&#10;  ],&#10;});&#10;</code></pre>
<p>This feature requires <code>@tanstack/react-start</code> v1.138.0 or later. See the <a href="/workers/framework-guides/web-apps/tanstack-start/#static-prerendering">TanStack Start framework guide</a> for more details.</p>


<h2 id="build-image-policies-for-workers-builds-and-cloudflare-pages"><a href="/changelog/post/2025-12-01-build-image-policies-dev-plat/">Build image policies for Workers Builds and Cloudflare Pages</a></h2>
<p><em>2025-12-18</em></p>
<p>We've published build image policies for <a href="/workers/ci-cd/builds/build-image/#build-image-policy">Workers Builds</a> and <a href="/pages/configuration/build-image/#build-image-policy">Cloudflare Pages</a>, which establish:</p>
<ul>
<li><strong>Minor version updates</strong>: We typically update preinstalled software to the latest available minor version without notice. For tools that don't follow semantic versioning (e.g., Bun or Hugo), we provide 3 months’ notice.</li>
<li><strong>Major version updates</strong>: Before preinstalled software reaches end-of-life, we update to the next stable LTS version with 3 months’ notice.</li>
<li><strong>Build image version deprecation (Pages only)</strong>: We provide 6 months’ notice before deprecation. Projects on v1 or v2 will be automatically moved to v3 on their specified deprecation dates.</li>
</ul>
<p>To prepare for updates, monitor the <a href="https://developers.cloudflare.com/changelog/">Cloudflare Changelog</a>, dashboard notifications, and email. You can also <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">override default versions</a> to maintain specific versions.</p>


<h2 id="retrieve-your-authentication-token-with-wrangler-auth-token"><a href="/changelog/post/2025-12-18-wrangler-auth-token/">Retrieve your authentication token with `wrangler auth token`</a></h2>
<p><em>2025-12-18</em></p>
<p>Wrangler now includes a new <a href="/workers/wrangler/commands/general/#auth-token"><code>wrangler auth token</code></a> command that retrieves your current authentication token or credentials for use with other tools and scripts.</p>
<pre tabindex="0"><code class="language-sh">wrangler auth token&#10;</code></pre>
<p>The command returns whichever authentication method is currently configured, in priority order: API token from <code>CLOUDFLARE_API_TOKEN</code>, or OAuth token from <code>wrangler login</code> (automatically refreshed if expired).</p>
<p>Use the <code>--json</code> flag to get structured output including the token type:</p>
<pre tabindex="0"><code class="language-sh">wrangler auth token --json&#10;</code></pre>
<p>The JSON output includes the authentication type:</p>
<pre tabindex="0"><code class="language-jsonc">// API token&#10;{ &quot;type&quot;: &quot;api_token&quot;, &quot;token&quot;: &quot;...&quot; }&#10;&#10;// OAuth token&#10;{ &quot;type&quot;: &quot;oauth&quot;, &quot;token&quot;: &quot;...&quot; }&#10;&#10;// API key/email (only available with --json)&#10;{ &quot;type&quot;: &quot;api_key&quot;, &quot;key&quot;: &quot;...&quot;, &quot;email&quot;: &quot;...&quot; }&#10;</code></pre>
<p>API key/email credentials from <code>CLOUDFLARE_API_KEY</code> and <code>CLOUDFLARE_EMAIL</code> require the <code>--json</code> flag since this method uses two values instead of a single token.</p>


<h2 id="support-for-ctx-exports-in-cloudflare-vitest-pool-workers"><a href="/changelog/post/2025-12-16-vitest-ctx-exports-support/">Support for ctx.exports in @cloudflare/vitest-pool-workers</a></h2>
<p><em>2025-12-16</em></p>
<p>The <a href="/workers/testing/vitest-integration/"><code>@cloudflare/vitest-pool-workers</code></a> package now supports the <a href="/workers/runtime-apis/context/#exports"><code>ctx.exports</code> API</a>, allowing you to access your Worker's top-level exports during tests.</p>
<p>You can access <code>ctx.exports</code> in unit tests by calling <code>createExecutionContext()</code>:</p>
<pre tabindex="0"><code class="language-ts">import { createExecutionContext } from &quot;cloudflare:test&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;&#10;it(&quot;can access ctx.exports&quot;, async () =&gt; {&#10;  const ctx = createExecutionContext();&#10;  const result = await ctx.exports.MyEntryPoint.myMethod();&#10;  expect(result).toBe(&quot;expected value&quot;);&#10;});&#10;</code></pre>
<p>Alternatively, you can import <code>exports</code> directly from <code>cloudflare:workers</code>:</p>
<pre tabindex="0"><code class="language-ts">import { exports } from &quot;cloudflare:workers&quot;;&#10;import { it, expect } from &quot;vitest&quot;;&#10;&#10;it(&quot;can access imported exports&quot;, async () =&gt; {&#10;  const result = await exports.MyEntryPoint.myMethod();&#10;  expect(result).toBe(&quot;expected value&quot;);&#10;});&#10;</code></pre>
<p>See the <a href="https://github.com/cloudflare/workers-sdk/tree/main/fixtures/vitest-plugin-examples/context-exports">context-exports fixture</a> for a complete example.</p>


<h2 id="configure-your-framework-for-cloudflare-automatically"><a href="/changelog/post/2025-12-16-wrangler-autoconfig/">Configure your framework for Cloudflare automatically</a></h2>
<p><em>2025-12-16</em></p>
<p>Wrangler now supports automatic configuration for popular web frameworks in experimental mode, making it even easier to deploy to Cloudflare Workers.</p>
<p>Previously, if you wanted to deploy an application using a popular web framework like Next.js or Astro, you had to follow tutorials to set up your application for deployment to Cloudflare Workers. This usually involved creating a Wrangler file, installing adapters, or changing configuration options.</p>
<p>Now <code>wrangler deploy</code> does this for you. Starting with Wrangler 4.55, you can use <code>npx wrangler deploy --x-autoconfig</code> in the directory of any web application using one of the supported frameworks. Wrangler will then proceed to configure and deploy it to your Cloudflare account.</p>
<p>You can also configure your application without deploying it by using the new <code>npx wrangler setup</code> command. This enables you to easily review what changes we are making so your application is ready for Cloudflare Workers.</p>
<p>The following application frameworks are supported starting today:</p>
<ul>
<li>Next.js</li>
<li>Astro</li>
<li>Nuxt</li>
<li>TanStack Start</li>
<li>SolidStart</li>
<li>React Router</li>
<li>SvelteKit</li>
<li>Docusaurus</li>
<li>Qwik</li>
<li>Analog</li>
</ul>
<p>Automatic configuration also supports static sites by detecting the assets directory and build command. From a single index.html file to the output of a generator like Jekyll or Hugo, you can just run <code>npx wrangler deploy --x-autoconfig</code> to upload to Cloudflare.</p>
<p>We're really excited to bring you automatic configuration so you can do more with Workers. Please let us know if you run into challenges using this experimentally. We’ve opened a <a href="https://github.com/cloudflare/workers-sdk/discussions/11667">GitHub discussion</a> and would love to hear your feedback.</p>


<h2 id="new-best-practices-guide-for-durable-objects"><a href="/changelog/post/2025-12-15-rules-of-durable-objects/">New Best Practices guide for Durable Objects</a></h2>
<p><em>2025-12-15</em></p>
<p>A new <a href="/durable-objects/best-practices/rules-of-durable-objects/">Rules of Durable Objects</a> guide is now available, providing opinionated best practices for building effective Durable Objects applications. This guide covers design patterns, storage strategies, concurrency, and common anti-patterns to avoid.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Design around your &quot;atom&quot; of coordination</strong> — Create one Durable Object per logical unit (chat room, game session, user) instead of a global singleton that becomes a bottleneck.</li>
<li><strong>Use SQLite storage with RPC methods</strong> — SQLite-backed Durable Objects with typed RPC methods provide the best developer experience and performance.</li>
<li><strong>Understand input and output gates</strong> — Learn how Cloudflare's runtime prevents data races by default, how write coalescing works, and when to use <code>blockConcurrencyWhile()</code>.</li>
<li><strong>Leverage Hibernatable WebSockets</strong> — Reduce costs for real-time applications by allowing Durable Objects to sleep while maintaining WebSocket connections.</li>
</ul>
<p>The <a href="/durable-objects/examples/testing-with-durable-objects/">testing documentation</a> has also been updated with modern patterns using <code>@cloudflare/vitest-pool-workers</code>, including examples for testing SQLite storage, alarms, and direct instance access:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17718.md")</div>


<h2 id="billing-for-sqlite-storage"><a href="/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/">Billing for SQLite Storage</a></h2>
<p><em>2025-12-12</em></p>
<p>Storage billing for SQLite-backed Durable Objects will be enabled in January 2026, with a target date of January 7, 2026 (no earlier).</p>
<p>To view your SQLite storage usage, go to the <strong>Durable Objects</strong> page</p>
<div class="nb-dash-button"></div>
<p>If you do not want to incur costs, please take action such as optimizing queries or deleting unnecessary stored data in order to reduce your SQLite storage usage ahead of the January 7th target. Only usage on and after the billing target date will incur charges.</p>
<p>Developers on the Workers Paid plan with Durable Object's SQLite storage usage beyond included limits will incur charges according to <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">SQLite storage pricing</a> announced in September 2024 with the <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">public beta</a>. Developers on the Workers Free plan will not be charged.</p>
<p>Compute billing for SQLite-backed Durable Objects has been enabled since the initial public beta. SQLite-backed Durable Objects currently incur <a href="/durable-objects/platform/pricing/#compute-billing">charges for requests and duration</a>, and no changes are being made to compute billing.</p>
<p>For more information about SQLite storage pricing and limits, refer to the <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">Durable Objects pricing documentation</a>.</p>


<h2 id="python-cold-start-improvements"><a href="/changelog/post/2025-12-08-python-cold-start-improvements/">Python cold start improvements</a></h2>
<p><em>2025-12-08</em></p>
<p>Python Workers now feature improved cold start performance, reducing initialization time for new Worker instances.
This improvement is particularly noticeable for Workers with larger dependency sets or complex initialization logic.</p>
<p>Every time you deploy a Python Worker, a memory snapshot is captured after the top level of the Worker is executed.
This snapshot captures all imports, including package imports that are often costly to load. The memory snapshot is loaded
when the Worker is first started, avoiding the need to reload the Python runtime and all dependencies on each cold start.</p>
<p>We set up a benchmark that imports common packages (<a href="https://www.python-httpx.org/">httpx</a>,
<a href="https://fastapi.tiangolo.com/">fastapi</a> and <a href="https://docs.pydantic.dev/latest/">pydantic</a>)
to see how Python Workers stack up against other platforms:</p>
<table>
<thead>
<tr>
<th>Platform</th>
<th>Mean Cold Start (ms)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Python Workers</td>
<td>1027</td>
</tr>
<tr>
<td>AWS Lambda</td>
<td>2502</td>
</tr>
<tr>
<td>Google Cloud Run</td>
<td>3069</td>
</tr>
</tbody>
</table>
<p>These benchmarks run continuously. You can view the results and the methodology on our <a href="https://cold.edgeworker.net">benchmark page</a>.</p>
<p>In additional testing, we have found that without any memory snapshot, the cold start for this benchmark takes around 10 seconds, so this change improves cold start performance by roughly a factor of 10.</p>
<p>To get started with Python Workers, check out our <a href="/workers/languages/python/">Python Workers overview</a>.</p>


<h2 id="easy-python-package-management-with-pywrangler"><a href="/changelog/post/2025-12-08-python-pywrangler/">Easy Python package management with Pywrangler</a></h2>
<p><em>2025-12-08</em></p>
<p>We are introducing a brand new tool called Pywrangler, which simplifies package management in Python Workers by
automatically installing Workers-compatible Python packages into your project.</p>
<p>With Pywrangler, you specify your Worker's Python dependencies in your <code>pyproject.toml</code> file:</p>
<pre tabindex="0"><code class="language-toml">[project]&#10;name = &quot;python-beautifulsoup-worker&quot;&#10;version = &quot;0.1.0&quot;&#10;description = &quot;A simple Worker using beautifulsoup4&quot;&#10;requires-python = &quot;&gt;=3.12&quot;&#10;dependencies = [&#10;    &quot;beautifulsoup4&quot;&#10;]&#10;&#10;[dependency-groups]&#10;dev = [&#10;  &quot;workers-py&quot;,&#10;  &quot;workers-runtime-sdk&quot;&#10;]&#10;</code></pre>
<p>You can then develop and deploy your Worker using the following commands:</p>
<pre tabindex="0"><code class="language-bash">uv run pywrangler dev&#10;uv run pywrangler deploy&#10;</code></pre>
<p>Pywrangler automatically downloads and vendors the necessary packages for your Worker, and these packages are bundled with the Worker when you deploy.</p>
<p>Consult the <a href="/workers/languages/python/packages/">Python packages documentation</a> for full details on Pywrangler and Python package management in Workers.</p>


<h2 id="wrangler-config-is-optional-when-using-vite-plugin"><a href="/changelog/post/2025-12-08-vite-optional-config/">Wrangler config is optional when using Vite plugin</a></h2>
<p><em>2025-12-08</em></p>
<p>When using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> to build and deploy Workers, a Wrangler configuration file is now optional for assets-only (static) sites. If no <code>wrangler.toml</code>, <code>wrangler.json</code>, or <code>wrangler.jsonc</code> file is found, the plugin generates sensible defaults for an assets-only site. The <code>name</code> is based on the <code>package.json</code> or the project directory name, and the <code>compatibility_date</code> uses the latest date supported by your installed Miniflare version.</p>
<p>This allows easier setup for static sites using Vite. Note that SPAs will still need to <a href="https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/">set <code>assets.not_found_handling</code> to <code>single-page-application</code></a> in order to function correctly.</p>


<h2 id="configure-workers-programmatically-using-the-vite-plugin"><a href="/changelog/post/2025-12-08-vite-programmatic-config/">Configure Workers programmatically using the Vite plugin</a></h2>
<p><em>2025-12-08</em></p>
<p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> now supports programmatic configuration of Workers without a Wrangler configuration file. You can use the <code>config</code> option to define Worker settings directly in your Vite configuration, or to modify existing configuration loaded from a Wrangler config file. This is particularly useful when integrating with other build tools or frameworks, as it allows them to control Worker configuration without needing users to manage a separate config file.</p>
<h4 id="2025-12-08-vite-programmatic-config-the-config-option">The <code>config</code> option</h4>
<p>The Vite plugin's new <code>config</code> option accepts either a partial configuration object or a function that receives the current configuration and returns overrides. This option is applied after any config file is loaded, allowing the plugin to override specific values or define Worker configuration entirely in code.</p>
<h4 id="2025-12-08-vite-programmatic-config-example-usage">Example usage</h4>
<p>Setting <code>config</code> to an object to provide configuration values that merge with defaults and config file settings:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: {&#10;				name: &quot;my-worker&quot;,&#10;				compatibility_flags: [&quot;nodejs_compat&quot;],&#10;				send_email: [&#10;					{&#10;						name: &quot;EMAIL&quot;,&#10;					},&#10;				],&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>Use a function to modify the existing configuration:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: (userConfig) =&gt; {&#10;				delete userConfig.compatibility_flags;&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>Return an object with values to merge:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: (userConfig) =&gt; {&#10;				if (!userConfig.compatibility_flags.includes(&quot;no_nodejs_compat&quot;)) {&#10;					return { compatibility_flags: [&quot;nodejs_compat&quot;] };&#10;				}&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<h4 id="2025-12-08-vite-programmatic-config-auxiliary-workers">Auxiliary Workers</h4>
<p>Auxiliary Workers also support the <code>config</code> option, enabling multi-Worker architectures without config files.</p>
<p>Define auxiliary Workers without config files using <code>config</code> inside the <code>auxiliaryWorkers</code> array:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			config: {&#10;				name: &quot;entry-worker&quot;,&#10;				main: &quot;./src/entry.ts&quot;,&#10;				services: [{ binding: &quot;API&quot;, service: &quot;api-worker&quot; }],&#10;			},&#10;			auxiliaryWorkers: [&#10;				{&#10;					config: {&#10;						name: &quot;api-worker&quot;,&#10;						main: &quot;./src/api.ts&quot;,&#10;					},&#10;				},&#10;			],&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>For more details and examples, see <a href="/workers/vite-plugin/reference/programmatic-configuration/">Programmatic configuration</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/4/">Previous</a><span>Page 5 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/6/">Next</a></nav>
