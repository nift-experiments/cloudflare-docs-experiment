<h1 id="changelog">Changelog</h1>

<h2 id="panic-recovery-for-rust-workers"><a href="/changelog/post/2025-09-19-workers-rs-panic-recovery/">Panic Recovery for Rust Workers</a></h2>
<p><em>2025-09-19</em></p>
<p>In <a href="https://github.com/cloudflare/workers-rs">workers-rs</a>, Rust panics were previously non-recoverable. A panic would put the Worker into an invalid state, and further function calls could result in memory overflows or exceptions.</p>
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


<h2 id="increased-vcpu-for-workers-builds-on-paid-plans"><a href="/changelog/post/2025-09-07-builds-increased-cpu-paid/">Increased vCPU for Workers Builds on paid plans</a></h2>
<p><em>2025-09-18</em></p>
<p>We recently <a href="/changelog/2025-08-04-builds-increased-disk-size/">increased the available disk space</a> from 8 GB to 20 GB for <strong>all</strong> plans. Building on that improvement, we’re now doubling the CPU power available for paid plans — from 2 vCPU to <strong>4 vCPU</strong>.</p>
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


<h2 id="preview-urls-now-default-to-opt-in"><a href="/changelog/post/2025-09-17-update-preview-url-setting/">Preview URLs now default to opt-in</a></h2>
<p><em>2025-09-17</em></p>
<p>To prevent the accidental exposure of applications, we've updated how <a href="/workers/versions-and-deployments/preview-urls/">Worker preview URLs</a> (<code>&lt;PREVIEW&gt;-&lt;WORKER_NAME&gt;.&lt;SUBDOMAIN&gt;.workers.dev</code>) are handled. We made this change to ensure preview URLs are only active when intentionally configured, improving the default security posture of your Workers.</p>
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


<h2 id="remote-bindings-ga-connect-to-remote-resources-d1-kv-r2-etc-during-local-development"><a href="/changelog/post/2025-09-16-remote-bindings-ga/">Remote bindings GA - Connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<p><em>2025-09-16</em></p>
<p>Three months ago <a href="/changelog/2025-06-18-remote-bindings-beta/">we announced the public beta</a> of <a href="/workers/local-development/#remote-bindings">remote bindings</a> for local development. Now, we're excited to say that it's available for everyone in Wrangler, Vite, and Vitest without using an experimental flag!</p>
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


<h2 id="d1-automatically-retries-read-only-queries"><a href="/changelog/post/2025-09-11-d1-automatic-read-retries/">D1 automatically retries read-only queries</a></h2>
<p><em>2025-09-11</em></p>
<p>D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors. You can access the number of execution attempts in the returned <a href="/d1/worker-api/return-object/#d1result">response metadata</a> property <code>total_attempts</code>.</p>
<p>At the moment, only read-only queries are retried, that is, queries containing only the following SQLite keywords: <code>SELECT</code>, <code>EXPLAIN</code>, <code>WITH</code>. Queries containing any <a href="https://sqlite.org/lang_keywords.html">SQLite keyword</a> that leads to database writes are not retried.</p>
<p>The retry success ratio among read-only retryable errors varies from 5% all the way up to 95%, depending on the underlying error and its duration (like network errors or other internal errors).</p>
<p>The retry success ratio among all retryable errors is lower, indicating that there are write-queries that could be retried. Therefore, we recommend D1 users to continue applying <a href="/d1/best-practices/retry-queries/">retries in their own code</a> for queries that are not read-only but are idempotent according to the business logic of the application.</p>
<p><img src="/assets/upstream/images/changelog/d1/d1-auto-retry-success-ratio.png" alt="D1 automatically query retries success ratio" /></p>
<p>D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing changes slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.</p>
<p>The read-only query detection heuristics are simple for now, and there is room for improvement to capture more cases of queries that can be retried, so this is just the beginning.</p>


<h2 id="worker-version-rollback-limit-increased-from-10-to-100"><a href="/changelog/post/2025-09-11-increased-version-rollback-limit/">Worker version rollback limit increased from 10 to 100</a></h2>
<p><em>2025-09-11</em></p>
<p>The number of recent versions available for a Worker rollback has been increased from 10 to 100.</p>
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


<h2 id="agents-sdk-v0-1-0-and-workers-ai-provider-v2-0-0-with-ai-sdk-v5-support"><a href="/changelog/post/2025-09-03-agents-sdk-beta-v5/">Agents SDK v0.1.0 and workers-ai-provider v2.0.0 with AI SDK v5 support</a></h2>
<p><em>2025-09-10</em></p>
<p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v5</a> and introducing automatic message migration that handles all legacy formats transparently.</p>
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


<h2 id="built-with-cloudflare-button"><a href="/changelog/post/2025-09-10-built-with-cloudflare-button/">Built with Cloudflare button</a></h2>
<p><em>2025-09-10</em></p>
<p>We've updated our &quot;Built with Cloudflare&quot; button to make it easier to share that you're building on Cloudflare with the world. Embed it in your project's README, blog post, or wherever you want to let people know.</p>
<p><img src="https://workers.cloudflare.com/built-with-cloudflare.svg" alt="Built with Cloudflare" /></p>
<p>Check out the <a href="/workers/platform/built-with-cloudflare">documentation</a> for usage information.</p>


<h2 id="deploy-static-sites-to-workers-without-a-configuration-file"><a href="/changelog/post/2025-09-09-interactive-wrangler-assets/">Deploy static sites to Workers without a configuration file</a></h2>
<p><em>2025-09-09</em></p>
<p>Deploying static site to Workers is now easier. When you run <code>wrangler deploy [directory]</code> or <code>wrangler deploy --assets [directory]</code> without an existing <a href="/workers/wrangler/configuration/">configuration file</a>, <a href="/workers/wrangler/">Wrangler CLI</a> now guides you through the deployment process with interactive prompts.</p>
<h4 id="2025-09-09-interactive-wrangler-assets-before-and-after">Before and after</h4>
<p><strong>Before:</strong> Required remembering multiple flags and parameters</p>
<pre><code class="language-bash">wrangler deploy --assets ./dist --compatibility-date 2025-09-09 --name my-project&#10;</code></pre>
<p><strong>After:</strong> Simple directory deployment with guided setup</p>
<pre><code class="language-bash">wrangler deploy dist&#10;&#35; Interactive prompts handle the rest as shown in the example flow below&#10;</code></pre>
<h4 id="2025-09-09-interactive-wrangler-assets-what-s-new">What's new</h4>
<p><strong>Interactive prompts for missing configuration:</strong></p>
<ul>
<li>Wrangler detects when you're trying to deploy a directory of static assets</li>
<li>Prompts you to confirm the deployment type</li>
<li>Asks for a project name (with smart defaults)</li>
<li>Automatically sets the compatibility date to today</li>
</ul>
<p><strong>Automatic configuration generation:</strong></p>
<ul>
<li>Creates a <code>wrangler.jsonc</code> file with your deployment settings</li>
<li>Stores your choices for future deployments</li>
<li>Eliminates the need to remember complex command-line flags</li>
</ul>
<h4 id="2025-09-09-interactive-wrangler-assets-example-workflow">Example workflow</h4>
<pre><code class="language-bash">&#35; Deploy your built static site&#10;wrangler deploy dist&#10;&#10;&#35; Wrangler will prompt:&#10;✔ It looks like you are trying to deploy a directory of static assets only. Is this correct? … yes&#10;✔ What do you want to name your project? … my-astro-site&#10;&#10;&#35; Automatically generates a wrangler.jsonc file and adds it to your project:&#10;{&#10;  &quot;name&quot;: &quot;my-astro-site&quot;,&#10;  &quot;compatibility_date&quot;: &quot;2025-09-09&quot;,&#10;  &quot;assets&quot;: {&#10;    &quot;directory&quot;: &quot;dist&quot;&#10;  }&#10;}&#10;&#10;&#35; Next time you run wrangler deploy, this will use the configuration in your newly generated wrangler.jsonc file&#10;wrangler deploy&#10;</code></pre>
<h4 id="2025-09-09-interactive-wrangler-assets-requirements">Requirements</h4>
<ul>
<li>You must use Wrangler version 4.24.4 or later in order to use this feature</li>
</ul>


<h2 id="increased-static-asset-limits-for-workers"><a href="/changelog/post/2025-09-02-increased-static-asset-limits/">Increased static asset limits for Workers</a></h2>
<p><em>2025-09-04</em></p>
<p>You can now upload up to <strong>100,000 static assets</strong> per Worker version</p>
<ul>
<li>Paid and Workers for Platforms users can now upload up to <strong>100,000 static assets</strong> per Worker version, a 5x increase from the previous limit of 20,000.</li>
<li>Customers on the free plan still have the same limit as before — 20,000 static assets per version of your Worker</li>
<li>The individual file size limit of 25 MiB remains unchanged for all customers.</li>
</ul>
<p>This increase allows you to build larger applications with more static assets without hitting limits.</p>
<h4 id="2025-09-02-increased-static-asset-limits-wrangler">Wrangler</h4>
<p>To take advantage of the increased limits, you must use <strong>Wrangler version 4.34.0 or higher</strong>.
Earlier versions of Wrangler will continue to enforce the previous 20,000 file limit.</p>
<h4 id="2025-09-02-increased-static-asset-limits-learn-more">Learn more</h4>
<p>For more information about Workers static assets, see the <a href="/workers/static-assets/">Static Assets documentation</a> and <a href="/workers/platform/limits/#static-assets">Platform Limits</a>.</p>


<h2 id="a-new-simpler-rest-api-for-cloudflare-workers-beta"><a href="/changelog/post/2025-09-03-new-workers-api/">A new, simpler REST API for Cloudflare Workers (Beta)</a></h2>
<p><em>2025-09-04</em></p>
<p>You can now manage <a href="/api/resources/workers/subresources/beta/subresources/workers/methods/create/"><strong>Workers</strong></a>, <a href="/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)"><strong>Versions</strong></a>, and <a href="/api/resources/workers/subresources/scripts/subresources/content/methods/update/"><strong>Deployments</strong></a> as separate resources with a new, resource-oriented API (Beta).</p>
<p>This new API is supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a> and the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare Typescript SDK</a>, allowing platform teams to manage a Worker's infrastructure in Terraform, while development teams handle code deployments from a separate repository or workflow. We also designed this API with AI agents in mind, as a clear, predictable structure is essential for them to reliably build, test, and deploy applications.</p>
<h4 id="2025-09-03-new-workers-api-try-it-out">Try it out</h4>
- [**New beta API endpoints**](/api/resources/workers/subresources/beta/)
- [**Cloudflare TypeScript SDK v5.0.0**](https://github.com/cloudflare/cloudflare-typescript)
- [**Cloudflare Go SDK v6.0.0**](https://github.com/cloudflare/cloudflare-go)
- [**Terraform provider v5.9.0**](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs): [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) , [`cloudflare_worker_version`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version), and [`cloudflare_workers_deployments`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_deployment) resources.
- See full examples in our [Infrastructure as Code (IaC) guide](/workers/platform/infrastructure-as-code)
<h4 id="2025-09-03-new-workers-api-before-eight-endpoints-with-mixed-responsibilities">Before: Eight+ endpoints with mixed responsibilities</h4>
<img src="/assets/upstream/images/workers/platform/api-before.png" alt="Before">
<p>The existing API was originally designed for simple, one-shot script uploads:</p>
<pre><code class="language-sh">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/scripts/$SCRIPT_NAME&quot; \&#10;    &#45;H &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;    &#45;H &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;    &#45;H &quot;Content-Type: multipart/form-data&quot; \&#10;    &#45;F &#x27;metadata={&#10;      &quot;main_module&quot;: &quot;worker.js&quot;,&#10;      &quot;compatibility_date&quot;: &quot;$today$&quot;&#10;    }&#x27; \&#10;    &#45;F &quot;worker.js=@worker.js;type=application/javascript+module&quot;&#10;</code></pre>
<p>This API worked for creating a basic Worker, uploading all of its code, and deploying it immediately — but came with challenges:</p>
<ul>
<li>
<p><strong>A Worker couldn't exist without code</strong>: To create a Worker, you had to upload its code in the same API request. This meant platform teams couldn't provision Workers with the proper settings, and then hand them off to development teams to deploy the actual code.</p>
</li>
<li>
<p><strong>Several endpoints implicitly created deployments</strong>: Simple updates like adding a secret or changing a script's content would implicitly create a new version and immediately deploy it.</p>
</li>
<li>
<p><strong>Updating a setting was confusing</strong>: Configuration was scattered across eight endpoints with overlapping responsibilities.  This ambiguity made it difficult for human developers (and even more so for AI agents) to reliably update a Worker via API.</p>
</li>
<li>
<p><strong>Scripts used names as primary identifiers</strong>: This meant simple renames could turn into a risky migration, requiring you to create a brand new Worker and update every reference. If you were using Terraform, this could inadvertently destroy your Worker altogether.</p>
</li>
</ul>
<h4 id="2025-09-03-new-workers-api-after-three-resources-with-clear-boundaries">After: Three resources with clear boundaries</h4>
<img src="/assets/upstream/images/workers/platform/api-after.png" alt="After">
The new API introduces cleaner resource management with three core resources: [**Worker**](/api/resources/workers/subresources/beta/subresources/workers/methods/create/), [**Versions**](/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)), and [**Deployment**](/api/resources/workers/subresources/scripts/subresources/content/methods/update/).
<p>All endpoints now use simple JSON payloads, with script content embedded as <code>base64</code>-encoded strings -- a more consistent and reliable approach than the previous <code>multipart/form-data</code> format.</p>
<ul>
<li>
<p><strong>Worker</strong>: The parent resource representing your application. It has a stable UUID and holds persistent settings like <code>name</code>, <code>tags</code>, and <code>logpush</code>. You can now create a Worker to establish its identity and settings <strong>before</strong> any code is uploaded.</p>
</li>
<li>
<p><strong>Version</strong>: An immutable snapshot of your code and its specific configuration, like bindings and <code>compatibility_date</code>. Creating a new version is a safe action that doesn't affect live traffic.</p>
</li>
<li>
<p><strong>Deployment</strong>: An explicit action that directs traffic to a specific version.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17786.md")</aside>
<h4 id="2025-09-03-new-workers-api-why-this-matters">Why this matters</h4>
<h4 id="2025-09-03-new-workers-api-you-can-now-create-workers-before-uploading-code">You can now create Workers before uploading code</h4>
<p>Workers are now standalone resources that can be created and configured without any code. Platform teams can provision Workers with the right settings, then hand them off to development teams for implementation.</p>
<h4 id="2025-09-03-new-workers-api-example-typescript-sdk">Example: Typescript SDK</h4>
<pre><code class="language-ts">// Step 1: Platform team creates the Worker resource (no code needed)&#10;const worker = await client.workers.beta.workers.create({&#10;  name: &quot;payment-service&quot;,&#10;  account_id: &quot;...&quot;,&#10;  observability: {&#10;    enabled: true,&#10;  },&#10;});&#10;<p>// Step 2: Development team adds code and creates a version later&#10;const version = await client.workers.beta.workers.versions.create(worker.id, {&#10;account_id: &quot;...&quot;,&#10;main_module: &quot;worker.js&quot;,&#10;compatibility_date: &quot;$today&quot;,&#10;bindings: [ /<em>...</em>/ ],&#10;modules: [&#10;{&#10;name: &quot;worker.js&quot;,&#10;content_type: &quot;application/javascript+module&quot;,&#10;content_base64: Buffer.from(scriptContent).toString(&quot;base64&quot;),&#10;},&#10;],&#10;});</p>&#10;<p>// Step 3: Deploy explicitly when ready&#10;const deployment = await client.workers.scripts.deployments.create(worker.name, {&#10;account_id: &quot;...&quot;,&#10;strategy: &quot;percentage&quot;,&#10;versions: [&#10;{&#10;percentage: 100,&#10;version_id: version.id,&#10;},&#10;],&#10;});&#10;</code></pre></p>
<h4 id="2025-09-03-new-workers-api-example-terraform">Example: Terraform</h4>
If you use Terraform, you can now declare the Worker in your Terraform configuration and manage configuration outside of Terraform in your Worker's [`wrangler.jsonc` file](/workers/wrangler/configuration/) and deploy code changes using [Wrangler](/workers/wrangler/).
<pre><code class="language-tf">resource &quot;cloudflare_worker&quot; &quot;my_worker&quot; {&#10;  account_id = &quot;...&quot;&#10;  name = &quot;my-important-service&quot;&#10;}&#10;&#35; Manage Versions and Deployments here or outside of Terraform&#10;&#35; resource &quot;cloudflare_worker_version&quot; &quot;my_worker_version&quot; {}&#10;&#35; resource &quot;cloudflare_workers_deployment&quot; &quot;my_worker_deployment&quot; {}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-deployments-are-always-explicit-never-implicit">Deployments are always explicit, never implicit</h4>
<p>Creating a version and deploying it are now always explicit, separate actions - never implicit side effects. To update version-specific settings (like bindings), you create a new version with those changes. The existing deployed version remains unchanged until you explicitly deploy the new one.</p>
<pre><code class="language-sh">&#35; Step 1: Create a new version with updated settings (doesn&#x27;t affect live traffic)&#10;POST /workers/workers/{id}/versions&#10;{&#10;  &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;  &quot;bindings&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;MY_NEW_ENV_VAR&quot;,&#10;      &quot;text&quot;: &quot;new_value&quot;,&#10;      &quot;type&quot;: &quot;plain_text&quot;&#10;    }&#10;  ],&#10;  &quot;modules&quot;: [...]&#10;}&#10;&#10;&#35; Step 2: Explicitly deploy when ready (now affects live traffic)&#10;POST /workers/scripts/{script_name}/deployments&#10;{&#10;  &quot;strategy&quot;: &quot;percentage&quot;,&#10;  &quot;versions&quot;: [&#10;    {&#10;      &quot;percentage&quot;: 100,&#10;      &quot;version_id&quot;: &quot;new_version_id&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-settings-are-clearly-organized-by-scope">Settings are clearly organized by scope</h4>
Configuration is now logically divided: [**Worker settings**](/api/resources/workers/subresources/beta/subresources/workers/) (like `name` and `tags`) persist across all versions, while [**Version settings**](/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/) (like `bindings` and `compatibility_date`) are specific to each code snapshot.
<pre><code class="language-sh">&#35; Worker settings (the parent resource)&#10;PUT /workers/workers/{id}&#10;{&#10;  &quot;name&quot;: &quot;payment-service&quot;,&#10;  &quot;tags&quot;: [&quot;production&quot;],&#10;  &quot;logpush&quot;: true,&#10;}&#10;</code></pre>
<pre><code class="language-sh">&#35; Version settings (the &quot;code&quot;)&#10;POST /workers/workers/{id}/versions&#10;{&#10;  &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;  &quot;bindings&quot;: [...],&#10;  &quot;modules&quot;: [...]&#10;}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-workers-api-endpoints-now-support-uuids-in-addition-to-names"><code>/workers</code> API endpoints now support UUIDs (in addition to names)</h4>
<p>The <code>/workers/workers/</code> path now supports addressing a Worker by both its immutable UUID and its mutable name.</p>
<pre><code class="language-sh">&#35; Both work for the same Worker&#10;GET /workers/workers/29494978e03748669e8effb243cf2515  # UUID (stable for automation)&#10;GET /workers/workers/payment-service                  # Name (convenient for humans)&#10;</code></pre>
<p>This dual approach means:</p>
<ul>
<li>Developers can use readable names for debugging.</li>
<li>Automation can rely on stable UUIDs to prevent errors when Workers are renamed.</li>
<li>Terraform can rename Workers without destroying and recreating them.</li>
</ul>
<h4 id="2025-09-03-new-workers-api-learn-more">Learn more</h4>
- [Infrastructure as Code (IaC) guide](/workers/platform/infrastructure-as-code)
- [API documentation](/api/resources/workers/subresources/beta/)
- [Versions and Deployments overview](/workers/versions-and-deployments/)
<h4 id="2025-09-03-new-workers-api-technical-notes">Technical notes</h4>
<ul>
<li>The pre-existing Workers REST API remains fully supported. Once the new API exits beta, we'll provide a migration timeline with ample notice and comprehensive migration guides.</li>
<li>Existing Terraform resources and SDK methods will continue to be fully supported through the current major version.</li>
<li>While the Deployments API currently remains on the <code>/scripts/</code> endpoint, we plan to introduce a new Deployments endpoint under <code>/workers/</code> to match the new API structure.</li>
</ul>


<h2 id="content-type-returned-in-workers-assets-for-javascript-files-is-now-text-javascript"><a href="/changelog/post/2025-08-25-workers-assets-javascript-content-type/">Content type returned in Workers Assets for Javascript files is now `text/javascript`</a></h2>
<p><em>2025-08-25</em></p>
<p>JavaScript asset responses have been updated to use the <code>text/javascript</code> Content-Type header instead of <code>application/javascript</code>. While both MIME types are widely supported by browsers, the HTML Living Standard explicitly recommends <code>text/javascript</code> as the preferred type going forward.</p>
<p>This change improves:</p>
<ul>
<li>Standards alignment: Ensures consistency with the HTML spec and modern web platform guidance.</li>
<li>Interoperability: Some developer tools, validators, and proxies expect text/javascript and may warn or behave inconsistently with application/javascript.</li>
<li>Future-proofing: By following the spec-preferred MIME type, we reduce the risk of deprecation warnings or unexpected behavior in evolving browser environments.</li>
<li>Consistency: Most frameworks, CDNs, and hosting providers now default to text/javascript, so this change matches common ecosystem practice.</li>
</ul>
<p>Because all major browsers accept both MIME types, this update is backwards compatible and should not cause breakage.</p>
<p>Users will see this change on the next deployment of their assets.</p>


<h2 id="build-durable-multi-step-applications-in-python-with-workflows-now-in-beta"><a href="/changelog/post/2025-08-22-workflows-python-beta/">Build durable multi-step applications in Python with Workflows (now in beta)</a></h2>
<p><em>2025-08-22</em></p>
<p>You can now build <a href="/workflows/">Workflows</a> using Python. With Python Workflows, you get automatic retries, state persistence, and the ability to run multi-step operations that can span minutes, hours, or weeks using Python’s familiar syntax and the <a href="/workers/languages/python/">Python Workers</a> runtime.</p>
<p>Python Workflows use the same step-based execution model as JavaScript Workflows, but with Python syntax and access to Python’s ecosystem. Python Workflows also enable <a href="/workflows/python/dag/">DAG (Directed Acyclic Graph) workflows</a>, where you can define complex dependencies between steps using the depends parameter.</p>
<p>Here’s a simple example:</p>
<pre><code class="language-python">from workers import Response, WorkflowEntrypoint&#10;&#10;class PythonWorkflowStarter(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do(&quot;my first step&quot;)&#10;        async def my_first_step():&#10;            &#35; do some work&#10;            return &quot;Hello Python!&quot;&#10;&#10;        await my_first_step()&#10;&#10;        await step.sleep(&quot;my-sleep-step&quot;, &quot;10 seconds&quot;)&#10;&#10;        @step.do(&quot;my second step&quot;)&#10;        async def my_second_step():&#10;            &#35; do some more work&#10;            return &quot;Hello again!&quot;&#10;&#10;        await my_second_step()&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        await self.env.MY_WORKFLOW.create()&#10;        return Response(&quot;Hello Workflow creation!&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17831.md")</aside>
<p>Python Workflows support the same core capabilities as JavaScript Workflows, including sleep scheduling, event-driven workflows, and built-in error handling with configurable retry policies.</p>
<p>To learn more and get started, refer to <a href="/workflows/python/">Python Workflows documentation</a>.</p>


<h2 id="new-getbyname-api-to-access-durable-objects"><a href="/changelog/post/2025-08-21-durable-objects-get-by-name/">New getByName() API to access Durable Objects</a></h2>
<p><em>2025-08-21</em></p>
<p>You can now create a client (a <a href="/durable-objects/api/stub/">Durable Object stub</a>) to a Durable Object with the new <code>getByName</code> method, removing the need to convert Durable Object names to IDs and then create a stub.</p>
<pre><code class="language-js">// Before: (1) translate name to ID then (2) get a client &#10;const objectId = env.MY_DURABLE_OBJECT.idFromName(&quot;foo&quot;); // or .newUniqueId()&#10;const stub = env.MY_DURABLE_OBJECT.get(objectId); &#10;&#10;// Now: retrieve client to Durable Object directly via its name &#10;const stub = env.MY_DURABLE_OBJECT.getByName(&quot;foo&quot;);&#10;&#10;// Use client to send request to the remote Durable Object&#10;const rpcResponse = await stub.sayHello();&#10;</code></pre>
<p>Each Durable Object has a globally-unique name, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together. You can have billions of Durable Objects, providing isolation between application tenants.</p>
<p>To learn more, visit the Durable Objects <a href="/durable-objects/api/namespace/#getbyname">API Documentation</a> or the <a href="/durable-objects/get-started/">getting started guide</a>.</p>


<h2 id="easier-debugging-in-workers-with-improved-wrangler-error-screen"><a href="/changelog/post/2025-08-19-improved-wrangler-error-screen/">Easier debugging in Workers with improved Wrangler error screen</a></h2>
<p><em>2025-08-19</em></p>
<p>Wrangler's error screen has received several improvements to enhance your debugging experience!</p>
<p>The error screen now features a refreshed design thanks to <a href="https://www.npmjs.com/package/youch">youch</a>, with support for both light and dark themes, improved source map resolution logic that handles missing source files more reliably, and better error cause display.</p>
<table>
<thead>
<tr>
<th>Before</th>
<th>After (Light)</th>
<th>After (Dark)</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="/assets/upstream/images/workers/changelog/old-error-screen.png" alt="Old error screen" /></td>
<td><img src="/assets/upstream/images/workers/changelog/new-error-screen-light.png" alt="New light theme error screen" /></td>
<td><img src="/assets/upstream/images/workers/changelog/new-error-screen-dark.png" alt="New dark theme error screen" /></td>
</tr>
</tbody>
</table>
<p>Try it out now with <code>npx wrangler@latest dev</code> in your Workers project.</p>


<h2 id="the-node-js-and-web-file-system-apis-in-workers"><a href="/changelog/post/2025-08-15-nodejs-fs/">The Node.js and Web File System APIs in Workers</a></h2>
<p><em>2025-08-15</em></p>
<p>Implementations of the <a href="https://nodejs.org/docs/latest/api/fs.html"><code>node:fs</code> module</a> and the <a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API">Web File System API</a> are now available in Workers.</p>
<h4 id="2025-08-15-nodejs-fs-using-the-node-fs-module">Using the <code>node:fs</code> module</h4>
<p>The <code>node:fs</code> module provides access to a virtual file system in Workers. You can use it to read and write files, create directories, and perform other file system operations.</p>
<p>The virtual file system is ephemeral with each individual request havig its own isolated temporary file space. Files written to the file system will not persist across requests and will not be shared across requests or across different Workers.</p>
<p>Workers running with the <code>nodejs_compat</code> compatibility flag will have access to the <code>node:fs</code> module by default when the compatibility date is set to <code>2025-09-01</code> or later. Support for the API can also be enabled using the <code>enable_nodejs_fs_module</code> compatibility flag together with the <code>nodejs_compat</code> flag. The <code>node:fs</code> module can be disabled using the <code>disable_nodejs_fs_module</code> compatibility flag.</p>
<pre><code class="language-js">import fs from &quot;node:fs&quot;;&#10;&#10;const config = JSON.parse(fs.readFileSync(&quot;/bundle/config.json&quot;, &quot;utf-8&quot;));&#10;&#10;export default {&#10;	async fetch(request) {&#10;		return new Response(`Config value: ${config.value}`);&#10;	},&#10;};&#10;</code></pre>
<p>There are a number of initial limitations to the <code>node:fs</code> implementation:</p>
<ul>
<li>The glob APIs (e.g. <code>fs.globSync(...)</code>) are not implemented.</li>
<li>The file watching APIs (e.g. <code>fs.watch(...)</code>) are not implemented.</li>
<li>The file timestamps (modified time, access time, etc) are only partially supported. For now, these will always return the Unix epoch.</li>
</ul>
<p>Refer to the <a href="https://nodejs.org/docs/latest/api/fs.html">Node.js documentation</a> for more information on the <code>node:fs</code> module and its APIs.</p>
<h4 id="2025-08-15-nodejs-fs-the-web-file-system-api">The Web File System API</h4>
<p>The Web File System API provides access to the same virtual file system as the <code>node:fs</code> module, but with a different API surface. The Web File System API is only available in Workers running with the <code>enable_web_file_system</code> compatibility flag. The <code>nodejs_compat</code> compatibility flag is not required to use the Web File System API.</p>
<pre><code class="language-js">const root = navigator.storage.getDirectory();&#10;&#10;export default {&#10;	async fetch(request) {&#10;		const tmp = await root.getDirectoryHandle(&quot;/tmp&quot;);&#10;		const file = await tmp.getFileHandle(&quot;data.txt&quot;, { create: true });&#10;		const writable = await file.createWritable();&#10;		const writer = writable.getWriter();&#10;		await writer.write(&quot;Hello, World!&quot;);&#10;		await writer.close();&#10;&#10;		return new Response(&quot;File written successfully!&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>As there are still some parts of the Web File System API that are not fully standardized, there may be some differences between the Workers implementation and the implementations in browsers.</p>


<h2 id="workers-static-assets-corrected-handling-of-double-slashes-in-redirect-rule-paths"><a href="/changelog/post/2025-08-15-static-assets-redirect-url/">Workers Static Assets: Corrected handling of double slashes in redirect rule paths</a></h2>
<p><em>2025-08-15</em></p>
<p><a href="/workers/static-assets/">Static Assets</a>: Fixed a bug in how <a href="https://developers.cloudflare.com/workers/static-assets/redirects/">redirect rules</a> defined in your Worker's <code>_redirects</code> file are processed.</p>
<p>If you're serving Static Assets with a <code>_redirects</code> file containing a rule like <code>/ja/* /:splat</code>, paths with double slashes were previously misinterpreted as external URLs. For example, visiting <code>/ja//example.com</code> would incorrectly redirect to <code>https://example.com</code> instead of <code>/example.com</code> on your domain. This has been fixed and double slashes now correctly resolve as local paths. Note: <a href="/pages/">Cloudflare Pages</a> was not affected by this issue.</p>


<h2 id="workers-per-branch-preview-urls-now-support-long-branch-names"><a href="/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/">Workers per-branch preview URLs now support long branch names</a></h2>
<p><em>2025-08-14T01:00:00+00:00</em></p>
<p>We've updated <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> for Cloudflare Workers to support long branch names.</p>
<p>Previously, branch and Worker names exceeding the 63-character DNS limit would cause alias generation to fail, leaving pull requests without aliased preview URLs. This particularly impacted teams relying on descriptive branch naming.</p>
<p>Now, Cloudflare automatically truncates long branch names and appends a unique hash, ensuring every pull request gets a working preview link.</p>
<h4 id="2025-08-08-support-long-branch-names-preview-aliases-how-it-works">How it works</h4>
<ul>
<li><strong>63 characters or less</strong>: <code>&lt;branch-name&gt;-&lt;worker-name&gt;</code> → Uses actual branch name as is</li>
<li><strong>64 characters or more</strong>: <code>&lt;truncated-branch-name&gt;--&lt;hash&gt;-&lt;worker-name&gt;</code> → Uses truncated name with 4-character hash</li>
<li><strong>Hash generation</strong>: The hash is derived from the full branch name to ensure uniqueness</li>
<li><strong>Stable URLs</strong>: The same branch always generates the same hash across all commits</li>
</ul>
<h4 id="2025-08-08-support-long-branch-names-preview-aliases-requirements-and-compatibility">Requirements and compatibility</h4>
<ul>
<li><strong>Wrangler 4.30.0 or later</strong>: This feature requires updating to wrangler@4.30.0+</li>
<li><strong>No configuration needed</strong>: Works automatically with existing preview URL setups</li>
</ul>


<h2 id="python-workers-handlers-now-live-in-an-entrypoint-class"><a href="/changelog/post/2025-08-14-new-python-handlers/">Python Workers handlers now live in an entrypoint class</a></h2>
<p><em>2025-08-14</em></p>
<p>We are changing how Python Workers are structured by default. Previously, handlers were defined at the top-level of a module as <code>on_fetch</code>, <code>on_scheduled</code>, etc. methods, but now they live in an entrypoint class.</p>
<p>Here's an example of how to now define a Worker with a fetch handler:</p>
<pre><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(&quot;Hello World!&quot;)&#10;</code></pre>
<p>To keep using the old-style handlers, you can specify the <code>disable_python_no_global_handlers</code> compatibility flag in your wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17785.md")</div>
<p>Consult the <a href="/workers/languages/python/">Python Workers documentation</a> for more details.</p>


<h2 id="terraform-provider-improvements-python-workers-support-smaller-plan-diffs-and-api-sdk-fixes"><a href="/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/">Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes</a></h2>
<p><em>2025-08-14</em></p>
<p>The recent <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script">Cloudflare Terraform Provider</a> and SDK releases (such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a>) bring significant improvements to the Workers developer experience. These updates focus on reliability, performance, and adding <a href="/workers/languages/python/">Python Workers</a> support.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-terraform-improvements">Terraform Improvements</h4>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-fixed-unwarranted-plan-diffs">Fixed Unwarranted Plan Diffs</h4>
<p>Resolved several issues with the <code>cloudflare_workers_script</code> resource that resulted in unwarranted plan diffs, including:</p>
<ul>
<li>Using Durable Objects migrations</li>
<li>Using some bindings such as <code>secret_text</code></li>
<li>Using smart placement</li>
</ul>
<p>A resource should never show a plan diff if there isn't an actual change. This fix reduces unnecessary noise in your Terraform plan and is available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-improved-file-management">Improved File Management</h4>
<p>You can now specify <code>content_file</code> and <code>content_sha256</code> instead of <code>content</code>. This prevents the Workers script content from being stored in the state file which greatly reduces plan diff size and noise. If your workflow synced plans remotely, this should now happen much faster since there is less data to sync. This is available in Cloudflare Terraform Provider 5.7.0.</p>
<pre><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id      = &quot;123456789&quot;&#10;  script_name     = &quot;my_worker&quot;&#10;  main_module     = &quot;worker.mjs&quot;&#10;  content_file    = &quot;worker.mjs&quot;&#10;  content_sha256  = filesha256(&quot;worker.mjs&quot;)&#10;}&#10;</code></pre>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-assets-headers-and-redirects-support">Assets Headers and Redirects Support</h4>
<p>Fixed the <code>cloudflare_workers_script</code> resource to properly support headers and redirects for Assets:</p>
<pre><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id      = &quot;123456789&quot;&#10;  script_name     = &quot;my_worker&quot;&#10;  main_module     = &quot;worker.mjs&quot;&#10;  content_file    = &quot;worker.mjs&quot;&#10;  content_sha256  = filesha256(&quot;worker.mjs&quot;)&#10;  assets = {&#10;    config = {&#10;      headers = file(&quot;_headers&quot;)&#10;      redirects = file(&quot;_redirects&quot;)&#10;    }&#10;    &#35; Completion jwt from:&#10;    &#35; https://developers.cloudflare.com/api/resources/workers/subresources/assets/subresources/upload/&#10;    jwt = &quot;jwt&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-python-workers-support">Python Workers Support</h4>
<p>Added support for uploading <a href="/workers/languages/python/">Python Workers</a> (beta) in Terraform. You can now deploy Python Workers with:</p>
<pre><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id       = &quot;123456789&quot;&#10;  script_name      = &quot;my_worker&quot;&#10;  content_file     = &quot;worker.py&quot;&#10;  content_sha256   = filesha256(&quot;worker.py&quot;)&#10;  content_type     = &quot;text/x-python&quot;&#10;}&#10;</code></pre>
<p>Available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-sdk-enhancements">SDK Enhancements</h4>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-improved-file-upload-api">Improved File Upload API</h4>
<p>Fixed an issue where Workers script versions in the SDK did not allow uploading files. This now works, and also has an improved files upload interface:</p>
<pre><code class="language-js">const scriptContent = `&#10;  export default {&#10;    async fetch(request, env, ctx) {&#10;      return new Response(&#x27;Hello World!&#x27;, { status: 200 });&#10;    }&#10;  };&#10;`;&#10;&#10;client.workers.scripts.versions.create(&#x27;my-worker&#x27;, {&#10;  account_id: &#x27;123456789&#x27;,&#10;  metadata: {&#10;    main_module: &#x27;my-worker.mjs&#x27;,&#10;  },&#10;  files: [&#10;    await toFile(&#10;      Buffer.from(scriptContent),&#10;      &#x27;my-worker.mjs&#x27;,&#10;      {&#10;        type: &quot;application/javascript+module&quot;,&#10;      }&#10;    )&#10;  ]&#10;});&#10;</code></pre>
<p>Will be available in cloudflare-typescript 4.6.0. A similar change will be available in cloudflare-python 4.4.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-fixed-updating-kv-values">Fixed updating KV values</h4>
<p>Previously when creating a KV value like this:</p>
<pre><code class="language-js">await cf.kv.namespaces.values.update(&quot;my-kv-namespace&quot;, &quot;key1&quot;, {&#10;  account_id: &quot;123456789&quot;,&#10;  metadata: &quot;my metadata&quot;,&#10;  value: JSON.stringify({&#10;    hello: &quot;world&quot;&#10;  })&#10;});&#10;</code></pre>
<p>...and recalling it in your Worker like this:</p>
<pre><code class="language-ts">const value = await c.env.KV.get&lt;{hello: string}&gt;(&quot;key1&quot;, &quot;json&quot;);&#10;</code></pre>
<p>You'd get back this: <code>{metadata:'my metadata', value:&quot;{'hello':'world'}&quot;}</code> instead of the correct value of <code>{hello: 'world'}</code></p>
<p>This is fixed in cloudflare-typescript 4.5.0 and will be fixed in cloudflare-python 4.4.0.</p>


<h2 id="messagechannel-and-messageport"><a href="/changelog/post/2025-08-11-messagechannel/">MessageChannel and MessagePort</a></h2>
<p><em>2025-08-11T01:00:00+00:00</em></p>
<p>A minimal implementation of the <a href="https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel">MessageChannel API</a> is now available in Workers. This means that you can use <code>MessageChannel</code> to send messages between different parts of your Worker, but not across different Workers.</p>
<p>The <code>MessageChannel</code> and <code>MessagePort</code> APIs will be available by default at the global scope
with any worker using a compatibility date of <code>2025-08-15</code> or later. It is also available
using the <code>expose_global_message_channel</code> compatibility flag, or can be explicitly disabled
using the <code>no_expose_global_message_channel</code> compatibility flag.</p>
<pre><code class="language-js">const { port1, port2 } = new MessageChannel();&#10;&#10;port2.onmessage = (event) =&gt; {&#10;	console.log(&#x27;Received message:&#x27;, event.data);&#10;};&#10;&#10;port2.postMessage(&#x27;Hello from port2!&#x27;);&#10;</code></pre>
<p>Any value that can be used with the <code>structuredClone(...)</code> API can be sent over the port.</p>
<h4 id="2025-08-11-messagechannel-differences">Differences</h4>
<p>There are a number of key limitations to the <code>MessageChannel</code> API in Workers:</p>
<ul>
<li>Transfer lists are currently not supported. This means that you will not be able to transfer
ownership of objects like <code>ArrayBuffer</code> or <code>MessagePort</code> between ports.</li>
<li>The <code>MessagePort</code> is not yet serializable. This means that you cannot send a <code>MessagePort</code> object
through the <code>postMessage</code> method or via JSRPC calls.</li>
<li>The <code>'messageerror'</code> event is only partially supported. If the <code>'onmessage'</code> handler throws an
error, the <code>'messageerror'</code> event will be triggered, however, it will not be triggered when there
are errors serializing or deserializing the message data. Instead, the error will be thrown when
the <code>postMessage</code> method is called on the sending port.</li>
<li>The <code>'close'</code> event will be emitted on both ports when one of the ports is closed, however it
will not be emitted when the Worker is terminated or when one of the ports is garbage collected.</li>
</ul>


<h2 id="wrangler-and-the-cloudflare-vite-plugin-support-env-files-in-local-development"><a href="/changelog/post/2025-08-08-dot-env-in-local-dev/">Wrangler and the Cloudflare Vite plugin support `.env` files in local development</a></h2>
<p><em>2025-08-08T01:00:00+00:00</em></p>
<p>Now, you can use <code>.env</code> files to provide secrets and override environment variables on the <code>env</code> object during local development with Wrangler and the Cloudflare Vite plugin.</p>
<p>Previously in local development, if you wanted to provide secrets or environment variables during local development, you had to use <code>.dev.vars</code> files.
This is still supported, but you can now also use <code>.env</code> files, which are more familiar to many developers.</p>
<h4 id="2025-08-08-dot-env-in-local-dev-using-env-files-in-local-development">Using <code>.env</code> files in local development</h4>
<p>You can create a <code>.env</code> file in your project root to define environment variables that will be used when running <code>wrangler dev</code> or <code>vite dev</code>. The <code>.env</code> file should be formatted like a <code>dotenv</code> file, such as <code>KEY=&quot;VALUE&quot;</code>:</p>
<pre><code class="language-bash">TITLE=&quot;My Worker&quot;&#10;API_TOKEN=&quot;dev-token&quot;&#10;</code></pre>
<p>When you run <code>wrangler dev</code> or <code>vite dev</code>, the environment variables defined in the <code>.env</code> file will be available in your Worker code via the <code>env</code> object:</p>
<pre><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		const title = env.TITLE; // &quot;My Worker&quot;&#10;		const apiToken = env.API_TOKEN; // &quot;dev-token&quot;&#10;		const response = await fetch(&#10;			`https://api.example.com/data?token=${apiToken}`,&#10;		);&#10;		return new Response(`Title: ${title} - ` + (await response.text()));&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-08-08-dot-env-in-local-dev-multiple-environments-with-env-files">Multiple environments with <code>.env</code> files</h4>
<p>If your Worker defines multiple <a href="/workers/wrangler/environments/">environments</a>, you can set different variables for each environment (ex: production or staging) by creating files named <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you use <code>wrangler &lt;command&gt; --env &lt;environment-name&gt;</code> or <code>CLOUDFLARE_ENV=&lt;environment-name&gt; vite dev</code>, the corresponding environment-specific file will also be loaded and merged with the <code>.env</code> file.</p>
<p>For example, if you want to set different environment variables for the <code>staging</code> environment, you can create a file named <code>.env.staging</code>:</p>
<pre><code class="language-bash">API_TOKEN=&quot;staging-token&quot;&#10;</code></pre>
<p>When you run <code>wrangler dev --env staging</code> or <code>CLOUDFLARE_ENV=staging vite dev</code>, the environment variables from <code>.env.staging</code> will be merged onto those from <code>.env</code>.</p>
<pre><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		const title = env.TITLE; // &quot;My Worker&quot; (from `.env`)&#10;		const apiToken = env.API_TOKEN; // &quot;staging-token&quot; (from `.env.staging`, overriding the value from `.env`)&#10;		const response = await fetch(&#10;			`https://api.example.com/data?token=${apiToken}`,&#10;		);&#10;		return new Response(`Title: ${title} - ` + (await response.text()));&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-08-08-dot-env-in-local-dev-find-out-more">Find out more</h4>
<p>For more information on how to use <code>.env</code> files with Wrangler and the Cloudflare Vite plugin, see the following documentation:</p>
<ul>
<li><a href="/workers/local-development/environment-variables">Environment variables and secrets</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler">Wrangler Documentation</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler/vite">Cloudflare Vite Plugin Documentation</a></li>
</ul>


<h2 id="directly-import-waituntil-in-workers-for-easily-spawning-background-tasks"><a href="/changelog/post/2025-08-08-add-waituntil-cloudflare-workers/">Directly import `waitUntil` in Workers for easily spawning background tasks</a></h2>
<p><em>2025-08-08</em></p>
<p>You can now import <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a> from <code>cloudflare:workers</code> to extend your Worker's execution beyond the request lifecycle from anywhere in your code.</p>
<p>Previously, <code>waitUntil</code> could only be accessed through the <a href="/workers/runtime-apis/context/">execution context</a> (<code>ctx</code>) parameter passed to your Worker's handler functions. This meant that if you needed to schedule background tasks from deeply nested functions or utility modules, you had to pass the <code>ctx</code> object through multiple function calls to access <code>waitUntil</code>.</p>
<p>Now, you can import <code>waitUntil</code> directly and use it anywhere in your Worker without needing to pass <code>ctx</code> as a parameter:</p>
<pre><code class="language-js">import { waitUntil } from &quot;cloudflare:workers&quot;;&#10;&#10;export function trackAnalytics(eventData) {&#10;	const analyticsPromise = fetch(&quot;https://analytics.example.com/track&quot;, {&#10;		method: &quot;POST&quot;,&#10;		body: JSON.stringify(eventData),&#10;	});&#10;&#10;	// Extend execution to ensure analytics tracking completes&#10;	waitUntil(analyticsPromise);&#10;}&#10;</code></pre>
<p>This is particularly useful when you want to:</p>
<ul>
<li>Schedule background tasks from utility functions or modules</li>
<li>Extend execution for analytics, logging, or cleanup operations</li>
<li>Avoid passing the execution context through multiple layers of function calls</li>
</ul>
<pre><code class="language-js">import { waitUntil } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Background task that should complete even after response is sent&#10;		cleanupTempData(env.KV_NAMESPACE);&#10;		return new Response(&quot;Hello, World!&quot;);&#10;	}&#10;};&#10;&#10;function cleanupTempData(kvNamespace) {&#10;	// This function can now use waitUntil without needing ctx&#10;	const deletePromise = kvNamespace.delete(&quot;temp-key&quot;);&#10;	waitUntil(deletePromise);&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17784.md")</aside>
<p>For more information, see the <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code> documentation</a>.</p>


<h2 id="requests-made-from-cloudflare-workers-can-now-force-a-revalidation-of-their-cache-with-the-origin"><a href="/changelog/post/2025-08-07-cache-no-cache/">Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin</a></h2>
<p><em>2025-08-07</em></p>
<p>By setting the value of the <code>cache</code> property to <code>no-cache</code>, you can force <a href="/workers/reference/how-the-cache-works/">Cloudflare's
cache</a> to revalidate its contents with the origin when
making subrequests from <a href="/workers">Cloudflare Workers</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17783.md")</div>
<p>When <code>no-cache</code> is set, the Worker request will first look for a match in Cloudflare's cache, then:</p>
<ul>
<li>If there is a match, a conditional request is sent to the origin, regardless of whether or not the match is fresh or stale. If the resource has not changed, the
cached version is returned. If the resource has changed, it will be downloaded from the origin, updated in the cache, and returned.</li>
<li>If there is no match, Workers will make a standard request to the origin and cache the response.</li>
</ul>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the
<a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part
of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code>
property on <code>Request</code> to <code>'no-cache'</code>, the Workers runtime threw an exception.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>


<h2 id="agents-sdk-adds-mcp-elicitation-support-http-streamable-support-task-queues-email-integration-and-more"><a href="/changelog/post/2025-08-05-agents-MCP-update/">Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more</a></h2>
<p><em>2025-08-05</em></p>
<p>The latest releases of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings major improvements to MCP transport protocols support and agents connectivity. Key updates include:</p>
<h4 id="2025-08-05-agents-MCP-update-mcp-elicitation-support">MCP elicitation support</h4>
<p>MCP servers can now request user input during tool execution, enabling interactive workflows like confirmations, forms, and multi-step processes. This feature uses durable storage to preserve elicitation state even during agent hibernation, ensuring seamless user interactions across agent lifecycle events.</p>
<pre><code class="language-ts">// Request user confirmation via elicitation&#10;const confirmation = await this.elicitInput({&#10;	message: `Are you sure you want to increment the counter by ${amount}?`,&#10;	requestedSchema: {&#10;		type: &quot;object&quot;,&#10;		properties: {&#10;			confirmed: {&#10;				type: &quot;boolean&quot;,&#10;				title: &quot;Confirm increment&quot;,&#10;				description: &quot;Check to confirm the increment&quot;,&#10;			},&#10;		},&#10;		required: [&quot;confirmed&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Check out our <a href="https://github.com/whoiskatrin/agents/tree/main/examples/mcp-elicitation-demo">demo</a> to see elicitation in action.</p>
<h4 id="2025-08-05-agents-MCP-update-http-streamable-transport-for-mcp">HTTP streamable transport for MCP</h4>
<p>MCP now supports HTTP streamable transport which is recommended over SSE. This transport type offers:</p>
<ul>
<li><strong>Better performance</strong>: More efficient data streaming and reduced overhead</li>
<li><strong>Improved reliability</strong>: Enhanced connection stability and error recover- <strong>Automatic fallback</strong>: If streamable transport is not available, it gracefully falls back to SSE</li>
</ul>
<pre><code class="language-ts">export default MyMCP.serve(&quot;/mcp&quot;, {&#10;	binding: &quot;MyMCP&quot;,&#10;});&#10;</code></pre>
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
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	doSomethingExpensive(payload) {&#10;		// a long running process that you want to run in the background&#10;	}&#10;&#10;	queueSomething() {&#10;		await this.queue(&quot;doSomethingExpensive&quot;, somePayload); // this will NOT block further execution, and runs in the background&#10;		await this.queue(&quot;doSomethingExpensive&quot;, someOtherPayload); // the callback will NOT run until the previous callback is complete&#10;		// ... call as many times as you want&#10;	}&#10;}&#10;</code></pre>
<p>Want to try it yourself? Just define a method like processMessage in your agent, and you’re ready to scale.</p>
<h4 id="2025-08-05-agents-MCP-update-new-email-adapter">New email adapter</h4>
<p>Want to build an AI agent that can receive and respond to emails automatically? With the new email adapter and onEmail lifecycle method, now you can.</p>
<pre><code class="language-ts">export class EmailAgent extends Agent {&#10;	async onEmail(email: AgentEmail) {&#10;		const raw = await email.getRaw();&#10;		const parsed = await PostalMime.parse(raw);&#10;&#10;		// create a response based on the email contents&#10;		// and then send a reply&#10;&#10;		await this.replyToEmail(email, {&#10;			fromName: &quot;Email Agent&quot;,&#10;			body: `Thanks for your email! You&#x27;ve sent us &quot;${parsed.subject}&quot;. We&#x27;ll process it shortly.`,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>You route incoming mail like this:</p>
<pre><code class="language-ts">export default {&#10;	async email(email, env) {&#10;		await routeAgentEmail(email, env, {&#10;			resolver: createAddressBasedEmailResolver(&quot;EmailAgent&quot;),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>You can find a full example <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">here</a>.</p>
<h4 id="2025-08-05-agents-MCP-update-automatic-context-wrapping-for-custom-methods">Automatic context wrapping for custom methods</h4>
<p>Custom methods are now automatically wrapped with the agent's context, so calling <code>getCurrentAgent()</code> should work regardless of where in an agent's lifecycle it's called. Previously this would not work on RPC calls, but now just works out of the box.</p>
<pre><code class="language-ts">export class MyAgent extends Agent {&#10;	async suggestReply(message) {&#10;		// getCurrentAgent() now correctly works, even when called inside an RPC method&#10;		const { agent } = getCurrentAgent()!;&#10;		return generateText({&#10;			prompt: `Suggest a reply to: &quot;${message}&quot; from &quot;${agent.name}&quot;`,&#10;			tools: [replyWithEmoji],&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>Try it out and tell us what you build!</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/6/">Previous</a><span>Page 7 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/8/">Next</a></nav>
