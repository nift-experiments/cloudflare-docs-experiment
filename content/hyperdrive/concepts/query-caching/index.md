<p>Hyperdrive automatically caches cacheable read queries that your Worker sends to your database when query caching is turned on. This reduces database load and avoids a network round trip to your database for popular queries. Query caching is enabled by default.</p>
<h2 id="what-does-hyperdrive-cache">What does Hyperdrive cache?</h2>
<p>Hyperdrive uses database protocols to differentiate between a mutating query (a query that writes to the database) and a non-mutating query (a read-only query). Hyperdrive caches eligible read-only query responses and does not cache writes.</p>
<p>Besides determining the difference between a <code>SELECT</code> and an <code>INSERT</code>, Hyperdrive also parses the database wire-protocol and uses it to differentiate between a mutating or non-mutating query.</p>
<p>For example, a read query that populates the front page of a news site would be cached:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9098.md")
</div></div>
<p>Mutating queries (including <code>INSERT</code>, <code>UPSERT</code>, or <code>CREATE TABLE</code>) and queries that use functions designated as <a href="https://www.postgresql.org/docs/current/xfunc-volatility.html"><code>volatile</code></a> or <a href="https://www.postgresql.org/docs/current/xfunc-volatility.html"><code>stable</code></a> by PostgreSQL are not cached:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9101.md")
</div></div>
<p>Common PostgreSQL functions that are <strong>not cacheable</strong> include:</p>
<table>
<thead>
<tr>
<th>Function</th>
<th>PostgreSQL volatility category</th>
<th>Cached</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>NOW()</code></td>
<td>STABLE</td>
<td>No</td>
</tr>
<tr>
<td><code>CURRENT_TIMESTAMP</code></td>
<td>STABLE</td>
<td>No</td>
</tr>
<tr>
<td><code>CURRENT_DATE</code></td>
<td>STABLE</td>
<td>No</td>
</tr>
<tr>
<td><code>CURRENT_TIME</code></td>
<td>STABLE</td>
<td>No</td>
</tr>
<tr>
<td><code>LOCALTIME</code></td>
<td>STABLE</td>
<td>No</td>
</tr>
<tr>
<td><code>LOCALTIMESTAMP</code></td>
<td>STABLE</td>
<td>No</td>
</tr>
<tr>
<td><code>TIMEOFDAY()</code></td>
<td>VOLATILE</td>
<td>No</td>
</tr>
<tr>
<td><code>RANDOM()</code></td>
<td>VOLATILE</td>
<td>No</td>
</tr>
<tr>
<td><code>LASTVAL()</code></td>
<td>VOLATILE</td>
<td>No</td>
</tr>
<tr>
<td><code>TXID_CURRENT()</code></td>
<td>STABLE</td>
<td>No</td>
</tr>
</tbody>
</table>
<p>Only functions designated as <code>IMMUTABLE</code> by PostgreSQL (functions whose return value never changes for the same inputs) are compatible with Hyperdrive caching. If your query uses a <code>STABLE</code> or <code>VOLATILE</code> function, move the function call to your application code and pass the resulting value as a query parameter instead.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-use-sql-comments-as-cache-controls">Do not use SQL comments as cache controls</h3>
@markup("md", "content/.markup/bodies/9095.md")
</aside>
<h2 id="default-cache-settings">Default cache settings</h2>
<p>The default caching behavior for Hyperdrive is:</p>
<ul>
<li><code>max_age</code> = 60 seconds (1 minute)</li>
<li><code>stale_while_revalidate</code> = 15 seconds</li>
</ul>
<p>The <code>max_age</code> setting determines the maximum lifetime a query response will be served from cache. Cached responses may be evicted from the cache prior to this time if they are rarely used.</p>
<p>The <code>stale_while_revalidate</code> setting allows Hyperdrive to continue serving stale cache results for an additional period of time while it is revalidating the cache. In most cases, revalidation should happen rapidly.</p>
<p>You can set a maximum <code>max_age</code> of 1 hour.</p>
<h2 id="read-after-write-behavior">Read-after-write behavior</h2>
<p>Hyperdrive does not purge or invalidate cached read query results when your application writes to your database. A later matching <code>SELECT</code> can return the cached result until the configured <code>max_age</code> expires. Hyperdrive can also serve the result during the <code>stale_while_revalidate</code> window while it refreshes the cache in the background.</p>
<p>Writes still go to your database. Hyperdrive only caches eligible read query responses.</p>
<p>This means you should choose a caching strategy based on how fresh each read must be:</p>
<ul>
<li><strong>Use query caching for reads that can tolerate brief staleness.</strong> Good examples include public content, dashboards, search results, product catalogs, and other high-volume reads where a short delay after writes is acceptable.</li>
<li><strong>Lower <code>max_age</code> and <code>stale_while_revalidate</code> when a short stale window works.</strong> This keeps query caching enabled while reducing how long Hyperdrive can serve an older result.</li>
<li><strong>Use a cache-disabled Hyperdrive configuration for reads that must be fresh.</strong> Create a second Hyperdrive configuration with <code>--caching-disabled</code>, bind it alongside your cached configuration, and route those reads through the cache-disabled binding. Good examples include authentication, sessions, permissions, billing state, admin settings, and reads immediately after a write. Refer to <a href="#disable-caching">Disable caching</a> for an example.</li>
<li><strong>Disable query caching everywhere only when most reads must be fresh.</strong> You still get Hyperdrive's connection pooling and fast connection setup when caching is disabled.</li>
</ul>
<p>If an object-relational mapping (ORM) library or authentication library owns the SQL, create separate database clients for the cached and cache-disabled Hyperdrive bindings. Pass the cache-disabled client to the library or module that needs fresh reads, and use the cached client for reads that can tolerate the configured stale window.</p>
<h2 id="disable-caching">Disable caching</h2>
<p>Disable caching on a per-Hyperdrive configuration basis by using the <a href="/workers/wrangler/install-and-update/">Wrangler</a> CLI to set the <code>--caching-disabled</code> option.</p>
<p>To create a separate cache-disabled Hyperdrive configuration against the same database:</p>
<pre><code class="language-sh">npx wrangler hyperdrive create my-database-fresh --connection-string=&quot;&lt;DATABASE_CONNECTION_STRING&gt;&quot; --caching-disabled&#10;</code></pre>
<p>To turn off caching on an existing Hyperdrive configuration:</p>
<pre><code class="language-sh">npx wrangler hyperdrive update &lt;HYPERDRIVE_CONFIG_ID&gt; --caching-disabled&#10;</code></pre>
<p>You can configure multiple Hyperdrive connections from a single application: one connection that enables caching for popular queries, and a second connection for fresh reads that should not use query caching.</p>
<p>When you use multiple Hyperdrive configurations for the same database, account for the total origin connections across configurations. Refer to <a href="/hyperdrive/configuration/tune-connection-pool/">Tune connection pool</a> for guidance.</p>
<p>For example, using database drivers:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9104.md")
</div></div>
<p>The Wrangler configuration remains the same both for PostgreSQL and MySQL.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9105.md")
</div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>For more information, refer to <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive works</a>.</li>
<li>To connect to PostgreSQL, refer to <a href="/hyperdrive/examples/connect-to-postgres/">Connect to PostgreSQL</a>.</li>
<li>For troubleshooting guidance, refer to <a href="/hyperdrive/observability/troubleshooting/">Troubleshoot and debug</a>.</li>
</ul>
