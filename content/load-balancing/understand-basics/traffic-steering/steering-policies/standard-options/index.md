<p><strong>Standard steering</strong> policies include <strong>Off - Failover</strong> and <strong>Random</strong>.</p>
<p>These are the only steering policies available to non-Enterprise customers who have not purchased <strong>Traffic steering</strong>.</p>
<h2 id="off-failover">Off - Failover</h2>
<p>Failover steering uses the pool order to determine failover priority (the failover order).</p>
<p>Failover directs traffic from unhealthy pools — determined by <a href="/load-balancing/monitors/">health monitors</a> and the <strong>Health Threshold</strong> — to the next healthy pool in the configuration. Customers commonly use this option to set up <a href="/load-balancing/load-balancers/common-configurations/#active---passive-failover">active - passive failover</a>.</p>
<p>If all pools are marked unhealthy, Load Balancing will direct traffic to the fallback pool. The default fallback pool is the last pool listed in the Load Balancing configuration.</p>
<p>If no monitors are attached to the load balancer, it will direct traffic to the primary pool exclusively.</p>
<h3 id="failback-behavior">Failback behavior</h3>
<p>In an active/standby setup, with two origin pools:</p>
<ul>
<li>Traffic always routes to Pool 1 (the primary pool) unless it becomes unhealthy.</li>
<li>If Pool 1 is marked unhealthy, traffic shifts to Pool 2 (the standby pool).</li>
<li>Once Pool 1 becomes healthy again, traffic automatically shifts back to Pool 1, assuming no <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a> or other settings require subsequent requests to stay at Pool 2.</li>
</ul>
<p>This behavior is known as failback and ensures traffic resumes normal routing when the primary pool recovers.</p>
<h2 id="random-steering">Random steering</h2>
<p>Choose <strong>Random</strong> to route traffic to a healthy pool at random. Customers can use this option to set up <a href="/load-balancing/load-balancers/common-configurations/#active---active-failover">active - active failover</a> (also known as round robin), where traffic is split equally between multiple pools.</p>
<p>Similar to setting Weights to direct the amount of traffic going to each endpoint, customers can also set Weights on pools via the <a href="/api/resources/load_balancers/methods/create/">API's</a> <code>random_steering</code> object to determine the percentage of traffic sent to each pool.</p>
