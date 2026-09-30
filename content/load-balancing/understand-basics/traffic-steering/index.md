<p>When requests come to your load balancer, it distributes them across your pools and endpoints according to four factors:</p>
<ol>
<li><a href="/load-balancing/understand-basics/health-details/">Pool and endpoint health</a>: Traffic decisions start with which pools and endpoints are available and should receive traffic.</li>
<li><a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">Pool sets</a>: The preferred way to define new API-managed location routing. A matched pool set can replace pool selection and provide its own steering policy, weights, and fallback pool.</li>
<li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">Global traffic steering</a>: Policies set on your <a href="/load-balancing/load-balancers/">load balancer</a> that route traffic to attached and available pools.</li>
<li><a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/">Local traffic steering</a>: These are policies set on each <a href="/load-balancing/pools/">pool</a> that route traffic to available endpoints within the pool.</li>
</ol>
<p>When a pool or endpoint becomes unhealthy, your load balancer and pools redistribute traffic according to these same policies.</p>
