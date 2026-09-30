---
cp9:
  canonical: https://developers.cloudflare.com/workflows/get-started/durable-agents/
  description: Build a durable AI agent using Cloudflare Workflows that researches GitHub repositories with automatic retries.
  full_title: Build a Durable AI Agent · Cloudflare Workflows docs
  head_html: <title>Build a Durable AI Agent · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Build a durable AI agent using Cloudflare Workflows that researches GitHub repositories with automatic retries."><link rel="canonical" href="https://developers.cloudflare.com/workflows/get-started/durable-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/get-started/durable-agents/index.md"><meta property="og:title" content="Build a Durable AI Agent · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build a durable AI agent using Cloudflare Workflows that researches GitHub repositories with automatic retries."><meta property="og:url" content="https://developers.cloudflare.com/workflows/get-started/durable-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/get-started/durable-agents/#page","headline":"Build a Durable AI Agent \u00b7 Cloudflare Workflows docs","description":"Build a durable AI agent using Cloudflare Workflows that researches GitHub repositories with automatic retries.","url":"https://developers.cloudflare.com/workflows/get-started/durable-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/get-started/durable-agents/
  schema: 1
---
<p>In this guide, you will build an AI agent that researches GitHub repositories. Give it a task like &quot;Compare open-source LLM projects&quot; and it will:</p>
<ol>
<li>Search GitHub for relevant repositories</li>
<li>Fetch details about each one (stars, forks, activity)</li>
<li>Analyze and compare them</li>
<li>Return a recommendation</li>
</ol>
<p>Each LLM call and tool call becomes a <span class="nb-glossary-tooltip" title="step">step</span> — a self-contained, individually retryable unit of work. If any step fails, Workflows retries it automatically. If the entire Workflow crashes mid-task, it resumes from the last successful step.</p>
<table>
<thead>
<tr>
<th>Challenge</th>
<th>Solution with Workflows</th>
</tr>
</thead>
<tbody>
<tr>
<td>Long-running agent loops</td>
<td>Durable execution that survives any interruption</td>
</tr>
<tr>
<td>Unreliable LLM and API calls</td>
<td>Automatic retry with independent checkpoints</td>
</tr>
<tr>
<td>Waiting for human approval</td>
<td><code>waitForEvent()</code> pauses for hours or days</td>
</tr>
<tr>
<td>Polling for job completion</td>
<td><code>step.sleep()</code> between checks without consuming resources</td>
</tr>
</tbody>
</table>
<p>This guide uses the <a href="/agents/">Agents SDK</a> with Workflows for real-time progress updates and the Anthropic SDK for LLM calls. The same patterns apply to any LLM SDK (OpenAI, Google AI, Mistral, etc.).</p>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the steps and pull down the complete agent, utilizing <a href="/ai-gateway">AI Gateway</a>, run the following command:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest -- --template cloudflare/docs-examples/workflows/durableAgent&#10;</code></pre>
<p>Use this option if you are familiar with Cloudflare Workflows or want to explore the code first.</p>
<p>Follow the steps below to learn how to build a durable AI agent from scratch.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17514.md")
</div></details>
<p>You will also need an <a href="https://platform.claude.com/settings/keys">Anthropic API key</a> for LLM calls. New accounts include free credits.</p>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17515.md")
</div>
<h2 id="2-define-your-tools"><ol start="2">
<li>Define your tools</li>
</ol></h2>
<p>Tools are functions the LLM can call to interact with external systems. You define the schema (what inputs the tool accepts) and the implementation (what it does). The LLM decides when to use each tool based on the task.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17516.md")
</div>
<p>These tools complement each other: <code>search_repos</code> finds repositories, and <code>get_repo</code> fetches details about specific ones.</p>
<h2 id="3-write-your-workflow"><ol start="3">
<li>Write your Workflow</li>
</ol></h2>
<p>The <code>AgentWorkflow</code> class from the Agents SDK extends Cloudflare Workflows with bidirectional Agent communication. Your Workflow can report progress, broadcast to WebSocket clients, and call Agent methods via RPC.</p>
<ul>
<li>The <a href="/workflows/build/workers-api/#step"><code>step</code></a> object provides methods to define durable steps.</li>
<li><code>step.do(name, callback)</code> executes code and persists the result. If the Workflow is interrupted, it resumes from the last successful step.</li>
<li><code>this.reportProgress()</code> sends progress updates to the Agent (non-durable).</li>
<li><code>this.broadcastToClients()</code> sends messages to all connected WebSocket clients (non-durable).</li>
</ul>
<p>For a gentler introduction, refer to <a href="/workflows/get-started/guide/">Build your first Workflow</a>.</p>
<p>Create <code>src/workflow.ts</code>:</p>
<pre tabindex="0"><code class="language-ts">import { AgentWorkflow } from &quot;agents/workflows&quot;;&#10;import type { AgentWorkflowEvent, AgentWorkflowStep } from &quot;agents/workflows&quot;;&#10;import Anthropic from &quot;@anthropic-ai/sdk&quot;;&#10;import {&#10;	tools,&#10;	searchReposTool,&#10;	getRepoTool,&#10;	type SearchReposInput,&#10;	type GetRepoInput,&#10;} from &quot;./tools&quot;;&#10;import type { ResearchAgent } from &quot;./agent&quot;;&#10;&#10;type Params = { task: string };&#10;&#10;export class ResearchWorkflow extends AgentWorkflow&lt;ResearchAgent, Params&gt; {&#10;	async run(event: AgentWorkflowEvent&lt;Params&gt;, step: AgentWorkflowStep) {&#10;		const client = new Anthropic({ apiKey: this.env.ANTHROPIC_API_KEY });&#10;&#10;		const messages: Anthropic.MessageParam[] = [&#10;			{ role: &quot;user&quot;, content: event.payload.task },&#10;		];&#10;&#10;		const toolDefinitions = tools.map(({ run, ...rest }) =&gt; rest);&#10;&#10;		// Durable agent loop - each turn is checkpointed&#10;		for (let turn = 0; turn &lt; 10; turn++) {&#10;			// Report progress to Agent and connected clients&#10;			await this.reportProgress({&#10;				step: `llm-turn-${turn}`,&#10;				status: &quot;running&quot;,&#10;				percent: turn / 10,&#10;				message: `Processing turn ${turn + 1}...`,&#10;			});&#10;&#10;			const response = (await step.do(&#10;				`llm-turn-${turn}`,&#10;				{ retries: { limit: 3, delay: &quot;10 seconds&quot;, backoff: &quot;exponential&quot; } },&#10;				async () =&gt; {&#10;					const msg = await client.messages.create({&#10;						model: &quot;claude-sonnet-4-5-20250929&quot;,&#10;						max_tokens: 4096,&#10;						tools: toolDefinitions,&#10;						messages,&#10;					});&#10;					// Serialize for Workflow state&#10;					return JSON.parse(JSON.stringify(msg));&#10;				},&#10;			)) as Anthropic.Message;&#10;&#10;			if (!response || !response.content) continue;&#10;&#10;			messages.push({ role: &quot;assistant&quot;, content: response.content });&#10;&#10;			if (response.stop_reason === &quot;end_turn&quot;) {&#10;				const textBlock = response.content.find(&#10;					(b): b is Anthropic.TextBlock =&gt; b.type === &quot;text&quot;,&#10;				);&#10;				const result = {&#10;					status: &quot;complete&quot;,&#10;					turns: turn + 1,&#10;					result: textBlock?.text ?? null,&#10;				};&#10;&#10;				// Report completion (durable)&#10;				await step.reportComplete(result);&#10;				return result;&#10;			}&#10;&#10;			const toolResults: Anthropic.ToolResultBlockParam[] = [];&#10;&#10;			for (const block of response.content) {&#10;				if (block.type !== &quot;tool_use&quot;) continue;&#10;&#10;				// Broadcast tool execution to clients&#10;				this.broadcastToClients({&#10;					type: &quot;tool_call&quot;,&#10;					tool: block.name,&#10;					turn,&#10;				});&#10;&#10;				const result = await step.do(&#10;					`tool-${turn}-${block.id}`,&#10;					{ retries: { limit: 2, delay: &quot;5 seconds&quot; } },&#10;					async () =&gt; {&#10;						switch (block.name) {&#10;							case &quot;search_repos&quot;:&#10;								return searchReposTool.run(block.input as SearchReposInput);&#10;							case &quot;get_repo&quot;:&#10;								return getRepoTool.run(block.input as GetRepoInput);&#10;							default:&#10;								return `Unknown tool: ${block.name}`;&#10;						}&#10;					},&#10;				);&#10;&#10;				toolResults.push({&#10;					type: &quot;tool_result&quot;,&#10;					tool_use_id: block.id,&#10;					content: result,&#10;				});&#10;			}&#10;&#10;			messages.push({ role: &quot;user&quot;, content: toolResults });&#10;		}&#10;&#10;		return { status: &quot;max_turns_reached&quot;, turns: 10 };&#10;	}&#10;}&#10;</code></pre>
<details class="nb-details"><summary>Why separate steps for LLM and tools?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17517.md")
</div></details>
<h2 id="4-write-your-agent"><ol start="4">
<li>Write your Agent</li>
</ol></h2>
<p>The Agent handles HTTP requests, WebSocket connections, and Workflow lifecycle events. It triggers a workflow instance <code>runWorkflow()</code> and receives progress updates via callbacks.</p>
<p>Create <code>src/agent.ts</code>:</p>
<pre tabindex="0"><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;&#10;type State = {&#10;	currentWorkflow?: string;&#10;	status?: string;&#10;};&#10;&#10;export class ResearchAgent extends Agent&lt;Env, State&gt; {&#10;	initialState: State = {};&#10;&#10;	// Start a research task - called via HTTP or WebSocket&#10;	async startResearch(task: string) {&#10;		const instanceId = await this.runWorkflow(&quot;RESEARCH_WORKFLOW&quot;, { task });&#10;		this.setState({&#10;			...this.state,&#10;			currentWorkflow: instanceId,&#10;			status: &quot;running&quot;,&#10;		});&#10;		return { instanceId };&#10;	}&#10;&#10;	// Get status of a workflow&#10;	async getResearchStatus(instanceId: string) {&#10;		return this.getWorkflow(instanceId);&#10;	}&#10;&#10;	// Called when workflow reports progress&#10;	async onWorkflowProgress(&#10;		workflowName: string,&#10;		instanceId: string,&#10;		progress: unknown,&#10;	) {&#10;		// Broadcast to all connected WebSocket clients&#10;		this.broadcast(JSON.stringify({ type: &quot;progress&quot;, instanceId, progress }));&#10;	}&#10;&#10;	// Called when workflow completes&#10;	async onWorkflowComplete(&#10;		workflowName: string,&#10;		instanceId: string,&#10;		result?: unknown,&#10;	) {&#10;		this.setState({ ...this.state, status: &quot;complete&quot; });&#10;		this.broadcast(JSON.stringify({ type: &quot;complete&quot;, instanceId, result }));&#10;	}&#10;&#10;	// Called when workflow errors&#10;	async onWorkflowError(&#10;		workflowName: string,&#10;		instanceId: string,&#10;		error: string,&#10;	) {&#10;		this.setState({ ...this.state, status: &quot;error&quot; });&#10;		this.broadcast(JSON.stringify({ type: &quot;error&quot;, instanceId, error }));&#10;	}&#10;}&#10;</code></pre>
<h2 id="5-configure-your-project"><ol start="5">
<li>Configure your project</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17519.md")
</div>
<h2 id="6-write-your-api"><ol start="6">
<li>Write your API</li>
</ol></h2>
<p>The Worker routes requests to the Agent, which manages workflow lifecycle. Use <code>routeAgentRequest()</code> for WebSocket connections and <code>getAgentByName()</code> for server-side RPC calls.</p>
<p>Replace <code>src/index.ts</code>:</p>
<pre tabindex="0"><code class="language-ts">import { getAgentByName, routeAgentRequest } from &quot;agents&quot;;&#10;&#10;export { ResearchAgent } from &quot;./agent&quot;;&#10;export { ResearchWorkflow } from &quot;./workflow&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const url = new URL(request.url);&#10;&#10;		// Route WebSocket connections to /agents/research-agent/{name}&#10;		const agentResponse = await routeAgentRequest(request, env);&#10;		if (agentResponse) return agentResponse;&#10;&#10;		// HTTP API for starting research tasks&#10;		if (request.method === &quot;POST&quot; &amp;&amp; url.pathname === &quot;/research&quot;) {&#10;			const { task, agentId } = await request.json&lt;{&#10;				task: string;&#10;				agentId?: string;&#10;			}&gt;();&#10;&#10;			// Get agent instance by name (creates if doesn&#x27;t exist)&#10;			const agent = await getAgentByName(&#10;				env.ResearchAgent,&#10;				agentId ?? &quot;default&quot;,&#10;			);&#10;&#10;			// Start the research workflow via RPC&#10;			const result = await agent.startResearch(task);&#10;			return Response.json(result);&#10;		}&#10;&#10;		// Check workflow status&#10;		if (url.pathname === &quot;/status&quot;) {&#10;			const instanceId = url.searchParams.get(&quot;instanceId&quot;);&#10;			const agentId = url.searchParams.get(&quot;agentId&quot;) ?? &quot;default&quot;;&#10;&#10;			if (!instanceId) {&#10;				return Response.json({ error: &quot;instanceId required&quot; }, { status: 400 });&#10;			}&#10;&#10;			const agent = await getAgentByName(env.ResearchAgent, agentId);&#10;			const status = await agent.getResearchStatus(instanceId);&#10;&#10;			return Response.json(status);&#10;		}&#10;&#10;		return new Response(&quot;POST /research with { task } to start&quot;, {&#10;			status: 400,&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="7-develop-locally"><ol start="7">
<li>Develop locally</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17520.md")
</div>
<p>The agent will search for repositories, fetch details, and return a comparison. Progress updates are broadcast to any connected WebSocket clients.</p>
<h2 id="8-deploy"><ol start="8">
<li>Deploy</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17521.md")
</div>
<h2 id="real-time-client-integration">Real-time client integration</h2>
<p>Connect to your Agent via WebSocket to receive real-time progress updates. The <code>useAgent</code> hook connects to <code>/agents/{agent-name}/{instance-name}</code>:</p>
<pre tabindex="0"><code>/agents/research-agent/default  → ResearchAgent instance &quot;default&quot;&#10;/agents/research-agent/user-123 → ResearchAgent instance &quot;user-123&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-tsx">import { useState } from &quot;react&quot;;&#10;import { useAgent } from &quot;agents/react&quot;;&#10;&#10;function ResearchUI({ agentId = &quot;default&quot; }) {&#10;	const [progress, setProgress] = useState(null);&#10;&#10;	const { state } = useAgent({&#10;		agent: &quot;research-agent&quot;, // Maps to ResearchAgent class&#10;		name: agentId, // Instance name&#10;		onMessage: (message) =&gt; {&#10;			const data = JSON.parse(message.data);&#10;			if (data.type === &quot;progress&quot;) {&#10;				setProgress(data.progress);&#10;			}&#10;		},&#10;	});&#10;&#10;	return (&#10;		&lt;div&gt;&#10;			{progress &amp;&amp; (&#10;				&lt;p&gt;&#10;					{progress.message} ({Math.round(progress.percent * 100)}%)&#10;				&lt;/p&gt;&#10;			)}&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;</code></pre>
<p>Agent class names are automatically converted to kebab-case for URLs (<code>ResearchAgent</code> → <code>research-agent</code>).</p>
<h2 id="learn-more">Learn more</h2>
<div class="nb-card nb-link-card"><h3 id="card-agents-sdk-workflows-agents-runtime-execution-run-workflows"><a href="/agents/runtime/execution/run-workflows/">Agents SDK Workflows</a></h3><p>Complete API reference for AgentWorkflow, lifecycle callbacks, and bidirectional communication.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-events-and-parameters-workflows-build-events-and-parameters"><a href="/workflows/build/events-and-parameters/">Events and parameters</a></h3><p>Pass data to Workflows and pause for external events with waitForEvent.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-sleeping-and-retrying-workflows-build-sleeping-and-retrying"><a href="/workflows/build/sleeping-and-retrying/">Sleeping and retrying</a></h3><p>Configure retry behavior and sleep patterns.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-workers-api-workflows-build-workers-api"><a href="/workflows/build/workers-api/">Workers API</a></h3><p>Explore the full Workflows API for programmatic control.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-agents-sdk-agents"><a href="/agents/">Agents SDK</a></h3><p>For interactive agents with real-time chat and WebSocket connections.</p></div>
