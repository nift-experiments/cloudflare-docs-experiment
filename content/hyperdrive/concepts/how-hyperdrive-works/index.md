<p>Connecting to traditional centralized databases from Cloudflare's global network which consists of over <a href="https://www.cloudflare.com/network/">300 data center locations</a> presents a few challenges as queries can originate from any of these locations.</p>
<p>If your database is centrally located, queries can take a long time to get to the database and back. Queries can take even longer in situations where you have to establish new connections from stateless environments like Workers, requiring multiple round trips for each Worker invocation.</p>
<p>Traditional databases usually handle a maximum number of connections. With any reasonably large amount of distributed traffic, it becomes easy to exhaust these connections.</p>
<p>Hyperdrive solves these challenges by managing the number of global connections to your origin database, selectively parsing and choosing which query response to cache while reducing loading on your database and accelerating your database queries.</p>
<h2 id="how-hyperdrive-makes-databases-fast-globally">How Hyperdrive makes databases fast globally</h2>
<p>Hyperdrive accelerates database queries by:</p>
<ul>
<li>Performing the connection setup for new database connections near your Workers</li>
<li>Pooling existing connections near your database</li>
<li>Caching query results</li>
</ul>
<p>This ensures you have optimal performance when connecting to your database from Workers (whether your queries are cached or not).</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-comparison.svg" alt="Hyperdrive connection" /></p>
<h3 id="1-edge-connection-setup"><ol>
<li>Edge connection setup</li>
</ol></h3>
<p>When a database driver connects to a database from a Cloudflare Worker <strong>directly</strong>, it will first go through the connection setup. This may require multiple round trips to the database in order to verify and establish a secure connection. This can incur additional network latency due to the distance between your Cloudflare Worker and your database.</p>
<p><strong>With Hyperdrive</strong>, this connection setup occurs between your Cloudflare Worker and Hyperdrive on the edge, as close to your Worker as possible (see diagram, label <em>1. Connection setup</em>). This incurs significantly less latency, since the connection setup is completed within the same location.</p>
<p>Learn more about how connections work between Workers and Hyperdrive in <a href="/hyperdrive/concepts/connection-lifecycle/">Connection lifecycle</a>.</p>
<h3 id="2-connection-pooling"><ol start="2">
<li>Connection Pooling</li>
</ol></h3>
<p>Hyperdrive creates a pool of connections to your database that can be reused as your application executes queries against your database.</p>
<p>The pool of database connections is placed in one or more regions closest to your origin database. This minimizes the latency incurred by roundtrips between your Cloudflare Workers and database to establish new connections. This also ensures that as little network latency is incurred for uncached queries.</p>
<p>If the connection pool has pre-existing connections, the connection pool will try and reuse that connection (see diagram, label <em>2. Existing warm connection</em>).
If the connection pool does not have pre-existing connections, it will establish a new connection to your database and use that to route your query. This aims at reusing and creating the least number of connections possible as required to operate your application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9107.md")
</aside>
<p>Learn more about connection pooling behavior and configuration in <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="reduce-latency-with-placement">Reduce latency with Placement</h3>
@markup("md", "content/.markup/bodies/9106.md")
</aside>
<h3 id="3-query-caching"><ol start="3">
<li>Query Caching</li>
</ol></h3>
<p>Hyperdrive supports caching of non-mutating (read) queries to your database.</p>
<p>When queries are sent via Hyperdrive, Hyperdrive parses the query and determines whether the query is a mutating (write) or non-mutating (read) query.</p>
<p>For non-mutating queries, Hyperdrive caches the response for the configured <code>max_age</code>. When your Worker sends a later query that matches the original, Hyperdrive returns the cached response instead of sending the query back to the origin database.</p>
<p>Caching reduces the burden on your origin database and accelerates the response times for your queries.</p>
<p>Hyperdrive does not invalidate cached read query results when your application writes to your database. If your application needs read-after-write consistency, refer to <a href="/hyperdrive/concepts/query-caching/#read-after-write-behavior">Query caching</a> for guidance on using a separate cache-disabled Hyperdrive configuration for reads that must return fresh data.</p>
<p>Learn more about query caching behavior and configuration in <a href="/hyperdrive/concepts/query-caching/">Query caching</a>.</p>
<h2 id="pooling-mode">Pooling mode</h2>
<p>The Hyperdrive connection pooler operates in transaction mode, where the client that executes the query communicates through a single connection for the duration of a transaction. When that transaction has completed, the connection is returned to the pool.</p>
<p>Hyperdrive supports <a href="https://www.postgresql.org/docs/current/sql-set.html"><code>SET</code> statements</a> for the duration of a transaction or a query. For instance, if you manually create a transaction with <code>BEGIN</code>/<code>COMMIT</code>, <code>SET</code> statements within the transaction will take effect. Moreover, a query that includes a <code>SET</code> command (<code>SET X; SELECT foo FROM bar;</code>) will also apply the <code>SET</code> command. When a connection is returned to the pool, the connection is <code>RESET</code> such that the <code>SET</code> commands will not take effect on subsequent queries.</p>
<p>This implies that a single Worker invocation may obtain multiple connections to perform its database operations and may need to <code>SET</code> any configurations for every query or transaction. It is not recommended to wrap multiple database operations with a single transaction to maintain the <code>SET</code> state. Doing so will affect the performance and scaling of Hyperdrive, as the connection cannot be reused by other Worker isolates for the duration of the transaction.</p>
<p>Hyperdrive supports named prepared statements as implemented in the <code>postgres.js</code> and <code>node-postgres</code> drivers. Named prepared statements in other drivers may have worse performance or may not be supported.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/hyperdrive/concepts/connection-lifecycle/">Connection lifecycle</a></li>
<li><a href="/hyperdrive/concepts/query-caching/">Query caching</a></li>
<li><a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a></li>
</ul>
