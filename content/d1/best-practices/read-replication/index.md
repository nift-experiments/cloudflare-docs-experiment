---
cp9:
  canonical: https://developers.cloudflare.com/d1/best-practices/read-replication/
  description: Reduce read latency and scale throughput by replicating D1 databases across regions globally.
  full_title: Global read replication · Cloudflare D1 docs
  head_html: <title>Global read replication · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Reduce read latency and scale throughput by replicating D1 databases across regions globally."><link rel="canonical" href="https://developers.cloudflare.com/d1/best-practices/read-replication/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/best-practices/read-replication/index.md"><meta property="og:title" content="Global read replication · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reduce read latency and scale throughput by replicating D1 databases across regions globally."><meta property="og:url" content="https://developers.cloudflare.com/d1/best-practices/read-replication/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/best-practices/read-replication/#page","headline":"Global read replication \u00b7 Cloudflare D1 docs","description":"Reduce read latency and scale throughput by replicating D1 databases across regions globally.","url":"https://developers.cloudflare.com/d1/best-practices/read-replication/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/best-practices/read-replication/
  schema: 1
---
<p>D1 read replication can lower latency for read queries and scale read throughput by adding read-only database copies, called read replicas, across regions globally closer to clients.</p>
<p>To use read replication, you must use the <a href="/d1/worker-api/d1-database/#withsession">D1 Sessions API</a>, otherwise all queries will continue to be executed only by the primary database.</p>
<p>A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. All queries within a session read from a database instance which is as up-to-date as your query needs it to be. Sessions API ensures <a href="/d1/best-practices/read-replication/#replica-lag-and-consistency-model">sequential consistency</a> for all queries in a session.</p>
<p>To checkout D1 read replication, deploy the following Worker code using Sessions API, which will prompt you to create a D1 database and enable read replication on said database.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tip-place-your-database-further-away-for-the-read-replication-demo">Tip: Place your database further away for the read replication demo</h3>
@markup("md", "content/.markup/bodies/7382.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7383.md")
</div>
<h2 id="primary-database-instance-vs-read-replicas">Primary database instance vs read replicas</h2>
<p><img src="/images/d1/d1-read-replication-concept.png" alt="D1 read replication concept" /></p>
<p>When using D1 without read replication, D1 routes all queries (both read and write) to a specific database instance in <a href="/d1/configuration/data-location/">one location in the world</a>, known as the <span class="nb-glossary-tooltip" title="primary database instance">primary database instance</span>. D1 request latency is dependent on the physical proximity of a user to the primary database instance. Users located further away from the primary database instance experience longer request latency due to <a href="https://www.cloudflare.com/learning/cdn/glossary/round-trip-time-rtt/">network round-trip time</a>.</p>
<p>When using read replication, D1 creates multiple asynchronously replicated copies of the primary database instance, which only serve read requests, called <span class="nb-glossary-tooltip" title="read replica">read replicas</span>. D1 creates the read replicas in <a href="/d1/best-practices/read-replication/#read-replica-locations">multiple regions</a> throughout the world across Cloudflare's network.</p>
<p>Even though a user may be located far away from the primary database instance, they could be close to a read replica. When D1 routes read requests to the read replica instead of the primary database instance, the user enjoys faster responses for their read queries.</p>
<p>D1 asynchronously replicates changes from the primary database instance to all read replicas. This means that at any given time, a read replica may be arbitrarily out of date. The time it takes for the latest committed data in the primary database instance to be replicated to the read replica is known as the <span class="nb-glossary-tooltip" title="replica lag">replica lag</span>. Replica lag and non-deterministic routing to individual replicas can lead to application data consistency issues.
The D1 Sessions API solves this by ensuring sequential consistency.
For more information, refer to <a href="/d1/best-practices/read-replication/#replica-lag-and-consistency-model">replica lag and consistency model</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7381.md")
</aside>
<table>
<thead>
<tr>
<th>Type of database instance</th>
<th>Description</th>
<th>How it handles write queries</th>
<th>How it handles read queries</th>
</tr>
</thead>
<tbody>
<tr>
<td>Primary database instance</td>
<td>The database instance containing the “original” copy of the database</td>
<td>Can serve write queries</td>
<td>Can serve read queries</td>
</tr>
<tr>
<td>Read replica database instance</td>
<td>A database instance containing a copy of the original database which asynchronously receives updates from the primary database instance</td>
<td>Forwards any write queries to the primary database instance</td>
<td>Can serve read queries using its own copy of the database</td>
</tr>
</tbody>
</table>
<h2 id="benefits-of-read-replication">Benefits of read replication</h2>
<p>A system with multiple read replicas located around the world improves the performance of databases:</p>
<ul>
<li>The query latency decreases for users located close to the read replicas. By shortening the physical distance between a the database instance and the user, read query latency decreases, resulting in a faster application.</li>
<li>The read throughput increases by distributing load across multiple replicas. Since multiple database instances are able to serve read-only requests, your application can serve a larger number of queries at any given time.</li>
</ul>
<h2 id="use-sessions-api">Use Sessions API</h2>
<p>By using <a href="/d1/worker-api/d1-database/#withsession">Sessions API</a> for read replication, all of your queries from a single <span class="nb-glossary-tooltip" title="session">session</span> read from a version of the database which ensures sequential consistency. This ensures that the version of the database you are reading is logically consistent even if the queries are handled by different read replicas.</p>
<p>D1 read replication achieves this by attaching a <span class="nb-glossary-tooltip" title="bookmark">bookmark</span> to each query within a session. For more information, refer to <a href="/d1/reference/time-travel/#bookmarks">Bookmarks</a>.</p>
<h3 id="enable-read-replication">Enable read replication</h3>
<p>Read replication can be enabled at the database level in the Cloudflare dashboard. Check <strong>Settings</strong> for your D1 database to view if read replication is enabled.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>D1</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select an existing database > **Settings** > **Enable Read Replication**.
<h3 id="start-a-session-without-constraints">Start a session without constraints</h3>
<p>To create a session from any available database version, use <code>withSession()</code> without any parameters, which will route the first query to any database instance, either the primary database instance or a read replica.</p>
<pre tabindex="0"><code class="language-ts">const session = env.DB.withSession() // synchronous&#10;// query executes on either primary database or a read replica&#10;const result = await session&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run()&#10;</code></pre>
<ul>
<li><code>withSession()</code> is the same as <code>withSession(&quot;first-unconstrained&quot;)</code></li>
<li>This approach is best when your application does not require the latest database version. All queries in a session ensure sequential consistency.</li>
<li>Refer to the <a href="/d1/worker-api/d1-database#withsession">D1 Workers Binding API documentation</a>.</li>
</ul>
<p>{/* #### Example of a D1 session without constraints</p>
<p>Suppose you want to develop a feature for displaying “likes” on a social network application.</p>
<p>The number of likes is a good example of a situation which does not require the latest information all the time. When displaying the number of likes of a post, the first request starts a new D1 session using the constraint <code>first-unconstrained</code>, which will be served by the nearest D1 read replica.</p>
<p>Subsequent interactions on the application should continue using the same session by passing the <code>bookmark</code> from the first query to subsequent requests. This guarantees that all interactions will observe information at least as up-to-date as the initial request, and therefore never show information older than what a user has already observed. The number of likes will be updated with newer counts over time with subsequent requests as D1 asynchronously updates the read replicas with the changes from the primary database.</p>
<pre tabindex="0"><code class="language-js">async function getLikes(postId: string, db: D1Database, bookmark: string | null): GetLikesResult {&#10;  // NOTE: Achieve sequential consistency with given bookmark,&#10;  //       or start a new session that can be served by any replica.&#10;  const session = db.withSession(bookmark ?? &quot;first-unconstrained&quot;);&#10;  const { results } = session&#10;	.prepare(&quot;SELECT * FROM likes WHERE postId = ?&quot;)&#10;	.bind(postId)&#10;	.run();&#10;  return { bookmark: session.getBookmark(), likes: results };&#10;}&#10;</code></pre>
<h3 id="start-a-session-with-all-latest-data">Start a session with all latest data</h3>
<p>To create a session from the latest database version, use <code>withSession(&quot;first-primary&quot;)</code>, which will route the first query to the primary database instance.</p>
<pre tabindex="0"><code class="language-ts">const session = env.DB.withSession(`first-primary`) // synchronous&#10;// query executes on primary database&#10;const result = await session&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run()&#10;</code></pre>
<ul>
<li>This approach is best when your application requires the latest database version. All queries in a session ensure sequential consistency.</li>
<li>Refer to the <a href="/d1/worker-api/d1-database#withsession">D1 Workers Binding API documentation</a>.</li>
</ul>
<p>{/* #### Example of using <code>first-primary</code></p>
<p>Suppose you want to develop a webpage for an electricity provider which lists the electricity bill statements. An assumption here is that each statement is immutable. Once issued, it never changes.</p>
<p>In this scenario, you want the first request of the page to show a list of all the statements and their issue dates. Therefore, the first request starts a new D1 session using the constraint <code>first-primary</code> to get the latest information (ensuring that the list includes all issued bill statements) from the primary database instance.</p>
<p>Then, when opening an individual electricity bill statement, we can continue using the same session by passing the <code>bookmark</code> from the first query to subsequent requests. Since each bill statement is immutable, any bill statement listed from the first query is guaranteed to be available in subsequent requests using the same session.</p>
<pre tabindex="0"><code class="language-ts">async function listBillStatements(accountId: string, db: D1Database): Promise&lt;ListBillStatementsResult&gt; {&#10;	const session = db.withSession(&#x27;first-primary&#x27;);&#10;	const { results } = (await session.prepare(&#x27;SELECT * FROM bills WHERE accountId = ?&#x27;).bind(accountId).run()) as unknown as {&#10;		results: Bill[];&#10;	};&#10;	return { bookmark: session.getBookmark() ?? &#x27;first-unconstrained&#x27;, bills: results };&#10;}&#10;&#10;async function getBillStatement(accountId: string, billId: string, bookmark: string, db: D1Database): Promise&lt;GetBillStatementResult&gt; {&#10;	// NOTE: We achieve sequential consistency with the given `bookmark`.&#10;	const session = db.withSession(bookmark);&#10;	const result = (await session&#10;		.prepare(&#x27;SELECT * FROM bills WHERE accountId = ? AND billId = ? LIMIT 1&#x27;)&#10;		.bind(accountId, billId)&#10;		.first()) as unknown as Bill;&#10;&#10;	return { bookmark: session.getBookmark() ?? &#x27;first-unconstrained&#x27;, bill: result };&#10;}&#10;</code></pre>
<h3 id="start-a-session-from-previous-context-bookmark">Start a session from previous context (bookmark)</h3>
<p>To create a new session from the context of a previous session, pass a <code>bookmark</code> parameter to guarantee that the session starts with a database version that is at least as up-to-date as the provided <code>bookmark</code>.</p>
<pre tabindex="0"><code class="language-ts">// retrieve bookmark from previous session stored in HTTP header&#10;const bookmark = request.headers.get(&#x27;x-d1-bookmark&#x27;) ?? &#x27;first-unconstrained&#x27;;&#10;&#10;const session = env.DB.withSession(bookmark)&#10;const result = await session&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run()&#10;// store bookmark for a future session&#10;response.headers.set(&#x27;x-d1-bookmark&#x27;, session.getBookmark() ?? &quot;&quot;)&#10;</code></pre>
<ul>
<li>Starting a session with a <code>bookmark</code> ensures the new session will be at least as up-to-date as the previous session that generated the given <code>bookmark</code>.</li>
<li>Refer to the <a href="/d1/worker-api/d1-database#withsession">D1 Workers Binding API documentation</a>.</li>
</ul>
<p>{/* #### Example of using <code>bookmark</code></p>
<p>This example follows from <a href="/d1/best-practices/read-replication/#example-of-using-first-primary">Example of using <code>first-primary</code></a>, but retrieves the <code>bookmark</code> from HTTP cookie.</p>
<pre tabindex="0"><code class="language-ts">import { ListBillStatementsResult, GetBillStatementResult, Bill } from &#x27;./types&#x27;;&#10;&#10;async function listBillStatements(accountId: string, db: D1Database): Promise&lt;ListBillStatementsResult&gt; {&#10;	const session = db.withSession(&#x27;first-primary&#x27;);&#10;	const { results } = (await session.prepare(&#x27;SELECT * FROM bills WHERE accountId = ?&#x27;).bind(accountId).run()) as unknown as {&#10;		results: Bill[];&#10;	};&#10;	return { bookmark: session.getBookmark() ?? &#x27;first-unconstrained&#x27;, bills: results };&#10;}&#10;&#10;async function getBillStatement(accountId: string, billId: string, bookmark: string, db: D1Database): Promise&lt;GetBillStatementResult&gt; {&#10;	// NOTE: We achieve sequential consistency with the given `bookmark`.&#10;	const session = db.withSession(bookmark);&#10;	const result = (await session&#10;		.prepare(&#x27;SELECT * FROM bills WHERE accountId = ? AND billId = ? LIMIT 1&#x27;)&#10;		.bind(accountId, billId)&#10;		.first()) as unknown as Bill;&#10;&#10;	return { bookmark: session.getBookmark() ?? &#x27;first-unconstrained&#x27;, bill: result };&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// URL path&#10;		const url = new URL(request.url);&#10;		const path = url.pathname;&#10;&#10;		// Method&#10;		const method = request.method;&#10;&#10;		// Fetch using first-unconstrained&#10;		if (path === &#x27;/bills&#x27; &amp;&amp; method === &#x27;GET&#x27;) {&#10;			// List bills&#10;			const result = await listBillStatements(&#x27;1&#x27;, env.DB);&#10;			return new Response(JSON.stringify(result), { status: 200 });&#10;		}&#10;		if (path === &#x27;/bill&#x27; &amp;&amp; method === &#x27;GET&#x27;) {&#10;			// Get bill&#10;			const result = await getBillStatement(&#x27;1&#x27;, &#x27;1&#x27;, &#x27;first-unconstrained&#x27;, env.DB);&#10;			return new Response(JSON.stringify(result), { status: 200 });&#10;		}&#10;&#10;		// Fetch using bookmark from cookie&#10;		if (path === &#x27;/bill/cookie&#x27; &amp;&amp; method === &#x27;GET&#x27;) {&#10;			// Get bill&#10;			const cookie = request.headers.get(&#x27;Cookie&#x27;);&#10;			const bookmark =&#10;				cookie&#10;					?.split(&#x27;;&#x27;)&#10;					.find((c) =&gt; c.trim().startsWith(&#x27;X-D1-Bookmark&#x27;))&#10;					?.split(&#x27;=&#x27;)[1] ?? &#x27;first-unconstrained&#x27;;&#10;			console.log(&#x27;bookmark&#x27;, bookmark);&#10;			const result = await getBillStatement(&#x27;1&#x27;, &#x27;1&#x27;, bookmark, env.DB);&#10;			return new Response(JSON.stringify(result), {&#10;				status: 200,&#10;				headers: {&#10;					&#x27;Set-Cookie&#x27;: `X-D1-Bookmark=${result.bookmark}; Path=/; SameSite=Strict`,&#10;				},&#10;			});&#10;		}&#10;&#10;		// To ingest data&#10;		if (path === &#x27;/bill&#x27; &amp;&amp; method === &#x27;POST&#x27;) {&#10;			// Create bill&#10;			const { accountId, amount, description, due_date } = await request.json();&#10;			const session = env.DB.withSession(&#x27;first-primary&#x27;);&#10;			const { results } = await session&#10;				.prepare(&#x27;INSERT INTO bills (accountId, amount, description, due_date) VALUES (?, ?, ?, ?) RETURNING *&#x27;)&#10;				.bind(accountId, amount, description, due_date)&#10;				.run();&#10;			const bookmark = session.getBookmark() ?? &#x27;first-unconstrained&#x27;;&#10;&#10;			return new Response(JSON.stringify(results), {&#10;				status: 201,&#10;				headers: {&#10;					// Set bookmark cookie&#10;					&#x27;Set-Cookie&#x27;: `X-D1-Bookmark=${bookmark}; Path=/; SameSite=Strict`,&#10;				},&#10;			});&#10;		}&#10;		return new Response(&#x27;Not Found&#x27;, {&#10;			status: 404,&#10;			statusText: &#x27;Not Found&#x27;,&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h3 id="check-where-d1-request-was-processed">Check where D1 request was processed</h3>
<p>To see how D1 requests are processed by the addition of read replicas, <code>served_by_region</code> and <code>served_by_primary</code> fields are returned in the <code>meta</code> object of <a href="/d1/worker-api/return-object/#d1result">D1 Result</a>.</p>
<pre tabindex="0"><code class="language-ts">const result = await env.DB.withSession()&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run();&#10;console.log({&#10;  servedByRegion: result.meta.served_by_region ?? &quot;&quot;,&#10;  servedByPrimary: result.meta.served_by_primary ?? &quot;&quot;,&#10;});&#10;</code></pre>
<ul>
<li><code>served_by_region</code> and <code>served_by_primary</code> fields are present for all D1 remote requests, regardless of whether read replication is enabled or if the Sessions API is used. On local development, <code>npx wrangler dev</code>, these fields are <code>undefined</code>.</li>
</ul>
<h3 id="enable-read-replication-via-rest-api">Enable read replication via REST API</h3>
<p>With the REST API, set <code>read_replication.mode: auto</code> to enable read replication on a D1 database.</p>
<p>For this REST endpoint, you need to have an API token with <code>D1:Edit</code> permission. If you do not have an API token, follow the guide: <a href="/fundamentals/api/get-started/create-token/">Create API token</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7391.md")
</div></div>
<h3 id="disable-read-replication-via-rest-api">Disable read replication via REST API</h3>
<p>With the REST API, set <code>read_replication.mode: disabled</code> to disable read replication on a D1 database.</p>
<p>For this REST endpoint, you need to have an API token with <code>D1:Edit</code> permission. If you do not have an API token, follow the guide: <a href="/fundamentals/api/get-started/create-token/">Create API token</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7380.md")
</aside>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7394.md")
</div></div>
<h3 id="check-if-read-replication-is-enabled">Check if read replication is enabled</h3>
<p>On the Cloudflare dashboard, check <strong>Settings</strong> for your D1 database to view if read replication is enabled.</p>
<p>Alternatively, <code>GET</code> D1 database REST endpoint returns if read replication is enabled or disabled.</p>
<p>For this REST endpoint, you need to have an API token with <code>D1:Read</code> permission. If you do not have an API token, follow the guide: <a href="/fundamentals/api/get-started/create-token/">Create API token</a>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7397.md")
</div></div>
<ul>
<li>Check the <code>read_replication</code> property of the <code>result</code> object
<ul>
<li><code>&quot;mode&quot;: &quot;auto&quot;</code> indicates read replication is enabled</li>
<li><code>&quot;mode&quot;: &quot;disabled&quot;</code> indicates read replication is disabled</li>
</ul>
</li>
</ul>
<h2 id="read-replica-locations">Read replica locations</h2>
<p>Currently, D1 automatically creates a read replica in <a href="/d1/configuration/data-location/#available-location-hints">every supported region</a>, including the region where the primary database instance is located. These regions are:</p>
<ul>
<li>ENAM</li>
<li>WNAM</li>
<li>WEUR</li>
<li>EEUR</li>
<li>APAC</li>
<li>OC</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7379.md")
</aside>
<h2 id="observability">Observability</h2>
<p>To see the impact of read replication and check the how D1 requests are processed by additional database instances, you can use:</p>
<ul>
<li>The <code>meta</code> object within the <a href="/d1/worker-api/return-object/#d1result"><code>D1Result</code></a> return object, which includes new fields:
<ul>
<li><code>served_by_region</code></li>
<li><code>served_by_primary</code></li>
</ul>
</li>
<li>The Cloudflare dashboard, where you can view your database metrics breakdown by region that processed D1 requests.</li>
</ul>
<h2 id="pricing">Pricing</h2>
D1 read replication is built into D1, so you don’t pay extra storage or compute costs for read replicas. You incur the exact same D1 [usage billing](/d1/platform/pricing/#billing-metrics) with or without replicas, based on `rows_read` and `rows_written` by your queries.
<h2 id="known-limitations">Known limitations</h2>
<p>There are some known limitations for D1 read replication.</p>
<ul>
<li>Sessions API is only available via the <a href="/d1/worker-api/d1-database/#withsession">D1 Worker Binding</a> and not yet available via the REST API.</li>
</ul>
<h2 id="background-information">Background information</h2>
<h3 id="replica-lag-and-consistency-model">Replica lag and consistency model</h3>
<p>To account for <span class="nb-glossary-tooltip" title="replica lag">replica lag</span>, it is important to consider the consistency model for D1. A consistency model is a logical framework that governs how a database system serves user queries (how the data is updated and accessed) when there are multiple database instances. Different models can be useful in different use cases. Most database systems provide <a href="https://jepsen.io/consistency/models/read-committed">read committed</a>, <a href="https://jepsen.io/consistency/models/snapshot-isolation">snapshot isolation</a>, or <a href="https://jepsen.io/consistency/models/serializable">serializable</a> consistency models, depending on their configuration.</p>
<h4 id="without-a-consistency-model-framework">Without a consistency model framework</h4>
<p>Consider what could happen in a distributed database system without an explicit framework to enforce a consistency model.</p>
<p><img src="/images/d1/consistency-without-sessions-api.png" alt="Distributed replicas could cause inconsistencies without Sessions API" /></p>
<ol>
<li>Your SQL write query is processed by the primary database instance.</li>
<li>You obtain a response acknowledging the write query.</li>
<li>Your subsequent SQL read query goes to a read replica.</li>
<li>The read replica has not yet been updated, so does not contain changes from your SQL write query. The returned results are inconsistent from your perspective.</li>
</ol>
<h4 id="with-sessions-api">With Sessions API</h4>
<p>When using D1 Sessions API, your queries obtain bookmarks which allows the read replica to only serve sequentially consistent data.</p>
<p><img src="/images/d1/consistency-with-sessions-api.png" alt="D1 offers sequential consistency when using Sessions API" /></p>
<ol>
<li>SQL write query is processed by the primary database instance.</li>
<li>You obtain a response acknowledging the write query. You also obtain a bookmark (100) which identifies the state of the database after the write query.</li>
<li>Your subsequent SQL read query goes to a read replica, and also provides the bookmark (100).</li>
<li>The read replica will wait until it has been updated to be at least as up-to-date as the provided bookmark (100).</li>
<li>Once the read replica has been updated (bookmark 104), it serves your read query, which is now sequentially consistent.</li>
</ol>
<p>In the diagram, the returned bookmark is bookmark 104, which is different from the one provided in your read query (bookmark 100). This can happen if there were other writes from other client requests that also got replicated to the read replica in between the two write/read queries you executed.</p>
<h4 id="sessions-api-provides-sequential-consistency">Sessions API provides sequential consistency</h4>
<p>D1 read replication offers <a href="https://jepsen.io/consistency/models/sequential">sequential consistency</a>. D1 creates a global order of all operations which have taken place on the database, and can identify the latest version of the database that a query has seen, using <a href="/d1/reference/time-travel/#bookmarks">bookmarks</a>. It then serves the query with a database instance that is at least as up-to-date as the bookmark passed along with the query to execute.</p>
<p>Sequential consistency has properties such as:</p>
<ul>
<li><strong>Monotonic reads</strong>: If you perform two reads one after the other (read-1, then read-2), read-2 cannot read a version of the database prior to read-1.</li>
<li><strong>Monotonic writes</strong>: If you perform write-1 then write-2, all processes observe write-1 before write-2.</li>
<li><strong>Writes follow reads</strong>: If you read a value, then perform a write, the subsequent write must be based on the value that was just read.</li>
<li><strong>Read my own writes</strong>: If you write to the database, all subsequent reads will see the write.</li>
</ul>
<h2 id="supplementary-information">Supplementary information</h2>
<p>You may wish to refer to the following resources:</p>
<ul>
<li>Blog: <a href="https://blog.cloudflare.com/d1-read-replication-beta/">Sequential consistency without borders: How D1 implements global read replication</a></li>
<li>Blog: <a href="https://blog.cloudflare.com/building-d1-a-global-database/">Building D1: a Global Database</a></li>
<li><a href="/d1/worker-api/d1-database#withsession">D1 Sessions API documentation</a></li>
<li><a href="https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api-template">Starter code for D1 Sessions API demo</a></li>
<li><a href="/d1/tutorials/using-read-replication-for-e-com">E-commerce store read replication tutorial</a></li>
</ul>
