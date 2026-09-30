<p>Cloudflare Workers can connect to and query your data in both SQL and NoSQL databases, including:</p>
<ul>
<li>Cloudflare's own <a href="/d1/">D1</a>, a serverless SQL-based database.</li>
<li>Traditional hosted relational databases, including Postgres and MySQL, using <a href="/hyperdrive/">Hyperdrive</a> (recommended) to significantly speed up access.</li>
<li>Serverless databases, including Supabase, MongoDB Atlas, PlanetScale, and Prisma.</li>
</ul>
<h3 id="d1-sql-database">D1 SQL database</h3>
<p>D1 is Cloudflare's own SQL-based, serverless database. It is optimized for global access from Workers, and can scale out with multiple, smaller (10GB) databases, such as per-user, per-tenant or per-entity databases. Similar to some serverless databases, D1 pricing is based on query and storage costs.</p>
<table>
<thead>
<tr>
<th>Database</th>
<th>Library or Driver</th>
<th>Connection Method</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/d1/">D1</a></td>
<td><a href="/d1/worker-api/">Workers binding</a>, integrates with <a href="https://www.prisma.io/">Prisma</a>, <a href="https://orm.drizzle.team/">Drizzle</a>, and other ORMs</td>
<td><a href="/d1/worker-api/">Workers binding</a>, <a href="/api/resources/d1/subresources/database/methods/create/">REST API</a></td>
</tr>
</tbody>
</table>
<h3 id="traditional-sql-databases">Traditional SQL databases</h3>
<p>Traditional databases use SQL drivers that use <a href="/workers/runtime-apis/tcp-sockets/">TCP sockets</a> to connect to the database. TCP is the de-facto standard protocol that many databases, such as PostgreSQL and MySQL, use for client connectivity.
These drivers are also widely compatible with your preferred ORM libraries and query builders.</p>
<p>This also includes serverless databases that are PostgreSQL or MySQL-compatible like <a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/supabase/">Supabase</a>, <a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/neon/">Neon</a>, or PlanetScale (either <a href="/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/">MySQL</a> or <a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/planetscale-postgres/">PostgreSQL</a>),
which can be connected to using both native <a href="/hyperdrive/">TCP sockets and Hyperdrive</a> or <a href="/workers/databases/connecting-to-databases/#serverless-databases">serverless HTTP-based drivers</a> (detailed below).</p>
<table>
<thead>
<tr>
<th>Database</th>
<th>Integration</th>
<th>Library or Driver</th>
<th>Connection Method</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/workers/tutorials/postgres/">Postgres</a></td>
<td>Direct connection</td>
<td><a href="https://node-postgres.com/">node-postgres</a>,<a href="https://github.com/porsager/postgres">Postgres.js</a></td>
<td><a href="/workers/runtime-apis/tcp-sockets/">TCP Socket</a> via database driver, using <a href="/hyperdrive/">Hyperdrive</a> for optimal performance (optional, recommended)</td>
</tr>
<tr>
<td><a href="/workers/tutorials/mysql/">MySQL</a></td>
<td>Direct connection</td>
<td><a href="https://github.com/sidorares/node-mysql2">mysql2</a>, <a href="https://github.com/mysqljs/mysql">mysql</a></td>
<td><a href="/workers/runtime-apis/tcp-sockets/">TCP Socket</a> via database driver, using <a href="/hyperdrive/">Hyperdrive</a> for optimal performance (optional, recommended)</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="speed-up-database-connectivity-with-hyperdrive">Speed up database connectivity with Hyperdrive</h3>
@markup("md", "content/.markup/bodies/16591.md")
</aside>
<h3 id="serverless-databases">Serverless databases</h3>
<p>Serverless databases may provide direct connection to the underlying database, or provide HTTP-based proxies and drivers (also known as serverless drivers).</p>
<p>For PostgreSQL and MySQL serverless databases, you can connect to the underlying database directly using the native database drivers and ORMs you are familiar with, using Hyperdrive (recommended) to speed up connectivity and pool database connections. When you use Hyperdrive, your connection pool is managed across all of Cloudflare regions and optimized for usage from Workers.</p>
<p>You can also use serverless driver libraries to connect to the HTTP-based proxies managed by the database provider. These may also provide connection pooling for traditional SQL databases and reduce the amount of roundtrips needed to establish a secure connection, similarly to Hyperdrive.</p>
<table>
<thead>
<tr>
<th>Database</th>
<th>Library or Driver</th>
<th>Connection Method</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://planetscale.com/blog/introducing-the-planetscale-serverless-driver-for-javascript">PlanetScale</a></td>
<td><a href="/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale">Hyperdrive (MySQL)</a>, <a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/planetscale-postgres/">Hyperdrive (PostgreSQL)</a>, <a href="https://github.com/planetscale/database-js">@planetscale/database</a></td>
<td><a href="/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql2/">mysql2</a>, <a href="/hyperdrive/examples/connect-to-mysql/mysql-drivers-and-libraries/mysql/">mysql</a>, <a href="/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/">node-postgres</a>, <a href="/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/postgres-js/">Postgres.js</a>, or API via client library</td>
</tr>
<tr>
<td><a href="https://github.com/supabase/supabase/tree/master/examples/with-cloudflare-workers">Supabase</a></td>
<td><a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/supabase/">Hyperdrive</a>, <a href="https://github.com/supabase/supabase-js">@supabase/supabase-js</a></td>
<td><a href="/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/">node-postgres</a>,<a href="/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/postgres-js/">Postgres.js</a>, or API via client library</td>
</tr>
<tr>
<td><a href="https://www.prisma.io/docs/guides/deployment/deployment-guides/deploying-to-cloudflare-workers">Prisma</a></td>
<td><a href="https://github.com/prisma/prisma">prisma</a></td>
<td>API via client library</td>
</tr>
<tr>
<td><a href="https://blog.cloudflare.com/neon-postgres-database-from-workers/">Neon</a></td>
<td><a href="/hyperdrive/examples/connect-to-postgres/postgres-database-providers/neon/">Hyperdrive</a>, <a href="https://neon.tech/blog/serverless-driver-for-postgres/">@neondatabase/serverless</a></td>
<td><a href="/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/node-postgres/">node-postgres</a>,<a href="/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/postgres-js/">Postgres.js</a>, or API via client library</td>
</tr>
<tr>
<td><a href="https://hasura.io/blog/building-applications-with-cloudflare-workers-and-hasura-graphql-engine/">Hasura</a></td>
<td>API</td>
<td>GraphQL API via fetch()</td>
</tr>
<tr>
<td><a href="https://blog.cloudflare.com/cloudflare-workers-database-integration-with-upstash/">Upstash Redis</a></td>
<td><a href="https://github.com/upstash/upstash-redis">@upstash/redis</a></td>
<td>API via client library</td>
</tr>
<tr>
<td><a href="https://docs.pingcap.com/tidbcloud/integrate-tidbcloud-with-cloudflare">TiDB Cloud</a></td>
<td><a href="https://github.com/tidbcloud/serverless-js">@tidbcloud/serverless</a></td>
<td>API via client library</td>
</tr>
</tbody>
</table>
<p>Once you have installed the necessary packages, use the APIs provided by these packages to connect to your database and perform operations on it. Refer to detailed links for service-specific instructions.</p>
<h2 id="authentication">Authentication</h2>
<p>If your database requires authentication, use Wrangler secrets to securely store your credentials. To do this, create a secret in your Cloudflare Workers project using the following <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret</code></a> command:</p>
<pre><code class="language-sh">wrangler secret put &lt;SECRET_NAME&gt;&#10;</code></pre>
<p>Then, retrieve the secret value in your code using the following code snippet:</p>
<pre><code class="language-js">const secretValue = env.&lt;SECRET_NAME&gt;;&#10;</code></pre>
<p>Use the secret value to authenticate with the external service. For example, if the external service requires an API key or database username and password for authentication, include these in using the relevant service's library or API.</p>
<p>For services that require mTLS authentication, use <a href="/workers/runtime-apis/bindings/mtls">mTLS certificates</a> to present a client certificate.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn how to connect to <a href="/hyperdrive/">an existing PostgreSQL database</a> with Hyperdrive.</li>
<li>Discover <a href="/workers/platform/storage-options/">other storage options available</a> for use with Workers.</li>
<li><a href="/d1/get-started/">Create your first database</a> with Cloudflare D1.</li>
</ul>
