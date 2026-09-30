---
cp9:
  canonical: https://developers.cloudflare.com/mesh/get-started/
  description: Set up Cloudflare Mesh and connect your first server, laptop, or phone to your private network.
  full_title: Get started with Cloudflare Mesh · Cloudflare Docs
  head_html: <title>Get started with Cloudflare Mesh · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Cloudflare Mesh and connect your first server, laptop, or phone to your private network."><link rel="canonical" href="https://developers.cloudflare.com/mesh/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/mesh/get-started/index.md"><meta property="og:title" content="Get started with Cloudflare Mesh · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Cloudflare Mesh and connect your first server, laptop, or phone to your private network."><meta property="og:url" content="https://developers.cloudflare.com/mesh/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Mesh"><meta name="algolia_product_filter" content="Cloudflare Mesh"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Cloudflare Mesh"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/mesh/get-started/#page","headline":"Get started with Cloudflare Mesh \u00b7 Cloudflare Docs","description":"Set up Cloudflare Mesh and connect your first server, laptop, or phone to your private network.","url":"https://developers.cloudflare.com/mesh/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /mesh/get-started/
  schema: 1
---
<p>Set up Cloudflare Mesh so your devices and servers can reach each other by private IP.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>
<p>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></p>
</li>
<li>
<p>A <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Zero Trust organization</a> with an active subscription, including the Free plan</p>
</li>
<li>
<p>A laptop or phone to connect as a client device</p>
</li>
<li>
<p>(Optional) A Linux server to deploy a Mesh node</p>
<details class="nb-details"><summary>Linux server requirements</summary><div class="nb-details-body">
</li>
</ul>
@input("content/.markup/bodies/10734.md")
</div></details>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="mesh-nodes-are-optional">Mesh nodes are optional</h3>
@markup("md", "content/.markup/bodies/10733.md")
</aside>
<p>Cloudflare Mesh requires that the Mesh node's <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> is configured to use <a href="/mesh/concepts/#protocol-requirement">MASQUE</a>. Hostname routes, IPv6 CIDR routes, and high availability do not work if the device profile uses WireGuard instead.</p>
<h2 id="choose-a-participant-type">Choose a participant type</h2>
<p>Choose an enrollment method based on what you want to connect:</p>
<table>
<thead>
<tr>
<th>Goal</th>
<th>Participant type</th>
<th>Enrollment method</th>
<th>Browser required</th>
</tr>
</thead>
<tbody>
<tr>
<td>Run a service or route a subnet from Linux</td>
<td><a href="#1-configure-mesh">Mesh node</a></td>
<td>Connector token</td>
<td>No</td>
</tr>
<tr>
<td>Connect an unattended Windows, macOS, or Linux device</td>
<td><a href="/mesh/guides/connect-client-devices/#headless-windows-macos-and-linux-devices">Headless client device</a></td>
<td>Service token and managed deployment parameters</td>
<td>No</td>
</tr>
<tr>
<td>Connect a user device with identity</td>
<td><a href="#2-connect-a-client-device">Client device</a></td>
<td>Interactive identity provider enrollment</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="1-configure-mesh"><ol>
<li>Configure Mesh</li>
</ol></h2>
<p>Choose the dashboard wizard or API and Terraform resources.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10745.md")
</div></div>
<h2 id="2-connect-a-client-device"><ol start="2">
<li>Connect a client device</li>
</ol></h2>
<p>Connect a laptop or phone to your Mesh network:</p>
<h3 id="windows-macos-and-linux">Windows, macOS, and Linux</h3>
<p>To enroll your device using the client GUI:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10750.md")
</div></div>
<h3 id="ios-and-android">iOS and Android</h3>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Download</a> and install the Cloudflare One Agent app.</li>
<li>Launch the Cloudflare One Agent app.</li>
<li>Select <strong>Next</strong>.</li>
<li>Review the privacy policy and select <strong>Accept</strong>.</li>
<li>Enter your <span class="nb-glossary-tooltip" title="team name">team name</span>.</li>
<li>Complete the authentication steps required by your organization.</li>
<li>After authenticating, select <strong>Install VPN Profile</strong>.</li>
<li>In the <strong>Connection request</strong> popup window, select <strong>OK</strong>.</li>
<li>If you did not enable <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect">auto-connect</a>, manually turn on the switch to <strong>Connected</strong>.</li>
</ol>
<p>Once you see a <strong>Connected</strong> status, your device is on the mesh and receives its own Mesh IP.</p>
<h2 id="3-test-connectivity"><ol start="3">
<li>Test connectivity</li>
</ol></h2>
<p>From a Windows, macOS, or Linux client device, verify TCP connectivity to a Mesh node or another enrolled device. For example, test SSH:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="os"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10754.md")
</div></div>
<p>Replace <code>&lt;MESH-IP&gt;</code> with the Mesh IP shown on the Mesh overview page. Replace port <code>22</code> with the port used by your service. You can test HTTP services from a mobile browser. A connected client or healthy connector status does not verify peer connectivity. Verify the application protocol you intend to use. If you turned on the ICMP Gateway proxy, you can also run <code>ping &lt;MESH-IP&gt;</code> as a diagnostic check.</p>
<h2 id="logs">Logs</h2>
<p>Traffic from Mesh nodes appears in <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway activity logs</a> with the identity <code>warp_connector@&lt;your-team-name&gt;.cloudflareaccess.com</code>. Client device traffic appears in Gateway activity logs under the enrolled user's identity.</p>
<h2 id="required-account-settings">Required account settings</h2>
<p>The dashboard wizard configures the following Cloudflare One settings automatically for new deployments. Non-wizard deployments must configure the same settings:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>What it does</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">Device enrollment policy</a></td>
<td>Allows devices to enroll into your Cloudflare One account using email-based <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN</a>. Only created if you do not already have an existing device enrollment policy in your account.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">Device profile</a></td>
<td>Creates a profile configured with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> in <strong>Include mode</strong>, so only Mesh traffic routes through Cloudflare. This prevents disrupting existing network connectivity on your server. Only created if you do not already have an active Mesh node (formerly WARP Connector) in your account.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-all-cloudflare-one-traffic-to-reach-enrolled-devices">Allow all Cloudflare One traffic to reach enrolled devices</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#assign-a-unique-ip-address-to-each-device">Assign a unique IP address to each device</a></td>
<td>Enables device-to-device connectivity for Mesh networking.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a></td>
<td>Enables TCP and UDP proxying for Mesh services. ICMP proxying is optional and supports diagnostics such as <code>ping</code> and <code>traceroute</code>.</td>
</tr>
</tbody>
</table>
<p>For automated deployments, the device profile documentation includes API and Terraform examples. Set <code>service_mode_v2 = { mode = &quot;warp&quot; }</code>, replace the generic example's <code>wireguard</code> protocol with <code>tunnel_protocol = &quot;masque&quot;</code>, and configure Split Tunnels to route <code>100.96.0.0/12</code> through Cloudflare. Match Mesh nodes with <code>identity.email == &quot;warp_connector@&lt;TEAM_NAME&gt;.cloudflareaccess.com&quot;</code>, and place this profile before broader profiles. The device enrollment documentation includes the Terraform enrollment-policy flow.</p>
<h3 id="automated-settings">Automated settings</h3>
<p>The <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_device_settings"><code>cloudflare_zero_trust_device_settings</code></a> resource supports unique device IPs and the TCP and UDP Gateway proxies:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_zero_trust_device_settings&quot; &quot;mesh&quot; {&#10;	account_id                        = var.cloudflare_account_id&#10;	use_zt_virtual_ip                 = true&#10;	gateway_proxy_enabled             = true&#10;	gateway_udp_proxy_enabled         = true&#10;}&#10;</code></pre>
<h3 id="human-only-settings">Human-only settings</h3>
<p>The Terraform resource does not configure <strong>Allow all Cloudflare One traffic to reach enrolled devices</strong> or the ICMP Gateway proxy. Before connecting participants, turn on enrolled-device reachability in the dashboard. Turn on ICMP only if you require <code>ping</code>, <code>traceroute</code>, or another ICMP-based workflow.</p>
<h3 id="existing-cloudflare-one-accounts">Existing Cloudflare One accounts</h3>
<p>If your account already has a Cloudflare One deployment, the setup wizard will not overwrite your existing configuration. Verify the following settings are enabled for Mesh to work:</p>
<ul>
<li>[ ] <strong>Device enrollment</strong> — At least one <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">enrollment rule</a> must exist so that devices and nodes can register with your account.</li>
<li>[ ] <strong>Device profile for Mesh nodes</strong> — Your Mesh nodes need a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">device profile</a> that routes the Mesh IP range (<code>100.96.0.0/12</code>) through Cloudflare. In Include mode, add the Mesh range. In Exclude mode, verify that no custom or legacy entry contains the Mesh range.</li>
<li>[ ] <strong>Mesh connectivity</strong> — In your device profile settings, enable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-all-cloudflare-one-traffic-to-reach-enrolled-devices">Allow all Cloudflare One traffic to reach enrolled devices</a>.</li>
<li>[ ] <strong>Unique device IPs</strong> — Enable <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#assign-a-unique-ip-address-to-each-device">Assign a unique IP address to each device</a> so that each participant gets a routable Mesh IP.</li>
<li>[ ] <strong>Client mode</strong> — Mesh nodes must run in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">Traffic and DNS mode</a>. DNS-only or proxy-only modes are not supported.</li>
<li>[ ] <strong>Traffic proxying</strong> — Turn on the <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a> for the protocols you use. TCP and UDP carry Mesh services. ICMP supports diagnostic tools such as <code>ping</code> and <code>traceroute</code>.</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<ul>
<li><strong>Node shows as Offline</strong> — On the server, run <code>warp-cli status</code>. If the output does not show <code>Status update: Connected</code>:
<ul>
<li>Run <code>warp-cli connect</code>.</li>
<li>If your private network uses a firewall to restrict Internet traffic, ensure that it allows the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">WARP ports and IPs</a>.</li>
<li>Review your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/">WARP daemon logs</a> for information about why the connection is failing.</li>
</ul>
</li>
<li><strong>Client device cannot reach Mesh IPs</strong> — Verify that your Split Tunnel configuration routes the Mesh IP range (<code>100.96.0.0/12</code>) through Cloudflare. For details, refer to <a href="/mesh/guides/connect-client-devices/">Connect client devices</a>.</li>
<li><strong>Windows firewall blocks Mesh traffic</strong> — Windows Firewall blocks inbound traffic from <code>100.96.0.0/12</code> by default. Add a firewall rule that allows incoming requests from this range for your desired protocols and ports.</li>
</ul>
<p>For general client issues, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/">Troubleshoot the Cloudflare One Client</a>.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/mesh/guides/connect-client-devices/"><strong>Connect client devices</strong></a> — Platform-specific installation details, Split Tunnel configuration, and firewall considerations.</li>
<li><a href="/mesh/guides/run-mesh-in-containers/"><strong>Run in Docker / Kubernetes</strong></a> — Deploy a Mesh node as a Docker container for Docker Compose, Kubernetes, and CI/CD pipelines.</li>
<li><a href="/mesh/features/routes/"><strong>Add routes</strong></a> — Make an entire subnet behind your node reachable (databases, printers, other servers).</li>
<li><a href="/mesh/features/high-availability/"><strong>Enable high availability</strong></a> — Run multiple replicas for production resilience.</li>
<li><a href="/mesh/best-practices/"><strong>Tips and best practices</strong></a> — Cloud VPC configuration, updating the client, running alongside cloudflared.</li>
</ul>
