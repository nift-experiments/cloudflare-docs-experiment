---
cp9:
  canonical: https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/
  description: Learn how Python Workers run via Pyodide in V8 isolates and how local development works.
  full_title: How Python Workers Work · Cloudflare Workers docs
  head_html: <title>How Python Workers Work · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Python Workers run via Pyodide in V8 isolates and how local development works."><link rel="canonical" href="https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/index.md"><meta property="og:title" content="How Python Workers Work · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Python Workers run via Pyodide in V8 isolates and how local development works."><meta property="og:url" content="https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/#page","headline":"How Python Workers Work \u00b7 Cloudflare Workers docs","description":"Learn how Python Workers run via Pyodide in V8 isolates and how local development works.","url":"https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/languages/python/how-python-workers-work/
  schema: 1
---
<p>Workers written in Python are executed by <a href="https://pyodide.org/en/stable/index.html">Pyodide</a>.
Pyodide is a <a href="https://github.com/python/cpython">CPython</a> (the reference implementation of Python — commonly referred to as just &quot;Python&quot;) compiled to WebAssembly.</p>
<p>When you write a Python Worker, your code is interpreted directly by Pyodide, within a V8 isolate.
Refer to <a href="/workers/reference/how-workers-works/">How Workers works</a> to learn more.</p>
<h2 id="local-development">Local Development</h2>
<p>A basic Python Worker includes a Python file with a <code>Default</code> class extending <code>WorkerEntrypoint</code>, such as:</p>
<pre tabindex="0"><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(&quot;Hello world!&quot;)&#10;</code></pre>
<p>...and a <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> that points to this <code>.py</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17005.md")
</div>
<p>When you run <code>uv run pywrangler dev</code> to do local dev, the Workers runtime will:</p>
<ol>
<li>Determine which version of Pyodide is required, based on your compatibility date</li>
<li>Install any packages necessary based on your <code>pyproject.toml</code> file</li>
<li>Create a new v8 isolate for your Worker, and automatically inject Pyodide</li>
<li>Serve your Python code using Pyodide</li>
</ol>
<p>There are no extra toolchain or precompilation steps needed. The Python execution environment is provided directly by the Workers runtime, mirroring how Workers written in JavaScript work.</p>
<p>Refer to the <a href="/workers/languages/python/examples/">Python examples</a> to learn how to use Python within Workers.</p>
<h2 id="deployment-lifecycle-and-cold-start-optimizations">Deployment Lifecycle and Cold Start Optimizations</h2>
<p>To reduce cold start times, when you deploy a Python Worker, Cloudflare performs as much of the expensive work as possible upfront, at deploy time. When you run <code>uv run pywrangler deploy</code>, the following happens:</p>
<ol>
<li>Wrangler uploads your Python code and any packages included in your <code>pyproject.toml</code> to the Workers API.</li>
<li>Cloudflare sends your Python code to the Workers runtime to be validated.</li>
<li>Cloudflare creates a new v8 isolate for your Worker, automatically injecting Pyodide.</li>
<li>Cloudflare executes the Worker entrypoint module and everything it imports at top level and then take a snapshot of the Worker’s WebAssembly linear memory. Effectively, we perform the expensive initialization work at deploy time, rather than at runtime.</li>
<li>Cloudflare deploys this snapshot alongside your Worker’s Python code to the Cloudflare network.</li>
</ol>
<p>When a request comes in to your Worker, we load this snapshot and use it to bootstrap your Worker in an isolate, avoiding expensive initialization time:</p>
<p><img src="/assets/upstream/images/workers/languages/python/python-workers-deployment.png" alt="Diagram of how Python Workers are deployed to Cloudflare" /></p>
<p>Refer to the <a href="https://blog.cloudflare.com/python-workers">blog post introducing Python Workers</a> for more detail about performance optimizations and how the Workers runtime will reduce cold starts for Python Workers.</p>
<h2 id="pyodide-and-python-versions">Pyodide and Python versions</h2>
<p>A new version of Python is released every year in August, and a new version of Pyodide is released six (6) months later.
When this new version of Pyodide is published, we will add it to Workers by gating it behind a Compatibility Flag, which is only enabled after a specified Compatibility Date.
This lets us continually provide updates, without risk of breaking changes, extending the commitment we’ve made for JavaScript to Python.</p>
<p>Each Python release has a <a href="https://devguide.python.org/versions/">five (5) year support window</a>.
Once this support window has passed for a given version of Python, security patches are no longer applied, making this version unsafe to rely on.
Following the Workers Runtime policy to never break an application that is live in production,
existing Python Workers on versions outside the support window will continue to work.
However, we do not recommend using Python versions outside the support window for new projects,
and we will not provide patches for issues arising from using these versions.
We also cannot guarantee that these older Python versions won't suffer from degraded performance,
including higher latency or CPU time usage.</p>
