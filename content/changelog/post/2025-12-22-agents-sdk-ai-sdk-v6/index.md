---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/
  description: New updates and improvements at Cloudflare.
  full_title: Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support · Changelog
  head_html: <title>Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/#page","headline":"Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-12-22-agents-sdk-ai-sdk-v6/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 22, 2025</time><h2 id="post-title">Agents SDK v0.3.0, workers-ai-provider v3.0.0, and ai-gateway-provider v3.0.0 with AI SDK v6 support</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> v0.3.0 bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v6</a> and introducing the unified tool pattern, dynamic tool approval, and enhanced React hooks with improved tool handling.</p>
<p>This release includes improved streaming and tool support, dynamic tool approval (for &quot;human in the loop&quot; systems), enhanced React hooks with <code>onToolCall</code> callback, improved error handling for streaming responses, and seamless migration from v5 patterns.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable tool execution and approval workflows.</p>
<p>Additionally, we've updated <strong>workers-ai-provider v3.0.0</strong>, the official provider for Cloudflare Workers AI models, and <strong>ai-gateway-provider v3.0.0</strong>, the provider for Cloudflare AI Gateway, to be compatible with AI SDK v6.</p>
<h4 id="agents-sdk-v0-3-0">Agents SDK v0.3.0</h4>
<h4 id="unified-tool-pattern">Unified Tool Pattern</h4>
<p>AI SDK v6 introduces a unified tool pattern where all tools are defined on the server using the <code>tool()</code> function. This replaces the previous client-side <code>AITool</code> pattern.</p>
<h4 id="server-side-tool-definition">Server-Side Tool Definition</h4>
<pre tabindex="0"><code class="language-ts">import { tool } from &quot;ai&quot;;&#10;import { z } from &quot;zod&quot;;&#10;&#10;// Server: Define ALL tools on the server&#10;const tools = {&#10;	// Server-executed tool&#10;	getWeather: tool({&#10;		description: &quot;Get weather for a city&quot;,&#10;		inputSchema: z.object({ city: z.string() }),&#10;		execute: async ({ city }) =&gt; fetchWeather(city)&#10;	}),&#10;&#10;	// Client-executed tool (no execute = client handles via onToolCall)&#10;	getLocation: tool({&#10;		description: &quot;Get user location from browser&quot;,&#10;		inputSchema: z.object({})&#10;		// No execute function&#10;	}),&#10;&#10;	// Tool requiring approval (dynamic based on input)&#10;	processPayment: tool({&#10;		description: &quot;Process a payment&quot;,&#10;		inputSchema: z.object({ amount: z.number() }),&#10;		needsApproval: async ({ amount }) =&gt; amount &gt; 100,&#10;		execute: async ({ amount }) =&gt; charge(amount)&#10;	})&#10;};&#10;</code></pre>
<h4 id="client-side-tool-handling">Client-Side Tool Handling</h4>
<pre tabindex="0"><code class="language-ts">// Client: Handle client-side tools via onToolCall callback&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;const { messages, sendMessage, addToolOutput } = useAgentChat({&#10;	agent,&#10;	onToolCall: async ({ toolCall, addToolOutput }) =&gt; {&#10;		if (toolCall.toolName === &quot;getLocation&quot;) {&#10;			const position = await new Promise((resolve, reject) =&gt; {&#10;				navigator.geolocation.getCurrentPosition(resolve, reject);&#10;			});&#10;			addToolOutput({&#10;				toolCallId: toolCall.toolCallId,&#10;				output: {&#10;					lat: position.coords.latitude,&#10;					lng: position.coords.longitude&#10;				}&#10;			});&#10;		}&#10;	}&#10;});&#10;</code></pre>
<p><strong>Key benefits of the unified tool pattern:</strong></p>
<ul>
<li><strong>Server-defined tools</strong>: All tools are defined in one place on the server</li>
<li><strong>Dynamic approval</strong>: Use <code>needsApproval</code> to conditionally require user confirmation</li>
<li><strong>Cleaner client code</strong>: Use <code>onToolCall</code> callback instead of managing tool configs</li>
<li><strong>Type safety</strong>: Full TypeScript support with proper tool typing</li>
</ul>
<h4 id="useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v6 capabilities.</p>
<pre tabindex="0"><code class="language-ts">// Basic chat setup with onToolCall&#10;const { messages, sendMessage, addToolOutput } = useAgentChat({&#10;	agent,&#10;	onToolCall: async ({ toolCall, addToolOutput }) =&gt; {&#10;		// Handle client-side tool execution&#10;		await addToolOutput({&#10;			toolCallId: toolCall.toolCallId,&#10;			output: { result: &quot;success&quot; }&#10;		});&#10;	}&#10;});&#10;</code></pre>
<h4 id="dynamic-tool-approval">Dynamic Tool Approval</h4>
<p>Use <code>needsApproval</code> on server tools to conditionally require user confirmation:</p>
<pre tabindex="0"><code class="language-ts">const paymentTool = tool({&#10;	description: &quot;Process a payment&quot;,&#10;	inputSchema: z.object({&#10;		amount: z.number(),&#10;		recipient: z.string()&#10;	}),&#10;	needsApproval: async ({ amount }) =&gt; amount &gt; 1000,&#10;	execute: async ({ amount, recipient }) =&gt; {&#10;		return await processPayment(amount, recipient);&#10;	}&#10;});&#10;</code></pre>
<h4 id="tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>The <code>isToolUIPart</code> and <code>getToolName</code> functions now check both static and dynamic tool parts:</p>
<pre tabindex="0"><code class="language-ts">import { isToolUIPart, getToolName } from &quot;ai&quot;;&#10;&#10;const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolOutput({&#10;		toolCallId: part.toolCallId,&#10;		output: &quot;User approved the action&quot;&#10;	});&#10;}&#10;</code></pre>
<p>If you need the v5 behavior (static-only checks), use the new functions:</p>
<pre tabindex="0"><code class="language-ts">import { isStaticToolUIPart, getStaticToolName } from &quot;ai&quot;;&#10;</code></pre>
<h4 id="converttomodelmessages-is-now-async">convertToModelMessages() is now async</h4>
<p>The <code>convertToModelMessages()</code> function is now asynchronous. Update all calls to await the result:</p>
<pre tabindex="0"><code class="language-ts">import { convertToModelMessages } from &quot;ai&quot;;&#10;&#10;const result = streamText({&#10;	messages: await convertToModelMessages(this.messages),&#10;	model: openai(&quot;gpt-4o&quot;)&#10;});&#10;</code></pre>
<h4 id="modelmessage-type">ModelMessage type</h4>
<p>The <code>CoreMessage</code> type has been removed. Use <code>ModelMessage</code> instead:</p>
<pre tabindex="0"><code class="language-ts">import { convertToModelMessages, type ModelMessage } from &quot;ai&quot;;&#10;&#10;const modelMessages: ModelMessage[] = await convertToModelMessages(messages);&#10;</code></pre>
<h4 id="generateobject-mode-option-removed">generateObject mode option removed</h4>
<p>The <code>mode</code> option for <code>generateObject</code> has been removed:</p>
<pre tabindex="0"><code class="language-ts">// Before (v5)&#10;const result = await generateObject({&#10;	mode: &quot;json&quot;,&#10;	model,&#10;	schema,&#10;	prompt&#10;});&#10;&#10;// After (v6)&#10;const result = await generateObject({&#10;	model,&#10;	schema,&#10;	prompt&#10;});&#10;</code></pre>
<h4 id="structured-output-with-generatetext">Structured Output with generateText</h4>
<p>While <code>generateObject</code> and <code>streamObject</code> are still functional, the recommended approach is to use <code>generateText</code>/<code>streamText</code> with the <code>Output.object()</code> helper:</p>
<pre tabindex="0"><code class="language-ts">import { generateText, Output, stepCountIs } from &quot;ai&quot;;&#10;&#10;const { output } = await generateText({&#10;	model: openai(&quot;gpt-4&quot;),&#10;	output: Output.object({&#10;		schema: z.object({ name: z.string() })&#10;	}),&#10;	stopWhen: stepCountIs(2),&#10;	prompt: &quot;Generate a name&quot;&#10;});&#10;</code></pre>
<blockquote>
<p><strong>Note</strong>: When using structured output with <code>generateText</code>, you must configure multiple steps with <code>stopWhen</code> because generating the structured output is itself a step.</p>
</blockquote>
<h4 id="workers-ai-provider-v3-0-0">workers-ai-provider v3.0.0</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v3.0.0 with AI SDK v6 support.</p>
<h4 id="model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre tabindex="0"><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v3.0.0 - enhanced v6 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v6 file handling with automatic conversion:</p>
<pre tabindex="0"><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre tabindex="0"><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages: await convertToModelMessages(messages),&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="ai-gateway-provider-v3-0-0">ai-gateway-provider v3.0.0</h4>
<p>The ai-gateway-provider v3.0.0 now supports AI SDK v6, enabling you to use Cloudflare AI Gateway with multiple AI providers including Anthropic, Azure, AWS Bedrock, Google Vertex, and Perplexity.</p>
<h4 id="ai-gateway-setup">AI Gateway Setup</h4>
<p>Use Cloudflare AI Gateway to add analytics, caching, and rate limiting to your AI applications:</p>
<pre tabindex="0"><code class="language-ts">import { createAIGateway } from &quot;ai-gateway-provider&quot;;&#10;&#10;// Create AI Gateway provider (v3.0.0 - enhanced v6 internals)&#10;const model = createAIGateway({&#10;	gatewayUrl: &quot;https://gateway.ai.cloudflare.com/v1/your-account-id/gateway&quot;,&#10;	headers: {&#10;		&quot;Authorization&quot;: `Bearer ${env.AI_GATEWAY_TOKEN}`&#10;	}&#10;})({&#10;	provider: &quot;openai&quot;,&#10;	model: &quot;gpt-4o&quot;&#10;});&#10;</code></pre>
<h4 id="migration-from-v5">Migration from v5</h4>
<h4 id="deprecated-apis">Deprecated APIs</h4>
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
<h4 id="breaking-changes-summary">Breaking Changes Summary</h4>
<ol>
<li><strong>Unified Tool Pattern</strong>: All tools must be defined on the server using <code>tool()</code></li>
<li><strong><code>convertToModelMessages()</code> is async</strong>: Add <code>await</code> to all calls</li>
<li><strong><code>CoreMessage</code> removed</strong>: Use <code>ModelMessage</code> instead</li>
<li><strong><code>generateObject</code> mode removed</strong>: Remove <code>mode</code> option</li>
<li><strong><code>isToolUIPart</code> behavior changed</strong>: Now checks both static and dynamic tool parts</li>
</ol>
<h4 id="installation">Installation</h4>
<p>Update your dependencies to use the latest versions:</p>
<pre tabindex="0"><code class="language-bash">npm install agents@^0.3.0 workers-ai-provider@^3.0.0 ai-gateway-provider@^3.0.0 ai@^6.0.0 @ai-sdk/react@^3.0.0 @ai-sdk/openai@^3.0.0&#10;</code></pre>
<h4 id="resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v6.md">Migration Guide</a> - Comprehensive migration documentation from v5 to v6</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-6-0">AI SDK v6 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://vercel.com/blog/ai-sdk-6">AI SDK v6 Announcement</a> - Learn about new features in v6</li>
<li><a href="https://sdk.vercel.ai/docs">AI SDK Documentation</a> - Complete AI SDK reference</li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade from v5 to v6?</li>
<li><strong>Unified tool pattern</strong> - How does the new server-defined tool pattern work for you?</li>
<li><strong>Dynamic tool approval</strong> - Does the <code>needsApproval</code> feature meet your needs?</li>
<li><strong>AI Gateway integration</strong> - How well does the new provider work with your setup?</li>
</ul>
</div></article></div>
