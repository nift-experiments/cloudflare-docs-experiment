---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers/4/
  description: '2026-04-01'
  full_title: workers changelog - page 4 | Cloudflare Docs
  head_html: <title>workers changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-04-01"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-04-01"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers/4/#page","headline":"workers changelog - page 4 | Cloudflare Docs","description":"2026-04-01","url":"https://developers.cloudflare.com/changelog/product/workers/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-l4-transport-telemetry-fields-in-workers"><a href="/changelog/post/2026-04-01-l4-transport-telemetry-fields/">New L4 transport telemetry fields in Workers</a></h2>
<p><em>2026-04-01</em></p>
<p>Three new properties are now available on <code>request.cf</code> in Workers that expose Layer 4 transport telemetry from the client connection. These properties let your Worker make decisions based on real-time connection quality signals — such as round-trip time and data delivery rate — without requiring any client-side changes.</p>
<p>Previously, this telemetry was only available via the <code>Server-Timing: cfL4</code> response header. These new properties surface the same data directly in the Workers runtime, so you can use it for routing, logging, or response customization.</p>
<h4 id="2026-04-01-l4-transport-telemetry-fields-new-properties">New properties</h4>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>clientTcpRtt</code></td>
<td>number | undefined</td>
<td>The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for TCP connections (HTTP/1, HTTP/2). For example, <code>22</code>.</td>
</tr>
<tr>
<td><code>clientQuicRtt</code></td>
<td>number | undefined</td>
<td>The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for QUIC connections (HTTP/3). For example, <code>42</code>.</td>
</tr>
<tr>
<td><code>edgeL4</code></td>
<td>Object | undefined</td>
<td>Layer 4 transport statistics. Contains <code>deliveryRate</code> (number) — the most recent data delivery rate estimate for the connection, in bytes per second. For example, <code>123456</code>.</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-01-l4-transport-telemetry-fields-example-log-connection-quality-metrics">Example: Log connection quality metrics</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const cf = request.cf;&#10;&#10;    const rtt = cf.clientTcpRtt ?? cf.clientQuicRtt ?? 0;&#10;    const deliveryRate = cf.edgeL4?.deliveryRate ?? 0;&#10;    const transport = cf.clientTcpRtt ? &quot;TCP&quot; : &quot;QUIC&quot;;&#10;&#10;    console.log(`Transport: ${transport}, RTT: ${rtt}ms, Delivery rate: ${deliveryRate} B/s`);&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;X-Client-RTT&quot;, String(rtt));&#10;    headers.set(&quot;X-Delivery-Rate&quot;, String(deliveryRate));&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/workers/runtime-apis/request/">Workers Runtime APIs: Request</a>.</p>


<h2 id="new-rfc-9440-mtls-certificate-fields-in-workers"><a href="/changelog/post/2026-03-27-rfc9440-mtls-fields/">New RFC 9440 mTLS certificate fields in Workers</a></h2>
<p><em>2026-03-27</em></p>
<p>Four new fields are now available on <code>request.cf.tlsClientAuth</code> in Workers for requests that include a mutual TLS (mTLS) client certificate. These fields encode the client certificate and its intermediate chain in <a href="https://www.rfc-editor.org/rfc/rfc9440">RFC 9440</a> format — the same standard format used by the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> HTTP headers — so your Worker can forward them directly to your origin without any custom parsing or encoding logic.</p>
<h4 id="2026-03-27-rfc9440-mtls-fields-new-fields">New fields</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>certRFC9440</code></td>
<td>String</td>
<td>The client leaf certificate in RFC 9440 format (<code>:base64-DER:</code>). Empty if no client certificate was presented.</td>
</tr>
<tr>
<td><code>certRFC9440TooLarge</code></td>
<td>Boolean</td>
<td><code>true</code> if the leaf certificate exceeded 10 KB and was omitted from <code>certRFC9440</code>.</td>
</tr>
<tr>
<td><code>certChainRFC9440</code></td>
<td>String</td>
<td>The intermediate certificate chain in RFC 9440 format as a comma-separated list. Empty if no intermediates were sent or if the chain exceeded 16 KB.</td>
</tr>
<tr>
<td><code>certChainRFC9440TooLarge</code></td>
<td>Boolean</td>
<td><code>true</code> if the intermediate chain exceeded 16 KB and was omitted from <code>certChainRFC9440</code>.</td>
</tr>
</tbody>
</table>
<h4 id="2026-03-27-rfc9440-mtls-fields-example-forwarding-client-certificate-headers-to-your-origin">Example: forwarding client certificate headers to your origin</h4>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request) {&#10;    const tls = request.cf.tlsClientAuth;&#10;&#10;    // Only forward if cert was verified and chain is complete&#10;    if (!tls || !tls.certVerified || tls.certRevoked || tls.certChainRFC9440TooLarge) {&#10;      return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;    }&#10;&#10;    const headers = new Headers(request.headers);&#10;    headers.set(&quot;Client-Cert&quot;, tls.certRFC9440);&#10;    headers.set(&quot;Client-Cert-Chain&quot;, tls.certChainRFC9440);&#10;&#10;    return fetch(new Request(request, { headers }));&#10;  },&#10;};&#10;</code></pre>
<p>For more information, refer to <a href="/ssl/client-certificates/client-certificate-variables/#workers-variables">Client certificate variables</a> and <a href="/cloudflare-one/access-controls/service-credentials/mutual-tls-authentication/">Mutual TLS authentication</a>.</p>


<h2 id="access-durable-object-jurisdiction-via-ctx-id-jurisdiction"><a href="/changelog/post/2026-03-26-durable-object-id-jurisdiction/">Access Durable Object jurisdiction via `ctx.id.jurisdiction`</a></h2>
<p><em>2026-03-26</em></p>
<p><code>ctx.id.jurisdiction</code> inside a Durable Object now reports the <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a> the object was created in — for example <code>&quot;eu&quot;</code> when accessed through <code>env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)</code> — so you can make region-aware decisions without passing the jurisdiction through method arguments or persisting it in storage. For the full list of ID-construction paths that preserve <code>jurisdiction</code>, refer to the <a href="/durable-objects/api/id/#jurisdiction">Durable Object ID documentation</a>.</p>
<pre tabindex="0"><code class="language-js">export class RegionalRoom extends DurableObject {&#10;	async fetch(request) {&#10;		// &quot;eu&quot; when accessed through env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;)&#10;		const region = this.ctx.id.jurisdiction;&#10;		return new Response(`Hello from ${region ?? &quot;the default region&quot;}!`);&#10;	}&#10;}&#10;&#10;// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const stub = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;).getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p><code>ctx.id.jurisdiction</code> is <code>undefined</code> for Durable Objects that were not created in a jurisdiction-restricted namespace. Alarms scheduled before 2026-03-15 also do not have <code>jurisdiction</code> stored; to backfill the value, reschedule the alarm from a <code>fetch()</code> or RPC handler.</p>


<h2 id="declare-required-secrets-in-your-wrangler-configuration"><a href="/changelog/post/2026-03-24-secrets-config-property/">Declare required secrets in your Wrangler configuration</a></h2>
<p><em>2026-03-25</em></p>
<p>The new <code>secrets</code> configuration property lets you declare the secret names your Worker requires in your Wrangler configuration file. Required secrets are validated during local development and deploy, and used as the source of truth for type generation.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17802.md")</div>
<h4 id="2026-03-24-secrets-config-property-local-development">Local development</h4>
<p>When <code>secrets</code> is defined, <code>wrangler dev</code> and <code>vite dev</code> load only the keys listed in <code>secrets.required</code> from <code>.dev.vars</code> or <code>.env</code>/<code>process.env</code>. Additional keys in those files are excluded. If any required secrets are missing, a warning is logged listing the missing names.</p>
<h4 id="2026-03-24-secrets-config-property-type-generation">Type generation</h4>
<p><code>wrangler types</code> generates typed bindings from <code>secrets.required</code> instead of inferring names from <code>.dev.vars</code> or <code>.env</code>. This lets you run type generation in CI or other environments where those files are not present. Per-environment secrets are supported — the aggregated <code>Env</code> type marks secrets that only appear in some environments as optional.</p>
<h4 id="2026-03-24-secrets-config-property-deploy">Deploy</h4>
<p><code>wrangler deploy</code> and <code>wrangler versions upload</code> validate that all secrets in <code>secrets.required</code> are configured on the Worker before the operation succeeds. If any required secrets are missing, the command fails with an error listing which secrets need to be set.</p>
<p>For more information, refer to the <a href="/workers/wrangler/configuration/#secrets-configuration-property"><code>secrets</code> configuration property</a> reference.</p>


<h2 id="dynamic-workers-now-in-open-beta"><a href="/changelog/post/2026-03-24-dynamic-workers-open-beta/">Dynamic Workers, now in open beta</a></h2>
<p><em>2026-03-24</em></p>
<p><a href="/dynamic-workers/">Dynamic Workers</a> are now in <a href="https://blog.cloudflare.com/dynamic-workers/">open beta</a> for all paid Workers users. You can now have a Worker spin up other Workers, called Dynamic Workers, at runtime to execute code on-demand in a secure, sandboxed environment. Dynamic Workers start in milliseconds, making them well suited for fast, secure code execution at scale.</p>
<h4 id="2026-03-24-dynamic-workers-open-beta-use-dynamic-workers-for">Use Dynamic Workers for</h4>
<ul>
<li><strong><a href="/agents/tools/codemode/">Code Mode</a></strong>: LLMs are trained to write code. Run tool-calling logic written in code instead of stepping through many tool calls, which can save up to 80% in inference tokens and cost.</li>
<li><strong>AI agents executing code</strong>: Run code for tasks like data analysis, file transformation, API calls, and chained actions.</li>
<li><strong>Running AI-generated code</strong>: Run generated code for prototypes, projects, and automations in a secure, isolated sandboxed environment.</li>
<li><strong>Fast development and previews</strong>: Load prototypes, previews, and playgrounds in milliseconds.</li>
<li><strong>Custom automations</strong>: Create custom tools on the fly that execute a task, call an integration, or automate a workflow.</li>
</ul>
<h4 id="2026-03-24-dynamic-workers-open-beta-executing-dynamic-workers">Executing Dynamic Workers</h4>
<p>Dynamic Workers support two loading modes:</p>
<ul>
<li><code>load(code)</code> — for one-time code execution (equivalent to calling <code>get()</code> with a null ID).</li>
<li><code>get(id, callback)</code> — caches a Dynamic Worker by ID so it can stay warm across requests. Use this when the same code will receive subsequent requests.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17801.md")</div>
<h4 id="2026-03-24-dynamic-workers-open-beta-helper-libraries-for-dynamic-workers">Helper libraries for Dynamic Workers</h4>
<p>Here are 3 new libraries to help you build with Dynamic Workers:</p>
<ul>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a></strong>: Replace individual tool calls with a single <code>code()</code> tool, so LLMs write and execute TypeScript that orchestrates multiple API calls in one pass.</p>
</li>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a></strong>: Resolve npm dependencies and bundle source files into ready-to-load modules for Dynamic Workers, all at runtime.</p>
</li>
<li>
<p><strong><a href="https://www.npmjs.com/package/@cloudflare/shell"><code>@cloudflare/shell</code></a></strong>: Give your agent a virtual filesystem inside a Dynamic Worker with persistent storage backed by SQLite and R2.</p>
</li>
</ul>
<h4 id="2026-03-24-dynamic-workers-open-beta-try-it-out">Try it out</h4>
<p><strong>Dynamic Workers Starter</strong></p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Use this <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers">starter</a> to deploy a Worker that can load and execute Dynamic Workers.</p>
<p><strong>Dynamic Workers Playground</strong></p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Deploy the <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">Dynamic Workers Playground</a> to write or import code, bundle it at runtime with <code>@cloudflare/worker-bundler</code>, execute it through a Dynamic Worker, and see real-time responses and execution logs.</p>
<p>For the full API reference and configuration options, refer to the <a href="/dynamic-workers/">Dynamic Workers documentation</a>.</p>
<h4 id="2026-03-24-dynamic-workers-open-beta-pricing">Pricing</h4>
<p>Dynamic Workers <a href="/dynamic-workers/pricing/">pricing</a> is based on three dimensions: Dynamic Workers created daily, requests, and CPU time.</p>
<table>
<thead>
<tr>
<th></th>
<th>Included</th>
<th>Additional usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Dynamic Workers created daily</strong></td>
<td>1,000 unique Dynamic Workers per month</td>
<td>+$0.002 per Dynamic Worker per day</td>
</tr>
<tr>
<td><strong>Requests</strong> ¹</td>
<td>10 million per month</td>
<td>+$0.30 per million requests</td>
</tr>
<tr>
<td><strong>CPU time</strong> ¹</td>
<td>30 million CPU milliseconds per month</td>
<td>+$0.02 per million CPU milliseconds</td>
</tr>
</tbody>
</table>
<p>¹ Uses <a href="/workers/platform/pricing/#workers">Workers Standard rates</a> and will appear as part of your existing Workers bill, not as separate Dynamic Workers charges.</p>
<p>Note: Dynamic Workers requests and CPU time are already billed as part of your Workers plan and will count toward your Workers requests and CPU usage. The Dynamic Workers created daily charge is not yet active — you will not be billed for the number of Dynamic Workers created at this time. Pricing information is shared in advance so you can estimate future costs.</p>


<h2 id="workflow-instances-now-support-pause-resume-restart-and-terminate-methods-in-local-development"><a href="/changelog/post/2026-03-23-local-dev-instance-methods/">Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development</a></h2>
<p><em>2026-03-23 12:00:00 UTC</em></p>
<p>Workflow instance methods <code>pause()</code>, <code>resume()</code>, <code>restart()</code>, and <code>terminate()</code> are now available in local development when using <code>wrangler dev</code>.</p>
<p>You can now test the full Workflow instance lifecycle locally:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.MY_WORKFLOW.create({&#10;	id: &quot;my-instance-id&quot;,&#10;});&#10;&#10;await instance.pause(); // pauses a running workflow instance&#10;await instance.resume(); // resumes a paused instance&#10;await instance.restart(); // restarts the instance from the beginning&#10;await instance.terminate(); // terminates the instance immediately&#10;</code></pre>


<h2 id="agents-sdk-v0-8-0-readable-state-idempotent-schedules-typed-agentclient-and-zod-4"><a href="/changelog/post/2026-03-23-agents-sdk-v0.8.0/">Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4</a></h2>
<p><em>2026-03-23</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> exposes agent state as a readable property, prevents duplicate schedule rows across Durable Object restarts, brings full TypeScript inference to <code>AgentClient</code>, and migrates to Zod 4.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-readable-state-on-useagent-and-agentclient">Readable <code>state</code> on <code>useAgent</code> and <code>AgentClient</code></h4>
<p>Both <code>useAgent</code> (React) and <code>AgentClient</code> (vanilla JS) now expose a <code>state</code> property that reflects the current agent state. Previously, reading state required manually tracking it through the <code>onStateUpdate</code> callback.</p>
<p><strong>React (<code>useAgent</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17655.md")</div>
<p><code>agent.state</code> is reactive — the component re-renders when state changes from either the server or a client-side <code>setState()</code> call.</p>
<p><strong>Vanilla JS (<code>AgentClient</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17656.md")</div>
<p>State starts as <code>undefined</code> and is populated when the server sends the initial state on connect (from <code>initialState</code>) or when <code>setState()</code> is called. Use optional chaining (<code>agent.state?.field</code>) for safe access. The <code>onStateUpdate</code> callback continues to work as before — the new <code>state</code> property is additive.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-idempotent-schedule">Idempotent <code>schedule()</code></h4>
<p><code>schedule()</code> now supports an <code>idempotent</code> option that deduplicates by <code>(type, callback, payload)</code>, preventing duplicate rows from accumulating when called in places that run on every Durable Object restart such as <code>onStart()</code>.</p>
<p><strong>Cron schedules are idempotent by default.</strong> Calling <code>schedule(&quot;0 * * * *&quot;, &quot;tick&quot;)</code> multiple times with the same callback, expression, and payload returns the existing schedule row instead of creating a new one. Pass <code>{ idempotent: false }</code> to override.</p>
<p>Delayed and date-scheduled types support opt-in idempotency:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17657.md")</div>
<p>Two new warnings help catch common foot-guns:</p>
<ul>
<li>Calling <code>schedule()</code> inside <code>onStart()</code> without <code>{ idempotent: true }</code> emits a <code>console.warn</code> with actionable guidance (once per callback; skipped for cron and when <code>idempotent</code> is set explicitly).</li>
<li>If an alarm cycle processes 10 or more stale one-shot rows for the same callback, the SDK emits a <code>console.warn</code> and a <code>schedule:duplicate_warning</code> diagnostics channel event.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-typed-agentclient-with-call-inference-and-stub-proxy">Typed <code>AgentClient</code> with <code>call</code> inference and <code>stub</code> proxy</h4>
<p><code>AgentClient</code> now accepts an optional agent type parameter for full type inference on RPC calls, matching the typed experience already available with <code>useAgent</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17658.md")</div>
<p>State is automatically inferred from the agent type, so <code>onStateUpdate</code> is also typed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17659.md")</div>
<p>Existing untyped usage continues to work without changes. The RPC type utilities (<code>AgentMethods</code>, <code>AgentStub</code>, <code>RPCMethods</code>) are now exported from <code>agents/client</code> for advanced typing scenarios.
<code>agents</code>, <code>@cloudflare/ai-chat</code>, and <code>@cloudflare/codemode</code> now require <code>zod ^4.0.0</code>. Zod v3 is no longer supported.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Turn serialization</strong> — <code>onChatMessage()</code> and <code>_reply()</code> work is now queued so user requests, tool continuations, and <code>saveMessages()</code> never stream concurrently.</li>
<li><strong>Duplicate messages on stop</strong> — Clicking stop during an active stream no longer splits the assistant message into two entries.</li>
<li><strong>Duplicate messages after tool calls</strong> — Orphaned client IDs no longer leak into persistent storage.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-keepalive-and-keepalivewhile-are-no-longer-experimental"><code>keepAlive()</code> and <code>keepAliveWhile()</code> are no longer experimental</h4>
<p><code>keepAlive()</code> now uses a lightweight in-memory ref count instead of schedule rows. Multiple concurrent callers share a single alarm cycle. The <code>@experimental</code> tag has been removed from both <code>keepAlive()</code> and <code>keepAliveWhile()</code>.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-codemode-tanstack-ai-integration"><code>@cloudflare/codemode</code>: TanStack AI integration</h4>
<p>A new entry point <code>@cloudflare/codemode/tanstack-ai</code> adds support for <a href="https://tanstack.com/ai">TanStack AI's</a> <code>chat()</code> as an alternative to the Vercel AI SDK's <code>streamText()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17660.md")</div>
<h4 id="2026-03-23-agents-sdk-v0.8.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="manage-cloudflare-tunnels-with-wrangler"><a href="/changelog/post/2026-03-19-wrangler-tunnel-commands/">Manage Cloudflare Tunnels with Wrangler</a></h2>
<p><em>2026-03-19</em></p>
<p>You can now manage <a href="/tunnel/">Cloudflare Tunnels</a> directly from <a href="/workers/wrangler/">Wrangler</a>, the CLI for the Cloudflare Developer Platform. The new <a href="/workers/wrangler/commands/tunnel/"><code>wrangler tunnel</code></a> commands let you create, run, and manage tunnels without leaving your terminal.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/wrangler-tunnel.gif" alt="Wrangler tunnel commands demo" /></p>
<p>Available commands:</p>
<ul>
<li><code>wrangler tunnel create</code> — Create a new remotely managed tunnel.</li>
<li><code>wrangler tunnel list</code> — List all tunnels in your account.</li>
<li><code>wrangler tunnel info</code> — Display details about a specific tunnel.</li>
<li><code>wrangler tunnel delete</code> — Delete a tunnel.</li>
<li><code>wrangler tunnel run</code> — Run a tunnel using the cloudflared daemon.</li>
<li><code>wrangler tunnel quick-start</code> — Start a free, temporary tunnel without an account using <a href="/tunnel/get-started/#quick-tunnels-development">Quick Tunnels</a>.</li>
</ul>
<p>Wrangler handles downloading and managing the <a href="/tunnel/downloads/">cloudflared</a> binary automatically. On first use, you will be prompted to download <code>cloudflared</code> to a local cache directory.</p>
<p>These commands are currently experimental and may change without notice.</p>
<p>To get started, refer to the <a href="/workers/wrangler/commands/tunnel/">Wrangler tunnel commands documentation</a>.</p>


<h2 id="cloudflare-codemode-v0-2-1-mcp-barrel-export-zero-dependency-main-entry-point-and-custom-sandbox-modules"><a href="/changelog/post/2026-03-17-codemode-sdk-v0.2.1/">@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules</a></h2>
<p><em>2026-03-17</em></p>
<p>The latest releases of <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> add a new MCP barrel export, remove <code>ai</code> and <code>zod</code> as required peer dependencies from the main entry point, and give you more control over the sandbox.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-new-cloudflare-codemode-mcp-export">New <code>@cloudflare/codemode/mcp</code> export</h4>
<p>A new <code>@cloudflare/codemode/mcp</code> entry point provides two functions that wrap MCP servers with Code Mode:</p>
<ul>
<li><strong><code>codeMcpServer({ server, executor })</code></strong> — wraps an existing MCP server with a single <code>code</code> tool where each upstream tool becomes a typed <code>codemode.*</code> method.</li>
<li><strong><code>openApiMcpServer({ spec, executor, request })</code></strong> — creates <code>search</code> and <code>execute</code> MCP tools from an OpenAPI spec with host-side request proxying and automatic <code>$ref</code> resolution.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17652.md")</div>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-zero-dependency-main-entry-point">Zero-dependency main entry point</h4>
<p><strong>Breaking change in v0.2.0:</strong> <code>generateTypes</code> and the <code>ToolDescriptor</code> / <code>ToolDescriptors</code> types have moved to <code>@cloudflare/codemode/ai</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17653.md")</div>
<p>The main entry point (<code>@cloudflare/codemode</code>) no longer requires the <code>ai</code> or <code>zod</code> peer dependencies. It now exports:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sanitizeToolName</code></td>
<td>Sanitize tool names into valid JS identifiers</td>
</tr>
<tr>
<td><code>normalizeCode</code></td>
<td>Normalize LLM-generated code into async arrow functions</td>
</tr>
<tr>
<td><code>generateTypesFromJsonSchema</code></td>
<td>Generate TypeScript type definitions from plain JSON Schema</td>
</tr>
<tr>
<td><code>jsonSchemaToType</code></td>
<td>Convert a single JSON Schema to a TypeScript type string</td>
</tr>
<tr>
<td><code>DynamicWorkerExecutor</code></td>
<td>Sandboxed code execution via Dynamic Worker Loader</td>
</tr>
<tr>
<td><code>ToolDispatcher</code></td>
<td>RPC target for dispatching tool calls from sandbox to host</td>
</tr>
</tbody>
</table>
<p>The <code>ai</code> and <code>zod</code> peer dependencies are now optional — only required when importing from <code>@cloudflare/codemode/ai</code>.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-custom-sandbox-modules">Custom sandbox modules</h4>
<p><code>DynamicWorkerExecutor</code> now accepts an optional <code>modules</code> option to inject custom ES modules into the sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17654.md")</div>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-internal-normalization-and-sanitization">Internal normalization and sanitization</h4>
<p><code>DynamicWorkerExecutor</code> now normalizes code and sanitizes tool names internally. You no longer need to call <code>normalizeCode()</code> or <code>sanitizeToolName()</code> before passing code and functions to <code>execute()</code>.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-upgrade">Upgrade</h4>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for the full API reference.</p>


<h2 id="access-durable-object-name-via-ctx-id-name"><a href="/changelog/post/2026-03-15-durable-object-id-name/">Access Durable Object name via `ctx.id.name`</a></h2>
<p><em>2026-03-15</em></p>
<p>When your Worker accesses a Durable Object via <code>idFromName()</code> or <code>getByName()</code>, the same name is now available on <code>ctx.id.name</code> inside the object — no need to pass it through method arguments or persist it in storage. This brings the runtime behavior in line with the <a href="/workers/languages/typescript/">Workers runtime types</a>.</p>
<p>This is especially useful for <a href="/durable-objects/api/alarms/">alarms</a>, where there is no calling client to pass the name as an argument. When an alarm handler runs, <code>ctx.id.name</code> will hold the same name the object was originally accessed with.</p>
<pre tabindex="0"><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class ChatRoom extends DurableObject {&#10;  async getRoomName() {&#10;    // ctx.id.name returns the name passed to getByName() or idFromName()&#10;    return this.ctx.id.name;&#10;  }&#10;}&#10;&#10;// Worker&#10;export default {&#10;  async fetch(request, env) {&#10;    const stub = env.CHAT_ROOM.getByName(&quot;general&quot;);&#10;    const roomName = await stub.getRoomName();&#10;    return new Response(`Welcome to ${roomName}!`);&#10;  },&#10;};&#10;</code></pre>
<p><code>ctx.id.name</code> is <code>undefined</code> in the following cases:</p>
<ul>
<li>For Durable Objects created with <code>newUniqueId()</code>.</li>
<li>When accessed via <code>idFromString()</code>, even if the ID was originally created from a name.</li>
<li>For <a href="/durable-objects/api/id/#name">names longer than 1,024 bytes</a>.</li>
</ul>
<p>This works the same way in local development with <code>wrangler dev</code> as it does in production. Run <code>npm update wrangler</code> to ensure you are on a version with this support.</p>
<p>For more information, refer to the <a href="/durable-objects/api/id/#name">Durable Object ID documentation</a>.</p>


<h2 id="workflow-steps-now-expose-retry-attempt-number-via-step-context"><a href="/changelog/post/2026-03-06-step-context-available/">Workflow steps now expose retry attempt number via step context</a></h2>
<p><em>2026-03-06 12:00:00 UTC</em></p>
<p>Cloudflare Workflows allows you to configure specific retry logic for each step in your workflow execution. Now, you can access <strong>which</strong> retry attempt is currently executing for calls to <code>step.do()</code>:</p>
<pre tabindex="0"><code class="language-ts">await step.do(&quot;my-step&quot;, async (ctx) =&gt; {&#10;	// ctx.attempt is 1 on first try, 2 on first retry, etc.&#10;	console.log(`Attempt ${ctx.attempt}`);&#10;});&#10;</code></pre>
<p>You can use the step context for improved logging &amp; observability, progressive backoff, or conditional logic in your workflow definition.</p>
<p>Note that the current attempt number is 1-indexed. For more information on retry behavior, refer to <a href="/workflows/build/sleeping-and-retrying/">Sleeping and Retrying</a>.</p>


<h2 id="workflows-step-limit-increased-to-25-000-steps-per-instance"><a href="/changelog/post/2026-03-03-step-limits-to-25k/">Workflows step limit increased to 25,000 steps per instance</a></h2>
<p><em>2026-03-03 12:00:00 UTC</em></p>
<p>Each Workflow on Workers Paid now supports 10,000 steps by default, configurable up to 25,000 steps in your <code>wrangler.jsonc</code> file:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;workflows&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;my-workflow&quot;,&#10;			&quot;binding&quot;: &quot;MY_WORKFLOW&quot;,&#10;			&quot;class_name&quot;: &quot;MyWorkflow&quot;,&#10;			&quot;limits&quot;: {&#10;				&quot;steps&quot;: 25000&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Previously, each instance was limited to 1,024 steps. Now, Workflows can support more complex, long-running executions without the additional complexity of recursive or child workflow calls.</p>
<p>Note that the maximum persisted state limit per Workflow instance remains <strong>100 MB</strong> for Workers Free and <strong>1 GB</strong> for Workers Paid. Refer to <a href="/workflows/reference/limits/">Workflows limits</a> for more information.</p>


<h2 id="agents-sdk-v0-7-0-observability-rewrite-keepalive-and-waitformcpconnections"><a href="/changelog/post/2026-03-02-agents-sdk-v0.7.0/">Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections</a></h2>
<p><em>2026-03-02</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> rewrites observability from scratch with <code>diagnostics_channel</code>, adds <code>keepAlive()</code> to prevent Durable Object eviction during long-running work, and introduces <code>waitForMcpConnections</code> so MCP tools are always available when <code>onChatMessage</code> runs.</p>
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
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="agents-sdk-v0-6-0-rpc-transport-for-mcp-optional-oauth-hardened-schema-conversion-and-cloudflare-ai-chat-fixes"><a href="/changelog/post/2026-02-25-agents-sdk-v0.6.0/">Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes</a></h2>
<p><em>2026-02-25</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> lets you define an Agent and an McpAgent in the same Worker and connect them over RPC — no HTTP, no network overhead. It also makes OAuth opt-in for simple MCP connections, hardens the schema converter for production workloads, and ships a batch of <code>@cloudflare/ai-chat</code> reliability fixes.</p>
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
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="better-windows-support-for-python-workers"><a href="/changelog/post/2026-02-13-pywrangler-windows-support/">Better Windows support for Python Workers</a></h2>
<p><em>2026-02-25</em></p>
<p><a href="https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler">Pywrangler</a>, the CLI tool for managing Python Workers and packages,
now supports Windows, allowing you to develop and deploy Python Workers from Windows environments.
Previously, Pywrangler was only available on macOS and Linux.</p>
<p>You can install and use Pywrangler on Windows the same way you would on other platforms.
<a href="/workers/languages/python/packages/">Specify your Worker's Python dependencies</a> in your <code>pyproject.toml</code> file,
then use the following commands to develop and deploy:</p>
<pre tabindex="0"><code class="language-bash">uvx --from workers-py pywrangler dev&#10;uvx --from workers-py pywrangler deploy&#10;</code></pre>
<p>All existing Pywrangler functionality, including package management, local development, and deployment, works on Windows without any additional configuration.</p>
<h4 id="2026-02-13-pywrangler-windows-support-requirements">Requirements</h4>
<p>This feature requires the following minimum versions:</p>
<ul>
<li><code>wrangler</code> &gt;= 4.64.0</li>
<li><code>workers-py</code> &gt;= 1.72.0</li>
<li><code>uv</code> &gt;= 0.29.8</li>
</ul>
<p>To upgrade <code>workers-py</code> (which includes Pywrangler) in your project, run:</p>
<pre tabindex="0"><code class="language-bash">uv tool upgrade workers-py&#10;</code></pre>
<p>To upgrade <code>wrangler</code>, run:</p>
<pre tabindex="0"><code class="language-bash">npm install -g wrangler@latest&#10;</code></pre>
<p>To upgrade <code>uv</code>, run:</p>
<pre tabindex="0"><code class="language-bash">uv self update&#10;</code></pre>
<p>To get started with Python Workers on Windows, refer to the <a href="/workers/languages/python/packages/">Python packages documentation</a> for full details on Pywrangler.</p>


<h2 id="write-structured-queries-to-filter-and-search-your-workers-logs-and-traces"><a href="/changelog/post/2026-02-24-observability-query-language/">Write structured queries to filter and search your Workers logs and traces</a></h2>
<p><em>2026-02-25</em></p>
<p><a href="/workers/observability/">Workers Observability</a> now includes a query language that lets you write structured queries directly in the search bar to filter your logs and traces. The search bar doubles as a free text search box — type any term to search across all metadata and attributes, or write field-level queries for precise filtering.</p>
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


<h2 id="no-config-no-problem-just-wrangler-deploy"><a href="/changelog/post/2026-02-25-wrangler-autoconfig-ga/">No config? No problem. Just `wrangler deploy`</a></h2>
<p><em>2026-02-25</em></p>
<p>You can now deploy any existing project to Cloudflare Workers — even without a Wrangler configuration file — and <code>wrangler deploy</code> will <em>just work</em>.</p>
<p>Starting with Wrangler <strong>4.68.0</strong>, running <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> <a href="/workers/framework-guides/automatic-configuration/">automatically configures your project</a> by detecting your framework, installing required adapters, and deploying it to Cloudflare Workers.</p>
<h4 id="2026-02-25-wrangler-autoconfig-ga-using-wrangler-locally">Using Wrangler locally</h4>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
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


<h2 id="deleteall-now-deletes-durable-object-alarm"><a href="/changelog/post/2026-02-24-deleteall-deletes-alarms/">deleteAll() now deletes Durable Object alarm</a></h2>
<p><em>2026-02-24</em></p>
<p><code>deleteAll()</code> now deletes a Durable Object alarm in addition to stored data for Workers with a compatibility date of <code>2026-02-24</code> or later. This change simplifies clearing a Durable Object's storage with a single API call.</p>
<p>Previously, <code>deleteAll()</code> only deleted user-stored data for an object. Alarm usage stores metadata in an object's storage, which required a separate <code>deleteAlarm()</code> call to fully clean up all storage for an object. The <code>deleteAll()</code> change applies to both KV-backed and SQLite-backed Durable Objects.</p>
<pre tabindex="0"><code class="language-js">// Before: two API calls required to clear all storage&#10;await this.ctx.storage.deleteAlarm();&#10;await this.ctx.storage.deleteAll();&#10;&#10;// Now: a single call clears both data and the alarm&#10;await this.ctx.storage.deleteAll();&#10;</code></pre>
<p>For more information, refer to the <a href="/durable-objects/api/sqlite-storage-api/#deleteall">Storage API documentation</a>.</p>


<h2 id="dropped-event-metrics-typed-pipelines-bindings-and-improved-setup"><a href="/changelog/post/2026-02-24-typed-bindings-setup-improvements-error-metrics/">Dropped event metrics, typed Pipelines bindings, and improved setup</a></h2>
<p><em>2026-02-24</em></p>
<p><a href="/pipelines/">Cloudflare Pipelines</a> ingests streaming data via <a href="/workers/">Workers</a> or HTTP endpoints, transforms it with SQL, and writes it to <a href="/r2/">R2</a> as Apache Iceberg tables. Today we're shipping three improvements to help you understand why streaming events get dropped, catch data quality issues early, and set up Pipelines faster.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-dropped-event-metrics">Dropped event metrics</h4>
<p>When <a href="/pipelines/streams/">stream</a> events don't match the expected schema, Pipelines accepts them during ingestion but drops them when attempting to deliver them to the <a href="/pipelines/sinks/">sink</a>. To help you identify the root cause of these issues, we are introducing a new dashboard and metrics that surface dropped events with detailed error messages.</p>
<p><img src="/assets/upstream/images/pipelines/pipelines-error-log-dash.png" alt="The Errors tab in the Cloudflare dashboard showing deserialization errors grouped by type with individual error details" /></p>
<p>Dropped events can also be queried programmatically via the new <code>pipelinesUserErrorsAdaptiveGroups</code> GraphQL dataset. The dataset breaks down failures by specific error type (<code>missing_field</code>, <code>type_mismatch</code>, <code>parse_failure</code>, or <code>null_value</code>) so you can trace issues back to the source.</p>
<pre tabindex="0"><code class="language-graphql">query GetPipelineUserErrors(&#10;	$accountTag: String!&#10;	$pipelineId: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			pipelinesUserErrorsAdaptiveGroups(&#10;				limit: 100&#10;				filter: {&#10;					pipelineId: $pipelineId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					errorFamily&#10;					errorType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>For the full list of dimensions, error types, and additional query examples, refer to <a href="/pipelines/observability/metrics/#user-error-metrics">User error metrics</a>.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-typed-pipelines-bindings">Typed Pipelines bindings</h4>
<p>Sending data to a Pipeline from a Worker previously used a generic <code>Pipeline&lt;PipelineRecord&gt;</code> type, which meant schema mismatches (wrong field names, incorrect types) were only caught at runtime as dropped events.</p>
<p>Running <code>wrangler types</code> now generates schema-specific TypeScript types for your <a href="/pipelines/streams/writing-to-streams/#send-via-workers">Pipeline bindings</a>. TypeScript catches missing required fields and incorrect field types at compile time, before your code is deployed.</p>
<pre tabindex="0"><code class="language-ts">declare namespace Cloudflare {&#10;	type EcommerceStreamRecord = {&#10;		user_id: string;&#10;		event_type: string;&#10;		product_id?: string;&#10;		amount?: number;&#10;	};&#10;	interface Env {&#10;		STREAM: import(&quot;cloudflare:pipelines&quot;).Pipeline&lt;Cloudflare.EcommerceStreamRecord&gt;;&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/pipelines/streams/writing-to-streams/#typed-pipeline-bindings">Typed Pipeline bindings</a>.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-improved-pipelines-setup">Improved Pipelines setup</h4>
<p>Setting up a new Pipeline previously required multiple manual steps: creating an R2 bucket, enabling R2 Data Catalog, generating an API token, and configuring format, compression, and rolling policies individually.</p>
<p>The <code>wrangler pipelines setup</code> command now offers a <strong>Simple</strong> setup mode that applies recommended defaults and automatically creates the <a href="/r2/buckets/">R2 bucket</a> and enables <a href="/r2-data-catalog/">R2 Data Catalog</a> if they do not already exist. Validation errors during setup prompt you to retry inline rather than restarting the entire process.</p>
<p>For a full walkthrough, refer to the <a href="/pipelines/getting-started/">Getting started guide</a>.</p>


<h2 id="cloudflare-codemode-v0-1-0-a-new-runtime-agnostic-modular-architecture"><a href="/changelog/post/2026-02-20-codemode-sdk-rewrite/">@cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture</a></h2>
<p><em>2026-02-20</em></p>
<p>The <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> package has been rewritten into a modular, runtime-agnostic SDK.</p>
<p><a href="https://blog.cloudflare.com/code-mode/">Code Mode</a> enables LLMs to write and execute code that orchestrates your tools, instead of calling them one at a time. This can (and does) yield significant token savings, reduces context window pressure and improves overall model performance on a task.</p>
<p>The new <code>Executor</code> interface is runtime agnostic and comes with a prebuilt <code>DynamicWorkerExecutor</code> to run generated code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loader</a>.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-breaking-changes">Breaking changes</h4>
<ul>
<li>Removed <code>experimental_codemode()</code> and <code>CodeModeProxy</code> — the package no longer owns an LLM call or model choice</li>
<li>New import path: <code>createCodeTool()</code> is now exported from <code>@cloudflare/codemode/ai</code></li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-new-features">New features</h4>
<ul>
<li><strong><code>createCodeTool()</code></strong> — Returns a standard AI SDK <code>Tool</code> to use in your AI agents.</li>
<li><strong><code>Executor</code> interface</strong> — Minimal <code>execute(code, fns)</code> contract. Implement for any code sandboxing primitive or runtime.</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-dynamicworkerexecutor"><code>DynamicWorkerExecutor</code></h4>
<p>Runs code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a>. It comes with the following features:</p>
<ul>
<li><strong>Network isolation</strong> — <code>fetch()</code> and <code>connect()</code> blocked by default (<code>globalOutbound: null</code>) when using <code>DynamicWorkerExecutor</code></li>
<li><strong>Console capture</strong> — <code>console.log/warn/error</code> captured and returned in <code>ExecuteResult.logs</code></li>
<li><strong>Execution timeout</strong> — Configurable via <code>timeout</code> option (default 30s)</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-usage">Usage</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17638.md")</div>
<h4 id="2026-02-20-codemode-sdk-rewrite-wrangler-configuration">Wrangler configuration</h4>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17639.md")</div>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for full API reference and examples.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-upgrade">Upgrade</h4>
<pre tabindex="0"><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>


<h2 id="agents-sdk-v0-5-0-protocol-message-control-retry-utilities-data-parts-and-cloudflare-ai-chat-v0-1-0"><a href="/changelog/post/2026-02-17-agents-sdk-v0.5.0/">Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0</a></h2>
<p><em>2026-02-17</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds built-in retry utilities, per-connection protocol message control, and a fully rewritten <code>@cloudflare/ai-chat</code> with data parts, tool approval persistence, and zero breaking changes.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-retry-utilities">Retry utilities</h4>
<p>A new <code>this.retry()</code> method lets you retry any async operation with exponential backoff and jitter. You can pass an optional <code>shouldRetry</code> predicate to bail early on non-retryable errors.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17635.md")</div>
<p>Retry options are also available per-task on <code>queue()</code>, <code>schedule()</code>, <code>scheduleEvery()</code>, and <code>addMcpServer()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17636.md")</div>
<p>Retry options are validated eagerly at enqueue/schedule time, and invalid values throw immediately. Internal retries have also been added for workflow operations (<code>terminateWorkflow</code>, <code>pauseWorkflow</code>, and others) with Durable Object-aware error detection.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-per-connection-protocol-message-control">Per-connection protocol message control</h4>
<p>Agents automatically send JSON text frames (identity, state, MCP server lists) to every WebSocket connection. You can now suppress these per-connection for clients that cannot handle them — binary-only devices, MQTT clients, or lightweight embedded systems.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17637.md")</div>
<p>Connections with protocol messages disabled still fully participate in RPC and regular messaging. Use <code>isConnectionProtocolEnabled(connection)</code> to check a connection's status at any time. The flag persists across Durable Object hibernation.</p>
<p>See <a href="/agents/runtime/communication/protocol-messages/">Protocol messages</a> for full documentation.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-cloudflare-ai-chat-v0-1-0"><code>@cloudflare/ai-chat</code> v0.1.0</h4>
<p>The first stable release of <code>@cloudflare/ai-chat</code> ships alongside this release with a major refactor of <code>AIChatAgent</code> internals — new <code>ResumableStream</code> class, WebSocket <code>ChatTransport</code>, and simplified SSE parsing — with zero breaking changes. Existing code using <code>AIChatAgent</code> and <code>useAgentChat</code> works as-is.</p>
<p>Key new features:</p>
<ul>
<li><strong>Data parts</strong> — Attach typed JSON blobs (<code>data-*</code>) to messages alongside text. Supports reconciliation (type+id updates in-place), append, and transient parts (ephemeral via <code>onData</code> callback). See <a href="/agents/communication-channels/chat/chat-agents/#data-parts">Data parts</a>.</li>
<li><strong>Tool approval persistence</strong> — The <code>needsApproval</code> approval UI now survives page refresh and DO hibernation. The streaming message is persisted to SQLite when a tool enters <code>approval-requested</code> state.</li>
<li><strong><code>maxPersistedMessages</code></strong> — Cap SQLite message storage with automatic oldest-message deletion.</li>
<li><strong><code>body</code> option on <code>useAgentChat</code></strong> — Send custom data with every request (static or dynamic).</li>
<li><strong>Incremental persistence</strong> — Hash-based cache to skip redundant SQL writes.</li>
<li><strong>Row size guard</strong> — Automatic two-pass compaction when messages approach the SQLite 2 MB limit.</li>
<li><strong><code>autoContinueAfterToolResult</code> defaults to <code>true</code></strong> — Client-side tool results and tool approvals now automatically trigger a server continuation, matching server-executed tool behavior. Set <code>autoContinueAfterToolResult: false</code> in <code>useAgentChat</code> to restore the previous behavior.</li>
</ul>
<p>Notable bug fixes:</p>
<ul>
<li>Resolved stream resumption race conditions</li>
<li>Resolved an issue where <code>setMessages</code> functional updater sent empty arrays</li>
<li>Resolved an issue where client tool schemas were lost after DO hibernation</li>
<li>Resolved <code>InvalidPromptError</code> after tool approval (<code>approval.id</code> was dropped)</li>
<li>Resolved an issue where message metadata was not propagated on broadcast/resume paths</li>
<li>Resolved an issue where <code>clearAll()</code> did not clear in-memory chunk buffers</li>
<li>Resolved an issue where <code>reasoning-delta</code> silently dropped data when <code>reasoning-start</code> was missed during stream resumption</li>
</ul>
<h4 id="2026-02-17-agents-sdk-v0.5.0-synchronous-queue-and-schedule-getters">Synchronous queue and schedule getters</h4>
<p><code>getQueue()</code>, <code>getQueues()</code>, <code>getSchedule()</code>, <code>dequeue()</code>, <code>dequeueAll()</code>, and <code>dequeueAllByCallback()</code> were unnecessarily <code>async</code> despite only performing synchronous SQL operations. They now return values directly instead of wrapping them in Promises. This is backward compatible — existing code using <code>await</code> on these methods will continue to work.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Fix TypeScript &quot;excessively deep&quot; error</strong> — A depth counter on <code>CanSerialize</code> and <code>IsSerializableParam</code> types bails out to <code>true</code> after 10 levels of recursion, preventing the &quot;Type instantiation is excessively deep&quot; error with deeply nested types like AI SDK <code>CoreMessage[]</code>.</li>
<li><strong>POST SSE keepalive</strong> — The POST SSE handler now sends <code>event: ping</code> every 30 seconds to keep the connection alive, matching the existing GET SSE handler behavior. This prevents POST response streams from being silently dropped by proxies during long-running tool calls.</li>
<li><strong>Widened peer dependency ranges</strong> — Peer dependency ranges across packages have been widened to prevent cascading major bumps during 0.x minor releases. <code>@cloudflare/ai-chat</code> and <code>@cloudflare/codemode</code> are now marked as optional peer dependencies.</li>
</ul>
<h4 id="2026-02-17-agents-sdk-v0.5.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="quick-editor-devtools-replaced-with-log-viewer"><a href="/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/">Quick Editor devtools replaced with log viewer</a></h2>
<p><em>2026-02-16</em></p>
<p>Cloudflare has deprecated the Workers Quick Editor dev tools inspector and replaced it with a lightweight log viewer.</p>
<p>This aligns our logging with <code>wrangler tail</code> and gives us the opportunity to focus our efforts on bringing benefits from the work we have invested in observability, which would not be possible otherwise.</p>
<p>We have made improvements to this logging viewer based on your feedback such that you can log object and array types, and easily clear the list of logs. This does not include class instances. Limitations are documented in the <a href="/workers/playground/">Workers Playground docs</a>.</p>
<p>If you do need to develop your Worker with a remote inspector, you can still do this using Wrangler locally. Cloning a project from your quick editor to your computer for local development can be done with the <code>wrangler init --from-dash</code> command. For more information, refer to <a href="/workers/wrangler/commands/general/#init">Wrangler commands</a>.</p>


<h2 id="new-best-practices-guide-for-workers"><a href="/changelog/post/2026-02-15-workers-best-practices/">New Best Practices guide for Workers</a></h2>
<p><em>2026-02-15</em></p>
<p>A new <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a> guide provides opinionated recommendations for building fast, reliable, observable, and secure Workers. The guide draws on production patterns, Cloudflare internal usage, and best practices observed from developers building on Workers.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Keep your compatibility date current and enable <code>nodejs_compat</code></strong> — Ensure you have access to the latest runtime features and Node.js built-in modules.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17799.md")</div>
- **Generate binding types with `wrangler types`** — Never hand-write your `Env` interface. Let Wrangler generate it from your actual configuration to catch mismatches at compile time.
- **Stream request and response bodies** — Avoid buffering large payloads in memory. Use `TransformStream` and `pipeTo` to stay within the 128 MB memory limit and improve time-to-first-byte.
- **Use bindings, not REST APIs** — Bindings to KV, R2, D1, Queues, and other Cloudflare services are direct, in-process references with no network hop and no authentication overhead.
- **Use Queues and Workflows for background work** — Move long-running or retriable tasks out of the critical request path. Use Queues for simple fan-out and buffering, and Workflows for multi-step durable processes.
- **Enable Workers Logs and Traces** — Configure observability before deploying to production so you have data when you need to debug.
- **Avoid global mutable state** — Workers reuse isolates across requests. Storing request-scoped data in module-level variables causes cross-request data leaks.
- **Always `await` or `waitUntil` your Promises** — Floating promises cause silent bugs and dropped work.
- **Use Web Crypto for secure token generation** — Never use `Math.random()` for security-sensitive operations.
<p>To learn more, refer to <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a>.</p>


<h2 id="introducing-glm-4-7-flash-on-workers-ai-cloudflare-tanstack-ai-and-workers-ai-provider-v3-1-1"><a href="/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/">Introducing GLM-4.7-Flash on Workers AI, @cloudflare/tanstack-ai, and workers-ai-provider v3.1.1</a></h2>
<p><em>2026-02-13</em></p>
<p>We're excited to announce <strong>GLM-4.7-Flash</strong> on Workers AI, a fast and efficient text generation model optimized for multilingual dialogue and instruction-following tasks, along with the brand-new <a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai"><strong>@cloudflare/tanstack-ai</strong></a> package and <a href="https://www.npmjs.com/package/workers-ai-provider"><strong>workers-ai-provider v3.1.1</strong></a>.</p>
<p>You can now run AI agents entirely on Cloudflare. With GLM-4.7-Flash's multi-turn tool calling support, plus full compatibility with TanStack AI and the Vercel AI SDK, you have everything you need to build agentic applications that run completely at the edge.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-glm-4-7-flash-multilingual-text-generation-model">GLM-4.7-Flash — Multilingual Text Generation Model</h4>
<p><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> is a multilingual model with a 131,072 token context window, making it ideal for long-form content generation, complex reasoning tasks, and multilingual applications.</p>
<p><strong>Key Features and Use Cases:</strong></p>
<ul>
<li><strong>Multi-turn Tool Calling for Agents</strong>: Build AI agents that can call functions and tools across multiple conversation turns</li>
<li><strong>Multilingual Support</strong>: Built to handle content generation in multiple languages effectively</li>
<li><strong>Large Context Window</strong>: 131,072 tokens for long-form writing, complex reasoning, and processing long documents</li>
<li><strong>Fast Inference</strong>: Optimized for low-latency responses in chatbots and virtual assistants</li>
<li><strong>Instruction Following</strong>: Excellent at following complex instructions for code generation and structured tasks</li>
</ul>
<p>Use GLM-4.7-Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, <a href="/ai-gateway/">AI Gateway</a>, or via <a href="/workers-ai/configuration/ai-sdk/">workers-ai-provider</a> for the Vercel AI SDK.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-4.7-flash/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-cloudflare-tanstack-ai-v0-1-1-tanstack-ai-adapters-for-workers-ai-and-ai-gateway">@cloudflare/tanstack-ai v0.1.1 — TanStack AI adapters for Workers AI and AI Gateway</h4>
<p>We've released <code>@cloudflare/tanstack-ai</code>, a new package that brings Workers AI and AI Gateway support to <a href="https://tanstack.com/ai">TanStack AI</a>. This provides a framework-agnostic alternative for developers who prefer TanStack's approach to building AI applications.</p>
<p><strong>Workers AI adapters</strong> support four configuration modes — plain binding (<code>env.AI</code>), plain REST, AI Gateway binding (<code>env.AI.gateway(id)</code>), and AI Gateway REST — across all capabilities:</p>
<ul>
<li><strong>Chat</strong> (<code>createWorkersAiChat</code>) — Streaming chat completions with tool calling, structured output, and reasoning text streaming.</li>
<li><strong>Image generation</strong> (<code>createWorkersAiImage</code>) — Text-to-image models.</li>
<li><strong>Transcription</strong> (<code>createWorkersAiTranscription</code>) — Speech-to-text.</li>
<li><strong>Text-to-speech</strong> (<code>createWorkersAiTts</code>) — Audio generation.</li>
<li><strong>Summarization</strong> (<code>createWorkersAiSummarize</code>) — Text summarization.</li>
</ul>
<p><strong>AI Gateway adapters</strong> route requests from third-party providers — OpenAI, Anthropic, Gemini, Grok, and OpenRouter — through Cloudflare AI Gateway for caching, rate limiting, and unified billing.</p>
<p>To get started:</p>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/tanstack-ai @tanstack/ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-workers-ai-provider-v3-1-1-transcription-speech-reranking-and-reliability">workers-ai-provider v3.1.1 — transcription, speech, reranking, and reliability</h4>
<p>The Workers AI provider for the <a href="https://ai-sdk.dev">Vercel AI SDK</a> now supports three new capabilities beyond chat and image generation:</p>
<ul>
<li><strong>Transcription</strong> (<code>provider.transcription(model)</code>) — Speech-to-text with automatic handling of model-specific input formats across binding and REST paths.</li>
<li><strong>Text-to-speech</strong> (<code>provider.speech(model)</code>) — Audio generation with support for voice and speed options.</li>
<li><strong>Reranking</strong> (<code>provider.reranking(model)</code>) — Document reranking for RAG pipelines and search result ordering.</li>
</ul>
<pre tabindex="0"><code class="language-typescript">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import {&#10;	experimental_transcribe,&#10;	experimental_generateSpeech,&#10;	rerank,&#10;} from &quot;ai&quot;;&#10;&#10;const workersai = createWorkersAI({ binding: env.AI });&#10;&#10;const transcript = await experimental_transcribe({&#10;	model: workersai.transcription(&quot;@cf/openai/whisper-large-v3-turbo&quot;),&#10;	audio: audioData,&#10;	mediaType: &quot;audio/wav&quot;,&#10;});&#10;&#10;const speech = await experimental_generateSpeech({&#10;	model: workersai.speech(&quot;@cf/deepgram/aura-1&quot;),&#10;	text: &quot;Hello world&quot;,&#10;	voice: &quot;asteria&quot;,&#10;});&#10;&#10;const ranked = await rerank({&#10;	model: workersai.reranking(&quot;@cf/baai/bge-reranker-base&quot;),&#10;	query: &quot;What is machine learning?&quot;,&#10;	documents: [&quot;ML is a branch of AI.&quot;, &quot;The weather is sunny.&quot;],&#10;});&#10;</code></pre>
<p>This release also includes a comprehensive reliability overhaul (v3.0.5):</p>
<ul>
<li><strong>Fixed streaming</strong> — Responses now stream token-by-token instead of buffering all chunks, using a proper <code>TransformStream</code> pipeline with backpressure.</li>
<li><strong>Fixed tool calling</strong> — Resolved issues with tool call ID sanitization, conversation history preservation, and a heuristic that silently fell back to non-streaming mode when tools were defined.</li>
<li><strong>Premature stream termination detection</strong> — Streams that end unexpectedly now report <code>finishReason: &quot;error&quot;</code> instead of silently reporting <code>&quot;stop&quot;</code>.</li>
<li><strong>AI Search support</strong> — Added <code>createAISearch</code> as the canonical export (renamed from AutoRAG). <code>createAutoRAG</code> still works with a deprecation warning.</li>
</ul>
<p>To upgrade:</p>
<pre tabindex="0"><code class="language-sh">npm install workers-ai-provider@latest ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-resources">Resources</h4>
<ul>
<li><a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai">@cloudflare/tanstack-ai on npm</a></li>
<li><a href="https://www.npmjs.com/package/workers-ai-provider">workers-ai-provider on npm</a></li>
<li><a href="https://github.com/cloudflare/ai">GitHub repository</a></li>
</ul>


<h2 id="workers-are-no-longer-limited-to-1000-subrequests"><a href="/changelog/post/2026-02-11-subrequests-limit/">Workers are no longer limited to 1000 subrequests</a></h2>
<p><em>2026-02-11</em></p>
<p>Workers no longer have a limit of 1000 subrequests per invocation, allowing you to make more <code>fetch()</code> calls or requests
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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/3/">Previous</a><span>Page 4 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/5/">Next</a></nav>
