<p>Magic Transit uses health check probes to determine the status of tunnels. Cloudflare uses this information to steer traffic through the best available route and warn you about potential issues with a tunnel. Service-level indicators (SLIs) and service-level objectives (SLOs) combine to determine when Cloudflare sends you tunnel health alerts. Refer to <a href="/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/">How Cloudflare calculates tunnel health alerts</a> for more information about SLIs and SLOs.</p>
<p>There are two types of health checks available: endpoint and tunnel health checks.</p>
<ul>
<li>
<p>Endpoint health checks evaluate connectivity from Cloudflare distributed data centers to your origin network. Endpoint probes flow over available tunnels to provide a broad picture of Internet health and do not inform tunnel selection or steering logic.</p>
<p>Cloudflare global network servers issue endpoint health checks outside of customer network namespaces and typically target endpoints beyond the tunnel-terminating border router.</p>
<p>During onboarding, you specify IP addresses to configure endpoint health checks.</p>
</li>
<li>
<p>Tunnel health checks monitor the status of the tunnels that route traffic from Cloudflare to your origin network. Magic Transit relies on health checks to steer traffic to the best available routes.</p>
<p>During onboarding, you specify the tunnel endpoints or tunnel health check targets that the tunnel probes from Cloudflare's global network will monitor.</p>
<p>You can access tunnel health check results through the API. Cloudflare aggregates these results from individual health check results on Cloudflare servers.</p>
</li>
</ul>
<p>Refer to <a href="/magic-transit/reference/tunnel-health-checks/">Tunnel health checks</a> for a deep dive into the different types of health checks, what they do, and how they work.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10639.md")
</aside>
<p>Refer to the following pages for details on how to use the various network health checks available.</p>
<ul class="directory-listing"><li><a href="/magic-transit/network-health/run-endpoint-health-checks/">Run endpoint health checks (beta)</a></li><li><a href="/magic-transit/network-health/check-tunnel-health-dashboard/">Check tunnel health in the dashboard</a></li><li><a href="/magic-transit/network-health/update-tunnel-health-checks-frequency/">Update tunnel health checks frequency</a></li><li><a href="/magic-transit/network-health/configure-tunnel-health-alerts/">Configure tunnel health alerts</a></li><li><a href="/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/">How Cloudflare calculates tunnel health alerts</a></li></ul>
