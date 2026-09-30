<p>Group multiple health monitors together to create sophisticated health checks for your applications, ensuring more intelligent and resilient traffic steering.</p>
<p>You can group multiple health monitors to build sophisticated health checks that more accurately reflect your application's true health. A Monitor Group allows you to combine several independent monitors, define aggregation logic, and use the collective result to determine the health of an origin pool.</p>
<p>Grouping multiple health monitors enables more intelligent and resilient failover. For example, you can require that both a general API gateway monitor and a specific login service monitor must be healthy for a pool to receive traffic.</p>
<h2 id="availability">Availability</h2>
<p>Monitor Groups are only available to customers on an Enterprise plan with the Load Balancing subscription.</p>
<p>Configuration is available via the <a href="/api/resources/load_balancers/subresources/monitor_groups/methods/create/">API</a> only.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10373.md")
</aside>
<h2 id="how-it-works">How it works</h2>
<p>When you attach a Monitor Group to a pool, the health of that pool is determined by aggregating the results of all enabled monitors within the group.</p>
<p>The sections below explain how monitor groups influence health status, latency, and result handling.</p>
<h2 id="endpoint-health-with-monitor-groups">Endpoint health with Monitor Groups</h2>
<p>A Monitor Group determines an endpoint's health using a combination of critical monitor overrides and quorum-based consensus.</p>
<p><strong>Critical Monitor Override</strong> (<code>must_be_healthy</code>): You can designate a monitor as critical by setting <code>&quot;must_be_healthy&quot;: true</code>. If a monitor with this setting fails its health check against an endpoint, that specific endpoint is immediately marked as unhealthy. This happens regardless of the status reported by other monitors in the group for that same endpoint. This provides a definitive override for essential services.</p>
<p><strong>Quorum-Based Health</strong>: In the absence of a failure from a <code>must_be_healthy</code> monitor, an endpoint's health is determined by a quorum of all other active monitors.</p>
<ul>
<li>An endpoint is considered unhealthy only if more than 50% of its assigned monitors report it as unhealthy.</li>
<li>Monitors marked as <code>&quot;monitoring_only&quot;: true</code> are excluded from the quorum calculation. They will still run and can trigger notifications, but they do not vote on the endpoint's health status.</li>
<li>Monitors marked as <code>disabled</code> will not send monitoring requests to any associated pool. They are also excluded from the quorum calculation.</li>
</ul>
<p>This quorum system prevents an endpoint from being prematurely marked as unhealthy due to a transient failure from a single, non-critical monitor.</p>
<h2 id="latency-for-steering">Latency for Steering</h2>
<p>For pools using Dynamic Steering, the pool's latency is calculated as the average latency of all its enabled, non-monitoring-only monitors. This aggregated RTT (Round Trip Time) value provides a more holistic view of an origin's performance and is used to make steering decisions.</p>
<h2 id="result-handling-for-different-intervals">Result handling for different intervals</h2>
<p>If monitors in a group have different check intervals, the group uses the last available result from each monitor until it is refreshed. For example, if one monitor runs every 10 seconds and another every 30 seconds, the 30-second monitor's result is considered valid for the full 30 seconds until its next run completes.</p>
