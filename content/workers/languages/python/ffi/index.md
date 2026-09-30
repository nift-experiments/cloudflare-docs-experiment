<p>Via <a href="https://pyodide.org/en/stable/">Pyodide</a>, Python Workers provide a <a href="https://en.wikipedia.org/wiki/Foreign_function_interface">Foreign Function Interface (FFI)</a> to JavaScript. This allows you to:</p>
<ul>
<li>Use <a href="/workers/runtime-apis/bindings/">bindings</a> to resources on Cloudflare, including <a href="/workers-ai/">Workers AI</a>, <a href="/vectorize/">Vectorize</a>, <a href="/r2/">R2</a>, <a href="/kv/">KV</a>, <a href="/d1/">D1</a>, <a href="/queues/">Queues</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> and more.</li>
<li>Use JavaScript globals, like <a href="/workers/runtime-apis/request/"><code>Request</code></a>, <a href="/workers/runtime-apis/response/"><code>Response</code></a>, and <a href="/workers/runtime-apis/fetch/"><code>fetch()</code></a>.</li>
<li>Use the full feature set of Cloudflare Workers — if an API is accessible in JavaScript, you can also access it in a Python Worker, writing exclusively Python code.</li>
</ul>
<p>The details of Pyodide's Foreign Function Interface are documented <a href="https://pyodide.org/en/stable/usage/type-conversions.html">here</a>, and Workers written in Python are able to take full advantage of this.</p>
<h2 id="using-bindings-from-python-workers">Using Bindings from Python Workers</h2>
<p>Bindings allow your Worker to interact with resources on the Cloudflare Developer Platform. When you declare a binding on your Worker, you grant it a specific capability, such as being able to read and write files to an <a href="/r2/">R2</a> bucket.</p>
<p>For example, to access a <a href="/kv">KV</a> namespace from a Python Worker, you would declare the following in your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17006.md")
</div>
<p>...and then call <code>.get()</code> on the binding object that is exposed on <code>env</code>:</p>
<pre><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        await self.env.FOO.put(&quot;bar&quot;, &quot;baz&quot;)&#10;        bar = await self.env.FOO.get(&quot;bar&quot;)&#10;        return Response(bar) # returns &quot;baz&quot;&#10;</code></pre>
<h3 id="converting-python-to-javascript">Converting Python to JavaScript</h3>
<p>Occasionally, to interoperate with JavaScript APIs, you may need to convert a Python object to JavaScript. Pyodide provides a <code>to_js</code> function to facilitate this conversion.</p>
<pre><code class="language-python">from js import Object&#10;from pyodide.ffi import to_js as _to_js&#10;&#10;from workers import WorkerEntrypoint, Response&#10;&#10;&#35; to_js converts between Python dictionaries and JavaScript Objects&#10;def to_js(obj):&#10;   return _to_js(obj, dict_converter=Object.fromEntries)&#10;</code></pre>
<p>For more details, see out the <a href="https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.to_js">documentation on <code>pyodide.ffi.to_js</code></a>.</p>
<h2 id="using-javascript-globals-from-python-workers">Using JavaScript globals from Python Workers</h2>
<p>We recommend using the <code>workers</code> module, which is provided by our <code>workers-runtime-sdk</code> package, to access JavaScript globals in a more Pythonic way.
However, if you need to access JavaScript globals directly for any reason, you can import them from the <code>js</code> module.</p>
<p>For example, note how <code>Response</code> is imported from <code>js</code> in the example below:</p>
<pre><code class="language-python">from workers import WorkerEntrypoint&#10;from js import Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response.new(&quot;Hello World!&quot;)&#10;</code></pre>
<p>Refer to the <a href="/workers/languages/python/examples/">Python examples</a> to learn how to call into JavaScript functions from Python, including <code>console.log</code> and logging, providing options to <code>Response</code>, and parsing JSON.</p>
