---
cp9:
  canonical: https://developers.cloudflare.com/workers/languages/python/packages/fastapi/
  description: Build Python Workers APIs using FastAPI with the built-in ASGI server.
  full_title: FastAPI · Cloudflare Workers docs
  head_html: <title>FastAPI · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Build Python Workers APIs using FastAPI with the built-in ASGI server."><link rel="canonical" href="https://developers.cloudflare.com/workers/languages/python/packages/fastapi/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/languages/python/packages/fastapi/index.md"><meta property="og:title" content="FastAPI · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build Python Workers APIs using FastAPI with the built-in ASGI server."><meta property="og:url" content="https://developers.cloudflare.com/workers/languages/python/packages/fastapi/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/languages/python/packages/fastapi/#page","headline":"FastAPI \u00b7 Cloudflare Workers docs","description":"Build Python Workers APIs using FastAPI with the built-in ASGI server.","url":"https://developers.cloudflare.com/workers/languages/python/packages/fastapi/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/languages/python/packages/fastapi/
  schema: 1
---
<p><a href="https://fastapi.tiangolo.com/">FastAPI</a> is supported in Python Workers.</p>
<p>FastAPI applications use a protocol called the <a href="https://asgi.readthedocs.io/en/latest/">Asynchronous Server Gateway Interface (ASGI)</a>.
This means that FastAPI never reads from or writes to a socket itself. An ASGI application expects to be hooked up to an ASGI server,
typically <a href="https://uvicorn.dev/">uvicorn</a>.
The ASGI server handles all of the raw sockets on the application’s behalf.</p>
<p>The Python Workers provide <a href="https://github.com/cloudflare/workers-py/blob/main/packages/runtime-sdk/src/workers/asgi.py">an ASGI server</a>
that you can use directly in your Python Worker, which lets you use FastAPI in Python Workers.</p>
<h2 id="quick-start">Quick Start</h2>
<p>To get started with FastAPI in Python Workers, follow these steps:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17012.md")
</div>
<h2 id="serve-a-frontend">Serve a frontend</h2>
<p>You can serve any static frontend alongside your FastAPI backend by using <a href="/workers/static-assets/">Workers Static Assets</a>.</p>
<p>This is equivalent to FastAPI's native <a href="https://fastapi.tiangolo.com/tutorial/frontend/"><code>app.frontend()</code></a> method, which serves a static build directory as low-priority routes so that API path operations are checked first. The difference is where the files live: <code>app.frontend()</code> reads files from the local filesystem, while on Workers the static assets are served from Cloudflare's globally distributed asset store through the <code>ASSETS</code> binding. This means your frontend files are not bundled inside the Worker itself, keeping the bundle small.</p>
<p>Place your frontend build output (for example, HTML, CSS, and JavaScript files)
in a directory such as <code>./public/</code>. Then configure your Wrangler file with an
<code>assets</code> block that includes a <code>binding</code> and sets <code>run_worker_first</code> to <code>true</code>.
This ensures every request reaches your FastAPI Worker first, so your API routes
take priority over static files.</p>
<p>Add a catch-all route at the end of your FastAPI app that proxies unmatched requests to the assets binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17013.md")
</div>
<p>Be sure to create a <code>pyproject.toml</code> file to manage your dependencies:</p>
<pre tabindex="0"><code class="language-toml">[project]&#10;name = &quot;my-fastapi-app&quot;&#10;version = &quot;0.1.0&quot;&#10;requires-python = &quot;&gt;=3.13&quot;&#10;dependencies = [&#10;    &quot;fastapi&quot;,&#10;]&#10;&#10;[dependency-groups]&#10;dev = [&#10;    &quot;workers-py&quot;,&#10;    &quot;workers-runtime-sdk&quot;&#10;]&#10;</code></pre>
<p>Then write your worker:</p>
<pre tabindex="0"><code class="language-python">from fastapi import FastAPI, Request&#10;from fastapi.responses import Response&#10;from workers import asgi&#10;&#10;&#10;app = FastAPI()&#10;Default = asgi.entrypoint(app)&#10;&#10;@app.get(&quot;/api/hello&quot;)&#10;async def api_hello():&#10;    return {&quot;message&quot;: &quot;Hello from the API&quot;}&#10;&#10;&#35; Catch-all: proxy everything else to Workers Static Assets.&#10;&#35; This is the Workers equivalent of app.frontend(&quot;/&quot;, directory=&quot;dist&quot;).&#10;@app.get(&quot;/{path:path}&quot;)&#10;async def frontend(path: str, request: Request):&#10;    env = request.scope[&quot;env&quot;]&#10;    asset_url = f&quot;https://assets.local/{path}&quot;&#10;    resp = await env.ASSETS.fetch(asset_url)&#10;    body = await resp.bytes()&#10;    return Response(content=body, status_code=resp.status, headers=resp.headers)&#10;</code></pre>
<p>You can run this worker locally using <code>uv run pywrangler dev</code>.</p>
<p>With this setup, a request to <code>/api/hello</code> is handled by FastAPI, while a request to <code>/index.html</code> or any other path is served from the <code>./public/</code> directory through the assets binding.</p>
<p>For more information on configuring static assets, refer to the <a href="/workers/static-assets/">Workers Static Assets documentation</a>.</p>
<h2 id="more-examples">More examples</h2>
<p>Clone the <code>cloudflare/python-workers-examples</code> repository and run the FastAPI examples there:</p>
<pre tabindex="0"><code class="language-bash">git clone https://github.com/cloudflare/python-workers-examples&#10;cd python-workers-examples/fastapi&#10;uv run pywrangler dev&#10;</code></pre>
