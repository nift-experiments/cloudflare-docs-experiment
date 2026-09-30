---
cp9:
  canonical: https://developers.cloudflare.com/workflows/python/bindings/
  description: Trigger and manage Workflows from Python Workers using FFI bindings to Cloudflare resources.
  full_title: Interact with a Workflow · Cloudflare Workflows docs
  head_html: <title>Interact with a Workflow · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Trigger and manage Workflows from Python Workers using FFI bindings to Cloudflare resources."><link rel="canonical" href="https://developers.cloudflare.com/workflows/python/bindings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/python/bindings/index.md"><meta property="og:title" content="Interact with a Workflow · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Trigger and manage Workflows from Python Workers using FFI bindings to Cloudflare resources."><meta property="og:url" content="https://developers.cloudflare.com/workflows/python/bindings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/python/bindings/#page","headline":"Interact with a Workflow \u00b7 Cloudflare Workflows docs","description":"Trigger and manage Workflows from Python Workers using FFI bindings to Cloudflare resources.","url":"https://developers.cloudflare.com/workflows/python/bindings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/python/bindings/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17500.md")
</aside>
<p>The Python Workers platform leverages <a href="https://en.wikipedia.org/wiki/Foreign_function_interface">FFI</a> to access bindings to Cloudflare resources. Refer to the <a href="/workers/languages/python/ffi/#using-bindings-from-python-workers">bindings</a> documentation for more information.</p>
<p>From the configuration perspective, enabling Python Workflows requires adding the <code>python_workflows</code> compatibility flag to your Wrangler configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17501.md")
</div>
<p>And this is how you use the payload in your workflow:</p>
<pre tabindex="0"><code class="language-python">from workers import WorkflowEntrypoint&#10;&#10;class DemoWorkflowClass(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do(&#x27;step-name&#x27;)&#10;        async def first_step():&#10;            payload = event[&quot;payload&quot;]&#10;            return payload&#10;</code></pre>
<h2 id="workflow">Workflow</h2>
<p>The <code>Workflow</code> binding gives you access to the <a href="/workflows/build/workers-api/#workflow">Workflow</a> class. All its methods are available
on the binding.</p>
<h3 id="create"><code>create</code></h3>
<p>Create (trigger) a new instance of a given Workflow.</p>
<ul>
<li><code>create(options=None)</code>* <code>options</code> - an <strong>optional</strong> dictionary of
options to pass to the workflow instance. Should contain the same keys as the
<a href="/workflows/build/workers-api/#workflowinstancecreateoptions">WorkflowInstanceCreateOptions</a>
type.</li>
</ul>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        event = {&quot;foo&quot;: &quot;bar&quot;}&#10;        await self.env.MY_WORKFLOW.create(params=event)&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
<p>The <code>create</code> method returns a <a href="/workflows/build/workers-api/#workflowinstance"><code>WorkflowInstance</code></a> object, which can be used to query the status of the workflow instance. Note that this is a Javascript object, and not a Python object.</p>
<h3 id="create-batch"><code>create_batch</code></h3>
<p>Create (trigger) a batch of new workflow instances, up to 100 instances at a time. This is useful if you need to create multiple instances at once within the <a href="/workflows/reference/limits/">instance creation limit</a>.</p>
<ul>
<li><code>create_batch(batch)</code>* <code>batch</code> - list of <code>WorkflowInstanceCreateOptions</code> to pass when creating an instance, including a user-provided ID and payload parameters.</li>
</ul>
<p>Each element of the <code>batch</code> list is expected to include both <code>id</code> and <code>params</code> properties:</p>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;			&#35; Create a new batch of 3 Workflow instances, each with its own ID and pass params to the Workflow instances&#10;        instances = [&#10;            {&quot;id&quot;: &quot;id-abc123&quot;, &quot;params&quot;: {&quot;hello&quot;: &quot;world-0&quot;}},&#10;            {&quot;id&quot;: &quot;id-def456&quot;, &quot;params&quot;: {&quot;hello&quot;: &quot;world-1&quot;}},&#10;            {&quot;id&quot;: &quot;id-ghi789&quot;, &quot;params&quot;: {&quot;hello&quot;: &quot;world-2&quot;}},&#10;        ]&#10;        await self.env.MY_WORKFLOW.create_batch(instances)&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
<h3 id="get"><code>get</code></h3>
<p>Get a workflow instance by ID.</p>
<ul>
<li><code>get(id)</code>* <code>id</code> - the ID of the workflow instance to get.</li>
</ul>
<p>Returns a <a href="/workflows/build/workers-api/#workflowinstance"><code>WorkflowInstance</code></a> object, which can be used to query the status of the workflow instance.</p>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        instance = await self.env.MY_WORKFLOW.get(&quot;abc-123&quot;)&#10;&#10;        &#35; FFI methods available for WorkflowInstance&#10;        await instance.status()&#10;        await instance.pause()&#10;        await instance.resume()&#10;        await instance.restart()&#10;        await instance.terminate()&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
<h3 id="send-event"><code>send_event</code></h3>
<p>Send an event to a workflow instance.</p>
<ul>
<li><code>send_event(type, payload)</code>* <code>type</code> - the type of event to send to the
workflow instance. * <code>payload</code> - the payload to send to the workflow instance.</li>
</ul>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        await self.env.MY_WORKFLOW.send_event(type=&quot;my-event-type&quot;, payload={&quot;foo&quot;: &quot;bar&quot;})&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
<h2 id="rest-api-http">REST API (HTTP)</h2>
<p>Refer to the <a href="/api/resources/workflows/subresources/instances/methods/create/">Workflows REST API documentation</a>.</p>
<h2 id="command-line-cli">Command line (CLI)</h2>
<p>Refer to the <a href="/workflows/get-started/guide/">CLI quick start</a> to learn more about how to manage and trigger Workflows via the command-line.</p>
