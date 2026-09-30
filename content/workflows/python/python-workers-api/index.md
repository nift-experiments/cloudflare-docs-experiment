---
cp9:
  canonical: https://developers.cloudflare.com/workflows/python/python-workers-api/
  description: Reference for the Python Workflows SDK, including WorkflowEntrypoint, step methods, and configuration options.
  full_title: Python Workers API · Cloudflare Workflows docs
  head_html: <title>Python Workers API · Cloudflare Workflows docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for the Python Workflows SDK, including WorkflowEntrypoint, step methods, and configuration options."><link rel="canonical" href="https://developers.cloudflare.com/workflows/python/python-workers-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workflows/python/python-workers-api/index.md"><meta property="og:title" content="Python Workers API · Cloudflare Workflows docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for the Python Workflows SDK, including WorkflowEntrypoint, step methods, and configuration options."><meta property="og:url" content="https://developers.cloudflare.com/workflows/python/python-workers-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workflows"><meta name="algolia_product_filter" content="Workflows"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workflows"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workflows/python/python-workers-api/#page","headline":"Python Workers API \u00b7 Cloudflare Workflows docs","description":"Reference for the Python Workflows SDK, including WorkflowEntrypoint, step methods, and configuration options.","url":"https://developers.cloudflare.com/workflows/python/python-workers-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workflows/python/python-workers-api/
  schema: 1
---
<p>This guide covers the Python Workflows SDK, with instructions on how to build and create workflows using Python.</p>
<h2 id="workflowentrypoint">WorkflowEntrypoint</h2>
<p>The <code>WorkflowEntrypoint</code> is the main entrypoint for a Python workflow. It extends the <code>WorkflowEntrypoint</code> class, and implements the <code>run</code> method.</p>
<pre tabindex="0"><code class="language-python">from workers import WorkflowEntrypoint&#10;&#10;class MyWorkflow(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        &#35; steps here&#10;</code></pre>
<h2 id="workflowstep">WorkflowStep</h2>
<ul>
<li>
<p><code>step.do(name=None, *, concurrent=False, config=None)</code> — a decorator that allows you to define a step in a workflow.</p>
<ul>
<li><code>name</code> — an optional name for the step. If omitted, the function name (<code>func.__name__</code>) is used.</li>
<li><code>concurrent</code> — an optional boolean that indicates whether dependencies for this step can run concurrently.</li>
<li><code>config</code> — an optional <a href="/workflows/build/workers-api/#workflowstepconfig"><code>WorkflowStepConfig</code></a> for configuring <a href="/workflows/build/sleeping-and-retrying/">step specific retry behaviour</a>. This is passed as a Python dictionary and then type translated into a <code>WorkflowStepConfig</code> object.</li>
</ul>
<p>All parameters except <code>name</code> are keyword-only.</p>
</li>
</ul>
<p>Dependencies are resolved implicitly by parameter name. If a step function parameter name matches a previously declared step function, its result is injected into the step.</p>
<p>If you define a <code>ctx</code> parameter, the step context is injected into that argument.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17497.md")
</aside>
<pre tabindex="0"><code class="language-python">from workers import WorkflowEntrypoint&#10;&#10;class MyWorkflow(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do()&#10;        async def my_first_step():&#10;            &#35; do some work&#10;            return &quot;Hello World!&quot;&#10;&#10;        await my_first_step()&#10;</code></pre>
<p>Note that the decorator doesn't make the call to the step, it just returns a callable that can be used to invoke the step. You have to call the callable to make the step run.</p>
<p>When returning state from a step, you must make sure that the returned value is serializable.</p>
<ul>
<li><code>step.sleep(name, duration)</code>
<ul>
<li><code>name</code> — the name of the step.</li>
<li><code>duration</code> — the duration to sleep for, as a <code>number</code> in milliseconds or as a <code>WorkflowDuration</code>-compatible string.</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-python">async def run(self, event, step):&#10;    await step.sleep(&quot;my-sleep-step&quot;, &quot;10 seconds&quot;)&#10;</code></pre>
<ul>
<li><code>step.sleep_until(name, timestamp)</code>
<ul>
<li><code>name</code> — the name of the step.</li>
<li><code>timestamp</code> — a <code>datetime.datetime</code> object or seconds from the Unix epoch to sleep the workflow instance until.</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-python">import datetime&#10;&#10;async def run(self, event, step):&#10;    await step.sleep_until(&quot;my-sleep-step&quot;, datetime.datetime.now() + datetime.timedelta(seconds=10))&#10;</code></pre>
<ul>
<li><code>step.wait_for_event(name, event_type, timeout=&quot;24 hours&quot;)</code>
<ul>
<li><code>name</code> — the name of the step.</li>
<li><code>event_type</code> — the type of event to wait for.</li>
<li><code>timeout</code> — the timeout for the <code>wait_for_event</code> call. The default timeout is 24 hours.</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-python">async def run(self, event, step):&#10;    await step.wait_for_event(&quot;my-wait-for-event-step&quot;, &quot;my-event-type&quot;)&#10;</code></pre>
<h3 id="event-parameter"><code>event</code> parameter</h3>
<p>The <code>event</code> parameter is a dictionary that contains the payload passed to the workflow instance, along with other metadata:</p>
<ul>
<li><code>payload</code> - the payload passed to the workflow instance.</li>
<li><code>timestamp</code> - the timestamp that the workflow was triggered.</li>
<li><code>instanceId</code> - the ID of the current workflow instance.</li>
<li><code>workflowName</code> - the name of the workflow.</li>
</ul>
<h2 id="error-handling">Error Handling</h2>
<p>Workflows semantics allow users to catch exceptions that get thrown to the top level.</p>
<p>Catching specific exceptions within an <code>except</code> block may not work, as some Python errors will not be re-instantiated into the same type of error when they are passed through the RPC layer.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17496.md")
</aside>
<pre tabindex="0"><code class="language-python">async def run(self, event, step):&#10;    async def try_step(fn):&#10;        try:&#10;            return await fn()&#10;        except Exception as e:&#10;            print(f&quot;Successfully caught {type(e).__name__}: {e}&quot;)&#10;&#10;    @step.do(&quot;my_failing&quot;)&#10;    async def my_failing():&#10;        print(&quot;Executing my_failing&quot;)&#10;        raise TypeError(&quot;Intentional error in my_failing&quot;)&#10;&#10;    await try_step(my_failing)&#10;</code></pre>
<h3 id="nonretryableerror">NonRetryableError</h3>
<p>The Python Workflows SDK provides a <code>NonRetryableError</code> class that can be used to signal that a step should not be retried.</p>
<pre tabindex="0"><code class="language-python">from workers.workflows import NonRetryableError&#10;&#10;raise NonRetryableError(message)&#10;</code></pre>
<h2 id="configure-a-workflow-instance">Configure a workflow instance</h2>
<p>You can bind a step to a specific retry policy by passing a <code>WorkflowStepConfig</code> object to the <code>config</code> parameter of the <code>step.do</code> decorator.
With Python Workflows, you need to make sure that your <code>dict</code> respects the <a href="/workflows/build/workers-api/#workflowstepconfig"><code>WorkflowStepConfig</code></a> type.</p>
<pre tabindex="0"><code class="language-python">from workers import WorkflowEntrypoint&#10;&#10;class DemoWorkflowClass(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do(&#x27;step-name&#x27;, config={&quot;retries&quot;: {&quot;limit&quot;: 1, &quot;delay&quot;: &quot;10 seconds&quot;}})&#10;        async def first_step():&#10;            &#35; do some work&#10;            pass&#10;</code></pre>
<h3 id="access-step-context-ctx">Access step context (<code>ctx</code>)</h3>
<p>If you define a <code>ctx</code> parameter, the <a href="/workflows/build/step-context/">step context</a> is injected into that argument. The context is a dictionary with the following keys:</p>
<table>
<thead>
<tr>
<th>Key</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>step</code></td>
<td><code>dict</code></td>
<td>Contains <code>name</code> (the step name) and <code>count</code> (how many times <code>step.do</code> has been called with this name).</td>
</tr>
<tr>
<td><code>attempt</code></td>
<td><code>int</code></td>
<td>The current attempt number (1-indexed).</td>
</tr>
<tr>
<td><code>config</code></td>
<td><code>dict</code></td>
<td>The resolved retry and timeout configuration for this step.</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-python">from workers import WorkflowEntrypoint&#10;&#10;class CtxWorkflow(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do()&#10;        async def read_context(ctx):&#10;            print(ctx[&quot;step&quot;][&quot;name&quot;])    # step name&#10;            print(ctx[&quot;step&quot;][&quot;count&quot;])   # step count&#10;            print(ctx[&quot;attempt&quot;])         # attempt number&#10;            print(ctx[&quot;config&quot;])          # resolved step config&#10;            return ctx[&quot;attempt&quot;]&#10;&#10;        return await read_context()&#10;</code></pre>
<h3 id="create-an-instance-via-binding">Create an instance via binding</h3>
<p>Note that <code>env</code> is a JavaScript object exposed to the Python script via <a href="https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.JsProxy">JsProxy</a>. You can access the binding like you would on a JavaScript worker. Refer to the <a href="/workflows/build/workers-api/#workflow">Workflow binding documentation</a> to learn more about the methods available.</p>
<p>Let's consider the previous binding called <code>MY_WORKFLOW</code>. Here's how you would create a new instance:</p>
<pre tabindex="0"><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        instance = await self.env.MY_WORKFLOW.create()&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
