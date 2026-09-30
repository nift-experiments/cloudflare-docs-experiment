---
cp9:
  canonical: https://developers.cloudflare.com/workers/languages/python/stdlib/
  description: Python standard library availability and limitations in Cloudflare Workers.
  full_title: Standard Library provided to Python Workers · Cloudflare Workers docs
  head_html: <title>Standard Library provided to Python Workers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Python standard library availability and limitations in Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/languages/python/stdlib/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/languages/python/stdlib/index.md"><meta property="og:title" content="Standard Library provided to Python Workers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Python standard library availability and limitations in Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/languages/python/stdlib/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/languages/python/stdlib/#page","headline":"Standard Library provided to Python Workers \u00b7 Cloudflare Workers docs","description":"Python standard library availability and limitations in Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/languages/python/stdlib/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/languages/python/stdlib/
  schema: 1
---
<p>Workers written in Python are executed by <a href="https://pyodide.org/en/stable/index.html">Pyodide</a>.</p>
<p>Pyodide is a port of CPython to WebAssembly — for the most part it behaves identically to <a href="https://github.com/python">CPython</a> (the reference implementation of Python — commonly referred to as just &quot;Python&quot;).
The majority of the CPython test suite passes when run against Pyodide. For the most part, you shouldn't need to worry about differences in behavior.</p>
<p>The full <a href="https://docs.python.org/3/library/index.html">Python Standard Library</a> is available in Python Workers, with the following exceptions:</p>
<h2 id="excluded-modules">Excluded modules</h2>
<p>The following modules are not available in Python Workers:</p>
<ul>
<li>curses</li>
<li>dbm</li>
<li>ensurepip</li>
<li>fcntl</li>
<li>grp</li>
<li>idlelib</li>
<li>lib2to3</li>
<li>msvcrt</li>
<li>pwd</li>
<li>resource</li>
<li>syslog</li>
<li>termios</li>
<li>tkinter</li>
<li>turtle.py</li>
<li>turtledemo</li>
<li>venv</li>
<li>winreg</li>
<li>winsound</li>
</ul>
<p>The following modules can be imported, but are not functional due to the limitations of the WebAssembly VM.</p>
<ul>
<li>multiprocessing</li>
<li>threading</li>
</ul>
<p>The following are present but cannot be imported due to a dependency on the termios package which has been removed:</p>
<ul>
<li>pty</li>
<li>tty</li>
</ul>
<h2 id="modules-with-limited-functionality">Modules with limited functionality</h2>
<ul>
<li><code>decimal</code>: The decimal module has C (_decimal) and Python (_pydecimal) implementations
with the same functionality. Only the C implementation is available (compiled to WebAssembly)</li>
<li><code>pydoc</code>: Help messages for Python builtins are not available</li>
<li><code>webbrowser</code>: The original webbrowser module is not available.</li>
</ul>
<h2 id="in-memory-filesystem">In-memory filesystem</h2>
<p>Python Workers have access to an ephemeral, in-memory filesystem. You can read and write files using standard Python file I/O (for example, <code>open()</code>, <code>pathlib.Path</code>), but all data is <strong>lost when the Worker isolate is destroyed</strong>. The filesystem is not shared between different isolate instances.</p>
<p>This can be useful for temporary file operations, but should not be relied upon for persistent storage. Use <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, or <a href="/durable-objects/">Durable Objects</a> for durable storage.</p>
