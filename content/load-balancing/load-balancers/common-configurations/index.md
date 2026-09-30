<p>Consider the following sections to understand how to achieve some commonly used load balancer configurations.</p>
<p>This page assumes you understand the Cloudflare <a href="/load-balancing/understand-basics/load-balancing-components/">Load Balancing components</a> and how to create and edit each of them.</p>
<h2 id="active-passive-failover">Active - Passive Failover</h2>
<p>An <strong>active-passive failover</strong> sends traffic to the endpoints in your active pool until a failure threshold (configurable) is reached. At the point of failure, your load balancer then redirects traffic to the passive pool.</p>
<p>This setup ensures uninterrupted service and helps with planned outages, but it might lead to slower traffic overall.</p>
<p>To set up a load balancer with <strong>active-passive failover</strong>:</p>
<ol>
<li>Create a load balancer with two pools (<code>primary</code> and <code>secondary</code>).</li>
<li>In the list of pools, set the following order:
<ol>
<li><code>primary</code></li>
<li><code>secondary</code></li>
</ol>
</li>
<li>For <strong>Traffic Steering</strong>, select <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/#off---failover"><strong>Off</strong></a>.</li>
</ol>
<p>With this setup, your load balancer will direct all traffic to <code>primary</code> until <code>primary</code> has fewer available endpoints than specified in its <strong>Health Threshold</strong>. Only then will your load balancer direct traffic to <code>secondary</code>.</p>
<p>In the event that all pools are marked down, Cloudflare uses the <strong>fallback pool</strong>, which is the option of last resort for successfully sending traffic to an endpoint. Since the fallback pool is a last resort, its health is not taken into account, and Cloudflare reports its status as <strong>No Health</strong>. You can select the fallback pool via the API or in the Cloudflare dashboard. For more on working with fallback pools, refer to <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">Pool-level steering</a>.</p>
<h2 id="active-active-failover">Active - Active Failover</h2>
<p>An <strong>active-active failover</strong> distributes traffic to endpoints in the same pool until the pool reaches its failure threshold (configurable). At the point of failure, your load balancer would then re-direct traffic to the <strong>fallback pool</strong>.</p>
<p>This setup speeds up overall requests, but is more vulnerable to planned or unplanned outages.</p>
<p>To set up a load balancer with <strong>active-active failover</strong>, either:</p>
<ul>
<li>Create a load balancer with a single pool (<code>primary</code>) with multiple endpoints (<code>endpoint-1</code> and <code>endpoint-2</code>) and set the same <a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/#weights"><strong>Weight</strong></a> for each endpoint.</li>
<li>Create a load balancer with two pools (<code>primary</code> and <code>secondary</code>) and — for <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/"><strong>Traffic Steering</strong></a> — select any option except for <strong>Off</strong>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10401.md")
</aside>
