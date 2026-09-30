<h1 id="changelog">Changelog</h1>

<h2 id="deprecate-legacy-workers-kv-namespace-api-routes"><a href="/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/">Deprecate legacy Workers KV namespace API routes</a></h2>
<p><em>2026-07-15</em></p>
<p>The legacy Workers KV API routes under <code>/accounts/{account_id}/workers/namespaces/*</code> are deprecated as of July 15, 2026, and will stop working on October 15, 2026. Migrate to the documented <a href="/api/resources/kv/">Workers KV API</a> routes under <code>/accounts/{account_id}/storage/kv/namespaces/*</code> before that date.</p>
<p>The legacy and replacement routes are interchangeable. They accept the same request parameters and return the same response payloads. To migrate, update the URL path from <code>/workers/namespaces/</code> to <code>/storage/kv/namespaces/</code>.</p>
<h4 id="2026-07-15-kv-legacy-namespace-routes-deprecation-what-you-need-to-do">What you need to do</h4>
<p>Update any integration that calls a route under <code>/accounts/{account_id}/workers/namespaces/</code> to use the equivalent route under <code>/accounts/{account_id}/storage/kv/namespaces/</code>. The migration is a direct URL path substitution — request parameters and response payloads are identical:</p>
<ul>
<li><code>GET</code> and <code>POST /accounts/{account_id}/workers/namespaces</code> → <code>GET</code> and <code>POST /accounts/{account_id}/storage/kv/namespaces</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/keys</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/metadata/{key_name}</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}/values/{key_name}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}</code></li>
</ul>
<p>For more information about the deprecation timeline, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="reduced-minimum-cache-ttl-for-workers-kv-to-30-seconds"><a href="/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/">Reduced minimum cache TTL for Workers KV to 30 seconds</a></h2>
<p><em>2026-01-30T12:00:00+00:00</em></p>
<p>The minimum <code>cacheTtl</code> parameter for Workers KV has been reduced from 60 seconds to 30 seconds. This change applies to both <code>get()</code> and <code>getWithMetadata()</code> methods.</p>
<p>This reduction allows you to maintain more up-to-date cached data and have finer-grained control over cache behavior. Applications requiring faster data refresh rates can now configure cache durations as low as 30 seconds instead of the previous 60-second minimum.</p>
<p>The <code>cacheTtl</code> parameter defines how long a KV result is cached at the global network location it is accessed from:</p>
<pre><code class="language-js">// Read with custom cache TTL&#10;const value = await env.NAMESPACE.get(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds (previously 60)&#10;});&#10;&#10;// getWithMetadata also supports the reduced cache TTL&#10;const valueWithMetadata = await env.NAMESPACE.getWithMetadata(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds&#10;});&#10;</code></pre>
<p>The default cache TTL remains unchanged at 60 seconds. Upgrade to the latest version of Wrangler to be able to use 30 seconds <code>cacheTtl</code>.</p>
<p>This change affects all KV read operations using the binding API. For more information, consult the <a href="/kv/api/read-key-value-pairs/#cachettl-parameter">Workers KV cache TTL documentation</a>.</p>


<h2 id="new-workers-kv-dashboard-ui"><a href="/changelog/post/2026-01-20-kv-dash-ui-homepage/">New Workers KV Dashboard UI</a></h2>
<p><em>2026-01-20</em></p>
<p><a href="/kv/">Workers KV</a> has an updated dashboard UI with new dashboard styling that makes it easier to navigate and see analytics and settings for a KV namespace.</p>
<p>The new dashboard features a <strong>streamlined homepage</strong> for easy access to your namespaces and key operations, with consistent design with the rest of the dashboard UI updates. It also provides an <strong>improved analytics view</strong>.</p>
<p><img src="/assets/upstream/images/changelog/kv/kv-dash-ui-homepage.png" alt="New KV Dashboard Homepage" /></p>
<p>The updated dashboard is now available for all Workers KV users. Log in to the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a> to start exploring the new interface.</p>


<h2 id="workers-kv-completes-hybrid-storage-provider-rollout-for-improved-performance-fault-tolerance"><a href="/changelog/post/2025-08-22-kv-performance-improvements/">Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance</a></h2>
<p><em>2025-08-22 12:00:00 UTC</em></p>
<p>Workers KV has completed rolling out performance improvements across all KV namespaces, providing a significant latency reduction on read operations for all KV users. This is due to architectural changes to KV's underlying storage infrastructure, which introduces a new metadata later and substantially improves redundancy.</p>
<p><img src="/assets/upstream/images/kv/changelog/kv-hybrid-providers-performance-improvements.png" alt="Workers KV latency improvements showing P95 and P99 performance gains in Europe, Asia, Africa and Middle East regions as measured within KV's internal storage gateway worker." /></p>
<h4 id="2025-08-22-kv-performance-improvements-performance-improvements">Performance improvements</h4>
<p>The new hybrid architecture delivers substantial latency reductions throughout Europe, Asia, Middle East, Africa regions. Over the past 2 weeks, we have observed the following:</p>
<ul>
<li><strong>p95 latency</strong>: Reduced from ~150ms to ~50ms (67% decrease)</li>
<li><strong>p99 latency</strong>: Reduced from ~350ms to ~250ms (29% decrease)</li>
</ul>


<h2 id="read-multiple-keys-from-workers-kv-with-bulk-reads"><a href="/changelog/post/2025-04-10-kv-bulk-reads/">Read multiple keys from Workers KV with bulk reads</a></h2>
<p><em>2025-04-17</em></p>
<p>You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.</p>
<p>This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by <a href="/workers/platform/limits/#simultaneous-open-connections">Workers simultaneous connection limits</a>.</p>
<pre><code class="language-js">// Read single key&#10;const key = &quot;key-a&quot;;&#10;const value = await env.NAMESPACE.get(key);&#10;&#10;// Read multiple keys&#10;const keys = [&quot;key-a&quot;, &quot;key-b&quot;, &quot;key-c&quot;, ...] // up to 100 keys&#10;const values : Map&lt;string, string?&gt; = await env.NAMESPACE.get(keys);&#10;&#10;// Print the value of &quot;key-a&quot; to the console.&#10;console.log(`The first key is ${values.get(&quot;key-a&quot;)}.`)&#10;</code></pre>
<p>Consult the <a href="/kv/api/read-key-value-pairs/">Workers KV Read key-value pairs API</a> for full details on Workers KV's new bulk reads support.</p>


<h2 id="workers-kv-namespace-limits-increased-to-1000"><a href="/changelog/post/2025-01-27-kv-increased-namespaces-limits/">Workers KV namespace limits increased to 1000</a></h2>
<p><em>2025-01-28</em></p>
<p>You can now have up to 1000 Workers KV namespaces per account.</p>
<p>Workers KV namespace limits were increased from 200 to 1000 for all accounts. Higher limits for Workers KV namespaces enable better organization of key-value data, such as by category, tenant, or environment.</p>
<p>Consult the <a href="/kv/platform/limits/">Workers KV limits documentation</a> for the rest of the limits. This increased limit is available for both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>



