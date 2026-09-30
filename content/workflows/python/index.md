<p>Workflow entrypoints can be declared using Python. To achieve this, you can export a <code>WorkflowEntrypoint</code> that runs on the Cloudflare Workers platform.
Refer to <a href="/workers/languages/python">Python Workers</a> for more information about Python on the Workers runtime.</p>
<h2 id="get-started">Get Started</h2>
<p>The main entrypoint for a Python workflow is the <a href="/workflows/build/workers-api/#workflowentrypoint"><code>WorkflowEntrypoint</code></a> class. Your workflow logic should exist inside the <a href="/workflows/build/workers-api/#run"><code>run</code></a> handler.</p>
<pre><code class="language-python">from workers import WorkflowEntrypoint&#10;&#10;class MyWorkflow(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        &#35; steps here&#10;</code></pre>
<p>For example, a Workflow may be defined as:</p>
<pre><code class="language-python">from workers import Response, WorkflowEntrypoint, WorkerEntrypoint&#10;&#10;class PythonWorkflowStarter(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;&#10;        @step.do(&#x27;step1&#x27;)&#10;        async def step_1():&#10;            &#35; does stuff&#10;            print(&#x27;executing step1&#x27;)&#10;&#10;        @step.do(&#x27;step2&#x27;)&#10;        async def step_2():&#10;            &#35; does stuff&#10;            print(&#x27;executing step2&#x27;)&#10;&#10;        await step_1()&#10;        await step_2()&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        await self.env.MY_WORKFLOW.create()&#10;        return Response(&quot;Hello world!&quot;)&#10;</code></pre>
<p>You must add both <code>python_workflows</code> and <code>python_workers</code> compatibility flags to your Wrangler configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17498.md")
</div>
<p>To run a Python Workflow locally, use <a href="/workers/wrangler/">Wrangler</a>, the CLI for Cloudflare Workers:</p>
<pre><code class="language-bash">npx wrangler@latest dev&#10;</code></pre>
<p>To deploy a Python Workflow to Cloudflare, run <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a>:</p>
<pre><code class="language-bash">npx wrangler@latest deploy&#10;</code></pre>
<p>Join the #python-workers channel in the <a href="https://discord.cloudflare.com/">Cloudflare Developers Discord</a> and let us know what you would like to see next.</p>
