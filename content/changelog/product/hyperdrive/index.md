<h1 id="changelog">Changelog</h1>

<h2 id="hyperdrive-support-for-python-workers"><a href="/changelog/post/2026-09-16-hyperdrive-python-workers/">Hyperdrive support for Python Workers</a></h2>
<p><em>2026-09-16</em></p>
<p><a href="/workers/languages/python/">Python Workers</a> can now connect to PostgreSQL and MySQL through Hyperdrive.</p>
<p>For setup, code examples, and limitations, refer to <a href="/hyperdrive/examples/python-workers/">Use Hyperdrive from Python Workers</a>.</p>


<h2 id="mysql-support-in-hyperdrive-is-now-generally-available"><a href="/changelog/post/2026-08-07-hyperdrive-mysql-ga/">MySQL support in Hyperdrive is now generally available</a></h2>
<p><em>2026-08-07</em></p>
<p>Support for MySQL in Hyperdrive is now generally available. You can connect to any MySQL database from your Workers using Hyperdrive.</p>
<p>Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.</p>
<p>You can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, with no code changes required. MySQL support is available at the same <a href="/hyperdrive/platform/pricing/">pricing</a> as Postgres.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17733.md")</div>
<p>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a> and <a href="/hyperdrive/get-started/">get started building Workers that connect to MySQL with Hyperdrive</a>.</p>


<h2 id="restart-a-hyperdrive-configuration-from-the-dashboard"><a href="/changelog/post/2026-08-07-hyperdrive-restart-configuration-dashboard/">Restart a Hyperdrive configuration from the dashboard</a></h2>
<p><em>2026-08-07</em></p>
<p>You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.</p>
<p>Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.</p>
<p>To restart, select your Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to the <strong>Settings</strong> tab, and select <strong>Restart</strong> under <strong>Danger zone</strong>. Restarting requires the <a href="/fundamentals/manage-members/roles/"><strong>Hyperdrive Admin</strong> role</a>. After a restart, the <strong>Settings</strong> tab shows when the configuration was last manually restarted.</p>
<p><img src="/assets/upstream/images/hyperdrive/dashboard-restart-danger-zone.png" alt="The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions." /></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17734.md")</aside>
<p>For more information, refer to <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>


<h2 id="create-planetscale-postgres-and-mysql-databases-billed-to-your-cloudflare-account"><a href="/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/">Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account</a></h2>
<p><em>2026-06-18</em></p>
<p>You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer. Cloudflare contract customers will be able to add PlanetScale usage to their contract in July so reach out to your Cloudflare account team if interested.</p>
<p>Create a PlanetScale database from the Cloudflare dashboard to check out globally distributed Workers optimized for regional data access.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/hyperdrive/planetscale-request-flow.svg" alt="Request flow from a user to Workers, Hyperdrive caches, connection pools, and PlanetScale." /></p>
<p>PlanetScale databases created from Cloudflare work with <a href="/workers/">Workers</a> through <a href="/hyperdrive/">Hyperdrive</a>. Hyperdrive manages database connection pools and query caching, so you can use PlanetScale as a centralized relational database for Workers applications without changing your database drivers, object-relational mapping (ORM) libraries, or SQL tooling.</p>
<p>PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard <a href="https://planetscale.com/pricing">pricing</a>. You can introspect per-database billing usage via PlanetScale's <a href="https://planetscale.com/docs/billing#organization-usage-and-billing-page">dashboard</a>.</p>
<p>When you create a PlanetScale database from the Cloudflare dashboard, you receive the same PlanetScale developer experience, including development branches, query insights, and Model Context Protocol (MCP) server support for agents.</p>
<p>To get started, refer to <a href="/hyperdrive/planetscale/">PlanetScale Postgres and MySQL with Hyperdrive</a>.</p>


<h2 id="hyperdrive-exposes-database-connection-pool-size-metrics"><a href="/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/">Hyperdrive exposes database connection pool size metrics</a></h2>
<p><em>2026-05-15</em></p>
<p>You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a>, you can see <code>waitingClients</code>, <code>currentPoolSize</code>, <code>availablePoolSlots</code>, and <code>maxPoolSize</code> for each of your configurations.</p>
<p>A new <strong>Pool connections</strong> chart has been added to the <strong>Metrics</strong> tab of each Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>. You can use the location selector to drill down into specific locations hosting your connection pool by airport code.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-pool-size-metrics-chart.png" alt="Hyperdrive pool size metrics chart" /></p>
<p>The chart shows:</p>
<ul>
<li><strong>Waiting clients</strong>: Client requests waiting for an available connection.</li>
<li><strong>Open connections</strong>: Active connections to your database.</li>
<li><strong>Pool size maximum</strong>: Your configured origin connection limit.</li>
</ul>
<p>Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to <a href="/hyperdrive/platform/limits/#request-a-limit-increase">increase your Hyperdrive connection limit</a>.</p>
<h4 id="2026-05-15-hyperdrive-pool-size-metrics-pool-size-metrics">Pool size metrics</h4>
<p>The <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a> exposes the following key connection pool metrics for each Hyperdrive configuration:</p>
<p>Under <code>avg</code>:</p>
<ul>
<li><strong><code>currentPoolSize</code></strong> — Average number of connections currently open in the pool.</li>
<li><strong><code>availablePoolSlots</code></strong> — Average number of pool connections available for checkout.</li>
<li><strong><code>waitingClients</code></strong> — Average number of clients waiting for a connection from the pool.</li>
</ul>
<p>Under <code>max</code>:</p>
<ul>
<li><strong><code>maxPoolSize</code></strong> — Configured maximum size of the connection pool.</li>
<li><strong><code>currentPoolSize</code></strong> — Peak number of connections open in the pool.</li>
<li><strong><code>waitingClients</code></strong> — Peak number of clients waiting for a connection from the pool.</li>
</ul>
<p>For more information, refer to <a href="/hyperdrive/observability/metrics/">Metrics and analytics</a> and <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>


<h2 id="hyperdrive-support-for-private-databases-with-workers-vpc"><a href="/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/">Hyperdrive support for private databases with Workers VPC</a></h2>
<p><em>2026-04-29</em></p>
<p>You can now connect Hyperdrive to a private database through a <a href="/workers-vpc/">Workers VPC service</a>. This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.</p>
<p>When creating a Hyperdrive configuration in the Cloudflare dashboard, choose <strong>Connect to private database</strong> and then <strong>Workers VPC</strong>. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.</p>
<p>You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:</p>
<pre><code class="language-sh">npx wrangler hyperdrive create my-vpc-database \&#10;  &#45;-service-id &lt;YOUR_VPC_SERVICE_ID&gt; \&#10;  &#45;-database &lt;DATABASE_NAME&gt; \&#10;  &#45;-user &lt;DATABASE_USER&gt; \&#10;  &#45;-password &lt;DATABASE_PASSWORD&gt; \&#10;  &#45;-scheme postgresql&#10;</code></pre>
<p>Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.</p>
<p>To get started, refer to <a href="/hyperdrive/configuration/connect-to-private-database-vpc/">Connect Hyperdrive to a private database using Workers VPC</a>.</p>


<h2 id="hyperdrive-now-supports-custom-tls-ssl-certificates-for-mysql"><a href="/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/">Hyperdrive now supports custom TLS/SSL certificates for MySQL</a></h2>
<p><em>2026-03-19</em></p>
<p>Hyperdrive now supports custom TLS/SSL certificates for MySQL databases, bringing the same certificate options previously available for PostgreSQL to MySQL connections.</p>
<p>You can now configure:</p>
<ul>
<li><strong>Server certificate verification</strong> with <code>VERIFY_CA</code> or <code>VERIFY_IDENTITY</code> SSL modes to verify that your MySQL database server's certificate is signed by the expected certificate authority (CA).</li>
<li><strong>Client certificates</strong> (mTLS) for Hyperdrive to authenticate itself to your MySQL database with credentials beyond username and password.</li>
</ul>
<p>Create a Hyperdrive configuration with custom certificates for MySQL:</p>
<pre><code class="language-bash">&#35; Upload a CA certificate&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create a Hyperdrive with VERIFY_IDENTITY mode&#10;npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;mysql://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-sslmode VERIFY_IDENTITY&#10;</code></pre>
<p>For more information, refer to <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">SSL/TLS certificates for Hyperdrive</a> and <a href="/hyperdrive/examples/connect-to-mysql/">MySQL TLS/SSL modes</a>.</p>


<h2 id="hyperdrive-no-longer-caches-queries-using-stable-postgresql-functions"><a href="/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/">Hyperdrive no longer caches queries using STABLE PostgreSQL functions</a></h2>
<p><em>2026-02-23</em></p>
<p>Hyperdrive now treats queries containing PostgreSQL <code>STABLE</code> functions as uncacheable, in addition to <code>VOLATILE</code> functions.</p>
<p>Previously, only functions <a href="https://www.postgresql.org/docs/current/xfunc-volatility.html">that PostgreSQL categorizes</a> as <code>VOLATILE</code> (for example, <code>RANDOM()</code>, <code>LASTVAL()</code>) were detected as uncacheable. <code>STABLE</code> functions (for example, <code>NOW()</code>, <code>CURRENT_TIMESTAMP</code>, <code>CURRENT_DATE</code>) were incorrectly allowed to be cached.</p>
<p>Because <code>STABLE</code> functions can return different results across different SQL statements within the same transaction, caching their results could serve stale or incorrect data. This change aligns Hyperdrive's caching behavior with PostgreSQL's function volatility semantics.</p>
<p>If your queries use <code>STABLE</code> functions, and you were relying on them being cached, move the function call to your application code and pass the result as a query parameter. For example, instead of <code>WHERE created_at &gt; NOW()</code>, compute the timestamp in your Worker and pass it as <code>WHERE created_at &gt; $1</code>.</p>
<p>Hyperdrive uses text-based pattern matching to detect uncacheable functions. References to function names like <code>NOW()</code> in SQL comments also cause the query to be marked as uncacheable.</p>
<p>For more information, refer to <a href="/hyperdrive/concepts/query-caching/">Query caching</a> and <a href="/hyperdrive/observability/troubleshooting/">Troubleshoot and debug</a>.</p>


<h2 id="connect-to-remote-databases-during-local-development-with-wrangler-dev"><a href="/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/">Connect to remote databases during local development with wrangler dev</a></h2>
<p><em>2025-12-04</em></p>
<p>You can now connect directly to remote databases and databases requiring TLS with <code>wrangler dev</code>.
This lets you run your Worker code locally while connecting to remote databases, without needing to use <code>wrangler dev --remote</code>.</p>
<p>The <code>localConnectionString</code> field and <code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code> environment variable can be used to configure the connection string used by <code>wrangler dev</code>.</p>
<pre><code class="language-jsonc">{&#10;  &quot;hyperdrive&quot;: [&#10;    {&#10;      &quot;binding&quot;: &quot;HYPERDRIVE&quot;,&#10;      &quot;id&quot;: &quot;your-hyperdrive-id&quot;,&#10;      &quot;localConnectionString&quot;: &quot;postgres://user:password@remote-host.example.com:5432/database?sslmode=require&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/local-development/">local development with Hyperdrive</a>.</p>


<h2 id="hyperdrive-now-supports-configuring-the-amount-of-database-connections"><a href="/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/">Hyperdrive now supports configuring the amount of database connections</a></h2>
<p><em>2025-07-03</em></p>
<p>You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.</p>
<p>All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the <a href="/hyperdrive/platform/limits/">Hyperdrive limits of your Workers plan</a>.</p>
<p>This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.</p>
<p>Refer to the <a href="/hyperdrive/concepts/connection-pooling/">Hyperdrive configuration documentation</a> for more information.</p>


<h2 id="hyperdrive-achieves-fedramp-moderate-impact-authorization"><a href="/changelog/post/2025-05-14-hyperdrive-fedramp/">Hyperdrive achieves FedRAMP Moderate-Impact Authorization</a></h2>
<p><em>2025-05-14</em></p>
<p>Hyperdrive has been approved for FedRAMP Authorization and is now available in the <a href="https://marketplace.fedramp.gov/products/FR2000863987">FedRAMP Marketplace</a>.</p>
<p>FedRAMP is a U.S. government program that provides standardized assessment and authorization for cloud products and services. As a result of this product update,
Hyperdrive has been approved as an authorized service to be used by U.S. federal agencies at the Moderate Impact level.</p>
<p>For detailed information regarding FedRAMP and its implications, please refer to the <a href="https://marketplace.fedramp.gov/products/FR2000863987">official FedRAMP documentation for Cloudflare</a>.</p>


<h2 id="hyperdrive-now-supports-custom-tls-ssl-certificates"><a href="/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/">Hyperdrive now supports custom TLS/SSL certificates</a></h2>
<p><em>2025-04-09</em></p>
<p>Hyperdrive now supports more SSL/TLS security options for your database connections:</p>
<ul>
<li>Configure Hyperdrive to verify server certificates with <code>verify-ca</code> or <code>verify-full</code> SSL modes and protect against man-in-the-middle attacks</li>
<li>Configure Hyperdrive to provide client certificates to the database server to authenticate itself (mTLS) for stronger security beyond username and password</li>
</ul>
<p>Use the new <code>wrangler cert</code> commands to create certificate authority (CA) certificate bundles or client certificate pairs:</p>
<pre><code class="language-bash">&#35; Create CA certificate bundle&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create client certificate pair&#10;npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name your-client-cert-name&#10;</code></pre>
<p>Then create a Hyperdrive configuration with the certificates and desired SSL mode:</p>
<pre><code class="language-bash">npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;postgres://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-mtls-certificate-id &lt;CLIENT_CERT_ID&gt;&#10;  &#45;-sslmode verify-full&#10;</code></pre>
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
<pre><code class="language-ts">import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export interface Env {&#10;	HYPERDRIVE: Hyperdrive;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;			disableEval: true, // Required for Workers compatibility&#10;		});&#10;&#10;		const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;		ctx.waitUntil(connection.end());&#10;&#10;		return new Response(JSON.stringify({ results, fields }), {&#10;			headers: {&#10;				&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				&quot;Access-Control-Allow-Origin&quot;: &quot;*&quot;,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a> and <a href="/hyperdrive/get-started/">get started building Workers that connect to MySQL with Hyperdrive</a>.</p>


<h2 id="hyperdrive-reduces-query-latency-by-up-to-90-and-now-supports-ip-access-control-lists"><a href="/changelog/post/2025-03-04-hyperdrive-pooling-near-database-and-ip-range-egress/">Hyperdrive reduces query latency by up to 90% and now supports IP access control lists</a></h2>
<p><em>2025-03-07</em></p>
<p>Hyperdrive now pools database connections in one or more regions close to your database. This means that your uncached queries and new database connections have up to 90% less latency as measured from connection pools.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-regional-pooling-query-latency-improvement.png" alt="Hyperdrive query latency decreases by 90% during Hyperdrive's gradual rollout of regional pooling." /></p>
<p>By improving placement of Hyperdrive database connection pools, Workers' Smart Placement is now more effective when used with Hyperdrive, ensuring that your Worker can be placed as close to your database as possible.</p>
<p>With this update, Hyperdrive also uses <a href="https://www.cloudflare.com/ips/">Cloudflare's standard IP address ranges</a> to connect to your database. This enables you to configure the firewall policies (IP access control lists) of your database to only allow access from Cloudflare and Hyperdrive.</p>
<p>Refer to <a href="/hyperdrive/concepts/how-hyperdrive-works/">documentation on how Hyperdrive makes connecting to regional databases from Cloudflare Workers fast</a>.</p>
<p>This improvement is enabled on all Hyperdrive configurations.</p>


<h2 id="automatic-configuration-for-private-databases-on-hyperdrive"><a href="/changelog/post/2025-01-28-hyperdrive-automated-private-database-configuration/">Automatic configuration for private databases on Hyperdrive</a></h2>
<p><em>2025-01-28</em></p>
<p>Hyperdrive now automatically configures your Cloudflare Tunnel to connect to your private database.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-private-database-automatic-configuration.png" alt="Automatic configuration of Cloudflare Access and Service Token in the Cloudflare dashboard for Hyperdrive." /></p>
<p>When creating a Hyperdrive configuration for a private database, you only need to provide your database credentials and set up a Cloudflare Tunnel within the private network where your database is accessible. Hyperdrive will automatically create the Cloudflare Access, Service Token, and Policies needed to secure and restrict your Cloudflare Tunnel to the Hyperdrive configuration.</p>
<p>To create a Hyperdrive for a private database, you can follow the <a href="/hyperdrive/configuration/connect-to-private-database/">Hyperdrive documentation</a>. You can still manually create the Cloudflare Access, Service Token, and Policies if you prefer.</p>
<p>This feature is available from the Cloudflare dashboard.</p>


<h2 id="up-to-10x-faster-cached-queries-for-hyperdrive"><a href="/changelog/post/2024-12-11-hyperdrive-caching-at-edge/">Up to 10x faster cached queries for Hyperdrive</a></h2>
<p><em>2024-12-11</em></p>
<p>Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.</p>
<p>When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.</p>
<p>This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-edge-caching-metrics.png" alt="Hyperdrive edge caching improves average session duration for database queries" /></p>
<p><em>P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period.</em></p>
<p>This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.</p>
<p>For more details on how Hyperdrive performs query caching, refer to the <a href="/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching">Hyperdrive documentation</a>.</p>



