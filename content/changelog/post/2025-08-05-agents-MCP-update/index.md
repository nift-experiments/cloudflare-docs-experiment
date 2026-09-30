<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 5, 2025</time><h2 id="post-title">Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest releases of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings major improvements to MCP transport protocols support and agents connectivity. Key updates include:</p>
<h4 id="mcp-elicitation-support">MCP elicitation support</h4>
<p>MCP servers can now request user input during tool execution, enabling interactive workflows like confirmations, forms, and multi-step processes. This feature uses durable storage to preserve elicitation state even during agent hibernation, ensuring seamless user interactions across agent lifecycle events.</p>
<pre><code class="language-ts">// Request user confirmation via elicitation&#10;const confirmation = await this.elicitInput({&#10;	message: `Are you sure you want to increment the counter by ${amount}?`,&#10;	requestedSchema: {&#10;		type: &quot;object&quot;,&#10;		properties: {&#10;			confirmed: {&#10;				type: &quot;boolean&quot;,&#10;				title: &quot;Confirm increment&quot;,&#10;				description: &quot;Check to confirm the increment&quot;,&#10;			},&#10;		},&#10;		required: [&quot;confirmed&quot;],&#10;	},&#10;});&#10;</code></pre>
<p>Check out our <a href="https://github.com/whoiskatrin/agents/tree/main/examples/mcp-elicitation-demo">demo</a> to see elicitation in action.</p>
<h4 id="http-streamable-transport-for-mcp">HTTP streamable transport for MCP</h4>
<p>MCP now supports HTTP streamable transport which is recommended over SSE. This transport type offers:</p>
<ul>
<li><strong>Better performance</strong>: More efficient data streaming and reduced overhead</li>
<li><strong>Improved reliability</strong>: Enhanced connection stability and error recover- <strong>Automatic fallback</strong>: If streamable transport is not available, it gracefully falls back to SSE</li>
</ul>
<pre><code class="language-ts">export default MyMCP.serve(&quot;/mcp&quot;, {&#10;	binding: &quot;MyMCP&quot;,&#10;});&#10;</code></pre>
<p>The SDK automatically selects the best available transport method, gracefully falling back from streamable-http to SSE when needed.</p>
<h4 id="enhanced-mcp-connectivity">Enhanced MCP connectivity</h4>
<p>Significant improvements to MCP server connections and transport reliability:</p>
<ul>
<li><strong>Auto transport selection</strong>: Automatically determines the best transport method, falling back from streamable-http to SSE as needed</li>
<li><strong>Improved error handling</strong>: Better connection state management and error reporting for MCP servers</li>
<li><strong>Reliable prop updates</strong>: Centralized agent property updates ensure consistency across different contexts</li>
</ul>
<h4 id="lightweight-queue-for-fast-task-deferral">Lightweight .queue for fast task deferral</h4>
<p>You can use <code>.queue()</code> to enqueue background work — ideal for tasks like processing user messages, sending notifications etc.</p>
<pre><code class="language-ts">class MyAgent extends Agent {&#10;	doSomethingExpensive(payload) {&#10;		// a long running process that you want to run in the background&#10;	}&#10;&#10;	queueSomething() {&#10;		await this.queue(&quot;doSomethingExpensive&quot;, somePayload); // this will NOT block further execution, and runs in the background&#10;		await this.queue(&quot;doSomethingExpensive&quot;, someOtherPayload); // the callback will NOT run until the previous callback is complete&#10;		// ... call as many times as you want&#10;	}&#10;}&#10;</code></pre>
<p>Want to try it yourself? Just define a method like processMessage in your agent, and you’re ready to scale.</p>
<h4 id="new-email-adapter">New email adapter</h4>
<p>Want to build an AI agent that can receive and respond to emails automatically? With the new email adapter and onEmail lifecycle method, now you can.</p>
<pre><code class="language-ts">export class EmailAgent extends Agent {&#10;	async onEmail(email: AgentEmail) {&#10;		const raw = await email.getRaw();&#10;		const parsed = await PostalMime.parse(raw);&#10;&#10;		// create a response based on the email contents&#10;		// and then send a reply&#10;&#10;		await this.replyToEmail(email, {&#10;			fromName: &quot;Email Agent&quot;,&#10;			body: `Thanks for your email! You&#x27;ve sent us &quot;${parsed.subject}&quot;. We&#x27;ll process it shortly.`,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>You route incoming mail like this:</p>
<pre><code class="language-ts">export default {&#10;	async email(email, env) {&#10;		await routeAgentEmail(email, env, {&#10;			resolver: createAddressBasedEmailResolver(&quot;EmailAgent&quot;),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>You can find a full example <a href="https://github.com/cloudflare/agents/tree/main/examples/email-agent">here</a>.</p>
<h4 id="automatic-context-wrapping-for-custom-methods">Automatic context wrapping for custom methods</h4>
<p>Custom methods are now automatically wrapped with the agent's context, so calling <code>getCurrentAgent()</code> should work regardless of where in an agent's lifecycle it's called. Previously this would not work on RPC calls, but now just works out of the box.</p>
<pre><code class="language-ts">export class MyAgent extends Agent {&#10;	async suggestReply(message) {&#10;		// getCurrentAgent() now correctly works, even when called inside an RPC method&#10;		const { agent } = getCurrentAgent()!;&#10;		return generateText({&#10;			prompt: `Suggest a reply to: &quot;${message}&quot; from &quot;${agent.name}&quot;`,&#10;			tools: [replyWithEmoji],&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>Try it out and tell us what you build!</p>
</div></article></div>
