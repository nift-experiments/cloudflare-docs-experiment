---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/cloudflare-one/2/
  description: '2026-05-28'
  full_title: cloudflare-one changelog - page 2 | Cloudflare Docs
  head_html: <title>cloudflare-one changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-05-28"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/cloudflare-one/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="cloudflare-one changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-05-28"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/cloudflare-one/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/cloudflare-one/2/#page","headline":"cloudflare-one changelog - page 2 | Cloudflare Docs","description":"2026-05-28","url":"https://developers.cloudflare.com/changelog/product/cloudflare-one/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/cloudflare-one/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="high-availability-replica-management-for-cloudflare-mesh"><a href="/changelog/post/2026-05-28-mesh-ha-replica-ui/">High availability replica management for Cloudflare Mesh</a></h2>
<p><em>2026-05-28</em></p>
<p>The <a href="/mesh/">Cloudflare Mesh</a> dashboard now shows per-replica details for <a href="/mesh/features/high-availability/">high availability</a> nodes. You can see which replica is active, view each replica's Mesh IP and connection details, and manually trigger failover — all from the node detail page.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/mesh-ha-replicas.gif" alt="Mesh HA replica tabs showing active and passive replicas with per-replica Mesh IPs and a manual failover option" /></p>
<h4 id="2026-05-28-mesh-ha-replica-ui-what-s-new">What's new</h4>
<ul>
<li><strong>Replica tabs</strong> on the node detail page — switch between replicas to see each one's Mesh IP, edge data center, origin IP, platform, version, and uptime.</li>
<li><strong>Active/passive badges</strong> identify which replica is currently routing traffic.</li>
<li><strong>Manual failover</strong> — promote a passive replica to active with a single click. The previous active replica switches to standby.</li>
<li><strong>HA badge</strong> in the overview table identifies nodes running multiple replicas.</li>
<li><strong>Active replica IP</strong> shown in the overview table — the dashboard now resolves which replica is active and displays the correct Mesh IP.</li>
</ul>
<h4 id="2026-05-28-mesh-ha-replica-ui-manual-failover">Manual failover</h4>
<p>To manually promote a passive replica:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/?to=/:account/mesh">Cloudflare dashboard</a>, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
<li>Select an HA-enabled node.</li>
<li>Select the passive replica tab.</li>
<li>Select <strong>Promote to active</strong> and confirm.</li>
</ol>
<p>Traffic reroutes to the promoted replica immediately. Refer to <a href="/mesh/features/high-availability/">High availability</a> for details on failover behavior.</p>


<h2 id="write-regex-using-natural-language-in-cloudflare-one"><a href="/changelog/post/2026-05-27-cloudy-regex-assistance/">Write regex using natural language in Cloudflare One</a></h2>
<p><em>2026-05-27</em></p>
<p><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> policy selectors which support regular expressions can now be authored in the dashboard using natural language. When building a <a href="/cloudflare-one/traffic-policies/expression-syntax/">policy</a> with a regex-based selector (like <code>matches regex</code>), you can describe what you want to match in plain English and the Cloudflare Agent will generate and validate a corresponding regular expression.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-regex-ai-generation.png" alt="Write policy regex using natural language" /></p>
<p>To get started, select a regex-compatible selector in the <a href="/cloudflare-one/traffic-policies/">Gateway policy builder</a> and select the icon. You'll see an input field for natural language, such as &quot;any URL starting with /api/v1&quot; or &quot;.com, .net, and .app hosts which contain <code>gooogle</code> in the host.&quot;</p>
<p>You can also use the tool to explain existing regular expressions. If a policy already contains a regex pattern, you can instantly generate a plain-language description.</p>
<p>A built-in feedback mechanism allows you to rate each interaction to help improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare One firewall policies</a> and expect to see the same functionality supported soon in <a href="/cloudflare-one/data-loss-prevention/">Data loss prevention profiles</a>.</p>


<h2 id="granular-permissions-for-cloudflare-tunnel-and-cloudflare-mesh"><a href="/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</a></h2>
<p><em>2026-05-21</em></p>
<p>You can now scope Cloudflare permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.</p>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the resource picker now lists <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes as scopable resource types. You can:</p>
<ul>
<li>Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.</li>
<li>Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.</li>
<li>Scope a single policy to one or many Tunnels and Mesh nodes at once.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-how-it-works">How it works</h4>
<p>Granular permissions are a parallel layer to existing account-level roles — they do not replace them.</p>
<ul>
<li><strong>Existing account-level roles continue to work.</strong> A member with <code>Cloudflare Access</code> or <code>Cloudflare Zero Trust</code> retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.</li>
<li><strong>Granular permissions are additive.</strong> For any API request on a specific Tunnel or Mesh node, access is granted if the principal has <strong>either</strong> the account-level role <strong>or</strong> a granular permission for that resource.</li>
<li><strong>Resource enumeration is authorization-aware.</strong> Listing endpoints (<code>GET /accounts/{id}/cfd_tunnel</code>, <code>GET /accounts/{id}/warp_connector</code>) return only the resources the principal has at least read access to.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-get-started">Get started</h4>
<ul>
<li>Configure <a href="/tunnel/guides/granular-permissions/">granular permissions for Cloudflare Tunnel</a>.</li>
<li>Configure <a href="/cloudflare-one/networks/connectors/granular-permissions/">granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One</a>.</li>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
</ul>


<h2 id="refreshed-access-login-page"><a href="/changelog/post/2026-05-12-access-login-page-refresh/">Refreshed Access login page</a></h2>
<p><em>2026-05-12</em></p>
<p>The <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">Access login page</a> and <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time password (OTP)</a> page now feature a refreshed design that improves visual consistency, user trust, and mobile responsiveness.</p>
<p><strong>Before:</strong></p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-login-old.png" alt="Screenshot of the previous Access login page" /></p>
<p><strong>After:</strong></p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-login-new.png" alt="Screenshot of the updated Access login page" /></p>
<p>The updated login experience includes:</p>
<ul>
<li><strong>Unified authentication card</strong> - All sign-in options (identity provider buttons, email input, OTP) now appear in a single card with consistent styling, replacing the previous multi-section layout.</li>
<li><strong>Consistent button styling</strong> - Identity provider buttons use a uniform size and layout for easier scanning and selection.</li>
<li><strong>Better mobile experience</strong> - Responsive layout improvements ensure the login page renders correctly on phones and tablets.</li>
<li><strong>Dark mode support</strong> - The login page now supports dark mode.</li>
</ul>


<h2 id="new-accounts-assigned-a-single-ipv4-anycast-address"><a href="/changelog/post/2026-05-12-single-anycast-ip-default/">New accounts assigned a single IPv4 anycast address</a></h2>
<p><em>2026-05-12</em></p>
<p>New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.</p>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.</p>
<p>To request additional anycast IP addresses for your account, contact your account team.</p>
<p>For tunnel configuration guidance, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Cloudflare WAN or <a href="/magic-transit/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Magic Transit.</p>


<h2 id="custom-dhcp-options-on-cloudflare-one-appliance"><a href="/changelog/post/2026-05-07-appliance-dhcp-options/">Custom DHCP options on Cloudflare One Appliance</a></h2>
<p><em>2026-05-07</em></p>
<p>When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.</p>
<p>Each option is defined by <code>option_number</code>, <code>value</code>, and one of four value types: <code>text</code>, <code>integer</code>, <code>hex</code>, or <code>ip</code>. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>


<h2 id="source-based-breakout-and-prioritization-on-cloudflare-one-appliance"><a href="/changelog/post/2026-05-07-appliance-source-based-breakout/">Source-based breakout and prioritization on Cloudflare One Appliance</a></h2>
<p><em>2026-05-07</em></p>
<p>Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by <strong>source</strong> in addition to destination application. You can pin breakout or priority behavior to:</p>
<ul>
<li>A source LAN interface — VLANs attached to that LAN are included automatically.</li>
<li>A source IP address, range, or CIDR block.</li>
</ul>
<p>This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">Breakout traffic</a>.</p>


<h2 id="self-serve-provisioning-of-cloudflare-one-virtual-appliance-via-api"><a href="/changelog/post/2026-05-07-virtual-appliance-self-serve-api/">Self-serve provisioning of Cloudflare One Virtual Appliance via API</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now create, rotate, and delete Cloudflare One Virtual Appliance instances and their license keys directly via the API and Terraform.</p>
<ul>
<li>Create a virtual appliance and receive a license key: <code>POST /accounts/{account_id}/magic/connectors</code> with <code>device.provision_license: true</code>.</li>
<li>Rotate the license key for an existing virtual appliance: <code>PATCH /accounts/{account_id}/magic/connectors/{connector_id}</code> with <code>provision_license: true</code>. The previous key is immediately and irrevocably revoked.</li>
<li>Delete a virtual appliance to release the associated licensed device.</li>
</ul>
<p>The license key is returned in the response only once, at create or rotate time. Copy and store it securely.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>


<h2 id="ipv6-cidr-routes-for-cloudflare-mesh"><a href="/changelog/post/2026-05-06-mesh-ipv6-routes/">IPv6 CIDR routes for Cloudflare Mesh</a></h2>
<p><em>2026-05-06</em></p>
<p><a href="/mesh/">Cloudflare Mesh</a> nodes now support IPv6 CIDR routes. You can advertise both IPv4 and IPv6 subnets through your Mesh nodes, making IPv6-only or dual-stack private networks reachable from any enrolled device.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-ipv6-routes.png" alt="IPv6 CIDR routes on a Mesh node in the Cloudflare dashboard" /></p>
<p>To add an IPv6 route, follow the same steps as <a href="/mesh/features/routes/#add-a-route">adding an IPv4 route</a> — enter the IPv6 CIDR (for example, <code>fd00::/64</code>) when configuring the route in the <a href="https://dash.cloudflare.com/?to=/:account/mesh">dashboard</a> or via the API.</p>


<h2 id="post-quantum-ipsec-interoperability-with-third-party-devices"><a href="/changelog/post/2026-04-30-ipsec-post-quantum-third-party/">Post-quantum IPsec interoperability with third-party devices</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare IPsec now supports post-quantum key agreement with compatible third-party devices. <a href="https://www.cisco.com/">Cisco</a> and <a href="https://www.fortinet.com/">Fortinet</a> are the first third-party vendors validated to interoperate with Cloudflare IPsec using ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>Post-quantum IPsec uses <a href="https://datatracker.ietf.org/doc/rfc9370/">RFC 9370</a> and <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/">draft-ietf-ipsecme-ikev2-mlkem</a> to negotiate hybrid key agreement during the IKEv2 <code>IKE_INTERMEDIATE</code> phase. This combines classical Diffie-Hellman (Group 20) with ML-KEM-768 or ML-KEM-1024 to protect against <a href="https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later">harvest-now, decrypt-later</a> attacks.</p>
<p>Key details:</p>
<ul>
<li>Compatible with Cisco 8000 Series Secure Routers with IOS XR Release 26.1.1 and Fortinet FortiOS 7.6.6 and later.</li>
<li>Uses ML-KEM-768 or ML-KEM-1024 as an additional Key Exchange to DH Group 20.</li>
<li>Follows RFC 9370 and draft-ietf-ipsecme-ikev2-mlkem standards.</li>
<li>No additional licensing required.</li>
</ul>
<p>Post-quantum IPsec with third-party devices is now generally available with confirmed interoperability for the platforms listed above. Cloudflare intends to support interoperability with more vendors as they build out support for draft-ietf-ipsecme-ikev2-mlkem. Contact your account team to discuss support for additional vendors.</p>
<p>For supported key exchange methods and the list of validated platforms, refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#tested-third-party-vendor-interoperability">GRE and IPsec tunnels</a>.</p>


<h2 id="network-session-logs-now-available-for-all-on-ramps"><a href="/changelog/post/2026-04-24-nsl-all-onramps/">Network Session Logs now available for all on-ramps</a></h2>
<p><em>2026-04-24</em></p>
<p><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a> are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints (PAC files)</a> and <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> egress — on-ramps that previously did not generate session logs.</p>
<p>Customers who already consume the <code>zero_trust_network_sessions</code> dataset via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> or <a href="/log-explorer/">Log Explorer</a> may see increased log volume if they use these on-ramps.</p>
<p>For field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>. For traffic analysis, refer to <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics</a>.</p>


<h2 id="network-session-analytics-dashboard"><a href="/changelog/post/2026-04-20-network-session-analytics/">Network session analytics dashboard</a></h2>
<p><em>2026-04-20</em></p>
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


<h2 id="new-streamlined-creation-experience-for-access-applications-and-gateway-policies"><a href="/changelog/post/2026-04-15-new-rule-and-application-builders/">New, streamlined creation experience for Access Applications and Gateway Policies</a></h2>
<p><em>2026-04-15</em></p>
<p>The Cloudflare One dashboard now features redesigned builders for two core workflows: creating Gateway policies and configuring self-hosted Access applications.</p>
<h4 id="2026-04-15-new-rule-and-application-builders-gateway-rule-builder">Gateway rule builder</h4>
<p>The Gateway rule builder now features a redesigned user experience, bringing it in line with the Access policy builder experience. Improvements include:</p>
<ul>
<li><strong>Streamlined UX</strong> with clearer states and improved user interactions</li>
<li><strong>Wirefilter editing</strong> for viewing and editing Gateway rules directly from wirefilter expressions</li>
<li><strong>Preview state</strong> to review the impact of your policy in a simple graphic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-rule-builder.png" alt="New Gateway rule builder" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Traffic policies</a>.</p>
<h4 id="2026-04-15-new-rule-and-application-builders-access-application-builder-for-self-hosted-apps">Access application builder for self-hosted apps</h4>
<p>The self-hosted Access application builder now offers a simplified creation workflow with fewer steps from setup to save. Improvements include:</p>
<ul>
<li><strong>New application selection experience</strong> that makes choosing the right application type before you begin easier.</li>
<li><strong>Streamlined creation flow</strong> with fewer clicks to build and save an application</li>
<li><strong>Inline policy creation</strong> for building Access policies directly within the application creation flow</li>
<li><strong>Preview state</strong> to understand how your policies enforce user access before saving</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-application-builder.png" alt="New Access application builder" /></p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/">self-hosted applications</a>.</p>


<h2 id="introducing-cloudflare-mesh"><a href="/changelog/post/2026-04-14-cloudflare-mesh/">Introducing Cloudflare Mesh</a></h2>
<p><em>2026-04-14</em></p>
<p><a href="/mesh/">Cloudflare Mesh</a> is now available (<a href="https://blog.cloudflare.com/mesh/">blog post</a>). Mesh connects your services and devices with post-quantum encrypted networking, allowing you to route traffic privately between servers, laptops, and phones over TCP, UDP, and ICMP.</p>
<p><img src="/assets/upstream/images/cloudflare-one/connections/mesh-network-map.gif" alt="Cloudflare Mesh network map showing nodes and devices connected through Cloudflare" /></p>
<h4 id="2026-04-14-cloudflare-mesh-what-cloudflare-mesh-does">What Cloudflare Mesh does</h4>
<ul>
<li>Assigns a private <a href="/mesh/concepts/#mesh-ips">Mesh IP</a> to every enrolled device and node.</li>
<li>Enables any participant to reach any other participant by IP — including client-to-client, without deploying any infrastructure.</li>
<li>Supports <a href="/mesh/features/routes/">CIDR routes</a> for subnet routing through Mesh nodes.</li>
<li>Supports <a href="/mesh/features/high-availability/">high availability</a> with active-passive replicas for nodes with routes.</li>
<li>All traffic flows through Cloudflare, so <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>, <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a>, and access rules apply to every connection.</li>
</ul>
<h4 id="2026-04-14-cloudflare-mesh-what-changed">What changed</h4>
<ul>
<li><strong>WARP Connector</strong> is now <strong>Cloudflare Mesh</strong>. Existing WARP Connectors are now called mesh nodes. All existing deployments continue to work — no migration required.</li>
<li><strong>Peer-to-peer connectivity</strong> is now called <strong>Mesh connectivity</strong> and is part of the Cloudflare Mesh documentation.</li>
<li><strong>Mesh node limit</strong> increased from 10 to <strong>50 per account</strong>.</li>
<li>New <a href="https://dash.cloudflare.com/?to=/:account/mesh">dashboard experience</a> at <strong>Networking</strong> &gt; <strong>Mesh</strong> with an interactive network map, node management, route configuration, diagnostics, and a setup wizard.</li>
</ul>
<h4 id="2026-04-14-cloudflare-mesh-get-started">Get started</h4>
<p>Refer to the <a href="/mesh/">Cloudflare Mesh documentation</a> to set up your first Mesh network.</p>


<h2 id="link-aggregation-lacp-support-for-cloudflare-one-appliance"><a href="/changelog/post/2026-04-07-link-aggregation-lacp-appliance/">Link aggregation (LACP) support for Cloudflare One Appliance</a></h2>
<p><em>2026-04-07</em></p>
<p>Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.</p>
<p>This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.</p>
<p>To configure a Link Aggregation Group, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/link-aggregation/">Configure link aggregation groups</a>.</p>


<h2 id="organizations-is-now-in-public-beta-for-enterprises"><a href="/changelog/post/2026-04-06-organizations-public-beta/">Organizations is now in public beta for enterprises</a></h2>
<p><em>2026-04-06</em></p>
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


<h2 id="logs-ui-refresh"><a href="/changelog/post/2026-04-01-logs-ui-refresh/">Logs UI refresh</a></h2>
<p><em>2026-04-01</em></p>
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


<h2 id="user-risk-score-selector-in-access-policies"><a href="/changelog/post/2026-03-04-user-risk-score-access-policies/">User risk score selector in Access policies</a></h2>
<p><em>2026-03-04</em></p>
<p>You can now use <a href="/cloudflare-one/team-and-resources/users/risk-score/">user risk scores</a> in your <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. The new <strong>User Risk Score</strong> selector allows you to create Access policies that respond to user behavior patterns detected by Cloudflare's risk scoring system, including impossible travel, high DLP policy matches, and more.</p>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/#use-risk-scores-in-access-policies">Use risk scores in Access policies</a>.</p>


<h2 id="copy-cloudflare-one-resources-as-json-or-post-requests"><a href="/changelog/post/2026-03-copy-resources-as-json-or-post-requests/">Copy Cloudflare One resources as JSON or POST requests</a></h2>
<p><em>2026-03-02</em></p>
<p>You can now copy Cloudflare One resources as JSON or as a ready-to-use API POST request directly from the dashboard. This makes it simple to transition workflows into API calls, automation scripts, or infrastructure-as-code pipelines.</p>
<p>To use this feature, click the overflow menu (⋮) on any supported resource and select <strong>Copy as JSON</strong> or <strong>Copy as POST request</strong>. The copied output includes only the fields present on your resource, giving you a clean and minimal starting point for your own API calls.</p>
<p>Initially supported resources:</p>
<ul>
<li>Access applications</li>
<li>Access policies</li>
<li>Gateway policies</li>
<li>Resolver policies</li>
<li>Service tokens</li>
<li>Identity providers</li>
</ul>
<p>We will continue to add support for more resources throughout 2026.</p>


<h2 id="cloudflare-one-product-name-updates"><a href="/changelog/post/2026-02-17-product-name-updates/">Cloudflare One Product Name Updates</a></h2>
<p><em>2026-02-17</em></p>
<p>We are updating naming related to some of our Networking products to better clarify their place in the Zero Trust and Secure Access Service Edge (SASE) journey.</p>
<p>We are retiring some older brand names in favor of names that describe exactly what the products do within your network. We are doing this to help customers build better, clearer mental models for comprehensive SASE architecture delivered on Cloudflare.</p>
<h4 id="2026-02-17-product-name-updates-what-s-changing">What's changing</h4>
<ul>
<li><strong>Magic WAN</strong> → <strong>Cloudflare WAN</strong></li>
<li><strong>Magic WAN IPsec</strong> → <strong>Cloudflare IPsec</strong></li>
<li><strong>Magic WAN GRE</strong> → <strong>Cloudflare GRE</strong></li>
<li><strong>Magic WAN Connector</strong> → <strong>Cloudflare One Appliance</strong></li>
<li><strong>Magic Firewall</strong> → <strong>Cloudflare Network Firewall</strong></li>
<li><strong>Magic Network Monitoring</strong> → <strong>Network Flow</strong></li>
<li><strong>Magic Cloud Networking</strong> → <strong>Cloudflare One Multi-cloud Networking</strong></li>
</ul>
<p><strong>No action is required by you</strong> — all functionality, existing configurations, and billing will remain exactly the same.</p>
<p>For more information, visit the <a href="/cloudflare-one/">Cloudflare One documentation</a>.</p>


<h2 id="post-quantum-encryption-support-for-cloudflare-one-appliance"><a href="/changelog/post/2026-02-11-appliance-post-quantum-encryption/">Post-quantum encryption support for Cloudflare One Appliance</a></h2>
<p><em>2026-02-11</em></p>
<p>Cloudflare One Appliance version 2026.2.0 adds <a href="/ssl/post-quantum-cryptography/">post-quantum encryption</a> support using hybrid ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism).</p>
<p>The appliance now uses TLS 1.3 with hybrid ML-KEM for its connection to the Cloudflare edge. During the TLS handshake, the appliance and the edge share a symmetric secret over the TLS connection and inject it into the ESP layer of IPsec. This protects IPsec data plane traffic against harvest-now, decrypt-later attacks.</p>
<p>This upgrade deploys automatically to all appliances during their configured interrupt windows with no manual action required.</p>
<p>For more information, refer to <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a>.</p>


<h2 id="bgp-over-gre-and-ipsec-tunnels"><a href="/changelog/post/2026-01-30-bgp-over-tunnels/">BGP over GRE and IPsec tunnels</a></h2>
<p><em>2026-01-30</em></p>
<p>Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using IPsec and GRE tunnel on-ramps (beta).</p>
<p>Using BGP peering allows customers to:</p>
<ul>
<li>Automate the process of adding or removing networks and subnets.</li>
<li>Take advantage of failure detection and session recovery features.</li>
</ul>
<p>With this functionality, customers can:</p>
<ul>
<li>Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via IPsec and GRE tunnel on-ramps.</li>
<li>Secure the session by MD5 authentication to prevent misconfigurations.</li>
<li>Exchange routes dynamically between their devices and their Magic routing table.</li>
</ul>
<p>For configuration details, refer to:</p>
<ul>
<li><a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes">Configure BGP routes for Magic WAN</a></li>
<li><a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">Configure BGP routes for Magic Transit</a></li>
</ul>


<h2 id="configure-cloudflare-source-ips-beta"><a href="/changelog/post/2026-01-27-configure-cloudflare-source-ips/">Configure Cloudflare source IPs (beta)</a></h2>
<p><em>2026-01-27</em></p>
<p>Cloudflare source IPs are the IP addresses used by Cloudflare services (such as Load Balancing, Gateway, and Browser Isolation) when sending traffic to your private networks.</p>
<p>For customers using legacy mode routing, traffic to private networks is sourced from public Cloudflare IPs, which may cause IP conflicts. For customers using Unified Routing mode (beta), traffic to private networks is sourced from dedicated, non-Internet-routable private IPv4 range to ensure:</p>
<ul>
<li>Symmetric routing over private network connections</li>
<li>Proper firewall state preservation</li>
<li>Private traffic stays on secure paths</li>
</ul>
<p>Key details:</p>
<ul>
<li><strong>IPv4</strong>: Sourced from <code>100.64.0.0/12</code> by default, configurable to any <code>/12</code> CIDR</li>
<li><strong>IPv6</strong>: Sourced from <code>2606:4700:cf1:5000::/64</code> (not configurable)</li>
<li><strong>Affected connectors</strong>: GRE, IPsec, CNI, WARP Connector, and WARP Client (Cloudflare Tunnel is not affected)</li>
</ul>
<p>Configuring Cloudflare source IPs requires Unified Routing (beta) and the <code>Cloudflare One Networks Write</code> permission.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">Configure Cloudflare source IPs</a>.</p>


<h2 id="require-access-protection-for-zones"><a href="/changelog/post/2026-01-22-deny-by-default-for-zones/">Require Access protection for zones</a></h2>
<p><em>2026-01-22</em></p>
<p>You can now require Cloudflare Access protection for all hostnames in your account. When enabled, traffic to any hostname that does not have a matching Access application is automatically blocked.</p>
<p>This deny-by-default approach prevents accidental exposure of internal resources to the public Internet. If a developer deploys a new application or creates a DNS record without configuring an Access application, the traffic is blocked rather than exposed.</p>
<p><img src="/assets/upstream/images/changelog/access/require-cloudflare-access-protection.png" alt="Require Cloudflare Access protection in the dashboard" /></p>
<h4 id="2026-01-22-deny-by-default-for-zones-how-it-works">How it works</h4>
<ul>
<li><strong>Blocked by default</strong>: Traffic to all hostnames in the account is blocked unless an Access application exists for that hostname.</li>
<li><strong>Explicit access required</strong>: To allow traffic, create an Access application with an Allow or Bypass policy.</li>
<li><strong>Hostname exemptions</strong>: You can exempt specific hostnames from this requirement.</li>
</ul>
<p>To turn on this feature, refer to <a href="/cloudflare-one/access-controls/access-settings/require-access-protection/">Require Access protection</a>.</p>


<h2 id="breakout-traffic-visibility-via-netflow"><a href="/changelog/post/2025-12-31-connector-breakout-traffic-netflow/">Breakout traffic visibility via NetFlow</a></h2>
<p><em>2025-12-31</em></p>
<p>Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.</p>
<p>This feature allows you to:</p>
<ul>
<li>Monitor breakout traffic statistics in the Cloudflare dashboard.</li>
<li>View traffic patterns for applications configured to bypass Cloudflare.</li>
<li>Maintain visibility across all traffic passing through your Magic WAN Connector.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-wan/analytics/netflow-analytics/">NetFlow statistics</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/cloudflare-one/">Previous</a><span>Page 2 of 3</span><a class="pagination-next" rel="next" href="/changelog/product/cloudflare-one/3/">Next</a></nav>
