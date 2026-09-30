<p>You can configure Spectrum with Cloudflare <a href="/load-balancing/">Load Balancing</a> to provide TCP healthchecks, failover, and traffic steering, bringing resiliency to your Spectrum applications.</p>
<p>For an overview of how Cloudflare Load Balancing works refer to <a href="/load-balancing/understand-basics/load-balancing-components/">Load Balancing components</a>. For setup guidance refer to <a href="/load-balancing/additional-options/spectrum/">Add load balancing to Spectrum applications</a>.</p>
<h2 id="tcp-health-checks">TCP health checks</h2>
<p>You can configure a Cloudflare load balancer to probe any TCP port for an accepted connection, which is in addition to HTTP and HTTPS probing capabilities.</p>
<p>Health checks are optional within a load balancer. However, without a health check, the load balancer will distribute traffic to all endpoints in the first pool. With the health checks enabled, hosts that have gone into an error state will not receive traffic, maintaining uptime. This allows you to enable intelligent failover within a pool of hosts or amongst multiple pools.</p>
<p>The example below shows a TCP health check configuration for an application running on port 2408 with a refresh rate every 30 seconds. You can configure TCP health checks through the dashboard or through Cloudflare's API.</p>
<details class="nb-details"><summary>TCP health check - Dashboard example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13876.md")
</div></details>
<details class="nb-details"><summary>TCP health check - API example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13877.md")
</div></details>
<h2 id="traffic-steering">Traffic steering</h2>
<p>All traffic steering policies are available for transport load balancing through Spectrum. Refer to the Load Balancing documentation to learn more about the available <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">global traffic steering</a> and <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/">endpoint steering</a> options.</p>
<h2 id="weights">Weights</h2>
<p><a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights">Endpoint weights</a> allow you to have endpoints with different capacity or to split traffic amongst hosts for any other reason.</p>
<p>Weight configured within a load balancer pool will be honored with load balancing through Spectrum.</p>
<h2 id="requirements-and-limitations">Requirements and limitations</h2>
<ul>
<li>
<p>Load Balancing <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>, <a href="/load-balancing/understand-basics/adaptive-routing/#failover-across-pools">failover across pools</a>, and <a href="/load-balancing/additional-options/load-balancing-rules/">custom rules</a> are not supported by Spectrum.</p>
</li>
<li>
<p>UDP health checks are only available with public monitoring. TCP can be used with both public and private monitoring.</p>
</li>
<li>
<p>This feature requires an Enterprise plan. If you would like to upgrade, contact your account team.</p>
</li>
</ul>
