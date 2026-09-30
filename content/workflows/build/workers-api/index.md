<p>This guide details the Workflows API within Cloudflare Workers, including methods, types, and usage examples.</p>
<h2 id="workflowentrypoint">WorkflowEntrypoint</h2>
<p>The <code>WorkflowEntrypoint</code> class is the core element of a Workflow definition. A Workflow must extend this class and define a <code>run</code> method with at least one <code>step</code> call to be considered a valid Workflow.</p>
<pre><code class="language-ts">export class MyWorkflow extends WorkflowEntrypoint&lt;Env, Params&gt; {&#10;	async run(event: WorkflowEvent&lt;Params&gt;, step: WorkflowStep) {&#10;		// Steps here&#10;	}&#10;}&#10;</code></pre>
<h3 id="run">run</h3>
<ul>
<li><code>run(event: WorkflowEvent&lt;T&gt;, step: WorkflowStep): Promise&lt;T&gt;</code>
<ul>
<li><code>event</code> - the event passed to the Workflow, including an optional <code>payload</code> containing data (parameters)</li>
<li><code>step</code> - the <code>WorkflowStep</code> type that provides the step methods for your Workflow</li>
</ul>
</li>
</ul>
<p>The <code>run</code> method can optionally return data, which is available when querying the instance status via the <a href="/workflows/build/workers-api/#instancestatus">Workers API</a>, <a href="/api/resources/workflows/subresources/instances/subresources/status/">REST API</a> and the Workflows dashboard. This can be useful if your Workflow is computing a result, returning the key to data stored in object storage, or generating some kind of identifier you need to act on.</p>
<pre><code class="language-ts">export class MyWorkflow extends WorkflowEntrypoint&lt;Env, Params&gt; {&#10;	async run(event: WorkflowEvent&lt;Params&gt;, step: WorkflowStep) {&#10;		// Steps here&#10;		let someComputedState = await step.do(&quot;my step&quot;, async () =&gt; {});&#10;&#10;		// Optional: return state from our run() method&#10;		return someComputedState;&#10;	}&#10;}&#10;</code></pre>
<p>The <code>WorkflowEvent</code> type accepts an optional <a href="https://www.typescriptlang.org/docs/handbook/2/generics.html#working-with-generic-type-variables">type parameter</a> that allows you to provide a type for the <code>payload</code> property within the <code>WorkflowEvent</code>.</p>
<p>Refer to the <a href="/workflows/build/events-and-parameters/">events and parameters</a> documentation for how to handle events within your Workflow code.</p>
<p>Finally, any JS control-flow primitive (if conditions, loops, <code>try...catch</code> blocks, promises, and more) can be used to manage steps inside the <code>run</code> method.</p>
<h2 id="workflowevent">WorkflowEvent</h2>
<pre><code class="language-ts">export type WorkflowCronSchedule = {&#10;	/** Cron expression that triggered this event. */&#10;	cron: string;&#10;	/** Timestamp of the scheduled trigger, in milliseconds since the Unix epoch. */&#10;	scheduledTime: number;&#10;};&#10;&#10;export type WorkflowEvent&lt;T&gt; = {&#10;	payload: Readonly&lt;T&gt;;&#10;	timestamp: Date;&#10;	instanceId: string;&#10;	workflowName: string;&#10;	schedule?: WorkflowCronSchedule;&#10;};&#10;</code></pre>
<ul>
<li>The <code>WorkflowEvent</code> is the first argument to a Workflow's <code>run</code> method.
<ul>
<li><code>payload</code> - a default type of <code>any</code> or type <code>T</code> if a type parameter is provided.</li>
<li><code>timestamp</code> - a <code>Date</code> object set to the time the Workflow instance was created (triggered).</li>
<li><code>instanceId</code> - the ID of the associated instance.</li>
<li><code>workflowName</code> - the name of the associated Workflow.</li>
<li><code>schedule</code> - metadata for Workflow instances created by a cron schedule, including the <code>cron</code> expression and <code>scheduledTime</code> in milliseconds since the Unix epoch.</li>
</ul>
</li>
</ul>
<p>Refer to the <a href="/workflows/build/events-and-parameters/">events and parameters</a> documentation for how to handle events within your Workflow code.</p>
<h2 id="workflowstep">WorkflowStep</h2>
<h3 id="step">step</h3>
<ul>
<li><code>step.do(name: string, callback: (ctx: WorkflowStepContext): RpcSerializable): Promise&lt;T&gt;</code></li>
<li><code>step.do(name: string, callback: (ctx: WorkflowStepContext): RpcSerializable, rollbackOptions?: WorkflowStepRollbackOptions&lt;T&gt;): Promise&lt;T&gt;</code></li>
<li><code>step.do(name: string, config?: WorkflowStepConfig, callback: (ctx: WorkflowStepContext):
RpcSerializable): Promise&lt;T&gt;</code>
<ul>
<li><code>name</code> - the name of the step, up to 256 characters.</li>
<li><code>config</code> (optional) - an optional <code>WorkflowStepConfig</code> for configuring <a href="/workflows/build/sleeping-and-retrying/">step specific retry behaviour</a>.</li>
<li><code>callback</code> - an asynchronous function that receives a <a href="/workflows/build/step-context/"><code>WorkflowStepContext</code></a> and optionally returns serializable state for the Workflow to persist. In JavaScript Workflows, this includes a fresh, unlocked <code>ReadableStream&lt;Uint8Array&gt;</code> for large binary output.</li>
</ul>
</li>
<li><code>step.do(name: string, config?: WorkflowStepConfig, callback: (ctx: WorkflowStepContext):
RpcSerializable, rollbackOptions?: WorkflowStepRollbackOptions&lt;T&gt;): Promise&lt;T&gt;</code>
<ul>
<li><code>name</code> - the name of the step, up to 256 characters.</li>
<li><code>config</code> (optional) - an optional <code>WorkflowStepConfig</code> for configuring <a href="/workflows/build/sleeping-and-retrying/">step specific retry behaviour</a>.</li>
<li><code>callback</code> - an asynchronous function that receives a <a href="/workflows/build/step-context/"><code>WorkflowStepContext</code></a> and optionally returns serializable state for the Workflow to persist. In JavaScript Workflows, this includes a fresh, unlocked <code>ReadableStream&lt;Uint8Array&gt;</code> for large binary output.</li>
<li><code>rollbackOptions</code> (optional) - register rollback logic for the step. If the Workflow later fails, registered rollbacks run in reverse step-start order.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="returning-state">Returning state</h3>
@markup("md", "content/.markup/bodies/17532.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17533.md")
</div>
<ul>
<li><code>step.sleep(name: string, duration: WorkflowDuration): Promise&lt;void&gt;</code>
<ul>
<li><code>name</code> - the name of the step.</li>
<li><code>duration</code> - the duration to sleep for, as a <code>number</code> in milliseconds or as a <code>WorkflowDuration</code>-compatible string.</li>
<li>Refer to the <a href="/workflows/build/sleeping-and-retrying/">documentation on sleeping and retrying</a> to learn more about how Workflows are retried.</li>
</ul>
</li>
<li><code>step.sleepUntil(name: string, timestamp: Date | number): Promise&lt;void&gt;</code>
<ul>
<li><code>name</code> - the name of the step.</li>
<li><code>timestamp</code> - a JavaScript <code>Date</code> object or milliseconds from the Unix epoch to sleep the Workflow instance until.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17530.md")
</aside>
<ul>
<li><code>step.waitForEvent(name: string, options: ): Promise&lt;void&gt;</code>-
<code>name</code> - the name of the step. - <code>options</code> - an object with properties for
<code>type</code> (up to 100 characters <sup><a href="#footnote-1">1</a></sup>), which determines which event type this
<code>waitForEvent</code> call will match on when calling <code>instance.sendEvent</code>, and an
optional <code>timeout</code> property, which defines how long the <code>waitForEvent</code> call
will block for before throwing a timeout exception. The default timeout is 24
hours.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17534.md")
</div>
<p>Review the documentation on <a href="/workflows/build/events-and-parameters/">events and parameters</a> to learn how to send events to a running Workflow instance.</p>
<h2 id="workflowstepconfig">WorkflowStepConfig</h2>
<pre><code class="language-ts">export type WorkflowDynamicDelayContext = {&#10;	ctx: WorkflowStepContext;&#10;	error: Error;&#10;};&#10;&#10;export type WorkflowDelayFunction = (&#10;	input: WorkflowDynamicDelayContext,&#10;) =&gt; string | number | Promise&lt;string | number&gt;;&#10;&#10;export type WorkflowStepConfig = {&#10;	retries?: {&#10;		limit: number;&#10;		delay: string | number | WorkflowDelayFunction;&#10;		backoff?: WorkflowBackoff;&#10;	};&#10;	timeout?: string | number;&#10;};&#10;</code></pre>
<ul>
<li>A <code>WorkflowStepConfig</code> is an optional argument to the <code>do</code> method of a <code>WorkflowStep</code> and defines properties that allow you to configure the retry behaviour of that step.</li>
<li>Set <code>retries.delay</code> to a fixed duration, or pass a <code>WorkflowDelayFunction</code> to calculate the next retry delay from the current step context and thrown error.</li>
</ul>
<p>Refer to the <a href="/workflows/build/sleeping-and-retrying/">documentation on sleeping and retrying</a> to learn more about how Workflows are retried.</p>
<h2 id="rollback-options">Rollback options</h2>
<pre><code class="language-ts">type WorkflowRollbackContext&lt;T = unknown&gt; = {&#10;	ctx: WorkflowStepContext;&#10;	error: Error;&#10;	output: T | undefined;&#10;};&#10;&#10;type WorkflowRollbackHandler&lt;T = unknown&gt; = (&#10;	ctx: WorkflowRollbackContext&lt;T&gt;,&#10;) =&gt; Promise&lt;void&gt;;&#10;&#10;type WorkflowStepRollbackConfig = Pick&lt;&#10;	WorkflowStepConfig,&#10;	&quot;retries&quot; | &quot;timeout&quot;&#10;&gt;;&#10;&#10;type WorkflowStepRollbackOptions&lt;T = unknown&gt; = {&#10;	rollback: WorkflowRollbackHandler&lt;T&gt;;&#10;	rollbackConfig?: WorkflowStepRollbackConfig;&#10;};&#10;</code></pre>
<ul>
<li>Pass this <code>WorkflowStepRollbackOptions</code> object as the final argument to <code>step.do()</code> to register a compensating action for a successful step.</li>
<li><code>rollback</code> receives the original step context, the error that caused the Workflow to fail, and the step output returned by the forward step.</li>
<li><code>rollbackConfig</code> applies retry and timeout settings to the rollback handler itself.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17535.md")
</div>
<h2 id="workflowstepcontext">WorkflowStepContext</h2>
<pre><code class="language-ts">export type WorkflowStepContext = {&#10;	step: {&#10;		name: string;&#10;		count: number;&#10;	};&#10;	attempt: number;&#10;	config: WorkflowStepConfig;&#10;};&#10;</code></pre>
<ul>
<li>The <code>WorkflowStepContext</code> is passed as the first argument to the <code>step.do</code> callback function. It provides runtime information about the current step.
<ul>
<li><code>step.name</code> - the name of the step as passed to <code>step.do</code>.</li>
<li><code>step.count</code> - how many times <code>step.do</code> has been called with this name in the current Workflow run (1-indexed).</li>
<li><code>attempt</code> - the current attempt number (1-indexed). <code>1</code> on the first try, <code>2</code> on the first retry, and so on.</li>
<li><code>config</code> - the resolved <code>WorkflowStepConfig</code> for this step, including any defaults applied by the runtime.</li>
</ul>
</li>
</ul>
<p>Refer to the <a href="/workflows/build/step-context/">step context documentation</a> for usage examples.</p>
<h2 id="workflow-step-limits">Workflow step limits</h2>
<p>Each workflow on Workers Paid supports 10,000 steps by default. You can increase this up to 25,000 steps by configuring <code>steps</code> within the <code>limits</code> property of your Workflow definition in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17536.md")
</div>
<p><code>step.sleep</code> does not count towards the maximum steps limit.</p>
<p>Note that Workflows on Workers Free have a limit of 1,024 steps. Refer to <a href="/workflows/reference/limits/">Workflow limits</a> for more information.</p>
<h2 id="nonretryableerror">NonRetryableError</h2>
<ul>
<li><code>throw new NonRetryableError(message: <span class="nb-type">string</span>, name <span class="nb-type">string</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">NonRetryableError</span>
<ul>
<li>When thrown inside <a href="/workflows/build/workers-api/#step"><code>step.do()</code></a>, this error stops step retries, propagating the error to the top level (the <a href="/workflows/build/workers-api/#run">run</a> function). Any error not handled at this top level will cause the Workflow instance to fail.</li>
<li>Refer to the <a href="/workflows/build/sleeping-and-retrying/">documentation on sleeping and retrying</a> to learn more about how Workflows steps are retried.</li>
</ul>
</li>
</ul>
<h2 id="call-workflows-from-workers">Call Workflows from Workers</h2>
<p>Workflows exposes an API directly to your Workers scripts via the <a href="/workers/runtime-apis/bindings/#what-is-a-binding">bindings</a> concept. Bindings allow you to securely call a Workflow without having to manage API keys or clients.</p>
<p>You can bind to a Workflow by defining a <code>[[workflows]]</code> binding within your Wrangler configuration.</p>
<p>For example, to bind to a Workflow called <code>workflows-starter</code> and to make it available on the <code>MY_WORKFLOW</code> variable to your Worker script, you would configure the following fields within the <code>[[workflows]]</code> binding definition:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17537.md")
</div>
<h3 id="bind-from-pages">Bind from Pages</h3>
<p>You can bind and trigger Workflows from <a href="/pages/functions/">Pages Functions</a> by deploying a Workers project with your Workflow definition and then invoking that Worker using <a href="/pages/functions/bindings/#service-bindings">service bindings</a> or a standard <code>fetch()</code> call.</p>
<p>Visit the documentation on <a href="/workflows/build/call-workflows-from-pages/">calling Workflows from Pages</a> for examples.</p>
<h3 id="cross-script-calls">Cross-script calls</h3>
<p>You can also bind to a Workflow that is defined in a different Worker script from the script your Workflow definition is in. To do this, provide the <code>script_name</code> key with the name of the script to the <code>[[workflows]]</code> binding definition in your Wrangler configuration.</p>
<p>For example, if your Workflow is defined in a Worker script named <code>billing-worker</code>, but you are calling it from your <code>web-api-worker</code> script, your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> would resemble the following:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17538.md")
</div>
<p>If you're using TypeScript, run <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a> whenever you modify your Wrangler configuration file. This generates types for the <code>env</code> object based on your bindings, as well as <a href="/workers/languages/typescript/">runtime types</a>.</p>
<h2 id="workflow">Workflow</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17529.md")
</aside>
<p>The <code>Workflow</code> type provides methods that allow you to create, inspect the status, and manage running Workflow instances from within a Worker script.
It is part of the generated types produced by <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a>.</p>
<pre><code class="language-ts">interface Env {&#10;	// The &#x27;MY_WORKFLOW&#x27; variable should match the &quot;binding&quot; value set in the Wrangler config file&#10;	MY_WORKFLOW: Workflow;&#10;}&#10;</code></pre>
<p>The <code>Workflow</code> type exports the following methods:</p>
<h3 id="create">create</h3>
<p>Create (trigger) a new instance of the given Workflow.</p>
<ul>
<li><code>create(options?: WorkflowInstanceCreateOptions): Promise&lt;WorkflowInstance&gt;</code>
<ul>
<li><code>options</code> - optional properties to pass when creating an instance, including a user-provided ID and payload parameters.</li>
</ul>
</li>
</ul>
<p>An ID is automatically generated, but a user-provided ID can be specified (up to 100 characters <sup><a href="#footnote-1">1</a></sup>). This can be useful when mapping Workflows to users, merchants or other identifiers in your system. You can also provide a JSON object as the <code>params</code> property, allowing you to pass data for the Workflow instance to act on as its <a href="/workflows/build/events-and-parameters/"><code>WorkflowEvent</code></a>.</p>
<pre><code class="language-ts">// Create a new Workflow instance with your own ID and pass params to the Workflow instance&#10;let instance = await env.MY_WORKFLOW.create({&#10;	id: myIdDefinedFromOtherSystem,&#10;	params: { hello: &quot;world&quot; },&#10;});&#10;return Response.json({&#10;	id: instance.id,&#10;	details: await instance.status(),&#10;});&#10;</code></pre>
<p>Returns a <code>WorkflowInstance</code>.</p>
<p>Throws an error if the provided ID is already used by an existing instance that has not yet passed its <a href="/workflows/reference/limits/">retention limit</a>. To re-run a workflow with the same ID, you can <a href="/workflows/build/trigger-workflows/#restart-a-workflow"><code>restart</code></a> the existing instance.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17528.md")
</aside>
<p>You can also provide a type parameter to the <code>Workflows</code> type when creating (triggering) a Workflow instance using the <code>create</code> method of the <a href="/workflows/build/workers-api/#workflow">Workers API</a>. Note that this does <em>not</em> propagate type information into the Workflow itself, as TypeScript types are a build-time construct.</p>
<p>To provide an optional type parameter to the <code>Workflow</code>, pass a type argument with your type when defining your Workflow bindings:</p>
<pre><code class="language-ts">interface User {&#10;	email: string;&#10;	createdTimestamp: number;&#10;}&#10;&#10;interface Env {&#10;	// Pass our User type as the type parameter to the Workflow definition&#10;  MY_WORKFLOW: Workflow&lt;User&gt;;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// More likely to come from your database or via the request body!&#10;		const user: User = {&#10;			email: user@example.com,&#10;			createdTimestamp: Date.now()&#10;		}&#10;&#10;		let instance = await env.MY_WORKFLOW.create({&#10;			// params expects the type User&#10;			params: user&#10;		})&#10;&#10;		return Response.json({&#10;			id: instance.id,&#10;			details: await instance.status(),&#10;		});&#10;	}&#10;}&#10;</code></pre>
<h3 id="createbatch">createBatch</h3>
<p>Create (trigger) a batch of new instance of the given Workflow, up to 100 instances at a time.</p>
<p>This is useful when you are scheduling multiple instances at once. A call to <code>createBatch</code> is treated the same as a call to <code>create</code> (for a single instance) and allows you to work within the <a href="/workflows/reference/limits/">instance creation limit</a>.</p>
<ul>
<li><code>createBatch(batch: WorkflowInstanceCreateOptions[]): Promise&lt;WorkflowInstance[]&gt;</code>
<ul>
<li><code>batch</code> - list of Options to pass when creating an instance, including a user-provided ID and payload parameters.</li>
</ul>
</li>
</ul>
<p>Each element of the <code>batch</code> list is expected to include both <code>id</code> and <code>params</code> properties:</p>
<pre><code class="language-ts">// Create a new batch of 3 Workflow instances, each with its own ID and pass params to the Workflow instances&#10;const listOfInstances = [&#10;	{ id: &quot;id-abc123&quot;, params: { hello: &quot;world-0&quot; } },&#10;	{ id: &quot;id-def456&quot;, params: { hello: &quot;world-1&quot; } },&#10;	{ id: &quot;id-ghi789&quot;, params: { hello: &quot;world-2&quot; } },&#10;];&#10;let instances = await env.MY_WORKFLOW.createBatch(listOfInstances);&#10;</code></pre>
<p>Returns an array of <code>WorkflowInstance</code>.</p>
<p>Unlike <a href="/workflows/build/workers-api/#create"><code>create</code></a>, this operation is idempotent and will not fail if an ID is already in use. If an existing instance with the same ID is still within its <a href="/workflows/reference/limits/">retention limit</a>, it will be skipped and excluded from the returned array.</p>
<h3 id="deletebatch">deleteBatch</h3>
<p>Delete up to 100 Workflow instances and their stored state.</p>
<p><code>deleteBatch(instanceIds: string[])</code> returns a <code>Promise&lt;WorkflowBatchDeleteResult&gt;</code>. The <code>instanceIds</code> argument contains the IDs of the Workflow instances to delete.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17539.md")
</div>
<p>The operation returns successes and per-instance failures:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17540.md")
</div>
<p><code>deleted</code> contains the IDs that were deleted successfully. <code>errors</code> contains failures identified by instance ID, with a stable error code and message.</p>
<p><code>deleteBatch()</code> accepts between 1 and 100 IDs. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position. An ID whose instance does not exist is included in <code>errors</code>. If any ID is invalid, the call fails before deleting any instances. Deleting a running instance removes its stored state and stops its current execution without running rollback handlers.</p>
<h3 id="get">get</h3>
<p>Get a specific Workflow instance by ID.</p>
<ul>
<li><code>get(id: string): Promise&lt;WorkflowInstance&gt;</code>- <code>id</code> - the ID
of the Workflow instance.</li>
</ul>
<p>Returns a <code>WorkflowInstance</code>. Throws an exception if the instance ID does not exist.</p>
<pre><code class="language-ts">// Fetch an existing Workflow instance by ID:&#10;try {&#10;	let instance = await env.MY_WORKFLOW.get(id);&#10;	return Response.json({&#10;		id: instance.id,&#10;		details: await instance.status(),&#10;	});&#10;} catch (e: any) {&#10;	// Handle errors&#10;	// .get will throw an exception if the ID doesn&#x27;t exist or is invalid.&#10;	const msg = `failed to get instance ${id}: ${e.message}`;&#10;	console.error(msg);&#10;	return Response.json({ error: msg }, { status: 400 });&#10;}&#10;</code></pre>
<h2 id="workflowinstancecreateoptions">WorkflowInstanceCreateOptions</h2>
<p>Optional properties to pass when creating an instance.</p>
<pre><code class="language-ts">interface WorkflowInstanceCreateOptions {&#10;	/**&#10;	 &#42; An id for your Workflow instance. Must be unique within the Workflow.&#10;	 &#42;/&#10;	id?: string;&#10;	/**&#10;	 &#42; The event payload the Workflow instance is triggered with&#10;	 &#42;/&#10;	params?: unknown;&#10;	/**&#10;	 &#42; The retention policy for the Workflow instance.&#10;	 &#42; Defaults to the maximum retention period available for the owner&#x27;s account.&#10;	 &#42;/&#10;	retention?: {&#10;		/**&#10;		 &#42; How long to retain instance state after the Workflow completes successfully.&#10;		 &#42;/&#10;		successRetention?: WorkflowRetentionDuration;&#10;		/**&#10;		 &#42; How long to retain instance state after the Workflow ends in an errored or terminated state.&#10;		 &#42;/&#10;		errorRetention?: WorkflowRetentionDuration;&#10;	};&#10;}&#10;&#10;type WorkflowRetentionDuration = WorkflowSleepDuration;&#10;</code></pre>
<p>If <code>retention</code> is not set, instance state is retained for the maximum retention period available on your account (3 days on the Workers Free plan, 30 days on the Workers Paid plan). Refer to the <a href="/workflows/reference/limits/">retention limit</a> for more information.</p>
<p>The following example creates an instance that retains state for 1 day after success and 7 days after an error:</p>
<pre><code class="language-ts">let instance = await env.MY_WORKFLOW.create({&#10;	id: myIdDefinedFromOtherSystem,&#10;	params: { hello: &quot;world&quot; },&#10;	retention: {&#10;		successRetention: &quot;1 day&quot;,&#10;		errorRetention: &quot;7 days&quot;,&#10;	},&#10;});&#10;</code></pre>
<h2 id="workflowinstance">WorkflowInstance</h2>
<p>Represents a specific instance of a Workflow, and provides methods to manage the instance.</p>
<pre><code class="language-ts">declare abstract class WorkflowInstance {&#10;	public id: string;&#10;	/**&#10;	 &#42; Pause the instance.&#10;	 &#42;/&#10;	public pause(): Promise&lt;void&gt;;&#10;	/**&#10;	 &#42; Resume the instance. If it is already running, an error will be thrown.&#10;	 &#42;/&#10;	public resume(): Promise&lt;void&gt;;&#10;	/**&#10;	 &#42; Terminate the instance. If it is errored, terminated or complete, an error will be thrown.&#10;	 &#42;/&#10;	public terminate(options?: WorkflowInstanceTerminateOptions): Promise&lt;void&gt;;&#10;	/**&#10;	 &#42; Restart the instance from the beginning, or from a specific step.&#10;	 &#42;/&#10;	public restart(options?: WorkflowInstanceRestartOptions): Promise&lt;void&gt;;&#10;	/**&#10;	 &#42; Delete the instance and its stored state.&#10;	 &#42;/&#10;	public delete(): Promise&lt;void&gt;;&#10;	/**&#10;	 &#42; Returns the current status of the instance.&#10;	 &#42;/&#10;	public status(): Promise&lt;InstanceStatus&gt;;&#10;	/**&#10;	 &#42; Subscribe to events from this Workflow instance.&#10;	 &#42;/&#10;	public subscribe(&#10;		options?: WorkflowInstanceSubscribeOptions,&#10;	): Promise&lt;WorkflowInstanceSubscription&gt;;&#10;}&#10;</code></pre>
<h3 id="id">id</h3>
<p>Return the id of a Workflow.</p>
<ul>
<li><code>id: string</code></li>
</ul>
<h3 id="status">status</h3>
<p>Return the status of a running Workflow instance.</p>
<ul>
<li><code>status(): Promise&lt;InstanceStatus&gt;</code></li>
</ul>
<h3 id="pause">pause</h3>
<p>Pause a running Workflow instance.</p>
<ul>
<li><code>pause(): Promise&lt;void&gt;</code></li>
</ul>
<h3 id="resume">resume</h3>
<p>Resume a paused Workflow instance.</p>
<ul>
<li><code>resume(): Promise&lt;void&gt;</code></li>
</ul>
<h3 id="restart">restart</h3>
<p>Restart a Workflow instance from the beginning, or from a specific step.</p>
<ul>
<li><code>restart(options?: WorkflowInstanceRestartOptions): Promise&lt;void&gt;</code>
<ul>
<li><code>options</code> - optional properties that control from where the instance restarts.</li>
</ul>
</li>
</ul>
<pre><code class="language-ts">let instance = await env.MY_WORKFLOW.get(&quot;abc-123&quot;);&#10;&#10;// Restart the instance from the beginning.&#10;await instance.restart();&#10;&#10;// Restart the instance from the step named &quot;aggregate&quot;.&#10;await instance.restart({ from: { name: &quot;aggregate&quot; } });&#10;&#10;// Restart the instance from the third call to a step named &quot;process&quot;.&#10;await instance.restart({ from: { name: &quot;process&quot;, count: 3 } });&#10;</code></pre>
<p>When restarting from a specific step, the cached results of every earlier step are reused, while the target step and any steps that follow it run again. The call throws an error if no step matching <code>from</code> is found in the instance's execution history.</p>
<h4 id="workflowinstancerestartoptions">WorkflowInstanceRestartOptions</h4>
<pre><code class="language-ts">interface WorkflowInstanceRestartOptions {&#10;	/**&#10;	 &#42; The step to restart the instance from.&#10;	 &#42; If omitted, the instance restarts from the beginning.&#10;	 &#42;/&#10;	from?: {&#10;		/**&#10;		 &#42; The name of the step.&#10;		 &#42;/&#10;		name: string;&#10;		/**&#10;		 &#42; The 1-based index of the step, used when multiple steps share the same name and type. Defaults to 1 (the first occurrence).&#10;		 &#42;/&#10;		count?: number;&#10;		/**&#10;		 &#42; The step type. Use this to disambiguate when the same name is shared across step types. Defaults to &quot;do&quot;.&#10;		 &#42;/&#10;		type?: &quot;do&quot; | &quot;sleep&quot; | &quot;waitForEvent&quot;;&#10;	};&#10;}&#10;</code></pre>
<p>The <code>from</code> object identifies the step to restart from. Only <code>name</code> is required; <code>count</code> and <code>type</code> are only needed when the same step name appears more than once in the run.</p>
<ul>
<li><code>name</code> - the name of the step.</li>
<li><code>count</code> - the 1-based index of the step, used when multiple steps share the same name and type (for example, inside a loop). Defaults to <code>1</code> (the first occurrence). Corresponds to <code>step.count</code> in the <a href="/workflows/build/step-context/">step context</a>.</li>
<li><code>type</code> - the step type (<code>&quot;do&quot;</code>, <code>&quot;sleep&quot;</code>, or <code>&quot;waitForEvent&quot;</code>). Defaults to <code>&quot;do&quot;</code>. Use this when the same name is shared across different step types.</li>
</ul>
<h3 id="terminate">terminate</h3>
<p>Terminate a Workflow instance.</p>
<ul>
<li><code>terminate(options?: WorkflowInstanceTerminateOptions): Promise&lt;void&gt;</code>
<ul>
<li><code>options</code> - optional properties that control how the instance is terminated.</li>
</ul>
</li>
</ul>
<pre><code class="language-ts">let instance = await env.MY_WORKFLOW.get(&quot;abc-123&quot;);&#10;&#10;// Terminate without running rollback handlers.&#10;await instance.terminate();&#10;&#10;// Run registered rollback handlers before terminating.&#10;await instance.terminate({ rollback: true });&#10;</code></pre>
<p>If <code>rollback</code> is <code>true</code>, Workflows runs the rollback handlers registered by completed or eligible steps before the instance reaches the <code>terminated</code> state. Steps without rollback handlers are skipped.</p>
<h4 id="workflowinstanceterminateoptions">WorkflowInstanceTerminateOptions</h4>
<pre><code class="language-ts">interface WorkflowInstanceTerminateOptions {&#10;	/**&#10;	 &#42; If true, run registered rollback handlers before terminating the instance.&#10;	 &#42;/&#10;	rollback?: boolean;&#10;}&#10;</code></pre>
<h3 id="delete">delete</h3>
<p>Delete a Workflow instance and its stored state with <code>delete(): Promise&lt;void&gt;</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17541.md")
</div>
<p>Deleting a running instance stops its current execution without running rollback handlers. If a Workflow deletes its own instance, execution stops during <code>await instance.delete()</code>, and code after the call does not run.</p>
<h3 id="sendevent">sendEvent</h3>
<p><a href="/workflows/build/events-and-parameters/">Send an event</a> to a running Workflow instance.</p>
<ul>
<li><code>sendEvent(): Promise&lt;void&gt;</code>- <code>options</code> - the event <code>type</code>
(up to 100 characters <sup><a href="#footnote-1">1</a></sup>) and <code>payload</code> to send to the Workflow instance.
The <code>type</code> must match the <code>type</code> in the corresponding <code>waitForEvent</code> call in
your Workflow.</li>
</ul>
<p>Return <code>void</code> on success; throws an exception if the Workflow is not running or is an errored state.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17542.md")
</div>
<p>You can call <code>sendEvent</code> multiple times, setting the value of the <code>type</code> property to match the specific <code>waitForEvent</code> calls in your Workflow.</p>
<p>This allows you to wait for multiple events at once, or use <code>Promise.race</code> to wait for multiple events and allow the first event to progress the Workflow.</p>
<h3 id="subscribe">subscribe</h3>
<p>Subscribe to historical and live execution events from a Workflow instance.</p>
<ul>
<li><code>subscribe(options?: WorkflowInstanceSubscribeOptions): Promise&lt;WorkflowInstanceSubscription&gt;</code>
<ul>
<li><code>options</code> - optional properties that set the starting cursor and filter event types.</li>
</ul>
</li>
</ul>
<p>The returned subscription provides a <code>next()</code> method. Each call returns the next matching <code>WorkflowInstanceEvent</code> or waits for one. The subscription ends when the instance completes, errors, or terminates.</p>
<h4 id="workflowinstancesubscribeoptions">WorkflowInstanceSubscribeOptions</h4>
<pre><code class="language-ts">interface WorkflowInstanceSubscribeOptions {&#10;	/**&#10;	 &#42; The event ID after which to start.&#10;	 &#42;/&#10;	cursor?: number;&#10;	/**&#10;	 &#42; Emit only events with one of these types.&#10;	 &#42;/&#10;	filter?: WorkflowInstanceEventType[];&#10;}&#10;&#10;type WorkflowInstanceEventType = WorkflowInstanceEvent[&quot;type&quot;];&#10;</code></pre>
<p>Call <code>subscribe()</code> without options to receive all events. Use <code>cursor</code> and <code>filter</code> to control which events the subscription returns:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17543.md")
</div>
<p>For event types, filtering behavior, and cursor usage, refer to <a href="/workflows/build/subscribe-to-instance-events/">Subscribe to events</a>.</p>
<h3 id="instancestatus">InstanceStatus</h3>
<p>Details the status of a Workflow instance.</p>
<pre><code class="language-ts">type InstanceStatus = {&#10;	status:&#10;		| &quot;queued&quot; // means that instance is waiting to be started (see concurrency limits)&#10;		| &quot;running&quot;&#10;		| &quot;paused&quot;&#10;		| &quot;errored&quot;&#10;		| &quot;terminated&quot; // user terminated the instance while it was running&#10;		| &quot;complete&quot;&#10;		| &quot;waiting&quot; // instance is hibernating and waiting for sleep or event to finish&#10;		| &quot;waitingForPause&quot; // instance is finishing the current work to pause&#10;		| &quot;unknown&quot;;&#10;	error?: {&#10;		name: string;&#10;		message: string;&#10;	};&#10;	output?: unknown;&#10;	rollback: {&#10;		outcome: &quot;complete&quot; | &quot;failed&quot;;&#10;		error: {&#10;			name: string;&#10;			message: string;&#10;		} | null;&#10;	} | null;&#10;};&#10;</code></pre>
<p>If a Workflow enters rollback, the Workers API continues to report <code>status: &quot;running&quot;</code> for compatibility while the rollback is executing. After the instance reaches a terminal state, inspect <code>rollback</code> to determine whether compensating steps completed successfully or failed.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Match pattern: `^[a-zA-Z0-9_][a-zA-Z0-9-_]*$`</li></ol></section>
