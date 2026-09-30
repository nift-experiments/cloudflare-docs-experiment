<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 10, 2025</time><h2 id="post-title">Agents SDK v0.1.0 and workers-ai-provider v2.0.0 with AI SDK v5 support</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We've shipped a new release for the <a href="https://github.com/cloudflare/agents">Agents SDK</a> bringing full compatibility with <a href="https://ai-sdk.dev/docs/introduction">AI SDK v5</a> and introducing automatic message migration that handles all legacy formats transparently.</p>
<p>This release includes improved streaming and tool support, tool confirmation detection (for &quot;human in the loop&quot; systems), enhanced React hooks with automatic tool resolution, improved error handling for streaming responses, and seamless migration utilities that work behind the scenes.</p>
<p>This makes it ideal for building production AI chat interfaces with Cloudflare Workers AI models, agent workflows, human-in-the-loop systems, or any application requiring reliable message handling across SDK versions — all while maintaining backward compatibility.</p>
<p>Additionally, we've updated workers-ai-provider v2.0.0, the official provider for Cloudflare Workers AI models, to be compatible with AI SDK v5.</p>
<h4 id="useagentchat-options">useAgentChat(options)</h4>
<p>Creates a new chat interface with enhanced v5 capabilities.</p>
<pre><code class="language-ts">// Basic chat setup&#10;const { messages, sendMessage, addToolResult } = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	tools,&#10;});&#10;&#10;// With custom tool confirmation&#10;const chat = useAgentChat({&#10;	agent,&#10;	experimental_automaticToolResolution: true,&#10;	toolsRequiringConfirmation: [&quot;dangerousOperation&quot;],&#10;});&#10;</code></pre>
<h4 id="automatic-tool-resolution">Automatic Tool Resolution</h4>
<p>Tools are automatically categorized based on their configuration:</p>
<pre><code class="language-ts">const tools = {&#10;	// Auto-executes (has execute function)&#10;	getLocalTime: {&#10;		description: &quot;Get current local time&quot;,&#10;		inputSchema: z.object({}),&#10;		execute: async () =&gt; new Date().toLocaleString(),&#10;	},&#10;&#10;	// Requires confirmation (no execute function)&#10;	deleteFile: {&#10;		description: &quot;Delete a file from the system&quot;,&#10;		inputSchema: z.object({&#10;			filename: z.string(),&#10;		}),&#10;	},&#10;&#10;	// Server-executed (no client confirmation)&#10;	analyzeData: {&#10;		description: &quot;Analyze dataset on server&quot;,&#10;		inputSchema: z.object({ data: z.array(z.number()) }),&#10;		serverExecuted: true,&#10;	},&#10;} satisfies Record&lt;string, AITool&gt;;&#10;</code></pre>
<h4 id="message-handling">Message Handling</h4>
<p>Send messages using the new v5 format with parts array:</p>
<pre><code class="language-ts">// Text message&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [{ type: &quot;text&quot;, text: &quot;Hello, assistant!&quot; }],&#10;});&#10;&#10;// Multi-part message with file&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{ type: &quot;image&quot;, image: imageData },&#10;	],&#10;});&#10;</code></pre>
<h4 id="tool-confirmation-detection">Tool Confirmation Detection</h4>
<p>Simplified logic for detecting pending tool confirmations:</p>
<pre><code class="language-ts">const pendingToolCallConfirmation = messages.some((m) =&gt;&#10;	m.parts?.some(&#10;		(part) =&gt; isToolUIPart(part) &amp;&amp; part.state === &quot;input-available&quot;,&#10;	),&#10;);&#10;&#10;// Handle tool confirmation&#10;if (pendingToolCallConfirmation) {&#10;	await addToolResult({&#10;		toolCallId: part.toolCallId,&#10;		tool: getToolName(part),&#10;		output: &quot;User approved the action&quot;,&#10;	});&#10;}&#10;</code></pre>
<h4 id="automatic-message-migration">Automatic Message Migration</h4>
<p>Seamlessly handle legacy message formats without code changes.</p>
<pre><code class="language-ts">// All these formats are automatically converted:&#10;&#10;// Legacy v4 string content&#10;const legacyMessage = {&#10;	role: &quot;user&quot;,&#10;	content: &quot;Hello world&quot;,&#10;};&#10;&#10;// Legacy v4 with tool calls&#10;const legacyWithTools = {&#10;	role: &quot;assistant&quot;,&#10;	content: &quot;&quot;,&#10;	toolInvocations: [&#10;		{&#10;			toolCallId: &quot;123&quot;,&#10;			toolName: &quot;weather&quot;,&#10;			args: { city: &quot;SF&quot; },&#10;			state: &quot;result&quot;,&#10;			result: &quot;Sunny, 72°F&quot;,&#10;		},&#10;	],&#10;};&#10;&#10;// Automatically becomes v5 format:&#10;// {&#10;//   role: &quot;assistant&quot;,&#10;//   parts: [{&#10;//     type: &quot;tool-call&quot;,&#10;//     toolCallId: &quot;123&quot;,&#10;//     toolName: &quot;weather&quot;,&#10;//     args: { city: &quot;SF&quot; },&#10;//     state: &quot;result&quot;,&#10;//     result: &quot;Sunny, 72°F&quot;&#10;//   }]&#10;// }&#10;</code></pre>
<h4 id="tool-definition-updates">Tool Definition Updates</h4>
<p>Migrate tool definitions to use the new <code>inputSchema</code> property.</p>
<pre><code class="language-ts">// Before (AI SDK v4)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		parameters: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;&#10;// After (AI SDK v5)&#10;const tools = {&#10;	weather: {&#10;		description: &quot;Get weather information&quot;,&#10;		inputSchema: z.object({&#10;			city: z.string(),&#10;		}),&#10;		execute: async (args) =&gt; {&#10;			return await getWeather(args.city);&#10;		},&#10;	},&#10;};&#10;</code></pre>
<h4 id="cloudflare-workers-ai-integration">Cloudflare Workers AI Integration</h4>
<p>Seamless integration with Cloudflare Workers AI models through the updated workers-ai-provider v2.0.0.</p>
<h4 id="model-setup-with-workers-ai">Model Setup with Workers AI</h4>
<p>Use Cloudflare Workers AI models directly in your agent workflows:</p>
<pre><code class="language-ts">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import { useAgentChat } from &quot;agents/ai-react&quot;;&#10;&#10;// Create Workers AI model (v2.0.0 - same API, enhanced v5 internals)&#10;const model = createWorkersAI({&#10;	binding: env.AI,&#10;})(&quot;@cf/meta/llama-3.2-3b-instruct&quot;);&#10;</code></pre>
<h4 id="enhanced-file-and-image-support">Enhanced File and Image Support</h4>
<p>Workers AI models now support v5 file handling with automatic conversion:</p>
<pre><code class="language-ts">// Send images and files to Workers AI models&#10;sendMessage({&#10;	role: &quot;user&quot;,&#10;	parts: [&#10;		{ type: &quot;text&quot;, text: &quot;Analyze this image:&quot; },&#10;		{&#10;			type: &quot;file&quot;,&#10;			data: imageBuffer,&#10;			mediaType: &quot;image/jpeg&quot;,&#10;		},&#10;	],&#10;});&#10;&#10;// Workers AI provider automatically converts to proper format&#10;</code></pre>
<h4 id="streaming-with-workers-ai">Streaming with Workers AI</h4>
<p>Enhanced streaming support with automatic warning detection:</p>
<pre><code class="language-ts">// Streaming with Workers AI models&#10;const result = await streamText({&#10;	model: createWorkersAI({ binding: env.AI })(&quot;@cf/meta/llama-3.2-3b-instruct&quot;),&#10;	messages,&#10;	onChunk: (chunk) =&gt; {&#10;		// Enhanced streaming with warning handling&#10;		console.log(chunk);&#10;	},&#10;});&#10;</code></pre>
<h4 id="import-updates">Import Updates</h4>
<p>Update your imports to use the new v5 types:</p>
<pre><code class="language-ts">// Before (AI SDK v4)&#10;import type { Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;ai/react&quot;;&#10;&#10;// After (AI SDK v5)&#10;import type { UIMessage } from &quot;ai&quot;;&#10;// or alias for compatibility&#10;import type { UIMessage as Message } from &quot;ai&quot;;&#10;import { useChat } from &quot;@ai-sdk/react&quot;;&#10;</code></pre>
<h4 id="resources">Resources</h4>
<ul>
<li><a href="https://github.com/cloudflare/agents/blob/main/docs/migration-to-ai-sdk-v5.md">Migration Guide</a> - Comprehensive migration documentation</li>
<li><a href="https://ai-sdk.dev/docs/migration-guides/migration-guide-5-0">AI SDK v5 Documentation</a> - Official AI SDK migration guide</li>
<li><a href="https://github.com/cloudflare/agents-starter/pull/105">An Example PR showing the migration from AI SDK v4 to v5</a></li>
<li><a href="https://github.com/cloudflare/agents/issues">GitHub Issues</a> - Report bugs or request features</li>
</ul>
<h4 id="feedback-welcome">Feedback Welcome</h4>
<p>We'd love your feedback! We're particularly interested in feedback on:</p>
<ul>
<li><strong>Migration experience</strong> - How smooth was the upgrade process?</li>
<li><strong>Tool confirmation workflow</strong> - Does the new automatic detection work as expected?</li>
<li><strong>Message format handling</strong> - Any edge cases with legacy message conversion?</li>
</ul>
</div></article></div>
