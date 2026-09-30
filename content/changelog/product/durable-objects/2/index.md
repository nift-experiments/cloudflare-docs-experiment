---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/durable-objects/2/
  description: '2025-05-16'
  full_title: durable-objects changelog - page 2 | Cloudflare Docs
  head_html: <title>durable-objects changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-05-16"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/durable-objects/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="durable-objects changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-05-16"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/durable-objects/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/durable-objects/2/#page","headline":"durable-objects changelog - page 2 | Cloudflare Docs","description":"2025-05-16","url":"https://developers.cloudflare.com/changelog/product/durable-objects/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/durable-objects/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="durable-objects-are-now-supported-in-python-workers"><a href="/changelog/post/2025-05-14-python-worker-durable-object/">Durable Objects are now supported in Python Workers</a></h2>
<p><em>2025-05-16</em></p>
<p>You can now create <a href="/durable-objects/">Durable Objects</a> using
<a href="/workers/languages/python/">Python Workers</a>. A Durable Object is a special kind of
Cloudflare Worker which uniquely combines compute with storage, enabling stateful
long-running applications which run close to your users. For more info see
<a href="/durable-objects/concepts/what-are-durable-objects/">here</a>.</p>
<p>You can define a Durable Object in Python in a similar way to JavaScript:</p>
<pre tabindex="0"><code class="language-python">from workers import DurableObject, Response, WorkerEntrypoint&#10;&#10;from urllib.parse import urlparse&#10;&#10;class MyDurableObject(DurableObject):&#10;    def __init__(self, ctx, env):&#10;        self.ctx = ctx&#10;        self.env = env&#10;&#10;    def fetch(self, request):&#10;        result = self.ctx.storage.sql.exec(&quot;SELECT &#x27;Hello, World!&#x27; as greeting&quot;).one()&#10;        return Response(result.greeting)&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        url = urlparse(request.url)&#10;        id = env.MY_DURABLE_OBJECT.idFromName(url.path)&#10;        stub = env.MY_DURABLE_OBJECT.get(id)&#10;        greeting = await stub.fetch(request.url)&#10;        return greeting&#10;</code></pre>
<p>Define the Durable Object in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17773.md")</div>
<p>Then define the storage backend for your Durable Object:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17774.md")</div>
<p>Then test your new Durable Object locally by running <code>wrangler dev</code>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler dev&#10;</code></pre>
<p>Consult the <a href="/durable-objects/">Durable Objects documentation</a> for more details.</p>


<h2 id="durable-objects-on-workers-free-plan"><a href="/changelog/post/2025-04-07-durable-objects-free-tier/">Durable Objects on Workers Free plan</a></h2>
<p><em>2025-04-07</em></p>
<p>Durable Objects can now be used with zero commitment on the <a href="/workers/platform/pricing/">Workers Free plan</a> allowing you to build AI agents with <a href="/agents/">Agents SDK</a>, collaboration tools, and real-time applications like chat or multiplayer games.</p>
<p>Durable Objects let you build stateful, serverless applications with millions of tiny coordination instances that run your application code alongside (in the same thread!) your durable storage. Each Durable Object can access its own SQLite database through a <a href="/durable-objects/best-practices/access-durable-objects-storage/">Storage API</a>. A Durable Object class is defined in a Worker script encapsulating the Durable Object's behavior when accessed from a Worker. To try the code below, click the button:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/hello-world-do-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<pre tabindex="0"><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;// Durable Object&#10;export class MyDurableObject extends DurableObject {&#10;  ...&#10;	async sayHello(name) {&#10;		return `Hello, ${name}!`;&#10;	}&#10;}&#10;&#10;// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		// Every unique ID refers to an individual instance of the Durable Object class&#10;		const id = env.MY_DURABLE_OBJECT.idFromName(&quot;foo&quot;);&#10;&#10;		// A stub is a client used to invoke methods on the Durable Object&#10;		const stub = env.MY_DURABLE_OBJECT.get(id);&#10;&#10;		// Methods on the Durable Object are invoked via the stub&#10;		const response = await stub.sayHello(&quot;world&quot;);&#10;&#10;		return response;&#10;	},&#10;};&#10;</code></pre>
<p>Free plan <a href="/durable-objects/platform/pricing/">limits</a> apply to Durable Objects compute and storage usage. Limits allow developers to build real-world applications, with every Worker request able to call a Durable Object on the free plan.</p>
<p>For more information, checkout:</p>
<ul>
<li><a href="/durable-objects/concepts/what-are-durable-objects/">Documentation</a></li>
<li><a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object blog</a></li>
</ul>


<h2 id="sqlite-in-durable-objects-ga-with-10gb-storage-per-object"><a href="/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/">SQLite in Durable Objects GA with 10GB storage per object</a></h2>
<p><em>2025-04-07</em></p>
<p>SQLite in Durable Objects is now generally available (GA) with 10GB SQLite database per Durable Object. Since the <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">public beta</a> in September 2024, we've added feature parity and robustness for the SQLite storage backend compared to the preexisting key-value (KV) storage backend for Durable Objects.</p>
<p>SQLite-backed Durable Objects are recommended for all new Durable Object classes, using <code>new_sqlite_classes</code> <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">Wrangler configuration</a>. Only SQLite-backed Durable Objects have access to Storage API's <a href="/durable-objects/api/sqlite-storage-api/#sql-api">SQL</a> and <a href="/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api">point-in-time recovery</a> methods, which provide relational data modeling, SQL querying, and better data management.</p>
<pre tabindex="0"><code class="language-js">export class MyDurableObject extends DurableObject {&#10;  sql: SqlStorage&#10;  constructor(ctx: DurableObjectState, env: Env) {&#10;    super(ctx, env);&#10;    this.sql = ctx.storage.sql;&#10;  }&#10;&#10;  async sayHello() {&#10;    let result = this.sql&#10;      .exec(&quot;SELECT &#x27;Hello, World!&#x27; AS greeting&quot;)&#10;      .one();&#10;    return result.greeting;&#10;  }&#10;}&#10;</code></pre>
<p>KV-backed Durable Objects remain for backwards compatibility, and a migration path from key-value storage to SQL storage for existing Durable Object classes will be offered in the future.</p>
<p>For more details on SQLite storage, checkout <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object blog</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/durable-objects/">Previous</a><span>Page 2 of 2</span></nav>
