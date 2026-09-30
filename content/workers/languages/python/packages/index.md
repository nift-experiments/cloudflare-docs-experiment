---
cp9:
  canonical: https://developers.cloudflare.com/workers/languages/python/packages/
  description: Manage and use Python packages in Cloudflare Workers with Pywrangler.
  full_title: Python packages supported in Cloudflare Workers · Cloudflare Workers docs
  head_html: <title>Python packages supported in Cloudflare Workers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage and use Python packages in Cloudflare Workers with Pywrangler."><link rel="canonical" href="https://developers.cloudflare.com/workers/languages/python/packages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/languages/python/packages/index.md"><meta property="og:title" content="Python packages supported in Cloudflare Workers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage and use Python packages in Cloudflare Workers with Pywrangler."><meta property="og:url" content="https://developers.cloudflare.com/workers/languages/python/packages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/workers/languages/python/packages/#page","headline":"Python packages supported in Cloudflare Workers \u00b7 Cloudflare Workers docs","description":"Manage and use Python packages in Cloudflare Workers with Pywrangler.","url":"https://developers.cloudflare.com/workers/languages/python/packages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/languages/python/packages/
  schema: 1
---
<p><a href="https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler">Pywrangler</a> is a CLI tool for managing packages and Python Workers.
It is meant as a wrapper for wrangler that sets up a full environment for you, including bundling your packages into
your worker bundle on deployment.</p>
<p>To get started, create a pyproject.toml file with the following contents:</p>
<pre tabindex="0"><code class="language-toml">[project]&#10;name = &quot;YourProjectName&quot;&#10;version = &quot;0.1.0&quot;&#10;description = &quot;Add your description here&quot;&#10;requires-python = &quot;&gt;=3.13&quot;&#10;dependencies = [&#10;    &quot;fastapi&quot;&#10;]&#10;&#10;[dependency-groups]&#10;dev = [&#10;	&quot;workers-py&quot;,&#10;	&quot;workers-runtime-sdk&quot;&#10;]&#10;</code></pre>
<p>The above will allow your worker to depend on the <a href="https://fastapi.tiangolo.com/">FastAPI</a> package.</p>
<p>To run the worker locally:</p>
<pre tabindex="0"><code>uv run pywrangler dev&#10;</code></pre>
<p>To deploy your worker:</p>
<pre tabindex="0"><code>uv run pywrangler deploy&#10;</code></pre>
<p>Your dependencies will get bundled with your worker automatically on deployment.</p>
<p>The <code>pywrangler</code> CLI also supports all commands supported by the <code>wrangler</code> tool, for the full list of commands run <code>uv run pywrangler --help</code>.</p>
<h2 id="supported-libraries">Supported Libraries</h2>
<p>Python Workers support pure and <a href="https://peps.python.org/pep-0783/">PyEmscripten</a> Python packages on <a href="https://pypi.org/">PyPI</a>.
Additionally, Python Workers support packages that are included in <a href="https://pyodide.org/en/stable/usage/packages-in-pyodide.html">Pyodide</a>.</p>
<p>WebAssembly support for Python packages is still in early stages, and some packages may not yet be available as PyEmscripten wheels on PyPI.
If a package you would like to use is not yet available, we encourage you to reach out to the package maintainers and request PyEmscripten wheels.
You can also start a thread in the <a href="https://github.com/cloudflare/workerd/discussions/categories/python-packages">Python Packages Discussions</a>
on the Cloudflare Workers Runtime GitHub repository — we would be happy to help you communicate with package maintainers.</p>
