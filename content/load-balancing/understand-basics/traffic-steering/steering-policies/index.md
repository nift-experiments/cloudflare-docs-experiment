<p>Global traffic steering policies decide how a load balancer routes traffic to attached and healthy pools.
<br /></p>
<ul class="directory-listing"><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/">Standard</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">Geo</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/dynamic-steering/">Dynamic</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/proximity-steering/">Proximity</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/steering-policies/least-outstanding-requests/">Least Outstanding Requests</a></li></ul>
<h2 id="edns-client-subnet-ecs-support">EDNS Client Subnet (ECS) support</h2>
<div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/10453.md")
</div> support provides customers with more control over location-based steering during
gray-clouded DNS resolutions and can be used for proximity or geo (country) steering.
<p>Customers can configure their load balancer using the <code>location_strategy</code> parameter, which includes the properties <code>prefer_ecs</code> and <code>mode</code>.</p>
<p><code>prefer_ecs</code> determines whether the ECS geolocation should be preferred as the authoritative location.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;always&quot;</code></td>
<td>Always prefers ECS.</td>
</tr>
<tr>
<td><code>&quot;never&quot;</code></td>
<td>Never prefers ECS.</td>
</tr>
<tr>
<td><code>&quot;proximity&quot;</code></td>
<td>Prefers ECS only when <code>steering_policy=&quot;proximity&quot;</code>.</td>
</tr>
<tr>
<td><code>&quot;geo&quot;</code></td>
<td>Prefers ECS only when <code>steering_policy=&quot;geo&quot;</code> and only supports country-level steering.</td>
</tr>
</tbody>
</table>
<p><code>mode</code> determines the authoritative location when ECS is not preferred, does not exist in the request, or its geolocation lookup is unsuccessful.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&quot;pop&quot;</code></td>
<td>Uses the Cloudflare PoP location.</td>
</tr>
<tr>
<td><code>&quot;resolver_ip&quot;</code></td>
<td>Uses the DNS resolver geolocation data. If the geolocation lookup is unsuccessful, it uses the Cloudflare PoP location.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10452.md")
</aside>
