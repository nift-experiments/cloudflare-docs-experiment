---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workflows/
  description: 2026-09-17 12:00:00 UTC
  full_title: workflows changelog | Cloudflare Docs
  head_html: <title>workflows changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-17 12:00:00 UTC"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workflows/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workflows changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-17 12:00:00 UTC"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workflows/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workflows/#page","headline":"workflows changelog | Cloudflare Docs","description":"2026-09-17 12:00:00 UTC","url":"https://developers.cloudflare.com/changelog/product/workflows/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workflows/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="delete-workflow-instances-individually-or-in-batches"><a href="/changelog/post/2026-09-17-instance-delete/">Delete Workflow instances individually or in batches</a></h2>
<p><em>2026-09-17 12:00:00 UTC</em></p>
<p>You can now delete one or up to 100 Workflow instances and their stored state via the <a href="/workflows/build/workers-api/">Workflows API</a> or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. <a href="/workflows/reference/pricing/#storage-usage">Storage billing</a> is based on the average daily peak.</p>
<p>Delete one instance by calling <a href="/workflows/build/workers-api/#delete"><code>delete()</code></a> on its handle:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.MY_WORKFLOW.get(&quot;instance-abc&quot;);&#10;await instance.delete();&#10;</code></pre>
<p>If a Workflow deletes its own instance, execution stops during <code>await instance.delete()</code>. Code after the call does not run.</p>
<p>Delete multiple instances by calling <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch()</code></a> on the Workflow binding:</p>
<pre tabindex="0"><code class="language-ts">const result = await env.MY_WORKFLOW.deleteBatch([&#10;	&quot;instance-abc&quot;,&#10;	&quot;instance-def&quot;,&#10;]);&#10;&#10;console.log(result.deleted);&#10;console.log(result.errors);&#10;</code></pre>
<p>The batch result contains <code>{ id }</code> entries for successful deletions and per-instance errors. IDs that do not exist are returned as errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position.</p>
<p>Wrangler accepts positional instance IDs, a file containing a top-level JSON array of strings, or both, up to 100 IDs total. Use <code>latest</code> to delete the most recently created instance. Use <code>--local</code> against a local <code>wrangler dev</code> session:</p>
<pre tabindex="0"><code class="language-json">[&quot;instance-abc&quot;, &quot;instance-def&quot;]&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt; &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete my-workflow latest&#10;npx wrangler workflows instances delete my-workflow --filename ./instance-ids.json&#10;npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt; --local&#10;</code></pre>
<p>For more information, refer to <a href="/workflows/build/trigger-workflows/#delete-workflow-instances">Delete Workflow instances</a>, <a href="/workflows/build/workers-api/#delete"><code>delete</code></a>, and <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch</code></a>.</p>


<h2 id="stream-workflow-instance-events-in-your-worker-or-via-the-api-with-subscribe"><a href="/changelog/post/2026-09-15-instance-event-subscriptions/">Stream Workflow instance events in your Worker or via the API with .subscribe()</a></h2>
<p><em>2026-09-15 12:00:00 UTC</em></p>
<p>You can now stream Workflow instance events via <code>WorkflowInstance.subscribe()</code> and the <code>GET /subscribe</code> API endpoint. Workers and HTTP clients can react to <a href="/workflows/build/events-and-parameters/">workflow</a> and <a href="/workflows/build/step-context/#workflowstepcontext">step</a> events, including attempts, sleeps, waits, and rollbacks, without polling for instance status.</p>
<p>A subscription first streams the entire event history of the Workflow instance. After streaming past events, the subscription waits for new events as the instance runs. You can use <code>filter</code> to receive only specific event types or <code>cursor</code> to start a subscription at a specific event.</p>
<p>Use <code>.subscribe()</code> to update Workflow status in user-facing dashboards, send notifications when steps complete, or trigger follow-up work for specific events.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17835.md")</div>
<p>For event types, available fields, and subscription options, refer to <a href="/workflows/build/subscribe-to-instance-events/">Subscribe to events</a>.</p>


<h2 id="default-instance-retention-for-new-workflows-on-workers-paid-is-seven-days"><a href="/changelog/post/2026-09-10-paid-retention-default/">Default instance retention for new Workflows on Workers Paid is seven days</a></h2>
<p><em>2026-09-10 12:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> created on or after September 10, 2026, on the Workers Paid plan retain completed and errored instance state for seven days by default (previously 30 days). The seven day default helps to reduce storage costs by default. The maximum retention <a href="/workflows/reference/limits/">limit</a> remains 30 days.</p>
<p>The retention period for existing Workflows is unchanged. The Workers Free plan retains its three-day default and limit.</p>
<p>To set the retention period for a Workflow instance, specify <code>successRetention</code>, <code>errorRetention</code>, or both:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17834.md")</div>
<p>You can also set the retention period per Workflow and per instance in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a>.</p>
<p>For retention details, refer to <a href="/workflows/reference/pricing/">Workflows pricing</a> and the <a href="/workflows/build/workers-api/#workflowinstancecreateoptions"><code>WorkflowInstanceCreateOptions</code> API reference</a>.</p>


<h2 id="build-and-deploy-artifacts-repos-on-every-push"><a href="/changelog/post/2026-08-04-build-and-deploy-on-push/">Build and deploy Artifacts repos on every push</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now run your CI/CD pipeline on your <a href="/artifacts/">Artifacts</a> repo by defining a CI <a href="/workflows/">Workflow</a> with the <a href="https://github.com/cloudflare/ci">CI SDK</a>, automatically triggered on Artifacts push events.</p>
<p>This allows you to:</p>
<ul>
<li>Automatically build and deploy application code stored in Artifacts.</li>
<li>Run linting, type checking, tests, and other checks on every push.</li>
<li>Reuse dependencies when the lockfile (i.e. <code>pnpm-lock.yaml</code>) has not changed.</li>
<li>Stop deployment when a check or build fails.</li>
<li>Restrict API token access to the deployment step.</li>
<li>Deploy the output to a <a href="/workers/">Worker</a> or a <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> User Worker.</li>
</ul>
<p>Define your CI steps with <code>@cloudflare/ci</code>. Each <code>ci.runner()</code> spins up an isolated sandbox, and the <code>cache</code> option reuses installed dependencies across each sandboxed step in your CI job.</p>
<p>Point <code>cache.inputs</code> at your lockfile (i.e. <code>pnpm-lock.yaml</code>, <code>bun.lock</code>), and the install step only runs again when that lockfile changes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17690.md")</div>
<p>To start the Workflow automatically after each push, add a <code>cf.artifacts.repo.pushed</code> trigger to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17691.md")</div>
<p>To learn more, refer to <a href="/artifacts/guides/build-and-deploy-on-push/">Build and deploy Artifacts repos</a>.</p>


<h2 id="workflows-now-supports-delay-functions-when-retrying"><a href="/changelog/post/2026-07-09-dynamic-retry-delays/">Workflows now supports delay functions when retrying</a></h2>
<p><em>2026-07-09 12:00:00 UTC</em></p>
<p>With <a href="/workflows/">Workflows</a>, you can configure built-in retry behavior for each step. Previously, you could configure step retries with fixed delay durations, such as seconds, minutes, or hours, and backoff strategies such as <code>constant</code>, <code>linear</code>, or <code>exponential</code>.</p>
<p>Step retries now support dynamic delay functions. Instead of choosing only a base delay and backoff strategy, pass a function to <code>retries.delay</code> and calculate the next delay from the failed attempt and thrown error.</p>
<p>This is useful when retries should depend on the failure. Your Workflow may need to wait longer after a rate-limit error, but retry sooner after a short network failure. The delay function can also accommodate provider guidance if, for example, a downstream API returns a <code>Retry-After</code> value in its error messaging.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17833.md")</div>
<p>Dynamic delay functions can return a duration string, a number, or a promise that resolves to a duration. Use them to add adaptive retry behavior without writing separate queue or scheduling logic. For more information, refer to <a href="/workflows/build/sleeping-and-retrying/">Sleeping and retrying</a>.</p>


<h2 id="workflows-pricing-adds-per-step-billing-step-and-storage-billing-to-start-no-earlier-than-august-10-2026"><a href="/changelog/post/2026-07-07-workflows-billing-updates/">Workflows pricing adds per-step billing. Step and storage billing to start no earlier than August 10, 2026.</a></h2>
<p><em>2026-07-07T12:00:00</em></p>
<p><a href="/workflows/">Workflows</a> pricing now includes per-step billing. Requests and CPU time billing have been enabled since the initial public beta and is not changing.</p>
<h4 id="2026-07-07-workflows-billing-updates-workflows-adds-step-billing">Workflows adds step billing</h4>
<p>A step is each unit of work executed by a Workflow, including step operations such as <a href="/workflows/build/sleeping-and-retrying/">sleeping</a> or <a href="/workflows/build/events-and-parameters/">waiting for events</a>.</p>
<p>You can query Workflows analytics, including <code>stepCount</code> for a Workflow instance, with the <a href="/workflows/observability/metrics-analytics/#query-via-the-graphql-api">GraphQL Analytics API</a>.</p>
<h4 id="2026-07-07-workflows-billing-updates-steps-and-storage-billing-to-take-effect-august-10th-2026">Steps and storage billing to take effect August 10th, 2026</h4>
<p>Starting no earlier than August 10th, 2026, Cloudflare will begin billing for step and storage usage on Workers Paid plans.</p>
<p>Storage pricing has been published since Workflows became generally available and is not changing.  Storage is measured as persisted Workflow state in GB-months.</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Steps</td>
<td>3,000 included per day</td>
<td>500,000 included per month, then $0.80 per additional 100,000 steps</td>
</tr>
<tr>
<td>Storage</td>
<td>1 GB-month included</td>
<td>1 GB-month included, then $0.20 per additional GB-month</td>
</tr>
</tbody>
</table>
<p>Developers on the Workers Free plan will not be charged for steps or storage beyond the included amounts.</p>
<p>Cloudflare will not bill step and storage usage before August 10, 2026.</p>
<p>You can review Workflows usage in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> before this change takes effect. To reduce costs, consider reducing the number of steps per Workflow or improving the memory efficiency of your stored state.</p>
<p>Refer to the <a href="/workflows/reference/pricing/">Workflows pricing</a> page for full details.</p>


<h2 id="workflows-rollback-handlers-now-include-step-context"><a href="/changelog/post/2026-06-16-rollback-options/">Workflows rollback handlers now include step context</a></h2>
<p><em>2026-06-23 12:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> makes it easier to build reliable multi-step applications that can recover when downstream systems fail. Rollback handlers now receive the original <a href="/workflows/build/step-context/">step context</a> via a <code>ctx</code> object for the step being rolled back. This includes <code>ctx.step.name</code>, <code>ctx.step.count</code>, <code>ctx.attempt</code>, and the step <code>config</code> with defaults applied.</p>
<p>The <a href="/workflows/build/workers-api/#workflowstepconfig">step configuration</a> includes the retry and timeout settings used for that step, so you can customize your step recovery logic according to those fields.</p>
<pre tabindex="0"><code class="language-ts">await step.do(&#10;	&quot;create charge&quot;,&#10;	async () =&gt; {&#10;		const charge = await createCharge();&#10;		return { chargeId: charge.id };&#10;	},&#10;	{&#10;		rollback: async ({ ctx, output, error }) =&gt; {&#10;			// `output` is the value returned by the step being rolled back.&#10;			const { chargeId } = output as { chargeId: string };&#10;			await refundCharge(chargeId, {&#10;				// `ctx` is the original step context, including step name, count, attempt, and config.&#10;				reason: `${ctx.step.name}: ${error.message}`,&#10;			});&#10;		},&#10;		rollbackConfig: {&#10;			// `rollbackConfig` controls retries and timeout for the rollback handler.&#10;			retries: { limit: 3, delay: &quot;30 seconds&quot;, backoff: &quot;linear&quot; },&#10;			timeout: &quot;5 minutes&quot;,&#10;		},&#10;	},&#10;);&#10;</code></pre>
<p>Refer to <a href="/workflows/build/workers-api/#rollback-options">rollback options</a> to learn more.</p>


<h2 id="rollback-support-now-available-in-workflows"><a href="/changelog/post/2026-06-05-saga-rollbacks/">Rollback support now available in Workflows</a></h2>
<p><em>2026-06-05 15:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> now supports saga-style rollbacks,  allowing you to add compensating logic to each <code>step.do()</code> in case of downstream failures. If the instance fails, the rollback handlers will execute in reverse <code>step-start</code> order.</p>
<p>This is useful for multi-step operations that touch external systems, such as inventory reservations, payment authorization, ticket creation, or infrastructure provisioning. Instead of writing all cleanup logic in a top-level <code>catch</code>, you can keep each compensating action next to the step it undoes.</p>
<p>Rollback handlers support their own retry and timeout configuration, and Workflows now exposes rollback outcomes in instance status responses. Workflows analytics also emits rollback lifecycle events, making it easier to distinguish a forward execution failure from a rollback failure when debugging production workflows.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17832.md")</div>
<p>Refer to <a href="/workflows/build/workers-api/#rollback-options">rollback options</a> to learn more.</p>


<h2 id="schedule-workflow-instances-directly-from-your-workflow-binding"><a href="/changelog/post/2026-06-02-cron-workflows/">Schedule Workflow instances directly from your Workflow binding</a></h2>
<p><em>2026-06-02 15:00:00 UTC</em></p>
<p>You can now attach cron schedules directly to a Workflow binding in <code>wrangler.jsonc</code>. Each scheduled run creates a new Workflow instance automatically, so you do not need to define a separate Worker with a <code>scheduled</code> handler just to trigger your Workflow on an interval.</p>
<p>For example, you can configure hourly, every-15-minute, or weekday schedules on the same Workflow:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;workflows&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;my-scheduled-workflow&quot;,&#10;			&quot;binding&quot;: &quot;MY_WORKFLOW&quot;,&#10;			&quot;class_name&quot;: &quot;MyScheduledWorkflow&quot;,&#10;			&quot;schedules&quot;: [&quot;0 * * * *&quot;, &quot;*/15 * * * *&quot;, &quot;0 9 * * MON-FRI&quot;],&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>Cron workloads get all the same benefits of Workflows with built-in retries, multi-step durable execution, and configurable timeouts of Workflows.</p>
<pre tabindex="0"><code class="language-ts">import {&#10;	WorkflowEntrypoint,&#10;	WorkflowEvent,&#10;	WorkflowStep,&#10;} from &quot;cloudflare:workers&quot;;&#10;&#10;// Runs automatically on each cron schedule defined for the MY_WORKFLOW binding in wrangler.jsonc.&#10;export class MyScheduledWorkflow extends WorkflowEntrypoint&lt;Env&gt; {&#10;	async run(event: WorkflowEvent, step: WorkflowStep) {&#10;		const data = await step.do(&quot;fetch source data&quot;, async () =&gt; {&#10;			return await fetchSourceData();&#10;		});&#10;&#10;		// If this step fails, only this step is retried with the custom logic below&#10;		await step.do(&#10;			&quot;process and store results&quot;,&#10;			{&#10;				retries: { limit: 5, delay: &quot;30 seconds&quot;, backoff: &quot;exponential&quot; },&#10;				timeout: &quot;10 minutes&quot;,&#10;			},&#10;			async () =&gt; {&#10;				await processAndStore(data);&#10;			},&#10;		);&#10;	}&#10;}&#10;</code></pre>
<p>This makes it easier to build recurring, scheduled jobs such as database backups, invoice generation, report aggregation, and cleanup tasks without wiring up a separate Cron Trigger entrypoint.</p>
<p>For more information, refer to <a href="/workflows/build/trigger-workflows/">Trigger Workflows</a>.</p>


<h2 id="run-workflows-inside-dynamic-workers-with-the-cloudflare-dynamic-workflows-library"><a href="/changelog/post/2026-05-01-dynamic-workflows/">Run Workflows inside Dynamic Workers with the @cloudflare/dynamic-workflows library</a></h2>
<p><em>2026-05-01</em></p>
<p>You can now use <a href="https://github.com/cloudflare/dynamic-workflows"><code>@cloudflare/dynamic-workflows</code></a> to run a <a href="/workflows/">Workflow</a> inside a <a href="/dynamic-workers/">Dynamic Worker</a>, ensuring durable execution for code that is loaded at runtime.</p>
<p>The Worker Loader loads Dynamic Workers on demand, which previously made durability challenging. Even within a Dynamic Worker, a Workflow might sleep for hours or days between steps, and by the time it resumes, the original Dynamic Worker code would no longer be in memory.</p>
<p>The library solves this by tagging each Workflow instance with metadata that identifies which Dynamic Worker to load — for example, a tenant ID — then reloading the matching Dynamic Worker through the Worker Loader whenever a Workflow awakens.</p>
<p>Because Dynamic Workers are created on-demand, you do not have to register each Workflow up front or manage them individually. Load the Workflow code in the Dynamic Worker when it is needed, and the Workflows engine handles persistence and retries behind the scenes. Your Workflow code itself is unaffected by the routing and behaves as normal.</p>
<p>This unlocks patterns where the Workflow code itself is dynamic. For example, this is useful with:</p>
<ul>
<li><strong>SaaS platforms</strong> where each tenant defines their own automation, such as onboarding sequences, approval chains, or billing retry logic.</li>
<li><strong>AI agent frameworks</strong> where agents generate and execute multi-step plans at runtime, surviving restarts and waiting for human approval between tool calls.</li>
<li><strong>Multi-tenant job systems</strong> where each customer submits their own processing logic and every step persists progress and retries on failure.</li>
</ul>
<pre tabindex="0"><code class="language-ts">import {&#10;	createDynamicWorkflowEntrypoint,&#10;	DynamicWorkflowBinding,&#10;	wrapWorkflowBinding,&#10;	type WorkflowRunner,&#10;} from &quot;@cloudflare/dynamic-workflows&quot;;&#10;&#10;export { DynamicWorkflowBinding };&#10;&#10;interface Env {&#10;	WORKFLOWS: Workflow;&#10;	LOADER: WorkerLoader;&#10;}&#10;&#10;function loadTenant(env: Env, tenantId: string) {&#10;	return env.LOADER.get(tenantId, async () =&gt; ({&#10;		compatibilityDate: &quot;2026-01-01&quot;,&#10;		mainModule: &quot;index.js&quot;,&#10;		modules: { &quot;index.js&quot;: await fetchTenantCode(tenantId) },&#10;		// The Dynamic Worker uses this exactly like a real Workflow binding;&#10;		// every create() is tagged with { tenantId } automatically.&#10;		env: { WORKFLOWS: wrapWorkflowBinding({ tenantId }) },&#10;	}));&#10;}&#10;&#10;// The entrypoint name must match `class_name` in the workflows binding of your Wrangler config file.&#10;export const DynamicWorkflow = createDynamicWorkflowEntrypoint&lt;Env&gt;(&#10;	async ({ env, metadata }) =&gt; {&#10;		const stub = loadTenant(env, metadata.tenantId as string);&#10;		return stub.getEntrypoint(&quot;TenantWorkflow&quot;) as unknown as WorkflowRunner;&#10;	},&#10;);&#10;&#10;export default {&#10;	fetch(request: Request, env: Env) {&#10;		const tenantId = request.headers.get(&quot;x-tenant-id&quot;)!;&#10;		return loadTenant(env, tenantId).getEntrypoint().fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>For a full walkthrough, refer to the <a href="/dynamic-workers/usage/dynamic-workflows/">Dynamic Workflows guide</a>.</p>


<h2 id="additional-step-context-and-readablestream-support-now-available-in-workflows-step-do"><a href="/changelog/post/2026-04-21-step-context-and-readable-streams/">Additional step context and ReadableStream support now available in Workflows step.do()</a></h2>
<p><em>2026-04-21 12:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> now provides additional context inside <code>step.do()</code> callbacks and supports returning <code>ReadableStream</code> to handle larger step outputs.</p>
<h4 id="2026-04-21-step-context-and-readable-streams-step-context-properties">Step context properties</h4>
<p>The <code>step.do()</code> callback receives a context object with new properties <a href="/changelog/post/2026-03-06-step-context-available/">alongside</a> <code>attempt</code>:</p>
<ul>
<li><strong><code>step.name</code></strong> — The name passed to <code>step.do()</code></li>
<li><strong><code>step.count</code></strong> — How many times a step with that name has been invoked in this instance (1-indexed)
<ul>
<li>Useful when running the same step in a loop.</li>
</ul>
</li>
<li><strong><code>config</code></strong> — The resolved step configuration, including <code>timeout</code> and <code>retries</code> with defaults applied</li>
</ul>
<pre tabindex="0"><code class="language-ts">type ResolvedStepConfig = {&#10;	retries: {&#10;		limit: number;&#10;		delay: WorkflowDelayDuration | number;&#10;		backoff?: &quot;constant&quot; | &quot;linear&quot; | &quot;exponential&quot;;&#10;	};&#10;	timeout: WorkflowTimeoutDuration | number;&#10;};&#10;&#10;type WorkflowStepContext = {&#10;	step: {&#10;		name: string;&#10;		count: number;&#10;	};&#10;	attempt: number;&#10;	config: ResolvedStepConfig;&#10;};&#10;</code></pre>
<h4 id="2026-04-21-step-context-and-readable-streams-readablestream-support-in-step-do">ReadableStream support in <code>step.do()</code></h4>
<p>Steps can now return a <code>ReadableStream</code> directly. Although non-stream step outputs are <a href="/workflows/reference/limits/">limited to 1 MiB</a>, streamed outputs support much larger payloads.</p>
<pre tabindex="0"><code class="language-ts">const largePayload = await step.do(&quot;fetch-large-file&quot;, async () =&gt; {&#10;	const object = await env.MY_BUCKET.get(&quot;large-file.bin&quot;);&#10;	return object.body;&#10;});&#10;</code></pre>
<p>Note that streamed outputs are still considered part of the Workflow instance storage limit.</p>


<h2 id="increased-concurrency-creation-rate-and-queued-instance-limits-for-workflows-instances"><a href="/changelog/post/2026-04-15-workflows-limits-raised/">Increased concurrency, creation rate, and queued instance limits for Workflows instances</a></h2>
<p><em>2026-04-15 13:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> limits have been raised to the following:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent instances (running in parallel)</td>
<td>10,000</td>
<td>50,000</td>
</tr>
<tr>
<td>Instance creation rate (per account)</td>
<td>100/second per account</td>
<td>300/second per account, 100/second per workflow</td>
</tr>
<tr>
<td>Queued instances per Workflow <sup><a href="#2026-04-15-workflows-limits-raised-footnote-1">1</a></sup></td>
<td>1 million</td>
<td>2 million</td>
</tr>
</tbody>
</table>
<p>These increases apply to all users on the <a href="/workers/platform/pricing/">Workers Paid plan</a>. Refer to the <a href="/workflows/reference/limits/">Workflows limits documentation</a> for more details.</p>
<section class="footnotes"><h4 id="2026-04-15-workflows-limits-raised-footnotes">Footnotes</h4><ol><li id="2026-04-15-workflows-limits-raised-footnote-1">Queued instances are instances that have been created or awoken and are waiting for a concurrency slot.</li></ol></section>


<h2 id="all-wrangler-commands-for-workflows-now-support-local-development"><a href="/changelog/post/2026-04-01-wrangler-workflows-local/">All Wrangler commands for Workflows now support local development</a></h2>
<p><em>2026-04-01 12:00:00 UTC</em></p>
<p>All <code>wrangler workflows</code> commands now accept a <code>--local</code> flag to target a Workflow running in a local <code>wrangler dev</code> session instead of the production API.</p>
<p>You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows list --local&#10;npx wrangler workflows trigger my-workflow --local&#10;npx wrangler workflows instances list my-workflow --local&#10;npx wrangler workflows instances pause my-workflow &lt;INSTANCE_ID&gt; --local&#10;npx wrangler workflows instances send-event my-workflow &lt;INSTANCE_ID&gt; --type my-event --local&#10;</code></pre>
<p>All commands also accept <code>--port</code> to target a specific <code>wrangler dev</code> session (defaults to <code>8787</code>).</p>
<p>For more information, refer to <a href="/workflows/build/local-development/">Workflows local development</a>.</p>


<h2 id="workflow-instances-now-support-pause-resume-restart-and-terminate-methods-in-local-development"><a href="/changelog/post/2026-03-23-local-dev-instance-methods/">Workflow instances now support pause(), resume(), restart(), and terminate() methods in local development</a></h2>
<p><em>2026-03-23 12:00:00 UTC</em></p>
<p>Workflow instance methods <code>pause()</code>, <code>resume()</code>, <code>restart()</code>, and <code>terminate()</code> are now available in local development when using <code>wrangler dev</code>.</p>
<p>You can now test the full Workflow instance lifecycle locally:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.MY_WORKFLOW.create({&#10;	id: &quot;my-instance-id&quot;,&#10;});&#10;&#10;await instance.pause(); // pauses a running workflow instance&#10;await instance.resume(); // resumes a paused instance&#10;await instance.restart(); // restarts the instance from the beginning&#10;await instance.terminate(); // terminates the instance immediately&#10;</code></pre>


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


<h2 id="visualize-your-workflows-in-the-cloudflare-dashboard"><a href="/changelog/post/2026-02-03-workflows-visualizer/">Visualize your Workflows in the Cloudflare dashboard</a></h2>
<p><em>2026-02-04</em></p>
<p>Cloudflare Workflows now automatically generates visual diagrams from your code</p>
<p>Your Workflow is parsed to provide a visual map of the Workflow structure, allowing you to:</p>
<ul>
<li>Understand how steps connect and execute</li>
<li>Visualize loops and nested logic</li>
<li>Follow branching paths for conditional logic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workflows/2026-02-03-workflows-diagram.png" alt="Example diagram" /></p>
<p>You can collapse loops and nested logic to see the high-level flow, or expand them to see every step.</p>
<p>Workflow diagrams are available in beta for all JavaScript and TypeScript Workflows. Find your Workflows in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a> to see their diagrams.</p>


<h2 id="agents-sdk-v0-3-7-workflows-integration-synchronous-state-and-scheduleevery"><a href="/changelog/post/2026-02-03-agents-workflows-integration/">Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()</a></h2>
<p><em>2026-02-03</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings first-class support for <a href="/workflows/">Cloudflare Workflows</a>, synchronous state management, and new scheduling capabilities.</p>
<h4 id="2026-02-03-agents-workflows-integration-cloudflare-workflows-integration">Cloudflare Workflows integration</h4>
<p>Agents excel at real-time communication and state management. Workflows excel at durable execution. Together, they enable powerful patterns where Agents handle WebSocket connections while Workflows handle long-running tasks, retries, and human-in-the-loop flows.</p>
<p>Use the new <code>AgentWorkflow</code> class to define workflows with typed access to your Agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17624.md")</div>
<p>Start workflows from your Agent with <code>runWorkflow()</code> and handle lifecycle events:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17625.md")</div>
<p>Key workflow methods on your Agent:</p>
<ul>
<li><code>runWorkflow(workflowName, params, options?)</code> — Start a workflow with optional metadata</li>
<li><code>getWorkflow(workflowId)</code> / <code>getWorkflows(criteria?)</code> — Query workflows with cursor-based pagination</li>
<li><code>approveWorkflow(workflowId)</code> / <code>rejectWorkflow(workflowId)</code> — Human-in-the-loop approval flows</li>
<li><code>pauseWorkflow()</code>, <code>resumeWorkflow()</code>, <code>terminateWorkflow()</code> — Workflow control</li>
</ul>
<h4 id="2026-02-03-agents-workflows-integration-synchronous-setstate">Synchronous setState()</h4>
<p>State updates are now synchronous with a new <code>validateStateChange()</code> validation hook:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17626.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-scheduleevery-for-recurring-tasks">scheduleEvery() for recurring tasks</h4>
<p>The new <code>scheduleEvery()</code> method enables fixed-interval recurring tasks with built-in overlap prevention:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17627.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-callable-system-improvements">Callable system improvements</h4>
<ul>
<li><strong>Client-side RPC timeout</strong> — Set timeouts on callable method invocations</li>
<li><strong><code>StreamingResponse.error(message)</code></strong> — Graceful stream error signaling</li>
<li><strong><code>getCallableMethods()</code></strong> — Introspection API for discovering callable methods</li>
<li><strong>Connection close handling</strong> — Pending calls are automatically rejected on disconnect</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17628.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-email-and-routing-enhancements">Email and routing enhancements</h4>
<p><strong>Secure email reply routing</strong> — Email replies are now secured with HMAC-SHA256 signed headers, preventing unauthorized routing of emails to agent instances.</p>
<p><strong>Routing improvements:</strong></p>
<ul>
<li><code>basePath</code> option to bypass default URL construction for custom routing</li>
<li>Server-sent identity — Agents send <code>name</code> and <code>agent</code> type on connect</li>
<li>New <code>onIdentity</code> and <code>onIdentityChange</code> callbacks on the client</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17629.md")</div>
<h4 id="2026-02-03-agents-workflows-integration-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre tabindex="0"><code class="language-sh">npm i agents@latest&#10;</code></pre>
<p>For the complete Workflows API reference and patterns, see <a href="/agents/runtime/execution/run-workflows/">Run Workflows</a>.</p>


<h2 id="increased-workflows-instance-and-concurrency-limits"><a href="/changelog/post/2025-10-28-raising-limits/">Increased Workflows instance and concurrency limits</a></h2>
<p><em>2025-10-31</em></p>
<p>We've raised the <a href="/workflows/">Cloudflare Workflows</a> account-level limits for all accounts on the <a href="/workers/platform/pricing/">Workers paid plan</a>:</p>
<ul>
<li><strong>Instance creation rate</strong> increased from 100 workflow instances per 10 seconds to 100 instances per second</li>
<li><strong>Concurrency limit</strong> increased from 4,500 to 10,000 workflow instances per account</li>
</ul>
<p>These increases mean you can create new instances up to 10x faster, and have more workflow instances concurrently executing. To learn more and get started with Workflows, refer to <a href="/workflows/get-started/guide/">the getting started guide</a>.</p>
<p>If your application requires a higher limit, fill out the <a href="/workers/platform/limits/">Limit Increase Request Form</a> or contact your account team. Please refer to <a href="/workflows/reference/pricing/">Workflows pricing</a> for more information.</p>


<h2 id="build-durable-multi-step-applications-in-python-with-workflows-now-in-beta"><a href="/changelog/post/2025-08-22-workflows-python-beta/">Build durable multi-step applications in Python with Workflows (now in beta)</a></h2>
<p><em>2025-08-22</em></p>
<p>You can now build <a href="/workflows/">Workflows</a> using Python. With Python Workflows, you get automatic retries, state persistence, and the ability to run multi-step operations that can span minutes, hours, or weeks using Python’s familiar syntax and the <a href="/workers/languages/python/">Python Workers</a> runtime.</p>
<p>Python Workflows use the same step-based execution model as JavaScript Workflows, but with Python syntax and access to Python’s ecosystem. Python Workflows also enable <a href="/workflows/python/dag/">DAG (Directed Acyclic Graph) workflows</a>, where you can define complex dependencies between steps using the depends parameter.</p>
<p>Here’s a simple example:</p>
<pre tabindex="0"><code class="language-python">from workers import Response, WorkflowEntrypoint&#10;&#10;class PythonWorkflowStarter(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do(&quot;my first step&quot;)&#10;        async def my_first_step():&#10;            &#35; do some work&#10;            return &quot;Hello Python!&quot;&#10;&#10;        await my_first_step()&#10;&#10;        await step.sleep(&quot;my-sleep-step&quot;, &quot;10 seconds&quot;)&#10;&#10;        @step.do(&quot;my second step&quot;)&#10;        async def my_second_step():&#10;            &#35; do some more work&#10;            return &quot;Hello again!&quot;&#10;&#10;        await my_second_step()&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        await self.env.MY_WORKFLOW.create()&#10;        return Response(&quot;Hello Workflow creation!&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17831.md")</aside>
<p>Python Workflows support the same core capabilities as JavaScript Workflows, including sleep scheduling, event-driven workflows, and built-in error handling with configurable retry policies.</p>
<p>To learn more and get started, refer to <a href="/workflows/python/">Python Workflows documentation</a>.</p>


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


<h2 id="workflows-is-now-generally-available"><a href="/changelog/post/2025-04-07-workflows-ga/">Workflows is now Generally Available</a></h2>
<p><em>2025-04-07</em></p>
<p><a href="/workflows/">Workflows</a> is now <em>Generally Available</em> (or &quot;GA&quot;): in short, it's ready for production workloads. Alongside marking Workflows as GA, we've introduced a number of changes during the beta period, including:</p>
<ul>
<li>A new <code>waitForEvent</code> API that allows a Workflow to wait for an event to occur before continuing execution.</li>
<li>Increased concurrency: you can <a href="/changelog/2025-02-25-workflows-concurrency-increased/">run up to 4,500 Workflow instances</a> concurrently — and this will continue to grow.</li>
<li>Improved observability, including new CPU time metrics that allow you to better understand which Workflow instances are consuming the most resources and/or contributing to your bill.</li>
<li>Support for <code>vitest</code> for testing Workflows locally and in CI/CD pipelines.</li>
</ul>
<p>Workflows also supports the new <a href="/changelog/2025-03-25-higher-cpu-limits/">increased CPU limits</a> that apply to Workers, allowing you to run more CPU-intensive tasks (up to 5 minutes of CPU time per instance), not including the time spent waiting on network calls, AI models, or other I/O bound tasks.</p>
<h4 id="2025-04-07-workflows-ga-human-in-the-loop">Human-in-the-loop</h4>
<p>The new <code>step.waitForEvent</code> API allows a Workflow instance to wait on events and data, enabling human-in-the-the-loop interactions, such as approving or rejecting a request, directly handling webhooks from other systems, or pushing event data to a Workflow while it's running.</p>
<p>Because Workflows are just code, you can conditionally execute code based on the result of a <code>waitForEvent</code> call, and/or call <code>waitForEvent</code> multiple times in a single Workflow based on what the Workflow needs.</p>
<p>For example, if you wanted to implement a human-in-the-loop approval process, you could use <code>waitForEvent</code> to wait for a user to approve or reject a request, and then conditionally execute code based on the result.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17829.md")</div>
<p>You can then send a Workflow an event from an external service via HTTP or from within a Worker using the <a href="/workflows/build/workers-api/">Workers API</a> for Workflows:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17830.md")</div>
<p>Read the <a href="https://blog.cloudflare.com/workflows-is-now-generally-available/">GA announcement blog</a> to learn more about what landed as part of the Workflows GA.</p>


<h2 id="concurrent-workflow-instances-limits-increased"><a href="/changelog/post/2025-02-25-workflows-concurrency-increased/">Concurrent Workflow instances limits increased.</a></h2>
<p><em>2025-02-25</em></p>
<p><a href="/workflows/">Workflows</a> now supports up to 4,500 concurrent (running) instances, up from the previous limit of 100. This limit will continue to increase during the Workflows open beta. This increase applies to all users on the Workers Paid plan, and takes effect immediately.</p>
<p>Review the Workflows <a href="/workflows/reference/limits">limits documentation</a> and/or dive into the <a href="/workflows/get-started/guide/">get started guide</a> to start building on Workflows.</p>


<h2 id="build-ai-agents-with-example-prompts"><a href="/changelog/post/2025-02-14-example-ai-prompts/">Build AI Agents with Example Prompts</a></h2>
<p><em>2025-02-14</em></p>
<p>We've added an <a href="/workers/get-started/prompting/">example prompt</a> to help you get started with building AI agents and applications on Cloudflare <a href="/workers/">Workers</a>, including <a href="/workflows/">Workflows</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/kv/">Workers KV</a>.</p>
<p>You can use this prompt with your favorite AI model, including Claude 3.5 Sonnet, OpenAI's o3-mini, Gemini 2.0 Flash, or Llama 3.3 on Workers AI. Models with large context windows will allow you to paste the prompt directly: provide your own prompt within the <code>&lt;user_prompt&gt;&lt;/user_prompt&gt;</code> tags.</p>
<pre tabindex="0"><code class="language-sh">{paste_prompt_here}&#10;&lt;user_prompt&gt;&#10;user: Build an AI agent using Cloudflare Workflows. The Workflow should run when a new GitHub issue is opened on a specific project with the label &#x27;help&#x27; or &#x27;bug&#x27;, and attempt to help the user troubleshoot the issue by calling the OpenAI API with the issue title and description, and a clear, structured prompt that asks the model to suggest 1-3 possible solutions to the issue. Any code snippets should be formatted in Markdown code blocks. Documentation and sources should be referenced at the bottom of the response. The agent should then post the response to the GitHub issue. The agent should run as the provided GitHub bot account.&#10;&lt;/user_prompt&gt;&#10;</code></pre>
<p>This prompt is still experimental, but we encourage you to try it out and <a href="https://github.com/cloudflare/cloudflare-docs/issues/new?template=content.edit.yml">provide feedback</a>.</p>


<h2 id="increased-workflows-limits-and-improved-instance-queueing"><a href="/changelog/post/2025-01-15-workflows-more-steps/">Increased Workflows limits and improved instance queueing.</a></h2>
<p><em>2025-01-15</em></p>
<p><a href="/workflows/">Workflows</a> (beta) now allows you to define up to 1024 <a href="/workflows/build/workers-api/#workflowstep">steps</a>. <code>sleep</code> steps do not count against this limit.</p>
<p>We've also added:</p>
<ul>
<li><code>instanceId</code> as property to the <a href="/workflows/build/workers-api/#workflowevent"><code>WorkflowEvent</code></a> type, allowing you to retrieve the current instance ID from within a running Workflow instance</li>
<li>Improved queueing logic for Workflow instances beyond the current maximum concurrent instances, reducing the cases where instances are stuck in the queued state.</li>
<li>Support for <a href="/workflows/build/workers-api/#pause"><code>pause</code> and <code>resume</code></a> for Workflow instances in a queued state.</li>
</ul>
<p>We're continuing to work on increases to the number of concurrent Workflow instances, steps, and support for a new <code>waitForEvent</code> API over the coming weeks.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 2</span><a class="pagination-next" rel="next" href="/changelog/product/workflows/2/">Next</a></nav>
