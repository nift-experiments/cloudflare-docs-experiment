---
cp9:
  canonical: https://developers.cloudflare.com/workflows/build/events-and-parameters/
  description: Pass data to Workflows using events and parameters, including request details, database records, and webhook payloads.
  full_title: Events and parameters · Cloudflare Workflows docs
  head_html: <title>Events and parameters · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Pass data to Workflows using events and parameters, including request details, database records, and webhook payloads."><link rel="canonical" href="https://developers.cloudflare.com/workflows/build/events-and-parameters/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/build/events-and-parameters/index.md"><meta property="og:title" content="Events and parameters · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pass data to Workflows using events and parameters, including request details, database records, and webhook payloads."><meta property="og:url" content="https://developers.cloudflare.com/workflows/build/events-and-parameters/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/build/events-and-parameters/#page","headline":"Events and parameters \u00b7 Cloudflare Workflows docs","description":"Pass data to Workflows using events and parameters, including request details, database records, and webhook payloads.","url":"https://developers.cloudflare.com/workflows/build/events-and-parameters/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/build/events-and-parameters/
  schema: 1
---
<p>When a Workflow is triggered, it can receive an optional event. This event can include data that your Workflow can act on, including request details, user data fetched from your database (such as D1 or KV) or from a webhook, or messages from a Queue consumer.</p>
<p>Events are a powerful part of a Workflow, as you often want a Workflow to act on data. Because a given Workflow instance executes durably, events are a useful way to provide a Workflow with data that should be immutable (not changing) and/or represents data the Workflow needs to operate on at that point in time.</p>
<h2 id="pass-data-to-a-workflow">Pass data to a Workflow</h2>
<p>You can pass parameters to a Workflow in three ways:</p>
<ul>
<li>As an optional argument to the <code>create</code> method on a <a href="/workers/wrangler/commands/general/#trigger">Workflow binding</a> when triggering a Workflow from a Worker.</li>
<li>Via the <code>--params</code> flag when using the <code>wrangler</code> CLI to trigger a Workflow.</li>
<li>Via the <code>step.waitForEvent</code> API, which allows a Workflow instance to wait for an event (and optional data) to be received <em>while it is running</em>. Workflow instances can be sent events from external services over HTTP or via the Workers API for Workflows.</li>
</ul>
<p>You can pass any JSON-serializable object as a parameter.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17583.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17584.md")
</div>
<p>To pass parameters via the <code>wrangler</code> command-line interface, pass a JSON string as the second parameter to the <code>workflows trigger</code> sub-command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler@latest workflows trigger workflows-starter &#x27;{&quot;some&quot;:&quot;data&quot;}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">🚀 Workflow instance &quot;57c7913b-8e1d-4a78-a0dd-dce5a0b7aa30&quot; has been queued successfully&#10;</code></pre>
<h3 id="wait-for-events">Wait for events</h3>
<p>A running Workflow can wait for an event (or events) by calling <code>step.waitForEvent</code> within the Workflow, which allows you to send events to the Workflow in one of two ways:</p>
<ol>
<li>Via the <a href="/workflows/build/workers-api/">Workers API binding</a>: call <code>instance.sendEvent</code> to send events to specific workflow instances.</li>
<li>Using the REST API (HTTP API)'s <a href="/api/resources/workflows/subresources/instances/subresources/events/methods/create/">Events endpoint</a>.</li>
</ol>
<p>Because <code>waitForEvent</code> is part of the <code>WorkflowStep</code> API, you can call it multiple times within a Workflow, and use control flow to conditionally wait for an event.</p>
<p>Calling <code>waitForEvent</code> requires you to specify an <code>type</code> (up to 100 characters <sup><a href="#footnote-1">1</a></sup>), which is used to match the corresponding <code>type</code> when sending an event to a Workflow instance.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17582.md")
</aside>
<p>For example, to wait for billing webhook:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17585.md")
</div>
<p>The above example:</p>
<ul>
<li>Calls <code>waitForEvent</code> with a <code>type</code> of <code>stripe-webhook</code> - the corresponding <code>sendEvent</code> call would thus be <code>await instance.sendEvent({type: &quot;stripe-webhook&quot;, payload: webhookPayload})</code>.</li>
<li>Uses a TypeScript <a href="https://www.typescriptlang.org/docs/handbook/2/generics.html">type parameter</a> to type the return value of <code>step.waitForEvent</code> as our <code>IncomingStripeWebhook</code>.</li>
<li>Continues on with the rest of the Workflow.</li>
</ul>
<p>The default timeout for a <code>waitForEvent</code> call is 24 hours, which can be changed by passing <code>{ timeout: WorkflowTimeoutDuration }</code> as the second argument to your <code>waitForEvent</code> call.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17586.md")
</div>
<p>You can specify a timeout between 1 second and up to 365 days.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="timeout-behavior">Timeout behavior</h3>
@markup("md", "content/.markup/bodies/17581.md")
</aside>
<h3 id="send-events-to-running-workflows">Send events to running workflows</h3>
<p>Workflow instances that are waiting on events using the <code>waitForEvent</code> API can be sent events using the <code>instance.sendEvent</code> API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17587.md")
</div>
<ul>
<li>Similar to the <a href="#wait-for-events"><code>waitForEvent</code></a> example in this guide, the <code>type</code> property in our <code>waitForEvent</code> and <code>sendEvent</code> fields must match.</li>
<li>To send multiple events to a Workflow that has multiple <code>waitForEvent</code> calls, call <code>sendEvent</code> with the corresponding <code>type</code> property set (up to 100 characters <sup><a href="#footnote-1">1</a></sup>).</li>
<li>Events can also be sent using the REST API (HTTP API)'s <a href="/api/resources/workflows/subresources/instances/subresources/events/methods/create/">Events endpoint</a>.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="event-timing">Event timing</h3>
@markup("md", "content/.markup/bodies/17579.md")
</aside>
<h2 id="typescript-and-type-parameters">TypeScript and type parameters</h2>
<p>By default, the <code>WorkflowEvent</code> passed to the <code>run</code> method of your Workflow definition has a type that conforms to the following:</p>
<pre tabindex="0"><code class="language-ts">export type WorkflowCronSchedule = {&#10;	/** Cron expression that triggered this event. */&#10;	cron: string;&#10;	/** Timestamp of the scheduled trigger, in milliseconds since the Unix epoch. */&#10;	scheduledTime: number;&#10;};&#10;&#10;export type WorkflowEvent&lt;T&gt; = {&#10;	/** The data passed as the parameter when the Workflow instance was triggered. */&#10;	payload: Readonly&lt;T&gt;;&#10;	/** The timestamp that the Workflow was triggered. */&#10;	timestamp: Date;&#10;	/** ID of the current Workflow instance. */&#10;	instanceId: string;&#10;	/** Name of the current Workflow. */&#10;	workflowName: string;&#10;	/** Metadata for Workflow instances created by a cron schedule. */&#10;	schedule?: WorkflowCronSchedule;&#10;};&#10;</code></pre>
<p>When a Workflow instance is created by a cron schedule configured on a Workflow binding, <code>event.schedule</code> includes the cron expression that created the instance and the scheduled trigger time:</p>
<pre tabindex="0"><code class="language-ts">export class MyWorkflow extends WorkflowEntrypoint&lt;Env&gt; {&#10;	async run(event: WorkflowEvent&lt;unknown&gt;, step: WorkflowStep) {&#10;		if (event.schedule) {&#10;			console.log(event.schedule.cron);&#10;			console.log(new Date(event.schedule.scheduledTime));&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>You can optionally type these events by defining your own type and passing it as a <a href="https://www.typescriptlang.org/docs/handbook/2/generics.html#working-with-generic-type-variables">type parameter</a> to the <code>WorkflowEvent</code>:</p>
<pre tabindex="0"><code class="language-ts">// Define a type that conforms to the events your Workflow instance is&#10;// instantiated with&#10;interface YourEventType {&#10;	userEmail: string;&#10;	createdTimestamp: number;&#10;	metadata?: Record&lt;string, string&gt;;&#10;}&#10;</code></pre>
<p>When you pass your <code>YourEventType</code> to <code>WorkflowEvent</code> as a type parameter, the <code>event.payload</code> property now has the type <code>YourEventType</code> throughout your workflow definition:</p>
<pre tabindex="0"><code class="language-ts">// Import the Workflow definition&#10;import { WorkflowEntrypoint, WorkflowStep, WorkflowEvent} from &#x27;cloudflare:workers&#x27;;&#10;&#10;export class MyWorkflow extends WorkflowEntrypoint {&#10;	// Pass your type as a type parameter to WorkflowEvent&#10;	// The &#x27;payload&#x27; property will have the type of your parameter.&#10;	async run(event: WorkflowEvent&lt;YourEventType&gt;, step: WorkflowStep) {&#10;		let state = await step.do(&quot;my first step&quot;, async () =&gt; {&#10;			// Access your properties via event.payload&#10;          let userEmail = event.payload.userEmail&#10;          let createdTimestamp = event.payload.createdTimestamp&#10;        })&#10;&#10;        await step.do(&quot;my second step&quot;, async () =&gt; { /* your code here */ })&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17578.md")
</aside>
<p>You can also provide a type parameter to the <code>Workflows</code> type when creating (triggering) a Workflow instance using the <code>create</code> method of the <a href="/workflows/build/workers-api/#workflow">Workers API</a>. Note that this does <em>not</em> propagate type information into the Workflow itself, as TypeScript types are a build-time construct.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Match pattern: `^[a-zA-Z0-9_][a-zA-Z0-9-_]*$`</li></ol></section>
