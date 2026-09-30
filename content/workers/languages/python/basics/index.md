---
cp9:
  canonical: https://developers.cloudflare.com/workers/languages/python/basics/
  description: Learn the basics of Python Workers
  full_title: Learn the basics of Python Workers · Cloudflare Workers docs
  head_html: <title>Learn the basics of Python Workers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn the basics of Python Workers"><link rel="canonical" href="https://developers.cloudflare.com/workers/languages/python/basics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/languages/python/basics/index.md"><meta property="og:title" content="Learn the basics of Python Workers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn the basics of Python Workers"><meta property="og:url" content="https://developers.cloudflare.com/workers/languages/python/basics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/languages/python/basics/#page","headline":"Learn the basics of Python Workers \u00b7 Cloudflare Workers docs","description":"Learn the basics of Python Workers","url":"https://developers.cloudflare.com/workers/languages/python/basics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/languages/python/basics/
  schema: 1
---
<h2 id="fetch-handler">Fetch Handler</h2>
<p>As mentioned in the <a href="/workers/languages/python/">introduction to Python Workers</a>, a Python Worker can be as simple as four lines of code:</p>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(&quot;Hello World!&quot;)&#10;</code></pre>
<p>Similar to other Workers, the main entry point for a Python worker is the <a href="/workers/runtime-apis/handlers/fetch"><code>fetch</code> handler</a> which handles incoming requests
sent to the Worker.</p>
<p>In a Python Worker, this handler is placed in a <code>Default</code> class that extends the <code>WorkerEntrypoint</code> class (which you can import from the <code>workers</code> SDK module).</p>
<h2 id="the-request-interface">The <code>Request</code> Interface</h2>
<p>The <code>request</code> parameter passed to your <code>fetch</code> handler is a JavaScript Request object, exposed via the <a href="/workers/languages/python/ffi">foreign function interface (FFI)</a>,
allowing you to access it directly from your Python code.</p>
<p>Let's try editing the worker to accept a POST request. We know from the
<a href="/workers/runtime-apis/request">documentation for <code>Request</code></a> that we can call
<code>await request.json()</code> within an <code>async</code> function to parse the request body as
JSON.</p>
<p>In a Python Worker, you would write:</p>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint, Response&#10;from hello import hello&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        body = await request.json()&#10;        name = body[&quot;name&quot;]&#10;        return Response(hello(name))&#10;</code></pre>
<p>Many other JavaScript APIs are available in Python Workers via the FFI, so you can
call other methods in a similar way.</p>
<p>Once you edit the <code>src/entry.py</code>, Wrangler will automatically restart the local
development server.</p>
<p>Now, if you send a POST request with the appropriate body,
your Worker will respond with a personalized message.</p>
<pre tabindex="0"><code class="language-bash">curl --header &quot;Content-Type: application/json&quot; \&#10;  &#45;-request POST \&#10;  &#45;-data &#x27;{&quot;name&quot;: &quot;Python&quot;}&#x27; http://localhost:8787&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">Hello, Python!&#10;</code></pre>
<h2 id="return-json-responses">Return JSON responses</h2>
<p>To return JSON from a Python Worker, use <code>Response.json()</code>:</p>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        data = {&quot;message&quot;: &quot;Hello&quot;, &quot;status&quot;: &quot;ok&quot;}&#10;        return Response.json(data)&#10;</code></pre>
<h2 id="the-env-attribute">The <code>env</code> Attribute</h2>
<p>The <code>env</code> attribute on the <code>WorkerEntrypoint</code> can be used to access
<a href="/workers/configuration/environment-variables/">environment variables</a>,
<a href="/workers/configuration/secrets/">secrets</a>, and
<a href="/workers/runtime-apis/bindings/">bindings</a>.</p>
<p>For example, let us try setting and using an environment variable in a Python Worker. First, add the environment variable to your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17007.md")
</div>
<p>Then, you can access the <code>API_HOST</code> environment variable via the <code>env</code> parameter:</p>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(self.env.API_HOST)&#10;</code></pre>
<h2 id="modules">Modules</h2>
<p>Python workers can be split across multiple files.</p>
<p>Let's create a new Python file, called <code>src/hello.py</code>:</p>
<pre tabindex="0"><code class="language-python">def hello(name):&#10;    return &quot;Hello, &quot; + name + &quot;!&quot;&#10;</code></pre>
<p>Now, we can modify <code>src/entry.py</code> to make use of the new module.</p>
<pre tabindex="0"><code class="language-python">from hello import hello&#10;from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(hello(&quot;World&quot;))&#10;</code></pre>
<p>Once you edit <code>src/entry.py</code>, <a href="/workers/languages/python/#the-pywrangler-cli-tool"><code>pywrangler</code></a> will automatically detect the change and
reload your Worker.</p>
<h2 id="types-and-autocompletion">Types and Autocompletion</h2>
<p>The <code>workers-runtime-sdk</code> package provides the runtime SDK for Python Workers.
This package is automatically installed and included in your worker when you use <code>pywrangler</code>,
but you can also install it manually to take advantage of type hints and autocompletion
in your IDE.</p>
<p>To enable them, add the <code>workers-runtime-sdk</code> package to your <code>pyproject.toml</code> file.</p>
<pre tabindex="0"><code class="language-toml">dependencies = [&#10;  &quot;workers-runtime-sdk&quot;&#10;]&#10;</code></pre>
<p>Additionally, you can generate types based on your Worker configuration using <code>uv run pywrangler types</code></p>
<p>This includes <code>Env</code> types based on your bindings, module rules, and runtime types based on the <code>compatibility_date</code>
and <code>compatibility_flags</code> in your config file. See</p>
<h2 id="upgrading-pywrangler">Upgrading <code>pywrangler</code></h2>
<p>To upgrade to the latest version of <a href="/workers/languages/python/#the-pywrangler-cli-tool"><code>pywrangler</code></a> globally, run the following command:</p>
<pre tabindex="0"><code class="language-bash">uv tool upgrade workers-py&#10;</code></pre>
<p>To upgrade to the latest version of <code>pywrangler</code> in a specific project, run the following command:</p>
<pre tabindex="0"><code class="language-bash">uv lock --upgrade-package workers-py&#10;</code></pre>
<h2 id="next-up">Next Up</h2>
<ul>
<li>Learn details about local development, deployment, and <a href="/workers/languages/python/how-python-workers-work">how Python Workers work</a>.</li>
<li>Explore the <a href="/workers/languages/python/packages">package</a> docs for instructions on how to use packages with Python Workers.</li>
<li>Understand which parts of the <a href="/workers/languages/python/stdlib">Python Standard Library</a> are supported in Python Workers.</li>
<li>Learn about Python Workers' <a href="/workers/languages/python/ffi">foreign function interface (FFI)</a>, and how to use it to work with <a href="/workers/runtime-apis/bindings">bindings</a> and <a href="/workers/runtime-apis/">Runtime APIs</a>.</li>
</ul>
