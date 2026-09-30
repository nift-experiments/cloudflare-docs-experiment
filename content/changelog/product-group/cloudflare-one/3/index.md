<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-one-client-for-windows-version-2026-6-880-0"><a href="/changelog/post/2026-07-21-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.880.0)</a></h2>
<p><em>2026-07-22</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<h2 id="browser-based-login-for-plaintext-http-private-applications"><a href="/changelog/post/2026-07-20-http-private-apps-l7-auth/">Browser-based login for plaintext HTTP private applications</a></h2>
<p><em>2026-07-20</em></p>
<p>Cloudflare Access now uses the standard browser-based login flow for <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a> served over plaintext HTTP on port <code>80</code>.</p>
<p>Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an <code>Authentication required</code> pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">application token</a> on success.</p>
<p>This brings the HTTP experience in line with HTTPS apps (with <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">Gateway TLS decryption</a> turned on). No configuration change is required. The Cloudflare One Client is still required to route traffic to the private network, but it no longer manages the Access session for HTTP apps.</p>
<p>Other non-HTTP protocols (SSH, RDP, arbitrary TCP/UDP) continue to use the Cloudflare One Client notification flow.</p>


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


<h2 id="new-header-control-options-for-gateway-http-policies"><a href="/changelog/post/2026-07-17-http-request-header-manipulation/">New header control options for Gateway HTTP policies</a></h2>
<p><em>2026-07-17</em></p>
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


<h2 id="bulk-print-pdfs-for-browser-based-rdp"><a href="/changelog/post/2026-07-16-rdp-bulk-print/">Bulk print PDFs for browser-based RDP</a></h2>
<p><em>2026-07-16</em></p>
<p>Users in browser-based RDP sessions can now print multiple PDF files as a single print job. Copy the files to your clipboard on the remote machine, then select <strong>Print all PDFs</strong> in the clipboard panel. The files are combined into one PDF and sent to your local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/rdp-bulk-print.png" alt="The clipboard panel showing the Print all PDFs option for multiple selected PDF files." /></p>
<p>Bulk print is available in Chromium-based browsers and Firefox. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#print-pdfs">Print PDFs for browser-based RDP</a>.</p>


<h2 id="internal-dns-is-now-generally-available"><a href="/changelog/post/2026-07-15-internal-dns-ga/">Internal DNS is now generally available</a></h2>
<p><em>2026-07-15</em></p>
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


<h2 id="source-code-detection-improvements"><a href="/changelog/post/2026-07-10-source-code-detection-improvements/">Source code detection improvements</a></h2>
<p><em>2026-07-10</em></p>
<p>Data Loss Prevention (DLP) source code detection now focuses on identifying whole source code file uploads and downloads. Previously, source code detection performed partial scans resulting in a higher rate of false positives. Since only whole source code files are evaluated, code embedded in other content — such as chat messages, documentation, or code samples — is no longer flagged as source code, removing a common source of false positives.</p>
<p>Source code detection requires a minimum of 500 characters to evaluate a file. Files below this threshold are not flagged to reduce noise. This threshold filters out small fragments that lack enough context for reliable classification.</p>
<p>Enable and set <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds">confidence levels</a> to tune match sensitivity. A higher confidence level reduces false positives by requiring stronger signals that the content is truly source code. A lower confidence level catches more files at the cost of additional noise.</p>
<p>Source code detection applies to standalone source code files in <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policies</a>. It does not detect source code embedded within other file types or payloads, such as <code>.docx</code> files or chat messages.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code">Source Code predefined profiles</a>.</p>


<h2 id="wi-fi-signal-and-network-performance-analytics-for-cloudflare-one-client-devices"><a href="/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/">Wi-Fi signal and network performance analytics for Cloudflare One Client devices</a></h2>
<p><em>2026-07-09</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment.</p>
<p>The <strong>Device Monitoring</strong> page now analyzes hardware and network data between a Cloudflare One Client device and Cloudflare's edge, so you can diagnose connectivity and performance issues. Previously, this data was only available in raw DEX Device State Event logs, which required you to build your own analytics to interpret it.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-summary.png" alt="Device Monitoring summary with connection status, connection mode, Wi-Fi signal strength, traffic performance, and device health" /></p>
<p>A summary at the top of the page shows the health of each category at a glance, using <strong>Good</strong>, <strong>Fair</strong>, and <strong>Poor</strong> labels:</p>
<ul>
<li><strong>Connection</strong> — connection status, Cloudflare One Client mode, and tunnel type over time</li>
<li><strong>Wi-Fi signal strength</strong> — signal measured in dBm over time, with thresholds that flag a weak signal</li>
<li><strong>Traffic performance</strong> — upstream and downstream performance, including network throughput on the active interface</li>
<li><strong>Device health</strong> — hardware metrics such as CPU, memory, and disk</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-wifi-network.png" alt="Wi-Fi signal strength and network throughput charts on the Device Monitoring page" /></p>
<p>You can filter by category and adjust the time range to correlate a device's metrics with a user's reported issue.</p>
<p>These analytics are available to all Cloudflare One customers at no additional cost.</p>
<p>To learn more, refer to the <a href="/cloudflare-one/insights/dex/monitoring/">DEX monitoring documentation</a>.</p>


<h2 id="zero-trust-networks-route-endpoints-and-cloudflare-tunnel-connections-field-retiring-on-october-5-2026"><a href="/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/">Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026</a></h2>
<p><em>2026-07-09</em></p>
<p>On <strong>October 5, 2026</strong>, two changes take effect across the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> and <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>: the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the <code>connections</code> field. If you manage private network routes or read tunnel connection details through the API, <code>cloudflared</code>, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-route-endpoints">Route endpoints</h4>
<p>The CIDR-encoded route endpoints are deprecated in favor of the standard, <code>route_id</code>-based endpoints that already exist today. Both sets of endpoints route a private network through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or <a href="/mesh/">Cloudflare Mesh</a> (the API still refers to Mesh nodes as <code>warp_connector</code>) — only the request shape changes.</p>
<p><strong>Deprecated endpoints (removed October 5, 2026):</strong></p>
<ul>
<li>Create a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create/"><code>POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
<li>Update a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit/"><code>PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
<li>Delete a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete/"><code>DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
</ul>
<p><strong>Replacement endpoints:</strong></p>
<ul>
<li>Create a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/"><code>POST /accounts/{account_id}/teamnet/routes</code></a></li>
<li>Update a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit/"><code>PATCH /accounts/{account_id}/teamnet/routes/{route_id}</code></a></li>
<li>Delete a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete/"><code>DELETE /accounts/{account_id}/teamnet/routes/{route_id}</code></a></li>
</ul>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-what-is-changing">What is changing</h4>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Deprecated (CIDR-encoded path)</th>
<th align="left">Replacement</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Route identifier</td>
<td align="left">URL-encoded CIDR in the path (<code>/network/{ip_network_encoded}</code>)</td>
<td align="left"><code>route_id</code> in the path (<code>network</code> moves to the request body on create)</td>
</tr>
<tr>
<td align="left">Create</td>
<td align="left"><code>POST .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>POST .../teamnet/routes</code> with <code>network</code> and <code>tunnel_id</code> in the body</td>
</tr>
<tr>
<td align="left">Update</td>
<td align="left"><code>PATCH .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>PATCH .../teamnet/routes/{route_id}</code></td>
</tr>
<tr>
<td align="left">Delete</td>
<td align="left"><code>DELETE .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>DELETE .../teamnet/routes/{route_id}</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-action-required">Action required</h4>
<ol>
<li>Capture each route's <code>route_id</code> by calling <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/">List tunnel routes</a>, or read it from the response the first time you create a route with the replacement endpoint.</li>
<li>Update any scripts, backend services, or CI/CD pipelines that call the CIDR-encoded endpoints directly.</li>
<li>If you manage routes with the <code>cloudflared tunnel route ip add | delete</code> commands, upgrade <code>cloudflared</code> to the <a href="https://github.com/cloudflare/cloudflared/releases">latest version</a>.</li>
<li>If you manage routes with Terraform, make sure you are on a current version of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route"><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></a> resource and the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>.</li>
</ol>
<pre><code class="language-bash">&#35; Before: create a route by URL-encoding the CIDR into the path&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: create a route with the network in the request body&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;network&quot;: &quot;172.16.0.0/16&quot;, &quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: update or delete a route using its route_id&#10;curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;comment&quot;: &quot;Updated comment for this route.&quot;}&#x27;&#10;&#10;curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-cloudflare-tunnel-and-cloudflare-mesh-connections">Cloudflare Tunnel and Cloudflare Mesh connections</h4>
<p>Starting the same day, the <code>connections</code> array is removed from list and get responses for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> nodes (the <code>cfd_tunnel</code> and <code>warp_connector</code> API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.</p>
<p>This affects:</p>
<ul>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
</ul>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-action-required-1">Action required</h4>
<p>Fetch connection details from the tunnel-specific connections endpoint instead of parsing it off the list or get response. For Cloudflare Tunnel, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections</code></a>. For Cloudflare Mesh, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections</code></a>.</p>
<pre><code class="language-bash">&#35; Before: read connections off the tunnel object&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;&#35; After: query connections directly&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Update any dashboards, monitoring scripts, or automation that parses <code>connections</code> from the tunnel list or get response. <code>cloudflared</code> and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-why-we-are-making-these-changes">Why we are making these changes</h4>
<ul>
<li><strong>Smaller, faster responses.</strong> Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.</li>
<li><strong>A single way to identify a route.</strong> Consolidating on <code>route_id</code> removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.</li>
<li><strong>Consistency across the API.</strong> Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.</li>
</ul>
<p>To learn more, refer to the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a>, the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>, and <a href="/cloudflare-one/networks/routes/">Routes</a> documentation.</p>


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


<h2 id="ip-lists-ids-and-sip-rules-supported-in-unified-routing"><a href="/changelog/post/2026-07-08-unified-routing-iplist-ids-sip/">IP lists, IDS, and SIP rules supported in Unified Routing</a></h2>
<p><em>2026-07-08</em></p>
<p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> IP lists, IDS, and SIP rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. These features require a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Threat Intel Lists, Rate Limiting, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>


<h2 id="cloudflare-one-client-for-windows-version-2026-6-850-0"><a href="/changelog/post/2026-07-07-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.850.0)</a></h2>
<p><em>2026-07-08</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix addresses a Windows authentication issue in the embedded WebView2 browser. Single sign-on could fail to use the Windows primary account, causing users to be prompted for an interactive sign-in. The embedded authentication browser now allows SSO providers to use the OS primary account when available.</p>


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


<h2 id="cloudflare-one-client-for-linux-version-2026-6-836-0"><a href="/changelog/post/2026-07-01-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.836.0)</a></h2>
<p><em>2026-07-02</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This package is the same release as 2026.6.822.0, with a fix for our RPM package. Previously the repository served a single build to every OS version, so an install could pull a dependency that isn't available on that release. The repository now serves the correct build for each operating system version, so installs automatically pull the dependencies that version requires. Debian and Ubuntu were not affected.</p>
<p>If you installed version 2026.6.822.0 on an RPM-based distribution, we recommend refreshing your repository configuration:</p>
<pre><code class="language-bash">sudo curl -fsSL https://pkg.cloudflareclient.com/cloudflare-warp-ascii.repo | sudo tee /etc/yum.repos.d/cloudflare-warp.repo&#10;sudo dnf clean all&#10;sudo dnf install cloudflare-warp&#10;</code></pre>


<h2 id="fix-redirect-url-fragment-encoding-for-single-page-applications"><a href="/changelog/post/2026-07-01-spa-redirect-fragment-fix/">Fix redirect URL fragment encoding for single-page applications</a></h2>
<p><em>2026-07-01</em></p>
<p>Access now correctly preserves URL fragment characters (<code>/</code>, <code>?</code>, <code>=</code>, <code>&amp;</code>, <code>;</code>) when redirecting users back to an application after login. Previously, these characters were encoded with <code>encodeURIComponent</code>, which mangled fragment-based routes used by single-page applications (SPAs).</p>
<p>For example, an SPA URL like <code>https://app.example.com/#/dashboard?tab=settings&amp;view=advanced</code> would previously redirect to a broken URL after login. This is now handled correctly.</p>
<p>If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.</p>


<h2 id="independent-mfa-for-infrastructure-applications"><a href="/changelog/post/2026-07-01-ssh-mfa-piv-keys/">Independent MFA for infrastructure applications</a></h2>
<p><em>2026-07-01</em></p>
<p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.</p>
<p>With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, <code>root</code>) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.</p>
<h4 id="2026-07-01-ssh-mfa-piv-keys-enrollment">Enrollment</h4>
<p>Users enroll their YubiKey PIV key through the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. For enrollment instructions and SSH client setup, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps">Enroll a PIV key for infrastructure apps</a>.</p>
<h4 id="2026-07-01-ssh-mfa-piv-keys-configuration">Configuration</h4>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Enforce MFA for infrastructure applications</a>.</p>


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


<h2 id="cloudflare-one-client-for-linux-version-2026-6-822-0"><a href="/changelog/post/2026-06-29-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.822.0)</a></h2>
<p><em>2026-06-30</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li><a href="/mesh/">Cloudflare Mesh</a> functionality using the Cloudflare One Client is now supported on RHEL 9 and 10.</li>
<li>Cloudflare Mesh now supports <a href="/mesh/features/routes/#hostname-routes">hostname-based routing</a>.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the system display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>Fixed the in-client captive-portal browser rendering a blank &quot;Success&quot; page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Fixed an issue where some Debian releases experienced inaccurate version reporting for posture checks.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p>For RHEL deployments, this release introduces a dependency on the <a href="https://docs.fedoraproject.org/en-US/epel/">Extra Packages for Enterprise Linux</a> repository (EPEL). The EPEL repository provides packages that support the captive portal detection’s in-app browser authentication and system tray icon. See <a href="https://docs.fedoraproject.org/en-US/epel/getting-started/">Getting started with EPEL</a> for instructions on enabling EPEL.</p>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
</ul>


<h2 id="cloudflare-one-client-for-macos-version-2026-6-822-0"><a href="/changelog/post/2026-06-29-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.6.822.0)</a></h2>
<p><em>2026-06-30</em></p>
<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Added support for dashboard-managed client version deployments. Administrators can now upgrade or downgrade the client version on enrolled devices directly from the Zero Trust dashboard. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a> for details.</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>Fixed the in-client captive-portal browser rendering a blank &quot;Success&quot; page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>When deploying with Microsoft Intune, the client may be repeatedly reinstalled because Intune adds the client's embedded framework bundles to its install-detection list, and those frameworks cannot be detected as installed on their own. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/#repeated-reinstalls-on-macos-with-microsoft-intune">Repeated reinstalls on macOS with Microsoft Intune</a> for the workaround.</li>
</ul>


<h2 id="cloudflare-one-client-for-windows-version-2026-6-822-0"><a href="/changelog/post/2026-06-29-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.822.0)</a></h2>
<p><em>2026-06-30</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Added mandatory authentication. When enabled via MDM, the Cloudflare One Client blocks all Internet traffic from the moment the machine boots until the user authenticates, closing the visibility gap on newly deployed devices and during re-authentication. See the <a href="https://blog.cloudflare.com/mandatory-authentication-mfa/">announcement blog</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-no-auth-no-internet/">documentation</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Added support for dashboard-managed client version deployments. Administrators can now upgrade or downgrade the client version on enrolled devices directly from the Zero Trust dashboard. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a> for details.</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in Windows Accessibility settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>The UseWebView2 registry value (HKLM\SOFTWARE\Cloudflare\CloudflareWARP\UseWebView2 = y) is once again honored by the new GUI for authentication, so administrators who prefer the embedded WebView2 browser for sign-in can opt back in. This setting was effectively ignored in the previous release; the default browser was always used. This key is now also honored for re-authentications.</li>
<li>Fixed a crash in the authentication browser when navigating to a site that prompts for browser permissions (microphone, camera, notifications, etc.). The same fix had previously landed for the captive-portal browser; this extends it to the auth browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Fixed a high CPU issue when the device wakes from sleep.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Single sign-on in the embedded WebView2 authentication browser may fail to use the Windows primary account, prompting for an interactive sign-in.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>In rare cases, a registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Windows ARM may prompt the user to close running applications while trying to install this version. Simply click &quot;Ok&quot; with the default highlighted option.</li>
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


<h2 id="cloudflare-one-client-for-macos-version-2026-6-782-1"><a href="/changelog/post/2026-06-24-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.6.782.1)</a></h2>
<p><em>2026-06-25</em></p>
<p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release introduces upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation.</p>
<p><strong>Additional changes and improvements</strong></p>
<p>This release also introduces multiple fixes and improvements including:</p>
<ul>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/2/">Previous</a><span>Page 3 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/4/">Next</a></nav>
