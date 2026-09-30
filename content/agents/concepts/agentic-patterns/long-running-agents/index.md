---
cp9:
  canonical: https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/
  description: Build agents that persist for days, weeks, or months — surviving restarts, waking on demand, and managing work that spans far longer than any single request.
  full_title: Long-running agents · Cloudflare Agents docs
  head_html: <title>Long-running agents · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Build agents that persist for days, weeks, or months — surviving restarts, waking on demand, and managing work that spans far longer than any single request."><link rel="canonical" href="https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/index.md"><meta property="og:title" content="Long-running agents · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build agents that persist for days, weeks, or months — surviving restarts, waking on demand, and managing work that spans far longer than any single request."><meta property="og:url" content="https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Agents"><meta name="pcx_tags" content="AI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/#page","headline":"Long-running agents \u00b7 Cloudflare Agents docs","description":"Build agents that persist for days, weeks, or months \u2014 surviving restarts, waking on demand, and managing work that spans far longer than any single request.","url":"https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI"]}</script>
  markdown: true
  noindex: false
  route: /agents/concepts/agentic-patterns/long-running-agents/
  schema: 1
---
<p>Build agents that persist for days, weeks, or months — surviving restarts, waking on demand, and managing work that spans far longer than any single request.</p>
<p>The short version:</p>
<ul>
<li>Agents are durable identities, not always-on processes.</li>
<li>State, SQL data, schedules, and fiber checkpoints survive hibernation and restarts.</li>
<li>In-memory variables, timers, open fetches, and local closures do not survive eviction.</li>
<li>Use <code>keepAlive()</code> for active work measured in minutes, <code>runFiber()</code> when work needs recovery, <code>startFiber()</code> when callers need durable acceptance and status, and Workflows for heavyweight multi-step jobs.</li>
<li>Use sub-agents when one parent coordinates many long-lived child contexts.</li>
</ul>
<h2 id="why-cloudflare-for-long-running-agents">Why Cloudflare for long-running agents</h2>
<p>Agents spend most of their time waiting. Waiting for user input (seconds to days), LLM responses (seconds to minutes), tool results (seconds to hours), human approvals (hours to days), or scheduled wake-ups (minutes to months). On a traditional VM or container, you pay for all that idle time. An agent that is 99% dormant and 1% active still costs you 100% of a server.</p>
<p>Durable Objects invert this model. An agent exists as an addressable entity with persistent state, but consumes zero compute when hibernated. When something happens — an HTTP request, a WebSocket message, a scheduled alarm, an inbound email — the platform wakes the agent, loads its state from SQLite, and hands it the event. The agent does its work, then goes back to sleep.</p>
<p>This is the <a href="https://en.wikipedia.org/wiki/Actor_model">actor model</a>: each agent has an identity, durable state, and wakes on message. You do not manage servers, routing, health checks, or restart logic. The platform handles placement, scaling, and recovery.</p>
<p>The economics follow directly:</p>
<table>
<thead>
<tr>
<th></th>
<th>VMs / Containers</th>
<th>Durable Objects</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Idle cost</strong></td>
<td>Full compute cost, always</td>
<td>Zero (hibernated)</td>
</tr>
<tr>
<td><strong>Scaling</strong></td>
<td>Provision and manage capacity</td>
<td>Automatic, per-agent</td>
</tr>
<tr>
<td><strong>State</strong></td>
<td>External database required</td>
<td>Built-in SQLite</td>
</tr>
<tr>
<td><strong>Recovery</strong></td>
<td>You build it (process managers, health checks)</td>
<td>Platform restarts, state survives</td>
</tr>
<tr>
<td><strong>Identity / routing</strong></td>
<td>You build it (load balancers, sticky sessions)</td>
<td>Built-in (name to agent)</td>
</tr>
<tr>
<td><strong>10,000 agents, each active 1% of the time</strong></td>
<td>10,000 always-on instances</td>
<td>~100 active at any moment</td>
</tr>
</tbody>
</table>
<p>For agents — which are inherently bursty, stateful, and long-lived — this is a natural fit.</p>
<h2 id="the-lifecycle-of-a-long-running-agent">The lifecycle of a long-running agent</h2>
<p>A long-running agent is not a process that runs continuously. It is an entity that <strong>exists</strong> continuously but <strong>runs</strong> intermittently. Understanding the lifecycle is key to building agents that work reliably over long timelines.</p>
<pre tabindex="0"><code class="language-txt">Wake → onStart() → handle events → idle (~2 min) → hibernation&#10;  ▲                                                      │&#10;  └──────────────── alarm or request wakes agent ────────┘&#10;&#10;Eviction (crash / redeploy) can happen at any point.&#10;State persists in SQLite. Agent restarts on next event.&#10;</code></pre>
<h3 id="what-survives">What survives</h3>
<ul>
<li><strong><code>this.state</code></strong> — persisted to SQLite on every <code>setState()</code> call</li>
<li><strong><code>this.sql</code> data</strong> — all SQLite tables you create</li>
<li><strong>Scheduled tasks</strong> — stored in SQLite, trigger alarms to wake the agent</li>
<li><strong>Connection state</strong> — <code>connection.setState()</code> data for each WebSocket client</li>
<li><strong>Fiber checkpoints and ledgers</strong> — <code>stash()</code> data from <code>runFiber()</code> and retained <code>startFiber()</code> status rows</li>
</ul>
<p>Any higher-level abstractions built on SQLite also survive, since they share the same durable storage.</p>
<h3 id="what-does-not-survive">What does not survive</h3>
<ul>
<li><strong>In-memory variables</strong> — class fields not stored via <code>setState()</code> or <code>this.sql</code></li>
<li><strong>Running timers</strong> — <code>setTimeout</code>, <code>setInterval</code> are lost on hibernation/eviction</li>
<li><strong>Open fetch requests</strong> — in-flight HTTP calls are abandoned</li>
<li><strong>Local closures</strong> — callbacks and promise chains are lost</li>
</ul>
<p>The implication: any work that matters must be persisted or recoverable. The SDK provides primitives for this — schedules, fibers, queues — but understanding the boundary between &quot;in-memory&quot; and &quot;durable&quot; is essential.</p>
<h2 id="running-example-a-project-manager-agent">Running example: a project manager agent</h2>
<p>Throughout this doc, we build up a project manager agent that:</p>
<ul>
<li>Lives for the duration of a project (weeks or months)</li>
<li>Tracks tasks, assigns work to sub-agents, and reports progress</li>
<li>Wakes up on schedule to check deadlines and send reminders</li>
<li>Reacts to external events (webhooks from GitHub, emails from team members)</li>
<li>Handles long-running operations (CI pipelines, code reviews, deployments)</li>
<li>Survives any number of restarts and evictions along the way</li>
</ul>
<pre tabindex="0"><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;&#10;type ProjectState = {&#10;	name: string;&#10;	status: &quot;planning&quot; | &quot;active&quot; | &quot;review&quot; | &quot;complete&quot;;&#10;	tasks: Task[];&#10;	plan: Plan | null;&#10;};&#10;&#10;type Task = {&#10;	id: string;&#10;	title: string;&#10;	status: &quot;pending&quot; | &quot;in_progress&quot; | &quot;blocked&quot; | &quot;complete&quot;;&#10;	assignee?: string;&#10;	dueDate?: string;&#10;	completedAt?: number;&#10;	externalJobId?: string;&#10;};&#10;&#10;export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	initialState: ProjectState = {&#10;		name: &quot;&quot;,&#10;		status: &quot;planning&quot;,&#10;		tasks: [],&#10;		plan: null,&#10;	};&#10;}&#10;</code></pre>
<p>The <code>Plan</code> type is introduced in <a href="#planning-as-a-durability-strategy">Planning as a durability strategy</a>. We add capabilities to this agent section by section.</p>
<h2 id="waking-up-how-agents-get-activated">Waking up: how agents get activated</h2>
<p>A hibernated agent can be woken by any of these sources:</p>
<table>
<thead>
<tr>
<th>Wake source</th>
<th>How it works</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>HTTP request</strong></td>
<td>Any request to the agent's URL triggers <code>onRequest()</code></td>
<td>A webhook from GitHub</td>
</tr>
<tr>
<td><strong>WebSocket connection</strong></td>
<td>A client connects, triggering <code>onConnect()</code></td>
<td>A team member opens the dashboard</td>
</tr>
<tr>
<td><strong>RPC call</strong></td>
<td>Another Worker or agent calls a method via <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> or <a href="/agents/runtime/lifecycle/callable-methods/"><code>@callable</code></a></td>
<td>A coordinator agent delegates a task</td>
</tr>
<tr>
<td><strong>Scheduled alarm</strong></td>
<td>A stored schedule fires, triggering your callback</td>
<td>Daily standup reminder at 9am</td>
</tr>
<tr>
<td><strong>Email</strong></td>
<td>An inbound email triggers <code>onEmail()</code></td>
<td>A team member replies to a status email</td>
</tr>
</tbody>
</table>
<p>The pattern extends naturally to any event source that can reach a Worker — anything from telephony webhooks to chat platform bots. An external signal arrives, the platform wakes the agent, and the agent handles it.</p>
<p>The agent does not need to be &quot;started&quot; or &quot;deployed&quot; separately for each wake source — they all route to the same Durable Object instance. The agent's identity (its name) is the routing key.</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async onStart() {&#10;		// Daily deadline check at 9am UTC — idempotent, safe across restarts&#10;		await this.schedule(&#10;			&quot;0 9 * * *&quot;,&#10;			&quot;checkDeadlines&quot;,&#10;			{},&#10;			{&#10;				idempotent: true,&#10;			},&#10;		);&#10;&#10;		// Progress sync every 30 minutes&#10;		await this.scheduleEvery(1800, &quot;syncProgress&quot;);&#10;	}&#10;&#10;	async onRequest(request: Request): Promise&lt;Response&gt; {&#10;		const url = new URL(request.url);&#10;&#10;		if (url.pathname.endsWith(&quot;/github-webhook&quot;)) {&#10;			const event = await request.json();&#10;			await this.handleGitHubEvent(event);&#10;			return new Response(&quot;OK&quot;);&#10;		}&#10;&#10;		return Response.json({&#10;			project: this.state.name,&#10;			status: this.state.status,&#10;		});&#10;	}&#10;&#10;	async checkDeadlines() {&#10;		/* ... find overdue tasks, broadcast alerts ... */&#10;	}&#10;	async syncProgress() {&#10;		/* ... check on sub-agents, update task statuses ... */&#10;	}&#10;}&#10;</code></pre>
<h2 id="staying-alive-during-long-work">Staying alive during long work</h2>
<p>Sometimes an agent needs to do work that takes longer than the idle eviction window (~70–140 seconds). Streaming an LLM response, orchestrating a multi-step tool chain, or waiting on a slow API all risk the agent being evicted mid-flight.</p>
<p><code>keepAlive()</code> prevents this by creating a heartbeat that resets the inactivity timer:</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async generateProjectPlan(goal: string) {&#10;		const result = await this.keepAliveWhile(async () =&gt; {&#10;			const plan = await this.callLLM(`Create a project plan for: ${goal}`);&#10;			const tasks = await this.callLLM(&#10;				`Break this into tasks: ${JSON.stringify(plan)}`,&#10;			);&#10;			return { plan, tasks };&#10;		});&#10;&#10;		this.setState({&#10;			...this.state,&#10;			status: &quot;active&quot;,&#10;			plan: result.plan,&#10;			tasks: result.tasks,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p><code>keepAliveWhile()</code> is the recommended approach — it guarantees the heartbeat is cleaned up when the work finishes (or throws). For manual control, <code>keepAlive()</code> returns a disposer:</p>
<pre tabindex="0"><code class="language-ts">const dispose = await this.keepAlive();&#10;try {&#10;	await longWork();&#10;} finally {&#10;	dispose();&#10;}&#10;</code></pre>
<h3 id="when-keepalive-is-not-enough">When keepAlive is not enough</h3>
<p><code>keepAlive</code> is for work measured in minutes, not hours. For truly long-running operations, use a different strategy:</p>
<table>
<thead>
<tr>
<th>Duration</th>
<th>Strategy</th>
</tr>
</thead>
<tbody>
<tr>
<td>Seconds</td>
<td>Normal request handling</td>
</tr>
<tr>
<td>Minutes</td>
<td><code>keepAlive()</code> / <code>keepAliveWhile()</code></td>
</tr>
<tr>
<td>Minutes</td>
<td><code>startFiber()</code> when retryable acceptance matters</td>
</tr>
<tr>
<td>Minutes to hours</td>
<td><a href="/agents/runtime/execution/run-workflows/">Workflows</a></td>
</tr>
<tr>
<td>Hours to days</td>
<td>Async pattern: start job, hibernate, wake on completion</td>
</tr>
</tbody>
</table>
<h2 id="surviving-crashes-fibers-and-recovery">Surviving crashes: fibers and recovery</h2>
<p>An agent can be evicted at any time — a deploy, a platform restart, or hitting resource limits. If the agent was mid-task, that work is lost unless it was checkpointed.</p>
<p><a href="/agents/runtime/execution/durable-execution/"><code>runFiber()</code></a> provides crash-recoverable execution. It persists a row in SQLite for the duration of the work, and lets you <code>stash()</code> intermediate state. If the agent is evicted, the fiber row survives, and <code>onFiberRecovered()</code> is called on the next activation.</p>
<p>Use <a href="/agents/runtime/execution/durable-execution/#startfiber"><code>startFiber()</code></a> when the important boundary is durable acceptance. It adds an idempotency key, retained status records, inspection, cancellation, and cleanup on top of the same fiber machinery. By default it returns after acceptance; pass <code>waitForCompletion: true</code> when the request should stay open until the accepted job reaches a terminal status. This is a good fit for webhooks where the provider may retry delivery and the agent must avoid starting duplicate visible side effects.</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async executeTask(task: Task) {&#10;		await this.runFiber(`task:${task.id}`, async (ctx) =&gt; {&#10;			const resources = await this.gatherResources(task);&#10;			ctx.stash({ phase: &quot;prepared&quot;, resources, task });&#10;&#10;			const result = await this.runSubAgent(task, resources);&#10;			ctx.stash({ phase: &quot;executed&quot;, result, task });&#10;&#10;			await this.updateTaskStatus(task.id, &quot;complete&quot;, result);&#10;		});&#10;	}&#10;&#10;	async onFiberRecovered(ctx: FiberRecoveryContext) {&#10;		if (!ctx.name.startsWith(&quot;task:&quot;)) return;&#10;		const { phase, task } = ctx.snapshot as { phase: string; task: Task };&#10;&#10;		if (phase === &quot;prepared&quot;) {&#10;			await this.executeTask(task);&#10;		} else if (phase === &quot;executed&quot;) {&#10;			await this.updateTaskStatus(&#10;				task.id,&#10;				&quot;complete&quot;,&#10;				(ctx.snapshot as { result: unknown }).result,&#10;			);&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>The pattern is: <strong>checkpoint before expensive work, recover from the last checkpoint.</strong> This is not automatic replay — you decide what recovery means for your domain.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="testing-recovery-locally">Testing recovery locally</h3>
@markup("md", "content/.markup/bodies/2086.md")
</aside>
<p>For the full API reference — <code>FiberContext</code>, <code>FiberRecoveryContext</code>, concurrent fibers, inline vs fire-and-forget patterns — refer to <a href="/agents/runtime/execution/durable-execution/">Durable Execution</a>.</p>
<h2 id="handling-long-async-operations">Handling long async operations</h2>
<p>The project manager frequently kicks off work that takes far longer than any single activation — a CI pipeline runs for 20 minutes, a design review takes a day, a video asset takes hours to generate. The agent should not stay alive for any of this. Instead, it starts the work, persists the job ID in state, and hibernates. When the result arrives — via a callback, a poll, or a workflow completion — the agent wakes, correlates the result, and moves on.</p>
<h3 id="pattern-webhook-callback">Pattern: webhook callback</h3>
<p>The project manager starts a CI pipeline for a task. The pipeline takes 20 minutes. Rather than holding a connection open, the agent registers its own URL as the callback and goes to sleep:</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async startCIPipeline(task: Task) {&#10;		const response = await fetch(&quot;https://ci.example.com/api/pipelines&quot;, {&#10;			method: &quot;POST&quot;,&#10;			body: JSON.stringify({&#10;				repo: &quot;org/project&quot;,&#10;				branch: &quot;main&quot;,&#10;				callback_url: `${this.url}/ci-callback?taskId=${task.id}`,&#10;			}),&#10;		});&#10;&#10;		const { pipelineId } = await response.json();&#10;		this.updateTask(task.id, {&#10;			status: &quot;in_progress&quot;,&#10;			externalJobId: pipelineId,&#10;		});&#10;	}&#10;&#10;	async onRequest(request: Request): Promise&lt;Response&gt; {&#10;		const url = new URL(request.url);&#10;		if (url.pathname.endsWith(&quot;/ci-callback&quot;)) {&#10;			const taskId = url.searchParams.get(&quot;taskId&quot;);&#10;			const result = await request.json();&#10;			this.updateTask(taskId, {&#10;				status: result.status === &quot;success&quot; ? &quot;complete&quot; : &quot;blocked&quot;,&#10;			});&#10;			return new Response(&quot;OK&quot;);&#10;		}&#10;		// ... other routes&#10;	}&#10;}&#10;</code></pre>
<h3 id="pattern-polling-with-schedule">Pattern: polling with schedule</h3>
<p>Not every external service supports callbacks. When the project manager submits a video asset for generation, it needs to check back periodically until the job completes:</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async startVideoGeneration(task: Task) {&#10;		const response = await fetch(&quot;https://video-api.example.com/generate&quot;, {&#10;			method: &quot;POST&quot;,&#10;			body: JSON.stringify({ prompt: task.title }),&#10;		});&#10;		const { jobId } = await response.json();&#10;		this.updateTask(task.id, { status: &quot;in_progress&quot;, externalJobId: jobId });&#10;		await this.schedule(60, &quot;pollExternalJob&quot;, {&#10;			taskId: task.id,&#10;			jobId,&#10;			attempt: 1,&#10;		});&#10;	}&#10;&#10;	async pollExternalJob(payload: {&#10;		taskId: string;&#10;		jobId: string;&#10;		attempt: number;&#10;	}) {&#10;		const response = await fetch(&#10;			`https://video-api.example.com/status/${payload.jobId}`,&#10;		);&#10;		const status = await response.json();&#10;&#10;		if (status.state === &quot;complete&quot; || status.state === &quot;failed&quot;) {&#10;			this.updateTask(payload.taskId, {&#10;				status: status.state === &quot;complete&quot; ? &quot;complete&quot; : &quot;blocked&quot;,&#10;			});&#10;			return;&#10;		}&#10;&#10;		const nextDelay = Math.min(60 * payload.attempt, 600);&#10;		await this.schedule(nextDelay, &quot;pollExternalJob&quot;, {&#10;			...payload,&#10;			attempt: payload.attempt + 1,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<h3 id="pattern-workflow-delegation">Pattern: workflow delegation</h3>
<p>A production deployment involves multiple steps that must each retry independently — build, test, stage, promote. The project manager should not manage these steps internally; it delegates to a <a href="/agents/runtime/execution/run-workflows/">Workflow</a> that handles retries and step sequencing:</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async startDeployment(task: Task) {&#10;		const instanceId = await this.runWorkflow(&quot;DEPLOY_WORKFLOW&quot;, {&#10;			taskId: task.id,&#10;			environment: &quot;production&quot;,&#10;		});&#10;		this.updateTask(task.id, {&#10;			status: &quot;in_progress&quot;,&#10;			externalJobId: instanceId,&#10;		});&#10;	}&#10;&#10;	async onWorkflowComplete(&#10;		workflowName: string,&#10;		instanceId: string,&#10;		result?: unknown,&#10;	) {&#10;		const task = this.state.tasks.find((t) =&gt; t.externalJobId === instanceId);&#10;		if (task) this.updateTask(task.id, { status: &quot;complete&quot; });&#10;	}&#10;}&#10;</code></pre>
<h2 id="reconstructing-context-after-a-long-wait">Reconstructing context after a long wait</h2>
<p>The CI pipeline finishes 20 minutes later. The webhook wakes the project manager. The task status is updated. But now what? If the agent was using an LLM to orchestrate work — deciding which task to run next, drafting a status report, reasoning about blockers — it needs to pick up that reasoning thread. The original prompt, the in-flight tool call, the chain of thought — all gone from memory.</p>
<p>This is the fundamental challenge of long-running AI agents. Most frameworks assume tool calls complete within the LLM's timeout and do not address this directly.</p>
<p>Three approaches work today:</p>
<p><strong>Replay the full conversation history.</strong> <code>AIChatAgent</code> persists all messages in SQLite. When the result arrives, append it to the history and re-invoke the LLM. This is the simplest approach but re-processes the entire context window.</p>
<p><strong>Stash a continuation summary.</strong> Before hibernating, persist a compact description of what the agent was doing and what to do with the result:</p>
<pre tabindex="0"><code class="language-ts">ctx.stash({&#10;	task: &quot;Waiting for CI results&quot;,&#10;	onSuccess: &quot;Mark task complete, move to next step in plan&quot;,&#10;	onFailure: &quot;Notify team, schedule retry in 1 hour&quot;,&#10;	relevantContext: { taskId, planStep: 3 },&#10;});&#10;</code></pre>
<p>On recovery, use the stash to construct a focused prompt rather than replaying everything.</p>
<p><strong>Use the plan as context.</strong> If the agent has a structured plan, the plan itself provides sufficient context: &quot;I am on step 3 of 7, the step was 'run CI pipeline', the result just arrived.&quot; This is the most robust approach for long-running agents — the plan is both a recovery mechanism and a context reconstruction strategy. Refer to the next section.</p>
<h2 id="planning-as-a-durability-strategy">Planning as a durability strategy</h2>
<p>A structured plan is not just useful for showing progress to users — it is a durability mechanism. An agent with a plan can recover from any interruption by looking at where it left off.</p>
<pre tabindex="0"><code class="language-ts">type Plan = {&#10;	goal: string;&#10;	steps: PlanStep[];&#10;	currentStep: number;&#10;	createdAt: string;&#10;	updatedAt: string;&#10;};&#10;&#10;type PlanStep = {&#10;	id: string;&#10;	description: string;&#10;	status: &quot;pending&quot; | &quot;in_progress&quot; | &quot;complete&quot; | &quot;failed&quot; | &quot;skipped&quot;;&#10;	result?: unknown;&#10;};&#10;&#10;export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async createPlan(goal: string) {&#10;		const steps = await this.keepAliveWhile(async () =&gt; {&#10;			return this.callLLM(`&#10;        Break down this project goal into concrete steps.&#10;        Return a JSON array of { id, description } objects.&#10;        Goal: ${goal}&#10;      `);&#10;		});&#10;&#10;		this.setState({&#10;			...this.state,&#10;			plan: {&#10;				goal,&#10;				steps: steps.map((s: { id: string; description: string }) =&gt; ({&#10;					...s,&#10;					status: &quot;pending&quot; as const,&#10;				})),&#10;				currentStep: 0,&#10;				createdAt: new Date().toISOString(),&#10;				updatedAt: new Date().toISOString(),&#10;			},&#10;		});&#10;&#10;		await this.schedule(0, &quot;executeNextStep&quot;);&#10;	}&#10;&#10;	async executeNextStep() {&#10;		const { plan } = this.state;&#10;		if (!plan || plan.currentStep &gt;= plan.steps.length) {&#10;			this.setState({ ...this.state, status: &quot;complete&quot; });&#10;			return;&#10;		}&#10;&#10;		const step = plan.steps[plan.currentStep];&#10;&#10;		try {&#10;			const result = await this.keepAliveWhile(() =&gt; this.executeStep(step));&#10;&#10;			const updatedSteps = plan.steps.map((s) =&gt;&#10;				s.id === step.id ? { ...s, status: &quot;complete&quot; as const, result } : s,&#10;			);&#10;			this.setState({&#10;				...this.state,&#10;				plan: {&#10;					...plan,&#10;					steps: updatedSteps,&#10;					currentStep: plan.currentStep + 1,&#10;					updatedAt: new Date().toISOString(),&#10;				},&#10;			});&#10;&#10;			await this.schedule(0, &quot;executeNextStep&quot;);&#10;		} catch (error) {&#10;			const updatedSteps = plan.steps.map((s) =&gt;&#10;				s.id === step.id ? { ...s, status: &quot;failed&quot; as const } : s,&#10;			);&#10;			this.setState({&#10;				...this.state,&#10;				plan: {&#10;					...plan,&#10;					steps: updatedSteps,&#10;					updatedAt: new Date().toISOString(),&#10;				},&#10;			});&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>This pattern has several advantages for long-running agents:</p>
<ul>
<li><strong>Recovery is trivial</strong> — on restart, check <code>plan.currentStep</code> and resume</li>
<li><strong>Progress is visible</strong> — clients see which steps are done and what is next</li>
<li><strong>Re-planning is possible</strong> — if a step fails or requirements change, the agent can revise the remaining steps without losing completed work</li>
<li><strong>Human oversight</strong> — the plan is a natural approval checkpoint (&quot;here is what I am going to do — proceed?&quot;)</li>
<li><strong>Context reconstruction</strong> — the plan tells the LLM where it is, what happened, and what to do next, without replaying the full conversation</li>
</ul>
<h2 id="delegating-to-sub-agents">Delegating to sub-agents</h2>
<p>A project manager does not do everything itself. It delegates specialized work to sub-agents — each with their own identity, state, and lifecycle.</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async delegateTask(task: Task) {&#10;		const researcher = await this.subAgent(&#10;			ResearchAgent,&#10;			`research-${task.id}`,&#10;		);&#10;&#10;		const findings = await researcher.research(task.title);&#10;&#10;		this.updateTask(task.id, { status: &quot;complete&quot; });&#10;		return findings;&#10;	}&#10;}&#10;</code></pre>
<p>Sub-agents have their own state, schedules, durable fibers, and lifecycle. They are colocated under the parent, but each child stores its own SQLite data and runs callbacks with the child as <code>this</code>.</p>
<p>Because facets do not have independent alarm slots, the top-level parent owns the physical Durable Object alarm. The Agents SDK records which sub-agent owns each schedule or fiber recovery lease, wakes the parent, and routes the callback back into the child. The parent does not need to stay active while the sub-agent works — it can start the work, hibernate, and be woken by the child-owned schedule or recovery check.</p>
<p>For the full <code>subAgent()</code> API — typed RPC stubs, client routing, access control, storage isolation, and alarm-backed APIs — refer to <a href="/agents/runtime/execution/sub-agents/">Sub-agents</a>. For AI-specific sub-agent streaming (running full LLM turns through a child agent), refer to <a href="/agents/harnesses/think/sub-agents/">Think: Sub-agent RPC</a>.</p>
<h2 id="recovering-interrupted-llm-streams">Recovering interrupted LLM streams</h2>
<p>The patterns above handle the project manager's coordination work — scheduling, delegating, polling. But the project manager also uses an LLM directly: generating plans, summarizing progress, drafting status emails. Those LLM calls stream tokens over a connection that cannot be resumed if the agent is evicted mid-response.</p>
<p>For chat-oriented agents built on <code>AIChatAgent</code> or <code>Think</code>, this is an even sharper problem — the user watches the response stream in real time and sees it stop mid-sentence. Durable recovery wraps every chat turn in a <code>runFiber</code>. This provides automatic <code>keepAlive</code> during streaming and a recovery hook when the agent restarts:</p>
<pre tabindex="0"><code class="language-ts">import { AIChatAgent } from &quot;@cloudflare/ai-chat&quot;;&#10;import type {&#10;	ChatRecoveryContext,&#10;	ChatRecoveryOptions,&#10;} from &quot;@cloudflare/ai-chat&quot;;&#10;&#10;class ProjectChat extends AIChatAgent&lt;Env&gt; {&#10;	override async onChatRecovery(&#10;		ctx: ChatRecoveryContext,&#10;	): Promise&lt;ChatRecoveryOptions&gt; {&#10;		// ctx.partialText    — text generated before eviction&#10;		// ctx.recoveryData   — whatever you stashed via this.stash()&#10;		// ctx.messages        — full conversation history&#10;		// ctx.createdAt       — when the interrupted turn started&#10;		return {};&#10;	}&#10;}&#10;</code></pre>
<p>The right recovery strategy depends on the LLM provider:</p>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Strategy</th>
<th>How it works</th>
<th>Token cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers AI</td>
<td>Continue from partial</td>
<td><code>continueLastTurn()</code> — model continues via assistant prefill</td>
<td>Low</td>
</tr>
<tr>
<td>OpenAI (Responses API)</td>
<td>Retrieve completed response</td>
<td>Stash <code>responseId</code> during streaming, retrieve on recovery</td>
<td>Zero</td>
</tr>
<tr>
<td>Anthropic</td>
<td>Synthetic continuation</td>
<td>Persist partial, send a synthetic user message asking the model to continue</td>
<td>Medium</td>
</tr>
<tr>
<td>Other</td>
<td>Try prefill, fall back to synthetic</td>
<td><code>continueLastTurn()</code> if the provider supports it, synthetic message otherwise</td>
<td>Varies</td>
</tr>
</tbody>
</table>
<p>Use <code>ctx.createdAt</code> to suppress stale recoveries. For example, if a recovered chat turn is older than a few minutes, you may persist the partial answer but skip automatic continuation to avoid surprising the user with an old response.</p>
<p><code>AIChatAgent</code> and <a href="/agents/harnesses/think/"><code>Think</code></a> always use durable recovery. The default path persists partial output and continues or retries the turn when safe. Override <code>onChatRecovery</code> when a provider has a better recovery strategy. Configure <code>chatRecovery = { maxAttempts, terminalMessage, onExhausted }</code> to tune the terminal experience.</p>
<p>If the agent is interrupted before any assistant stream chunks are written, there is no partial assistant message to continue. When the latest persisted message is still the unanswered user message from that turn, chat recovery retries the turn automatically unless <code>onChatRecovery</code> returns <code>{ continue: false }</code>.</p>
<h2 id="managing-state-over-time">Managing state over time</h2>
<p>An agent that runs for months accumulates data: conversation history, timeline events, completed tasks, schedule records. Without management, this grows unbounded.</p>
<h3 id="housekeeping">Housekeeping</h3>
<p>Schedule periodic cleanup to prune old data and archive completed work:</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async onStart() {&#10;		await this.schedule(&quot;0 0 * * *&quot;, &quot;housekeeping&quot;, {}, { idempotent: true });&#10;	}&#10;&#10;	async housekeeping() {&#10;		const cutoff = Date.now() - 30 * 24 * 60 * 60 * 1000;&#10;		const toArchive = this.state.tasks.filter(&#10;			(t) =&gt; t.status === &quot;complete&quot; &amp;&amp; (t.completedAt ?? 0) &lt; cutoff,&#10;		);&#10;		for (const task of toArchive) {&#10;			this&#10;				.sql`INSERT INTO archived_tasks (id, data) VALUES (${task.id}, ${JSON.stringify(task)})`;&#10;		}&#10;		this.setState({&#10;			...this.state,&#10;			tasks: this.state.tasks.filter(&#10;				(t) =&gt; !toArchive.some((a) =&gt; a.id === t.id),&#10;			),&#10;		});&#10;&#10;		this.deleteWorkflows({&#10;			status: [&quot;complete&quot;, &quot;errored&quot;],&#10;			createdBefore: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000),&#10;		});&#10;	}&#10;}&#10;</code></pre>
<h3 id="conversation-history-management">Conversation history management</h3>
<p>For agents that use <code>AIChatAgent</code>, conversation history can grow large over extended lifespans. Without management, a 3-month conversation will exhaust the LLM's context window long before the project ends.</p>
<p>Strategies for managing conversation size:</p>
<ul>
<li><strong>Sliding window</strong> — keep only the last N messages in the active context. Simple and predictable.</li>
<li><strong>Summarization</strong> — periodically summarize older messages and replace them with a compact summary. Original messages can remain in SQLite for audit.</li>
<li><strong>Selective retention</strong> — retain messages that contain decisions, approvals, and key context while pruning routine exchanges.</li>
</ul>
<h2 id="end-of-life">End of life</h2>
<p>A long-running agent eventually completes its purpose. The project ships, the investigation concludes, the monitoring window closes. Clean up explicitly:</p>
<pre tabindex="0"><code class="language-ts">export class ProjectManager extends Agent&lt;Env, ProjectState&gt; {&#10;	async completeProject() {&#10;		const schedules = await this.listSchedules();&#10;		for (const schedule of schedules) {&#10;			await this.cancelSchedule(schedule.id);&#10;		}&#10;&#10;		this.setState({ ...this.state, status: &quot;complete&quot; });&#10;&#10;		// All SQLite data, schedules, and state are permanently deleted&#10;		await this.destroy();&#10;	}&#10;}&#10;</code></pre>
<p><code>this.destroy()</code> is permanent. If you may need the agent's data later, archive it to an external store (R2, D1, or an API call) before destroying. For agents that might be reactivated, simply mark them as complete and let them hibernate — they cost nothing when idle.</p>
<h2 id="when-to-use-workflows-vs-agent-internal-patterns">When to use Workflows vs agent-internal patterns</h2>
<p>Both Workflows and agent-internal primitives (schedules, fibers, queues) support long-running work. The right choice depends on the nature of the work:</p>
<table>
<thead>
<tr>
<th></th>
<th>Agent-internal</th>
<th>Workflows</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Best for</strong></td>
<td>Agent-centric work: scheduling, polling, state updates</td>
<td>Independent multi-step pipelines</td>
</tr>
<tr>
<td><strong>Durability</strong></td>
<td>SQLite (survives eviction)</td>
<td>Workflow engine (survives everything)</td>
</tr>
<tr>
<td><strong>Retries</strong></td>
<td><code>this.retry()</code>, schedule-level retries</td>
<td>Per-step retries with backoff</td>
</tr>
<tr>
<td><strong>Max duration</strong></td>
<td>Minutes per activation (with <code>keepAlive</code>)</td>
<td>30 minutes per step, unlimited steps</td>
</tr>
<tr>
<td><strong>Human approval</strong></td>
<td>Build it yourself (state + WebSocket)</td>
<td>Built-in <code>waitForApproval()</code></td>
</tr>
<tr>
<td><strong>Complexity</strong></td>
<td>Lower — everything is in the agent</td>
<td>Higher — separate class, wrangler config</td>
</tr>
</tbody>
</table>
<p>A pragmatic rule: if the work is about the agent managing its own lifecycle (checking deadlines, syncing state, sending reminders), use schedules and fibers. If the work is a discrete pipeline that could fail and retry independently (deploy, data processing, report generation), use a Workflow.</p>
<p>The project manager agent uses both: schedules for its own rhythms (daily standups, progress syncs), and Workflows for heavyweight operations (deployments, CI pipelines).</p>
<h2 id="summary">Summary</h2>
<p>Long-running agents on Cloudflare are not long-running processes. They are durable entities that wake, work, and sleep — potentially over weeks or months. The key primitives:</p>
<table>
<thead>
<tr>
<th>Primitive</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong><code>setState()</code> / <code>this.sql</code></strong></td>
<td>Persist state across activations</td>
</tr>
<tr>
<td><strong><code>schedule()</code> / <code>scheduleEvery()</code></strong></td>
<td>Wake the agent at future times</td>
</tr>
<tr>
<td><strong><code>keepAlive()</code> / <code>keepAliveWhile()</code></strong></td>
<td>Prevent eviction during active work</td>
</tr>
<tr>
<td><strong><code>runFiber()</code> / <code>stash()</code></strong></td>
<td>Checkpoint and recover long tasks</td>
</tr>
<tr>
<td><strong><code>startFiber()</code></strong></td>
<td>Durably accept, inspect, and cancel jobs</td>
</tr>
<tr>
<td><strong><code>chatRecovery</code></strong></td>
<td>Recover interrupted LLM streams</td>
</tr>
<tr>
<td><strong><code>onRequest()</code> / <code>onEmail()</code> / RPC</strong></td>
<td>Wake on external events</td>
</tr>
<tr>
<td><strong><code>runWorkflow()</code></strong></td>
<td>Delegate heavyweight multi-step work</td>
</tr>
<tr>
<td><strong><code>subAgent()</code></strong></td>
<td>Delegate specialized work to child agents</td>
</tr>
<tr>
<td><strong>Structured plans in state</strong></td>
<td>Enable recovery, visibility, and re-planning</td>
</tr>
</tbody>
</table>
<p>For the project manager agent, these compose into an agent that:</p>
<ol>
<li><strong>Plans</strong> — breaks goals into steps, persists the plan in state</li>
<li><strong>Executes</strong> — runs steps one at a time, hibernating between them</li>
<li><strong>Reacts</strong> — wakes on webhooks, emails, and schedules</li>
<li><strong>Recovers</strong> — resumes from the last checkpoint after any interruption</li>
<li><strong>Delegates</strong> — hands off work to sub-agents and Workflows</li>
<li><strong>Maintains</strong> — prunes old data, archives completed work, manages its own lifecycle</li>
<li><strong>Ends</strong> — cleans up and destroys itself when the project is done</li>
</ol>
<p>The agent does not need to run continuously to do any of this. It just needs to exist.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/runtime/execution/durable-execution/">Durable Execution</a> — <code>runFiber()</code>, <code>startFiber()</code>, <code>stash()</code>, and crash recovery</li>
<li><a href="/agents/runtime/execution/schedule-tasks/">Schedule tasks</a> — delayed, cron, and interval tasks</li>
<li><a href="/agents/runtime/execution/retries/">Retries</a> — retry options and patterns</li>
<li><a href="/agents/runtime/execution/run-workflows/">Workflows</a> — durable multi-step processing</li>
<li><a href="/agents/runtime/lifecycle/state/">Store and sync state</a> — <code>setState()</code> and persistence</li>
<li><a href="/agents/runtime/communication/websockets/">WebSockets</a> — lifecycle hooks and hibernation</li>
<li><a href="/agents/runtime/lifecycle/callable-methods/">Callable methods</a> — RPC via <code>@callable</code> and service bindings</li>
<li><a href="/agents/communication-channels/email/">Email routing</a> — receiving inbound email</li>
<li><a href="/agents/communication-channels/webhooks/">Webhooks</a> — receiving external events</li>
<li><a href="/agents/concepts/agentic-patterns/human-in-the-loop/">Human in the loop</a> — approval flows</li>
</ul>
