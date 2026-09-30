---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/concepts/connection-lifecycle/
  description: Understand how connections are managed between Workers, Hyperdrive, and your origin database.
  full_title: Connection lifecycle · Cloudflare Hyperdrive docs
  head_html: <title>Connection lifecycle · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how connections are managed between Workers, Hyperdrive, and your origin database."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/concepts/connection-lifecycle/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/concepts/connection-lifecycle/index.md"><meta property="og:title" content="Connection lifecycle · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how connections are managed between Workers, Hyperdrive, and your origin database."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/concepts/connection-lifecycle/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/concepts/connection-lifecycle/#page","headline":"Connection lifecycle \u00b7 Cloudflare Hyperdrive docs","description":"Understand how connections are managed between Workers, Hyperdrive, and your origin database.","url":"https://developers.cloudflare.com/hyperdrive/concepts/connection-lifecycle/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/concepts/connection-lifecycle/
  schema: 1
---
<p>Understanding how connections work between Workers, Hyperdrive, and your origin database is essential for building efficient applications with Hyperdrive.</p>
<p>By maintaining a connection pool to your database within Cloudflare's network, Hyperdrive reduces seven round-trips to your database before you can even send a query: the TCP handshake (1x), TLS negotiation (3x), and database authentication (3x).</p>
<h2 id="how-connections-are-managed">How connections are managed</h2>
<p>When you use a database client in a Cloudflare Worker, the connection lifecycle works differently than in traditional server environments. Here's what happens:</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-connection-lifecycle.svg" alt="Hyperdrive connection" /></p>
<p>Without Hyperdrive, every Worker invocation would need to establish a new connection directly to your origin database. This connection setup process requires multiple roundtrips across the Internet to complete the TCP handshake, TLS negotiation, and database authentication — that's 7x round trips and added latency before your query can even execute.</p>
<p>Hyperdrive solves this by splitting the connection setup into two parts: a fast edge connection and an optimized path to your database.</p>
<ol>
<li>
<p><strong>Connection setup on the edge</strong>: The database driver in your Worker code establishes a connection to the Hyperdrive instance. This happens at the edge, colocated with your Worker, making it extremely fast to create connections. This is why you use Hyperdrive's special connection string.</p>
</li>
<li>
<p><strong>Single roundtrip across regions</strong>: Since authentication has already been completed at the edge, Hyperdrive only needs a single round trip across regions to your database, instead of the multiple roundtrips that would be incurred during connection setup.</p>
</li>
<li>
<p><strong>Get existing connection from pool</strong>: Hyperdrive uses an existing connection from the pool that is colocated close to your database, minimizing latency.</p>
</li>
<li>
<p><strong>If no available connections, create new</strong>: When needed, new connections are created from a region close to your database to reduce the latency of establishing new connections.</p>
</li>
<li>
<p><strong>Run query</strong>: Your query is executed against the database and results are returned to your Worker through Hyperdrive.</p>
</li>
<li>
<p><strong>Connection teardown</strong>: When your Worker finishes processing the request, the database client connection in your Worker is automatically garbage collected. However, Hyperdrive keeps the connection to your origin database open in the pool, ready to be reused by the next Worker invocation. This means subsequent requests will still perform the fast edge connection setup, but will reuse one of the existing connections from Hyperdrive's pool near your database.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9112.md")
</aside>
<h2 id="cleaning-up-client-connections">Cleaning up client connections</h2>
<p>When your Worker finishes processing a request, the database client is automatically garbage collected and the edge connection to Hyperdrive is cleaned up. Hyperdrive keeps the underlying connection to your origin database open in its pool for reuse.</p>
<p>You do <strong>not</strong> need to call <code>client.end()</code>, <code>sql.end()</code>, <code>connection.end()</code> (or similar) to clean up database clients. Workers-to-Hyperdrive connections are automatically cleaned up when the request or invocation ends, including when a <a href="/workflows/">Workflow</a> or <a href="/queues/">Queue consumer</a> completes, or when a <a href="/durable-objects/">Durable Object</a> hibernates or is evicted when idle.</p>
<pre tabindex="0"><code class="language-ts">import { Client } from &quot;pg&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const client = new Client({&#10;			connectionString: env.HYPERDRIVE.connectionString,&#10;		});&#10;		await client.connect();&#10;&#10;		const result = await client.query(&quot;SELECT * FROM pg_tables&quot;);&#10;&#10;		// No need to call client.end() — Hyperdrive automatically cleans&#10;		// up the client connection when the request ends. The underlying&#10;		// pooled connection to your origin database remains open for reuse.&#10;		return Response.json(result.rows);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="create-database-clients-inside-your-handlers">Create database clients inside your handlers</h3>
@markup("md", "content/.markup/bodies/9111.md")
</aside>
<p>Do not create database clients or connection pools in the global scope. Instead, create a new client inside each handler invocation — Hyperdrive's connection pool ensures this is fast:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9113.md")
</div>
<h2 id="connection-lifecycle-considerations">Connection lifecycle considerations</h2>
<h3 id="durable-objects-and-persistent-connections">Durable Objects and persistent connections</h3>
<p>Unlike regular Workers, <a href="/durable-objects/">Durable Objects</a> can maintain state across multiple requests. If you keep a database client open in a Durable Object, the connection will remain allocated from Hyperdrive's connection pool. Long-lived Durable Objects can exhaust available connections if many objects keep connections open simultaneously.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9110.md")
</aside>
<h3 id="long-running-transactions">Long-running transactions</h3>
<p>Hyperdrive operates in <a href="/hyperdrive/concepts/how-hyperdrive-works/#pooling-mode">transaction pooling mode</a>, where a connection is held for the duration of a transaction. Long-running transactions that contain multiple queries can exhaust Hyperdrive's available connections more quickly because each transaction holds a connection from the pool until it completes.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/9109.md")
</aside>
<p>Refer to <a href="/hyperdrive/platform/limits/">Limits</a> to understand how many connections are available for your Hyperdrive configuration based on your Workers plan.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive works</a></li>
<li><a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a></li>
<li><a href="/hyperdrive/platform/limits/">Limits</a></li>
<li><a href="/durable-objects/">Durable Objects</a></li>
</ul>
