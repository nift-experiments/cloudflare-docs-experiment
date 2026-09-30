---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/14/
  description: '2026-01-07'
  full_title: Developer platform changelog - page 14 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 14 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-01-07"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/14/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 14"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-01-07"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/14/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/14/#page","headline":"Developer platform changelog - page 14 | Cloudflare Docs","description":"2026-01-07","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/14/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/14/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

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


<h2 id="custom-container-instance-types-now-available-for-all-users"><a href="/changelog/post/2026-01-05-custom-instance-types/">Custom container instance types now available for all users</a></h2>
<p><em>2026-01-05</em></p>
<p>Custom instance types are now enabled for all <a href="/containers">Cloudflare Containers</a> users. You can now specify specific vCPU, memory, and disk amounts, rather than being limited to pre-defined <a href="/containers/platform/limits/#instance-types">instance types</a>. Previously, only select Enterprise customers were able to customize their instance type.</p>
<p>To use a custom instance type, specify the <code>instance_type</code> property as an object with <code>vcpu</code>, <code>memory_mib</code>, and <code>disk_mb</code> fields in your Wrangler configuration:</p>
<pre tabindex="0"><code class="language-toml">[[containers]]&#10;image = &quot;./Dockerfile&quot;&#10;instance_type = { vcpu = 2, memory_mib = 6144, disk_mb = 12000 }&#10;</code></pre>
<p>Individual limits for custom instance types are based on the <code>standard-4</code> instance type (4 vCPU, 12 GiB memory, 20 GB disk). You must allocate at least 1 vCPU for custom instance types. For workloads requiring less than 1 vCPU, use the predefined instance types like <code>lite</code> or <code>basic</code>.</p>
<p>See the <a href="/containers/platform/limits/#custom-instance-types">limits documentation</a> for the full list of constraints on custom instance types.
See the <a href="/containers/get-started/">getting started guide</a> to deploy your first Container,</p>


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


<h2 id="terraform-v5-15-0-now-available"><a href="/changelog/post/2025-12-19-terraform-v5.15.0-provider/">Terraform v5.15.0 now available</a></h2>
<p><em>2025-12-19</em></p>
<p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.15 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2025-12-19-terraform-v5.15.0-provider-features">Features</h4>
<ul>
<li><strong>ai_search:</strong> Add AI Search endpoints (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/6f02adb420e872457f71f95b49cb527663388915">6f02adb</a>)</li>
<li><strong>certificate_pack:</strong> Ensure proper Terraform resource ID handling for path parameters in API calls (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/081f32acab4ce9a194a7ff51c8e9fcabd349895a">081f32a</a>)</li>
<li><strong>worker_version:</strong> Support <code>startup_time_ms</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/286ab55bea8d5be0faa5a2b5b8b157e4a2214eba">286ab55</a>)</li>
<li><strong>zero_trust_dlp_custom_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_integration_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_dlp_predefined_entry:</strong> Support <code>upload_status</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/7dc0fe3b23726ead8dc075f86728a0540846d90c">7dc0fe3</a>)</li>
<li><strong>zero_trust_gateway_policy:</strong> Support <code>forensic_copy</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b">5741fd0</a>)</li>
<li><strong>zero_trust_list:</strong> Support additional types (category, location, device) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5741fd0ed9f7270d20731cc47ec45eb0403a628b">5741fd0</a>)</li>
</ul>
<h4 id="2025-12-19-terraform-v5.15.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>access_rules:</strong> Add validation to prevent state drift. Ideally, we'd use Semantic Equality but since that isn't an option, this will remove a foot-gun. (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/44577911b3cbe45de6279aefa657bdee73c0794d">4457791</a>)</li>
<li><strong>cloudflare_pages_project:</strong> Addressing drift issues (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/6edffcfcf187fdc9b10b624b9a9b90aed2fb2b2e">6edffcf</a>) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/3db318e747423bf10ce587d9149e90edcd8a77b0">3db318e</a>)</li>
<li><strong>cloudflare_worker:</strong> Can be cleanly imported (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/4859b52968bb25570b680df9813f8e07fd50728f">4859b52</a>)</li>
<li><strong>cloudflare_worker:</strong> Ensure clean imports (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/5b525bc478a4e2c9c0d4fd659b92cc7f7c18016a">5b525bc</a>)</li>
<li><strong>list_items:</strong> Add validation for IP List items to avoid inconsistent state (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/b6733dc4be909a5ab35895a88e519fc2582ccada">b6733dc</a>)</li>
<li><strong>zero_trust_access_application:</strong> Remove all conditions from sweeper (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/3197f1aed61be326d507d9e9e3b795b9f1d18fd7">3197f1a</a>)</li>
<li><strong>spectrum_application:</strong> Map missing fields during spectrum resource import (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6495">#6495</a>) (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/commit/ddb4e722b82c735825a549d651a9da219c142efa">ddb4e72</a>)</li>
</ul>
<h4 id="2025-12-19-terraform-v5.15.0-provider-upgrade-to-newer-version">Upgrade to newer version</h4>
We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-12-19-terraform-v5.15.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)


<h2 id="static-prerendering-support-for-tanstack-start"><a href="/changelog/post/2025-12-19-tanstack-start-prerendering/">Static prerendering support for TanStack Start</a></h2>
<p><em>2025-12-19</em></p>
<p><a href="https://tanstack.com/start/">TanStack Start</a> apps can now prerender routes to static HTML at build time with access to build time environment variables
and bindings,  and serve them as <a href="/workers/static-assets/">static assets</a>. To enable prerendering, configure the <code>prerender</code> option of the TanStack Start plugin in your Vite config:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;&#10;export default defineConfig({&#10;  plugins: [&#10;    cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }),&#10;    tanstackStart({&#10;      prerender: {&#10;        enabled: true,&#10;      },&#10;    }),&#10;  ],&#10;});&#10;</code></pre>
<p>This feature requires <code>@tanstack/react-start</code> v1.138.0 or later. See the <a href="/workers/framework-guides/web-apps/tanstack-start/#static-prerendering">TanStack Start framework guide</a> for more details.</p>


<h2 id="r2-data-catalog-now-supports-automatic-snapshot-expiration"><a href="/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/">R2 Data Catalog now supports automatic snapshot expiration</a></h2>
<p><em>2025-12-18</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> now supports automatic snapshot expiration for Apache Iceberg tables.</p>
<p>In Apache Iceberg, a snapshot is metadata that represents the state of a table at a given point in time. Every mutation creates a new snapshot which enable powerful features like time travel queries and rollback capabilities but will accumulate over time.</p>
<p>Without regular cleanup, these accumulated snapshots can lead to:</p>
<ul>
<li>Metadata overhead</li>
<li>Slower table operations</li>
<li>Increased storage costs.</li>
</ul>
<p>Snapshot expiration in R2 Data Catalog automatically removes old table snapshots based on your configured retention policy, improving performance and storage costs.</p>
<pre tabindex="0"><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;&#35; Expire snapshots older than 7 days, always retain at least 10 recent snapshots&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>Snapshot expiration uses two parameters to determine which snapshots to remove:</p>
<ul>
<li><code>--older-than-days</code>: age threshold in days</li>
<li><code>--retain-last</code>: minimum snapshot count to retain</li>
</ul>
<p>Both conditions must be met before a snapshot is expired, ensuring you always retain recent snapshots even if they exceed the age threshold.</p>
<p>This feature complements <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a>, which optimizes query performance by combining small data files into larger ones. Together, these automatic maintenance operations keep your Iceberg tables performant and cost-efficient without manual intervention.</p>
<p>For more information, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a> or <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>


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


<h2 id="workers-for-platforms-dashboard-improvements"><a href="/changelog/post/2025-12-18-dashboard-improvements/">Workers for Platforms - Dashboard Improvements</a></h2>
<p><em>2025-12-18</em></p>
<p><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> lets you build multi-tenant platforms on <a href="/workers/">Cloudflare Workers</a>, allowing your end users to deploy and run their own code on your platform. It's designed for anyone building an AI vibe coding platform, e-commerce platform, website builder, or any product that needs to securely execute user-generated code at scale.</p>
<p>Previously, setting up Workers for Platforms required using the API. Now, the Workers for Platforms UI supports namespace creation, dispatch worker templates, and tag management, making it easier for Workers for Platforms customers to build and manage multi-tenant platforms directly from the Cloudflare dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers-for-platforms/dashboard-improvements.png" alt="Workers for Platforms Dashboard Improvements" /></p>
<h4 id="2025-12-18-dashboard-improvements-key-improvements">Key improvements</h4>
<ul>
<li><strong>Namespace Management:</strong> You can now create and configure <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace">dispatch namespaces</a> directly within the dashboard to start a new platform setup.</li>
<li><strong>Dispatch Worker Templates:</strong> New Dispatch Worker templates allow you to quickly define how traffic is routed to individual Workers within your namespace. Refer to the <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dynamic Dispatch documentation</a> for more examples.</li>
<li><strong>Tag Management:</strong> You can now set and update <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/tags/">tags</a> on User Workers, making it easier to group and manage your Workers.</li>
<li><strong>Binding Visibility:</strong> <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">Bindings</a> attached to User Workers are now visible directly within the User Worker view.</li>
<li><strong>Deploy Vibe Coding Platform in one-click:</strong> Deploy a <a href="/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">reference implementation</a> of an AI vibe coding platform directly from the dashboard. Powered by the Cloudflare's <a href="https://github.com/cloudflare/vibesdk">VibeSDK</a>, this starter kit integrates with Workers for Platforms to handle the deployment of AI-generated projects at scale.</li>
</ul>
<p>To get started, go to <strong>Workers for Platforms</strong> under <strong>Compute &amp; AI</strong> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>


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


<h2 id="r2-sql-now-supports-aggregations-and-schema-discovery"><a href="/changelog/post/2025-12-12-aggregation-support-and-more/">R2 SQL now supports aggregations and schema discovery</a></h2>
<p><em>2025-12-12</em></p>
<p>R2 SQL now supports aggregation functions, <code>GROUP BY</code>, <code>HAVING</code>, along with schema discovery commands to make it easy to explore your data catalog.</p>
<h4 id="2025-12-12-aggregation-support-and-more-aggregation-functions">Aggregation Functions</h4>
<p>You can now perform aggregations on Apache Iceberg tables in <a href="/r2-data-catalog/">R2 Data Catalog</a> using standard SQL functions including <code>COUNT(*)</code>, <code>SUM()</code>, <code>AVG()</code>, <code>MIN()</code>, and <code>MAX()</code>. Combine these with <code>GROUP BY</code> to analyze data across dimensions, and use <code>HAVING</code> to filter aggregated results.</p>
<pre tabindex="0"><code class="language-sql">&#45;- Calculate average transaction amounts by department&#10;SELECT department, COUNT(*), AVG(total_amount)&#10;FROM my_namespace.sales_data&#10;WHERE region = &#x27;North&#x27;&#10;GROUP BY department&#10;HAVING COUNT(*) &gt; 50&#10;ORDER BY AVG(total_amount) DESC&#10;</code></pre>
<pre tabindex="0"><code class="language-sql">&#45;- Find high-value departments&#10;SELECT department, SUM(total_amount)&#10;FROM my_namespace.sales_data&#10;GROUP BY department&#10;HAVING SUM(total_amount) &gt; 50000&#10;</code></pre>
<h4 id="2025-12-12-aggregation-support-and-more-schema-discovery">Schema Discovery</h4>
<p>New metadata commands make it easy to explore your data catalog and understand table structures:</p>
<ul>
<li><code>SHOW DATABASES</code> or <code>SHOW NAMESPACES</code> - List all available namespaces</li>
<li><code>SHOW TABLES IN namespace_name</code> - List tables within a namespace</li>
<li><code>DESCRIBE namespace_name.table_name</code> - View table schema and column types</li>
</ul>
<pre tabindex="0"><code class="language-bash">❯ npx wrangler r2 sql query &quot;{ACCOUNT_ID}_{BUCKET_NAME}&quot; &quot;DESCRIBE default.sales_data;&quot;&#10;&#10; ⛅️ wrangler 4.54.0&#10;─────────────────────────────────────────────&#10;&#10;┌──────────────────┬────────────────┬──────────┬─────────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────┐&#10;│ column_name      │ type           │ required │ initial_default │ write_default │ doc                                                                                               │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_id          │ BIGINT         │ false    │                 │               │ Unique identifier for each sales transaction                                                      │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_timestamp   │ TIMESTAMPTZ    │ false    │                 │               │ Exact date and time when the sale occurred (used for partitioning)                                │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ department       │ TEXT           │ false    │                 │               │ Product department (8 categories: Electronics, Beauty, Home, Toys, Sports, Food, Clothing, Books) │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ category         │ TEXT           │ false    │                 │               │ Product category grouping (4 categories: Premium, Standard, Budget, Clearance)                    │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ region           │ TEXT           │ false    │                 │               │ Geographic sales region (5 regions: North, South, East, West, Central)                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ product_id       │ INT            │ false    │                 │               │ Unique identifier for the product sold                                                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ quantity         │ INT            │ false    │                 │               │ Number of units sold in this transaction (range: 1-50)                                            │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ unit_price       │ DECIMAL(10, 2) │ false    │                 │               │ Price per unit in dollars (range: $5.00-$500.00)                                                  │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ total_amount     │ DECIMAL(10, 2) │ false    │                 │               │ Total sale amount before tax (quantity × unit_price with discounts applied)                       │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ discount_percent │ INT            │ false    │                 │               │ Discount percentage applied to this sale (0-50%)                                                  │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ tax_amount       │ DECIMAL(10, 2) │ false    │                 │               │ Tax amount collected on this sale                                                                 │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ profit_margin    │ DECIMAL(10, 2) │ false    │                 │               │ Profit margin on this sale as a decimal percentage                                                │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ customer_id      │ INT            │ false    │                 │               │ Unique identifier for the customer who made the purchase                                          │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ is_online_sale   │ BOOLEAN        │ false    │                 │               │ Boolean flag indicating if sale was made online (true) or in-store (false)                        │&#10;├──────────────────┼────────────────┼──────────┼─────────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────┤&#10;│ sale_date        │ DATE           │ false    │                 │               │ Calendar date of the sale (extracted from sale_timestamp)                                         │&#10;└──────────────────┴────────────────┴──────────┴─────────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────┘&#10;Read 0 B across 0 files from R2&#10;On average, 0 B / s&#10;</code></pre>
<p>To learn more about the new aggregation capabilities and schema discovery commands, check out the <a href="/r2-sql/sql-reference/">SQL reference</a>. If you're new to R2 SQL, visit our <a href="/r2-sql/get-started/">getting started guide</a> to begin querying your data.</p>


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


<h2 id="terraform-v5-14-0-now-available"><a href="/changelog/post/2025-12-05-terraform-v5.14.0-provider/">Terraform v5.14.0 now available</a></h2>
<p><em>2025-12-05</em></p>
<p>Earlier this year, we announced the launch of the new Terraform v5 Provider. We are aware of the high number of issues reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> to ensure its stability and reliability, including the v5.14 release. We have also pivoted from an <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">issue-to-issue approach to a resource-per-resource approach</a> - we will be focusing on specific resources to not only stabilize the resource but also ensure it is migration-friendly for those migrating from v4 to v5.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and help us build products that reflect your needs.</p>
<p>This release includes bug fixes, the stabilization of even more popular resources, and more.</p>
<h4 id="2025-12-05-terraform-v5.14.0-provider-deprecation-notice">Deprecation notice</h4>
<p>Resource affected: <code>api_shield_discovery_operation</code></p>
<p>Cloudflare continuously discovers and updates API endpoints and web assets of your web applications. To improve the maintainability of these dynamic resources, we are working on reducing the need to actively engage with discovered operations.</p>
<p>The corresponding public API endpoint of <a href="https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/">discovered operations</a> is not affected and will continue to be supported.</p>
<h4 id="2025-12-05-terraform-v5.14.0-provider-features">Features</h4>
<ul>
<li><strong>pages_project</strong>: Add v4 -&gt; v5 migration tests (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/pull/6506">#6506</a>)</li>
</ul>
<h4 id="2025-12-05-terraform-v5.14.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>account_members</strong>: Makes member policies a set (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6488">#6488</a>)</li>
<li><strong>pages_project</strong>: Ensures non empty refresh plans (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6515">#6515</a>)</li>
<li><strong>R2</strong>: Improves sweeper (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6512">#6512</a>)</li>
<li><strong>workers_kv</strong>: Ignores value import state for verify (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6521">#6521</a>)</li>
<li><strong>workers_script</strong>: No longer treats the migrations attribute as WriteOnly (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6489">#6489</a>)</li>
<li><strong>workers_script</strong>: Resolves resource drift when worker has unmanaged secret (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6504">#6504</a>)</li>
<li><strong>zero_trust_device_posture_rule</strong>: Preserves input.version and other fields (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6500">#6500</a>) and (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6503">#6503</a>)</li>
<li><strong>zero_trust_dlp_custom_profile</strong>: Adds sweepers for <code>dlp_custom_profile</code></li>
<li><strong>zone_subscription|account_subscription</strong>: Adds <code>partners_ent</code> as valid enum for <code>rate_plan.id</code> (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6505">#6505</a>)</li>
<li><strong>zone</strong>: Ensures datasource model schema parity (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6487">#6487</a>)</li>
<li><strong>subscription</strong>: Updates import signature to accept account_id/subscription_id to import account subscription (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6510">#6510</a>)</li>
</ul>
<h4 id="2025-12-05-terraform-v5.14.0-provider-upgrade-to-newer-version">Upgrade to newer version</h4>
We suggest waiting to migrate to v5 while we work on stabilization. This helps with avoiding any blocking issues while the Terraform resources are actively being [stabilized](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237). We will be releasing a new migration tool in March 2026 to help support v4 to v5 transitions for our most popular resources.
<h4 id="2025-12-05-terraform-v5.14.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](https://developers.cloudflare.com/terraform/)


<h2 id="connect-to-remote-databases-during-local-development-with-wrangler-dev"><a href="/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/">Connect to remote databases during local development with wrangler dev</a></h2>
<p><em>2025-12-04</em></p>
<p>You can now connect directly to remote databases and databases requiring TLS with <code>wrangler dev</code>.
This lets you run your Worker code locally while connecting to remote databases, without needing to use <code>wrangler dev --remote</code>.</p>
<p>The <code>localConnectionString</code> field and <code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code> environment variable can be used to configure the connection string used by <code>wrangler dev</code>.</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;  &quot;hyperdrive&quot;: [&#10;    {&#10;      &quot;binding&quot;: &quot;HYPERDRIVE&quot;,&#10;      &quot;id&quot;: &quot;your-hyperdrive-id&quot;,&#10;      &quot;localConnectionString&quot;: &quot;postgres://user:password@remote-host.example.com:5432/database?sslmode=require&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/local-development/">local development with Hyperdrive</a>.</p>


<h2 id="one-click-access-protection-for-workers-now-creates-reusable-cloudflare-access-policies"><a href="/changelog/post/2025-12-03-reusable-access-policies/">One-click Access protection for Workers now creates reusable Cloudflare Access policies</a></h2>
<p><em>2025-12-04</em></p>
<p>Workers applications now use reusable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access policies</a> to reduce duplication and simplify access management across multiple Workers.</p>
<p>Previously, enabling Cloudflare Access on a Worker created per-application policies, unique to each application. Now, we create reusable policies that can be shared across applications:</p>
<ul>
<li>
<p><strong>Preview URLs</strong>: All Workers preview URLs share a single &quot;Cloudflare Workers Preview URLs&quot; policy across your account. This policy is automatically created the first time you enable Access on any preview URL. By sharing a single policy across all preview URLs, you can configure access rules once and have them apply company-wide to all Workers which protect preview URLs. This makes it much easier to manage who can access preview environments without having to update individual policies for each Worker.</p>
</li>
<li>
<p><strong>Production workers.dev URLs</strong>: When enabled, each Worker gets its own reusable policy (named <code>&lt;worker-name&gt; - Production</code>) by default. We recognize production services often have different access requirements and having individual policies here makes it easier to configure service-to-service authentication or protect internal dashboards or applications with specific user groups. Keeping these policies separate gives you the flexibility to configure exactly the right access rules for each production service. When you disable Access on a production Worker, the associated policy is automatically cleaned up if it's not being used by other applications.</p>
</li>
</ul>
<p>This change reduces policy duplication, simplifies cross-company access management for preview environments, and provides the flexibility needed for production services. You can still customize access rules by editing the reusable policies in the Zero Trust dashboard.</p>
<p>To enable Cloudflare Access on your Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Workers &amp; Pages</strong>.</li>
<li>Select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, click <strong>Manage Cloudflare Access</strong> to customize the policy.</li>
</ol>
<p>For more information on configuring Cloudflare Access for Workers, refer to the <a href="/workers/configuration/routing/workers-dev/#manage-access-to-workersdev">Workers Access documentation</a>.</p>


<h2 id="agents-sdk-v0-2-24-with-resumable-streaming-mcp-improvements-and-schedule-fixes"><a href="/changelog/post/2025-11-26-agents-resumable-streaming/">Agents SDK v0.2.24 with resumable streaming, MCP improvements, and schedule fixes</a></h2>
<p><em>2025-11-26</em></p>
<p>The latest release of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings resumable streaming, significant MCP client improvements, and critical fixes for schedules and Durable Object lifecycle management.</p>
<h4 id="2025-11-26-agents-resumable-streaming-resumable-streaming">Resumable streaming</h4>
<p><code>AIChatAgent</code> now supports resumable streaming, allowing clients to reconnect and continue receiving streamed responses without losing data. This is useful for:</p>
<ul>
<li>Long-running AI responses</li>
<li>Users on unreliable networks</li>
<li>Users switching between devices mid-conversation</li>
<li>Background tasks where users navigate away and return</li>
<li>Real-time collaboration where multiple clients need to stay in sync</li>
</ul>
<p>Streams are maintained across page refreshes, broken connections, and syncing across open tabs and devices.</p>
<h4 id="2025-11-26-agents-resumable-streaming-other-improvements">Other improvements</h4>
<ul>
<li>Default JSON schema validator added to MCP client</li>
<li><a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">Schedules</a> can now safely destroy the agent</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-mcp-client-api-improvements">MCP client API improvements</h4>
<p>The <code>MCPClientManager</code> API has been redesigned for better clarity and control:</p>
<ul>
<li><strong>New <code>registerServer()</code> method</strong>: Register MCP servers without immediately connecting</li>
<li><strong>New <code>connectToServer()</code> method</strong>: Establish connections to registered servers</li>
<li><strong>Improved reconnect logic</strong>: <code>restoreConnectionsFromStorage()</code> now properly handles failed connections</li>
</ul>
<pre tabindex="0"><code class="language-ts">// Register a server to Agent&#10;const { id } = await this.mcp.registerServer({&#10;	name: &quot;my-server&quot;,&#10;	url: &quot;https://my-mcp-server.example.com&quot;,&#10;});&#10;&#10;// Connect when ready&#10;await this.mcp.connectToServer(id);&#10;&#10;// Discover tools, prompts and resources&#10;await this.mcp.discoverIfConnected(id);&#10;</code></pre>
<p>The SDK now includes a formalized <code>MCPConnectionState</code> enum with states: <code>idle</code>, <code>connecting</code>, <code>authenticating</code>, <code>connected</code>, <code>discovering</code>, and <code>ready</code>.</p>
<h4 id="2025-11-26-agents-resumable-streaming-enhanced-mcp-discovery">Enhanced MCP discovery</h4>
<p>MCP discovery fetches the available tools, prompts, and resources from an MCP server so your agent knows what capabilities are available. The <code>MCPClientConnection</code> class now includes a dedicated <code>discover()</code> method with improved reliability:</p>
<ul>
<li>Supports cancellation via AbortController</li>
<li>Configurable timeout (default 15s)</li>
<li>Discovery failures now throw errors immediately instead of silently continuing</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-bug-fixes">Bug fixes</h4>
<ul>
<li>Fixed a bug where <a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">schedules</a> meant to fire immediately with this.schedule(0, ...) or <code>this.schedule(new Date(), ...)</code> would not fire</li>
<li>Fixed an issue where schedules that took longer than 30 seconds would occasionally time out</li>
<li>Fixed SSE transport now properly forwards session IDs and request headers</li>
<li>Fixed AI SDK stream events conversion to UIMessageStreamPart</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest&#10;</code></pre>


<h2 id="launching-flux-2-dev-on-workers-ai"><a href="/changelog/post/2025-11-25-flux-2-dev-workers-ai/">Launching FLUX.2 [dev] on Workers AI</a></h2>
<p><em>2025-11-25</em></p>
<p>We've partnered with Black Forest Labs (BFL) to bring their latest FLUX.2 [dev] model to Workers AI! This model excels in generating high-fidelity images with physical world grounding, multi-language support, and digital asset creation. You can also create specific super images with granular controls like JSON prompting.</p>
<p>Read the <a href="https://bfl.ai/flux2">BFL blog</a> to learn more about the model itself. Read our <a href="https://blog.cloudflare.com/flux-2-workers-ai">Cloudflare blog</a> to see the model in action, or try it out yourself on our <a href="https://multi-modal.ai.cloudflare.com/">multi modal playground</a>.</p>
<p>Pricing documentation is available on the <a href="/workers-ai/models/flux-2-dev/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>. Note, we expect to drop pricing in the next few days after iterating on the model performance.</p>
<h4 id="2025-11-25-flux-2-dev-workers-ai-workers-ai-platform-specifics">Workers AI Platform specifics</h4>
<p>The model hosted on Workers AI is able to support up to 4 image inputs (512x512 per input image). Note, this image model is one of the most powerful in the catalog and is expected to be slower than the other image models we currently support. One catch to look out for is that this model takes multipart form data inputs, even if you just have a prompt.</p>
<p>With the REST API, the multipart form data input looks like this:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url &#x27;https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev&#x27; \&#10;  &#45;-header &#x27;Authorization: Bearer {TOKEN}&#x27; \&#10;  &#45;-header &#x27;Content-Type: multipart/form-data&#x27; \&#10;  &#45;-form &#x27;prompt=a sunset at the alps&#x27; \&#10;  &#45;-form steps=25&#10;  &#45;-form width=1024&#10;  &#45;-form height=1024&#10;</code></pre>
<p>With the Workers AI binding, you can use it as such:</p>
<pre tabindex="0"><code class="language-javascript">&#10;const form = new FormData();&#10;form.append(&#x27;prompt&#x27;, &#x27;a sunset with a dog&#x27;);&#10;form.append(&#x27;width&#x27;, &#x27;1024&#x27;);&#10;form.append(&#x27;height&#x27;, &#x27;1024&#x27;);&#10;&#10;//this dummy request is temporary hack&#10;//we&#x27;re pushing a change to address this soon&#10;const formRequest = new Request(&#x27;http://dummy&#x27;, {&#10;  method: &#x27;POST&#x27;,&#10;  body: form&#10;});&#10;const formStream = formRequest.body;&#10;const formContentType = formRequest.headers.get(&#x27;content-type&#x27;) || &#x27;multipart/form-data&#x27;;&#10;&#10;const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {&#10;  multipart: {&#10;    body: formStream,&#10;    contentType: formContentType&#10;  }&#10;});&#10;</code></pre>
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
<li><code>steps</code> (integer) - Number of inference steps. Higher values may improve quality but increase generation time</li>
<li><code>guidance</code> (float) - Guidance scale for generation. Higher values follow the prompt more closely</li>
<li><code>width</code> (integer) - Width of the image, default <code>1024</code> Range: 256-1920</li>
<li><code>height</code> (integer) - Height of the image, default <code>768</code> Range: 256-1920</li>
<li><code>seed</code> (integer) - Seed for reproducibility</li>
</ul>
</details>
<pre tabindex="0"><code>&#10;&#35;# Multi-Reference Images&#10;&#10;The FLUX.2 model is great at generating images based on reference images. You can use this feature to apply the style of one image to another, add a new character to an image, or iterate on past generate images. You would use it with the same multipart form data structure, with the input images in binary.&#10;&#10;For the prompt, you can reference the images based on the index, like `take the subject of image 1 and style it like image 0` or even use natural language like `place the dog beside the woman`.&#10;&#10;Note: you have to name the input parameter as `input_image_0`, `input_image_1`, `input_image_2` for it to work correctly. All input images must be smaller than 512x512.&#10;</code></pre>
<p>curl --request POST <br />
--url '<a href="https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT%7D/ai/run/@cf/black-forest-labs/flux-2-dev">https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/ai/run/@cf/black-forest-labs/flux-2-dev</a>' <br />
--header 'Authorization: Bearer {TOKEN}' <br />
--header 'Content-Type: multipart/form-data' <br />
--form 'prompt=take the subject of image 1 and style it like image 0' <br />
--form input_image_0=@/Users/johndoe/Desktop/icedoutkeanu.png <br />
--form input_image_1=@/Users/johndoe/Desktop/me.png <br />
--form steps=25
--form width=1024
--form height=1024</p>
<pre tabindex="0"><code>Through Workers AI Binding:&#10;</code></pre>
<p>//helper function to convert ReadableStream to Blob
async function streamToBlob(stream: ReadableStream, contentType: string): Promise<Blob> {
const reader = stream.getReader();
const chunks = [];</p>
<p>while (true) {
const { done, value } = await reader.read();
if (done) break;
chunks.push(value);
}</p>
<p>return new Blob(chunks, { type: contentType });
}</p>
<p>const image0 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const image1 = await fetch(&quot;<a href="http://image-url">http://image-url</a>&quot;);
const form = new FormData();</p>
<p>const image_blob0 = await streamToBlob(image0.body, &quot;image/png&quot;);
const image_blob1 = await streamToBlob(image1.body, &quot;image/png&quot;);
form.append('input_image_0', image_blob0)
form.append('input_image_1', image_blob1)
form.append('prompt', 'take the subject of image 1and style it like image 0')</p>
<p>//this dummy request is temporary hack
//we're pushing a change to address this soon
const formRequest = new Request('<a href="http://dummy">http://dummy</a>', {
method: 'POST',
body: form
});
const formStream = formRequest.body;
const formContentType = formRequest.headers.get('content-type') || 'multipart/form-data';</p>
<p>const resp = await env.AI.run(&quot;@cf/black-forest-labs/flux-2-dev&quot;, {
multipart: {
body: form,
contentType: &quot;multipart/form-data&quot;
}
})</p>
<pre tabindex="0"><code>&#10;&#35;# JSON Prompting&#10;&#10;The model supports prompting in JSON to get more granular control over images. You would pass the JSON as the value of the &#x27;prompt&#x27; field in the multipart form data. See the JSON schema below on the base parameters you can pass to the model.&#10;&#10;&lt;details&gt;&#10;  &lt;summary&gt;JSON Prompting Schema&lt;/summary&gt;&#10;</code></pre>
<p>{
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;scene&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Overall scene setting or location&quot;
},
&quot;subjects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;type&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Type of subject (e.g., desert nomad, blacksmith, DJ, falcon)&quot;
},
&quot;description&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Physical attributes, clothing, accessories&quot;
},
&quot;pose&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Action or stance&quot;
},
&quot;position&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;foreground&quot;, &quot;midground&quot;, &quot;background&quot;],
&quot;description&quot;: &quot;Depth placement in scene&quot;
}
},
&quot;required&quot;: [&quot;type&quot;, &quot;description&quot;, &quot;pose&quot;, &quot;position&quot;]
}
},
&quot;style&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Artistic rendering style (e.g., digital painting, photorealistic, pixel art, noir sci-fi, lifestyle photo, wabi-sabi photo)&quot;
},
&quot;color_palette&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;minItems&quot;: 3,
&quot;maxItems&quot;: 3,
&quot;description&quot;: &quot;Exactly 3 main colors for the scene (e.g., ['navy', 'neon yellow', 'magenta'])&quot;
},
&quot;lighting&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Lighting condition and direction (e.g., fog-filtered sun, moonlight with star glints, dappled sunlight)&quot;
},
&quot;mood&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Emotional atmosphere (e.g., harsh and determined, playful and modern, peaceful and dreamy)&quot;
},
&quot;background&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Background environment details&quot;
},
&quot;composition&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [
&quot;rule of thirds&quot;,
&quot;circular arrangement&quot;,
&quot;framed by foreground&quot;,
&quot;minimalist negative space&quot;,
&quot;S-curve&quot;,
&quot;vanishing point center&quot;,
&quot;dynamic off-center&quot;,
&quot;leading leads&quot;,
&quot;golden spiral&quot;,
&quot;diagonal energy&quot;,
&quot;strong verticals&quot;,
&quot;triangular arrangement&quot;
],
&quot;description&quot;: &quot;Compositional technique&quot;
},
&quot;camera&quot;: {
&quot;type&quot;: &quot;object&quot;,
&quot;properties&quot;: {
&quot;angle&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;eye level&quot;, &quot;low angle&quot;, &quot;slightly low&quot;, &quot;bird's-eye&quot;, &quot;worm's-eye&quot;, &quot;over-the-shoulder&quot;, &quot;isometric&quot;],
&quot;description&quot;: &quot;Camera perspective&quot;
},
&quot;distance&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;close-up&quot;, &quot;medium close-up&quot;, &quot;medium shot&quot;, &quot;medium wide&quot;, &quot;wide shot&quot;, &quot;extreme wide&quot;],
&quot;description&quot;: &quot;Framing distance&quot;
},
&quot;focus&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;deep focus&quot;, &quot;macro focus&quot;, &quot;selective focus&quot;, &quot;sharp on subject&quot;, &quot;soft background&quot;],
&quot;description&quot;: &quot;Focus type&quot;
},
&quot;lens&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;enum&quot;: [&quot;14mm&quot;, &quot;24mm&quot;, &quot;35mm&quot;, &quot;50mm&quot;, &quot;70mm&quot;, &quot;85mm&quot;],
&quot;description&quot;: &quot;Focal length (wide to telephoto)&quot;
},
&quot;f-number&quot;: {
&quot;type&quot;: &quot;string&quot;,
&quot;description&quot;: &quot;Aperture (e.g., f/2.8, the smaller the number the more blurry the background)&quot;
},
&quot;ISO&quot;: {
&quot;type&quot;: &quot;number&quot;,
&quot;description&quot;: &quot;Light sensitivity value (comfortable range between 100 &amp; 6400, lower = less sensitivity)&quot;
}
}
},
&quot;effects&quot;: {
&quot;type&quot;: &quot;array&quot;,
&quot;items&quot;: { &quot;type&quot;: &quot;string&quot; },
&quot;description&quot;: &quot;Post-processing effects (e.g., 'lens flare small', 'subtle film grain', 'soft bloom', 'god rays', 'chromatic aberration mild')&quot;
}
},
&quot;required&quot;: [&quot;scene&quot;, &quot;subjects&quot;]
}</p>
<pre tabindex="0"><code>&lt;/details&gt;&#10;&#10;&#35;# Other features to try&#10;&#10;&#45; The model also supports the most common latin and non-latin character languages&#10;&#45; You can prompt the model with specific hex codes like `#2ECC71`&#10;&#45; Try creating digital assets like landing pages, comic strips, infographics too!&#10;&#10;&#10;</code></pre>
<h4 id="2025-11-25-flux-2-dev-workers-ai-json-prompting">JSON Prompting</h4><h4 id="2025-11-25-flux-2-dev-workers-ai-other-features-to-try">Other features to try</h4>

<h2 id="mount-r2-buckets-in-containers"><a href="/changelog/post/2025-11-21-fuse-support-in-containers/">Mount R2 buckets in Containers</a></h2>
<p><em>2025-11-21</em></p>
<p><a href="/containers/">Containers</a> now support mounting R2 buckets as FUSE (Filesystem in Userspace) volumes, allowing applications to interact with <a href="/r2/">R2</a> using standard filesystem operations.</p>
<p>Common use cases include:</p>
<ul>
<li>Bootstrapping containers with datasets, models, or dependencies for <a href="/sandbox/">sandboxes</a> and <a href="/agents/">agent</a> environments</li>
<li>Persisting user configuration or application state without managing downloads</li>
<li>Accessing large static files without bloating container images or downloading at startup</li>
</ul>
<p>FUSE adapters like <a href="https://github.com/tigrisdata/tigrisfs">tigrisfs</a>, <a href="https://github.com/s3fs-fuse/s3fs-fuse">s3fs</a>, and <a href="https://github.com/GoogleCloudPlatform/gcsfuse">gcsfuse</a> can be installed in your container image and configured to mount buckets at startup.</p>
<pre tabindex="0"><code class="language-dockerfile">FROM alpine:3.20&#10;&#10;&#35; Install FUSE and dependencies&#10;RUN apk update &amp;&amp; \&#10;    apk add --no-cache ca-certificates fuse curl bash&#10;&#10;&#35; Install tigrisfs&#10;RUN ARCH=$(uname -m) &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;x86_64&quot; ]; then ARCH=&quot;amd64&quot;; fi &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;aarch64&quot; ]; then ARCH=&quot;arm64&quot;; fi &amp;&amp; \&#10;    VERSION=$(curl -s https://api.github.com/repos/tigrisdata/tigrisfs/releases/latest | grep -o &#x27;&quot;tag_name&quot;: &quot;[^&quot;]*&#x27; | cut -d&#x27;&quot;&#x27; -f4) &amp;&amp; \&#10;    curl -L &quot;https://github.com/tigrisdata/tigrisfs/releases/download/${VERSION}/tigrisfs_${VERSION#v}_linux_${ARCH}.tar.gz&quot; -o /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    tar -xzf /tmp/tigrisfs.tar.gz -C /usr/local/bin/ &amp;&amp; \&#10;    rm /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    chmod +x /usr/local/bin/tigrisfs&#10;&#10;&#35; Create startup script that mounts bucket&#10;RUN printf &#x27;#!/bin/sh\n\&#10;    set -e\n\&#10;    mkdir -p /mnt/r2\n\&#10;    R2_ENDPOINT=&quot;https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com&quot;\n\&#10;    /usr/local/bin/tigrisfs --endpoint &quot;${R2_ENDPOINT}&quot; -f &quot;${BUCKET_NAME}&quot; /mnt/r2 &amp;\n\&#10;    sleep 3\n\&#10;    ls -lah /mnt/r2\n\&#10;    &#x27; &gt; /startup.sh &amp;&amp; chmod +x /startup.sh&#10;&#10;CMD [&quot;/startup.sh&quot;]&#10;</code></pre>
<p>See the <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a> example for a complete guide on mounting R2 buckets and/or other S3-compatible storage buckets within your containers.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/13/">Previous</a><span>Page 14 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/15/">Next</a></nav>
