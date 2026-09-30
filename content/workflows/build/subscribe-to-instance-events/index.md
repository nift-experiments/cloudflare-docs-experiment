---
cp9:
  canonical: https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/
  description: Use Cloudflare Workflows subscribe method to receive historical and live instance events without polling status.
  full_title: Subscribe to instance events · Cloudflare Workflows docs
  head_html: <title>Subscribe to instance events · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudflare Workflows subscribe method to receive historical and live instance events without polling status."><link rel="canonical" href="https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/index.md"><meta property="og:title" content="Subscribe to instance events · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudflare Workflows subscribe method to receive historical and live instance events without polling status."><meta property="og:url" content="https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/#page","headline":"Subscribe to instance events \u00b7 Cloudflare Workflows docs","description":"Use Cloudflare Workflows subscribe method to receive historical and live instance events without polling status.","url":"https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/build/subscribe-to-instance-events/
  schema: 1
---
<p>Use <code>WorkflowInstance.subscribe()</code> to receive events without polling <a href="/workflows/build/workers-api/#status"><code>status()</code></a>. A subscription first delivers events recorded before you subscribed. After delivering these retained events, the subscription waits for new events as the instance runs.</p>
<p>You can subscribe immediately after creating an instance. To subscribe later, retrieve the instance with <a href="/workflows/build/workers-api/#get"><code>get()</code></a>. Subscriptions remain available during the <a href="/workflows/reference/limits/">instance retention period</a>.</p>
<h2 id="subscribe-to-all-events">Subscribe to all events</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17552.md")
</div>
<p>The subscription ends when the instance emits <code>workflow_completed</code>, <code>workflow_errored</code>, or <code>workflow_terminated</code>. After a terminal event, each later <code>next()</code> call returns <code>done: true</code>.</p>
<h2 id="filter-events">Filter events</h2>
<p>Set <code>filter</code> to limit <code>next()</code> results to specific event types.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17553.md")
</div>
<p>A subscription ends even when its filter excludes a terminal event. In that case, <code>next()</code> returns <code>done: true</code> without the event.</p>
<h2 id="resume-from-a-cursor">Resume from a cursor</h2>
<p>Each event includes an <code>eventId</code>. To resume after a remote procedure call (RPC) fails, store the last processed event ID. Then pass that ID as <code>cursor</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17554.md")
</div>
<p>The cursor identifies the last processed event. The subscription starts with the first event whose <code>eventId</code> is greater than the cursor.</p>
<h2 id="sensitive-outputs">Sensitive outputs</h2>
<p>For steps marked as sensitive, the <code>step_completed</code> event sets <code>output</code> to <code>&quot;[REDACTED]&quot;</code>.</p>
<h2 id="dispose-of-a-subscription">Dispose of a subscription</h2>
<p>A subscription holds a Workers RPC resource. Disposing the subscription stops event delivery, clears its state, and releases its resources.</p>
<p>Declare the subscription with <code>using</code> for automatic disposal when the scope exits, or call <code>subscription[Symbol.dispose]()</code> in a <code>finally</code> block. For more information, refer to <a href="/workers/runtime-apis/rpc/lifecycle/">RPC lifecycle</a>.</p>
<h2 id="event-fields">Event fields</h2>
<p>The public type definition shows the fields available on each event:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17555.md")
</div>
<p>The following sections describe when each event is emitted.</p>
<h3 id="workflow-lifecycle-events">Workflow lifecycle events</h3>
<table>
<thead>
<tr>
<th>Event type</th>
<th>Emitted when</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>workflow_queued</code></td>
<td>The instance enters the execution queue</td>
</tr>
<tr>
<td><code>workflow_started</code></td>
<td>The instance starts</td>
</tr>
<tr>
<td><code>workflow_running</code></td>
<td>The instance starts or resumes execution</td>
</tr>
<tr>
<td><code>workflow_paused</code></td>
<td>The instance pauses</td>
</tr>
<tr>
<td><code>workflow_waiting_for_pause</code></td>
<td>The instance waits for current work before pause</td>
</tr>
<tr>
<td><code>workflow_waiting</code></td>
<td>The instance enters waiting state</td>
</tr>
<tr>
<td><code>workflow_completed</code></td>
<td>The instance completes successfully</td>
</tr>
<tr>
<td><code>workflow_errored</code></td>
<td>The instance ends with an error</td>
</tr>
<tr>
<td><code>workflow_terminated</code></td>
<td>The instance is terminated</td>
</tr>
</tbody>
</table>
<h3 id="step-and-attempt-events">Step and attempt events</h3>
<table>
<thead>
<tr>
<th>Event type</th>
<th>Emitted when</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>step_started</code></td>
<td>A <code>step.do()</code> call starts</td>
</tr>
<tr>
<td><code>step_completed</code></td>
<td>A <code>step.do()</code> call completes</td>
</tr>
<tr>
<td><code>step_errored</code></td>
<td>A <code>step.do()</code> call errors</td>
</tr>
<tr>
<td><code>attempt_started</code></td>
<td>A step attempt starts</td>
</tr>
<tr>
<td><code>attempt_completed</code></td>
<td>A step attempt completes</td>
</tr>
<tr>
<td><code>attempt_errored</code></td>
<td>A step attempt errors</td>
</tr>
</tbody>
</table>
<h3 id="sleep-and-wait-events">Sleep and wait events</h3>
<table>
<thead>
<tr>
<th>Event type</th>
<th>Emitted when</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sleep_started</code></td>
<td>A <code>step.sleep()</code> or <code>step.sleepUntil()</code> call starts</td>
</tr>
<tr>
<td><code>sleep_completed</code></td>
<td>A sleep finishes</td>
</tr>
<tr>
<td><code>wait_started</code></td>
<td>A <code>step.waitForEvent()</code> call starts</td>
</tr>
<tr>
<td><code>wait_completed</code></td>
<td>A matching event reaches <code>step.waitForEvent()</code></td>
</tr>
<tr>
<td><code>wait_timed_out</code></td>
<td>A <code>step.waitForEvent()</code> call times out</td>
</tr>
</tbody>
</table>
<h3 id="rollback-events">Rollback events</h3>
<table>
<thead>
<tr>
<th>Event type</th>
<th>Emitted when</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rollback_started</code></td>
<td>The Workflow starts a rollback</td>
</tr>
<tr>
<td><code>rollback_step_started</code></td>
<td>A rollback handler starts</td>
</tr>
<tr>
<td><code>rollback_step_completed</code></td>
<td>A rollback handler completes</td>
</tr>
<tr>
<td><code>rollback_step_errored</code></td>
<td>A rollback handler errors</td>
</tr>
<tr>
<td><code>rollback_attempt_started</code></td>
<td>A rollback attempt starts</td>
</tr>
<tr>
<td><code>rollback_attempt_completed</code></td>
<td>A rollback attempt completes</td>
</tr>
<tr>
<td><code>rollback_attempt_errored</code></td>
<td>A rollback attempt errors</td>
</tr>
<tr>
<td><code>rollback_completed</code></td>
<td>All required rollback handlers complete</td>
</tr>
<tr>
<td><code>rollback_errored</code></td>
<td>The rollback operation errors</td>
</tr>
</tbody>
</table>
<p>For method signatures and option types, refer to <a href="/workflows/build/workers-api/#subscribe"><code>WorkflowInstance.subscribe()</code></a>.</p>
