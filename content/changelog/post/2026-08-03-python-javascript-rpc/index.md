<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 3, 2026</time><h2 id="post-title">Python and JavaScript Workers can now call each other via RPC</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now call methods between Python and JavaScript Workers using <a href="/workers/runtime-apis/rpc/">Workers RPC</a>. This works through <a href="/workers/runtime-apis/bindings/service-bindings/rpc/">Service bindings</a> without extra dependencies, schema definitions, or serialization code.</p>
<p>Cross-language RPC calls behave like ordinary function calls. Exceptions propagate to the call site. You can pass <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured cloneable types</a> as parameters or return values, and Pyodide Foreign Function Interface (FFI) automatically converts types between languages.</p>
<h4 id="call-a-typescript-worker-from-python">Call a TypeScript Worker from Python</h4>
<p>Define a method in a TypeScript Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17809.md")</div>
<p>Call it from a Python Worker through a Service binding:</p>
<pre><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;	async def fetch(self, request):&#10;		rpc = self.env.RPC&#10;		result = await rpc.add(42, 144)&#10;		return Response.json({&quot;result&quot;: result})&#10;</code></pre>
<p>Configure the Service binding in the Python Worker's Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17810.md")</div>
<h4 id="call-a-python-worker-from-javascript">Call a Python Worker from JavaScript</h4>
<p>Define a method in a Python Worker:</p>
<pre><code class="language-python">from workers import WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;	async def highlight_code(self, code: str, language: str) -&gt; dict:&#10;		from pygments.formatters import HtmlFormatter&#10;		from pygments import highlight&#10;		from pygments.lexers import get_lexer_by_name&#10;&#10;		lexer = get_lexer_by_name(language, stripall=True)&#10;		formatter = HtmlFormatter(linenos=True, cssclass=&quot;highlight&quot;, style=&quot;monokai&quot;)&#10;		highlighted_html = highlight(code, lexer, formatter)&#10;		css = formatter.get_style_defs(&quot;.highlight&quot;)&#10;&#10;		return {&#10;			&quot;html&quot;: highlighted_html,&#10;			&quot;css&quot;: css&#10;		}&#10;</code></pre>
<p>Call it from a JavaScript Worker through a Service binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17811.md")</div>
<p>Configure the Service binding in the JavaScript Worker's Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17812.md")</div>
<p>For more details on the announcement, read the <a href="https://blog.cloudflare.com/python-workers-rpc/">blog post</a>.</p>
<p>For more information, refer to the <a href="/workers/runtime-apis/rpc/">Workers RPC documentation</a> and the <a href="/workers/languages/python/">Python Workers overview</a>.</p>
</div></article></div>
