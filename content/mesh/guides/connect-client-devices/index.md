---
cp9:
  canonical: https://developers.cloudflare.com/mesh/guides/connect-client-devices/
  description: Connect laptops, phones, and desktops to Cloudflare Mesh and verify private network connectivity.
  full_title: Connect client devices to Cloudflare Mesh · Cloudflare Docs
  head_html: <title>Connect client devices to Cloudflare Mesh · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect laptops, phones, and desktops to Cloudflare Mesh and verify private network connectivity."><link rel="canonical" href="https://developers.cloudflare.com/mesh/guides/connect-client-devices/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/mesh/guides/connect-client-devices/index.md"><meta property="og:title" content="Connect client devices to Cloudflare Mesh · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect laptops, phones, and desktops to Cloudflare Mesh and verify private network connectivity."><meta property="og:url" content="https://developers.cloudflare.com/mesh/guides/connect-client-devices/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Mesh"><meta name="algolia_product_filter" content="Cloudflare Mesh"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Mesh"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/mesh/guides/connect-client-devices/#page","headline":"Connect client devices to Cloudflare Mesh \u00b7 Cloudflare Docs","description":"Connect laptops, phones, and desktops to Cloudflare Mesh and verify private network connectivity.","url":"https://developers.cloudflare.com/mesh/guides/connect-client-devices/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /mesh/guides/connect-client-devices/
  schema: 1
---
<p>Client devices — laptops, phones, and desktops — join your Mesh network by installing the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> and enrolling. Each device receives a <a href="/mesh/concepts/#mesh-ips">Mesh IP</a> and can immediately communicate with every other enrolled device and Mesh node.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">Device enrollment permissions</a> are configured for your account. The Mesh <a href="/mesh/get-started/">setup wizard</a> handles this automatically.</li>
</ul>
<h2 id="1-enroll-the-cloudflare-one-client"><ol>
<li>Enroll the Cloudflare One Client</li>
</ol></h2>
<p>Connect a laptop or phone to your Mesh network:</p>
<h3 id="windows-macos-and-linux">Windows, macOS, and Linux</h3>
<p>To enroll your device using the client GUI:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10724.md")
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
<h3 id="headless-windows-macos-and-linux-devices">Headless Windows, macOS, and Linux devices</h3>
<p>Do not use interactive CLI enrollment on a device without a browser. Instead, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/#check-for-service-token">create a Service Auth enrollment policy</a>. Configure the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization"><code>organization</code></a>, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#auth_client_id"><code>auth_client_id</code></a>, and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#auth_client_secret"><code>auth_client_secret</code></a> managed deployment parameters.</p>
<p>For platform-specific installation methods and configuration file locations, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/">Managed deployment</a>. For a complete Linux example, refer to <a href="/cloudflare-one/tutorials/deploy-client-headless-linux/">Deploy the Cloudflare One Client on headless Linux machines</a>.</p>
<p>This method works on <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">supported Windows, macOS, and Linux systems</a>. Service-token devices use the shared identity <code>non_identity@&lt;team-name&gt;.cloudflareaccess.com</code>. Policies based on identity provider users or groups do not apply to these devices. To assign device profiles, use the expression <code>identity.service_token_uuid == &quot;&lt;SERVICE_TOKEN_ID&gt;&quot;</code>, where <code>&lt;SERVICE_TOKEN_ID&gt;</code> is the service token resource UUID (<code>id</code>), not its <code>auth_client_id</code>. Place this <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/#service-token">Service Token selector</a> before broader OS or email profiles. Use the shared non-identity email only when all Service Auth devices should match the profile.</p>
<p>After enrollment, the device receives a Mesh IP and connects to your Mesh network.</p>
<h2 id="2-verify-connectivity"><ol start="2">
<li>Verify connectivity</li>
</ol></h2>
<p>From a Windows, macOS, or Linux device, test TCP connectivity to a Mesh node or another client device. For example, test SSH:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="os"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10728.md")
</div></div>
<p>Replace <code>&lt;MESH-IP&gt;</code> with the Mesh IP of a node (visible on the <a href="https://dash.cloudflare.com/?to=/:account/mesh">Mesh overview page</a>) or another enrolled device. Replace port <code>22</code> with the port used by your service. You can test HTTP services from a mobile browser. If you turned on the ICMP Gateway proxy, you can also run <code>ping &lt;MESH-IP&gt;</code> as a diagnostic check.</p>
<p>If the device profile routes <code>www.cloudflare.com</code> through WARP, verify the data path:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="os"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10731.md")
</div></div>
<p>In Include mode, expect <code>warp=off</code> for destinations that are not in the include list. Use the successful connection to an included Mesh IP as the data-path check. Do not rely only on the success message from <code>warp-cli</code>: Mesh connectivity requires Traffic and DNS mode. In DNS-only mode, use <code>warp-cli registration show</code> only to verify enrollment. DNS-only mode cannot carry Mesh traffic.</p>
<h2 id="what-devices-can-reach">What devices can reach</h2>
<p>Once connected, a client device can:</p>
<ul>
<li><strong>Other client devices</strong> — Reach any enrolled device by its Mesh IP. No Mesh nodes involved.</li>
<li><strong>Mesh nodes</strong> — Reach any online node by its Mesh IP. SSH, database connections, API calls all work.</li>
<li><strong>Subnets behind nodes</strong> — Access hosts on private networks that a node advertises via <a href="/mesh/features/routes/">CIDR routes</a> (for example, printers, databases, or servers that cannot run the client).</li>
</ul>
<p>All traffic is subject to your <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway network policies</a>, so you can control which users and devices can reach specific resources.</p>
<h2 id="split-tunnel-configuration">Split Tunnel configuration</h2>
<p>For client devices to reach Mesh IPs, the Mesh IP range must route through Cloudflare. How you configure this depends on your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel mode</a>.</p>
<h3 id="exclude-mode-default">Exclude mode (default)</h3>
<p>The Mesh setup wizard updates the default device profile to route the Mesh IP range through Cloudflare. If you did not use the wizard, or if another profile applies to the device, verify that <code>100.96.0.0/12</code> (or your custom device IP range) is not in the exclude list or contained by a broader exclusion.</p>
<p>Depending on your Cloudflare networking configuration, you may need to remove additional IPs from your exclude list. For a list of IPs to check, refer to <a href="/cloudflare-one/networks/routes/reserved-ips/">Reserved IP addresses</a>.</p>
<h3 id="include-mode">Include mode</h3>
<p>In Include mode, add the following to your include list:</p>
<ul>
<li><code>100.96.0.0/12</code> — Mesh IPs (device IPs)</li>
<li>Any CIDR routes you have <a href="/mesh/features/routes/">configured for your Mesh nodes</a></li>
</ul>
<p>The IPv4 range used for <a href="/mesh/features/routes/#hostname-routes">hostname routing</a> (<code>172.64.128.0/20</code>; requires MASQUE) and all Cloudflare One IPv6 ranges are <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">automatically routed through Cloudflare</a> and do not need to be added manually.</p>
<h2 id="firewall-considerations">Firewall considerations</h2>
<p>Some operating systems block inbound traffic from the Mesh IP range by default:</p>
<ul>
<li><strong>Windows</strong> — Windows Firewall blocks inbound traffic from <code>100.96.0.0/12</code>. Add a firewall rule that allows incoming requests from <code>100.96.0.0/12</code> for your desired protocols and ports.</li>
<li><strong>macOS / Linux</strong> — Most configurations allow this traffic by default. If you have custom firewall rules, ensure <code>100.96.0.0/12</code> is permitted.</li>
</ul>
