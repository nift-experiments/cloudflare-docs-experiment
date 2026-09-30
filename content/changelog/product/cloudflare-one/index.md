<h1 id="changelog">Changelog</h1>

<h2 id="access-for-infrastructure-now-supports-tagged-targets-and-tag-based-target-criteria"><a href="/changelog/post/2026-09-15-infrastructure-target-tags/">Access for Infrastructure now supports tagged targets and tag-based target criteria</a></h2>
<p><em>2026-09-15</em></p>
<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now integrates with <a href="/resource-tagging/">Resource Tagging</a>. You can attach key-value tags to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target">infrastructure targets</a> and use them in access policies.</p>
<p>You can manage tags on targets inline when you create or edit a target or through the central <a href="/resource-tagging/how-to/manage-tags/">Resource Tagging API</a>. Cloudflare keeps tags in sync across both methods.</p>
<p>Infrastructure applications also support a target criteria model with <code>include</code>, <code>require</code>, and <code>exclude</code> operators. Each operator can match targets by hostname, tag, or both.</p>
<ul>
<li><strong>Include</strong> matches targets that have any of the specified values.</li>
<li><strong>Require</strong> matches targets that have all of the specified values.</li>
<li><strong>Exclude</strong> rejects targets that have any of the specified values.</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-one/access/tags-in-infra-app.png" alt="Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol" /></p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Add an infrastructure application</a>.</p>


<h2 id="improved-ios-tap-to-type-experience-for-browser-isolation"><a href="/changelog/post/2026-09-09-ios-tap-to-type/">Improved iOS tap-to-type experience for Browser Isolation</a></h2>
<p><em>2026-09-09</em></p>
<p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> has improved the tap-to-type experience for users on iOS devices.</p>
<p>Previously, Browser Isolation displayed a full-screen overlay with the message <code>tap to type</code> when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.</p>
<p>If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.</p>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/tap-to-type.jpg" alt="Inline tap-to-type prompt over a focused text field in Browser Isolation" /></p>
<p>iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.</p>
<p>For more information on why this interaction is required, refer to <a href="/cloudflare-one/remote-browser-isolation/known-limitations/#ios">iOS limitations</a>.</p>


<h2 id="define-custom-applications-for-breakout-and-prioritized-traffic-from-the-cloudflare-one-appliance-dashboard"><a href="/changelog/post/2026-09-02-appliance-custom-application-traffic-steering/">Define custom applications for breakout and prioritized traffic from the Cloudflare One Appliance dashboard</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now define <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#create-edit-or-delete-a-custom-application">custom applications</a> for <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">breakout</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">prioritized</a> traffic on the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard, without calling the API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-custom-application-traffic-steering.gif" alt="Adding a custom application by hostname, IP subnet, and source subnet from the Traffic Steering tab of an appliance profile" /></p>
<ul>
<li>In <strong>Traffic Steering</strong> &gt; <strong>Breakout traffic</strong> or <strong>Prioritized traffic</strong>, select <strong>Assign application traffic</strong> &gt; <strong>Add</strong> to create a custom application matched by <strong>Hostnames</strong>, <strong>IP subnets</strong>, and/or the new <strong>Source subnets</strong> field, alongside Cloudflare-managed applications.</li>
<li>Edit or delete an existing custom application from the same panel, no API round-trip required.</li>
<li><strong>Source subnets</strong> lets you match traffic by its source IP range, complementing the existing <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">source LAN interface breakout criteria</a>.</li>
</ul>
<p>This complements the existing API and Terraform workflow for managing applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/">Breakout traffic</a> and <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/prioritized-traffic/">Prioritized traffic</a>.</p>


<h2 id="configure-dhcp-options-from-the-dashboard-on-cloudflare-one-appliance"><a href="/changelog/post/2026-09-02-appliance-dhcp-options-ui/">Configure DHCP options from the dashboard on Cloudflare One Appliance</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now configure <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">custom DHCP options</a> directly from the dashboard when the <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> is acting as the DHCP server for a LAN.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-09-01-appliance-dhcp-options-ui.gif" alt="Adding a custom DHCP option to a LAN's DHCP server from the Network Configuration tab of an appliance profile" /></p>
<ul>
<li>In <strong>LAN configuration</strong>, under <strong>DHCP server options</strong>, select <strong>Add DHCP option</strong> to choose from common options for PXE / iPXE boot, VoIP phone provisioning, and vendor-specific configuration, or select <strong>Add custom option</strong> to enter your own option code, type, and value.</li>
<li>This complements the existing <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/#configure-dhcp-options">API and Terraform workflow</a> for configuring DHCP options.</li>
</ul>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="create-multiple-cloudflare-tunnel-and-cloudflare-mesh-routes-at-once"><a href="/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/">Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now create multiple <a href="/tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> routes from the Routes page in a single action, instead of submitting one route at a time.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-09-01-tunnel-mesh-bulk.gif" alt="Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page" /></p>
<p>When creating a route, you can now:</p>
<ul>
<li><strong>Add multiple destinations at once</strong> — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.</li>
<li><strong>Queue up multiple routes</strong> — Select <strong>Add another</strong> to stage additional routes, including different types or connectors, before creating them all in one action.</li>
<li><strong>Retry only what failed</strong> — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.</li>
</ul>
<p>The same Routes UI already supports bulk creation for <a href="/cloudflare-wan/">Cloudflare WAN</a> static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, refer to <a href="/cloudflare-one/networks/routes/add-routes/">Add routes</a>.</p>


<h2 id="mcp-server-portals-support-mcp-2026-07-28-specification"><a href="/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/">MCP server portals support MCP 2026-07-28 specification</a></h2>
<p><em>2026-08-25</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support the stateless MCP <code>2026-07-28</code> specification for client and upstream server connections.</p>
<p>The portal's <code>/mcp</code> endpoint automatically accepts stateless MCP <code>2026-07-28</code> requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP <code>2026-07-28</code> support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.</p>
<p>SSE connections continue to use the legacy protocol. For details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport">MCP server portal transport and protocol compatibility</a>.</p>


<h2 id="download-the-cloudflare-one-virtual-appliance-for-your-hypervisor-from-the-dashboard"><a href="/changelog/post/2026-08-24-virtual-appliance-self-serve-download/">Download the Cloudflare One Virtual Appliance for your hypervisor from the dashboard</a></h2>
<p><em>2026-08-24</em></p>
<p>When you register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a>, you can now select your hypervisor and download the appliance directly from the dashboard — no need to look up asset URLs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-08-24-virtual-appliance-self-serve-download.png" alt="Selecting a hypervisor and downloading the Cloudflare One Virtual Appliance from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong>, choose <strong>Virtual appliance</strong>, then select your hypervisor: <strong>VMware ESXi</strong>, <strong>Proxmox</strong>, or <strong>libvirt/KVM</strong>.</li>
<li>Download the OVA image (VMware ESXi) or the install script (Proxmox and libvirt/KVM) for the selected hypervisor.</li>
<li>Use <strong>View setup guide</strong> to open deployment instructions for your platform.</li>
</ul>
<p>This complements the existing self-serve <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">registration and license key generation</a> in the dashboard.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#configure-a-virtual-machine">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="independent-mfa-supports-fido2-for-infrastructure-applications"><a href="/changelog/post/2026-08-12-fido2-keys-infrastructure-ssh/">Independent MFA supports FIDO2 for infrastructure applications</a></h2>
<p><em>2026-08-12</em></p>
<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Infrastructure</a> applications support independent multi-factor authentication (MFA) with FIDO2 keys. You can allow <code>ssh_fido2_key</code>, <code>piv_key</code>, or both in application-level and policy-level MFA settings.</p>
<p>Users enroll FIDO2 keys through the App Launcher and connect with the generated SSH identity. FIDO2 keys for SSH are separate from browser-based WebAuthn security keys and Personal Identity Verification (PIV) keys.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-fido2-key-for-infrastructure-apps">Enroll a FIDO2 key for infrastructure apps</a> and <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Configure MFA for infrastructure applications</a>.</p>


<h2 id="mcp-protocol-detection-and-ai-security-dashboard"><a href="/changelog/post/2026-08-12-mcp-detection-and-dashboard/">MCP protocol detection and AI Security dashboard</a></h2>
<p><em>2026-08-12</em></p>
<p>Cloudflare Gateway now automatically detects <a href="https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">Model Context Protocol (MCP)</a> traffic flowing through your network. MCP is the standard protocol used by AI agents to connect to external tools and data sources. Gateway identifies MCP requests by inspecting protocol-specific headers and payload characteristics.</p>
<h4 id="2026-08-12-mcp-detection-and-dashboard-mcp-policy-selector">MCP policy selector</h4>
<p>A new <strong>Is MCP</strong> selector (<code>experimental.is_mcp</code>) is available in <a href="/cloudflare-one/traffic-policies/http-policies/#is-mcp">HTTP policies</a>. Use this selector to build Gateway rules that allow, block, or isolate MCP traffic.</p>
<p>This selector is currently in beta and may change before general availability.</p>
<p>For example, the following policy blocks MCP traffic that does not arrive through an approved <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP portal</a>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Is MCP</td>
<td>is</td>
<td><em>True</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Traffic Source</td>
<td>is not</td>
<td><em>MCP portal</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-block-unknown-mcp.png" alt="Example Gateway policy that blocks MCP traffic not arriving through an MCP portal" /></p>
<h4 id="2026-08-12-mcp-detection-and-dashboard-ai-security-report">AI security report</h4>
<p>A new <strong>AI security report</strong> dashboard under <strong>Insights &amp; Logs &gt; Dashboards</strong> provides visibility into MCP usage across your organization. The dashboard includes:</p>
<ul>
<li>Total MCP request volume, unique users, and unique MCP servers</li>
<li>A timeseries chart of unique MCP servers observed over time</li>
<li>A summary of Gateway policies that target MCP traffic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-mcp-dashboard.png" alt="AI security report dashboard showing MCP detection data including total MCP requests, users, servers, and Gateway policies for MCP" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>


<h2 id="traffic-source-selector-in-gateway-policies"><a href="/changelog/post/2026-08-12-traffic-source-selector/">Traffic Source selector in Gateway policies</a></h2>
<p><em>2026-08-12</em></p>
<p>Gateway <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a> and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> policies now include a <strong>Traffic Source</strong> selector that identifies how traffic reaches Cloudflare. This allows administrators to write policies that target specific on-ramp methods - for example, applying different rules to traffic arriving via the Cloudflare One Client compared to traffic routed through an MCP portal or a proxy endpoint.</p>
<h4 id="2026-08-12-traffic-source-selector-available-traffic-source-values">Available traffic source values</h4>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Device client</td>
<td><code>device_client</code></td>
<td>Traffic from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client (WARP)</a></td>
</tr>
<tr>
<td>Mesh</td>
<td><code>mesh</code></td>
<td>Traffic from a <a href="/mesh/">Cloudflare Mesh</a> connector</td>
</tr>
<tr>
<td>Cloudflare WAN</td>
<td><code>cloudflare_wan</code></td>
<td>Traffic from <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a> (Magic WAN)</td>
</tr>
<tr>
<td>Clientless RDP</td>
<td><code>clientless_rdp</code></td>
<td>Traffic from a clientless RDP session</td>
</tr>
<tr>
<td>Proxy endpoint</td>
<td><code>proxy_endpoint</code></td>
<td>Traffic from a <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoint</a> (PAC file)</td>
</tr>
<tr>
<td>Clientless Browser Isolation</td>
<td><code>agentless_biso</code></td>
<td>Traffic from <a href="/cloudflare-one/remote-browser-isolation/">clientless Browser Isolation</a></td>
</tr>
<tr>
<td>MCP portal</td>
<td><code>mcp_portal</code></td>
<td>Traffic from an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP portal</a></td>
</tr>
</tbody>
</table>
<p>The selector uses the <code>net.onramp.type</code> API field in both HTTP and Network policies.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Traffic Source</td>
<td><code>net.onramp.type == &quot;device_client&quot;</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-08-12-traffic-source-selector-browser-isolation-selector">Browser Isolation selector</h4>
<p>A <strong>Browser Isolation</strong> selector is also available in Network and HTTP policies. This selector identifies whether the current session is running inside <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>, allowing administrators to apply different policy behavior to isolated traffic.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Browser Isolation</td>
<td><code>net.is_isolated == true</code></td>
</tr>
</tbody>
</table>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> and <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a>.</p>


<h2 id="hostname-routing-is-now-generally-available-with-a-new-public-ip-range-for-initial-resolved-ips"><a href="/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/">Hostname routing is now generally available, with a new public IP range for initial resolved IPs</a></h2>
<p><em>2026-08-11</em></p>
<p><a href="https://blog.cloudflare.com/tunnel-hostname-routing/">Hostname routing</a> is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:</p>
<ul>
<li><strong>Cloudflare Tunnel</strong>: route a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> (for example, <code>wiki.internal.local</code>) to a private application behind your tunnel, or a <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> (for example, <code>bank.example.com</code>) to egress through a specific tunnel and anchor traffic to a dedicated exit node.</li>
<li><strong>Cloudflare Mesh</strong>: attract a <a href="/mesh/features/routes/#hostname-routes">private or public hostname's traffic</a> to a Mesh node.</li>
</ul>
<p>Alongside GA, the default IPv4 range used for <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/17760.md")</div> (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p><strong>Why this is changing:</strong> Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restrictions block background requests to CGNAT addresses (<code>100.64.0.0/10</code>), which included the previous initial resolved IP default (<code>100.80.0.0/16</code>). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.</p>
<p><strong>What is affected:</strong> Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">Private</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public</a> hostname routing for Cloudflare Tunnel</li>
<li><a href="/mesh/features/routes/#hostname-routes">Hostname routes</a> for Cloudflare Mesh</li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access private applications</a> on non-HTTPS ports</li>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Egress policy host selectors</a> (Domain, Host, Application, and Content Categories)</li>
</ul>
<p>You can check your account's current range, or configure a custom range, at any time from <strong>Networking</strong> &gt; <strong>IP addresses</strong> &gt; <strong>Address space</strong> &gt; <strong>Custom IPs</strong>, or using the <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/#(resource)%20zero_trust.networks.subnets.initial_resolved_ip">Initial Resolved IP Subnet API</a>.</p>
<div class="nb-dash-button"></div>
<p>For full instructions, refer to <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">Configure initial resolved IPs</a>. The IPv6 range (<code>2606:4700:0cf1:4000::/64</code>) is unchanged and is not affected by this restriction.</p>
<p>The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">Automatically managed ranges</a> for details.</p>
<p>If you were relying on a Chrome Enterprise policy workaround (such as <code>LocalNetworkAccessRestrictionsTemporaryOptOut</code>) while your account was still on the legacy CGNAT-based range, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames">Google Chrome restricts access to private hostnames</a> for next steps.</p>


<h2 id="container-image-for-cloudflare-mesh"><a href="/changelog/post/2026-08-07-mesh-container-image/">Container image for Cloudflare Mesh</a></h2>
<p><em>2026-08-07</em></p>
<p><a href="/mesh/">Cloudflare Mesh</a> nodes can now run as Docker containers. The <a href="https://hub.docker.com/r/cloudflare/mesh"><code>cloudflare/mesh</code></a> image is available on Docker Hub for Docker Compose, Kubernetes, and any OCI-compatible runtime — no host-level package installation required.</p>
<p>The image supports <code>amd64</code> and <code>arm64</code> architectures and includes built-in <a href="/mesh/guides/run-mesh-in-containers/#source-nat">source NAT</a> so return traffic routes correctly without VPC route table changes.</p>
<h4 id="2026-08-07-mesh-container-image-deployment-patterns">Deployment patterns</h4>
<ul>
<li><strong>Docker Compose</strong> — add a <code>cloudflare-mesh</code> service to your <code>compose.yaml</code> and connect your entire stack to a private network.</li>
<li><strong>Kubernetes StatefulSet</strong> — deploy a standalone Mesh node with persistent registration state.</li>
<li><strong>Kubernetes sidecar</strong> — add the Mesh image as a sidecar container in a Pod to connect an application to Cloudflare without application changes.</li>
<li><strong>CI/CD</strong> — pull the image in a pipeline step, join the Mesh, run integration tests against private infrastructure, and tear down. The node disappears when the container exits.</li>
</ul>
<p>For <a href="/mesh/features/high-availability/">high availability</a>, run multiple replicas with the same Mesh node token. Cloudflare operates replicas in active-passive mode with automatic failover.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, runtime configuration, and deployment examples, refer to <a href="/mesh/guides/run-mesh-in-containers/">Run Mesh in Docker / Kubernetes</a>.</p>


<h2 id="control-cloudflare-gateway-dns-caching-with-a-maximum-ttl-setting"><a href="/changelog/post/2026-07-28-gateway-maximum-dns-ttl/">Control Cloudflare Gateway DNS caching with a maximum TTL setting</a></h2>
<p><em>2026-07-28</em></p>
<p>You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-max-ttl-traffic-settings.png" alt="The maximum DNS TTL setting in Traffic policies &gt; Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds" /></p>
<p>The setting is available at two levels:</p>
<ul>
<li><strong>Account level</strong> - In <strong>Traffic Policies</strong> &gt; <strong>Traffic Settings</strong>, under <strong>Proxy and inspection</strong>. This sets the default cap for all DNS locations.</li>
<li><strong>Per-location</strong> - Each <a href="/cloudflare-one/networks/resolvers-proxies/">DNS location</a> can inherit the account setting, disable the cap, or override it with a custom value.</li>
</ul>
<p>Two new fields are also available in DNS logs: <code>upstream_record_ttls</code> (the original TTL from the upstream response) and <code>applied_max_ttl</code> (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/">Maximum DNS TTL</a>.</p>


<h2 id="restart-reboot-or-shut-down-a-cloudflare-one-appliance-from-the-dashboard"><a href="/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/">Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard</a></h2>
<p><em>2026-07-17</em></p>
<p>You can now restart, reboot, or shut down a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard or via API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-17-appliance-restart-reboot-shutdown.gif" alt="Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page" /></p>
<ul>
<li><strong>Restart</strong> — Restart managed services. Purges temporary and (optionally) persistent state.</li>
<li><strong>Reboot</strong> — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.</li>
<li><strong>Shutdown</strong> — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.</li>
</ul>
<p>In the dashboard, go to <strong>Networking</strong> &gt; <strong>Connectors</strong> &gt; <strong>Appliances</strong>, select an appliance, then <strong>Edit</strong> &gt; <strong>Operations</strong> to send an operation. Via API, <code>POST</code> to the <code>/accounts/{account_id}/magic/connectors/{connector_id}/interrupts</code> endpoint.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/">Appliance operations</a>.</p>


<h2 id="bulk-print-pdfs-for-browser-based-rdp"><a href="/changelog/post/2026-07-16-rdp-bulk-print/">Bulk print PDFs for browser-based RDP</a></h2>
<p><em>2026-07-16</em></p>
<p>Users in browser-based RDP sessions can now print multiple PDF files as a single print job. Copy the files to your clipboard on the remote machine, then select <strong>Print all PDFs</strong> in the clipboard panel. The files are combined into one PDF and sent to your local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/rdp-bulk-print.png" alt="The clipboard panel showing the Print all PDFs option for multiple selected PDF files." /></p>
<p>Bulk print is available in Chromium-based browsers and Firefox. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#print-pdfs">Print PDFs for browser-based RDP</a>.</p>


<h2 id="ipsec-downgrade-protection-beta"><a href="/changelog/post/2026-07-08-ipsec-downgrade-protection/">IPsec downgrade protection (beta)</a></h2>
<p><em>2026-07-08</em></p>
<p>Cloudflare IPsec now supports the <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/"><code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code></a> IKEv2 extension to protect against downgrade attacks on IPsec tunnels.</p>
<p>IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable <a href="https://www.cloudflare.com/learning/security/threats/on-path-attack/">on-path attacker</a> can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography. The <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> extension addresses this by having both peers sign the entire handshake transcript during the authentication exchange, preventing an attacker from manipulating the negotiation without detection.</p>
<p>Key details:</p>
<ul>
<li>Available in beta for Cloudflare WAN and Magic Transit IPsec tunnels.</li>
<li>Cloudflare sends the <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> notification unconditionally as a responder when the feature flag is enabled.</li>
<li>Both the initiator (your device) and responder (Cloudflare) must support the extension for downgrade protection to be effective.</li>
<li>This feature is currently gated by a per-account feature flag. Contact your account team to turn it on.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#improved-downgrade-protection-beta">Downgrade protection</a> for more details.</p>


<h2 id="file-transfer-controls-for-browser-based-rdp-beta"><a href="/changelog/post/2026-07-07-rdp-file-transfer-beta/">File transfer controls for browser-based RDP (beta)</a></h2>
<p><em>2026-07-07</em></p>
<p>You can now configure file transfer controls for browser-based RDP with Cloudflare Access, allowing you to restrict whether users can upload or download files between their local machine and the remote Windows server.</p>
<p><img src="/assets/upstream/images/changelog/access/file-transfer-policy-control.png" alt="File transfer connection settings in the Access policy configuration." /></p>
<p>This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting file transfers, you can prevent sensitive data from being moved out of the remote session to a user's personal device.</p>
<h4 id="2026-07-07-rdp-file-transfer-beta-configuration-options">Configuration options</h4>
<p>File transfer controls are configured per policy within your Access application, alongside existing <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings">text clipboard controls</a>. For each policy, you can select one of the following options:</p>
<ul>
<li><strong>Client to remote RDP session allowed</strong> — Users can upload files from their local machine into the browser-based RDP session.</li>
<li><strong>Remote RDP session to client allowed</strong> — Users can download files from the browser-based RDP session to their local machine.</li>
<li><strong>Both directions allowed</strong> — Users can upload and download files between their local machine and the browser-based RDP session.</li>
<li><strong>Disable copying/pasting</strong> — Users are not allowed to transfer files between their local machine and the browser-based RDP session.</li>
</ul>
<p>By default, file transfer is denied for new policies. For existing Access applications created before this feature was available, file transfer remains denied.</p>
<h4 id="2026-07-07-rdp-file-transfer-beta-how-it-works">How it works</h4>
<p>To upload, drag files into the browser window or select the settings gear icon on the left side of the RDP session. To download, copy a file in the remote session and select the settings gear to download it, download multiple files as a zip, or print PDFs to a local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/clipboard-side-panel.png" alt="The clipboard side panel showing files available for transfer." /></p>
<p><img src="/assets/upstream/images/changelog/access/remote-doc-ready-for-download-or-print-local.png" alt="A remote document ready for download or local printing." /></p>
<p>This feature is in beta and available on all Zero Trust plans. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#transfer-files">File transfer for browser-based RDP</a>.</p>


<h2 id="browser-isolation-support-for-authorization-proxy-endpoints"><a href="/changelog/post/2026-07-07-authorization-proxy-endpoint-support/">Browser Isolation support for authorization proxy endpoints</a></h2>
<p><em>2026-07-07</em></p>
<p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> now supports Gateway <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">authorization proxy endpoints</a>. You can apply <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">HTTP Isolate policies</a> to traffic routed through authorization proxy endpoints, the same way you can for traffic from the Cloudflare One Client.</p>
<p>Previously, only <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a> supported Browser Isolation, and only with non-identity policies. Because authorization proxy endpoints authenticate users through an identity provider, you can now apply identity-based Isolate policies to PAC file-proxied traffic without requiring the Cloudflare One Client.</p>
<p>To get started, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">create an authorization proxy endpoint</a> and <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">build an Isolate policy</a>.</p>


<h2 id="self-serve-registration-of-cloudflare-one-virtual-appliance-in-the-dashboard"><a href="/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/">Self-serve registration of Cloudflare One Virtual Appliance in the dashboard</a></h2>
<p><em>2026-07-06</em></p>
<p>You can now register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a> and generate its license key directly from the dashboard, without contacting your account team.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-06-virtual-appliance-self-serve-ui.gif" alt="Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong> and choose <strong>Virtual appliance</strong> to register a virtual appliance and generate its authentication key.</li>
<li>Use <strong>Regenerate authentication key</strong> from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.</li>
<li>The authentication key is shown only once — copy and store it securely.</li>
</ul>
<p>This complements the existing <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">API and Terraform self-serve workflow</a> for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="hostname-routing-for-cloudflare-mesh"><a href="/changelog/post/2026-07-02-mesh-hostname-routing/">Hostname routing for Cloudflare Mesh</a></h2>
<p><em>2026-07-02</em></p>
<p>You can now add <a href="/mesh/features/routes/#hostname-routes">hostname routes</a> to a Cloudflare Mesh node, in addition to CIDR routes.</p>
<div class="nb-interactive-component" data-cf-component="MeshHostnameRoutingDiagram"></div>
<p>Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:</p>
<ul>
<li><strong>Private hostname</strong> (for example, <code>wiki.internal.local</code>) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.</li>
<li><strong>Public hostname</strong> (for example, <code>www.example.com</code>) — route that hostname's traffic through the node and egress via the node's public IP.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For setup steps, prerequisites, and DNS options, refer to <a href="/mesh/features/routes/#hostname-routes">Hostname routes</a>.</p>


<h2 id="new-permissions-and-roles-for-gateway-policies-and-lists"><a href="/changelog/post/2026-06-30-gateway-granular-permissions/">New permissions and roles for Gateway policies and lists</a></h2>
<p><em>2026-06-30</em></p>
<p>You can now assign granular, resource-scoped roles for <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> firewall policies and <a href="/cloudflare-one/reusable-components/lists/">Zero Trust lists</a>. Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.</p>
<h4 id="2026-06-30-gateway-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the following resource-scoped roles are now available:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zero Trust Gateway Firewall Policies Admin</td>
<td>Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway DNS Policies Admin</td>
<td>Can view and edit Gateway DNS policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway HTTP Policies Admin</td>
<td>Can view and edit Gateway HTTP policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Network Policies Admin</td>
<td>Can view and edit Gateway Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Egress Policies Admin</td>
<td>Can view and edit Gateway Egress policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Resolver Policies Admin</td>
<td>Can view and edit Gateway Resolver policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Admin</td>
<td>Can view and edit all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Read</td>
<td>Can view all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Read Only</td>
<td>Can view all Gateway resources.</td>
</tr>
<tr>
<td>Zero Trust DNS Locations Admin</td>
<td>Can view and edit DNS locations.</td>
</tr>
<tr>
<td>Zero Trust Proxy Endpoints Admin</td>
<td>Can view and edit Gateway Proxy Endpoints.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Admin</td>
<td>Can view and edit all Gateway and Access lists.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Read</td>
<td>Can view all Gateway and Access lists.</td>
</tr>
</tbody>
</table>
<p>These roles allow you to:</p>
<ul>
<li>Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.</li>
<li>Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.</li>
<li>Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.</li>
</ul>
<p>You can also now assign <em>Resource-scoped roles</em>. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. <strong>Existing account-level roles continue to work.</strong> A member with the <code>Cloudflare Gateway</code> or <code>Cloudflare Zero Trust</code> role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.</p>
<h4 id="2026-06-30-gateway-granular-permissions-get-started">Get started</h4>
<ul>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
<li>Learn how to <a href="/fundamentals/manage-members/policies/">create permission policies</a> that use these roles.</li>
</ul>


<h2 id="service-token-support-for-mcp-server-portals"><a href="/changelog/post/2026-06-26-mcp-portal-service-tokens/">Service token support for MCP server portals</a></h2>
<p><em>2026-06-26</em></p>
<p>You can now connect autonomous agents and bots to an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> using an <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a>. Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow.</p>
<p>To set this up:</p>
<ul>
<li>Add a <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth policy</a> that matches your service token to the portal's Access application.</li>
<li>Add a Service Auth policy that matches the same token to each linked MCP server's Access application.</li>
<li>Turn <strong>Require user auth</strong> off (<code>on_behalf: false</code>) for each linked server so the portal uses the admin credential instead of a per-user OAuth grant.</li>
</ul>
<p>The bot connects with <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> headers and sees the tools from every linked server it is authorized for. Servers that still require per-user OAuth are excluded from service token sessions because a service token cannot complete a per-user OAuth grant.</p>
<p>For step-by-step setup, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token">Connect with a service token</a>.</p>


<h2 id="manage-all-your-routes-from-one-page-in-the-dashboard"><a href="/changelog/post/2026-06-19-unified-routes-page/">Manage all your routes from one page in the dashboard</a></h2>
<p><em>2026-06-19</em></p>
<p>The <strong>Routes</strong> page in the Cloudflare dashboard now shows the routes across all of your connectors — <a href="/mesh/">Cloudflare Mesh</a> and <a href="/tunnel/">Cloudflare Tunnel</a> routes alongside <a href="/cloudflare-wan/">Cloudflare WAN</a> and <a href="/magic-transit/">Magic Transit</a> static routes — in a single table, instead of a separate routes view per product.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-06-19-unified-routes.gif" alt="The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table" /></p>
<p>From the unified Routes page you can:</p>
<ul>
<li><strong>Visualize your network with an interactive map</strong> that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.</li>
<li><strong>See every route in one table</strong>, with its destination, type, connector, priority, and source, and filter or sort to find what you need.</li>
<li><strong>Create, edit, and delete routes</strong> of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by <strong>connector name</strong> instead of typing its IP.</li>
<li><strong>Manage <a href="/cloudflare-one/networks/virtual-networks/">virtual networks</a></strong> from a dedicated tab.</li>
<li><strong>Test a route</strong> to see which connector and next hop a destination resolves to before you commit a change.</li>
</ul>
<p>To find it, go to <strong>Networking</strong> &gt; <strong>Routes</strong> in the dashboard sidebar.</p>
<div class="nb-dash-button"></div>
<p>Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to <a href="/cloudflare-one/networks/routes/add-routes/">add routes</a> and <a href="/cloudflare-one/networks/virtual-networks/">manage virtual networks</a>.</p>


<h2 id="cloudflare-identity-provider-is-now-the-default-for-new-accounts"><a href="/changelog/post/2026-06-18-cloudflare-idp-default/">Cloudflare identity provider is now the default for new accounts</a></h2>
<p><em>2026-06-18</em></p>
<p>When you create a new Zero Trust organization, Cloudflare now adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method. Previously, new organizations started with <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN (OTP)</a>.</p>
<p>With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> whenever you need to.</p>
<p>This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.</p>


<h2 id="cisco-ios-xe"><a href="/changelog/post/2026-06-02-cisco-ios-xe/">Cisco IOS XE</a></h2>
<p><em>2026-06-02</em></p>
<p>The Cisco IOS XE third-party integration guide for Cloudflare WAN has been updated to include:</p>
<ul>
<li>Post Quantum Cryptography (PQC)</li>
<li>Policy-Based Routing (PBR)</li>
<li>IP Service Level Agreement (IP SLA)</li>
</ul>
<p>This link will take you directly to the updated <a href="/cloudflare-wan/configuration/third-party/cisco-ios-xe/">Cisco IOS XE</a> guide.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 3</span><a class="pagination-next" rel="next" href="/changelog/product/cloudflare-one/2/">Next</a></nav>
