---
cp9:
  canonical: https://developers.cloudflare.com/workflows/reference/limits/
  description: Limits for Cloudflare Workflows, including maximum steps, payload sizes, and instance concurrency.
  full_title: Limits · Cloudflare Workflows docs
  head_html: <title>Limits · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Limits for Cloudflare Workflows, including maximum steps, payload sizes, and instance concurrency."><link rel="canonical" href="https://developers.cloudflare.com/workflows/reference/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/reference/limits/index.md"><meta property="og:title" content="Limits · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Limits for Cloudflare Workflows, including maximum steps, payload sizes, and instance concurrency."><meta property="og:url" content="https://developers.cloudflare.com/workflows/reference/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/reference/limits/#page","headline":"Limits \u00b7 Cloudflare Workflows docs","description":"Limits for Cloudflare Workflows, including maximum steps, payload sizes, and instance concurrency.","url":"https://developers.cloudflare.com/workflows/reference/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/reference/limits/
  schema: 1
---
<p>Limits that apply to authoring, deploying, and running Workflows are detailed below.</p>
<p>Many limits are inherited from those applied to Workers scripts and as documented in the <a href="/workers/platform/limits/">Workers limits</a> documentation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17493.md")
</aside>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workflow class definitions per script</td>
<td>3MB max script size per <a href="/workers/platform/limits/#account-plan-limits">Worker size limits</a></td>
<td>10MB max script size per <a href="/workers/platform/limits/#account-plan-limits">Worker size limits</a></td>
</tr>
<tr>
<td>Total scripts per account</td>
<td>100</td>
<td>500 (shared with <a href="/workers/platform/limits/#account-plan-limits">Worker script limits</a></td>
</tr>
<tr>
<td>Compute time per step <sup><a href="#footnote-3">3</a></sup></td>
<td>10 ms</td>
<td>30 seconds (default) / configurable to 5 minutes of <a href="/workers/platform/limits/#cpu-time">active CPU time</a></td>
</tr>
<tr>
<td>Duration (wall clock) per step <sup><a href="#footnote-3">3</a></sup></td>
<td>Unlimited</td>
<td>Unlimited - for example, waiting on network I/O calls or querying a database</td>
</tr>
<tr>
<td>Maximum non-stream step result per step <sup><a href="#footnote-9">9</a></sup></td>
<td>1MiB (2^20 bytes)</td>
<td>1MiB (2^20 bytes)</td>
</tr>
<tr>
<td>Maximum event <a href="/workflows/build/events-and-parameters/">payload size</a></td>
<td>1MiB (2^20 bytes)</td>
<td>1MiB (2^20 bytes)</td>
</tr>
<tr>
<td>Maximum state that can be persisted per Workflow instance <sup><a href="#footnote-10">10</a></sup></td>
<td>100MB</td>
<td>1GB</td>
</tr>
<tr>
<td>Maximum <code>step.sleep</code> duration</td>
<td>365 days (1 year)</td>
<td>365 days (1 year)</td>
</tr>
<tr>
<td>Maximum steps per Workflow <sup><a href="#footnote-5">5</a></sup></td>
<td>1,024</td>
<td>10,000 (default) / configurable up to 25,000</td>
</tr>
<tr>
<td>Maximum Workflow executions</td>
<td>100,000 per day <a href="/workers/platform/limits/#account-plan-limits">shared with Workers daily limit</a></td>
<td>Unlimited</td>
</tr>
<tr>
<td>Concurrent Workflow instances (executions) per account <sup><a href="#footnote-7">7</a></sup></td>
<td>100</td>
<td>50,000</td>
</tr>
<tr>
<td>Maximum Workflow instance creation rate <sup><a href="#footnote-8">8</a></sup></td>
<td>100 per second <sup><a href="#footnote-6">6</a></sup></td>
<td>300 per second per account <sup><a href="#footnote-6">6</a></sup>, 100 per second per workflow</td>
</tr>
<tr>
<td>Maximum number of <a href="/workflows/observability/metrics-analytics/#event-types">queued instances</a></td>
<td>100,000</td>
<td>2,000,000</td>
</tr>
<tr>
<td>Retention limit for completed Workflow instance state</td>
<td>3 days</td>
<td>30 days <sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td>Maximum length of a Workflow name <sup><a href="#footnote-4">4</a></sup></td>
<td>64 characters</td>
<td>64 characters</td>
</tr>
<tr>
<td>Maximum length of a Workflow instance ID <sup><a href="#footnote-4">4</a></sup></td>
<td>100 characters</td>
<td>100 characters</td>
</tr>
<tr>
<td>Maximum number of subrequests per Workflow instance</td>
<td>50/request</td>
<td>10,000/request (default) / configurable up to 10 million</td>
</tr>
<tr>
<td>Maximum number of retries per step</td>
<td>10,000</td>
<td>10,000</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/17492.md")
</aside>
<p>In JavaScript Workflows, if you need to persist large binary output from a step, return a <code>ReadableStream&lt;Uint8Array&gt;</code>. Streamed outputs still count toward the per-instance storage limit, so store very large or long-lived artifacts in external storage such as <a href="/r2/">R2</a> and return a reference when appropriate.</p>
<h3 id="waiting-instances-do-not-count-towards-instance-concurrency-limits"><code>waiting</code> instances do not count towards instance concurrency limits</h3>
<p>Instances that are in a <code>waiting</code> state — either sleeping via <code>step.sleep</code>, waiting for a retry, or waiting for an event via <code>step.waitForEvent</code> — do <strong>not</strong> count towards concurrency limits. This means you can have millions of Workflow instances sleeping or waiting for events simultaneously, as only actively <code>running</code> instances count toward the 10,000 concurrent instance limit.
However, if there are 10,000 concurrent instances actively running, an instance that has been in a <code>waiting</code> state will be queued instead of resuming immediately.
When an instance transitions from <code>running</code> to <code>waiting</code>, other <code>queued</code> instances will be scheduled (usually the oldest queued instance, on a best-effort basis). This state transition may not occur if the wait duration is very short.</p>
<p>For example, consider a Workflow that does some work, waits for 30 days, and then continues with more work:</p>
<pre tabindex="0"><code class="language-ts">import {&#10;	WorkflowEntrypoint,&#10;	WorkflowStep,&#10;	WorkflowEvent,&#10;} from &quot;cloudflare:workers&quot;;&#10;&#10;type Env = {&#10;	MY_WORKFLOW: Workflow;&#10;};&#10;&#10;export class MyWorkflow extends WorkflowEntrypoint&lt;Env&gt; {&#10;	async run(event: WorkflowEvent&lt;unknown&gt;, step: WorkflowStep) {&#10;		await step.do(&quot;initial work&quot;, async () =&gt; {&#10;			let resp = await fetch(&quot;https://api.cloudflare.com/client/v4/ips&quot;);&#10;			return await resp.json&lt;any&gt;();&#10;		});&#10;&#10;		await step.sleep(&quot;wait 30 days&quot;, &quot;30 days&quot;);&#10;&#10;		await step.do(&#10;			&quot;make a call to write that could maybe, just might, fail&quot;,&#10;			{&#10;				retries: {&#10;					limit: 5,&#10;					delay: &quot;5 seconds&quot;,&#10;					backoff: &quot;exponential&quot;,&#10;				},&#10;				timeout: &quot;15 minutes&quot;,&#10;			},&#10;			async () =&gt; {&#10;				if (Math.random() &gt; 0.5) {&#10;					throw new Error(&quot;API call to $STORAGE_SYSTEM failed&quot;);&#10;				}&#10;			},&#10;		);&#10;	}&#10;}&#10;</code></pre>
<p>While a given Workflow instance is waiting for 30 days, it will transition to the <code>waiting</code> state, allowing other <code>queued</code> instances to run if concurrency limits are reached.</p>
<h3 id="cron-triggered-instances-on-workers-paid">Cron-triggered instances on Workers Paid</h3>
<p>On <a href="/workers/platform/pricing/#workers">Workers Paid</a>, Workflow instances created by <code>schedules</code> can run for up to one hour per cron firing without consuming a Workflow concurrency slot.</p>
<p>After that budget is used, the instance yields and enters the normal concurrency queue. It resumes when a concurrency slot is available. The instance does not fail, time out, or terminate because it used this cron concurrency budget.</p>
<p>The following limits apply to Workflow <code>schedules</code>:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum number of <code>schedules</code> (cron expressions) per account</td>
<td>100</td>
</tr>
<tr>
<td>Maximum length of a cron expression</td>
<td>256 characters</td>
</tr>
</tbody>
</table>
<h3 id="increasing-workflow-step-limits">Increasing Workflow step limits</h3>
<p>Each Workflow instance supports 10,000 steps by default, but this can be increased up to 25,000 steps in your Wrangler configuration. Refer to <a href="/workflows/build/workers-api/#workflow-step-limits">Workflow step limits</a> for more information.</p>
<h3 id="increasing-workflow-cpu-limits">Increasing Workflow CPU limits</h3>
<p>Workflows are Worker scripts, and share the same <a href="/workers/platform/limits/#account-plan-limits">per invocation CPU limits</a> as any Workers do. Note that CPU time is active processing time: not time spent waiting on network requests, storage calls, or other general I/O, which don't count towards your CPU time or Workflows compute consumption.</p>
<p>If your Workflow exceeds its CPU time limit, it will throw the following error:</p>
<pre tabindex="0"><code class="language-txt">Error: Worker exceeded CPU time limit.&#10;</code></pre>
<p>This will appear as <code>exceededCpu</code> in <a href="/workers/wrangler/commands/general/#tail"><code>wrangler tail</code></a> outcomes and as <code>exceededResources</code> in <a href="/workers/observability/metrics-and-analytics/#invocation-statuses">Workers metrics</a>.</p>
<p>By default, the maximum CPU time per Workflow invocation is set to 30 seconds, but can be increased for all invocations associated with a Workflow definition by setting <code>limits.cpu_ms</code> in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17494.md")
</div>
<p>To learn more about CPU time and limits, <a href="/workers/platform/limits/#cpu-time">review the Workers documentation</a>.</p>
<h3 id="increasing-workflow-subrequest-limits">Increasing Workflow subrequest limits</h3>
<p>A subrequest is any request that a Workflow makes to either Internet resources using the <a href="/workers/runtime-apis/fetch/">Fetch API</a> or requests to other Cloudflare services like <a href="/r2/">R2</a>, <a href="/kv/">KV</a>, or <a href="/d1/">D1</a>. Because Workflows are long-running and often make many calls to external services or Cloudflare APIs, they can exceed the default subrequest limit.</p>
<p>If your Workflow exceeds its subrequest limit, it will throw the following error:</p>
<pre tabindex="0"><code class="language-txt">Error: Too many subrequests.&#10;</code></pre>
<p>This will appear as <code>exceededResources</code> in <a href="/workers/observability/metrics-and-analytics/#invocation-statuses">Workers metrics</a> and as <code>exception</code> in <a href="/workers/wrangler/commands/general/#tail"><code>wrangler tail</code></a> outcomes.</p>
<p>By default, the maximum number of subrequests per Workflow instance is 10,000 on Workers Paid plans, but this can be increased up to 10 million by setting <code>limits.subrequests</code> in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17495.md")
</div>
<p>Workers on the free plan remain limited to 50 external subrequests and 1,000 subrequests to Cloudflare services per invocation.</p>
<p>To learn more about subrequest limits, <a href="/workers/platform/limits/#subrequests">review the Workers documentation</a>.</p>
<h2 id="wall-time-limits-by-invocation-type">Wall time limits by invocation type</h2>
<p>Wall time (also called wall-clock time) is the total elapsed time from the start to end of an invocation, including time spent waiting on network requests, I/O, and other asynchronous operations. This is distinct from <a href="/workers/platform/limits/#cpu-time">CPU time</a>, which only measures time the CPU spends actively executing your code.</p>
<p>The following table summarizes the wall time limits for different types of Worker invocations across the developer platform:</p>
<table>
<thead>
<tr>
<th>Invocation type</th>
<th>Wall time limit</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>Incoming HTTP request</td>
<td>Unlimited</td>
<td>No hard limit while the client remains connected. A Worker that is still streaming a response body remains active. <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil()</code></a> extends execution for up to 30 seconds after the response or disconnect.</td>
</tr>
<tr>
<td><a href="/workers/configuration/cron-triggers/">Cron Triggers</a></td>
<td>15 minutes</td>
<td>Scheduled Workers have a maximum wall time of 15 minutes per invocation.</td>
</tr>
<tr>
<td><a href="/queues/configuration/javascript-apis/#consumer">Queue consumers</a></td>
<td>15 minutes</td>
<td>Each consumer invocation has a maximum wall time of 15 minutes.</td>
</tr>
<tr>
<td><a href="/durable-objects/api/alarms/">Durable Object alarm handlers</a></td>
<td>15 minutes</td>
<td>Alarm handler invocations have a maximum wall time of 15 minutes.</td>
</tr>
<tr>
<td><a href="/durable-objects/">Durable Objects</a> (RPC / HTTP)</td>
<td>Unlimited</td>
<td>No hard limit while the caller stays connected to the Durable Object. Durable Objects remain active while a request, RPC call, response stream, WebSocket, or pending I/O is in flight.</td>
</tr>
<tr>
<td><a href="/workflows/">Workflows</a> (per step)</td>
<td>Unlimited</td>
<td>Each step can run for an unlimited wall time. Individual steps are subject to the configured <a href="/workers/platform/limits/#cpu-time">CPU time limit</a>.</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-2">Workflow instance state and logs will be retained for 3 days on the Workers Free plan and for 30 days on the Workers Paid plan.</li>
<li id="footnote-3">A Workflow instance can run forever, as long as each step does not take more than the CPU time limit and the maximum number of steps per Workflow is not reached.</li>
<li id="footnote-4">Match pattern: _```^[a-zA-Z0-9_][a-zA-Z0-9-_]\*$```\_</li>
<li id="footnote-5">`step.sleep` does not count towards the maximum steps limit</li>
<li id="footnote-6">Workflows will return a HTTP 429 rate limited error if you exceed the rate of new Workflow instance creation.</li>
<li id="footnote-7">Only instances with a `running` state count towards the concurrency limits. Instances in the `waiting` state are excluded from these limits. Workers Paid cron-triggered Workflow instances have a separate one-hour cron concurrency budget per firing.</li>
<li id="footnote-8">Each instance created or restarted counts towards this limit</li>
<li id="footnote-9">Applies to non-stream `step.do()` return values. In JavaScript Workflows, `ReadableStream<Uint8Array>` is also a supported serializable return type for larger binary output.</li>
<li id="footnote-10">This total includes persisted bytes from streamed step outputs returned from JavaScript `step.do()` calls.</li></ol></section>
