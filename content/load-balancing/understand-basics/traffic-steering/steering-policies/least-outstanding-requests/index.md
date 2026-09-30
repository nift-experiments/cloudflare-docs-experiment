<p><strong>Least Outstanding Requests steering</strong> allows you to route traffic to pools that currently have the lowest number of outstanding requests.</p>
<p>This steering policy selects a pool by taking into consideration <code>random_steering</code> weights, as well as each pool's number of in-flight requests. Pools with more pending requests are weighted proportionately less in relation to others.</p>
<p>Least Outstanding Requests steering is best to use if your pools are easily overwhelmed by a spike in concurrent requests. This steering method lends itself to applications that value server health above latency, geographic alignment, or other metrics. It takes into account the <a href="/load-balancing/understand-basics/health-details/#how-a-pool-becomes-unhealthy">pool's health status</a>, <a href="/load-balancing/understand-basics/adaptive-routing/">adaptive routing</a>, and <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>.</p>
<h2 id="configure-via-the-api">Configure via the API</h2>
<pre><code class="language-json">{&#10;  &quot;steering_policy&quot;: &quot;least_outstanding_requests&quot;&#10;}&#10;</code></pre>
<p>Refer to the <a href="/api/resources/load_balancers/methods/update/">API documentation</a> for more information on the load balancer configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10451.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Least Outstanding Requests steering can be configured for <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">DNS-only load balancers</a>, but is only supported in a no-operation form. For DNS-only load balancers, all pool outstanding request counts are considered to be zero, meaning traffic is served solely based on <code>random_steering</code> weights.</p>
<p>Although it is configurable, it is not recommended to use Least Outstanding Requests steering for DNS-only load balancers due to its partial support.</p>
