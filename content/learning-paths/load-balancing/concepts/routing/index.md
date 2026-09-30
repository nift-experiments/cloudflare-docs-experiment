<p>Before, we covered how requests move from load balancers to pools and then from pools to individual servers.</p>
<p>What we did not mention, however, was <em>how</em> the load balancer and pools make those decisions.</p>
<p>This is a concept known as routing.</p>
<h2 id="how-it-works">How it works</h2>
<p>Generally, there are five questions involved with routing:</p>
<ol>
<li>By default, how does the load balancer distribute requests to pools?</li>
<li>By default, how do pools distribute requests to individual servers?</li>
<li>Within a pool, which servers are healthy?</li>
<li>Within a load balancer, which pools are healthy?</li>
<li>Are there any specialized routing rules?</li>
</ol>
<h3 id="distributing-requests-to-pools">Distributing requests to pools</h3>
<p>A load balancer's <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policy</a> controls how the load balancer distributes requests to pools.</p>
<p>Routing decisions can be based on proximity, pool performance, geography, and more.</p>
<h3 id="distributing-requests-within-pools">Distributing requests within pools</h3>
<p>Once the request reaches a pool, that pool's <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/">endpoint steering policy</a> controls how each pool distributes requests to the servers in the pool.</p>
<p>These decisions can be based on default percentages of traffic sent to individual servers (also known as the <strong>Weight</strong>), aspects of the request (such as source IP address), or both.</p>
<h3 id="endpoint-health">Endpoint health</h3>
<p>If an endpoint fails a health check - which would mark it as unhealthy - its pool will adjust routing according to its endpoint steering policy.</p>
<p>Both new and existing requests will go to healthy endpoints in the pool, ignoring the unhealthy endpoint.</p>
<h3 id="pool-health">Pool health</h3>
<p>With enough unhealthy endpoints, the pool itself may be considered unhealthy as well.</p>
<p>When a pool reaches <strong>Critical</strong> health, your load balancer will begin diverting traffic according to its <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">Traffic steering policy</a>:</p>
<ul>
<li>
<p><strong>Off</strong>:</p>
<ul>
<li>If the active pool becomes unhealthy, traffic goes to the next pool in order.</li>
<li>If an inactive pool becomes unhealthy, traffic continues to go to the active pool (but would skip over the unhealthy pool in the failover order).</li>
</ul>
</li>
<li>
<p><strong>All other methods</strong>: Traffic is distributed across all remaining pools according to the traffic steering policy.</p>
</li>
</ul>
<h4 id="fallback-pools">Fallback pools</h4>
<p>Often, load balancers have a special pool known as the <strong>Fallback Pool</strong>, which receives traffic no matter what.</p>
<p>This pool is meant to be the pool of last resort, meaning that its health is not taken into account when directing traffic.</p>
<p>Fallback pools are important because traffic still might be coming to your load balancer even when all the pools are unreachable (disabled or unhealthy). Your load balancer needs somewhere to route this traffic, so it will send it to the fallback pool.</p>
<h3 id="specialized-routing">Specialized routing</h3>
<p>Finally, specific settings can also affect the ways a load balancer distributes traffic, such as:</p>
<ul>
<li>Routing based on <a href="/load-balancing/additional-options/load-balancing-rules/">specific aspects</a> of the request.</li>
<li>Sending all requests from a <a href="/load-balancing/understand-basics/session-affinity/">specific end user</a> to the same server, preserving information about their user session like items in a shopping cart.</li>
</ul>
