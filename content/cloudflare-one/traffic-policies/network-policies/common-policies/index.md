<p>The following policies are commonly used to secure network traffic. Network policies are evaluated in order from top to bottom, and the first matching policy applies. Place more specific Allow policies above broader Block policies.</p>
<p>For a baseline set of recommended policies, refer to <a href="/learning-paths/secure-internet-traffic/build-network-policies/recommended-network-policies/">Secure your Internet traffic and SaaS apps</a>.</p>
<p>Refer to the <a href="/cloudflare-one/traffic-policies/network-policies/">network policies page</a> for a comprehensive list of other selectors, operators, and actions.</p>
<h2 id="block-unauthorized-applications">Block unauthorized applications</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6432.md")
</aside>
<p>To minimize the risk of <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/6433.md")
</div>, some organizations choose to limit their users' access to certain web-based tools and applications. For example, the following policy blocks known AI tools:
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6436.md")
</div></div>
<h2 id="check-user-identity">Check user identity</h2>
<p>Configure access on a per user or group basis by adding <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based conditions</a> to your policies.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6439.md")
</div></div>
<h2 id="enforce-device-posture">Enforce device posture</h2>
<p>Require devices to have certain software installed or other configuration attributes. For instructions on enabling a device posture check, refer to the <a href="/cloudflare-one/reusable-components/posture-checks/">device posture section</a>. For example, you can use a list of <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/">device serial numbers</a> to ensure users can only access an application if they connect with the Cloudflare One Client from a company device:</p>
<p>In the following example, you can use a list of <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/corp-device/">device serial numbers</a> to ensure users can only access an application if they connect with the Cloudflare One Client from a company device:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6443.md")
</div></div>
<h2 id="enforce-session-duration">Enforce session duration</h2>
<p>To require users to re-authenticate after a certain amount of time has elapsed, configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client sessions</a>.</p>
<h2 id="allow-only-approved-traffic">Allow only approved traffic</h2>
<p>Restrict user access to only the specific sites or applications configured in your <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>. This pattern uses two policies: an Allow policy to permit HTTP/HTTPS traffic, followed by a Block policy to deny everything else. Place the Allow policy above the Block policy so that matching traffic is allowed before the catch-all block applies.</p>
<h3 id="1-allow-http-and-https-traffic"><ol>
<li>Allow HTTP and HTTPS traffic</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6446.md")
</div></div>
<h3 id="2-block-all-other-traffic"><ol start="2">
<li>Block all other traffic</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6449.md")
</div></div>
<h2 id="filter-https-traffic-when-inspecting-on-all-ports">Filter HTTPS traffic when inspecting on all ports</h2>
<p>If your organization blocks traffic by default with a Network policy and you want to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">inspect HTTP traffic on all ports</a>, you need to explicitly allow HTTP and TLS traffic to filter it.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6452.md")
</div></div>
<h2 id="restrict-private-network-access-to-proxy-endpoint-users">Restrict private network access to proxy endpoint users</h2>
<p>When using proxy endpoints, by default all devices added to the proxy endpoint can access your internal applications and services connected through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>. To restrict access and add an additional layer of security, create the following policies.</p>
<h3 id="source-ip-proxy-endpoints">Source IP proxy endpoints</h3>
<p>When using <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a>, restrict access to only users connecting through the proxy endpoint from specific source IPs.</p>
<h4 id="1-allow-proxy-endpoint-traffic-from-specific-source-ips"><ol>
<li>Allow proxy endpoint traffic from specific source IPs</li>
</ol></h4>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6455.md")
</div></div>
<h4 id="2-block-all-other-proxy-endpoint-traffic-to-private-network"><ol start="2">
<li>Block all other proxy endpoint traffic to private network</li>
</ol></h4>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6458.md")
</div></div>
<h3 id="authorization-proxy-endpoints">Authorization proxy endpoints</h3>
<p>When using <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">authorization proxy endpoints</a>, add an additional layer of security by restricting access to only users connecting from specific source IPs. This prevents unauthorized access even if user credentials are compromised.</p>
<h4 id="1-allow-proxy-endpoint-traffic-from-specific-source-ips-1"><ol>
<li>Allow proxy endpoint traffic from specific source IPs</li>
</ol></h4>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6461.md")
</div></div>
<h4 id="2-block-all-other-proxy-endpoint-traffic-to-private-network-1"><ol start="2">
<li>Block all other proxy endpoint traffic to private network</li>
</ol></h4>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6464.md")
</div></div>
<h2 id="restrict-access-to-private-networks">Restrict access to private networks</h2>
<p>Restrict access to resources which you have connected through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>
<p>The following example consists of two policies: the first allows specific users to reach your application, and the second blocks all other traffic.</p>
<h3 id="1-allow-company-employees"><ol>
<li>Allow company employees</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6467.md")
</div></div>
<h3 id="2-block-everyone-else"><ol start="2">
<li>Block everyone else</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6470.md")
</div></div>
<h2 id="override-ip-address">Override IP address</h2>
<p>Override traffic directed toward a specific IP address with a different IP address.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6473.md")
</div></div>
