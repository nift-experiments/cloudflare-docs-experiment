---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/
  description: Run different Workflow logic for each user or tenant by combining Workflows with Dynamic Workers.
  full_title: Dynamic Workflows · Cloudflare Dynamic Workers docs
  head_html: <title>Dynamic Workflows · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Run different Workflow logic for each user or tenant by combining Workflows with Dynamic Workers."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/index.md"><meta property="og:title" content="Dynamic Workflows · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run different Workflow logic for each user or tenant by combining Workflows with Dynamic Workers."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Dynamic Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/#page","headline":"Dynamic Workflows \u00b7 Cloudflare Dynamic Workers docs","description":"Run different Workflow logic for each user or tenant by combining Workflows with Dynamic Workers.","url":"https://developers.cloudflare.com/dynamic-workers/usage/dynamic-workflows/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/usage/dynamic-workflows/
  schema: 1
---
<p>You can run a Workflow inside a Dynamic Worker to get durable execution for code that is loaded at runtime. Each step in the Workflow survives failures, can sleep for hours or days, can wait for external events, and resumes exactly where it left off — even if the isolate is recycled between steps.</p>
<p>Because Dynamic Workers are created on-demand, you do not have to register each Workflow up front or manage them individually. Load the code when it is needed, and the Workflows engine handles persistence and retries behind the scenes. This works equally well for one-time executions as it does for long-running, multi-step processes.</p>
<p>For example, you might be building:</p>
<ul>
<li>A SaaS platform where each tenant defines their own automation — onboarding sequences, approval chains, or billing retry logic — and you need each one to run durably without deploying a separate Workflow per customer.</li>
<li>An AI agent framework where agents generate and execute multi-step plans at runtime, and each plan needs to survive restarts, sleep between tool calls, and wait for human approval.</li>
<li>A multi-tenant job system where each customer submits their own processing logic — data transforms, webhook chains, scheduled tasks — and you want every step to persist progress and retry on failure without building your own orchestrator.</li>
</ul>
<p>The <code>@cloudflare/dynamic-workflows</code> library connects your Worker Loader to the Workflows engine so that each Dynamic Worker gets the full power of durable steps (<code>step.do()</code>, <code>step.sleep()</code>, <code>step.waitForEvent()</code>) without you having to build the plumbing yourself.</p>
<p>In this guide, you will use the <code>@cloudflare/dynamic-workflows</code> library to set up a Worker Loader, write a Dynamic Worker with durable steps, and trigger a Workflow instance.</p>
<h2 id="understand-the-model">Understand the model</h2>
<p>This setup has three parts:</p>
<ul>
<li><strong>Worker Loader</strong>: the main Worker you deploy. It receives requests, decides which Dynamic Worker to load, and creates Workflow instances. You write this code.</li>
<li><strong>Dynamic Worker</strong>: the per-tenant code that defines what the Workflow actually does — its steps, sleeps, and event waits. Each Dynamic Worker is loaded on-demand at runtime.</li>
<li><strong>DynamicWorkflow class</strong>: a Workflow entry point created by the library. When the Workflows engine needs to execute a step, this class loads the correct Dynamic Worker for that instance and runs the step inside it.</li>
</ul>
<p><img src="/assets/upstream/images/dynamic-workers/dynamic-workflows.png" alt="Architecture" /></p>
<p>Here is how they work together:</p>
<ul>
<li>The Worker Loader receives a request, loads the tenant's Dynamic Worker, and gives it a Workflow binding tagged with a tenant ID.</li>
<li>The Dynamic Worker calls <code>env.WORKFLOWS.create()</code> to start a new Workflow instance. The tenant ID is saved with the instance automatically.</li>
<li>The Workflows engine runs the steps defined in the Dynamic Worker — <code>step.do()</code>, <code>step.waitForEvent()</code>, <code>step.sleep()</code>. Each step is durable: its result is persisted and will not re-run after it succeeds.</li>
<li>If the isolate is recycled between steps (for example, during a sleep or while waiting for an event), the engine reads the tenant ID back from the instance, reloads the same Dynamic Worker through the Worker Loader, and resumes where it left off.</li>
</ul>
<p>The library provides two functions that handle the wiring between the Worker Loader and the Workflows engine, so you do not have to manually tag requests, parse payloads, or write your own <code>WorkflowEntrypoint</code> subclass.</p>
<ul>
<li><code>wrapWorkflowBinding</code>: creates a Workflow binding tagged with metadata (like <code>{ tenantId }</code>) that you pass to a Dynamic Worker. The library attaches that metadata to every instance the Dynamic Worker creates, so the engine can trace each instance back to the right tenant.</li>
<li><code>createDynamicWorkflowEntrypoint</code>: creates the DynamicWorkflow class that reloads the correct Dynamic Worker when the engine resumes. You give it a callback that takes the metadata and returns the tenant's Workflow class, and the library calls that callback whenever a step needs to run.</li>
</ul>
<h2 id="install-the-library">Install the library</h2>
<p>The library handles the wiring between the Worker Loader and the Workflows engine, so you do not have to manually tag requests, parse payloads, or write your own <code>WorkflowEntrypoint</code> subclass.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/dynamic-workflows</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/dynamic-workflows" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/dynamic-workflows</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/dynamic-workflows" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/dynamic-workflows</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/dynamic-workflows" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/dynamic-workflows</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/dynamic-workflows" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="configure-your-worker-loader">Configure your Worker Loader</h2>
<p>Your Worker Loader needs two <a href="/workers/runtime-apis/bindings/">bindings</a>:</p>
<ul>
<li>A <strong>Worker Loader</strong> binding (<code>LOADER</code>) to load Dynamic Workers at runtime.</li>
<li>A <strong>Workflow binding</strong> (<code>WORKFLOWS</code>) that points to the <code>DynamicWorkflow</code> class. This is the entrypoint the Workflows engine uses to route each instance to the correct Dynamic Worker.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8444.md")
</div>
<h2 id="create-the-worker-loader">Create the Worker Loader</h2>
<p>The Worker Loader is where you connect Dynamic Workers to the Workflows engine. In this file, you define:</p>
<ul>
<li>
<p>How to load a tenant's code: a function that takes a tenant ID, fetches their code, and gives them a Workflow binding. The binding is created with <code>wrapWorkflowBinding</code>, which tags every Workflow instance with the tenant ID so the engine can route back to the right code later.</p>
</li>
<li>
<p>How the engine resumes a Workflow: using <code>createDynamicWorkflowEntrypoint</code>, you define a callback that the engine calls whenever it needs to run a step. The callback receives the tenant ID from the instance metadata and returns the tenant's Workflow class. This is what makes durable execution work across isolate restarts — the engine knows how to reload the right code.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8443.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8445.md")
</div>
<p>Here is what happens when a request arrives:</p>
<ol>
<li>The <code>fetch</code> handler reads the tenant ID from the request header.</li>
<li><code>loadTenant</code> calls <code>env.LOADER.get()</code> to load (or reuse) a Dynamic Worker for that tenant. The Dynamic Worker receives <code>WORKFLOWS: wrapWorkflowBinding({ tenantId })</code> as a binding, which looks and behaves like a normal Workflow binding.</li>
<li>The request is forwarded to the Dynamic Worker's <code>fetch</code> handler, which can now call <code>env.WORKFLOWS.create()</code> to start a Workflow instance.</li>
</ol>
<p>When that Workflow instance later needs to run a step — for example, after a <code>step.sleep()</code> or when a new isolate picks it up — the Workflows engine calls <code>run()</code> on the <code>DynamicWorkflow</code> class. The library reads the <code>tenantId</code> back from the metadata stored on the instance and invokes the callback you passed to <code>createDynamicWorkflowEntrypoint</code>. That callback loads the Dynamic Worker for that tenant and returns its <code>TenantWorkflow</code> class, so the engine can execute the next step in the original code.</p>
<h2 id="write-the-dynamic-worker">Write the Dynamic Worker</h2>
<p>The Dynamic Worker is the code your user writes, and it does not need to know anything about the routing layer. It is a standard Workflow that uses <code>step.do()</code>, <code>step.sleep()</code>, and <code>step.waitForEvent()</code> as normal — from its perspective, <code>env.WORKFLOWS</code> is a regular Workflow binding.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8442.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8446.md")
</div>
<p>Normal Workflows behavior still applies. Workflow IDs, <code>.status()</code>, <code>.pause()</code>, retries, hibernation, and durable steps are unaffected by this architecture. The library only adds the routing between the Worker Loader and the Dynamic Worker.</p>
<h2 id="trigger-a-dynamic-workflow">Trigger a dynamic workflow</h2>
<p>Send a <code>POST</code> request to the Worker Loader with a tenant ID header and a JSON payload. The Worker Loader loads the matching Dynamic Worker, which calls <code>env.WORKFLOWS.create()</code> and returns the new instance ID.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST http://localhost:8787/ \&#10;  &#45;H &quot;x-tenant-id: tenant-42&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;name&quot;: &quot;Alice&quot;}&#x27;&#10;</code></pre>
<h2 id="check-workflow-status">Check workflow status</h2>
<p>Use the instance ID returned from the previous request to check the Workflow status. For more information on the status API, refer to the <a href="/workflows/build/workers-api/">Workers API reference</a>.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;http://localhost:8787/api/status?instanceId=YOUR_INSTANCE_ID&quot;&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://github.com/cloudflare/dynamic-workflows"><code>@cloudflare/dynamic-workflows</code> on GitHub</a></li>
<li><a href="/workflows/build/workers-api/">Workers API</a></li>
<li><a href="/workflows/build/trigger-workflows/">Trigger Workflows</a></li>
<li><a href="/workflows/build/events-and-parameters/">Events and parameters</a></li>
<li><a href="/dynamic-workers/getting-started/">Dynamic Workers getting started</a></li>
<li><a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loaders</a></li>
<li><a href="/dynamic-workers/usage/bindings/">Bindings with Dynamic Workers</a></li>
</ul>
