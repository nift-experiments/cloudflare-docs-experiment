---
cp9:
  canonical: https://developers.cloudflare.com/d1/examples/query-d1-from-python-workers/
  description: Learn how to query D1 from a Python Worker
  full_title: Query D1 from Python Workers · Cloudflare D1 docs
  head_html: <title>Query D1 from Python Workers · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to query D1 from a Python Worker"><link rel="canonical" href="https://developers.cloudflare.com/d1/examples/query-d1-from-python-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/examples/query-d1-from-python-workers/index.md"><meta property="og:title" content="Query D1 from Python Workers · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to query D1 from a Python Worker"><meta property="og:url" content="https://developers.cloudflare.com/d1/examples/query-d1-from-python-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="D1"><meta name="pcx_tags" content="Python"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/examples/query-d1-from-python-workers/#page","headline":"Query D1 from Python Workers \u00b7 Cloudflare D1 docs","description":"Learn how to query D1 from a Python Worker","url":"https://developers.cloudflare.com/d1/examples/query-d1-from-python-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Python"]}</script>
  markdown: true
  noindex: false
  route: /d1/examples/query-d1-from-python-workers/
  schema: 1
---
<p class="article-summary">Learn how to query D1 from a Python Worker</p>
<p>The Cloudflare Workers platform supports <a href="/workers/languages/">multiple languages</a>, including TypeScript, JavaScript, Rust and Python. This guide shows you how to query a D1 database from <a href="/workers/languages/python/">Python</a> and deploy your application globally.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before getting started, you should:</p>
<ol>
<li>Review the <a href="/d1/get-started/">D1 tutorial</a> for TypeScript and JavaScript to learn how to <strong>create a D1 database and configure a Workers project</strong>.</li>
<li>Refer to the <a href="/workers/languages/python/">Python language guide</a> to understand how Python support works on the Workers platform.</li>
<li>Have basic familiarity with the Python language.</li>
</ol>
<p>If you are new to Cloudflare Workers, refer to the <a href="/workers/get-started/guide/">Get started guide</a> first before continuing with this example.</p>
<h2 id="query-from-python">Query from Python</h2>
<p>This example assumes you have an existing D1 database. To allow your Python Worker to query your database, you first need to create a <a href="/workers/runtime-apis/bindings/">binding</a> between your Worker and your D1 database and define this in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>You will need the <code>database_name</code> and <code>database_id</code> for a D1 database. You can use the <code>wrangler</code> CLI to create a new database or fetch the ID for an existing database as follows:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 create my-first-db&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 info some-existing-db&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; ┌───────────────────┬──────────────────────────────────────┐&#10;&#35; │                   │ c89db32e-83f4-4e62-8cd7-7c8f97659029 │&#10;&#35; ├───────────────────┼──────────────────────────────────────┤&#10;&#35; │ name              │ db-enam                              │&#10;&#35; ├───────────────────┼──────────────────────────────────────┤&#10;&#35; │ created_at        │ 2023-06-12T16:52:03.071Z             │&#10;&#35; └───────────────────┴──────────────────────────────────────┘&#10;</code></pre>
<h3 id="1-configure-bindings"><ol>
<li>Configure bindings</li>
</ol></h3>
<p>In your Wrangler file, create a new <code>[[d1_databases]]</code> configuration block and set <code>database_name</code> and <code>database_id</code> to the name and id (respectively) of the D1 database you want to query:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7356.md")
</div>
<p>The value of <code>binding</code> is how you will refer to your database from within your Worker. If you change this, you must change this in your Worker script as well.</p>
<h3 id="2-create-your-python-worker"><ol start="2">
<li>Create your Python Worker</li>
</ol></h3>
<p>To create a Python Worker, create an empty file at <code>src/entry.py</code>, matching the value of <code>main</code> in your Wrangler file with the contents below:</p>
<pre tabindex="0"><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        &#35; Do anything else you&#x27;d like on request here!&#10;&#10;        try:&#10;            &#35; Query D1 - we&#x27;ll list all tables in our database in this example&#10;            results = await self.env.DB.prepare(&quot;PRAGMA table_list&quot;).run()&#10;            &#35; Return a JSON response&#10;            return Response.json(results)&#10;        except Exception as e:&#10;            return Response.json({&quot;error&quot;: &quot;Database query failed&quot;}, status=500)&#10;</code></pre>
<p>The value of <code>binding</code> in your Wrangler file exactly must match the name of the variable in your Python code. This example refers to the database via a <code>DB</code> binding, and queries this binding via <code>await self.env.DB.prepare(...)</code>.</p>
<p>You can then deploy your Python Worker directly:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Example output&#10;&#35;&#10;&#35; Your worker has access to the following bindings:&#10;&#35; - D1 Databases:&#10;&#35;   - DB: db-enam (c89db32e-83f4-4e62-8cd7-7c8f97659029)&#10;&#35; Total Upload: 0.18 KiB / gzip: 0.17 KiB&#10;&#35; Uploaded python-and-d1 (4.93 sec)&#10;&#35; Published python-and-d1 (0.51 sec)&#10;&#35;   https://python-and-d1.YOUR_SUBDOMAIN.workers.dev&#10;&#35; Current Deployment ID: 80b72e19-da82-4465-83a2-c12fb11ccc72&#10;</code></pre>
<p>Your Worker will be available at <code>https://python-and-d1.YOUR_SUBDOMAIN.workers.dev</code>.</p>
<p>If you receive an error deploying:</p>
<ul>
<li>Make sure you have configured your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> with the <code>database_id</code> and <code>database_name</code> of a valid D1 database.</li>
<li>Ensure <code>compatibility_flags = [&quot;python_workers&quot;]</code> is set in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, which is required for Python.</li>
<li>Review the <a href="/workers/observability/errors/">list of error codes</a>, and ensure your code does not throw an uncaught exception.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Refer to <a href="/workers/languages/python/">Workers Python documentation</a> to learn more about how to use Python in Workers.</li>
<li>Review the <a href="/d1/worker-api/">D1 Workers Binding API</a> and how to query D1 databases.</li>
<li>Learn <a href="/d1/best-practices/import-export-data/">how to import data</a> to your D1 database.</li>
</ul>
