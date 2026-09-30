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
<li>Enter your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ol>
@markup("md", "content/.markup/bodies/10725.md")
</div>.
6. Complete the authentication steps required by your organization.
7. After authenticating, select **Install VPN Profile**.
8. In the **Connection request** popup window, select **OK**.
9. If you did not enable [auto-connect](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect), manually turn on the switch to **Connected**.
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
