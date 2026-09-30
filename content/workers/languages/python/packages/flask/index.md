---
cp9:
  canonical: https://developers.cloudflare.com/workers/languages/python/packages/flask/
  description: Run Flask applications in Python Workers.
  full_title: Flask · Cloudflare Workers docs
  head_html: <title>Flask · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Run Flask applications in Python Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/languages/python/packages/flask/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/languages/python/packages/flask/index.md"><meta property="og:title" content="Flask · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run Flask applications in Python Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/languages/python/packages/flask/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/languages/python/packages/flask/#page","headline":"Flask \u00b7 Cloudflare Workers docs","description":"Run Flask applications in Python Workers.","url":"https://developers.cloudflare.com/workers/languages/python/packages/flask/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/languages/python/packages/flask/
  schema: 1
---
<p><a href="https://flask.palletsprojects.com/">Flask</a> is supported in Python Workers.</p>
<p>Flask applications rely on a protocol called the Web Server Gateway Interface
(WSGI). This means that Flask never directly reads or writes to a socket,
instead relying on the WSGI server to communicate.</p>
<p>Python Workers include a <a href="https://github.com/cloudflare/workers-py/blob/main/packages/runtime-sdk/src/workers/wsgi.py">WSGI server</a>
which you can use with Flask applications.</p>
<h2 id="create-a-flask-worker">Create a Flask Worker</h2>
<p>Use this quick start to run a minimal Flask application.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17009.md")
</div>
<h2 id="serve-a-frontend">Serve a frontend</h2>
<p>You can serve any static frontend alongside your flask backend by using <a href="/workers/static-assets/">Workers Static Assets</a>.
Using Static Assets means your frontend files are not bundled inside the Worker itself, keeping the bundle small.</p>
<p>Place your static files in a directory such as <code>./public/</code>. Then configure your
Wrangler file with an <code>assets</code> block that includes a <code>binding</code> and sets
<code>run_worker_first</code> to <code>true</code>. This ensures every request reaches your FastAPI
Worker first, so your API routes take priority over static files.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17010.md")
</div>
<p>The following Worker handles an API route before forwarding other requests. The catch-all handlers return each asset's body, status, and headers:</p>
<pre tabindex="0"><code class="language-python">from flask import Flask, Response, request&#10;from pyodide.ffi import run_sync&#10;from workers import wsgi&#10;&#10;&#10;app = Flask(__name__)&#10;&#10;&#10;@app.get(&quot;/api/hello&quot;)&#10;def api_hello():&#10;    return {&quot;message&quot;: &quot;Hello from the API&quot;}&#10;&#10;&#10;@app.get(&quot;/&quot;)&#10;@app.get(&quot;/&lt;path:path&gt;&quot;)&#10;def frontend(path=&quot;&quot;):&#10;    assets = request.environ[&quot;workers.env&quot;].ASSETS&#10;    asset_response = run_sync(assets.fetch(f&quot;https://assets.local/{path}&quot;))&#10;    body = run_sync(asset_response.bytes())&#10;    return Response(&#10;        body,&#10;        status=asset_response.status,&#10;        headers=asset_response.headers,&#10;    )&#10;&#10;&#10;Default = wsgi.entrypoint(app)&#10;</code></pre>
<p><code>run_sync</code> bridges both asynchronous asset operations into Flask's synchronous
handler. API routes take priority, and unmatched paths are served from
<code>./public/</code>.</p>
<h2 id="more-examples">More examples</h2>
<p>Clone the <code>cloudflare/python-workers-examples</code> repository and run the flask-todo
example there:</p>
<pre tabindex="0"><code class="language-bash">git clone https://github.com/cloudflare/python-workers-examples&#10;cd python-workers-examples/flask-todo&#10;&#35;  See README.md for instructions&#10;</code></pre>
