<div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/5117.md")
</div> (also called token IPs) are ephemeral addresses that Gateway assigns to DNS queries so it can associate hostname-based traffic with the correct policy or tunnel at the network layer, where hostname information is not usually available. Refer to [Gateway initial resolved IPs](/cloudflare-one/networks/routes/reserved-ips/#gateway-initial-resolved-ips) for a list of features that depend on this range.
<p>By default, initial resolved IPs are assigned from:</p>
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p>The IPv6 range is not configurable.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5116.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>You have the <a href="/fundamentals/api/reference/permissions/">Cloudflare One Networks Write</a> permission (for API access), or dashboard access to <strong>Networking</strong> &gt; <strong>IP addresses</strong> &gt; <strong>Address space</strong> &gt; <strong>Custom IPs</strong>.</li>
<li>Your new range does not conflict with existing routes or other reserved <a href="/cloudflare-one/networks/routes/reserved-ips/">Cloudflare One subnets</a> in your account.</li>
</ul>
<h2 id="check-your-current-range">Check your current range</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5120.md")
</div></div>
<h2 id="update-your-range">Update your range</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5123.md")
</div></div>
<p>The new CIDR must not conflict with existing private routes or other reserved subnets in your account. If it does, the request fails and the response describes the conflicting route or subnet.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5115.md")
</aside>
<p>The default IPv4 range is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">automatically routed through the Cloudflare One Client</a> and does not require any Split Tunnel configuration. If you configure a custom range, update your <a href="/cloudflare-one/networks/routes/reserved-ips/#split-tunnel-configuration">Split Tunnel configuration</a> so that traffic to the new range routes through the Cloudflare One Client, and remove the old range if it is no longer used by any other reserved IP purpose.</p>
<p>Initial resolved IPs have a TTL of approximately 10 minutes. DNS queries resolved before you change your range continue to use the previous range until that TTL expires. After that, new DNS queries receive an initial resolved IP from the new range.</p>
