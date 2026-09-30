---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/18/
  description: '2025-08-05'
  full_title: Developer platform changelog - page 18 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 18 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-08-05"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/18/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 18"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-08-05"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/18/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/18/#page","headline":"Developer platform changelog - page 18 | Cloudflare Docs","description":"2025-08-05","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/18/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/18/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="agents-sdk-adds-mcp-elicitation-support-http-streamable-support-task-queues-email-integration-and-more"><a href="/changelog/post/2025-08-05-agents-MCP-update/">Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more</a></h2>
<p><em>2025-08-05</em></p>
<p>The latest releases of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings major improvements to MCP transport protocols support and agents connectivity. Key updates include:</p>
<h4 id="2025-08-05-agents-MCP-update-mcp-elicitation-support">MCP elicitation support</h4>
<p>MCP servers can now request user input during tool execution, enabling interactive workflows like confirmations, forms, and multi-step processes. This feature uses durable storage to preserve elicitation state even during agent hibernation, ensuring seamless user interactions across agent lifecycle events.</p>
<pre tabindex="0"><code class="language-ts">// Request user confirmation via elicitation&#10;const confirmation = await this.elicitInput({&#10;	message: `Are you sure you want to increment the counter by ${amount}?`,&#10;	requestedSchema: {&#10;		type: &quot;object&quot;,&#10;		properties: {&#10;			confirmed: {&#10;				type: &quot;boolean&quot;,&#10;				title: &quot;Confirm increment&quot;,&#10;				description: &quot;Check to confirm the increment&quot;,&#10;			},&#10;		},&#10;		required: [&quot;confirmed&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Check out our <a href="https://github.com/whoiskatrin/agents/tree/main/examples/mcp-elicitation-demo">demo</a> to see elicitation in action.</p>
<h4 id="2025-08-05-agents-MCP-update-http-streamable-transport-for-mcp">HTTP streamable transport for MCP</h4>
<p>MCP now supports HTTP streamable transport which is recommended over SSE. This transport type offers:</p>
<ul>
<li><strong>Better performance</strong>: More efficient data streaming and reduced overhead</li>
<li><strong>Improved reliability</strong>: Enhanced connection stability and error recover- <strong>Automatic fallback</strong>: If streamable transport is not available, it gracefully falls back to SSE</li>
</ul>
<pre tabindex="0"><code class="language-ts">export default MyMCP.serve(&quot;/mcp&quot;, {&#10;	binding: &quot;MyMCP&quot;,&#10;});&#10;</code></pre>
<p>The SDK automatically selects the best available transport method, gracefully falling back from streamable-http to SSE when needed.</p>
<h4 id="2025-08-05-agents-MCP-update-enhanced-mcp-connectivity">Enhanced MCP connectivity</h4>
<p>Significant improvements to MCP server connections and transport reliability:</p>
<ul>
<li><strong>Auto transport selection</strong>: Automatically determines the best transport method, falling back from streamable-http to SSE as needed</li>
<li><strong>Improved error handling</strong>: Better connection state management and error reporting for MCP servers</li>
<li><strong>Reliable prop updates</strong>: Centralized agent property updates ensure consistency across different contexts</li>
</ul>
<h4 id="2025-08-05-agents-MCP-update-lightweight-queue-for-fast-task-deferral">Lightweight .queue for fast task deferral</h4>
<p>You can use <code>.queue()</code> to enqueue background work — ideal for tasks like processing user messages, sending notifications etc.</p>
<pre tabindex="0"><code class="language-ts">class MyAgent extends Agent {&#10;	doSomethingExpensive(payload) {&#10;		// a long running process that you want to run in the background&#10;	}&#10;&#10;	queueSomething() {&#10;		await this.queue(&quot;doSomethingExpensive&quot;, somePayload); // this will NOT block further execution, and runs in the background&#10;		await this.queue(&quot;doSomethingExpensive&quot;, someOtherPayload); // the callback will NOT run until the previous callback is complete&#10;		// ... call as many times as you want&#10;	}&#10;}&#10;</code></pre>
<p>Want to try it yourself? Just define a method like processMessage in your agent, and you’re ready to scale.</p>
<h4 id="2025-08-05-agents-MCP-update-new-email-adapter">New email adapter</h4>
<p>Want to build an AI agent that can receive and respond to emails automatically? With the new email adapter and onEmail lifecycle method, now you can.</p>
<pre tabindex="0"><code class="language-ts">export class EmailAgent extends Agent {&#10;	async onEmail(email: AgentEmail) {&#10;		const raw = await email.getRaw();&#10;		const parsed = await PostalMime.parse(raw);&#10;&#10;		// create a response based on the email contents&#10;		// and then send a reply&#10;&#10;		await this.replyToEmail(email, {&#10;			fromName: &quot;Email Agent&quot;,&#10;			body: `Thanks for your email! You&#x27;ve sent us &quot;${parsed.subject}&quot;. We&#x27;ll process it shortly.`,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>You route incoming mail like this:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async email(email, env) {&#10;		await routeAgentEmail(email, env, {&#10;			resolver: createAddressBasedEmailResolver(&quot;EmailAgent&quot;),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>You can find a full example <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">here</a>.</p>
<h4 id="2025-08-05-agents-MCP-update-automatic-context-wrapping-for-custom-methods">Automatic context wrapping for custom methods</h4>
<p>Custom methods are now automatically wrapped with the agent's context, so calling <code>getCurrentAgent()</code> should work regardless of where in an agent's lifecycle it's called. Previously this would not work on RPC calls, but now just works out of the box.</p>
<pre tabindex="0"><code class="language-ts">export class MyAgent extends Agent {&#10;	async suggestReply(message) {&#10;		// getCurrentAgent() now correctly works, even when called inside an RPC method&#10;		const { agent } = getCurrentAgent()!;&#10;		return generateText({&#10;			prompt: `Suggest a reply to: &quot;${message}&quot; from &quot;${agent.name}&quot;`,&#10;			tools: [replyWithEmoji],&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>Try it out and tell us what you build!</p>


<h2 id="cloudflare-sandbox-sdk-adds-streaming-code-interpreter-git-support-process-control-and-more"><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more</a></h2>
<p><em>2025-08-05</em></p>
<p>We’ve shipped a major release for the <a href="https://github.com/cloudflare/sandbox-sdk">@cloudflare/sandbox</a> SDK, turning it into a full-featured, container-based execution platform that runs securely on Cloudflare Workers.</p>
<p>This update adds live streaming of output, persistent Python and JavaScript code interpreters with rich output support (charts, tables, HTML, JSON), file system access, Git operations, full background process control, and the ability to expose running services via public URLs.</p>
<p>This makes it ideal for building AI agents, CI runners, cloud REPLs, data analysis pipelines, or full developer tools — all without managing infrastructure.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-code-interpreter-python-js-ts">Code interpreter (Python, JS, TS)</h4>
<p>Create persistent code contexts with support for rich visual + structured outputs.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-createcodecontext-options">createCodeContext(options)</h4>
<p>Creates a new code execution context with persistent state.</p>
<pre tabindex="0"><code class="language-ts">// Create a Python context&#10;const pythonCtx = await sandbox.createCodeContext({ language: &quot;python&quot; });&#10;&#10;// Create a JavaScript context&#10;const jsCtx = await sandbox.createCodeContext({ language: &quot;javascript&quot; });&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-runcode-code-options">runCode(code, options)</h4>
<p>Executes code with optional streaming callbacks.</p>
<pre tabindex="0"><code class="language-ts">// Simple execution&#10;const execution = await sandbox.runCode(&#x27;print(&quot;Hello World&quot;)&#x27;, {&#10;	context: pythonCtx,&#10;});&#10;&#10;// With streaming callbacks&#10;await sandbox.runCode(&#10;	`&#10;for i in range(5):&#10;    print(f&quot;Step {i}&quot;)&#10;    time.sleep(1)&#10;`,&#10;	{&#10;		context: pythonCtx,&#10;		onStdout: (output) =&gt; console.log(&quot;Real-time:&quot;, output.text),&#10;		onResult: (result) =&gt; console.log(&quot;Result:&quot;, result),&#10;	},&#10;);&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-real-time-streaming-output">Real-time streaming output</h4>
<p>Returns a streaming response for real-time processing.</p>
<pre tabindex="0"><code class="language-ts">const stream = await sandbox.runCodeStream(&#10;	&quot;import time; [print(i) for i in range(10)]&quot;,&#10;);&#10;// Process the stream as needed&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-rich-output-handling">Rich output handling</h4>
<p>Interpreter outputs are auto-formatted and returned in multiple formats:</p>
<ul>
<li>text</li>
<li>html (e.g., Pandas tables)</li>
<li>png, svg (e.g., Matplotlib charts)</li>
<li>json (structured data)</li>
<li>chart (parsed visualizations)</li>
</ul>
<pre tabindex="0"><code class="language-ts">const result = await sandbox.runCode(&#10;	`&#10;import seaborn as sns&#10;import matplotlib.pyplot as plt&#10;&#10;data = sns.load_dataset(&quot;flights&quot;)&#10;pivot = data.pivot(&quot;month&quot;, &quot;year&quot;, &quot;passengers&quot;)&#10;sns.heatmap(pivot, annot=True, fmt=&quot;d&quot;)&#10;plt.title(&quot;Flight Passengers&quot;)&#10;plt.show()&#10;&#10;pivot.to_dict()&#10;`,&#10;	{ context: pythonCtx },&#10;);&#10;&#10;if (result.png) {&#10;	console.log(&quot;Chart output:&quot;, result.png);&#10;}&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-preview-urls-from-exposed-ports">Preview URLs from Exposed Ports</h4>
<p>Start background processes and expose them with live URLs.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.startProcess(&quot;python -m http.server 8000&quot;);&#10;const preview = await sandbox.exposePort(8000);&#10;&#10;console.log(&quot;Live preview at:&quot;, preview.url);&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-full-process-lifecycle-control">Full process lifecycle control</h4>
<p>Start, inspect, and terminate long-running background processes.</p>
<pre tabindex="0"><code class="language-ts">const process = await sandbox.startProcess(&quot;node server.js&quot;);&#10;console.log(`Started process ${process.id} with PID ${process.pid}`);&#10;&#10;// Monitor the process&#10;const logStream = await sandbox.streamProcessLogs(process.id);&#10;for await (const log of parseSSEStream&lt;LogEvent&gt;(logStream)) {&#10;	console.log(`Server: ${log.data}`);&#10;}&#10;</code></pre>
<ul>
<li>listProcesses() - List all running processes</li>
<li>getProcess(id) - Get detailed process status</li>
<li>killProcess(id, signal) - Terminate specific processes</li>
<li>killAllProcesses() - Kill all processes</li>
<li>streamProcessLogs(id, options) - Stream logs from running processes</li>
<li>getProcessLogs(id) - Get accumulated process output</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-git-integration">Git integration</h4>
<p>Clone Git repositories directly into the sandbox.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.gitCheckout(&quot;https://github.com/user/repo&quot;, {&#10;	branch: &quot;main&quot;,&#10;	targetDir: &quot;my-project&quot;,&#10;});&#10;</code></pre>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>


<h2 id="openai-open-models-now-available-on-workers-ai"><a href="/changelog/post/2025-08-05-openai-open-models/">OpenAI open models now available on Workers AI</a></h2>
<p><em>2025-08-05</em></p>
<p>We're thrilled to be a Day 0 partner with <a href="http://openai.com/index/introducing-gpt-oss">OpenAI</a> to bring their <a href="https://openai.com/index/gpt-oss-model-card/">latest open models</a> to Workers AI, including support for Responses API, Code Interpreter, and Web Search (coming soon).</p>
<p>Get started with the new models at <code>@cf/openai/gpt-oss-120b</code> and <code>@cf/openai/gpt-oss-20b</code>.
Check out the <a href="https://blog.cloudflare.com/openai-gpt-oss-on-workers-ai">blog</a> for more details about the new models, and the <a href="/workers-ai/models/gpt-oss-120b"><code>gpt-oss-120b</code></a> and <a href="/workers-ai/models/gpt-oss-20b"><code>gpt-oss-20b</code></a> model pages for more information about pricing and context windows.</p>
<h4 id="2025-08-05-openai-open-models-responses-api">Responses API</h4>
If you call the model through:
- Workers Binding, it will accept/return Responses API – `env.AI.run(“@cf/openai/gpt-oss-120b”)`
- REST API on `/run` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/run/@cf/openai/gpt-oss-120b`
- REST API on new `/responses` endpoint, it will accept/return Responses API – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/responses`
- REST API for OpenAI Compatible endpoint, it will return Chat Completions (coming soon) – `https://api.cloudflare.com/client/v4/accounts/<account_id>/ai/v1/chat/completions`
<pre tabindex="0"><code>curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/ai/v1/responses \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_KEY&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;model&quot;: &quot;@cf/openai/gpt-oss-120b&quot;,&#10;    &quot;reasoning&quot;: {&quot;effort&quot;: &quot;medium&quot;},&#10;    &quot;input&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What are the benefits of open-source models?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;&#10;</code></pre>
<h4 id="2025-08-05-openai-open-models-code-interpreter">Code Interpreter</h4>
The model is natively trained to support stateful code execution, and we've implemented support for this feature using our [Sandbox SDK](https://github.com/cloudflare/sandbox-sdk) and [Containers](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Cloudflare's Developer Platform is uniquely positioned to support this feature, so we're very excited to bring our products together to support this new use case.
<h4 id="2025-08-05-openai-open-models-web-search-coming-soon">Web Search (coming soon)</h4>
We are working to implement Web Search for the model, where users can bring their own Exa API Key so the model can browse the Internet.


<h2 id="increased-disk-space-for-workers-builds"><a href="/changelog/post/2025-08-04-builds-increased-disk-size/">Increased disk space for Workers Builds</a></h2>
<p><em>2025-08-04T01:00:00+00:00</em></p>
<p>As part of the ongoing open beta for <a href="/workers/ci-cd/builds/">Workers Builds</a>, we’ve increased the available disk space for builds from <strong>8 GB</strong> to <strong>20 GB</strong> for both Free and Paid plans.</p>
<p>This provides more space for larger projects, dependencies, and build artifacts while improving overall build reliability.</p>
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
<td>Disk Space</td>
<td>20 GB</td>
<td>20 GB</td>
</tr>
</tbody>
</table>
<p>All other <a href="/workers/ci-cd/builds/limits-and-pricing/">build limits</a> — including CPU, memory, build minutes, and timeout remain unchanged.</p>


<h2 id="terraform-v5-8-2-now-available"><a href="/changelog/post/2025-08-01-terraform-v5.8.2-provider/">Terraform v5.8.2 now available</a></h2>
<p><em>2025-08-01</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and reliability. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_custom_pages`
  - `cloudflare_page_rule`
  - `cloudflare_dns_record`
  - `cloudflare_argo_tiered_caching`
- Addressed chronic drift issues in `cloudflare_logpush_job`, `cloudflare_zero_trust_dns_location`, `cloudflare_ruleset` & `cloudflare_api_token`
- `cloudflare_zone_subscription` returns expected values `rate_plan.id` from former versions
- `cloudflare_workers_script` can now successfully be destroyed with bindings & migration for Durable Objects now recorded in tfstate 
- Ability to configure `add_headers` under `cloudflare_zero_trust_gateway_policy` 
- Other bug fixes
<p>For a more detailed look at all of the changes, see the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.2">changelog</a> in GitHub.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-issues-closed">Issues Closed</h4>
- [#5666: cloudflare_ruleset example lists id which is a read-only field](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5666)
- [#5578: cloudflare_logpush_job plan always suggests changes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5578)
- [#5552: 5.4.0: Since provider update, existing cloudflare_list_item would be recreated "created" state](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5552)
- [#5670: cloudflare_zone_subscription: uses wrong ID field in Read/Update](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5670)
- [#5548: cloudflare_api_token resource always shows changes (drift)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5548)
- [#5634: cloudflare_workers_script with bindings fails to be destroyed](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5634)
- [#5616: cloudflare_workers_script Unable to deploy worker assets](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5616)
- [#5331: cloudflare_workers_script 500 internal server error when uploading python](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5331)
- [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5704: cloudflare_workers_script randomly fails to deploy when changing compatibility_date](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5704)
- [#5439: cloudflare_workers_script (v5.2.0) ignoring content and bindings properties](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5439)
- [#5522: cloudflare_workers_script always detects changes after apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5522)
- [#5693: cloudflare_zero_trust_access_identity_provider gives recurring change on OTP pin login](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5693)
- [#5567: cloudflare_r2_custom_domain doesn't roundtrip jurisdiction properly](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5567)
- [#5179: Bad request with when creating cloudflare_api_shield_schema resource](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5179)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-01-terraform-v5.8.2-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="develop-locally-with-containers-and-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-08-01-containers-in-vite-dev/">Develop locally with Containers and the Cloudflare Vite plugin</a></h2>
<p><em>2025-08-01</em></p>
<p>You can now configure and run <a href="/containers">Containers</a> alongside your <a href="/workers">Worker</a> during local development when using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. Previously, you could only develop locally when using <a href="/workers/wrangler/">Wrangler</a> as your local development server.</p>
<h4 id="2025-08-01-containers-in-vite-dev-configuration">Configuration</h4>
<p>You can simply configure your Worker and your Container(s) in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17782.md")</div>
<h4 id="2025-08-01-containers-in-vite-dev-worker-code">Worker Code</h4>
<p>Once your Worker and Containers are configured, you can access the Container instances from your Worker code:</p>
<pre tabindex="0"><code class="language-ts">import { Container, getContainer } from &quot;@cloudflare/containers&quot;;&#10;&#10;export class MyContainer extends Container {&#10;  defaultPort = 4000; // Port the container is listening on&#10;  sleepAfter = &quot;10m&quot;; // Stop the instance if requests not sent for 10 minutes&#10;}&#10;&#10;async fetch(request, env) {&#10;  const { &quot;session-id&quot;: sessionId } = await request.json();&#10;  // Get the container instance for the given session ID&#10;  const containerInstance = getContainer(env.MY_CONTAINER, sessionId)&#10;  // Pass the request to the container instance on its default port&#10;  return containerInstance.fetch(request);&#10;}&#10;</code></pre>
<h4 id="2025-08-01-containers-in-vite-dev-local-development">Local development</h4>
<p>To develop your Worker locally, start a local dev server by running</p>
<pre tabindex="0"><code class="language-sh">vite dev&#10;</code></pre>
<p>in your terminal.</p>
<h4 id="2025-08-01-containers-in-vite-dev-resources">Resources</h4>
<p>Learn more about <a href="https://developers.cloudflare.com/containers/">Cloudflare Containers</a> or the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a> in our developer docs.</p>


<h2 id="deploy-to-cloudflare-buttons-now-support-worker-environment-variables-secrets-and-secrets-store-secrets"><a href="/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/">Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets</a></h2>
<p><em>2025-07-29T01:00:00+00:00</em></p>
<p>Any template which uses <a href="/workers/configuration/environment-variables/">Worker environment variables</a>, <a href="/workers/configuration/secrets/">secrets</a>, or <a href="/secrets-store/">Secrets Store secrets</a> can now be deployed using a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare button</a>.</p>
<p>Define environment variables and secrets store bindings in your Wrangler configuration file as normal:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17781.md")</div>
<p>Add secrets to a <code>.dev.vars.example</code> or <code>.env.example</code> file:</p>
<pre tabindex="0"><code class="language-ini">COOKIE_SIGNING_KEY=my-secret # comment&#10;</code></pre>
<p>And optionally, you can add a description for these bindings in your template's <code>package.json</code> to help users understand how to configure each value:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;private&quot;: true,&#10;	&quot;cloudflare&quot;: {&#10;		&quot;bindings&quot;: {&#10;			&quot;API_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Select your company&#x27;s API key for connecting to the example service.&quot;&#10;			},&#10;			&quot;COOKIE_SIGNING_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Generate a random string using `openssl rand -hex 32`.&quot;&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in <a href="/workers/platform/deploy-buttons/">our documentation</a>.</p>


<h2 id="introducing-pricing-for-the-browser-rendering-api-0-09-per-browser-hour"><a href="/changelog/post/2025-07-28-br-pricing/">Introducing pricing for the Browser Rendering API — $0.09 per browser hour</a></h2>
<p><em>2025-07-28T12:00:00+00:00</em></p>
<p>We’ve launched pricing for <a href="/browser-run/">Browser Rendering</a>, including a free tier and a pay-as-you-go model that scales with your needs. Starting <strong>August 20, 2025</strong>, Cloudflare will begin billing for Browser Rendering.</p>
<p>There are two ways to use Browser Rendering. Depending on the method you use, here’s how billing will work:</p>
<ul>
<li><a href="/browser-run/quick-actions/"><strong>REST API</strong></a>: Charged for <strong>Duration</strong> only ($/browser hour)</li>
<li><a href="/browser-run/#integration-methods"><strong>Browser Sessions</strong></a>: Charged for both <strong>Duration</strong> and <strong>Concurrency</strong> ($/browser hour and # of concurrent browsers)</li>
</ul>
<p>Included usage and pricing by plan</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>Included duration</th>
<th>Included concurrency</th>
<th>Price (beyond included)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Free</strong></td>
<td>10 minutes per day</td>
<td>3 concurrent browsers</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>10 hours per month</td>
<td>10 concurrent browsers (averaged monthly)</td>
<td><strong>1. REST API</strong>: $0.09 per additional browser hour <br /><strong>2. Workers Bindings</strong>: $0.09 per additional browser hour <br /> $2.00 per additional concurrent browser</td>
</tr>
</tbody>
</table>
<p>What you need to know:</p>
<ul>
<li><strong>Workers Free Plan:</strong> 10 minutes of browser usage per day with 3 concurrent browsers at no charge.</li>
<li><strong>Workers Paid Plan:</strong> 10 hours of browser usage per month with 10 concurrent browsers (averaged monthly) at no charge. Additional usage is charged as shown above.</li>
</ul>
<p>You can monitor usage via the <a href="https://dash.cloudflare.com/?to=/:account/workers/browser-run">Cloudflare dashboard</a>. Go to <strong>Compute</strong> &gt; <strong>Browser Run</strong>.</p>
<p><img src="/assets/upstream/images/browser-run/dashboard.png" alt="Browser Rendering dashboard" /></p>
<p>If you've been using Browser Rendering and do not wish to incur charges, ensure your usage stays within your plan's <a href="/browser-run/pricing/">included usage</a>. To estimate costs, take a look at these <a href="/browser-run/pricing/#examples-of-workers-paid-pricing">example pricing scenarios</a>.</p>


<h2 id="browser-rendering-now-supports-local-development"><a href="/changelog/post/2025-07-22-br-local-dev/">Browser Rendering now supports local development</a></h2>
<p><em>2025-07-22T11:00:00+00:00</em></p>
<p>You can now run your Browser Rendering locally using <code>npx wrangler dev</code>, which spins up a browser directly on your machine before deploying to Cloudflare's global network. By running tests locally, you can quickly develop, debug, and test changes without needing to deploy or worry about usage costs.</p>
<p>Get started with this <a href="/browser-run/how-to/deploy-worker/">example guide</a> that shows how to use Cloudflare's <a href="/browser-run/puppeteer/">fork of Puppeteer</a> (you can also use <a href="/browser-run/playwright/">Playwright</a>) to take screenshots of webpages and store the results in <a href="/kv/">Workers KV</a>.</p>


<h2 id="test-out-code-changes-before-shipping-with-per-branch-preview-deployments-for-cloudflare-workers"><a href="/changelog/post/2025-07-23-workers-preview-urls/">Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers</a></h2>
<p><em>2025-07-22T01:00:00+00:00</em></p>
<p>Now, when you connect your Cloudflare Worker to a git repository on GitHub or GitLab, each branch of your repository has its own stable preview URL, that you can use to preview code changes before merging the pull request and deploying to production.</p>
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
<pre tabindex="0"><code class="language-bash">wrangler versions upload --preview-alias staging&#10;</code></pre>
<h4 id="2025-07-23-workers-preview-urls-limitations-while-in-beta">Limitations while in beta</h4>
<ul>
<li>Only available on the <strong>workers.dev</strong> subdomain (custom domains not yet supported)</li>
<li>Requires <strong>Wrangler v4.21.0+</strong></li>
<li>Preview URLs are not generated for Workers that use <a href="/durable-objects/">Durable Objects</a></li>
<li>Not yet supported for <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a></li>
</ul>


<h2 id="audio-mode-for-media-transformations"><a href="/changelog/post/2025-07-22-media-transformations-audio-mode/">Audio mode for Media Transformations</a></h2>
<p><em>2025-07-22</em></p>
<p>We now support <code>audio</code> mode! Use this feature to extract audio from a source video, outputting
an M4A file to use in downstream workflows like <a href="/workers-ai/">AI inference</a>, content moderation, or transcription.</p>
<p>For example,</p>
<pre tabindex="0"><code class="language-text">https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;https://example.com/cdn-cgi/media/mode=audio,time=3s,duration=60s/&lt;input video with diction&gt;&#10;</code></pre>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>


<h2 id="subaddressing-support-in-email-routing"><a href="/changelog/post/2025-07-21-subaddressing/">Subaddressing support in Email Routing</a></h2>
<p><em>2025-07-21</em></p>
<p>Subaddressing, as defined in <a href="https://www.rfc-editor.org/rfc/rfc5233">RFC 5233</a>, also known as plus addressing, is now supported in Email Routing. This enables using the &quot;+&quot; separator to augment your custom addresses with arbitrary detail information.</p>
<p>Now you can send an email to <code>user+detail@example.com</code> and it will be captured by the <code>user@example.com</code> custom address. The <code>+detail</code> part is ignored by Email Routing, but it can be captured next in the processing chain in the logs, an <a href="/email-service/api/route-emails/email-handler/">Email Worker</a> or an <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">Agent application</a>.</p>
<p>Customers can use this feature to dynamically add context to their emails, such as tracking the source of an email or categorizing emails without needing to create multiple custom addresses.</p>
<p><img src="/assets/upstream/images/changelog/email-service/subaddressing.png" alt="Subaddressing" /></p>
<p>Check our <a href="/email-service/configuration/email-routing-addresses/#subaddressing">Developer Docs</a> to learn how to enable subaddressing in Email Routing.</p>


<h2 id="the-cloudflare-vite-plugin-now-supports-vite-7"><a href="/changelog/post/2025-07-17-vite-plugin-vite-7-support/">The Cloudflare Vite plugin now supports Vite 7</a></h2>
<p><em>2025-07-17T01:00:00+00:00</em></p>
<p><a href="https://vite.dev/blog/announcing-vite7">Vite 7</a> is now supported in the Cloudflare Vite plugin.
See the <a href="https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#700-2025-06-24">Vite changelog</a> for a list of changes.</p>
<p>Note that the minimum Node.js versions supported by Vite 7 are 20.19 and 22.12.
We continue to support Vite 6 so you do not need to immediately upgrade.</p>


<h2 id="faster-more-reliable-udp-traffic-for-cloudflare-tunnel"><a href="/changelog/post/2025-07-15-udp-improvements/">Faster, more reliable UDP traffic for Cloudflare Tunnel</a></h2>
<p><em>2025-07-15</em></p>
<p>Your real-time applications running over <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> are now faster and more reliable. We've completely re-architected the way <code>cloudflared</code> proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.</p>
<p>This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.</p>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>Faster UDP performance</strong>: We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.</li>
<li><strong>Greater reliability for mixed traffic</strong>: UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.</li>
</ul>
<p>Learn more about running <a href="/reference-architecture/architectures/sase/#connecting-applications">TCP or UDP applications</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">private networks</a> through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>


<h2 id="terraform-v5-7-0-now-available"><a href="/changelog/post/2025-07-11-terraform-v5.7.0-provider/">Terraform v5.7.0 now available</a></h2>
<p><em>2025-07-14</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release, with 13.5% of resources impacted. We have committed to releasing improvements on a 2 week cadeance to ensure it's stability and relability, including the v5.7 release.</p>
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


<h2 id="faster-indexing-and-new-jobs-view-in-autorag"><a href="/changelog/post/2025-07-08-autorag-jobs-view/">Faster indexing and new Jobs view in AutoRAG</a></h2>
<p><em>2025-07-08</em></p>
<p>You can now expect <strong>3-5× faster indexing</strong> in AutoRAG, and with it, a brand new <strong>Jobs view</strong> to help you monitor indexing progress.</p>
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


<h2 id="heic-support-in-cloudflare-images"><a href="/changelog/post/heic-support/">HEIC support in Cloudflare Images</a></h2>
<p><em>2025-07-08</em></p>
<p>You can use Images to ingest HEIC images and serve them in supported output formats like AVIF, WebP, JPEG, and PNG.</p>
<p>When inputting a HEIC image, dimension and sizing limits may still apply. Refer to our documentation to see limits for <a href="/images/storage/upload-images/methods/">uploading to Images</a> or <a href="/images/optimization/transformations/overview/">transforming a remote image</a>.</p>


<h2 id="workers-now-supports-javascript-debug-terminals-in-vscode-cursor-and-windsurf-ides"><a href="/changelog/post/2025-07-04-javascript-debug-terminals/">Workers now supports JavaScript debug terminals in VSCode, Cursor and Windsurf IDEs</a></h2>
<p><em>2025-07-04</em></p>
<p>Workers now support breakpoint debugging using VSCode's built-in <a href="https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_javascript-debug-terminal">JavaScript Debug Terminals</a>. All you have to do is open a JS debug terminal (<code>Cmd + Shift + P</code> and then type <code>javascript debug</code>) and run <code>wrangler dev</code> (or <code>vite dev</code>) from within the debug terminal. VSCode will automatically connect to your running Worker (even if you're running multiple Workers at once!) and start a debugging session.</p>
<p>In 2023 we announced <a href="https://blog.cloudflare.com/debugging-cloudflare-workers/">breakpoint debugging support</a> for Workers, which meant that you could easily debug your Worker code in Wrangler's built-in devtools (accessible via the <code>[d]</code> hotkey) as well as multiple other devtools clients, <a href="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/">including VSCode</a>. For most developers, breakpoint debugging via VSCode is the most natural flow, but until now it's required <a href="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/#setup-vs-code-to-use-breakpoints">manually configuring a <code>launch.json</code> file</a>, running <code>wrangler dev</code>, and connecting via VSCode's built-in debugger. Now it's much more seamless!</p>


<h2 id="hyperdrive-now-supports-configuring-the-amount-of-database-connections"><a href="/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/">Hyperdrive now supports configuring the amount of database connections</a></h2>
<p><em>2025-07-03</em></p>
<p>You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.</p>
<p>All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the <a href="/hyperdrive/platform/limits/">Hyperdrive limits of your Workers plan</a>.</p>
<p>This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.</p>
<p>Refer to the <a href="/hyperdrive/concepts/connection-pooling/">Hyperdrive configuration documentation</a> for more information.</p>


<h2 id="enhanced-support-for-static-assets-with-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/">Enhanced support for static assets with the Cloudflare Vite plugin</a></h2>
<p><em>2025-07-01</em></p>
<p>You can now use any of Vite's <a href="https://vite.dev/guide/assets">static asset handling</a> features in your Worker as well as in your frontend.
These include importing assets as URLs, importing as strings and importing from the <code>public</code> directory as well as inlining assets.</p>
<p>Additionally, assets imported as URLs in your Worker are now automatically moved to the client build output.</p>
<p>Here is an example that fetches an imported asset using the <a href="/workers/static-assets/binding/#binding">assets binding</a> and modifies the response.</p>
<pre tabindex="0"><code class="language-ts">// Import the asset URL&#10;// This returns the resolved path in development and production&#10;import myImage from &quot;./my-image.png&quot;;&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		// Fetch the asset using the binding&#10;		const response = await env.ASSETS.fetch(new URL(myImage, request.url));&#10;		// Create a new `Response` object that can be modified&#10;		const modifiedResponse = new Response(response.body, response);&#10;		// Add an additional header&#10;		modifiedResponse.headers.append(&quot;my-header&quot;, &quot;imported-asset&quot;);&#10;&#10;		// Return the modified response&#10;		return modifiedResponse;&#10;	},&#10;};&#10;</code></pre>
<p>Refer to <a href="/workers/vite-plugin/reference/static-assets/">Static Assets</a> in the Cloudflare Vite plugin docs for more info.</p>


<h2 id="mail-authentication-requirements-for-email-routing"><a href="/changelog/post/2025-06-30-mail-authentication/">Mail authentication requirements for Email Routing</a></h2>
<p><em>2025-06-30</em></p>
<p>The Email Routing platform supports <a href="https://datatracker.ietf.org/doc/html/rfc7208">SPF</a> records and <a href="https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail">DKIM (DomainKeys Identified Mail)</a> signatures and
honors these protocols when the sending domain has them configured. However, if the sending domain doesn't implement them,
we still forward the emails to upstream mailbox providers.</p>
<p>Starting on July 3, 2025, we will require all emails to be authenticated using at least one of the protocols, SPF or DKIM, to
forward them. We also strongly recommend that all senders implement the DMARC protocol.</p>
<p>If you are using a Worker with an Email trigger to receive email messages and forward them upstream, you will need to handle the case where
the forward action may fail due to missing authentication on the incoming email.</p>
<p>SPAM has been a long-standing issue with email. By enforcing mail authentication, we will increase the efficiency of identifying abusive senders and blocking
bad emails.
If you're an email server delivering emails to large mailbox providers, it's likely you already use these protocols; otherwise, please ensure
you have them properly configured.</p>


<h2 id="remote-bindings-beta-now-works-with-next-js-connect-to-remote-resources-d1-kv-r2-etc-during-local-development"><a href="/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/">Remote bindings (beta) now works with Next.js — connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<p><em>2025-06-30</em></p>
<p>We <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">recently announced</a> our public beta for <a href="/workers/local-development/#remote-bindings">remote bindings</a>, which allow you to connect to deployed resources running on your Cloudflare account (like <a href="/r2">R2 buckets</a> or <a href="/d1">D1 databases</a>) while running a local development session.</p>
<p>Now, you can use remote bindings with your Next.js applications through the <a href="https://opennext.js.org/cloudflare/bindings#remote-bindings"><code>@opennextjs/cloudflare</code> adaptor</a> by enabling the experimental feature in your <code>next.config.ts</code>:</p>
<pre tabindex="0"><code class="language-diff">&#45; initOpenNextCloudflareForDev();&#10;&#43; initOpenNextCloudflareForDev({&#10;&#43;  experimental: { remoteBindings: true }&#10;&#43; });&#10;</code></pre>
<p>Then, all you have to do is specify which bindings you want connected to the deployed resource on your Cloudflare account via the <code>experimental_remote</code> flag in your binding definition:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17780.md")</div>
<p>You can then run <code>next dev</code> to start a local development session (or start a preview with <code>opennextjs-cloudflare preview</code>), and all requests to <code>env.MY_BUCKET</code> will be proxied to the remote <code>testing-bucket</code> — rather than the <a href="/workers/local-development/#bindings-during-local-development">default local binding simulations</a>.</p>
<h4 id="2025-06-25-getPlatformProxy-support-remote-bindings-remote-bindings-isr">Remote bindings &amp; ISR</h4>
<p>Remote bindings are also used during the build process, which comes with significant benefits for pages using <a href="https://opennext.js.org/aws/inner_workings/components/server/node#isrssg">Incremental Static Regeneration (ISR)</a>. During the build step for an ISR page, your server executes the page's code just as it would for normal user requests. If a page needs data to display (like fetching user info from <a href="/kv">KV</a>), those requests are actually made. The server then uses this fetched data to render the final HTML.</p>
<p>Data fetching is a critical part of this process, as the finished HTML is only as good as the data it was built with. If the build process can't fetch real data, you end up with a pre-rendered page that's empty or incomplete.</p>
<p><strong>With remote bindings support in OpenNext,</strong> your pre-rendered pages are built with real data from the start. The build process uses any configured remote bindings, and any data fetching occurs against the deployed resources on your Cloudflare account.</p>
<p><strong>Want to learn more?</strong> Get started with <a href="https://opennext.js.org/cloudflare/bindings#remote-bindings">remote bindings and OpenNext</a>.</p>
<p><strong>Have feedback?</strong> Join the discussion in our <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">beta announcement</a> to share feedback or report any issues.</p>


<h2 id="run-and-connect-workers-in-separate-dev-commands-with-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/">Run and connect Workers in separate dev commands with the Cloudflare Vite plugin</a></h2>
<p><em>2025-06-26</em></p>
<p>Workers can now talk to each other across separate dev commands using service bindings and tail consumers, whether started with <code>vite dev</code> or <code>wrangler dev</code>.</p>
<p>Simply start each Worker in its own terminal:</p>
<pre tabindex="0"><code class="language-sh">&#35; Terminal 1&#10;vite dev&#10;&#10;&#35; Terminal 2&#10;wrangler dev&#10;</code></pre>
<p>This is useful when different teams maintain different Workers, or when each Worker has its own build setup or tooling.</p>
<p>Check out the <a href="/workers/local-development/multi-workers">Developing with multiple Workers</a> guide to learn more about the different approaches and when to use each one.</p>


<h2 id="run-ai-generated-code-on-demand-with-code-sandboxes-new"><a href="/changelog/post/2025-06-24-announcing-sandboxes/">Run AI-generated code on-demand with Code Sandboxes (new)</a></h2>
<p><em>2025-06-25</em></p>
<p>AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing <a href="https://www.npmjs.com/package/@cloudflare/sandbox">Sandboxes</a>, which let your Worker run actual processes in a secure, container-based environment.</p>
<pre tabindex="0"><code class="language-ts">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;		return sandbox.exec(&quot;ls&quot;, [&quot;-la&quot;]);&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-06-24-announcing-sandboxes-methods">Methods</h4>
<ul>
<li><code>exec(command: string, args: string[], options?: { stream?: boolean })</code>:Execute a command in the sandbox.</li>
<li><code>gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })</code>: Checkout a git repository in the sandbox.</li>
<li><code>mkdir(path: string, options: { recursive?: boolean; stream?: boolean })</code>: Create a directory in the sandbox.</li>
<li><code>writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })</code>: Write content to a file in the sandbox.</li>
<li><code>readFile(path: string, options: { encoding?: string; stream?: boolean })</code>: Read content from a file in the sandbox.</li>
<li><code>deleteFile(path: string, options?: { stream?: boolean })</code>: Delete a file from the sandbox.</li>
<li><code>renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })</code>: Rename a file in the sandbox.</li>
<li><code>moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })</code>: Move a file from one location to another in the sandbox.</li>
<li><code>ping()</code>: Ping the sandbox.</li>
</ul>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>
<p>You can try it today from your Worker, with just a few lines of code. Let us know what you build.</p>


<h2 id="cloudflare-actors-library-sdk-for-durable-objects-in-beta"><a href="/changelog/post/2025-06-25-actors-package-alpha/">@cloudflare/actors library - SDK for Durable Objects in beta</a></h2>
<p><em>2025-06-25</em></p>
<p>The new <a href="https://www.npmjs.com/package/@cloudflare/actors">@cloudflare/actors</a> library is now in beta!</p>
<p>The <code>@cloudflare/actors</code> library is a new SDK for Durable Objects and provides a powerful set of abstractions for building real-time, interactive, and multiplayer applications on top of Durable Objects. With beta usage and feedback, <code>@cloudflare/actors</code> will become the recommended way to build on Durable Objects and draws upon Cloudflare's experience building products/features on Durable Objects.</p>
<p>The name &quot;actors&quot; originates from the <a href="/durable-objects/concepts/what-are-durable-objects/#actor-programming-model">actor programming model</a>, which closely ties to how Durable Objects are modelled.</p>
<p>The <code>@cloudflare/actors</code> library includes:</p>
<ul>
<li>Storage helpers for querying embeddeded, per-object SQLite storage</li>
<li>Storage helpers for managing SQL schema migrations</li>
<li>Alarm helpers for scheduling multiple alarms provided a date, delay in seconds, or cron expression</li>
<li><code>Actor</code> class for using Durable Objects with a defined pattern</li>
<li>Durable Objects <a href="https://developers.cloudflare.com/durable-objects/api/base/">Workers API</a> is always available for your application as needed</li>
</ul>
<p>Storage and alarm helper methods can be combined with <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#storage--alarms-with-durableobject-class">any Javascript class</a> that defines your Durable Object, i.e, ones that extend <code>DurableObject</code> including the <code>Actor</code> class.</p>
<pre tabindex="0"><code class="language-js">import { Storage } from &quot;@cloudflare/actors/storage&quot;;&#10;&#10;export class ChatRoom extends DurableObject&lt;Env&gt; {&#10;    storage: Storage;&#10;&#10;    constructor(ctx: DurableObjectState, env: Env) {&#10;        super(ctx, env)&#10;        this.storage = new Storage(ctx.storage);&#10;        this.storage.migrations = [{&#10;            idMonotonicInc: 1,&#10;            description: &quot;Create users table&quot;,&#10;            sql: &quot;CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)&quot;&#10;        }]&#10;    }&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        // Run migrations before executing SQL query&#10;        await this.storage.runMigrations();&#10;&#10;        // Query with SQL template&#10;        let userId = new URL(request.url).searchParams.get(&quot;userId&quot;);&#10;        const query = this.storage.sql`SELECT * FROM users WHERE id = ${userId};`&#10;        return new Response(`${JSON.stringify(query)}`);&#10;    }&#10;}&#10;</code></pre>
<p><code>@cloudflare/actors</code> library introduces the <code>Actor</code> class pattern. <code>Actor</code> lets you access Durable Objects without writing the Worker that communicates with your Durable Object (the Worker is created for you). By default, requests are routed to a Durable Object named &quot;default&quot;.</p>
<pre tabindex="0"><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(&#x27;Hello, World!&#x27;)&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>You can <a href="/durable-objects/get-started/#3-instantiate-and-communicate-with-a-durable-object">route</a> to different Durable Objects by name within your <code>Actor</code> class using <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#actor-with-custom-name"><code>nameFromRequest</code></a>.</p>
<pre tabindex="0"><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    static nameFromRequest(request: Request): string {&#10;        let url = new URL(request.url);&#10;        return url.searchParams.get(&quot;userId&quot;) ?? &quot;foo&quot;;&#10;    }&#10;&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(`Actor identifier (Durable Object name): ${this.identifier}`);&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>For more examples, check out the library <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#getting-started">README</a>. <code>@cloudflare/actors</code> library is a place for more helpers and built-in patterns, like retry handling and Websocket-based applications, to reduce development overhead for common Durable Objects functionality. Please share feedback and what more you would like to see on our <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord channel</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/17/">Previous</a><span>Page 18 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/19/">Next</a></nav>
