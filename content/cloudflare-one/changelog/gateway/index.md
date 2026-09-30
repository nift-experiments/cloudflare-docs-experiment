<h2 id="2026-08-13">2026-08-13</h2>

<strong>Detect and control software package downloads with package registry security</strong>

<p>Cloudflare Gateway can now detect software package downloads and give you policy control over supply chain traffic. When a developer or CI/CD pipeline downloads a package through Gateway, the proxy identifies the registry protocol from the request URL and extracts the package ecosystem, name, version, and namespace. You can then write <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a> using <code>pkg.*</code> selectors to allow or block package downloads.</p>
<h4 id="2026-08-13-package-protection-supported-ecosystems">Supported ecosystems</h4>
<p>Gateway detects package downloads for the following ecosystems:</p>
<table>
<thead>
<tr>
<th>Ecosystem</th>
<th>Namespace</th>
</tr>
</thead>
<tbody>
<tr>
<td>npm</td>
<td>Scope (for example, <code>@babel</code>)</td>
</tr>
<tr>
<td>PyPI</td>
<td>--</td>
</tr>
<tr>
<td>RubyGems</td>
<td>--</td>
</tr>
<tr>
<td>Cargo</td>
<td>--</td>
</tr>
<tr>
<td>Go</td>
<td>Module path</td>
</tr>
<tr>
<td>Maven</td>
<td>Group ID</td>
</tr>
<tr>
<td>NuGet</td>
<td>--</td>
</tr>
</tbody>
</table>
<h4 id="2026-08-13-package-protection-selectors">Selectors</h4>
<p>In the dashboard, select <strong>Package Ecosystem</strong> to access the package registry selectors. After selecting a single ecosystem, nested fields for package name, version, and namespace become available. Five <code>pkg.*</code> selectors are available for HTTP policies with the Allow and Block actions:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pkg.ecosystem</code></td>
<td>The package ecosystem detected from the request URL.</td>
</tr>
<tr>
<td><code>pkg.name</code></td>
<td>The package name extracted from the download URL.</td>
</tr>
<tr>
<td><code>pkg.version</code></td>
<td>The package version, with support for ecosystem-aware comparison operators.</td>
</tr>
<tr>
<td><code>pkg.namespace</code></td>
<td>The package namespace, when the ecosystem supports one.</td>
</tr>
<tr>
<td><code>pkg.purl</code></td>
<td>The <a href="https://github.com/package-url/purl-spec">Package URL (PURL)</a> derived from the detected coordinates. Available in the API only.</td>
</tr>
</tbody>
</table>
<p>Detection is based on the registry protocol rather than the hostname, so it works the same way whether traffic goes to a public registry, a corporate proxy such as Artifactory or Nexus, or a self-hosted mirror.</p>
<p>Package registry security requires <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a> to be turned on.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/package-registry-security/">Package registry security</a>.</p>


<h2 id="2026-08-12">2026-08-12</h2>

<strong>MCP protocol detection and AI Security dashboard</strong>

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


<h2 id="2026-08-12-1">2026-08-12</h2>

<strong>Traffic Source selector in Gateway policies</strong>

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


<h2 id="2026-08-11">2026-08-11</h2>

<strong>Hostname routing is now generally available, with a new public IP range for initial resolved IPs</strong>

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


<h2 id="2026-07-28">2026-07-28</h2>

<strong>Control Cloudflare Gateway DNS caching with a maximum TTL setting</strong>

<p>You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-max-ttl-traffic-settings.png" alt="The maximum DNS TTL setting in Traffic policies &gt; Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds" /></p>
<p>The setting is available at two levels:</p>
<ul>
<li><strong>Account level</strong> - In <strong>Traffic Policies</strong> &gt; <strong>Traffic Settings</strong>, under <strong>Proxy and inspection</strong>. This sets the default cap for all DNS locations.</li>
<li><strong>Per-location</strong> - Each <a href="/cloudflare-one/networks/resolvers-proxies/">DNS location</a> can inherit the account setting, disable the cap, or override it with a custom value.</li>
</ul>
<p>Two new fields are also available in DNS logs: <code>upstream_record_ttls</code> (the original TTL from the upstream response) and <code>applied_max_ttl</code> (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/">Maximum DNS TTL</a>.</p>


<h2 id="2026-07-17">2026-07-17</h2>

<strong>New header control options for Gateway HTTP policies</strong>

<p>Cloudflare Gateway now supports advanced header control on <a href="/cloudflare-one/traffic-policies/http-policies/#allow">Allow policies</a>. Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables.</p>
<h4 id="2026-07-17-http-request-header-manipulation-header-operations">Header operations</h4>
<p>Gateway HTTP policies using the Allow action support three operations in <code>rule_settings</code>:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>API field</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Add</td>
<td><code>add_headers</code></td>
<td>Appends a value to the header. Existing values are preserved.</td>
</tr>
<tr>
<td>Overwrite</td>
<td><code>set_headers</code></td>
<td>Replaces the header value. Creates the header if it does not exist.</td>
</tr>
<tr>
<td>Delete</td>
<td><code>delete_headers</code></td>
<td>Removes the header from the request.</td>
</tr>
</tbody>
</table>
<p>Gateway applies operations in order: delete, then overwrite, then add.</p>
<h4 id="2026-07-17-http-request-header-manipulation-dynamic-variables">Dynamic variables</h4>
<p>Header values can include dynamic variables using the <code>@{...}</code> syntax. Gateway resolves variables at request time from identity, device, and network context.</p>
<table>
<thead>
<tr>
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@{identity.email}</code></td>
<td>User email from the identity provider</td>
</tr>
<tr>
<td><code>@{identity.name}</code></td>
<td>User display name from the identity provider</td>
</tr>
<tr>
<td><code>@{identity.id}</code></td>
<td>Cloudflare identity UUID</td>
</tr>
<tr>
<td><code>@{identity.groups}</code></td>
<td>Identity provider group memberships</td>
</tr>
<tr>
<td><code>@{identity.SAML}</code></td>
<td>SAML attributes (if configured)</td>
</tr>
<tr>
<td><code>@{identity.OIDC}</code></td>
<td>OIDC claims (if configured)</td>
</tr>
<tr>
<td><code>@{source.ip}</code></td>
<td>Source IP of the connection</td>
</tr>
<tr>
<td><code>@{destination.ip}</code></td>
<td>Destination IP of the request</td>
</tr>
<tr>
<td><code>@{device.id}</code></td>
<td>Cloudflare One Client device UUID</td>
</tr>
<tr>
<td><code>@{device.posture}</code></td>
<td>Device posture check results (JSON string)</td>
</tr>
</tbody>
</table>
<p>You can mix static text and dynamic variables in a single header value. For example, <code>user-@{identity.email}</code> resolves to <code>user-jdoe@example.com</code>.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tenant-control/">Custom headers</a>.</p>


<h2 id="2026-07-15">2026-07-15</h2>

<strong>Internal DNS is now generally available</strong>

<p><a href="/dns/internal-dns/">Internal DNS</a> is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.</p>
<h4 id="2026-07-15-internal-dns-ga-why-it-matters">Why it matters</h4>
<ul>
<li><strong>Consolidate DNS operations.</strong> Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.</li>
<li><strong>Simplify split-horizon DNS.</strong> Internal and external resolution are defined as separate <a href="/dns/internal-dns/dns-views/">views</a> over shared zones, managed from a single control plane — so there is no drift to chase down.</li>
<li><strong>Extend Zero Trust to DNS.</strong> Resolver policies decide which users and devices resolve against which view, enforced by the same <a href="/cloudflare-one/traffic-policies/">Gateway</a> that already governs the rest of your traffic.</li>
</ul>
<p>Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.</p>
<pre><code class="language-json">POST /zones&#10;{&#10;  &quot;account&quot;: {&#10;    &quot;id&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;  },&#10;  &quot;name&quot;: &quot;corp.internal&quot;,&#10;  &quot;type&quot;: &quot;internal&quot;&#10;}&#10;</code></pre>
<p>Internal DNS is included with <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for Enterprise customers. To get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>


<h2 id="2026-06-30">2026-06-30</h2>

<strong>New permissions and roles for Gateway policies and lists</strong>

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


<h2 id="2026-06-05">2026-06-05</h2>

<strong>Filter Workers' public Internet traffic using Gateway policies</strong>

<p>Workers using a <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> binding with <code>network_id: &quot;cf1:network&quot;</code> now egress to public Internet destinations through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>. This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.</p>
<div class="nb-interactive-component" data-cf-component="WorkersVPCEgressDiagram"></div>
<p>What you get by default:</p>
<ul>
<li><strong>Visibility.</strong> Worker egress shows up in Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> logs alongside your other traffic, so you can audit what your Workers are calling and when.</li>
<li><strong>Enforcement.</strong> Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17825.md")</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17826.md")</div>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>. For policy authoring, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway traffic policies</a>.</p>


<h2 id="2026-05-27">2026-05-27</h2>

<strong>Write regex using natural language in Cloudflare One</strong>

<p><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> policy selectors which support regular expressions can now be authored in the dashboard using natural language. When building a <a href="/cloudflare-one/traffic-policies/expression-syntax/">policy</a> with a regex-based selector (like <code>matches regex</code>), you can describe what you want to match in plain English and the Cloudflare Agent will generate and validate a corresponding regular expression.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-regex-ai-generation.png" alt="Write policy regex using natural language" /></p>
<p>To get started, select a regex-compatible selector in the <a href="/cloudflare-one/traffic-policies/">Gateway policy builder</a> and select the icon. You'll see an input field for natural language, such as &quot;any URL starting with /api/v1&quot; or &quot;.com, .net, and .app hosts which contain <code>gooogle</code> in the host.&quot;</p>
<p>You can also use the tool to explain existing regular expressions. If a policy already contains a regex pattern, you can instantly generate a plain-language description.</p>
<p>A built-in feedback mechanism allows you to rate each interaction to help improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare One firewall policies</a> and expect to see the same functionality supported soon in <a href="/cloudflare-one/data-loss-prevention/">Data loss prevention profiles</a>.</p>


<h2 id="2026-05-12">2026-05-12</h2>

<strong>Create Gateway firewall policies with natural language</strong>

<p>Cloudflare Gateway now supports natural language policy creation for <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> firewall policies. Administrators can describe the outcome they want in plain language, and Cloudflare will generate a complete policy rule that populates the policy builder form.</p>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-create-with-ai.png" alt="Create with AI button on the Gateway firewall policies page" /></p>
<p>To create a policy with natural language, select <strong>Create with AI</strong> on any Gateway firewall policy tab. Choose a policy type, describe what the policy should do, and a fully configured rule will appear in the policy builder for review. You can edit any field before saving, or re-generate with a different prompt.</p>
<p>The generated policy incorporates your account context - including lists, DLP profiles, applications, and device posture checks - so that references to your existing resources resolve automatically.</p>
<p>A built-in feedback mechanism allows you to rate each generated policy and provide optional comments, which Cloudflare uses to improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Gateway firewall policies</a>.</p>


<h2 id="2026-04-29">2026-04-29</h2>

<strong>Gateway Authorization Proxy and hosted PAC files are now generally available</strong>

<p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Gateway Authorization Proxy</a> and <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">hosted PAC files</a> are now generally available for all plan types.</p>
<p>Authorization proxy endpoints add an identity-aware option alongside the existing <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a>, using <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> authentication to verify who a user is before applying Gateway filtering — without installing the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>. Cloudflare-hosted PAC files let you create and distribute PAC files directly from Cloudflare One on Cloudflare's global network.</p>
<p>These features are ideal for environments where deploying a device client is not an option, such as virtual desktops (VDI) or compliance-restricted endpoints.</p>
<p>To get started, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints documentation</a>.</p>


<h2 id="2026-04-24">2026-04-24</h2>

<strong>Network Session Logs now available for all on-ramps</strong>

<p><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a> are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints (PAC files)</a> and <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> egress — on-ramps that previously did not generate session logs.</p>
<p>Customers who already consume the <code>zero_trust_network_sessions</code> dataset via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> or <a href="/log-explorer/">Log Explorer</a> may see increased log volume if they use these on-ramps.</p>
<p>For field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>. For traffic analysis, refer to <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics</a>.</p>


<h2 id="2026-04-20">2026-04-20</h2>

<strong>Network session analytics dashboard</strong>

<p>The new <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics</a> dashboard is now available in Cloudflare One. This dashboard provides visibility into your network traffic patterns, helping you understand how traffic flows through your Cloudflare One infrastructure.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-network-session-analytics.png" alt="Cloudflare One Network Session Analytics" /></p>
<h4 id="2026-04-20-network-session-analytics-what-you-can-do-with-network-session-analytics">What you can do with Network session analytics</h4>
<ul>
<li><strong>Analyze geographic distribution</strong>: View a world map showing where your network traffic originates, with a list of top locations by session count.</li>
<li><strong>Monitor key metrics</strong>: Track session count, total bytes transferred, and unique users.</li>
<li><strong>Identify connection issues</strong>: Analyze connection close reasons to troubleshoot network problems.</li>
<li><strong>Review protocol usage</strong>: See which network protocols (TCP, UDP, ICMP) are most used.</li>
</ul>
<h4 id="2026-04-20-network-session-analytics-dashboard-features">Dashboard features</h4>
<ul>
<li><strong>Summary metrics</strong>: Session count, bytes total, and unique users</li>
<li><strong>Traffic by location</strong>: World map visualization and location list with top traffic sources</li>
<li><strong>Top protocols</strong>: Breakdown of TCP, UDP, ICMP, and ICMPv6 traffic</li>
<li><strong>Connection close reasons</strong>: Insights into why sessions terminated (client closed, origin closed, timeouts, errors)</li>
</ul>
<h4 id="2026-04-20-network-session-analytics-how-to-access">How to access</h4>
<ol>
<li>Log in to <a href="https://dash.cloudflare.com">Cloudflare One</a>.</li>
<li>Go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Dashboards</strong>.</li>
<li>Select <strong>Network session analytics</strong>.</li>
</ol>
<p>For more information, refer to the <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics documentation</a>.</p>


<h2 id="2026-04-14">2026-04-14</h2>

<strong>Configure how sensitive data appears in DLP payload logs</strong>

<p>You can now configure how sensitive data matches are displayed in your DLP payload match logs — giving your incident response team the context they need to validate alerts without compromising your security posture.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, select <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>DLP settings</strong> and find the <strong>Payload log masking</strong> card.</p>
<p>Previously, all DLP payload logs used a single masking mode that obscured matched data entirely and hid the original character count, making it difficult to distinguish true positives from false positives. This update introduces three options:</p>
<ul>
<li><strong>Full Mask (default):</strong> Masks the match while preserving character count and visual formatting (for example, <code>***-**-****</code> for a Social Security Number). This is an improvement over the previous default, which did not preserve character count.</li>
<li><strong>Partial Mask:</strong> Reveals 25% of the matched content while masking the remainder (for example, <code>***-**-6789</code>).</li>
<li><strong>Clear Text:</strong> Stores the full, unmasked violation for deep investigation (for example, <code>123-45-6789</code>).</li>
</ul>
<p><strong>Important:</strong> The masking level you select is applied at detection time, before the payload is encrypted. This means the chosen format is what your team will see after decrypting the log with your private key — the existing encryption workflow is unchanged.</p>
<p><strong>Applies to all enabled detections:</strong> When a masking level other than Full Mask is selected, it applies to all sensitive data matches found within a payload window — not just the match that triggered the policy. Any data matched by your enabled DLP detection entries will be masked at the selected level.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-the-payload-of-matched-rules">DLP logging options</a>.</p>


<h2 id="2026-04-06">2026-04-06</h2>

<strong>Organizations is now in public beta for enterprises</strong>

<p>We're announcing the public beta of <strong>Organizations</strong> for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.</p>
<p><strong>What's New</strong></p>
<p><strong>Organizations [BETA]</strong>: <a href="/fundamentals/organizations/">Organizations</a> are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.</p>
<p><strong>Self-serve onboarding</strong>: Enterprise customers can <a href="/fundamentals/organizations/setup/">create an Organization</a> in the dashboard and assign accounts where they are already Super Administrators.</p>
<p><strong>Centralized Account Management</strong>: At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly.
<strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.
<strong>Implicit access</strong>: Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.</p>
<p><strong>Unified analytics</strong>: View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.</p>
<p><strong>Terraform provider support</strong>: Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization">Cloudflare Terraform provider</a>.</p>
<p><strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17731.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/organizations/">Get started with Organizations</a></li>
<li><a href="/fundamentals/organizations/setup/">Set up your Organization</a></li>
<li><a href="/fundamentals/organizations/limitations/">Review limitations</a></li>
</ul>


<h2 id="2026-04-01">2026-04-01</h2>

<strong>Logs UI refresh</strong>

<p>Access authentication logs and Gateway activity logs (DNS, Network, and HTTP) now feature a refreshed user interface that gives you more flexibility when viewing and analyzing your logs.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-new-logs-ui.png" alt="Screenshot of the new logs UI showing DNS query logs with customizable columns and filtering options" /></p>
<p>The updated UI includes:</p>
<ul>
<li><strong>Filter by field</strong> - Select any field value to add it as a filter and narrow down your results.</li>
<li><strong>Customizable fields</strong> - Choose which fields to display in the log table. Querying for fewer fields improves log loading performance.</li>
<li><strong>View details</strong> - Select a timestamp to view the full details of a log entry.</li>
<li><strong>Switch to classic view</strong> - Return to the previous log viewer interface if needed.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/">Access authentication logs</a> and <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a>.</p>


<h2 id="2026-03-24">2026-03-24</h2>

<strong>OIDC Claims filtering now available in Gateway Firewall, Resolver, and Egress policies</strong>

<p>Cloudflare Gateway now supports <a href="/cloudflare-one/traffic-policies/identity-selectors/#oidc-claims">OIDC Claims</a> as a selector in Firewall, Resolver, and Egress policies. Administrators can use custom OIDC claims from their identity provider to build fine-grained, identity-based traffic policies across all Gateway policy types.</p>
<p>With this update, you can:</p>
<ul>
<li>Filter traffic in <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> firewall policies based on OIDC claim values.</li>
<li>Apply custom <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> to route DNS queries to specific resolvers depending on a user's OIDC claims.</li>
<li>Control <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a> to assign dedicated egress IPs based on OIDC claim attributes.</li>
</ul>
<p>For example, you can create a policy that routes traffic differently for users with <code>department=engineering</code> in their OIDC claims, or restrict access to certain destinations based on a user's role claim.</p>
<p>To get started, configure <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> on your identity provider and use the <strong>OIDC Claims</strong> selector in the Gateway policy builder.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/identity-selectors/">Identity-based policies</a>.</p>


<h2 id="2026-03-04">2026-03-04</h2>

<strong>Gateway Authorization Proxy and hosted PAC files (open beta)</strong>

<p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Gateway Authorization Proxy</a> and <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">PAC file hosting</a> are now in open beta for all plan types.</p>
<p>Previously, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">proxy endpoints</a> relied on static source IP addresses to authorize traffic, providing no user-level identity in logs or policies. The new authorization proxy replaces IP-based authorization with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> authentication, verifying who a user is before applying Gateway filtering without installing the WARP client.</p>
<p>This is ideal for environments where you cannot deploy a device client, such as virtual desktops (VDI), mergers and acquisitions, or compliance-restricted endpoints.</p>
<h4 id="2026-03-04-gateway-authorization-proxy-open-beta-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Identity-aware proxy traffic</strong> — Users authenticate through your identity provider (Okta, Microsoft Entra ID, Google Workspace, and others) via Cloudflare Access. Logs now show exactly which user accessed which site, and you can write <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity-based policies</a> like &quot;only the Finance team can access this accounting tool.&quot;</li>
<li><strong>Multiple identity providers</strong> — Display one or multiple login methods simultaneously, giving flexibility for organizations managing users across different identity systems.</li>
<li><strong>Cloudflare-hosted PAC files</strong> — Create and host <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">PAC files</a> directly in Cloudflare One with pre-configured templates for Okta and Azure, hosted at <code>https://pac.cloudflare-gateway.com/&lt;account-id&gt;/&lt;slug&gt;</code> on Cloudflare's global network.</li>
<li><strong>Simplified billing</strong> — Each user occupies a seat, exactly like they do with the Cloudflare One Client. No new metrics to track.</li>
</ul>
<h4 id="2026-03-04-gateway-authorization-proxy-open-beta-get-started">Get started</h4>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong> &gt; <strong>Proxy endpoints</strong>.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Create an authorization proxy endpoint</a> and configure Access policies.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">Create a hosted PAC file</a> or write your own.</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#3b-configure-browser-to-use-pac-file">Configure browsers</a> to use the PAC file URL.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">Install the Cloudflare certificate</a> for HTTPS inspection.</li>
</ol>
<p>For more details, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints documentation</a> and the <a href="https://blog.cloudflare.com/gateway-authorization-proxy-identity-aware-policies/">announcement blog post</a>.</p>


<h2 id="2026-02-27">2026-02-27</h2>

<strong>New protocols added for Gateway Protocol Detection (Beta)</strong>

<p>Gateway <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol Detection</a> now supports seven additional protocols in beta:</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>IMAP</td>
<td>Internet Message Access Protocol — email retrieval</td>
</tr>
<tr>
<td>POP3</td>
<td>Post Office Protocol v3 — email retrieval</td>
</tr>
<tr>
<td>SMTP</td>
<td>Simple Mail Transfer Protocol — email sending</td>
</tr>
<tr>
<td>MYSQL</td>
<td>MySQL database wire protocol</td>
</tr>
<tr>
<td>RSYNC-DAEMON</td>
<td>rsync daemon protocol</td>
</tr>
<tr>
<td>LDAP</td>
<td>Lightweight Directory Access Protocol</td>
</tr>
<tr>
<td>NTP</td>
<td>Network Time Protocol</td>
</tr>
</tbody>
</table>
<p>These protocols join the existing set of detected protocols (HTTP, HTTP2, SSH, TLS, DCERPC, MQTT, and TPKT) and can be used with the <em>Detected Protocol</em> selector in <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a> to identify and filter traffic based on the application-layer protocol, without relying on port-based identification.</p>
<p>If protocol detection is enabled on your account, these protocols will automatically be logged when detected in your Gateway network traffic.</p>
<p>For more information on using Protocol Detection, refer to the <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol detection documentation</a>.</p>


<h2 id="2025-12-17">2025-12-17</h2>

<strong>Shadow IT - domain level SaaS analytics</strong>

<p>Zero Trust has again upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>With this update, you can review data transfer metrics at the domain level, rather than just the application level, providing more granular insight into your data transfer patterns.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-domain.png" alt="New Domain Level Metrics" /></p>
<p>These metrics can be filtered by all available filters on the dashboard, including user, application, or content category.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="2025-11-06">2025-11-06</h2>

<strong>Applications to be remapped to the new categories</strong>

<p>We have previously added new application categories to better reflect their content and improve HTTP traffic management: refer to <a href="/cloudflare-one/changelog/gateway/#2025-10-28">Changelog</a>.
While the new categories are live now, we want to ensure you have ample time to review and adjust any existing rules you have configured against old categories.
The remapping of existing applications into these new categories will be completed by January 30, 2026.
This timeline allows you a dedicated period to:</p>
<ul>
<li>Review the new category structure.</li>
<li>Identify any policies you have that target the older categories.</li>
<li>Adjust your rules to reference the new, more precise categories before the old mappings change.
Once the applications have been fully remapped by January 30, 2026, you might observe some changes in the traffic being mitigated or allowed by your existing policies. We encourage you to use the intervening time to prepare for a smooth transition.</li>
</ul>
<p><strong>Applications being remappedd</strong></p>
<table>
<thead>
<tr>
<th>Application Name</th>
<th>Existing Category</th>
<th>New Category</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Photos</td>
<td>File Sharing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Flickr</td>
<td>File Sharing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>ADP</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Greenhouse</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>myCigna</td>
<td>Human Resources</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>UnitedHealthcare</td>
<td>Human Resources</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>ZipRecruiter</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Amazon Business</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Jobcenter</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Jobsuche</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Zenjob</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>DocuSign</td>
<td>Legal</td>
<td>Business</td>
</tr>
<tr>
<td>Postident</td>
<td>Legal</td>
<td>Business</td>
</tr>
<tr>
<td>Adobe Creative Cloud</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Airtable</td>
<td>Productivity</td>
<td>Development</td>
</tr>
<tr>
<td>Autodesk Fusion360</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Coursera</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Microsoft Power BI</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Tableau</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Duolingo</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Adobe Reader</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>AnpiReport</td>
<td>Productivity</td>
<td>Travel</td>
</tr>
<tr>
<td>ビズリーチ</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>doda (デューダ)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>求人ボックス</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>マイナビ2026</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Power Apps</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>RECRUIT AGENT</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>シフトボード</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>スタンバイ</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Doctolib</td>
<td>Productivity</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>Miro</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>MyFitnessPal</td>
<td>Productivity</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>Sentry Mobile</td>
<td>Productivity</td>
<td>Travel</td>
</tr>
<tr>
<td>Slido</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Arista Networks</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Atlassian</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>CoderPad</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>eAgreements</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Vmware</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Vmware Vcenter</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>AWS Skill Builder</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Microsoft Office 365 (GCC)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Microsoft Exchange Online (GCC)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Canva</td>
<td>Sales &amp; Marketing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Instacart</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Wawa</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>McDonald's</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Vrbo</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>American Airlines</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>Booking.com</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>Ticketmaster</td>
<td>Shopping</td>
<td>Entertainment &amp; Events</td>
</tr>
<tr>
<td>Airbnb</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>DoorDash</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Expedia</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>EasyPark</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>UEFA Tickets</td>
<td>Shopping</td>
<td>Entertainment &amp; Events</td>
</tr>
<tr>
<td>DHL Express</td>
<td>Shopping</td>
<td>Business</td>
</tr>
<tr>
<td>UPS</td>
<td>Shopping</td>
<td>Business</td>
</tr>
</tbody>
</table>
<p>For more information on creating HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>


<h2 id="2025-10-28">2025-10-28</h2>

<strong>New Application Categories added for HTTP Traffic Management</strong>

<p>To give you precision and flexibility while creating policies to block unwanted traffic, we are introducing new, more granular application categories in the Gateway product.</p>
<p>We have added the following categories to provide more precise organization and allow for finer-grained policy creation, designed around how users interact with different types of applications:</p>
<ul>
<li>Business</li>
<li>Education</li>
<li>Entertainment &amp; Events</li>
<li>Food &amp; Drink</li>
<li>Health &amp; Fitness</li>
<li>Lifestyle</li>
<li>Navigation</li>
<li>Photography &amp; Graphic Design</li>
<li>Travel</li>
</ul>
<p>The new categories are live now, but we are providing a transition period for existing applications to be fully remapped to these new categories.</p>
<p>The full remapping will be completed by January 30, 2026.</p>
<p>We encourage you to use this time to:</p>
<ul>
<li>Review the new category structure.</li>
<li>Identify and adjust any existing HTTP policies that reference older categories to ensure a smooth transition.</li>
</ul>
<p>For more information on creating HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>


<h2 id="2025-10-20">2025-10-20</h2>

<strong>Schedule DNS policies from the UI</strong>

<p>Admins can now create <a href="/cloudflare-one/traffic-policies/dns-policies/timed-policies/">scheduled DNS policies</a> directly from the Zero Trust dashboard, without using the API. You can configure policies to be active during specific, recurring times, such as blocking social media during business hours or gaming sites on school nights.</p>
<ul>
<li><strong>Preset Schedules</strong>: Use built-in templates for common scenarios like Business Hours, School Days, Weekends, and more.</li>
<li><strong>Custom Schedules</strong>: Define your own schedule with specific days and up to three non-overlapping time ranges per day.</li>
<li><strong>Timezone Control</strong>: Choose to enforce a schedule in a specific timezone (for example, US Eastern) or based on the local time of each user.</li>
<li><strong>Combined with Duration</strong>: Policies can have both a schedule and a duration. If both are set, the duration's expiration takes precedence.</li>
</ul>
<p>You can see the flow in the demo GIF:</p>
<p><img src="/assets/upstream/images/gateway/gateway-dns-scheduled-policies-ui.gif" alt="Schedule DNS policies demo" /></p>
<p>This update makes time-based DNS policies accessible to all Gateway customers, removing the technical barrier of the API.</p>


<h2 id="2025-10-10">2025-10-10</h2>

<strong>New domain categories added</strong>

<p>We have added three new domain categories under the Technology parent category, to better reflect online content and improve DNS filtering.</p>
<p><strong>New categories added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>26</td>
<td>Technology</td>
<td>194</td>
<td>Keep Awake Software</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>192</td>
<td>Remote Access</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>193</td>
<td>Shareware/Freeware</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>


<h2 id="2025-09-30">2025-09-30</h2>

<strong>Application granular controls for operations in SaaS applications</strong>

<p>Gateway users can now apply granular controls to their file sharing and AI chat applications through <a href="/cloudflare-one/traffic-policies/http-policies">HTTP policies</a>.</p>
<p>The new feature offers two methods of controlling SaaS applications:</p>
<ul>
<li><strong>Application Controls</strong> are curated groupings of Operations which provide an easy way for users to achieve a specific outcome. Application Controls may include <em>Upload</em>, <em>Download</em>, <em>Prompt</em>, <em>Voice</em>, and <em>Share</em> depending on the application.</li>
<li><strong>Operations</strong> are controls aligned to the most granular action a user can take. This provides a fine-grained approach to enforcing policy and generally aligns to the SaaS providers API specifications in naming and function.</li>
</ul>
<p>Get started using <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls">Application Granular Controls</a> and refer to the list of <a href="/cloudflare-one/traffic-policies/http-policies/granular-controls/#compatible-applications">supported applications</a>.</p>


<h2 id="2025-09-25">2025-09-25</h2>

<strong>Refine DLP Scans with New Body Phase Selector</strong>

<p>You can now more precisely control your HTTP DLP policies by specifying whether to scan the request or response body, helping to reduce false positives and target specific data flows.</p>
<p>In the Gateway HTTP policy builder, you will find a new selector called <em>Body Phase</em>. This allows you to define the direction of traffic the DLP engine will inspect:</p>
<ul>
<li><em>Request Body</em>: Scans data sent from a user's machine to an upstream service. This is ideal for monitoring data uploads, form submissions, or other user-initiated data exfiltration attempts.</li>
<li><em>Response Body</em>: Scans data sent to a user's machine from an upstream service. Use this to inspect file downloads and website content for sensitive data.</li>
</ul>
<p>For example, consider a policy that blocks Social Security Numbers (SSNs). Previously, this policy might trigger when a user visits a website that contains example SSNs in its content (the response body). Now, by setting the <strong>Body Phase</strong> to <em>Request Body</em>, the policy will only trigger if the user attempts to upload or submit an SSN, ignoring the content of the web page itself.</p>
<p>All policies without this selector will continue to scan both request and response bodies to ensure continued protection.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/#body-phase">Gateway HTTP policy selectors</a>.</p>


<h2 id="2025-09-11">2025-09-11</h2>

<strong>DNS filtering for private network onramps</strong>

<p><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/#dns-filtering">Magic WAN</a> and <a href="/mesh/features/routes/#dns-filtering">WARP Connector</a> users can now securely route their DNS traffic to the Gateway resolver without exposing traffic to the public Internet.</p>
<p>Routing DNS traffic to the Gateway resolver allows DNS resolution and filtering for traffic coming from private networks while preserving source internal IP visibility. This ensures Magic WAN users have full integration with our Cloudflare One features, including <a href="/cloudflare-one/traffic-policies/resolver-policies/#internal-dns">Internal DNS</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">hostname-based policies</a>.</p>
<p>To configure DNS filtering, change your Magic WAN or WARP Connector DNS settings to use Cloudflare's shared resolver IPs, <code>172.64.36.1</code> and <code>172.64.36.2</code>. Once you configure DNS resolution and filtering, you can use <em>Source Internal IP</em> as a traffic selector in your <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policies</a> for routing private DNS traffic to your <a href="/dns/internal-dns/">Internal DNS</a>.</p>


<h2 id="2025-08-27">2025-08-27</h2>

<strong>Shadow IT - SaaS analytics dashboard</strong>

<p>Zero Trust has significantly upgraded its <strong>Shadow IT analytics</strong>, providing you with unprecedented visibility into your organizations use of SaaS tools. With this dashboard, you can review who is using an application and volumes of data transfer to the application.</p>
<p>You can review these metrics against application type, such as Artificial Intelligence or Social Media. You can also mark applications with an approval status, including <strong>Unreviewed</strong>, <strong>In Review</strong>, <strong>Approved</strong>, and <strong>Unapproved</strong> designating how they can be used in your organization.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/shadow-it-analytics.png" alt="Cloudflare One Analytics Dashboards" /></p>
<p>These application statuses can also be used in Gateway HTTP policies, so you can block, isolate, limit uploads and downloads, and more based on the application status.</p>
<p>Both the analytics and policies are accessible in the Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a>, empowering organizations with better visibility and control.</p>


<h2 id="2025-08-21">2025-08-21</h2>

<strong>Gateway BYOIP Dedicated Egress IPs now available.</strong>

<p>Enterprise Gateway users can now use Bring Your Own IP (BYOIP) for dedicated egress IPs.</p>
<p>Admins can now onboard and use their own IPv4 or IPv6 prefixes to egress traffic from Cloudflare, delivering greater control, flexibility, and compliance for network traffic.</p>
<p>Get started by following the <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP onboarding process</a>. Once your IPs are onboarded, go to <strong>Gateway</strong> &gt; <strong>Egress policies</strong> and select or create an egress policy. In <strong>Select an egress IP</strong>, choose <em>Use dedicated egress IPs (Cloudflare or BYOIP)</em>, then select your BYOIP address from the dropdown menu.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-byoip-dedicated-egress-ips.png" alt="Screenshot of a dropdown menu adding a BYOIP IPv4 address as a dedicated egress IP in a Gateway egress policy" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP for dedicated egress IPs</a>.</p>


<h2 id="2025-07-28">2025-07-28</h2>

<strong>Scam domain category introduced under Security Threats</strong>

<p>We have introduced a new Security Threat category called <strong>Scam</strong>. Relevant domains are marked with the Scam category. Scam typically refers to fraudulent websites and schemes designed to trick victims into giving away money or personal information.</p>
<p><strong>New category added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>191</td>
<td>Scam</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>


<h2 id="2025-07-24">2025-07-24</h2>

<strong>Gateway HTTP Filtering on all ports available in open BETA</strong>

<p><a href="/cloudflare-one/traffic-policies/">Gateway</a> can now apply <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP filtering</a> to all proxied HTTP requests, not just traffic on standard HTTP (<code>80</code>) and HTTPS (<code>443</code>) ports. This means all requests can now be filtered by <a href="/cloudflare-one/traffic-policies/http-policies/antivirus-scanning/">A/V scanning</a>, <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">file sandboxing</a>, <a href="/cloudflare-one/data-loss-prevention/#data-in-transit">Data Loss Prevention (DLP)</a>, and more.</p>
<p>You can turn this <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">setting</a> on by going to <strong>Settings</strong> &gt; <strong>Network</strong> &gt; <strong>Firewall</strong> and choosing  <em>Inspect on all ports</em>.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-Inspection-all-ports.png" alt="HTTP Inspection on all ports setting" /></p>
<p>To learn more, refer to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">Inspect on all ports (Beta)</a>.</p>


<h2 id="2025-07-22">2025-07-22</h2>

<strong>Google Bard Application replaced by Gemini</strong>

<p>The <strong>Google Bard</strong> application (ID: 1198) has been deprecated and fully removed from the system. It has been replaced by the <strong>Gemini</strong> application (ID: 1340).
Any existing Gateway policies that reference the old Google Bard application will no longer function.
To ensure your policies continue to work as intended, you should update them to use the new Gemini application.
We recommend replacing all instances of the deprecated Bard application with the new Gemini application in your Gateway policies.
For more information about application policies, please see the <a href="/cloudflare-one/traffic-policies/application-app-types/">Cloudflare Gateway documentation</a>.</p>


<h2 id="2025-06-18">2025-06-18</h2>

<strong>Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025</strong>

<p><a href="/cloudflare-one/traffic-policies/">Gateway</a> will now evaluate <a href="/cloudflare-one/traffic-policies/network-policies/">Network (Layer 4) policies</a> <strong>before</strong> <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP (Layer 7) policies</a>. This change preserves your existing security posture and does not affect which traffic is filtered — but it may impact how notifications are displayed to end users.</p>
<p>This change will roll out progressively between <strong>July 14–18, 2025</strong>. If you use HTTP policies, we recommend reviewing your configuration ahead of rollout to ensure the user experience remains consistent.</p>
<h4 id="2025-06-17-new-order-of-enforcement-updated-order-of-enforcement">Updated order of enforcement</h4>
<p><strong>Previous order:</strong></p>
<ol>
<li>DNS policies</li>
<li>HTTP policies</li>
<li>Network policies</li>
</ol>
<p><strong>New order:</strong></p>
<ol>
<li>DNS policies</li>
<li><strong>Network policies</strong></li>
<li><strong>HTTP policies</strong></li>
</ol>
<h4 id="2025-06-17-new-order-of-enforcement-action-required-review-your-gateway-http-policies">Action required: Review your Gateway HTTP policies</h4>
<p>This change may affect block notifications. For example:</p>
<ul>
<li>You have an <strong>HTTP policy</strong> to block <code>example.com</code> and display a block page.</li>
<li>You also have a <strong>Network policy</strong> to block <code>example.com</code> silently (no client notification).</li>
</ul>
<p>With the new order, the Network policy will trigger first — and the user will no longer see the HTTP block page.</p>
<p>To ensure users still receive a block notification, you can:</p>
<ul>
<li>Add a client notification to your Network policy, or</li>
<li>Use only the HTTP policy for that domain.</li>
</ul>
<hr />
<h4 id="2025-06-17-new-order-of-enforcement-why-we-re-making-this-change">Why we’re making this change</h4>
<p>This update is based on user feedback and aims to:</p>
<ul>
<li>Create a more intuitive model by evaluating network-level policies before application-level policies.</li>
<li>Minimize <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-zero-trust-context">526 connection errors</a> by verifying the network path to an origin before attempting to establish a decrypted TLS connection.</li>
</ul>
<hr />
<p>To learn more, visit the <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">Gateway order of enforcement documentation</a>.</p>


<h2 id="2025-05-29">2025-05-29</h2>

<strong>New Gateway Analytics in the Cloudflare One Dashboard</strong>

<p>Users can now access significant enhancements to Cloudflare Gateway analytics, providing you with unprecedented visibility into your organization's DNS queries, HTTP requests, and Network sessions. These powerful new dashboards enable you to go beyond raw logs and gain actionable insights into how your users are interacting with the Internet and your protected resources.</p>
<p>You can now visualize and explore:</p>
<ul>
<li>Patterns Over Time: Understand trends in traffic volume and blocked requests, helping you identify anomalies and plan for future capacity.</li>
<li>Top Users &amp; Destinations: Quickly pinpoint the most active users, enabling better policy enforcement and resource allocation.</li>
<li>Actions Taken: See a clear breakdown of security actions applied by Gateway policies, such as blocks and allows, offering a comprehensive view of your security posture.</li>
<li>Geographic Regions: Gain insight into the global distribution of your traffic.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-analytics.png" alt="Gateway Analytics" /></p>
<p>To access the new overview, log in to your Cloudflare <a href="https://one.dash.cloudflare.com/">Zero Trust dashboard</a> and go to Analytics in the side navigation bar.</p>


<h2 id="2025-05-27">2025-05-27</h2>

<strong>Gateway Protocol Detection Now Available for Pay-as-you-go and Free Plans</strong>

<p>All Cloudflare One Gateway users can now use Protocol detection logging and filtering, including those on Pay-as-you-go and Free plans.</p>
<p>With Protocol Detection, admins can identify and enforce policies on traffic proxied through Gateway based on the underlying network protocol (for example, HTTP, TLS, or SSH), enabling more granular traffic control and security visibility no matter your plan tier.</p>
<p>This feature is available to enable in your account network settings for all accounts. For more information on using Protocol Detection, refer to the <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">Protocol detection documentation</a>.</p>


<h2 id="2025-05-14">2025-05-14</h2>

<strong>Domain Categories improvements</strong>

<p><strong>New categories added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Ads</td>
<td>66</td>
<td>Advertisements</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>185</td>
<td>Personal Finance</td>
</tr>
<tr>
<td>3</td>
<td>Business &amp; Economy</td>
<td>186</td>
<td>Brokerage &amp; Investing</td>
</tr>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>187</td>
<td>Compromised Domain</td>
</tr>
<tr>
<td>21</td>
<td>Security Threats</td>
<td>188</td>
<td>Potentially Unwanted Software</td>
</tr>
<tr>
<td>6</td>
<td>Education</td>
<td>189</td>
<td>Reference</td>
</tr>
<tr>
<td>9</td>
<td>Government &amp; Politics</td>
<td>190</td>
<td>Charity and Non-profit</td>
</tr>
</tbody>
</table>
<p><strong>Changes to existing categories</strong></p>
<table>
<thead>
<tr>
<th>Original Name</th>
<th>New Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>Religion</td>
<td>Religion &amp; Spirituality</td>
</tr>
<tr>
<td>Government</td>
<td>Government/Legal</td>
</tr>
<tr>
<td>Redirect</td>
<td>URL Alias/Redirect</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>


<h2 id="2025-05-13">2025-05-13</h2>

<strong>New Applications Added for DNS Filtering</strong>

<p>You can now create DNS policies to manage outbound traffic for an expanded list of applications.
This update adds support for 273 new applications, giving you more control over your organization's outbound traffic.</p>
<p>With this update, you can:</p>
<ul>
<li>Create DNS policies for a wider range of applications</li>
<li>Manage outbound traffic more effectively</li>
<li>Improve your organization's security and compliance posture</li>
</ul>
<p>For more information on creating DNS policies, see our <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policy documentation</a>.</p>


<h2 id="2025-04-28">2025-04-28</h2>

<strong>FQDN Filtering For Gateway Egress Policies</strong>

<p>Cloudflare One administrators can now control which egress IP is used based on a destination's fully qualified domain name (FDQN) within Gateway Egress policies.</p>
<ul>
<li>Host, Domain, Content Categories, and Application selectors are now available in the Gateway Egress policy builder in beta.</li>
<li>During the beta period, you can use these selectors with traffic on-ramped to Gateway with the WARP client, proxy endpoints (commonly deployed with PAC files), or Cloudflare Browser Isolation.
<ul>
<li>For WARP client support, additional configuration is required. For more information, refer to the <a href="/cloudflare-one/traffic-policies/egress-policies/#limitations">WARP client configuration documentation</a>.</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/gateway/Gateway-Egress-FQDN-Policy-preview.png" alt="Egress by FQDN and Hostname" /></p>
<p>This will help apply egress IPs to your users' traffic when an upstream application or network requires it, while the rest of their traffic can take the most performant egress path.</p>


<h2 id="2025-04-11">2025-04-11</h2>

<strong>HTTP redirect and custom block page redirect</strong>

<p>You can now use more flexible redirect capabilities in Cloudflare One with Gateway.</p>
<ul>
<li>A new <strong>Redirect</strong> action is available in the HTTP policy builder, allowing admins to redirect users to any URL when their request matches a policy. You can choose to preserve the original URL and query string, and optionally include policy context via query parameters.</li>
<li>For <strong>Block</strong> actions, admins can now configure a custom URL to display when access is denied. This block page redirect is set at the account level and can be overridden in DNS or HTTP policies. Policy context can also be passed along in the URL.</li>
</ul>
<p>Learn more in our documentation for <a href="/cloudflare-one/traffic-policies/http-policies/#redirect">HTTP Redirect</a> and <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/#redirect-to-a-block-page">Block page redirect</a>.</p>


<h2 id="2025-03-21">2025-03-21</h2>

<strong>Secure DNS Locations Management User Role</strong>

<p>We're excited to introduce the <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations"><strong>Cloudflare Zero Trust Secure DNS Locations Write role</strong></a>, designed to provide DNS filtering customers with granular control over third-party access when configuring their Protective DNS (PDNS) solutions.</p>
<p>Many DNS filtering customers rely on external service partners to manage their DNS location endpoints. This role allows you to grant access to external parties to administer DNS locations without overprovisioning their permissions.</p>
<p><strong>Secure DNS Location Requirements:</strong></p>
<ul>
<li>
<p>Mandate usage of <a href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip">Bring your own DNS resolver IP addresses</a> if available on the account.</p>
</li>
<li>
<p>Require source network filtering for IPv4/IPv6/DoT endpoints; token authentication or source network filtering for the DoH endpoint.</p>
</li>
</ul>
<p>You can assign the new role via Cloudflare Dashboard (<code>Manage Accounts &gt; Members</code>) or via API. For more information, refer to the <a href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations">Secure DNS Locations documentation</a>.</p>


<h2 id="2025-02-03">2025-02-03</h2>

<strong>Block files that are password-protected, compressed, or otherwise unscannable.</strong>

<p>Gateway HTTP policies can now block files that are password-protected, compressed, or otherwise unscannable.</p>
<p>These unscannable files are now matched with the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types">Download and Upload File Types traffic selectors</a> for HTTP policies:</p>
<ul>
<li>Password-protected Microsoft Office document</li>
<li>Password-protected PDF</li>
<li>Password-protected ZIP archive</li>
<li>Unscannable ZIP archive</li>
</ul>
<p>To get started inspecting and modifying behavior based on these and other rules, refer to <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP filtering</a>.</p>


<h2 id="2025-02-12">2025-02-12</h2>
<p><strong>Upload/Download File Size selectors for HTTP policies</strong></p>
<p>Gateway and DLP users can now create HTTP policies with the <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-size">Download and Upload File Size (MiB)</a> traffic selectors. This update allows users to block uploads or downloads based on file size.</p>
<h2 id="2025-02-02">2025-02-02</h2>
<p><strong>The default global Cloudflare root certificate expired on 2025-02-02 at 16:05 UTC</strong></p>
<p>If you installed the default Cloudflare certificate before 2024-10-17, you must generate a new certificate and activate it for your Zero Trust organization to avoid inspection errors. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/common-issues/#browser-and-certificate-issues">Troubleshooting</a> for instructions and troubleshooting steps.</p>
<h2 id="2025-01-08">2025-01-08</h2>
<p><strong>Bring your own resolver IP (BYOIP) for DNS locations</strong></p>
<p>Enterprise users can now <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip">provide an IP address</a> for a private DNS resolver to use with <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a>. Gateway supports bringing your own IPv4 and IPv6 addresses.</p>
<h2 id="2024-11-20">2024-11-20</h2>
<p><strong>Category filtering in the network policy builder</strong></p>
<p>Gateway users can now create network policies with the <a href="/cloudflare-one/traffic-policies/network-policies/#content-categories">Content Categories</a> and <a href="/cloudflare-one/traffic-policies/network-policies/#security-risks">Security Risks</a> traffic selectors. This update simplifies malicious traffic blocking and streamlines network monitoring for improved security management.</p>
<h2 id="2024-10-17">2024-10-17</h2>
<p><strong>Per-account Cloudflare root certificate</strong></p>
<p>Gateway users can now generate <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">unique root CAs</a> for their Zero Trust account. Both generated certificate and custom certificate users must <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#activate-a-root-certificate">activate a root certificate</a> to use it for inspection. Per-account certificates replace the default Cloudflare certificate, which is set to expire on 2025-02-02.</p>
<h2 id="2024-10-10">2024-10-10</h2>
<p><strong>Time-based policy duration</strong></p>
<p>Gateway now offers <a href="/cloudflare-one/traffic-policies/dns-policies/timed-policies/#time-based-policy-duration">time-based DNS policy duration</a>. With policy duration, you can configure a duration of time for a policy to turn on or set an exact date and time to turn a policy off.</p>
<h2 id="2024-10-04">2024-10-04</h2>
<p><strong>Expanded Gateway log fields</strong></p>
<p>Gateway now offers new fields in <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">activity logs</a> for DNS, network, and HTTP policies to provide greater insight into your users' traffic routed through Gateway.</p>
<h2 id="2024-09-30">2024-09-30</h2>
<p><strong>File sandboxing</strong></p>
<p>Gateway users on Enterprise plans can create HTTP policies with <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">file sandboxing</a> to quarantine previously unseen files downloaded by your users and scan them for malware.</p>
<h2 id="2024-07-30">2024-07-30</h2>
<p><strong>UK NCSC indicator feed publicly available in Gateway</strong></p>
<p>Gateway users on any plan can now use the <a href="/security-center/indicator-feeds/#publicly-available-feeds">PDNS threat intelligence feed</a> provided by the UK National Cyber Security Centre (NCSC) in DNS policies.</p>
<h2 id="2024-07-14">2024-07-14</h2>
<p><strong>Gateway DNS filter non-authenticated queries</strong></p>
<p>Gateway users can now select which endpoints to use for a given DNS location. Available endpoints include IPv4, IPv6, DNS over HTTPS (DoH), and DNS over TLS (DoT). Users can protect each configured endpoint by specifying allowed source networks. Additionally, for the DoH endpoint, users can filter traffic based on source networks and/or authenticate user identity tokens.</p>
<h2 id="2024-06-25">2024-06-25</h2>
<p><strong>Gateway DNS policy setting to ignore CNAME category matches</strong></p>
<p>Gateway now offers the ability to selectively ignore CNAME domain categories in DNS policies via the <a href="/cloudflare-one/traffic-policies/domain-categories/#ignore-cname-domain-categories"><strong>Ignore CNAME domain categories</strong> setting</a> in the policy builder and the <a href="/api/resources/zero_trust/subresources/gateway/subresources/rules/methods/create/"><code>ignore_cname_category_matches</code> setting</a> in the API.</p>
<h2 id="2024-04-05">2024-04-05</h2>
<p><strong>Gateway file type control improvements</strong></p>
<p>Gateway now offers a more extensive, categorized <a href="/cloudflare-one/traffic-policies/http-policies/#download-and-upload-file-types">list of files</a> to control uploads and downloads.</p>


