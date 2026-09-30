<p>This guide describes the storage &amp; database products available as part of Cloudflare Workers, including recommended use-cases and best practices.</p>
<h2 id="choose-a-storage-product">Choose a storage product</h2>
<p>The following table maps our storage &amp; database products to common industry terms as well as recommended use-cases:</p>
<table>
<thead>
<tr>
<th>Use-case</th>
<th>Product</th>
<th>Ideal for</th>
</tr>
</thead>
<tbody>
<tr>
<td>Key-value storage</td>
<td><a href="/kv/">Workers KV</a></td>
<td>Configuration data, service routing metadata, personalization (A/B testing)</td>
</tr>
<tr>
<td>Object storage / blob storage</td>
<td><a href="/r2/">R2</a></td>
<td>User-facing web assets, images, machine learning and training datasets, analytics datasets, log and event data.</td>
</tr>
<tr>
<td>Accelerate a Postgres or MySQL database</td>
<td><a href="/hyperdrive/">Hyperdrive</a></td>
<td>Connecting to an existing database in a cloud or on-premise using your existing database drivers &amp; ORMs.</td>
</tr>
<tr>
<td>Global coordination &amp; stateful serverless</td>
<td><a href="/durable-objects/">Durable Objects</a></td>
<td>Building collaborative applications; global coordination across clients; real-time WebSocket applications; strongly consistent, transactional storage.</td>
</tr>
<tr>
<td>Lightweight SQL database</td>
<td><a href="/d1/">D1</a></td>
<td>Relational data, including user profiles, product listings and orders, and/or customer data.</td>
</tr>
<tr>
<td>Task processing, batching and messaging</td>
<td><a href="/queues/">Queues</a></td>
<td>Background job processing (emails, notifications, APIs), message queuing, and deferred tasks.</td>
</tr>
<tr>
<td>Vector search &amp; embeddings queries</td>
<td><a href="/vectorize/">Vectorize</a></td>
<td>Storing <a href="/workers-ai/models/?tasks=Text+Embeddings">embeddings</a> from AI models for semantic search and classification tasks.</td>
</tr>
<tr>
<td>Streaming ingestion</td>
<td><a href="/pipelines/">Pipelines</a></td>
<td>Streaming data ingestion and processing, including clickstream analytics, telemetry/log data, and structured data for querying</td>
</tr>
<tr>
<td>Time-series metrics</td>
<td><a href="/analytics/analytics-engine/">Analytics Engine</a></td>
<td>Write and query high-cardinality time-series data, usage metrics, and service-level telemetry using Workers and/or SQL.</td>
</tr>
</tbody>
</table>
<p>Applications can build on multiple storage &amp; database products: for example, using Workers KV for session data; R2 for large file storage, media assets and user-uploaded files; and Hyperdrive to connect to a hosted Postgres or MySQL database.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pages-functions">Pages Functions</h3>
@markup("md", "content/.markup/bodies/16186.md")
</aside>
<h2 id="sql-database-options">SQL database options</h2>
<p>There are three options for SQL-based databases available when building applications with Workers.</p>
<ul>
<li><strong>Hyperdrive</strong> if you have an existing Postgres or MySQL database, require large (1TB, 100TB or more) single databases, and/or want to use your existing database tools. You can also connect Hyperdrive to database platforms like <a href="https://planetscale.com/">PlanetScale</a> or <a href="https://neon.tech/">Neon</a>.</li>
<li><strong>D1</strong> for lightweight, serverless applications that are read-heavy, have global users that benefit from D1's <a href="/d1/best-practices/read-replication/">read replication</a>, and do not require you to manage and maintain a traditional RDBMS.</li>
<li><strong>Durable Objects</strong> for stateful serverless workloads, per-user or per-customer SQL state, and building distributed systems (D1 and Queues are built on Durable Objects) where Durable Object's <a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">strict serializability</a> enables global ordering of requests and storage operations.</li>
</ul>
<h3 id="session-storage">Session storage</h3>
<p>We recommend using <a href="/kv/">Workers KV</a> for storing session data, credentials (API keys), and/or configuration data. These are typically read at high rates (thousands of RPS or more), are not typically modified (within KV's 1 write RPS per unique key limit), and do not need to be immediately consistent.</p>
<p>Frequently read keys benefit from KV's <a href="/kv/concepts/how-kv-works/">internal cache</a>, and repeated reads to these &quot;hot&quot; keys will typically see latencies in the 500µs to 10ms range.</p>
<p>Authentication frameworks like <a href="https://openauth.js.org/docs/storage/cloudflare/">OpenAuth</a> use Workers KV as session storage when deployed to Cloudflare, and <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> uses KV to securely store and distribute user credentials so that they can be validated as close to the user as possible and reduce overall latency.</p>
<h2 id="product-overviews">Product overviews</h2>
<h3 id="workers-kv">Workers KV</h3>
<p>Workers KV is an eventually consistent key-value data store that caches on the Cloudflare global network.</p>
<p>It is ideal for projects that require:</p>
<ul>
<li>High volumes of reads and/or repeated reads to the same keys.</li>
<li>Low-latency global reads (typically within 10ms for hot keys)</li>
<li>Per-object time-to-live (TTL).</li>
<li>Distributed configuration and/or session storage.</li>
</ul>
<p>To get started with KV:</p>
<ul>
<li>Read how <a href="/kv/concepts/how-kv-works/">KV works</a>.</li>
<li>Create a <a href="/kv/concepts/kv-namespaces/">KV namespace</a>.</li>
<li>Review the <a href="/kv/api/">KV Runtime API</a>.</li>
<li>Learn about KV <a href="/kv/platform/limits/">Limits</a>.</li>
</ul>
<h3 id="r2">R2</h3>
<p>R2 is S3-compatible blob storage that allows developers to store large amounts of unstructured data without egress fees associated with typical cloud storage services.</p>
<p>It is ideal for projects that require:</p>
<ul>
<li>Storage for files which are infrequently accessed.</li>
<li>Large object storage (for example, gigabytes or more per object).</li>
<li>Strong consistency per object.</li>
<li>Asset storage for websites (refer to <a href="/r2/buckets/public-buckets/#caching">caching guide</a>)</li>
</ul>
<p>To get started with R2:</p>
<ul>
<li>Read the <a href="/r2/get-started/">Get started guide</a>.</li>
<li>Learn about R2 <a href="/r2/platform/limits/">Limits</a>.</li>
<li>Review the <a href="/r2/api/workers/workers-api-reference/">R2 Workers API</a>.</li>
</ul>
<h3 id="durable-objects">Durable Objects</h3>
<p>Durable Objects provide low-latency coordination and consistent storage for the Workers platform through global uniqueness and a transactional storage API.</p>
<ul>
<li>
<p>Global Uniqueness guarantees that there will be a single instance of a Durable Object class with a given ID running at once, across the world. Requests for a Durable Object ID are routed by the Workers runtime to the Cloudflare data center that owns the Durable Object.</p>
</li>
<li>
<p>The transactional storage API provides strongly consistent key-value storage to the Durable Object. Each Object can only read and modify keys associated with that Object. Execution of a Durable Object is single-threaded, but multiple request events may still be processed out-of-order from how they arrived at the Object.</p>
</li>
</ul>
<p>It is ideal for projects that require:</p>
<ul>
<li>Real-time collaboration (such as a chat application or a game server).</li>
<li>Consistent storage.</li>
<li>Data locality.</li>
</ul>
<p>To get started with Durable Objects:</p>
<ul>
<li>Read the <a href="https://blog.cloudflare.com/introducing-workers-durable-objects/">introductory blog post</a>.</li>
<li>Review the <a href="/durable-objects/">Durable Objects documentation</a>.</li>
<li>Get started with <a href="/durable-objects/get-started/">Durable Objects</a>.</li>
<li>Learn about Durable Objects <a href="/durable-objects/platform/limits/">Limits</a>.</li>
</ul>
<h3 id="d1">D1</h3>
<p><a href="/d1/">D1</a> is Cloudflare’s native serverless database. With D1, you can create a database by importing data or defining your tables and writing your queries within a Worker or through the API.</p>
<p>D1 is ideal for:</p>
<ul>
<li>Persistent, relational storage for user data, account data, and other structured datasets.</li>
<li>Use-cases that require querying across your data ad-hoc (using SQL).</li>
<li>Workloads with a high ratio of reads to writes (most web applications).</li>
</ul>
<p>To get started with D1:</p>
<ul>
<li>Read <a href="/d1">the documentation</a></li>
<li>Follow the <a href="/d1/get-started/">Get started guide</a> to provision your first D1 database.</li>
<li>Review the <a href="/d1/worker-api/">D1 Workers Binding API</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16185.md")
</aside>
<h3 id="queues">Queues</h3>
<p>Cloudflare Queues allows developers to send and receive messages with guaranteed delivery. It integrates with <a href="/workers">Cloudflare Workers</a> and offers at-least once delivery, message batching, and does not charge for egress bandwidth.</p>
<p>Queues is ideal for:</p>
<ul>
<li>Offloading work from a request to schedule later.</li>
<li>Send data from Worker to Worker (inter-Service communication).</li>
<li>Buffering or batching data before writing to upstream systems, including third-party APIs or <a href="/queues/examples/send-errors-to-r2/">Cloudflare R2</a>.</li>
</ul>
<p>To get started with Queues:</p>
<ul>
<li><a href="/queues/get-started/">Set up your first queue</a>.</li>
<li>Learn more <a href="/queues/reference/how-queues-works/">about how Queues works</a>.</li>
</ul>
<h3 id="hyperdrive">Hyperdrive</h3>
<p>Hyperdrive is a service that accelerates queries you make to MySQL and Postgres databases, making it faster to access your data from across the globe, irrespective of your users’ location.</p>
<p>Hyperdrive allows you to:</p>
<ul>
<li>Connect to an existing database from Workers without connection overhead.</li>
<li>Cache frequent queries across Cloudflare's global network to reduce response times on highly trafficked content.</li>
<li>Reduce load on your origin database with connection pooling.</li>
</ul>
<p>To get started with Hyperdrive:</p>
<ul>
<li><a href="/hyperdrive/get-started/">Connect Hyperdrive</a> to your existing database.</li>
<li>Learn more <a href="/hyperdrive/concepts/how-hyperdrive-works/">about how Hyperdrive speeds up your database queries</a>.</li>
</ul>
<h2 id="pipelines">Pipelines</h2>
<p>Pipelines is a streaming ingestion service that allows you to ingest high volumes of real time data, without managing any infrastructure.</p>
<p>Pipelines allows you to:</p>
<ul>
<li>Ingest data at extremely high throughput (tens of thousands of records per second or more)</li>
<li>Batch and write data directly to object storage, ready for querying</li>
<li>(Future) Transform and aggregate data during ingestion</li>
</ul>
<p>To get started with Pipelines:</p>
<ul>
<li><a href="/pipelines/getting-started/">Create a Pipeline</a> that can batch and write records to R2.</li>
</ul>
<h3 id="analytics-engine">Analytics Engine</h3>
<p>Analytics Engine is Cloudflare's time-series and metrics database that allows you to write unlimited-cardinality analytics at scale using a built-in API to write data points from Workers and query that data using SQL directly.</p>
<p>Analytics Engine allows you to:</p>
<ul>
<li>Expose custom analytics to your own customers</li>
<li>Build usage-based billing systems</li>
<li>Understand the health of your service on a per-customer or per-user basis</li>
<li>Add instrumentation to frequently called code paths, without impacting performance or overwhelming external analytics systems with events</li>
</ul>
<p>Cloudflare uses Analytics Engine internally to store and product per-product metrics for products like D1 and R2 at scale.</p>
<p>To get started with Analytics Engine:</p>
<ul>
<li>Learn how to <a href="/analytics/analytics-engine/get-started/">get started with Analytics Engine</a></li>
<li>See <a href="/analytics/analytics-engine/recipes/usage-based-billing-for-your-saas-product/">an example of writing time-series data to Analytics Engine</a></li>
<li>Understand the <a href="/analytics/analytics-engine/sql-api/">SQL API</a> for reading data from your Analytics Engine datasets</li>
</ul>
<h3 id="vectorize">Vectorize</h3>
<p>Vectorize is a globally distributed vector database that enables you to build full-stack, AI-powered applications with Cloudflare Workers and <a href="/workers-ai/">Workers AI</a>.</p>
<p>Vectorize allows you to:</p>
<ul>
<li>Store embeddings from any vector embeddings model (Bring Your Own embeddings) for semantic search and classification tasks.</li>
<li>Add context to Large Language Model (LLM) queries by using vector search as part of a <a href="/workers-ai/guides/tutorials/build-a-retrieval-augmented-generation-ai/">Retrieval Augmented Generation</a> (RAG) workflow.</li>
<li><a href="/vectorize/reference/metadata-filtering/">Filter on vector metadata</a> to reduce the search space and return more relevant results.</li>
</ul>
<p>To get started with Vectorize:</p>
<ul>
<li><a href="/vectorize/get-started/intro/">Create your first vector database</a>.</li>
<li>Combine <a href="/vectorize/get-started/embeddings/">Workers AI and Vectorize</a> to generate, store and query text embeddings.</li>
<li>Learn more about <a href="/vectorize/reference/what-is-a-vector-database/">how vector databases work</a>.</li>
</ul>
<h2 id="sql-in-durable-objects-vs-d1">SQL in Durable Objects vs D1</h2>
<p>Cloudflare Workers offers a SQLite-backed serverless database product - <a href="/d1/">D1</a>. How should you compare <a href="/durable-objects/best-practices/access-durable-objects-storage/">SQLite in Durable Objects</a> and D1?</p>
<p><strong>D1 is a managed database product.</strong></p>
<p>D1 fits into a familiar architecture for developers, where application servers communicate with a database over the network. Application servers are typically Workers; however, D1 also supports external, non-Worker access via an <a href="https://developers.cloudflare.com/api/resources/d1/subresources/database/methods/query/">HTTP API</a>, which helps unlock <a href="/d1/reference/community-projects/#_top">third-party tooling</a> support for D1.</p>
<p>D1 aims for a &quot;batteries included&quot; feature set, including the above HTTP API, <a href="/d1/reference/migrations/#_top">database schema management</a>, <a href="/d1/best-practices/import-export-data/">data import/export</a>, and <a href="/d1/observability/metrics-analytics/#query-insights">database query insights</a>.</p>
<p>With D1, your application code and SQL database queries are not colocated which can impact application performance. If performance is a concern with D1, Workers has <a href="/workers/configuration/placement/#_top">Smart Placement</a> to dynamically run your Worker in the best location to reduce total Worker request latency, considering everything your Worker talks to, including D1.</p>
<p><strong>SQLite in Durable Objects is a lower-level compute with storage building block for distributed systems.</strong></p>
<p>By design, Durable Objects are accessed with Workers-only.</p>
<p>Durable Objects require a bit more effort, but in return, give you more flexibility and control. With Durable Objects, you must implement two pieces of code that run in different places: a front-end Worker which routes incoming requests from the Internet to a unique Durable Object, and the Durable Object itself, which runs on the same machine as the SQLite database. You get to choose what runs where, and it may be that your application benefits from running some application business logic right next to the database.</p>
<p>With SQLite in Durable Objects, you may also need to build some of your own database tooling that comes out-of-the-box with D1.</p>
<p>SQL query pricing and limits are intended to be identical between D1 (<a href="/d1/platform/pricing/">pricing</a>, <a href="/d1/platform/limits/">limits</a>) and SQLite in Durable Objects (<a href="/durable-objects/platform/pricing/#sqlite-storage-backend">pricing</a>, <a href="/durable-objects/platform/limits/">limits</a>).</p>
