---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/examples/python-workers/
  description: Connect Python Workers to PostgreSQL and MySQL with Hyperdrive.
  full_title: Python Workers · Cloudflare Hyperdrive docs
  head_html: <title>Python Workers · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Python Workers to PostgreSQL and MySQL with Hyperdrive."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/examples/python-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/examples/python-workers/index.md"><meta property="og:title" content="Python Workers · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Python Workers to PostgreSQL and MySQL with Hyperdrive."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/examples/python-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Hyperdrive,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/examples/python-workers/#page","headline":"Python Workers \u00b7 Cloudflare Hyperdrive docs","description":"Connect Python Workers to PostgreSQL and MySQL with Hyperdrive.","url":"https://developers.cloudflare.com/hyperdrive/examples/python-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/examples/python-workers/
  schema: 1
---
<p>You can use Hyperdrive with <a href="/workers/languages/python/">Python Workers</a>.
To achieve this, you need to set your compatibility date to <code>2026-09-08</code> or later.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="hyperdrive-support-in-python-workers-is-in-beta">Hyperdrive support in Python Workers is in beta.</h3>
@markup("md", "content/.markup/bodies/9022.md")
</aside>
<h2 id="supported-drivers">Supported drivers</h2>
<p>Hyperdrive in Python Workers uses <a href="/workers/runtime-apis/tcp-sockets/#connect">TCP socket support</a> to establish database connections.
While you can use any Python driver that works with TCP connections,
we strongly recommend using the drivers in the tables below, as they have been tested and verified to work with Hyperdrive.</p>
<h3 id="postgresql">PostgreSQL</h3>
<table>
<thead>
<tr>
<th>Driver</th>
<th>Documentation</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>asyncpg</code> (recommended)</td>
<td><a href="https://magicstack.github.io/asyncpg/current/">asyncpg documentation</a></td>
</tr>
<tr>
<td><code>pg8000</code></td>
<td><a href="https://codeberg.org/tlocke/pg8000">pg8000 documentation</a></td>
</tr>
<tr>
<td><code>psycopg</code></td>
<td><a href="https://www.psycopg.org/psycopg3/docs/index.html">psycopg documentation</a></td>
</tr>
</tbody>
</table>
<h3 id="mysql">MySQL</h3>
<table>
<thead>
<tr>
<th>Driver</th>
<th>Documentation</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>aiomysql</code> (recommended)</td>
<td><a href="https://aiomysql.readthedocs.io/en/latest/">aiomysql documentation</a></td>
</tr>
<tr>
<td><code>pymysql</code></td>
<td><a href="https://pymysql.readthedocs.io/">pymysql documentation</a></td>
</tr>
</tbody>
</table>
<h2 id="connect-to-your-database">Connect to your database</h2>
<p>Before you begin, <a href="/workers/languages/python/#the-pywrangler-cli-tool">create a Python Worker</a> and <a href="/hyperdrive/get-started/">create a Hyperdrive configuration</a> for your database.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9027.md")
</div>
<h2 id="limitations-and-compatibility">Limitations and compatibility</h2>
<h3 id="socket-support">Socket support</h3>
<p>TCP socket support in Python Workers internally uses the <a href="/workers/runtime-apis/tcp-sockets/#connect"><code>connect</code></a> API.
While most standard library socket operations are supported, some low-level operations might not work as expected.</p>
<h3 id="concurrency-and-async-safety">Concurrency and async safety</h3>
<p>Socket operations in Python Workers do not block the event loop.
Although Python's native socket operations are synchronous, the underlying TCP socket implementation in Python Workers is asynchronous.
This allows multiple requests to be processed concurrently while one request waits for a socket operation to complete.</p>
<p>To ensure synchronous database operations are serialized, use a lock to prevent concurrent access:</p>
<pre tabindex="0"><code class="language-python">import asyncio&#10;&#10;lock = asyncio.Lock()&#10;&#10;async with lock:&#10;    &#35; Your database operation here&#10;    synchronous_db_operation()&#10;</code></pre>
<h3 id="sqlalchemy-support">SQLAlchemy support</h3>
<p>Currently, only synchronous SQLAlchemy ORMs are supported in Python Workers.
Async SQLAlchemy ORMs are not yet supported due to a lack of greenlet support in the Python Workers environment.</p>
