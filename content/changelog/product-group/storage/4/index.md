---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/storage/4/
  description: '2025-05-29'
  full_title: Storage changelog - page 4 | Cloudflare Docs
  head_html: <title>Storage changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-05-29"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/storage/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Storage changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-05-29"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/storage/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/storage/4/#page","headline":"Storage changelog - page 4 | Cloudflare Docs","description":"2025-05-29","url":"https://developers.cloudflare.com/changelog/product-group/storage/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/storage/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="50-500ms-faster-d1-rest-api-requests"><a href="/changelog/post/2025-05-30-d1-rest-api-latency/">50-500ms Faster D1 REST API Requests</a></h2>
<p><em>2025-05-29</em></p>
<p>Users using Cloudflare's <a href="/api/resources/d1/">REST API</a> to query their D1 database can see lower end-to-end request latency now that D1 authentication is performed at the closest Cloudflare network data center that received the request. Previously, authentication required D1 REST API requests to proxy to Cloudflare's core, centralized data centers, which added network round trips and latency.</p>
<p>Latency improvements range from 50-500 ms depending on request location and <a href="/d1/configuration/data-location/">database location</a> and only apply to the REST API. REST API requests and databases outside the United States see a bigger benefit since Cloudflare's primary core data centers reside in the United States.</p>
<p>D1 query endpoints like <code>/query</code> and <code>/raw</code> have the most noticeable improvements since they no longer access Cloudflare's core data centers. D1 control plane endpoints such as those to create and delete databases see smaller improvements, since they still require access to Cloudflare's core data centers for other control plane metadata.</p>


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


<h2 id="hyperdrive-achieves-fedramp-moderate-impact-authorization"><a href="/changelog/post/2025-05-14-hyperdrive-fedramp/">Hyperdrive achieves FedRAMP Moderate-Impact Authorization</a></h2>
<p><em>2025-05-14</em></p>
<p>Hyperdrive has been approved for FedRAMP Authorization and is now available in the <a href="https://marketplace.fedramp.gov/products/FR2000863987">FedRAMP Marketplace</a>.</p>
<p>FedRAMP is a U.S. government program that provides standardized assessment and authorization for cloud products and services. As a result of this product update,
Hyperdrive has been approved as an authorized service to be used by U.S. federal agencies at the Moderate Impact level.</p>
<p>For detailed information regarding FedRAMP and its implications, please refer to the <a href="https://marketplace.fedramp.gov/products/FR2000863987">official FedRAMP documentation for Cloudflare</a>.</p>


<h2 id="publish-messages-to-queues-directly-via-http"><a href="/changelog/post/2025-05-09-publish-to-queues-via-http/">Publish messages to Queues directly via HTTP</a></h2>
<p><em>2025-05-09 12:00:00 UTC</em></p>
<p>You can now publish messages to <a href="/queues/">Cloudflare Queues</a> directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within <a href="/workers/">Cloudflare Workers</a>. You can already consume from queues via Workers or <a href="/queues/configuration/pull-consumers/">HTTP pull consumers</a>, and now publishing is just as flexible.</p>
<p>Publishing via HTTP requires a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <code>Queues Edit</code> permissions for authentication. Here's a simple example:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/queues/&lt;queue_id&gt;/messages&quot; \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{ &quot;body&quot;: { &quot;greeting&quot;: &quot;hello&quot;, &quot;timestamp&quot;:  &quot;2025-07-24T12:00:00Z&quot;} }&#x27;&#10;</code></pre>
<p>You can also use our <a href="/fundamentals/api/reference/sdks/">SDKs</a> for TypeScript, Python, and Go.</p>
<p>To get started with HTTP publishing, check out our <a href="/queues/examples/publish-to-a-queue-via-http/">step-by-step example</a> and the full API documentation in our <a href="/api/resources/queues/subresources/messages/methods/push/">API reference</a>.</p>


<h2 id="r2-dashboard-experience-gets-new-updates"><a href="/changelog/post/2025-05-01-r2-dashboard-updates/">R2 Dashboard experience gets new updates</a></h2>
<p><em>2025-05-01</em></p>
<p>We're excited to announce several improvements to the <a href="/r2/">Cloudflare R2</a> dashboard experience that make managing your object storage easier and more intuitive:</p>
<p><img src="/assets/upstream/images/r2/r2-dashboard-updates.png" alt="Cloudflare R2 Dashboard" /></p>
<h4 id="2025-05-01-r2-dashboard-updates-all-new-settings-page">All-new settings page</h4>
<p>We've redesigned the bucket settings page, giving you a centralized location to manage all your bucket configurations in one place.</p>
<h4 id="2025-05-01-r2-dashboard-updates-improved-navigation-and-sharing">Improved navigation and sharing</h4>
<ul>
<li>Deeplink support for prefix directories: Navigate through your bucket hierarchy without losing your state. Your browser's back button now works as expected, and you can share direct links to specific prefix directories with teammates.</li>
<li>Objects as clickable links: Objects are now proper links that you can copy or <code>CMD + Click</code> to open in a new tab.</li>
</ul>
<h4 id="2025-05-01-r2-dashboard-updates-clearer-public-access-controls">Clearer public access controls</h4>
<ul>
<li>Renamed &quot;r2.dev domain&quot; to &quot;Public Development URL&quot; for better clarity when exposing bucket contents for non-production workloads.</li>
<li>Public Access status now clearly displays &quot;Enabled&quot; when your bucket is exposed to the internet (via Public Development URL or Custom Domains).</li>
</ul>
<p>We've also made numerous other usability improvements across the board to make your R2 experience smoother and more productive.</p>


<h2 id="increased-limits-for-queues-pull-consumers"><a href="/changelog/post/2025-04-17-pull-consumer-limits/">Increased limits for Queues pull consumers</a></h2>
<p><em>2025-04-17 12:00:00 UTC</em></p>
<p><a href="/queues/configuration/pull-consumers/">Queues pull consumers</a> can now pull and acknowledge up to <strong>5,000 messages / second per queue</strong>. Previously, pull consumers were rate limited to 1,200 requests / 5 minutes, aggregated across all queues.</p>
<p>Pull consumers allow you to consume messages over HTTP from any environment—including outside of <a href="/workers">Cloudflare Workers</a>. They’re also useful when you need fine-grained control over how quickly messages are consumed.</p>
<p>To setup a new queue with a pull based consumer using <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler queues create my-queue&#10;npx wrangler queues consumer http add my-queue&#10;</code></pre>
<p>You can also configure a pull consumer using the <a href="/api/resources/queues/subresources/consumers/methods/create/">REST API</a> or the Queues dashboard.</p>
<p>Once configured, you can pull messages from the queue using any HTTP client. You'll need a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API Token</a> with <code>queues_read</code> and <code>queues_write</code> permissions. For example:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull&quot; \&#10;&#45;-header &quot;Authorization: Bearer ${API_TOKEN}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{ &quot;visibility_timeout&quot;: 10000, &quot;batch_size&quot;: 2 }&#x27;&#10;</code></pre>
<p>To learn more about how to acknowledge messages, pull batches at once, and setup multiple consumers, refer to the <a href="/queues/configuration/pull-consumers">pull consumer documentation</a>.</p>
<p>As always, Queues doesn't charge for data egress. Pull operations continue to be billed at the <a href="/queues/platform/pricing">existing rate</a>, of $0.40 / million operations. The increased limits are available now, on all new and existing queues. If you're new to Queues, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>


<h2 id="read-multiple-keys-from-workers-kv-with-bulk-reads"><a href="/changelog/post/2025-04-10-kv-bulk-reads/">Read multiple keys from Workers KV with bulk reads</a></h2>
<p><em>2025-04-17</em></p>
<p>You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.</p>
<p>This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by <a href="/workers/platform/limits/#simultaneous-open-connections">Workers simultaneous connection limits</a>.</p>
<pre tabindex="0"><code class="language-js">// Read single key&#10;const key = &quot;key-a&quot;;&#10;const value = await env.NAMESPACE.get(key);&#10;&#10;// Read multiple keys&#10;const keys = [&quot;key-a&quot;, &quot;key-b&quot;, &quot;key-c&quot;, ...] // up to 100 keys&#10;const values : Map&lt;string, string?&gt; = await env.NAMESPACE.get(keys);&#10;&#10;// Print the value of &quot;key-a&quot; to the console.&#10;console.log(`The first key is ${values.get(&quot;key-a&quot;)}.`)&#10;</code></pre>
<p>Consult the <a href="/kv/api/read-key-value-pairs/">Workers KV Read key-value pairs API</a> for full details on Workers KV's new bulk reads support.</p>


<h2 id="d1-read-replication-public-beta"><a href="/changelog/post/2025-04-10-d1-read-replication-beta/">D1 Read Replication Public Beta</a></h2>
<p><em>2025-04-10</em></p>
<p>D1 read replication is available in public beta to help lower average latency and increase overall throughput for read-heavy applications like e-commerce websites or content management tools.</p>
<p>Workers can leverage read-only database copies, called read replicas, by using D1 <a href="/d1/best-practices/read-replication">Sessions API</a>. A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. With Sessions API, D1 queries in a session are guaranteed to be <a href="/d1/best-practices/read-replication/#replica-lag-and-consistency-model">sequentially consistent</a> to avoid data consistency pitfalls. D1 <a href="/d1/reference/time-travel/#bookmarks">bookmarks</a> can be used from a previous session to ensure logical consistency between sessions.</p>
<pre tabindex="0"><code class="language-ts">// retrieve bookmark from previous session stored in HTTP header&#10;const bookmark = request.headers.get(&quot;x-d1-bookmark&quot;) ?? &quot;first-unconstrained&quot;;&#10;&#10;const session = env.DB.withSession(bookmark);&#10;const result = await session&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run();&#10;// store bookmark for a future session&#10;response.headers.set(&quot;x-d1-bookmark&quot;, session.getBookmark() ?? &quot;&quot;);&#10;</code></pre>
<p>Read replicas are automatically created by Cloudflare (currently one in each supported <a href="/d1/best-practices/read-replication/#read-replica-locations">D1 region</a>), are active/inactive based on query traffic, and are transparently routed to by Cloudflare at no additional cost.</p>
<p>To checkout D1 read replication, deploy the following Worker code using Sessions API, which will prompt you to create a D1 database and enable read replication on said database.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>To learn more about how read replication was implemented, go to our <a href="https://blog.cloudflare.com/d1-read-replication-beta">blog post</a>.</p>


<h2 id="cloudflare-pipelines-now-available-in-beta"><a href="/changelog/post/2025-04-10-launching-pipelines/">Cloudflare Pipelines now available in beta</a></h2>
<p><em>2025-04-10</em></p>
<p><a href="/pipelines">Cloudflare Pipelines</a> is now available in beta, to all users with a <a href="/workers/platform/pricing">Workers Paid</a> plan.</p>
<p>Pipelines let you ingest high volumes of real time data, without managing the underlying infrastructure. A single pipeline can ingest up to 100 MB of data per second, via HTTP or from a <a href="/workers">Worker</a>. Ingested data is automatically batched, written to output files, and delivered to an <a href="/r2">R2 bucket</a> in your account. You can use Pipelines to build a data lake of clickstream data, or to store events from a Worker.</p>
<p>Create your first pipeline with a single command:</p>
<pre tabindex="0"><code class="language-bash">$ npx wrangler@latest pipelines create my-clickstream-pipeline --r2-bucket my-bucket&#10;&#10;🌀 Authorizing R2 bucket &quot;my-bucket&quot;&#10;🌀 Creating pipeline named &quot;my-clickstream-pipeline&quot;&#10;✅ Successfully created pipeline my-clickstream-pipeline&#10;&#10;Id:    0e00c5ff09b34d018152af98d06f5a1xvc&#10;Name:  my-clickstream-pipeline&#10;Sources:&#10;  HTTP:&#10;    Endpoint:        https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&#10;    Authentication:  off&#10;    Format:          JSON&#10;  Worker:&#10;    Format:  JSON&#10;Destination:&#10;  Type:         R2&#10;  Bucket:       my-bucket&#10;  Format:       newline-delimited JSON&#10;  Compression:  GZIP&#10;Batch hints:&#10;  Max bytes:     100 MB&#10;  Max duration:  300 seconds&#10;  Max records:   100,000&#10;&#10;🎉 You can now send data to your pipeline!&#10;&#10;Send data to your pipeline&#x27;s HTTP endpoint:&#10;curl &quot;https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&quot; -d &#x27;[{ ...JSON_DATA... }]&#x27;&#10;&#10;To send data to your pipeline from a Worker, add the following configuration to your config file:&#10;{&#10;  &quot;pipelines&quot;: [&#10;    {&#10;      &quot;pipeline&quot;: &quot;my-clickstream-pipeline&quot;,&#10;      &quot;binding&quot;: &quot;PIPELINE&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Head over to our <a href="/pipelines/getting-started">getting started guide</a> for an in-depth tutorial to building with Pipelines.</p>


<h2 id="r2-data-catalog-is-a-managed-apache-iceberg-data-catalog-built-directly-into-r2-buckets"><a href="/changelog/post/2025-04-10-r2-data-catalog-beta/">R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets</a></h2>
<p><em>2025-04-10</em></p>
<p>Today, we are launching <a href="/r2-data-catalog/">R2 Data Catalog</a> in open beta, a managed Apache Iceberg catalog built directly into your <a href="/r2/">Cloudflare R2</a> bucket.</p>
<p>If you are not already familiar with it, <a href="https://iceberg.apache.org/">Apache Iceberg</a> is an open table format designed to handle large-scale analytics datasets stored in object storage, offering ACID transactions and schema evolution. R2 Data Catalog exposes a standard Iceberg REST catalog interface, so you can connect engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, and <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> to start querying your tables using the tools you already know.</p>
<p>To enable a data catalog on your R2 bucket, find <strong>R2 Data Catalog</strong> in your buckets settings in the dashboard, or run:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 bucket catalog enable my-bucket&#10;</code></pre>
<p>And that's it. You'll get a catalog URI and warehouse you can plug into your favorite Iceberg engines.</p>
<p>Visit our <a href="/r2-data-catalog/get-started/">getting started guide</a> for step-by-step instructions on enabling R2 Data Catalog, creating tables, and running your first queries.</p>


<h2 id="hyperdrive-now-supports-custom-tls-ssl-certificates"><a href="/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/">Hyperdrive now supports custom TLS/SSL certificates</a></h2>
<p><em>2025-04-09</em></p>
<p>Hyperdrive now supports more SSL/TLS security options for your database connections:</p>
<ul>
<li>Configure Hyperdrive to verify server certificates with <code>verify-ca</code> or <code>verify-full</code> SSL modes and protect against man-in-the-middle attacks</li>
<li>Configure Hyperdrive to provide client certificates to the database server to authenticate itself (mTLS) for stronger security beyond username and password</li>
</ul>
<p>Use the new <code>wrangler cert</code> commands to create certificate authority (CA) certificate bundles or client certificate pairs:</p>
<pre tabindex="0"><code class="language-bash">&#35; Create CA certificate bundle&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create client certificate pair&#10;npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name your-client-cert-name&#10;</code></pre>
<p>Then create a Hyperdrive configuration with the certificates and desired SSL mode:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;postgres://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-mtls-certificate-id &lt;CLIENT_CERT_ID&gt;&#10;  &#45;-sslmode verify-full&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">configuring SSL/TLS certificates for Hyperdrive</a> to enhance your database security posture.</p>


<h2 id="hyperdrive-free-plan-makes-fast-global-database-access-available-to-all"><a href="/changelog/post/2025-04-08-hyperdrive-free-plan/">Hyperdrive Free plan makes fast, global database access available to all</a></h2>
<p><em>2025-04-08</em></p>
<p>Hyperdrive is now available on the Free plan of Cloudflare Workers, enabling you to build Workers that connect to PostgreSQL or MySQL databases without compromise.</p>
<p>Low-latency access to SQL databases is critical to building full-stack Workers applications. We want you to be able to build on fast, global apps on Workers,
regardless of the tools you use. So we made Hyperdrive available for all, to make it easier to build Workers that connect to PostgreSQL and MySQL.</p>
<p>If you want to learn more about how Hyperdrive works, read the <a href="https://blog.cloudflare.com/how-hyperdrive-speeds-up-database-access">deep dive</a> on how Hyperdrive can make your database queries up to 4x faster.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-global-placement.png" alt="Hyperdrive provides edge connection setup and global connection pooling for optimal latencies." /></p>
<p>Visit the docs to <a href="/hyperdrive/get-started/">get started</a> with Hyperdrive for PostgreSQL or MySQL.</p>


<h2 id="hyperdrive-introduces-support-for-mysql-and-mysql-compatible-databases"><a href="/changelog/post/2025-04-08-hyperdrive-mysql-support/">Hyperdrive introduces support for MySQL and MySQL-compatible databases</a></h2>
<p><em>2025-04-08</em></p>
<p>Hyperdrive now supports connecting to MySQL and MySQL-compatible databases, including Amazon RDS and Aurora MySQL, Google Cloud SQL for MySQL, Azure Database for MySQL, PlanetScale and MariaDB.</p>
<p>Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.</p>
<p>Best of all, you can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, no code changes required.</p>
<pre tabindex="0"><code class="language-ts">import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export interface Env {&#10;	HYPERDRIVE: Hyperdrive;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;			disableEval: true, // Required for Workers compatibility&#10;		});&#10;&#10;		const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;		ctx.waitUntil(connection.end());&#10;&#10;		return new Response(JSON.stringify({ results, fields }), {&#10;			headers: {&#10;				&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				&quot;Access-Control-Allow-Origin&quot;: &quot;*&quot;,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a> and <a href="/hyperdrive/get-started/">get started building Workers that connect to MySQL with Hyperdrive</a>.</p>


<h2 id="create-fully-managed-rag-pipelines-for-your-ai-applications-with-autorag"><a href="/changelog/post/2025-04-07-autorag-open-beta/">Create fully-managed RAG pipelines for your AI applications with AutoRAG</a></h2>
<p><em>2025-04-07</em></p>
<p><a href="/ai-search/">AutoRAG</a> is now in open beta, making it easy for you to build fully-managed retrieval-augmented generation (RAG) pipelines without managing infrastructure. Just upload your docs to <a href="/r2/get-started/">R2</a>, and AutoRAG handles the rest: embeddings, indexing, retrieval, and response generation via API.</p>
<p>With AutoRAG, you can:</p>
<ul>
<li><strong>Customize your pipeline:</strong> Choose from <a href="/workers-ai">Workers AI</a> models, configure chunking strategies, edit system prompts, and more.</li>
<li><strong>Instant setup:</strong> AutoRAG provisions everything you need from <a href="/vectorize">Vectorize</a>, <a href="/ai-gateway">AI gateway</a>, to pipeline logic for you, so you can go from zero to a working RAG pipeline in seconds.</li>
<li><strong>Keep your index fresh:</strong> AutoRAG continuously syncs your index with your data source to ensure responses stay accurate and up to date.</li>
<li><strong>Ask questions:</strong> Query your data and receive grounded responses via a <a href="/ai-search/api/search/workers-binding/">Workers binding</a> or <a href="/ai-search/api/search/rest-api/">API</a>.</li>
</ul>
<p>Whether you're building internal tools, AI-powered search, or a support assistant, AutoRAG gets you from idea to deployment in minutes.</p>
<p>Get started in the <a href="https://dash.cloudflare.com/?to=/:account/ai/autorag">Cloudflare dashboard</a> or check out the <a href="/ai-search/get-started/">guide</a> for instructions on how to build your RAG pipeline today.</p>


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


<h2 id="new-pause-purge-apis-for-queues"><a href="/changelog/post/2025-03-25-pause-purge-queues/">New Pause & Purge APIs for Queues</a></h2>
<p><em>2025-03-27 12:00:00 UTC</em></p>
<p><a href="/queues/">Queues</a> now supports the ability to pause message delivery and/or purge (delete) messages on a queue. These operations can be useful when:</p>
<ul>
<li>Your consumer has a bug or downtime, and you want to temporarily stop messages from being processed while you fix the bug</li>
<li>You have pushed invalid messages to a queue due to a code change during development, and you want to clean up the backlog</li>
<li>Your queue has a backlog that is stale and you want to clean it up to allow new messages to be consumed</li>
</ul>
<p>To pause a queue using <a href="/workers/wrangler/">Wrangler</a>, run the <code>pause-delivery</code> command. Paused queues continue to receive messages. And you can easily unpause a queue using the <code>resume-delivery</code> command.</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues pause-delivery my-queue&#10;Pausing message delivery for queue my-queue.&#10;Paused message delivery for queue my-queue.&#10;&#10;$ wrangler queues resume-delivery my-queue&#10;Resuming message delivery for queue my-queue.&#10;Resumed message delivery for queue my-queue.&#10;</code></pre>
<p>Purging a queue permanently deletes all messages in the queue. Unlike pausing, purging is an irreversible operation:</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues purge my-queue&#10;✔ This operation will permanently delete all the messages in queue my-queue. Type my-queue to proceed. … my-queue&#10;Purged queue &#x27;my-queue&#x27;&#10;</code></pre>
<p>You can also do these operations using the <a href="/api/resources/queues/">Queues REST API</a>, or the dashboard page for a queue.</p>
<p><img src="/assets/upstream/images/queues/pause-purge.png" alt="Pause and purge using the dashboard" /></p>
<p>This feature is available on all new and existing queues. Head over to the <a href="/queues/configuration/pause-purge">pause and purge documentation</a> to learn more. And if you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>


<h2 id="hyperdrive-reduces-query-latency-by-up-to-90-and-now-supports-ip-access-control-lists"><a href="/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/">Hyperdrive reduces query latency by up to 90% and now supports IP access control lists</a></h2>
<p><em>2025-03-07</em></p>
<p>Hyperdrive now pools database connections in one or more regions close to your database. This means that your uncached queries and new database connections have up to 90% less latency as measured from connection pools.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-regional-pooling-query-latency-improvement.png" alt="Hyperdrive query latency decreases by 90% during Hyperdrive's gradual rollout of regional pooling." /></p>
<p>By improving placement of Hyperdrive database connection pools, Workers' Smart Placement is now more effective when used with Hyperdrive, ensuring that your Worker can be placed as close to your database as possible.</p>
<p>With this update, Hyperdrive also uses <a href="https://www.cloudflare.com/ips/">Cloudflare's standard IP address ranges</a> to connect to your database. This enables you to configure the firewall policies (IP access control lists) of your database to only allow access from Cloudflare and Hyperdrive.</p>
<p>Refer to <a href="/hyperdrive/concepts/how-hyperdrive-works/">documentation on how Hyperdrive makes connecting to regional databases from Cloudflare Workers fast</a>.</p>
<p>This improvement is enabled on all Hyperdrive configurations.</p>


<h2 id="set-retention-polices-for-your-r2-bucket-with-bucket-locks"><a href="/changelog/post/2025-03-06-r2-bucket-locks/">Set retention polices for your R2 bucket with bucket locks</a></h2>
<p><em>2025-03-06</em></p>
<p>You can now use <a href="/r2/buckets/bucket-locks/">bucket locks</a> to set retention policies on your <a href="/r2/buckets/">R2 buckets</a> (or specific prefixes within your buckets) for a specified period — or indefinitely. This can help ensure compliance by protecting important data from accidental or malicious deletion.</p>
<p>Locks give you a few ways to ensure your objects are retained (not deleted or overwritten). You can:</p>
<ul>
<li>Lock objects for a specific duration, for example 90 days.</li>
<li>Lock objects until a certain date, for example January 1, 2030.</li>
<li>Lock objects indefinitely, until the lock is explicitly removed.</li>
</ul>
<p>Buckets can have up to 1,000 <a href="/r2/buckets/">bucket lock rules</a>. Each rule specifies which objects it covers (via prefix) and how long those objects must remain retained.</p>
<p>Here are a couple of examples showing how you can configure bucket lock rules using <a href="/workers/wrangler/">Wrangler</a>:</p>
<h4 id="2025-03-06-r2-bucket-locks-ensure-all-objects-in-a-bucket-are-retained-for-at-least-180-days">Ensure all objects in a bucket are retained for at least 180 days</h4>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name 180-days-all --retention-days 180&#10;</code></pre>
<h4 id="2025-03-06-r2-bucket-locks-prevent-deletion-or-overwriting-of-all-logs-indefinitely-via-prefix">Prevent deletion or overwriting of all logs indefinitely (via prefix)</h4>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket lock add &lt;bucket&gt; --name indefinite-logs --prefix logs/ --retention-indefinite&#10;</code></pre>
<p>For more information on bucket locks and how to set retention policies for objects in your R2 buckets, refer to our <a href="/r2/buckets/bucket-locks/">documentation</a>.</p>


<h2 id="super-slurper-now-supports-migrations-from-all-s3-compatible-storage-providers"><a href="/changelog/post/2025-02-24-r2-super-slurper-s3-compatible-support/">Super Slurper now supports migrations from all S3-compatible storage providers</a></h2>
<p><em>2025-02-24</em></p>
<p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> can now migrate data from any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>. This includes transfers from services like MinIO, Wasabi, Backblaze B2, and DigitalOcean Spaces.</p>
<p><img src="/assets/upstream/images/changelog/r2/super-slurper-s3-compat-screenshot-border.png" alt="Super Slurper S3-Compatible Source" /></p>
<p>For more information on Super Slurper and how to migrate data from your existing S3-compatible storage buckets to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>


<h2 id="customize-queue-message-retention-periods"><a href="/changelog/post/2025-02-14-customize-queue-retention-period/">Customize queue message retention periods</a></h2>
<p><em>2025-02-14 12:00:00 UTC</em></p>
<p>You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.</p>
<p><img src="/assets/upstream/images/queues/customize-retention-period.png" alt="Customize a queue's message retention period" /></p>
<p>You can customize the retention period on the settings page for your queue, or using Wrangler:</p>
<pre tabindex="0"><code class="language-bash">$ wrangler queues update my-queue --message-retention-period-secs 600&#10;</code></pre>
<p>This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>


<h2 id="super-slurper-now-transfers-data-to-r2-up-to-5x-faster"><a href="/changelog/post/2025-02-14-r2-super-slurper-faster-migrations/">Super Slurper now transfers data to R2 up to 5x faster</a></h2>
<p><em>2025-02-14</em></p>
<p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to <a href="/r2/">Cloudflare R2</a> up to 5x faster than it did before.</p>
<p>We moved from a centralized service to a distributed system built on the Cloudflare Developer Platform — using <a href="/workers/">Cloudflare Workers</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/queues/">Queues</a> — to both improve performance and increase system concurrency capabilities (and we'll share more details about how we did it soon!)</p>
<p><img src="/assets/upstream/images/r2/slurper-objects-over-time-border.png" alt="Super Slurper Objects Migrated" /></p>
<p><em>Time to copy 75,000 objects from AWS S3 to R2 decreased from 15 minutes 30 seconds (old) to 3 minutes 25 seconds (after performance improvements)</em></p>
<p>For more information on Super Slurper and how to migrate data from existing object storage to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>


<h2 id="automatic-configuration-for-private-databases-on-hyperdrive"><a href="/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/">Automatic configuration for private databases on Hyperdrive</a></h2>
<p><em>2025-01-28</em></p>
<p>Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-private-database-automatic-configuration.png" alt="Automatic configuration of Cloudflare Access and Service Token in the Cloudflare dashboard for Hyperdrive." /></p>
<p>When creating a Hyperdrive configuration for a private database, you only need to provide your database credentials and set up a Cloudflare Tunnel within the private network where your database is accessible. Hyperdrive will automatically create the Cloudflare Access, Service Token, and Policies needed to secure and restrict your Cloudflare Tunnel to the Hyperdrive configuration.</p>
<p>To create a Hyperdrive for a private database, you can follow the <a href="/hyperdrive/configuration/connect-to-private-database/">Hyperdrive documentation</a>. You can still manually create the Cloudflare Access, Service Token, and Policies if you prefer.</p>
<p>This feature is available from the Cloudflare dashboard.</p>


<h2 id="workers-kv-namespace-limits-increased-to-1000"><a href="/changelog/post/2025-01-27-kv-increased-namespaces-limits/">Workers KV namespace limits increased to 1000</a></h2>
<p><em>2025-01-28</em></p>
<p>You can now have up to 1000 Workers KV namespaces per account.</p>
<p>Workers KV namespace limits were increased from 200 to 1000 for all accounts. Higher limits for Workers KV namespaces enable better organization of key-value data, such as by category, tenant, or environment.</p>
<p>Consult the <a href="/kv/platform/limits/">Workers KV limits documentation</a> for the rest of the limits. This increased limit is available for both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>


<h2 id="40-60-faster-d1-worker-api-requests"><a href="/changelog/post/2025-01-07-d1-faster-query/">40-60% Faster D1 Worker API Requests</a></h2>
<p><em>2025-01-07</em></p>
<p>Users making <a href="/d1/">D1</a> requests via the <a href="/d1/worker-api/">Workers API</a> can see up to a 60% end-to-end latency improvement due to the removal of redundant network round trips needed for each request to a D1 database.</p>
<p><img src="/images/d1/faster-d1-worker-api.png" alt="D1 Worker API latency" /></p>
<p><em>p50, p90, and p95 request latency aggregated across entire D1 service. These latencies are a reference point and should not be viewed as your exact workload improvement.</em></p>
<p>This performance improvement benefits all D1 Worker API traffic, especially cross-region requests where network latency is an outsized latency factor. For example, a user in Europe talking to a database in North America. D1 <a href="/d1/configuration/data-location/#provide-a-location-hint">location hints</a> can be used to influence the geographic location of a database.</p>
<p>For more details on how D1 removed redundant round trips, see the D1 specific release note <a href="/d1/platform/release-notes/#2025-01-07">entry</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/storage/3/">Previous</a><span>Page 4 of 5</span><a class="pagination-next" rel="next" href="/changelog/product-group/storage/5/">Next</a></nav>
