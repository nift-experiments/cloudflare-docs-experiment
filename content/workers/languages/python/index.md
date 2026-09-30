<p>Cloudflare Workers provides a first-class Python experience, including support for:</p>
<ul>
<li>Easy to install and fast-booting <a href="/workers/languages/python/packages">Packages</a>, including <a href="https://fastapi.tiangolo.com/">FastAPI</a>, <a href="https://pypi.org/project/langchain/">Langchain</a>, <a href="https://docs.pydantic.dev/latest/">Pydantic</a> and more.</li>
<li>A robust <a href="/workers/languages/python/ffi">foreign function interface (FFI)</a> that lets you use JavaScript objects and functions directly from Python — including all <a href="/workers/runtime-apis/">Runtime APIs</a></li>
<li>An ecosystem of services on the Workers Platform accessible via <a href="/workers/runtime-apis/bindings/">bindings</a>, including:
<ul>
<li>State storage and databases like <a href="/kv">KV</a>, <a href="/d1">D1</a>, <a href="/durable-objects/">Durable Objects</a></li>
<li>Access to <a href="/workers/configuration/environment-variables/">Environment Variables</a>, <a href="/workers/configuration/secrets/">Secrets</a>, and other Workers using <a href="/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a></li>
<li>AI capabilities with <a href="/workers-ai/">Workers AI</a>, <a href="/vectorize">Vectorize</a></li>
<li>File storage with <a href="/r2">R2</a></li>
<li><a href="/workflows/">Durable Workflows</a>, <a href="/queues/">Queues</a>, and <a href="/workers/runtime-apis/bindings/">more</a></li>
</ul>
</li>
</ul>
<h2 id="introduction">Introduction</h2>
<p>A Python Worker can be as simple as four lines of code:</p>
<pre><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(&quot;Hello World!&quot;)&#10;</code></pre>
<p>Similar to other Workers, the main entry point for a Python worker is the <a href="/workers/runtime-apis/handlers/fetch"><code>fetch</code> handler</a> which handles incoming requests
sent to the Worker.</p>
<p>In a Python Worker, this handler is placed in a <code>Default</code> class that extends the <code>WorkerEntrypoint</code> class (which you can import from the <code>workers</code> SDK module).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17004.md")
</aside>
<h3 id="the-pywrangler-cli-tool">The <code>pywrangler</code> CLI tool</h3>
<p>To run a Python Worker locally, install packages, and deploy it to Cloudflare, you use <a href="https://github.com/cloudflare/workers-py">pywrangler</a>,
the CLI for Python Workers.</p>
<p>To set it up, first, ensure <a href="https://docs.astral.sh/uv/#installation">uv</a> and <a href="https://nodejs.org/en">Node</a> are installed.</p>
<p>Then set up your development environment:</p>
<pre><code class="language-bash">uvx --from workers-py pywrangler init&#10;</code></pre>
<p>This will create a <code>pyproject.toml</code> file with <code>workers-py</code> as a development
dependency. <code>pywrangler init</code> will create a wrangler config file. You can then
run <code>pywrangler</code> with:</p>
<pre><code class="language-bash">uv run pywrangler dev&#10;</code></pre>
<p>To deploy a Python Worker to Cloudflare, run <code>pywrangler deploy</code>:</p>
<pre><code class="language-bash">uv run pywrangler deploy&#10;</code></pre>
<h3 id="python-worker-templates">Python Worker Templates</h3>
<p>When you initialize a new Python Worker project and select from one of many templates:</p>
<pre><code class="language-bash">uv run pywrangler init&#10;</code></pre>
<p>Or you can clone the examples repository to explore more options:</p>
<pre><code class="language-bash">git clone https://github.com/cloudflare/python-workers-examples&#10;cd python-workers-examples/hello&#10;</code></pre>
<h2 id="next-up">Next Up</h2>
<ul>
<li>Learn more about <a href="/workers/languages/python/basics">the basics of Python Workers</a></li>
<li>Learn details about local development, deployment, and <a href="/workers/languages/python/how-python-workers-work">how to Python Workers work</a>.</li>
<li>Explore the <a href="/workers/languages/python/packages">package</a> docs for instructions on how to use packages with Python Workers.</li>
<li>Understand which parts of the <a href="/workers/languages/python/stdlib">Python Standard Library</a> are supported in Python Workers.</li>
<li>Learn about Python Workers' <a href="/workers/languages/python/ffi">foreign function interface (FFI)</a>, and how to use it to work with <a href="/workers/runtime-apis/bindings">bindings</a> and <a href="/workers/runtime-apis/">Runtime APIs</a>.</li>
</ul>
