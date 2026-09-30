---
cp9:
  canonical: https://developers.cloudflare.com/workflows/build/trigger-workflows/
  description: Trigger Workflows from Workers bindings, the REST API, or the Wrangler CLI.
  full_title: Trigger Workflows · Cloudflare Workflows docs
  head_html: <title>Trigger Workflows · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Trigger Workflows from Workers bindings, the REST API, or the Wrangler CLI."><link rel="canonical" href="https://developers.cloudflare.com/workflows/build/trigger-workflows/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/build/trigger-workflows/index.md"><meta property="og:title" content="Trigger Workflows · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Trigger Workflows from Workers bindings, the REST API, or the Wrangler CLI."><meta property="og:url" content="https://developers.cloudflare.com/workflows/build/trigger-workflows/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workflows"><meta name="pcx_tags" content="Bindings"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/build/trigger-workflows/#page","headline":"Trigger Workflows \u00b7 Cloudflare Workflows docs","description":"Trigger Workflows from Workers bindings, the REST API, or the Wrangler CLI.","url":"https://developers.cloudflare.com/workflows/build/trigger-workflows/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Bindings"]}</script>
  markdown: true
  noindex: false
  route: /workflows/build/trigger-workflows/
  schema: 1
---
<p>You can trigger Workflows both programmatically and via the Workflows APIs, including:</p>
<ol>
<li>With <a href="/workers">Workers</a> via HTTP requests in a <code>fetch</code> handler, or bindings from a <code>queue</code> or <code>scheduled</code> handler</li>
<li>On a recurring interval by defining <code>schedules</code> on a Workflow binding in your Wrangler configuration</li>
<li>Using the <a href="/api/resources/workflows/methods/list/">Workflows REST API</a></li>
<li>Via the <a href="/workers/wrangler/commands/workflows/#workflows">wrangler CLI</a> in your terminal</li>
</ol>
<h2 id="workers-api-bindings">Workers API (Bindings)</h2>
<p>You can interact with Workflows programmatically from any Worker script by creating a binding to a Workflow. A Worker can bind to multiple Workflows, including Workflows defined in other Workers projects (scripts) within your account.</p>
<p>You can trigger a Workflow:</p>
<ul>
<li>Directly over HTTP via the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch</code></a> handler</li>
<li>From a <a href="/queues/configuration/javascript-apis/#consumer">Queue consumer</a> inside a <code>queue</code> handler</li>
<li>On a recurring schedule by defining <code>schedules</code> on the Workflow binding in <code>wrangler.jsonc</code></li>
<li>From a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> inside a <code>scheduled</code> handler</li>
<li>Within a <a href="/durable-objects/">Durable Object</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17546.md")
</aside>
<p>To bind to a Workflow from your Workers code, you need to define a <a href="/workers/wrangler/configuration/">binding</a> to a specific Workflow. For example, to bind to the Workflow defined in the <a href="/workflows/get-started/guide/">get started guide</a>, you would configure the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> with the below:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17547.md")
</div>
<p>The <code>binding = &quot;MY_WORKFLOW&quot;</code> line defines the JavaScript variable that our Workflow methods are accessible on, including <code>create</code> (which triggers a new instance) or <code>get</code> (which returns the status of an existing instance).</p>
<h3 id="schedule-a-workflow-directly">Schedule a Workflow directly</h3>
<p>If you want to create Workflow instances on a recurring interval, add a <code>schedules</code> array (up to 100 cron expressions per account) to the Workflow binding in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17548.md")
</div>
<p>Each matching cron expression creates a new Workflow instance automatically. Use this when you want to run a Workflow on a schedule without defining top-level <code>triggers.crons</code> and a separate <code>scheduled</code> handler.</p>
<p>Scheduled instances include the matching cron expression and scheduled trigger time on <code>event.schedule</code>:</p>
<pre tabindex="0"><code class="language-ts">export class MyWorkflow extends WorkflowEntrypoint&lt;Env&gt; {&#10;	async run(event: WorkflowEvent&lt;unknown&gt;, step: WorkflowStep) {&#10;		if (event.schedule) {&#10;			console.log(event.schedule.cron);&#10;			console.log(new Date(event.schedule.scheduledTime));&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>On <a href="/workers/platform/pricing/#workers">Workers Paid</a>, Workflow instances created by <code>schedules</code> can run for up to one hour per cron firing without consuming a Workflow concurrency slot. If the instance pauses or sleeps after that window, the instance yields and enters the normal concurrency queue upon resume. It resumes when a concurrency slot is available.</p>
<p>Use the latest Wrangler release when configuring Workflow schedules. If your local Wrangler schema does not recognize <code>schedules</code> yet, update Wrangler before deploying.</p>
<p>The following example shows how you can manage Workflows from within a Worker, including:</p>
<ul>
<li>Retrieving the status of an existing Workflow instance by its ID</li>
<li>Creating (triggering) a new Workflow instance</li>
<li>Returning the status of a given instance ID</li>
</ul>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;	MY_WORKFLOW: Workflow;&#10;}&#10;&#10;export default {&#10;	async fetch(req: Request, env: Env) {&#10;		// Get instanceId from query parameters&#10;		const instanceId = new URL(req.url).searchParams.get(&quot;instanceId&quot;);&#10;&#10;		// If an ?instanceId=&lt;id&gt; query parameter is provided, fetch the status&#10;		// of an existing Workflow by its ID.&#10;		if (instanceId) {&#10;			let instance = await env.MY_WORKFLOW.get(instanceId);&#10;			return Response.json({&#10;				status: await instance.status(),&#10;			});&#10;		}&#10;&#10;		// Else, create a new instance of our Workflow, passing in any (optional)&#10;		// params and return the ID.&#10;		const newId = crypto.randomUUID();&#10;		let instance = await env.MY_WORKFLOW.create({ id: newId });&#10;		return Response.json({&#10;			id: instance.id,&#10;			details: await instance.status(),&#10;		});&#10;	},&#10;};&#10;</code></pre>
<h3 id="inspect-a-workflow-s-status">Inspect a Workflow's status</h3>
<p>You can inspect the status of any running Workflow instance by calling <code>status</code> against a specific instance ID. This allows you to programmatically inspect whether an instance is queued (waiting to be scheduled), actively running, paused, or errored.</p>
<pre tabindex="0"><code class="language-ts">let instance = await env.MY_WORKFLOW.get(&quot;abc-123&quot;);&#10;let status = await instance.status(); // Returns an InstanceStatus&#10;</code></pre>
<p>The possible values of status are as follows:</p>
<pre tabindex="0"><code class="language-ts">  status:&#10;    | &quot;queued&quot; // means that instance is waiting to be started (see concurrency limits)&#10;    | &quot;running&quot;&#10;    | &quot;paused&quot;&#10;    | &quot;errored&quot;&#10;    | &quot;terminated&quot; // user terminated the instance while it was running&#10;    | &quot;complete&quot;&#10;    | &quot;waiting&quot; // instance is hibernating and waiting for sleep or event to finish&#10;    | &quot;waitingForPause&quot; // instance is finishing the current work to pause&#10;    | &quot;unknown&quot;;&#10;  error?: {&#10;    name: string,&#10;    message: string&#10;  };&#10;	output?: unknown;&#10;	rollback:&#10;		| {&#10;				outcome: &quot;complete&quot; | &quot;failed&quot;;&#10;				error: {&#10;					name: string,&#10;					message: string,&#10;				} | null,&#10;		  }&#10;		| null;&#10;</code></pre>
<p>If your Workflow registers rollback handlers on <code>step.do()</code>, inspect <code>rollback</code> after the instance finishes to see whether the compensating steps completed successfully. While rollback is actively running, the Workers API continues to return <code>status: &quot;running&quot;</code>.</p>
<p>To receive historical and live execution updates without polling, refer to <a href="/workflows/build/subscribe-to-instance-events/">Subscribe to events</a>.</p>
<h3 id="explicitly-pause-a-workflow">Explicitly pause a Workflow</h3>
<p>You can explicitly pause a Workflow instance (and later resume it) by calling <code>pause</code> against a specific instance ID.</p>
<pre tabindex="0"><code class="language-ts">let instance = await env.MY_WORKFLOW.get(&quot;abc-123&quot;);&#10;await instance.pause(); // Returns Promise&lt;void&gt;&#10;</code></pre>
<h3 id="resume-a-workflow">Resume a Workflow</h3>
<p>You can resume a paused Workflow instance by calling <code>resume</code> against a specific instance ID.</p>
<pre tabindex="0"><code class="language-ts">let instance = await env.MY_WORKFLOW.get(&quot;abc-123&quot;);&#10;await instance.resume(); // Returns Promise&lt;void&gt;&#10;</code></pre>
<p>Calling <code>resume</code> on an instance that is not currently paused will have no effect.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17545.md")
</aside>
<h3 id="stop-a-workflow">Stop a Workflow</h3>
<p>You can stop/terminate a Workflow instance by calling <code>terminate</code> against a specific instance ID.</p>
<pre tabindex="0"><code class="language-ts">let instance = await env.MY_WORKFLOW.get(&quot;abc-123&quot;);&#10;await instance.terminate(); // Returns Promise&lt;void&gt;&#10;</code></pre>
<p>To run registered rollback handlers before terminating, pass <code>rollback: true</code>:</p>
<pre tabindex="0"><code class="language-ts">let instance = await env.MY_WORKFLOW.get(&quot;abc-123&quot;);&#10;await instance.terminate({ rollback: true }); // Returns Promise&lt;void&gt;&#10;</code></pre>
<p>You can also run rollback handlers from Wrangler:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows instances terminate &lt;WORKFLOW_NAME&gt; &lt;INSTANCE_ID&gt; --rollback&#10;&#35; For a local Workflows instance during wrangler dev:&#10;npx wrangler workflows instances terminate &lt;WORKFLOW_NAME&gt; &lt;INSTANCE_ID&gt; --local --rollback&#10;</code></pre>
<p>Once stopped/terminated, the Workflow instance <em>cannot</em> be resumed.</p>
<h3 id="restart-a-workflow">Restart a Workflow</h3>
<pre tabindex="0"><code class="language-ts">let instance = await env.MY_WORKFLOW.get(&quot;abc-123&quot;);&#10;await instance.restart(); // Returns Promise&lt;void&gt;&#10;</code></pre>
<p>Restarting an instance will immediately cancel any in-progress steps, erase any intermediate state, and treat the Workflow as if it was run for the first time.</p>
<p>To restart an instance from a specific step instead of the beginning, refer to <a href="/workflows/build/workers-api/#restart"><code>restart</code></a> in the Workers API reference.</p>
<h3 id="delete-workflow-instances">Delete Workflow instances</h3>
<p>Deleting an instance removes its stored state. Deleting a running instance stops its current execution without running rollback handlers.</p>
<p>Delete one instance by calling <code>delete()</code> on its handle:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17549.md")
</div>
<p>If a Workflow deletes its own instance, execution stops during <code>await instance.delete()</code>. Code after the call does not run.</p>
<p>Delete up to 100 instances in one call with <code>deleteBatch()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17550.md")
</div>
<p><code>deleteBatch()</code> accepts between 1 and 100 IDs. Missing IDs are returned as per-instance errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position. If any ID is invalid, the call fails before deleting any instances.</p>
<p>Wrangler accepts one or more instance IDs or a file containing a top-level JSON array of strings. You can combine positional IDs with <code>--filename</code>, up to 100 IDs total. Use <code>latest</code> to delete the most recently created instance.</p>
<pre tabindex="0"><code class="language-json">[&quot;instance-abc&quot;, &quot;instance-def&quot;]&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows instances delete &lt;WORKFLOW_NAME&gt; &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete &lt;WORKFLOW_NAME&gt; &lt;INSTANCE_ID&gt; &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete &lt;WORKFLOW_NAME&gt; latest&#10;npx wrangler workflows instances delete &lt;WORKFLOW_NAME&gt; --filename ./instance-ids.json&#10;&#35; For local Workflow instances during wrangler dev:&#10;npx wrangler workflows instances delete &lt;WORKFLOW_NAME&gt; &lt;INSTANCE_ID&gt; --local&#10;</code></pre>
<p>For the full APIs, refer to <a href="/workflows/build/workers-api/#delete"><code>delete</code></a> and <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch</code></a>.</p>
<h3 id="trigger-a-workflow-from-another-workflow">Trigger a Workflow from another Workflow</h3>
<p>You can create a new Workflow instance from within a step of another Workflow. The parent Workflow will not block waiting for the child Workflow to complete — it continues execution immediately after the child instance is successfully created.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17551.md")
</div>
<p>If the child Workflow fails to start, the step will fail and be retried according to your retry configuration. Once the child instance is successfully created, it runs independently from the parent.</p>
<h2 id="rest-api-http">REST API (HTTP)</h2>
<p>Refer to the <a href="/api/resources/workflows/subresources/instances/methods/create/">Workflows REST API documentation</a>.</p>
<h2 id="command-line-cli">Command line (CLI)</h2>
<p>Refer to the <a href="/workflows/get-started/guide/">CLI quick start</a> to learn more about how to manage and trigger Workflows via the command-line.</p>
