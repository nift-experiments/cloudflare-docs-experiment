<p><strong>Least Outstanding Requests steering</strong> allows you to route traffic to endpoints that currently have the lowest number of outstanding requests.</p>
<p>This steering policy selects an endpoint by taking into consideration endpoint weights, as well as each endpoint's number of in-flight requests. Endpoints with more pending requests are weighted proportionately less in relation to others.</p>
<p>Least Outstanding Requests steering is best to use if your endpoints are easily overwhelmed by a spike in concurrent requests. It supports <a href="/load-balancing/understand-basics/adaptive-routing/">adaptive routing</a> and <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>.</p>
<h2 id="configure-via-the-api">Configure via the API</h2>
<pre><code class="language-json">{&#10;  &quot;origin_steering&quot;: {&#10;    &quot;policy&quot;: &quot;least_outstanding_requests&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Refer to the <a href="/api/resources/load_balancers/subresources/pools/methods/update/">API documentation</a> for more information on the pool configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10464.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Least Outstanding Requests steering can be configured for pools that are part of <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">DNS-only load balancers</a>, but is only supported in a no-operation form. When endpoint steering logic is applied for a pool on a DNS-only load balancer, all endpoint outstanding request counts are considered to be zero, meaning traffic is served solely based on endpoint weights.</p>
<p>Although it is configurable, it is not recommended to associate pools that use Least Outstanding Requests steering with DNS-only load balancers due to its partial support.</p>
