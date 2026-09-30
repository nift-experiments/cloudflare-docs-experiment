<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17500.md")
</aside>
<p>The Python Workers platform leverages <a href="https://en.wikipedia.org/wiki/Foreign_function_interface">FFI</a> to access bindings to Cloudflare resources. Refer to the <a href="/workers/languages/python/ffi/#using-bindings-from-python-workers">bindings</a> documentation for more information.</p>
<p>From the configuration perspective, enabling Python Workflows requires adding the <code>python_workflows</code> compatibility flag to your Wrangler configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17501.md")
</div>
<p>And this is how you use the payload in your workflow:</p>
<pre><code class="language-python">from workers import WorkflowEntrypoint&#10;&#10;class DemoWorkflowClass(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do(&#x27;step-name&#x27;)&#10;        async def first_step():&#10;            payload = event[&quot;payload&quot;]&#10;            return payload&#10;</code></pre>
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
<pre><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        event = {&quot;foo&quot;: &quot;bar&quot;}&#10;        await self.env.MY_WORKFLOW.create(params=event)&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
<p>The <code>create</code> method returns a <a href="/workflows/build/workers-api/#workflowinstance"><code>WorkflowInstance</code></a> object, which can be used to query the status of the workflow instance. Note that this is a Javascript object, and not a Python object.</p>
<h3 id="create-batch"><code>create_batch</code></h3>
<p>Create (trigger) a batch of new workflow instances, up to 100 instances at a time. This is useful if you need to create multiple instances at once within the <a href="/workflows/reference/limits/">instance creation limit</a>.</p>
<ul>
<li><code>create_batch(batch)</code>* <code>batch</code> - list of <code>WorkflowInstanceCreateOptions</code> to pass when creating an instance, including a user-provided ID and payload parameters.</li>
</ul>
<p>Each element of the <code>batch</code> list is expected to include both <code>id</code> and <code>params</code> properties:</p>
<pre><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;			&#35; Create a new batch of 3 Workflow instances, each with its own ID and pass params to the Workflow instances&#10;        instances = [&#10;            {&quot;id&quot;: &quot;id-abc123&quot;, &quot;params&quot;: {&quot;hello&quot;: &quot;world-0&quot;}},&#10;            {&quot;id&quot;: &quot;id-def456&quot;, &quot;params&quot;: {&quot;hello&quot;: &quot;world-1&quot;}},&#10;            {&quot;id&quot;: &quot;id-ghi789&quot;, &quot;params&quot;: {&quot;hello&quot;: &quot;world-2&quot;}},&#10;        ]&#10;        await self.env.MY_WORKFLOW.create_batch(instances)&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
<h3 id="get"><code>get</code></h3>
<p>Get a workflow instance by ID.</p>
<ul>
<li><code>get(id)</code>* <code>id</code> - the ID of the workflow instance to get.</li>
</ul>
<p>Returns a <a href="/workflows/build/workers-api/#workflowinstance"><code>WorkflowInstance</code></a> object, which can be used to query the status of the workflow instance.</p>
<pre><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        instance = await self.env.MY_WORKFLOW.get(&quot;abc-123&quot;)&#10;&#10;        &#35; FFI methods available for WorkflowInstance&#10;        await instance.status()&#10;        await instance.pause()&#10;        await instance.resume()&#10;        await instance.restart()&#10;        await instance.terminate()&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
<h3 id="send-event"><code>send_event</code></h3>
<p>Send an event to a workflow instance.</p>
<ul>
<li><code>send_event(type, payload)</code>* <code>type</code> - the type of event to send to the
workflow instance. * <code>payload</code> - the payload to send to the workflow instance.</li>
</ul>
<pre><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        await self.env.MY_WORKFLOW.send_event(type=&quot;my-event-type&quot;, payload={&quot;foo&quot;: &quot;bar&quot;})&#10;        return Response.json({&quot;status&quot;: &quot;success&quot;})&#10;</code></pre>
<h2 id="rest-api-http">REST API (HTTP)</h2>
<p>Refer to the <a href="/api/resources/workflows/subresources/instances/methods/create/">Workflows REST API documentation</a>.</p>
<h2 id="command-line-cli">Command line (CLI)</h2>
<p>Refer to the <a href="/workflows/get-started/guide/">CLI quick start</a> to learn more about how to manage and trigger Workflows via the command-line.</p>
