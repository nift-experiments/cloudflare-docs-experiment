<p>Hyperdrive maintains a pool of connections to your database that are shared across Worker invocations. You can configure the maximum number of these connections based on your database capacity and application requirements.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9030.md")
</aside>
<h2 id="configure-connection-pool-size">Configure connection pool size</h2>
<p>You can configure the connection pool size using the Cloudflare dashboard, the Wrangler CLI, or the Cloudflare API.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9034.md")
</div></div>
<p>All Hyperdrive configurations have a minimum of 5 connections. The maximum connection count depends on your <a href="/hyperdrive/platform/limits/">Workers plan</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9029.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9028.md")
</aside>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Start conservatively</strong>: Begin with a lower connection count and gradually increase it based on your application's performance.</li>
<li><strong>Monitor database metrics</strong>: Watch your database's connection usage and performance metrics to optimize the connection count.</li>
<li><strong>Consider database limits</strong>: Ensure your configured connection count does not exceed your database's maximum connection limit.</li>
<li><strong>Account for multiple configurations</strong>: If you have multiple Hyperdrive configurations connecting to the same database, consider the total connection count across all configurations.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/hyperdrive/concepts/connection-pooling/">Connection pooling concepts</a></li>
<li><a href="/hyperdrive/concepts/connection-lifecycle/">Connection lifecycle</a></li>
<li><a href="/hyperdrive/observability/metrics/">Metrics and analytics</a></li>
<li><a href="/hyperdrive/platform/limits/">Hyperdrive limits</a></li>
<li><a href="/hyperdrive/concepts/query-caching/">Query caching</a></li>
</ul>
