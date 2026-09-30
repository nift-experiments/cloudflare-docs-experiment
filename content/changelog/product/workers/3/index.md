---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers/3/
  description: '2026-06-16'
  full_title: workers changelog - page 3 | Cloudflare Docs
  head_html: <title>workers changelog - page 3 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-16"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers/3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers changelog - page 3"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-16"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers/3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers/3/#page","headline":"workers changelog - page 3 | Cloudflare Docs","description":"2026-06-16","url":"https://developers.cloudflare.com/changelog/product/workers/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers/3/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="workers-tracing-now-supports-custom-spans"><a href="/changelog/post/2026-06-16-custom-spans/">Workers tracing now supports custom spans</a></h2>
<p><em>2026-06-16</em></p>
<p>You can now create custom trace spans in your Workers code using <code>tracing.enterSpan()</code>. Custom spans appear alongside the automatic platform instrumentation (fetch calls, KV reads, D1 queries, and other platform operations) in your traces and OpenTelemetry exports, with correct parent-child nesting.</p>
<p>The API is available via <code>import { tracing } from &quot;cloudflare:workers&quot;</code> or through the handler context as <code>ctx.tracing</code>:</p>
<pre tabindex="0"><code class="language-ts">import { tracing } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return tracing.enterSpan(&quot;handleRequest&quot;, async (span) =&gt; {&#10;      span.setAttribute(&quot;url.path&quot;, new URL(request.url).pathname);&#10;      const data = await env.MY_KV.get(&quot;key&quot;);&#10;      return new Response(data);&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>Spans nest automatically based on the JavaScript async context, and are auto-ended when the callback returns or its returned promise settles. The <code>Span</code> object provides <code>setAttribute(key, value)</code> for attaching metadata and an <code>isTraced</code> property to check whether the current request is being sampled.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_custom_spans_screenshot.png" alt="Trace waterfall showing custom spans nested alongside automatic KV and fetch instrumentation" /></p>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> in your Wrangler configuration for spans to be recorded.</p>
<p>For full API details and examples, refer to <a href="/workers/observability/traces/custom-spans/">Custom spans</a>.</p>


<h2 id="introducing-glm-5-2-on-workers-ai"><a href="/changelog/post/2026-06-16-glm-5.2-workers-ai/">Introducing GLM-5.2 on Workers AI</a></h2>
<p><em>2026-06-16</em></p>
<p>We are excited to announce <strong>GLM-5.2</strong> on Workers AI, Z.ai's flagship agentic coding model.</p>
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


<h2 id="filter-durable-objects-metrics-by-object-id-or-name"><a href="/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/">Filter Durable Objects metrics by object ID or name</a></h2>
<p><em>2026-06-12</em></p>
<p>You can now filter the <strong>Metrics</strong> tab for a Durable Objects namespace by an individual Durable Object's <a href="/durable-objects/api/id/">ID</a> or <a href="/durable-objects/api/id/#name">name</a> in the Cloudflare dashboard. Previously, metrics charts only showed aggregate, namespace-level data, making it difficult to isolate the behavior of a specific object.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-metrics-dashboard.png" alt="The Durable Objects Metrics tab filtered to a single object by ID, showing per-object requests and errors by invocation status." /></p>
<p>Start typing an ID or name into the filter and select a match from the autocomplete dropdown. The autocomplete only shows objects with invocations during the selected time range, so an object that does not appear has not been invoked in that window. This does not necessarily mean the object has been deleted. Every chart on the page updates to reflect only the selected object. This makes it easier to identify and investigate a single Durable Object when debugging a high-traffic object, an error spike, or unexpected storage usage. Clear the filter to return to namespace-level metrics.</p>
<p>Metrics are powered by the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, so standard analytics behavior such as ingestion delay and <a href="/analytics/faq/graphql-api-inconsistent-results/">sampling</a> applies.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/">Metrics and analytics</a>.</p>


<h2 id="track-dynamic-workers-usage-from-the-dashboard-and-graphql-api"><a href="/changelog/post/2026-06-11-dynamic-workers-count/">Track Dynamic Workers usage from the dashboard and GraphQL API</a></h2>
<p><em>2026-06-11</em></p>
<p><img src="/assets/upstream/images/workers/changelog/dynamic-workers-count.png" alt="Dynamic Workers usage on the Workers overview page" /></p>
<p>Customers can now view the number of <a href="/dynamic-workers/">Dynamic Workers</a> invoked during their billing period from the Workers overview page in the Cloudflare dashboard.</p>
<p>This count reflects the number of Dynamic Workers that Cloudflare would bill for during the selected billing period. Dynamic Workers usage data only goes back to June 1, 2026.</p>
<p>You can also query this count through the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> by using <code>workersInvocationsByOwnerAndScriptGroups</code> and selecting <code>distinctDynamicWorkerCount</code>:</p>
<pre tabindex="0"><code class="language-graphql">query getDynamicWorkersCount(&#10;	$accountTag: string!&#10;	$filter: AccountWorkersInvocationsByOwnerAndScriptGroupsFilter_InputObject&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			workersInvocationsByOwnerAndScriptGroups(limit: 10000, filter: $filter) {&#10;				uniq {&#10;					distinctDynamicWorkerCount&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use variables to set the account and billing-period date range:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;	&quot;filter&quot;: {&#10;		&quot;date_geq&quot;: &quot;2026-06-01&quot;,&#10;		&quot;date_leq&quot;: &quot;2026-06-30&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/dynamic-workers/pricing/">Dynamic Workers pricing</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="pipeline-binding-configuration-field-renamed-to-stream"><a href="/changelog/post/2026-05-27-pipeline-binding-stream-field/">Pipeline binding configuration field renamed to stream</a></h2>
<p><em>2026-06-04</em></p>
<p>The <code>pipeline</code> field inside the <code>pipelines</code> binding configuration in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> has been renamed to <code>stream</code>. The old field is deprecated but still accepted.</p>
<p>Update your configuration to use <code>stream</code> to avoid the deprecation warning.</p>
<p><strong>Before (deprecated):</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17739.md")</div>
<p><strong>After:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17740.md")</div>
<p>No other changes are required. The binding name, TypeScript types, and runtime API (<code>env.MY_PIPELINE.send(...)</code>) remain the same.</p>
<p>For more information on configuring pipeline bindings, refer to <a href="/pipelines/streams/writing-to-streams/#configure-pipeline-binding">Writing to streams</a>.</p>


<h2 id="new-workers-bulk-secrets-api-endpoint"><a href="/changelog/post/2026-06-03-bulk-secrets-api/">New Workers bulk secrets API endpoint</a></h2>
<p><em>2026-06-03</em></p>
<p>You can now create, update, or delete multiple secrets for your Worker in a single request using the <a href="/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update/">bulk secrets endpoint</a>.</p>
<ul>
<li>Include a secret with a value to create or update.</li>
<li>Set a secret to <code>null</code> to delete.</li>
<li>Secrets not included in the request are left unchanged.</li>
</ul>
<p>The following example creates <code>API_KEY</code>, updates the already existing <code>DB_PASSWORD</code>, and deletes <code>OLD_SECRET</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;secrets&quot;: {&#10;    &quot;API_KEY&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;API_KEY&quot;, &quot;text&quot;: &quot;my-api-key&quot; },&#10;    &quot;DB_PASSWORD&quot;: { &quot;type&quot;: &quot;secret_text&quot;, &quot;name&quot;: &quot;DB_PASSWORD&quot;, &quot;text&quot;: &quot;my-db-password&quot; },&#10;    &quot;OLD_SECRET&quot;: null&#10;  }&#10;}&#10;</code></pre>
<p>You can do the same from the command line using <a href="/workers/wrangler/commands/workers/#secret-bulk"><code>wrangler secret bulk</code></a>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler secret bulk &lt; secrets.json&#10;</code></pre>
<p>To delete a key, set its value to <code>null</code> in the JSON file. Deletion is not supported with <code>.env</code> files.</p>
<p>Each request supports up to <strong>100 total operations</strong> (creates, updates, and deletes combined).</p>


<h2 id="store-wrangler-s-oauth-credentials-in-your-os-keychain"><a href="/changelog/post/2026-06-03-wrangler-keyring-credential-storage/">Store Wrangler's OAuth credentials in your OS keychain</a></h2>
<p><em>2026-06-03</em></p>
<p><a href="/workers/wrangler/">Wrangler</a> can now store the OAuth credentials returned by <code>wrangler login</code> in an <a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">AES-256-GCM</a>-encrypted file, with the encryption key held in your operating system keychain. The default behavior is unchanged — credentials still live in a plaintext TOML file unless you opt in.</p>
<p>To opt in, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --use-keyring&#10;</code></pre>
<p>The choice is persisted across Wrangler invocations. Opt back out with <code>npx wrangler login --no-use-keyring</code>, or override the preference for a single command with the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>
<p><code>wrangler whoami</code> now reports where credentials are stored:</p>
<pre tabindex="0"><code class="language-sh">🔐 Credentials are stored in: Encrypted file (~/.config/.wrangler/config/default.enc) with key in macOS Keychain (service=wrangler, account=default)&#10;</code></pre>
<p>Per-platform backends:</p>
<ul>
<li><strong>macOS</strong> uses the built-in Keychain via <code>/usr/bin/security</code>.</li>
<li><strong>Linux</strong> uses <a href="https://wiki.gnome.org/Projects/Libsecret">libsecret</a> via the <code>secret-tool</code> CLI from the <code>libsecret-tools</code> package.</li>
<li><strong>Windows</strong> uses Credential Manager via <a href="https://www.npmjs.com/package/@napi-rs/keyring"><code>@napi-rs/keyring</code></a>, installed on-demand the first time you opt in.</li>
</ul>
<p>Refer to <a href="/workers/wrangler/commands/general/#storing-oauth-credentials-in-the-os-keychain">Storing OAuth credentials in the OS keychain</a> for the full details, including the migration behavior on opt-in/opt-out and the <code>CLOUDFLARE_AUTH_USE_KEYRING</code> environment variable.</p>


<h2 id="schedule-workflow-instances-directly-from-your-workflow-binding"><a href="/changelog/post/2026-06-02-cron-workflows/">Schedule Workflow instances directly from your Workflow binding</a></h2>
<p><em>2026-06-02 15:00:00 UTC</em></p>
<p>You can now attach cron schedules directly to a Workflow binding in <code>wrangler.jsonc</code>. Each scheduled run creates a new Workflow instance automatically, so you do not need to define a separate Worker with a <code>scheduled</code> handler just to trigger your Workflow on an interval.</p>
<p>For example, you can configure hourly, every-15-minute, or weekday schedules on the same Workflow:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;workflows&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;my-scheduled-workflow&quot;,&#10;			&quot;binding&quot;: &quot;MY_WORKFLOW&quot;,&#10;			&quot;class_name&quot;: &quot;MyScheduledWorkflow&quot;,&#10;			&quot;schedules&quot;: [&quot;0 * * * *&quot;, &quot;*/15 * * * *&quot;, &quot;0 9 * * MON-FRI&quot;],&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>Cron workloads get all the same benefits of Workflows with built-in retries, multi-step durable execution, and configurable timeouts of Workflows.</p>
<pre tabindex="0"><code class="language-ts">import {&#10;	WorkflowEntrypoint,&#10;	WorkflowEvent,&#10;	WorkflowStep,&#10;} from &quot;cloudflare:workers&quot;;&#10;&#10;// Runs automatically on each cron schedule defined for the MY_WORKFLOW binding in wrangler.jsonc.&#10;export class MyScheduledWorkflow extends WorkflowEntrypoint&lt;Env&gt; {&#10;	async run(event: WorkflowEvent, step: WorkflowStep) {&#10;		const data = await step.do(&quot;fetch source data&quot;, async () =&gt; {&#10;			return await fetchSourceData();&#10;		});&#10;&#10;		// If this step fails, only this step is retried with the custom logic below&#10;		await step.do(&#10;			&quot;process and store results&quot;,&#10;			{&#10;				retries: { limit: 5, delay: &quot;30 seconds&quot;, backoff: &quot;exponential&quot; },&#10;				timeout: &quot;10 minutes&quot;,&#10;			},&#10;			async () =&gt; {&#10;				await processAndStore(data);&#10;			},&#10;		);&#10;	}&#10;}&#10;</code></pre>
<p>This makes it easier to build recurring, scheduled jobs such as database backups, invoice generation, report aggregation, and cleanup tasks without wiring up a separate Cron Trigger entrypoint.</p>
<p>For more information, refer to <a href="/workflows/build/trigger-workflows/">Trigger Workflows</a>.</p>


<h2 id="agents-sdk-v0-14-0-agent-skills-messengers-scheduled-tasks-workflows-and-hardened-chat-recovery"><a href="/changelog/post/2026-06-02-agents-sdk-v0.14.0/">Agents SDK v0.14.0: Agent Skills, messengers, scheduled tasks, Workflows, and hardened chat recovery</a></h2>
<p><em>2026-06-02</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds four new ways to build with <code>@cloudflare/think</code>: on-demand Agent Skills, chat messengers (starting with Telegram), declarative scheduled tasks, and durable reasoning steps inside Workflows. This release also significantly hardens durable chat recovery, so turns reliably ride through deploys, evictions, and stalled model streams in production.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-agent-skills-experimental">Agent Skills (experimental)</h4>
<p>Give an agent a catalog of on-demand instructions, resources, and scripts. A skill source adds a catalog to the system prompt, and the model activates a skill only when a task matches — so a large library of capabilities does not bloat every prompt.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17667.md")</div>
<p>The <code>agents:skills</code> import bundles a local <code>./skills</code> directory through the Agents Vite plugin (one directory per skill, each with a <code>SKILL.md</code>). Skills can also load from R2 or a manifest. When skills are available, Think exposes <code>activate_skill</code>, <code>read_skill_resource</code>, and an optional <code>run_skill_script</code> tool. Skill loading is resilient: a duplicate or failing source is skipped with a warning instead of breaking the agent.</p>
<p>Agent Skills are <strong>experimental</strong>, and script execution in particular is early. The API may change in a future release. We would love your feedback — tell us what you are building and what is missing in the <a href="https://github.com/cloudflare/agents/discussions">Agents repository</a>.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-messengers">Messengers</h4>
<p>Connect a Think agent directly to a chat platform. Think owns the webhook route, conversation routing, durable reply fiber, and streamed delivery back to the provider. Telegram ships as the first provider.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17668.md")</div>
<p>Each Chat SDK thread maps to its own Think sub-agent by default, so group chats and direct messages do not share memory. Multiple bots, custom conversation routing, and custom providers are all supported.</p>
<h4 id="2026-06-02-agents-sdk-v0.14.0-scheduled-tasks">Scheduled tasks</h4>
<p>Declare recurring, timezone-aware prompts and handlers with a typed domain-specific language (DSL). Think reconciles the declarations on startup and re-arms the next occurrence after each run, backed by durable idempotent submissions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17669.md")</div>
<h4 id="2026-06-02-agents-sdk-v0.14.0-think-workflows">Think Workflows</h4>
<p>Run a model-driven reasoning step inside a Cloudflare Workflow with <code>ThinkWorkflow</code> and <code>step.prompt()</code>, with durable typed structured output, long waits, and approval gates.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17670.md")</div>
<h4 id="2026-06-02-agents-sdk-v0.14.0-production-hardening-for-durable-chat-recovery">Production hardening for durable chat recovery</h4>
<p>Durable chat turns have always been designed to survive a mid-turn deploy or Durable Object eviction. This release is a major hardening pass on that machinery for production.</p>
<ul>
<li><strong>Better recovery during deploys.</strong> Turns now ride through continuous deploys and evictions without losing completed work or re-running tools that already ran.</li>
<li><strong>A live &quot;recovering…&quot; signal.</strong> <code>useAgentChat</code> exposes a new <code>isRecovering</code> flag, so a recovering turn shows progress instead of looking frozen. Most UIs render <code>isStreaming || isRecovering</code> as &quot;busy&quot;.</li>
<li><strong>Stalled streams recover.</strong> Set <code>chatStreamStallTimeoutMs</code> to route a hung provider stream into the same recovery path instead of leaving an infinite spinner.</li>
<li><strong>Sub-agents re-attach.</strong> On parent recovery, an in-flight <code>agentTool()</code> child is re-attached to its result rather than abandoned and re-run, so long-running children no longer lose work under deploys.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-mcp-transport-improvements">MCP transport improvements</h4>
<ul>
<li><strong>Resumable streams</strong> — In-flight tool calls over Server-Sent Events (SSE) survive a dropped connection. Clients reconnect with <code>Last-Event-ID</code> and replay anything they missed.</li>
<li><strong>Readable server IDs</strong> — <code>addMcpServer</code> accepts an optional <code>id</code>, so tools surface as readable keys (for example <code>tool_github_create_pull_request</code>) instead of opaque connection IDs.</li>
<li><strong>Better handling of concurrent requests</strong> — Overlapping JSON-RPC requests are now correctly correlated to their responses across the HTTP and RPC transports.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Compaction</strong> — A <code>Session</code>'s <code>tokenCounter</code> now also drives the compaction boundary decision (&quot;what to compress&quot;), not just the fire/no-fire trigger.</li>
<li><strong><code>@cloudflare/worker-bundler</code></strong> — Adds a <code>virtualModules</code> option to <code>createWorker</code> to provide in-memory module source during bundling.</li>
<li><strong>Client-tool continuations</strong> — Parallel tool results now coalesce into a single continuation, immediate resume requests attach to the pending continuation, and server-side <code>needsApproval</code> continuations resume reliably after approval.</li>
</ul>
<h4 id="2026-06-02-agents-sdk-v0.14.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>


<h2 id="share-local-dev-servers-through-cloudflare-tunnel-in-wrangler-and-vite"><a href="/changelog/post/2026-05-18-local-dev-tunnels/">Share local dev servers through Cloudflare Tunnel in Wrangler and Vite</a></h2>
<p><em>2026-05-18</em></p>
<p>You can now share local dev sessions through <a href="/tunnel/">Cloudflare Tunnel</a> and get a public URL when using either <a href="/workers/wrangler/">Wrangler</a> or the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. This is useful when you need to share a preview, test a webhook, or access your app from another device.</p>
<p><img src="/assets/upstream/images/changelog/workers/vite-local-dev-tunnel.gif" alt="Vite local dev tunnel demo" /></p>
<p>This lets you either:</p>
<ul>
<li>start a temporary <a href="/tunnel/get-started/#quick-tunnels-development">Quick tunnel</a> with a random <code>*.trycloudflare.com</code> hostname, or</li>
<li>use an existing <a href="/tunnel/get-started/#create-a-tunnel">named tunnel</a> for a stable hostname and to restrict access with <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>.</li>
</ul>
<p>To start a tunnel, press <code>t</code> in Wrangler or <code>t + Enter</code> in Vite while your dev server is running. For details on setting up a named tunnel, refer to <a href="/workers/local-development/local-dev-tunnels/">Share a local dev server</a>.</p>


<h2 id="hyperdrive-exposes-database-connection-pool-size-metrics"><a href="/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/">Hyperdrive exposes database connection pool size metrics</a></h2>
<p><em>2026-05-15</em></p>
<p>You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a>, you can see <code>waitingClients</code>, <code>currentPoolSize</code>, <code>availablePoolSlots</code>, and <code>maxPoolSize</code> for each of your configurations.</p>
<p>A new <strong>Pool connections</strong> chart has been added to the <strong>Metrics</strong> tab of each Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>. You can use the location selector to drill down into specific locations hosting your connection pool by airport code.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-pool-size-metrics-chart.png" alt="Hyperdrive pool size metrics chart" /></p>
<p>The chart shows:</p>
<ul>
<li><strong>Waiting clients</strong>: Client requests waiting for an available connection.</li>
<li><strong>Open connections</strong>: Active connections to your database.</li>
<li><strong>Pool size maximum</strong>: Your configured origin connection limit.</li>
</ul>
<p>Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to <a href="/hyperdrive/platform/limits/#request-a-limit-increase">increase your Hyperdrive connection limit</a>.</p>
<h4 id="2026-05-15-hyperdrive-pool-size-metrics-pool-size-metrics">Pool size metrics</h4>
<p>The <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a> exposes the following key connection pool metrics for each Hyperdrive configuration:</p>
<p>Under <code>avg</code>:</p>
<ul>
<li><strong><code>currentPoolSize</code></strong> — Average number of connections currently open in the pool.</li>
<li><strong><code>availablePoolSlots</code></strong> — Average number of pool connections available for checkout.</li>
<li><strong><code>waitingClients</code></strong> — Average number of clients waiting for a connection from the pool.</li>
</ul>
<p>Under <code>max</code>:</p>
<ul>
<li><strong><code>maxPoolSize</code></strong> — Configured maximum size of the connection pool.</li>
<li><strong><code>currentPoolSize</code></strong> — Peak number of connections open in the pool.</li>
<li><strong><code>waitingClients</code></strong> — Peak number of clients waiting for a connection from the pool.</li>
</ul>
<p>For more information, refer to <a href="/hyperdrive/observability/metrics/">Metrics and analytics</a> and <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>


<h2 id="new-domains-tab-in-the-workers-dashboard"><a href="/changelog/post/2026-05-14-domains-tab/">New Domains tab in the Workers dashboard</a></h2>
<p><em>2026-05-14</em></p>
<p>In your Worker's dashboard, there is now a dedicated <strong>Domains</strong> tab where you can purchase a new domain through Cloudflare Registrar and have it automatically connected, add an <a href="/workers/configuration/routing/custom-domains/">existing domain</a>, and manage all of your Worker's routing in one place.</p>
<p><img src="/assets/upstream/images/workers/changelog/domains-tab.png" alt="The new Domains tab in the Workers dashboard" /></p>
<p>You can also enable or disable your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a> and <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a>, put them behind <a href="/cloudflare-one/access-controls/">Cloudflare Access</a> to require sign-in, and jump directly to <a href="/analytics/">analytics</a> or domain overview for any connected domain.</p>
<p>To get started, go to <strong>Workers &amp; Pages</strong>, select a Worker, and open the <strong>Domains</strong> tab.</p>
<div class="nb-dash-button"></div>


<h2 id="agents-sdk-v0-12-4-chat-recovery-routing-retries-durable-think-submissions-and-voice-connection-control"><a href="/changelog/post/2026-05-13-agents-sdk-v0.12.4/">Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control</a></h2>
<p><em>2026-05-13</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings more reliable chat recovery, fixes Agent state synchronization during reconnects, adds durable submissions for Think, exposes routing retry configuration, and adds connection control for Voice agents.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-chat-recovery-improvements">Chat recovery improvements</h4>
<p><code>@cloudflare/ai-chat</code> now keeps server turns running when a browser or client stream is interrupted. This is useful for long-running AI responses where users refresh the page, close a tab, or temporarily lose connection. Calling <code>stop()</code> still cancels the server turn.</p>
<p>Set <code>cancelOnClientAbort: true</code> if browser or client aborts should also cancel the server turn:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17661.md")</div>
<p>Notable bug fixes:</p>
<ul>
<li>Chat stream resume negotiation no longer throws when replay races with a closed WebSocket connection.</li>
<li>Recovered chat continuations no longer leave <code>useAgentChat</code> stuck in a streaming state when the original socket disconnects before a terminal response.</li>
<li>Approval auto-continuation preserves reasoning parts and persists continuation reasoning in the final message.</li>
<li><code>isServerStreaming</code> now resets correctly when a resumed stream moves from the fallback observer path to a transport-owned stream.</li>
</ul>
<h4 id="2026-05-13-agents-sdk-v0.12.4-agent-state-and-routing-fixes">Agent state and routing fixes</h4>
<p><code>agents@0.12.4</code> prevents duplicate initial state frames during WebSocket connection setup. This avoids stale initial state messages overwriting state updates already sent by the client.</p>
<p>Agent recovery is also more reliable when tool calls span a Durable Object restart. Recovery now defers user finish hooks until after agent startup and isolates hook failures, so one failed hook does not block other recovered runs from finalizing.</p>
<p><code>getAgentByName()</code> now supports <code>routingRetry</code> for transient Durable Object routing failures:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17662.md")</div>
<h4 id="2026-05-13-agents-sdk-v0.12.4-durable-think-submissions">Durable Think submissions</h4>
<p><code>@cloudflare/think</code> now supports durable programmatic submissions. <code>submitMessages()</code> provides durable acceptance, idempotent retries, status inspection, cancellation, and cleanup for server-driven turns that should continue after the caller returns.</p>
<p><code>Think.chat()</code> RPC turns now run inside chat recovery fibers and persist their stream chunks. Interrupted sub-agent turns can recover partial output instead of starting over.</p>
<p><code>ChatOptions.tools</code> has been removed from the TypeScript API. Define durable tools on the child agent or use agent tools for orchestration. Runtime <code>options.tools</code> values passed by legacy callers are ignored with a warning.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-think-message-pruning-behavior-change">Think message pruning behavior change</h4>
<p><code>@cloudflare/think</code> no longer applies <code>pruneMessages({ toolCalls: &quot;before-last-2-messages&quot; })</code> to model context by default. The previous default could strip client-side tool results from longer multi-turn flows.</p>
<p><code>truncateOlderMessages</code> still runs as before, so context cost remains bounded. Subclasses that relied on the old aggressive pruning can opt back in from <code>beforeTurn</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17663.md")</div>
<h4 id="2026-05-13-agents-sdk-v0.12.4-voice-agent-connection-control">Voice agent connection control</h4>
<p><code>@cloudflare/voice</code> adds an <code>enabled</code> option to <code>useVoiceAgent</code>. React apps can now delay creating and connecting a <code>VoiceClient</code> until prerequisites such as capability tokens are ready.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17664.md")</div>
<p>This release also fixes Workers AI speech-to-text session edge cases and <code>withVoice</code> text streaming from AI SDK <code>textStream</code> responses.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-other-improvements">Other improvements</h4>
<ul>
<li><strong>Streamable HTTP routing</strong> — Server-to-client requests now route through the originating POST stream when no standalone SSE stream is available.</li>
<li><strong>Structured tool output</strong> — Tool output shapes are preserved when truncating older messages or oversized persisted rows.</li>
<li><strong>Non-chat Think tool steps</strong> — Think agent-tool children can complete without emitting assistant text and can return structured output through <code>getAgentToolOutput</code>.</li>
<li><strong>Sub-agent schedules</strong> — Stale sub-agent schedule rows are pruned when their owning facet registry entry no longer exists.</li>
<li><strong><code>@cloudflare/codemode</code></strong> — Adds a browser-safe export with an iframe sandbox executor and resolves OpenAPI specs inside the sandbox to avoid Worker Loader RPC size limits.</li>
</ul>
<h4 id="2026-05-13-agents-sdk-v0.12.4-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/think@latest @cloudflare/voice@latest&#10;</code></pre>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>


<h2 id="waf-and-framework-adapter-mitigations-for-react-and-next-js-vulnerabilities"><a href="/changelog/post/2026-05-06-react-nextjs-vulnerabilities/">WAF and framework adapter mitigations for React and Next.js vulnerabilities</a></h2>
<p><em>2026-05-07 12:00:00 UTC</em></p>
<p>Multiple security vulnerabilities were disclosed by the React team and Vercel affecting React Server Components and Next.js. These include denial of service, middleware and proxy bypass, server-side request forgery, cross-site scripting, and cache poisoning issues across a range of severity levels.</p>
<p><strong>We strongly recommend updating your application and its dependencies immediately.</strong> Patched versions are available for React (<code>react-server-dom-webpack</code>, <code>react-server-dom-parcel</code>, and <code>react-server-dom-turbopack</code> <code>19.0.6</code>, <code>19.1.7</code>, and <code>19.2.6</code>) and Next.js (<code>15.5.16</code> and <code>16.2.5</code>).</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-waf-protections">WAF protections</h4>
<p>Cloudflare WAF rules deployed in response to prior React Server Component CVEs (<a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a> and <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a>) already provide coverage for the newly disclosed denial-of-service vulnerabilities. These rules are enabled by default with a Block action for all customers using the Cloudflare Managed Ruleset, including Free plan customers using the Free Managed Ruleset.</p>
<table>
<thead>
<tr>
<th>Ruleset</th>
<th>Rule description</th>
<th>Rule ID</th>
<th>Default action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a></td>
<td><code>2694f1610c0b471393b21aef102ec699</code></td>
<td>Block</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a></td>
<td><code>aaede80b4d414dc89c443cea61680354</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>The existing rules detect the underlying attack patterns generically. As a result, they apply to the new <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> denial-of-service vulnerability in Server Components and the corresponding Next.js advisory <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>.</p>
<p>Cloudflare is investigating whether WAF rules can be safely and effectively deployed for three of the high-severity advisories: <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>, <a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a>, and <a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a>. If it is possible to create a managed WAF rule that mitigates these CVEs and does not potentially break application behavior, Cloudflare will add additional managed WAF rules. These rules will be announced through the <a href="/waf/change-log/changelog/">WAF changelog</a>. Because these vulnerabilities were shared with Cloudflare with minimal advance notice, we are still investigating what WAF mitigations are possible.</p>
<p>Several of the disclosed vulnerabilities are not possible to block in WAF. We strongly recommend updating your applications so they are not purely reliant on WAF mitigations.</p>
<p>Customers on Pro, Business, or Enterprise plans should ensure that <a href="/waf/get-started/#1-deploy-the-cloudflare-managed-ruleset">Managed Rules are enabled</a>.</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-next-js-adapters">Next.js adapters</h4>
<p><strong>Vinext:</strong> <a href="https://github.com/cloudflare/vinext">Vinext</a> is a Vite plugin that reimplements the Next.js API surface. Vinext's latest release is not vulnerable to any of the disclosed CVEs. Vinext's architecture differs from stock Next.js in ways that sidestep the affected code paths. For example, it does not implement the PPR resume protocol, does not expose Pages Router data-route endpoints, and strips internal headers such as <code>x-nextjs-data</code> at request boundaries. As an extra layer of defense, we added a React <code>19.2.6</code> or later requirement when running <code>vinext init</code> (<a href="https://github.com/cloudflare/vinext/pull/1118">PR #1118</a>, <a href="https://github.com/cloudflare/vinext/pull/1112">PR #1112</a>) to prevent accidentally running a vulnerable version of React with Vinext.</p>
<p><strong>OpenNext on Cloudflare:</strong> OpenNext is an adapter that lets you deploy Next.js apps to the Cloudflare Workers platform. OpenNext itself is not directly vulnerable to the React denial-of-service CVE, but users must update the Next.js version in their application. The OpenNext team has updated the adapter to further harden against these vectors and released a new version of the Cloudflare adapter. Test fixtures and examples have been updated to use patched versions (<a href="https://github.com/opennextjs/opennextjs-cloudflare/pull/1255">PR #1255</a>).</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-summary-of-disclosed-vulnerabilities">Summary of disclosed vulnerabilities</h4>
<table>
<thead>
<tr>
<th>Advisory</th>
<th>Severity</th>
<th>Issue</th>
<th>WAF status</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a></td>
<td>High</td>
<td>Denial of service in Server Components</td>
<td><strong>WAF rules in place:</strong> <code>2694f1610c0b471393b21aef102ec699</code>, <code>aaede80b4d414dc89c443cea61680354</code><br/>Cloudflare is investigating additional managed WAF coverage</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a></td>
<td>High</td>
<td>Middleware bypass via segment-prefetch routes</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a></td>
<td>High</td>
<td>Denial of service via connection exhaustion in Cache Components</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv"><code>GHSA-492v-c6pp-mqqv</code></a></td>
<td>High</td>
<td>Middleware bypass via dynamic route parameter injection</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r"><code>GHSA-c4j6-fc7j-m34r</code></a></td>
<td>High</td>
<td>SSRF via WebSocket upgrades</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5"><code>GHSA-36qx-fr4f-26g5</code></a></td>
<td>High</td>
<td>Middleware bypass in Pages Router i18n</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q"><code>GHSA-ffhc-5mcf-pf4q</code></a></td>
<td>Moderate</td>
<td>XSS via CSP nonces</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h"><code>GHSA-gx5p-jg67-6x7h</code></a></td>
<td>Moderate</td>
<td>XSS in <code>beforeInteractive</code> scripts</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh"><code>GHSA-h64f-5h5j-jqjh</code></a></td>
<td>Moderate</td>
<td>Denial of service in Image Optimization API</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7"><code>GHSA-wfc6-r584-vfw7</code></a></td>
<td>Moderate</td>
<td>Cache poisoning in RSC responses</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949"><code>GHSA-vfv6-92ff-j949</code></a></td>
<td>Low</td>
<td>Cache poisoning via RSC cache-busting collisions</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq"><code>GHSA-3g8h-86w9-wvmq</code></a></td>
<td>Low</td>
<td>Middleware redirect cache poisoning</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
</tbody>
</table>


<h2 id="automatic-tracing-across-durable-object-and-worker-subrequests"><a href="/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/">Automatic tracing across Durable Object and Worker subrequests</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now get a single unified trace across Worker-to-Worker subrequests, with trace context propagating automatically. Previously, <a href="/workers/observability/traces/">automatic tracing</a> produced disconnected traces when a Worker called another Worker through a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> or <a href="/durable-objects/">Durable Object</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-04-28-worker-to-worker-context-prop.png" alt="Unified trace showing nested spans across a Durable Object subrequest and a service binding call" /></p>
<p>This means you can:</p>
<ul>
<li>Follow a request through your entire Worker architecture in one trace view</li>
<li>See service binding and Durable Object calls as nested child spans instead of separate traces</li>
<li>Debug cross-Worker request flows in the Cloudflare dashboard or in an external observability platform via <a href="/workers/observability/exporting-opentelemetry-data/">OpenTelemetry</a></li>
</ul>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> in your Wrangler configuration for traces to be recorded. Checkout <a href="/workers/observability/traces/">Workers tracing</a> to get started.</p>
<p>Up next, we are working on external trace context propagation using <a href="https://www.w3.org/TR/trace-context/">W3C Trace Context standards</a>, which will allow traces from your Workers to link with traces from services outside of Cloudflare.</p>


<h2 id="run-workflows-inside-dynamic-workers-with-the-cloudflare-dynamic-workflows-library"><a href="/changelog/post/2026-05-01-dynamic-workflows/">Run Workflows inside Dynamic Workers with the @cloudflare/dynamic-workflows library</a></h2>
<p><em>2026-05-01</em></p>
<p>You can now use <a href="https://github.com/cloudflare/dynamic-workflows"><code>@cloudflare/dynamic-workflows</code></a> to run a <a href="/workflows/">Workflow</a> inside a <a href="/dynamic-workers/">Dynamic Worker</a>, ensuring durable execution for code that is loaded at runtime.</p>
<p>The Worker Loader loads Dynamic Workers on demand, which previously made durability challenging. Even within a Dynamic Worker, a Workflow might sleep for hours or days between steps, and by the time it resumes, the original Dynamic Worker code would no longer be in memory.</p>
<p>The library solves this by tagging each Workflow instance with metadata that identifies which Dynamic Worker to load — for example, a tenant ID — then reloading the matching Dynamic Worker through the Worker Loader whenever a Workflow awakens.</p>
<p>Because Dynamic Workers are created on-demand, you do not have to register each Workflow up front or manage them individually. Load the Workflow code in the Dynamic Worker when it is needed, and the Workflows engine handles persistence and retries behind the scenes. Your Workflow code itself is unaffected by the routing and behaves as normal.</p>
<p>This unlocks patterns where the Workflow code itself is dynamic. For example, this is useful with:</p>
<ul>
<li><strong>SaaS platforms</strong> where each tenant defines their own automation, such as onboarding sequences, approval chains, or billing retry logic.</li>
<li><strong>AI agent frameworks</strong> where agents generate and execute multi-step plans at runtime, surviving restarts and waiting for human approval between tool calls.</li>
<li><strong>Multi-tenant job systems</strong> where each customer submits their own processing logic and every step persists progress and retries on failure.</li>
</ul>
<pre tabindex="0"><code class="language-ts">import {&#10;	createDynamicWorkflowEntrypoint,&#10;	DynamicWorkflowBinding,&#10;	wrapWorkflowBinding,&#10;	type WorkflowRunner,&#10;} from &quot;@cloudflare/dynamic-workflows&quot;;&#10;&#10;export { DynamicWorkflowBinding };&#10;&#10;interface Env {&#10;	WORKFLOWS: Workflow;&#10;	LOADER: WorkerLoader;&#10;}&#10;&#10;function loadTenant(env: Env, tenantId: string) {&#10;	return env.LOADER.get(tenantId, async () =&gt; ({&#10;		compatibilityDate: &quot;2026-01-01&quot;,&#10;		mainModule: &quot;index.js&quot;,&#10;		modules: { &quot;index.js&quot;: await fetchTenantCode(tenantId) },&#10;		// The Dynamic Worker uses this exactly like a real Workflow binding;&#10;		// every create() is tagged with { tenantId } automatically.&#10;		env: { WORKFLOWS: wrapWorkflowBinding({ tenantId }) },&#10;	}));&#10;}&#10;&#10;// The entrypoint name must match `class_name` in the workflows binding of your Wrangler config file.&#10;export const DynamicWorkflow = createDynamicWorkflowEntrypoint&lt;Env&gt;(&#10;	async ({ env, metadata }) =&gt; {&#10;		const stub = loadTenant(env, metadata.tenantId as string);&#10;		return stub.getEntrypoint(&quot;TenantWorkflow&quot;) as unknown as WorkflowRunner;&#10;	},&#10;);&#10;&#10;export default {&#10;	fetch(request: Request, env: Env) {&#10;		const tenantId = request.headers.get(&quot;x-tenant-id&quot;)!;&#10;		return loadTenant(env, tenantId).getEntrypoint().fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>For a full walkthrough, refer to the <a href="/dynamic-workers/usage/dynamic-workflows/">Dynamic Workflows guide</a>.</p>


<h2 id="introducing-billable-usage-dashboard-and-budget-alerts"><a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Introducing Billable Usage dashboard and Budget alerts</a></h2>
<p><em>2026-04-21</em></p>
<p>Pay-as-you-go customers can now monitor usage-based costs and configure spend alerts through two new features: the Billable Usage dashboard and Budget alerts.</p>
<h4 id="2026-04-13-billable-usage-dashboard-and-budget-alerts-billable-usage-dashboard">Billable Usage dashboard</h4>
<p>The Billable Usage dashboard provides daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.</p>
<p>The dashboard displays:</p>
<ul>
<li>A bar chart showing daily usage charges for your billing period</li>
<li>A sortable table breaking down usage by product, including total usage, billable usage, and cumulative costs</li>
<li>Ability to view previous billing periods</li>
</ul>
<p>Usage data aligns to your billing cycle, not the calendar month. The total usage cost shown at the end of a completed billing period matches the usage overage charges on your corresponding invoice.</p>
<p>To access the dashboard, go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-billable-usage-dashboard.png" alt="Screenshot of the Billable Usage dashboard in the Cloudflare dashboard" /></p>
<h4 id="2026-04-13-billable-usage-dashboard-and-budget-alerts-budget-alerts">Budget alerts</h4>
<p>Budget alerts allow you to set dollar-based thresholds for your account-level usage spend. You receive an email notification when your projected monthly spend reaches your configured threshold, giving you proactive visibility into your bill before month-end.</p>
<p>To configure a budget alert:</p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</li>
<li>Select <strong>Set Budget Alert</strong>.</li>
<li>Enter a budget threshold amount greater than $0.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>Alternatively, configure alerts via <strong>Notifications</strong> &gt; <strong>Add</strong> &gt; <strong>Budget Alert</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-budget-alert-modal.png" alt="Create Budget Alert modal in the Cloudflare dashboard" /></p>
<p>You can create multiple budget alerts at different dollar amounts. The notifications system automatically deduplicates alerts if multiple thresholds trigger at the same time. Budget alerts are calculated daily based on your usage trends and fire once per billing cycle when your projected spend first crosses your threshold.</p>
<p>Both features are available to Pay-as-you-go accounts with usage-based products (Workers, R2, Images, etc.). Enterprise contract accounts are not supported.</p>
<p>For more information, refer to the <a href="/billing/understand/usage-based-billing/">Usage based billing documentation</a>.</p>


<h2 id="websocket-binary-messages-now-delivered-as-blob-by-default"><a href="/changelog/post/2026-04-21-websocket-standard-binary-type/">WebSocket binary messages now delivered as Blob by default</a></h2>
<p><em>2026-04-21</em></p>
<p>Binary frames received on a <code>WebSocket</code> are now delivered to the <code>message</code> event as <a href="https://developer.mozilla.org/en-US/docs/Web/API/Blob"><code>Blob</code></a> objects by default. This matches the <a href="https://websockets.spec.whatwg.org/">WebSocket specification</a> and standard browser behavior. Previously, binary frames were always delivered as <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer"><code>ArrayBuffer</code></a>. The <a href="/workers/runtime-apis/websockets/#binarytype"><code>binaryType</code></a> property on <code>WebSocket</code> controls the delivery type on a per-WebSocket basis.</p>
<p>This change has been active for Workers with compatibility dates on or after <code>2026-03-17</code>, via the <a href="/workers/configuration/compatibility-flags/#websocket-standard-binary-type"><code>websocket_standard_binary_type</code></a> compatibility flag. We should have documented this change when it shipped but didn't. We're sorry for the trouble that caused. If your Worker handles binary WebSocket messages and assumes <code>event.data</code> is an <code>ArrayBuffer</code>, the frames will arrive as <code>Blob</code> instead, and a naive <code>instanceof ArrayBuffer</code> check will silently drop every frame.</p>
<p>To opt back into <code>ArrayBuffer</code> delivery, assign <code>binaryType</code> before calling <code>accept()</code>. This works regardless of the compatibility flag:</p>
<pre tabindex="0"><code class="language-js">const resp = await fetch(&quot;https://example.com&quot;, {&#10;	headers: { Upgrade: &quot;websocket&quot; },&#10;});&#10;const ws = resp.webSocket;&#10;&#10;// Opt back into ArrayBuffer delivery for this WebSocket.&#10;ws.binaryType = &quot;arraybuffer&quot;;&#10;ws.accept();&#10;&#10;ws.addEventListener(&quot;message&quot;, (event) =&gt; {&#10;	if (typeof event.data === &quot;string&quot;) {&#10;		// Text frame.&#10;	} else {&#10;		// event.data is an ArrayBuffer because we set binaryType above.&#10;	}&#10;});&#10;</code></pre>
<p>If you are not ready to migrate and want to keep <code>ArrayBuffer</code> as the default for all WebSockets in your Worker, add the <code>no_websocket_standard_binary_type</code> flag to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>This change has no effect on the Durable Object hibernatable WebSocket <a href="/durable-objects/best-practices/websockets/"><code>webSocketMessage</code></a> handler, which continues to receive binary data as <code>ArrayBuffer</code>.</p>
<p>For more information, refer to <a href="/workers/runtime-apis/websockets/#binary-messages">WebSockets binary messages</a>.</p>


<h2 id="increased-concurrency-creation-rate-and-queued-instance-limits-for-workflows-instances"><a href="/changelog/post/2026-04-15-workflows-limits-raised/">Increased concurrency, creation rate, and queued instance limits for Workflows instances</a></h2>
<p><em>2026-04-15 13:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> limits have been raised to the following:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent instances (running in parallel)</td>
<td>10,000</td>
<td>50,000</td>
</tr>
<tr>
<td>Instance creation rate (per account)</td>
<td>100/second per account</td>
<td>300/second per account, 100/second per workflow</td>
</tr>
<tr>
<td>Queued instances per Workflow <sup><a href="#2026-04-15-workflows-limits-raised-footnote-1">1</a></sup></td>
<td>1 million</td>
<td>2 million</td>
</tr>
</tbody>
</table>
<p>These increases apply to all users on the <a href="/workers/platform/pricing/">Workers Paid plan</a>. Refer to the <a href="/workflows/reference/limits/">Workflows limits documentation</a> for more details.</p>
<section class="footnotes"><h4 id="2026-04-15-workflows-limits-raised-footnotes">Footnotes</h4><ol><li id="2026-04-15-workflows-limits-raised-footnote-1">Queued instances are instances that have been created or awoken and are waiting for a concurrency slot.</li></ol></section>


<h2 id="local-explorer-for-local-resource-data"><a href="/changelog/post/2026-04-13-local-explorer/">Local Explorer for local resource data</a></h2>
<p><em>2026-04-13</em></p>
<p>Local Explorer is a browser-based interface and REST API for viewing and editing local resource data during development. It removes the need to write throwaway scripts or dig through <code>.wrangler/state</code> to understand what data your Worker has stored locally.</p>
<p>Local Explorer is available in Wrangler 4.82.1+ and the Cloudflare Vite plugin 1.32.0+. Start a local development session and press <code>e</code> in your terminal, or navigate to <code>/cdn-cgi/local/explorer</code> on your local dev server.</p>
<h4 id="2026-04-13-local-explorer-supported-resources">Supported resources</h4>
<p>Local Explorer supports five resource types and works across multiple workers running locally:</p>
<ul>
<li><strong><a href="/kv/">KV</a></strong> — Browse keys, view values and metadata, create, update, and delete key-value pairs.</li>
<li><strong><a href="/r2/">R2</a></strong> — List objects, view metadata, upload files, and delete objects. Supports directory views and multi-select.</li>
<li><strong><a href="/d1/">D1</a></strong> — Browse tables and rows, run arbitrary SQL queries, and edit schemas in a full data studio.</li>
<li><strong><a href="/durable-objects/">Durable Objects</a></strong> (SQLite storage) — Browse individual object SQLite tables, run SQL queries, and edit schemas.</li>
<li><strong><a href="/workflows/">Workflows</a></strong> — List instances, view status and step history, trigger new runs, and pause, resume, restart, or terminate instances.</li>
</ul>
<h4 id="2026-04-13-local-explorer-openapi-powered-rest-api">OpenAPI-powered REST API</h4>
<p>Local Explorer exposes a REST API at <code>/cdn-cgi/local/explorer/api</code> that provides programmatic access to the same operations available in the browser. The root endpoint returns an <a href="https://www.openapis.org/">OpenAPI specification</a> describing all available endpoints, parameters, and response formats.</p>
<pre tabindex="0"><code class="language-sh">curl http://localhost:8787/cdn-cgi/local/explorer/api&#10;</code></pre>
<p>Point an AI coding agent at <code>/cdn-cgi/local/explorer/api</code> and it can discover and interact with your local resources without manual setup. This enables iterative development loops where an agent can populate test data in KV or D1, inspect Durable Object state, trigger Workflow runs, or upload files to R2.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>


<h2 id="relaxed-simultaneous-connection-limiting-for-workers"><a href="/changelog/post/2026-04-09-relaxed-connection-limiting/">Relaxed simultaneous connection limiting for Workers</a></h2>
<p><em>2026-04-09</em></p>
<p>The <a href="/workers/platform/limits/#simultaneous-open-connections">simultaneous open connections limit</a> has been relaxed. Previously, each Worker invocation was limited to six open connections at a time for the entire lifetime of each connection, including while reading the response body. Now, a connection is freed as soon as response headers arrive, so the six-connection limit only constrains how many connections can be in the initial &quot;waiting for headers&quot; phase simultaneously.</p>
<h4 id="2026-04-09-relaxed-connection-limiting-before-new-connections-are-blocked-until-an-earlier-connection-fully-completes">Before: New connections are blocked until an earlier connection fully completes</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-limit-before.svg" alt="A 7th fetch is queued until an earlier connection fully completes, including reading its entire response body" /></p>
<h4 id="2026-04-09-relaxed-connection-limiting-after-new-connections-can-start-as-soon-as-response-headers-arrive">After: New connections can start as soon as response headers arrive</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-limit-after.svg" alt="A 7th fetch starts as soon as any earlier connection receives its response headers" /></p>
<p>This means Workers can now have many more connections open at the same time without queueing, as long as no more than six are waiting for their initial response. This eliminates the <code>Response closed due to connection limit</code> exception that could previously occur when the runtime canceled stalled connections to prevent deadlocks.</p>
<p>Previously, the runtime used a deadlock avoidance algorithm that watched each open connection for I/O activity. If all six connections appeared idle — even momentarily — the runtime would cancel the least-recently-used connection to make room for new requests. In practice, this heuristic was fragile. For example, when a response used <code>Content-Encoding: gzip</code>, the runtime's internal decompression created brief gaps between read and write operations. During these gaps, the connection appeared stalled despite being actively read by the Worker. If multiple connections hit these gaps at the same time, the runtime could spuriously cancel a connection that was working correctly. By only counting connections during the waiting-for-headers phase — where the runtime is fully in control and there is no ambiguity about whether the connection is active — this class of bug is eliminated entirely.</p>
<h4 id="2026-04-09-relaxed-connection-limiting-before-connections-could-be-canceled-during-brief-internal-pauses">Before: Connections could be canceled during brief internal pauses</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-cancel-before.svg" alt="A connection with gaps from gzip decompression appears idle and is canceled by the runtime" /></p>
<h4 id="2026-04-09-relaxed-connection-limiting-after-connections-complete-normally-regardless-of-internal-pauses">After: Connections complete normally regardless of internal pauses</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-cancel-after.svg" alt="The same connection completes normally because the body phase is no longer counted against the limit" /></p>


<h2 id="websockets-now-automatically-reply-to-close-frames"><a href="/changelog/post/2026-04-07-websocket-auto-reply-to-close/">WebSockets now automatically reply to Close frames</a></h2>
<p><em>2026-04-07</em></p>
<p>The Workers runtime now automatically sends a reciprocal Close frame when it receives a Close frame from the peer. The <code>readyState</code> transitions to <code>CLOSED</code> before the <code>close</code> event fires. This matches the <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close_event">WebSocket specification</a> and standard browser behavior.</p>
<p>This change is enabled by default for Workers using compatibility dates on or after <code>2026-04-07</code> (via the <a href="/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close"><code>web_socket_auto_reply_to_close</code></a> compatibility flag). Existing code that manually calls <code>close()</code> inside the <code>close</code> event handler will continue to work — the call is silently ignored when the WebSocket is already closed.</p>
<pre tabindex="0"><code class="language-js">const [client, server] = Object.values(new WebSocketPair());&#10;server.accept();&#10;&#10;server.addEventListener(&quot;close&quot;, (event) =&gt; {&#10;	// readyState is already CLOSED — no need to call server.close().&#10;	console.log(server.readyState); // WebSocket.CLOSED&#10;	console.log(event.code); // 1000&#10;	console.log(event.wasClean); // true&#10;});&#10;</code></pre>
<h4 id="2026-04-07-websocket-auto-reply-to-close-half-open-mode-for-websocket-proxying">Half-open mode for WebSocket proxying</h4>
<p>The automatic close behavior can interfere with WebSocket proxying, where a Worker sits between a client and a backend and needs to coordinate the close on both sides independently. To support this use case, pass <code>{ allowHalfOpen: true }</code> to <code>accept()</code>:</p>
<pre tabindex="0"><code class="language-js">const [client, server] = Object.values(new WebSocketPair());&#10;&#10;server.accept({ allowHalfOpen: true });&#10;&#10;server.addEventListener(&quot;close&quot;, (event) =&gt; {&#10;	// readyState is still CLOSING here, giving you time&#10;	// to coordinate the close on the other side.&#10;	console.log(server.readyState); // WebSocket.CLOSING&#10;&#10;	// Manually close when ready.&#10;	server.close(event.code, &quot;done&quot;);&#10;});&#10;</code></pre>
<p>For more information, refer to <a href="/workers/runtime-apis/websockets/#close-behavior">WebSockets Close behavior</a>.</p>


<h2 id="all-wrangler-commands-for-workflows-now-support-local-development"><a href="/changelog/post/2026-04-01-wrangler-workflows-local/">All Wrangler commands for Workflows now support local development</a></h2>
<p><em>2026-04-01 12:00:00 UTC</em></p>
<p>All <code>wrangler workflows</code> commands now accept a <code>--local</code> flag to target a Workflow running in a local <code>wrangler dev</code> session instead of the production API.</p>
<p>You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows list --local&#10;npx wrangler workflows trigger my-workflow --local&#10;npx wrangler workflows instances list my-workflow --local&#10;npx wrangler workflows instances pause my-workflow &lt;INSTANCE_ID&gt; --local&#10;npx wrangler workflows instances send-event my-workflow &lt;INSTANCE_ID&gt; --type my-event --local&#10;</code></pre>
<p>All commands also accept <code>--port</code> to target a specific <code>wrangler dev</code> session (defaults to <code>8787</code>).</p>
<p>For more information, refer to <a href="/workflows/build/local-development/">Workflows local development</a>.</p>


<h2 id="deploy-hooks-are-now-available-for-workers-builds"><a href="/changelog/post/2026-04-01-deploy-hooks/">Deploy Hooks are now available for Workers Builds</a></h2>
<p><em>2026-04-01</em></p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports Deploy Hooks — trigger builds from your headless CMS, a Cron Trigger, a Slack bot, or any system that can send an HTTP request.</p>
<p>Each Deploy Hook is a unique URL tied to a specific branch. Send it a <code>POST</code> and your Worker builds and deploys.</p>
<pre tabindex="0"><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/&lt;DEPLOY_HOOK_ID&gt;&quot;&#10;</code></pre>
<p>To create one, go to <strong>Workers &amp; Pages</strong> &gt; your Worker &gt; <strong>Settings</strong> &gt; <strong>Builds</strong> &gt; <strong>Deploy Hooks</strong>.</p>
<p>Since a Deploy Hook is a URL, you can also call it from another Worker. For example, a Worker with a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> can rebuild your project on a schedule:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17803.md")</div>
<p>You can also use Deploy Hooks to <a href="/workers/ci-cd/builds/deploy-hooks/#cms-integration">rebuild when your CMS publishes new content</a> or <a href="/workers/ci-cd/builds/deploy-hooks/#deploy-from-a-slack-slash-command">deploy from a Slack slash command</a>.</p>
<h4 id="2026-04-01-deploy-hooks-built-in-optimizations">Built-in optimizations</h4>
<ul>
<li><strong>Automatic deduplication</strong>: If a Deploy Hook fires multiple times before the first build starts running, redundant builds are automatically skipped. This keeps your build queue clean when webhooks retry or CMS events arrive in bursts.</li>
<li><strong>Last triggered</strong>: The dashboard shows when each hook was last triggered.</li>
<li><strong>Build source</strong>: Your Worker's build history shows which Deploy Hook started each build by name.</li>
</ul>
<p>Deploy Hooks are rate limited to 10 builds per minute per Worker and 100 builds per minute per account. For all limits, see <a href="/workers/ci-cd/builds/limits-and-pricing/">Limits &amp; pricing</a>.</p>
<p>To get started, read the <a href="/workers/ci-cd/builds/deploy-hooks/">Deploy Hooks documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/2/">Previous</a><span>Page 3 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/4/">Next</a></nav>
