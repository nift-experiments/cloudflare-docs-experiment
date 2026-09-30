<h1 id="changelog">Changelog</h1>

<h2 id="waf-release-2026-07-14"><a href="/changelog/post/2026-07-14-waf-release/">WAF Release - 2026-07-14</a></h2>
<p><em>2026-07-14</em></p>
<p>This release introduces new rules targeting critical infrastructure vulnerabilities. These include an unauthenticated memory disclosure flaw in Citrix NetScaler ADC and Gateway (CVE-2026-8451) and a high-severity pre-authentication remote code execution (RCE) vulnerability in Progress Kemp LoadMaster (CVE-2026-8037).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-8451: An insufficient input validation vulnerability affects Citrix NetScaler ADC and NetScaler Gateway appliances configured as a SAML Identity Provider (IdP). Remote, unauthenticated attackers can exploit this flaw by sending malformed requests to trigger a memory overread, allowing them to leak chunks of sensitive data from adjacent appliance memory.</p>
</li>
<li>
<p>CVE-2026-8037: A critical OS command injection vulnerability in Progress Kemp LoadMaster load balancers allows unauthenticated remote attackers to achieve remote code execution (RCE).</p>
</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="78826e3223b94da493a2ade876973ac4">76973ac4</code>
</td>
<td>N/A</td>
<td>Citrix Netscaler ADC - Insufficient Input Validation - CVE:CVE-2026-8451</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6b64d216620449fbb273d07910233f36">10233f36</code>
</td>
<td>N/A</td>
<td>Progress Kemp LoadMaster - Remote Code Execution - CVE:CVE-2026-8037</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>		
</tbody>
</table>


<h2 id="precursor-introduces-session-based-bot-detection"><a href="/changelog/post/2026-07-13-precursor-session-based-detection/">Precursor introduces session-based bot detection</a></h2>
<p><em>2026-07-13</em></p>
<p>Precursor is rolling out to all customers starting today. Precursor is client-side JavaScript that enables session-based bot detection.</p>
<p>You can <a href="https://blog.cloudflare.com/introducing-precursor">read the announcement blog</a> for background on why we built Precursor and how session-level behavioral detection works.</p>
<p>With Precursor enabled, Cloudflare can:</p>
<ul>
<li>Continuously evaluate behavioral signals across a session</li>
<li>Re-validate challenge clearance as behavior changes</li>
<li>Update bot scores with session context</li>
<li>Provide client-side visibility where none previously existed</li>
</ul>
<p>It integrates with existing protections, including Security Rules, and can be enabled directly from the Cloudflare dashboard with configurable modes to balance security and user experience.</p>
<img src="/images/precursor/enabling_precursor.gif" alt="Animated walkthrough of enabling Precursor in the Cloudflare dashboard" style="border:1px solid #e5e7eb;border-radius:6px;display:block;margin:16px 0;" />
<p>To learn more, refer to the <a href="/cloudflare-challenges/precursor/">Precursor documentation</a>.</p>


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


<h2 id="new-options-to-manage-ai-traffic"><a href="/changelog/post/2026-07-01-ai-traffic-options/">New options to manage AI traffic</a></h2>
<p><em>2026-07-01</em></p>
<p>Not all AI traffic is the same. Now, all customers — including those on the Free plan — can manage AI crawlers based on what they actually do on your site. Cloudflare groups AI traffic into three behaviors you can control independently: <a href="/bots/concepts/bot/#ai-bots">Search, Agent, and Training</a>. This lets you keep the automated traffic that sends readers and revenue back to you, while blocking the traffic that only takes from your content.</p>
<p>Each behavior maps to a real use case. <strong>Search</strong> covers crawlers that index your content so they can answer questions about it later, where you should expect referral traffic or other equitable compensation in return. <strong>Agent</strong> covers automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents. <strong>Training</strong> covers crawlers that take your content to train or fine-tune a model. For each preset you can choose to block on all pages, block only on pages that display ads, or choose not to block.</p>
<p><img src="/assets/upstream/images/changelog/bots/ai-bot-traffic-policies.png" alt="The Configure AI bot traffic policies screen, where Search, Agent, and Training can each be set to allow, block, or block only on pages with ads" /></p>
<p>Starting <strong>September 15, 2026</strong>, new domains onboarding to Cloudflare receive updated defaults: Bots classified as Training or as Agent are blocked on pages that display ads, while <strong>Search</strong> remains allowed. On that date, multi-purpose crawlers that combine Search and Training will be affected by the new defaults to block Training. All customers can <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/settings">opt out of the new defaults</a> at any time before September 15.</p>


<h2 id="more-visibility-into-bot-traffic-with-botbase-and-business-insights"><a href="/changelog/post/2026-07-01-botbase-attribution-business-insights/">More visibility into bot traffic with BotBase and Business Insights</a></h2>
<p><em>2026-07-01</em></p>
<p>With Content Independence Day 2026, <a href="/bots/get-started/bot-management/">Enterprise Bot Management</a> customers get two new tools that make bot traffic far easier to see and reason about: <a href="/bots/botbase/">BotBase</a>, a searchable directory of every bot Cloudflare tracks, and <a href="/bots/business-insights/">Business Insights</a>, a dashboard that shows how much value each crawler sends back to your business.</p>
<p>BotBase is Cloudflare's directory of all known bots and agents, available directly in the dashboard. It shows how Cloudflare classifies each bot by behavior — Search, Agent, Training, and other categories such as Transact, Data Collection, SEO, and Ads Verification — so you can understand why a given crawler is visiting you. You can search and filter the full catalogue, filter your own traffic down to a single bot to investigate its activity on your zone, and copy any bot's detection ID to target it precisely in <a href="/security/rules/">Security rules</a>. Every tracked bot in BotBase is also published in <a href="https://radar.cloudflare.com/bots/directory">Cloudflare Radar's bots and agents directory</a>.</p>
<p>Business Insights is built for content owners and business decision-makers who want to know which bots help or harm their business, without reading rule syntax. The dashboard reports crawl-to-referral ratios both site-wide and per bot operator — comparing how often a company crawls your content against how many visitors it actually refers back — over the last 24 hours, 7 days, or 30 days. Each operator is labeled with Cloudflare's <a href="/bots/concepts/bot/verified-bots/">updated classification</a> and an action status of Allowed, Blocked, or Partially blocked, giving stakeholders a shared, at-a-glance view of the AI traffic reaching your site.</p>
<p><img src="/assets/upstream/images/changelog/bots/attribution-business-insights.png" alt="The Business Insights dashboard, showing bot traffic, content page requests, crawl-to-referral ratio, and a per-operator bot activity table" /></p>


<h2 id="waf-release-2026-07-01"><a href="/changelog/post/2026-07-01-waf-release/">WAF Release - 2026-07-01</a></h2>
<p><em>2026-07-01</em></p>
<p>This release adds targeted coverage for a path traversal flaw in Fortinet FortiSandbox (CVE-2026-39813) and transitions the Anomaly:Header:User-Agent - Fake Bing or MSN Bot rule action from Block to Disabled.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-39813: A path traversal vulnerability in Fortinet FortiSandbox allows remote, unauthenticated attackers to read arbitrary files from the underlying filesystem due to insufficient validation of user-supplied input paths.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="32075e19b1494117ac5915e8d84c92c9">d84c92c9</code>
</td>
<td>N/A</td>
<td>Fortinet FortiSandbox - Path Traversal - CVE:CVE-2026-39813</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ae20608d93b94e97988db1bbc12cf9c8">c12cf9c8</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:User-Agent - Fake Bing or MSN Bot</td>
<td>Enabled</td>
<td>Disabled</td>
<td>
				We are changing the action for this rule from BLOCK to Disabled
</td>
</tr>
</tbody>
</table>


<h2 id="regionalized-ip-bindings-for-regional-services"><a href="/changelog/post/2026-06-23-regionalized-ip-bindings/">Regionalized IP Bindings for Regional Services</a></h2>
<p><em>2026-06-23</em></p>
<p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>


<h2 id="waf-release-2026-06-23"><a href="/changelog/post/2026-06-23-waf-release/">WAF Release - 2026-06-23</a></h2>
<p><em>2026-06-23</em></p>
<p>This week's release introduces new managed protection to address a critical pre-authentication OS command injection vulnerability in Ivanti Sentry (CVE-2026-10520).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-10520: An OS command injection vulnerability in Ivanti Sentry allows remote, unauthenticated attackers to execute arbitrary system commands with root privileges. The flaw stems from improper sanitization of input strings parsed during internal configuration handling.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="500a90789f874345b60b0de7242fdf83">242fdf83</code>
</td>
<td>N/A</td>
<td>Ivanti Sentry - Command Injection - CVE:CVE-2026-10520</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>		
</tbody>
</table>


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


<h2 id="post-quantum-ml-dsa-certificates-for-authenticated-origin-pulls-and-custom-origin-trust-store"><a href="/changelog/post/2026-06-17-pqc-mldsa-aop-cots/">Post-quantum ML-DSA certificates for Authenticated Origin Pulls and Custom Origin Trust Store</a></h2>
<p><em>2026-06-17</em></p>
<p>Cloudflare now accepts <a href="https://csrc.nist.gov/pubs/fips/204/final">ML-DSA</a> (FIPS 204) post-quantum certificates on the connection between Cloudflare's edge and your origin server. Combined with our existing <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a> key agreement, this lets you establish end-to-end post-quantum authentication on the Cloudflare-to-origin connection.</p>
<p>ML-DSA is supported in two origin-facing features:</p>
<ul>
<li><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a> (AOP) — upload an ML-DSA client certificate that Cloudflare will present during the mTLS handshake to your origin. Available at both zone-level and per-hostname scopes.</li>
<li><a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a> (COTS) — upload an ML-DSA certificate authority that Cloudflare will trust when validating your origin server certificate under <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) encryption mode</a>.</li>
</ul>
<p>Refer to <a href="/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures">Post-quantum signatures</a> for certificate generation and setup guidance, and to <a href="/ssl/post-quantum-cryptography/pqc-cloudflare-products/">PQC in Cloudflare products</a> for the current post-quantum deployment status across Cloudflare.</p>


<h2 id="use-cloudforce-one-threat-intelligence-in-waf-rules"><a href="/changelog/post/2026-06-15-threat-intelligence-fields/">Use Cloudforce One threat intelligence in WAF rules</a></h2>
<p><em>2026-06-15</em></p>
<p>You can now match incoming requests against Cloudforce One threat intelligence in your WAF rules. A new detection looks up the client IP address of each request against the threat intelligence database. If the IP was involved in threat activity in the past seven days, Cloudflare populates <code>cf.intel.ip.*</code> fields that you can use in <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a>.</p>
<p>The detection populates the following fields. Use the <a href="/ruleset-engine/rules-language/functions/#any"><code>any()</code></a> function with the <code>[*]</code> wildcard to match array values:</p>
<ul>
<li><code>cf.intel.ip.datasets</code> — the dataset that flagged the IP address (<code>ddos</code> or <code>waf</code>).</li>
<li><code>cf.intel.ip.target_industries</code> — industries the IP address has targeted.</li>
<li><code>cf.intel.ip.attacker_names</code> — known threat actors associated with the IP address.</li>
<li><code>cf.intel.ip.attacker_countries</code> — source countries of the threat activity.</li>
<li><code>cf.intel.ip.target_countries</code> — countries the IP address has targeted.</li>
</ul>
<p>For example, the following custom rule expression blocks requests from IP addresses associated with DDoS activity that have targeted France:</p>
<pre><code class="language-txt">any(cf.intel.ip.target_countries[*] == &quot;FR&quot;) and any(cf.intel.ip.datasets[*] == &quot;ddos&quot;)&#10;</code></pre>
<p>These fields work with the Cloudflare API and Terraform. Matches are logged in <a href="/waf/analytics/security-analytics/">Security Analytics</a>.</p>
<p>The threat intelligence detection is available to customers with an active <a href="/security-center/cloudforce-one/">Cloudforce One</a> subscription. For more information, refer to <a href="/waf/detections/threat-intelligence/">Threat intelligence</a>.</p>


<h2 id="waf-release-2026-06-15"><a href="/changelog/post/2026-06-15-waf-release/">WAF Release - 2026-06-15</a></h2>
<p><em>2026-06-15</em></p>
<p>This week's release introduces new managed protection to address a critical SQL injection vulnerability in Ghost CMS (CVE-2026-26980) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic. These rules protect affected installations from unauthorized data exfiltration at the network edge.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-26980: A blind SQL injection vulnerability in the Ghost CMS Content API (versions 3.24.0 to 6.19.0) allows unauthenticated remote attackers to inject malicious SQL commands via query parameters due to improper input validation.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="439c4ef64b32447989bdf412b4c29bc6">b4c29bc6</code>
</td>
<td>N/A</td>
<td>Ghost CMS - SQLi - CVE:CVE-2026-26980</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6c64b68ef5ed45e7a622cdaab56f403f">b56f403f</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>		
</tbody>
</table>


<h2 id="automated-cease-and-desist-templates-for-brand-protection"><a href="/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/">Automated Cease and Desist templates for Brand Protection</a></h2>
<p><em>2026-06-10</em></p>
<p><strong>TL;DR:</strong> Brand Protection now features an <strong>Automated Cease &amp; Desist (C&amp;D)</strong> workflow. When you discover an infringing domain hosted outside of Cloudflare, you can instantly generate, review, and download a custom-branded, pre-filled legal notice in seconds.</p>
<h4 id="2026-06-08-brand-protection-cease-and-desist-letters-why-this-matters">Why this matters</h4>
This update introduces a major shift from pure detection to actionable enforcement, eliminating the manual burden for your Trust & Safety and Legal teams:
<ul>
<li><strong>Instant WHOIS and Recipient Lookup:</strong> We automatically scrape registrar data and WHOIS contact information (such as the registrant or registrar abuse email) behind the scenes, highlighting exactly where your notice needs to be sent</li>
<li><strong>Smart Template Automation:</strong> We pre-fill your custom-branded templates with essential metadata, including the infringing domain, registrar name, and discovery date.</li>
<li><strong>Tailored Enforcement Tones:</strong> Choose from three default layout strategies depending on the severity of the infrastructure match:
<ul>
<li><em>Exact Match:</em> A formal demand for identical trademark infringements</li>
<li><em>Similar Match:</em> A standard notice optimized for typosquatting (one-character distance matches)</li>
<li><em>Friendly Tone:</em> An amicable initial outreach for potential unintentional or accidental infringements</li>
</ul>
</li>
<li><strong>Full Editing Control:</strong> Before creating the final PDF, a real-time review screen allows you to fine-tune the messaging, modify placeholders, and ensure your text aligns perfectly with internal legal standards</li>
</ul>
<h4 id="2026-06-08-brand-protection-cease-and-desist-letters-how-it-works">How it works</h4>
When reviewing a malicious domain match inside your dashboard, your enforcement path splits depending on where the attacker is located:
<ol>
<li><strong>On the Cloudflare Network:</strong> If the domain uses Cloudflare’s network or registrar, trigger our existing integrated abuse reporting flow with one click.</li>
<li><strong>Hosted Elsewhere:</strong> If the domain is hosted on an external provider, click the <strong>Generate C&amp;D Letter</strong> option to launch the new document builder, pick your template, verify the auto-populated recipient data, and download your finalized PDF.</li>
</ol>
<p>You can manage your templates and enforce matches by going to the <strong>Cloudflare Dashboard &gt; Application Security &gt; Brand Protection</strong> and selecting your detected Brand Protection matches.
For more information, read the <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>
<blockquote>
<p><strong>Note:</strong> Cloudflare does not represent you and cannot provide you with legal advice. Only you can decide whether your rights have been infringed, whether a cease and desist letter is appropriate, and what that letter should say.</p>
</blockquote>


<h2 id="waf-release-2026-06-09"><a href="/changelog/post/2026-06-09-waf-release/">WAF Release - 2026-06-09</a></h2>
<p><em>2026-06-09</em></p>
<p>This release introduces new detections for a critical SQL injection vulnerability in Drupal installations utilizing PostgreSQL (CVE-2026-9082), alongside targeted protection for an unsafe deserialization flaw in the Mirasvit Cache Warmer extension (CVE-2026-45247). Additionally, this release includes coverage for a prototype pollution vector in Axios (CVE-2026-40175) and a new generic rule designed to identify and block sophisticated SQL Injection (SQLi) bypass attempts leveraging obfuscated boolean logic.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-9082: A database abstraction vulnerability affects Drupal sites configured with a PostgreSQL backend. Remote, unauthenticated attackers can exploit this flaw via crafted inputs to inject malicious SQL commands and access or manipulate backend data.</p>
</li>
<li>
<p>CVE-2026-45247: A PHP Object Injection vulnerability exists in the Mirasvit Cache Warmer extension for Magento and Adobe Commerce. This flaw stems from unsafe deserialization of untrusted user input, enabling unauthenticated attackers to execute arbitrary code on the hosting server.</p>
</li>
<li>
<p>CVE-2026-40175: A prototype pollution vulnerability affects the Axios HTTP client library. Attackers can exploit this to inject malicious properties into the global JavaScript object prototype, potentially causing application crashes (Denial of Service) or executing unauthorized code depending on the application structure.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of these vulnerabilities could allow unauthenticated attackers to execute arbitrary code, manipulate database contents, or induce application crashes, leading to severe operational disruption or complete server compromise. These newly deployed signatures intercept these advanced malicious payloads at the edge before they can interact with vulnerable software configurations.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b4f88cb767874def810edd0b387cf935">387cf935</code>
</td>
<td>N/A</td>
<td>Axios - Prototype Pollution - CVE:CVE-2026-40175</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="098997bb8b5f48abb4039bd6417eb9e0">417eb9e0</code>
</td>
<td>N/A</td>
<td>Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - Body</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8a7650b99ec04a91a19b8295fd3857fd">fd3857fd</code>
</td>
<td>N/A</td>
<td>Drupal - PostgreSQL SQLi - CVE:CVE-2026-9082 - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="525c0871787840e6a6193f6caee241d2">aee241d2</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1ec4aeaf7900463397b82b35d8620070">d8620070</code>
</td>
<td>N/A</td>
<td>SQLi - Obfuscated Boolean - Headers</td>
<td>N/A</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="fb74766654c44ff2a5204dc4e0be4d47">e0be4d47</code>
</td>
<td>N/A</td>
<td>Mirasvit Cache Warmer - PHP Object Injection - CVE:CVE-2026-45247</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="create-waf-rules-directly-from-threat-events-saved-views"><a href="/changelog/post/2026-06-08-create-waf-rules-from-threat-events/">Create WAF rules directly from Threat Events saved views</a></h2>
<p><em>2026-06-08</em></p>
<p>Cloudforce One users can now turn <a href="/security-center/cloudforce-one/#analyze-threat-events">Threat Events indicators</a> into active defense. With this update, users can instantly generate a WAF rule that matches the dynamic list of IP addresses returned by any of their <strong>Saved Views</strong>.</p>
<h4 id="2026-06-08-create-waf-rules-from-threat-events-why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is immediately actionable. Previously, blocking threat actors required manually extracting indicators from threat events and copying them into your firewall rules.
This new integration bridges the gap between threat discovery and threat mitigation:</p>
<ul>
<li>When you identify an active threat pattern - such as an ongoing campaign targeting a specific industry, or using a known indicator type - you can pivot from investigation to mitigation in a single click.</li>
<li>Instead of writing complex, static IP rules, this functionality allows you to leverage the specific filtering logic you have already defined and saved within your Threat Events ecosystem.</li>
<li>Automating the generation of the WAF rule expression from your threat views eliminates manual copying errors, ensuring that the right malicious infrastructure is blocked instantly.</li>
</ul>
<h4 id="2026-06-08-create-waf-rules-from-threat-events-how-to-use-it">How to use it</h4>
<p>You can implement these rules through both the dashboard UI and via the API / Terraform.</p>
<p>Go to <strong>Cloudflare Dashboard</strong> &gt; <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Manage Views</strong>, select your desired view, and select <strong>Create WAF Rule</strong>.</p>
<p>This will automatically pre-populate the <a href="/firewall/cf-dashboard/create-edit-delete-rules/">WAF rule builder</a> with the matching threat event IP indicators.</p>
<p>You can also automate this workflow by utilizing the <a href="/firewall/api/cf-firewall-rules/"><strong>WAF Rule Builder API</strong></a> alongside your <a href="/firewall/api/cf-firewall-rules/">Threat Events saved views endpoints</a>.</p>


<h2 id="introducing-threat-actor-profiles-in-threat-events"><a href="/changelog/post/2026-06-08-threat-actor-profiles/">Introducing Threat Actor Profiles in Threat Events</a></h2>
<p><em>2026-06-08</em></p>
<p><strong>TL;DR:</strong> We’ve launched <strong>Threat Actor Profiles</strong> directly inside the Threat Events dashboard. You can now immediately pivot from a generic alert or blocked event to a profile that unmasks the &quot;Who, Why, and How&quot; behind a threat event.</p>
<h4 id="2026-06-08-threat-actor-profiles-why-this-matters">Why this matters</h4>
Security teams often suffer from a visibility gap. When an attack is blocked, it's difficult to know if it was a random automated bot or a sophisticated advanced persistent threat (APT) campaign specifically targeting your industry. Finding out usually means leaving your security dashboard to hunt through external OSINT feeds or static, out-of-date threat reports.
Threat Actor Profiles solve this by sharing Cloudforce One’s deep adversary research directly inside your workflow:
* Cloudflare sees the traffic in real-time across approximately 20% of the web. This means actor profiles display active malicious infrastructure the moment it touches our global edge.
* Every profile provides clear strategic and tactical modules including alternative aliases, origin tracking, historical threat event volume, and MITRE ATT&CK mapping detailing the adversary's technical methods.
* You can search the dedicated threat actor directory or click an actor's name inside any threat event to view all details and related events to the specific threat actor.
<h4 id="2026-06-08-threat-actor-profiles-how-to-use-it">How to use it</h4>
Adversary tracking is now available in the Cloudflare Dashbboard and ready to be included in your daily investigation workflow:
* Click on the **Threat Actor** name in the Threat Events table to open their full identity profile and review their aliases and attack stats.
* Navigate to **Cloudflare Dashboard > Application Security > Threat Intelligence** to explore the new **Threat Actors** tab. Here, you can browse a card-based directory of all established entities tracked by Cloudforce One.
<p>Learn more in the <a href="https://developers.cloudflare.com/security-center/cloudforce-one/#identify-the-adversary">Cloudforce One documentation</a>.</p>


<h2 id="security-scans-more-frequent"><a href="/changelog/post/2026-05-29-security-insights-default-scans/">Security scans more frequent</a></h2>
<p><em>2026-05-29</em></p>
<p>Security Insights scans now run more often. Cloudflare scans Free accounts <strong>every 7 days</strong>, Pro and Business accounts <strong>every 3 days</strong>, and Enterprise accounts <strong>daily</strong>.</p>
<p>In addition, all accounts and zones now receive scans by default. You no longer need to enable scans before Cloudflare checks your account for misconfigurations, vulnerabilities, and other security risks.</p>
<p>Granular on-demand scans are now available on any plan. You can trigger an on-demand scan for any zone, insight, insight type from the Cloudflare dashboard in order to quickly re-check your security posture after remediating an issue.</p>
<p>To learn more, refer to the <a href="/security/security-insights/">Security Insights documentation</a>.</p>


<h2 id="cloudflare-tunnel-now-runs-connectivity-pre-checks-at-startup"><a href="/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/">Cloudflare Tunnel now runs connectivity pre-checks at startup</a></h2>
<p><em>2026-05-27</em></p>
<p>Starting with <a href="https://github.com/cloudflare/cloudflared/releases"><code>cloudflared</code> version 2026.5.2</a>, <a href="/tunnel/">Cloudflare Tunnel</a> automates the entire <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">connectivity pre-checks workflow</a> directly inside the binary. Previously, customers had to install <code>dig</code> and <code>netcat</code> and run those commands by hand to verify their environment. Now <code>cloudflared</code> does it natively at startup — and surfaces actionable remediation when something is blocked.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/cloudflared-connectivity-prechecks.gif" alt="cloudflared connectivity pre-checks output" /></p>
<p>On every <code>cloudflared tunnel run</code> (and <code>cloudflared tunnel diag</code>), the binary now natively checks:</p>
<ul>
<li><strong>DNS resolution</strong> — <code>region1.v2.argotunnel.com</code> and <code>region2.v2.argotunnel.com</code> resolve to valid Cloudflare IPs.</li>
<li><strong>Transport connectivity</strong> — outbound <code>UDP (QUIC)</code> and <code>TCP (HTTP/2)</code> on port <code>7844</code>.</li>
<li><strong>Management API</strong> — outbound <code>TCP/443</code> to <code>api.cloudflare.com</code> for software updates.</li>
</ul>
<p>Results are printed in a scannable CLI table with three states:</p>
<ul>
<li>✅ <strong>Pass</strong> — the check succeeded.</li>
<li>⚠️ <strong>Warn</strong> — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.</li>
<li>❌ <strong>Fail</strong> — a blocking issue, with a specific remediation hint (for example, <code>Allow outbound UDP on port 7844</code>).</li>
</ul>
<p>If DNS is unresolvable, or <strong>both</strong> UDP and TCP fail on port 7844, <code>cloudflared</code> exits early with the failure rather than looping on opaque <code>failed to dial</code> errors.</p>
<p>Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.</p>
<p>To get the new behavior, upgrade <code>cloudflared</code> to version <code>2026.5.2</code> or later. For more details, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">Connectivity pre-checks documentation</a>.</p>


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


<h2 id="waf-release-2026-05-20"><a href="/changelog/post/2026-05-20-waf-release/">WAF Release - 2026-05-20</a></h2>
<p><em>2026-05-20</em></p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<p><strong>Continuous Rule Improvements</strong></p>
<p>We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="bcdcec3ea63a480896513dc39e9c068d">9e9c068d</code>
</td>
<td>N/A</td>
<td>Sitecore - Cache Poisoning - CVE:CVE-2025-53693 Beta</td>
<td>N/A</td>
<td>Block</td>
<td>
				This rule is merged into the original rule "Sitecore - Cache Poisoning - CVE:CVE-2025-53693" (ID:{" "}
				<code class="nb-rule-id" title="d1bd7563e6254db48ce703807c5b669c">7c5b669c</code>).
</td>
</tr>
</tbody>
</table>


<h2 id="waf-release-2026-05-15-emergency"><a href="/changelog/post/2026-05-15-emergency-waf-release/">WAF Release - 2026-05-15 - Emergency</a></h2>
<p><em>2026-05-15</em></p>
<p>This emergency release introduces two new rules to detect nginx heap buffer overflow and heap spray exploitation attempts targeting the rewrite module's <code>is_args</code> stale-state bug (CVE-2026-42945).</p>
<p><strong>Key Findings</strong></p>
<p>CVE-2026-42945: nginx Heap Buffer Overflow via Stale <code>is_args</code> in Rewrite Module</p>
<p>Successful exploitation allows remote attackers to trigger a heap buffer overflow in nginx's rewrite module by sending crafted URIs containing escapable characters. A length/copy pass mismatch in <code>ngx_http_script_copy_capture_code()</code> causes the copy pass to write escaped data into an undersized buffer, leading to heap corruption. This enables denial of service (worker process crash) and, with heap feng shui techniques, potential remote code execution.</p>
<p>We strongly recommend upgrading to nginx 1.30.1 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, avoid <code>rewrite</code> directives with <code>?</code> in the replacement string followed by <code>set</code> or <code>if</code> referencing capture groups.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2013e3e58efe4b79a26e214f7e52be73">7e52be73</code>
</td>
<td>N/A</td>
<td>nginx - Remote Code Execution - Buffer Overread - CVE:CVE-2026-42945</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="68226e83a4d14ee9a9c878469df0ee6c">9df0ee6c</code>
</td>
<td>N/A</td>
<td>nginx - Remote Code Execution - Heap Spray - CVE:CVE-2026-42945</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>


<h2 id="agent-readiness-scores-now-available-in-url-scanner-via-the-cloudflare-dashboard"><a href="/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/">Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard</a></h2>
<p><em>2026-05-12</em></p>
<p>We’ve added a new <strong>Agent Readiness</strong> tab to URL Scanner reports accessible via the Cloudflare dashboard. This feature evaluates your site against emerging AI standards and provides six specialized scores to help you optimize for the next generation of AI agents and automated discovery.</p>
<p>The Internet is shifting from a human-read web to a machine-read web. AI agents now browse, interact with, and even perform transactions on websites. If a site isn't &quot;agent-ready,&quot; these bots may consume excessive bandwidth, fail to find critical information, or be unable to navigate your services efficiently.</p>
<p>This update provides material value by breaking down readiness into six actionable categories:</p>
<ul>
<li><strong>Basic Web Presence</strong></li>
<li><strong>Discoverability</strong></li>
<li><strong>Content Accessibility</strong></li>
<li><strong>Bot Access Control</strong></li>
<li><strong>Protocol Discovery</strong></li>
<li><strong>Commerce</strong></li>
</ul>
<h4 id="2026-05-12-URL-scanner-report-agent-readiness-accessing-the-report">Accessing the report</h4>
<p>You can view these scores for any scanned URL directly in the dashboard or via our API.</p>
<ul>
<li><strong>Dashboard:</strong> Go to <strong>Protect &amp; Connect &gt; Application Security &gt; Investigate</strong>. After running a scan, select the <strong>Agent Readiness</strong> tab in the report.</li>
<li><strong>API:</strong> Use the <a href="https://developers.cloudflare.com/radar/investigate/url-scanner/">URL Scanner API</a> to programmatically retrieve these scores for your infrastructure.</li>
</ul>
<p>To learn more about the methodology behind these scores, refer to the <a href="https://blog.cloudflare.com/agent-readiness/">blogpost</a>.</p>


<h2 id="waf-release-2026-05-11"><a href="/changelog/post/2026-05-11-waf-release/">WAF Release - 2026-05-11</a></h2>
<p><em>2026-05-11</em></p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<p><strong>Continuous Rule Improvements</strong></p>
<p>We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="23ac4a9e53f94467ba470c9468b3c389">68b3c389</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Java Deserialization - Body - Beta</td>
<td>Block</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Remote Code Execution - Java Deserialization" (ID:{" "}
				<code class="nb-rule-id" title="36b0532eb3c941449afed2d3744305c4">744305c4</code>).
</td>
</tr>
</tbody>
</table>


<h2 id="waf-and-framework-adapter-mitigations-for-react-and-next-js-vulnerabilities"><a href="/changelog/post/2026-05-06-react-nextjs-vulnerabilities/">WAF and framework adapter mitigations for React and Next.js vulnerabilities</a></h2>
<p><em>2026-05-07 12:00:00 UTC</em></p>
<p>Multiple security vulnerabilities were disclosed by the React team and Vercel affecting React Server Components and Next.js. These include denial of service, middleware and proxy bypass, server-side request forgery, cross-site scripting, and cache poisoning issues across a range of severity levels.</p>
<p><strong>We strongly recommend updating your application and its dependencies immediately.</strong> Patched versions are available for React (<code>react-server-dom-webpack</code>, <code>react-server-dom-parcel</code>, and <code>react-server-dom-turbopack</code> <code>19.0.6</code>, <code>19.1.7</code>, and <code>19.2.6</code>) and Next.js (<code>15.5.16</code> and <code>16.2.5</code>).</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-waf-protections">WAF protections</h4>
<p>Cloudflare WAF rules deployed in response to prior React Server Component CVEs (<a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a> and <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a>) already provide coverage for the newly disclosed denial-of-service vulnerabilities. These rules are enabled by default with a Block action for all customers using the Cloudflare Managed Ruleset, including Free plan customers using the Free Managed Ruleset.</p>
<table>
<thead>
<tr>
<th>Ruleset</th>
<th>Rule description</th>
<th>Rule ID</th>
<th>Default action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a></td>
<td><code>2694f1610c0b471393b21aef102ec699</code></td>
<td>Block</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a></td>
<td><code>aaede80b4d414dc89c443cea61680354</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>The existing rules detect the underlying attack patterns generically. As a result, they apply to the new <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> denial-of-service vulnerability in Server Components and the corresponding Next.js advisory <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>.</p>
<p>Cloudflare is investigating whether WAF rules can be safely and effectively deployed for three of the high-severity advisories: <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>, <a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a>, and <a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a>. If it is possible to create a managed WAF rule that mitigates these CVEs and does not potentially break application behavior, Cloudflare will add additional managed WAF rules. These rules will be announced through the <a href="/waf/change-log/changelog/">WAF changelog</a>. Because these vulnerabilities were shared with Cloudflare with minimal advance notice, we are still investigating what WAF mitigations are possible.</p>
<p>Several of the disclosed vulnerabilities are not possible to block in WAF. We strongly recommend updating your applications so they are not purely reliant on WAF mitigations.</p>
<p>Customers on Pro, Business, or Enterprise plans should ensure that <a href="/waf/get-started/#1-deploy-the-cloudflare-managed-ruleset">Managed Rules are enabled</a>.</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-next-js-adapters">Next.js adapters</h4>
<p><strong>Vinext:</strong> <a href="https://github.com/cloudflare/vinext">Vinext</a> is a Vite plugin that reimplements the Next.js API surface. Vinext's latest release is not vulnerable to any of the disclosed CVEs. Vinext's architecture differs from stock Next.js in ways that sidestep the affected code paths. For example, it does not implement the PPR resume protocol, does not expose Pages Router data-route endpoints, and strips internal headers such as <code>x-nextjs-data</code> at request boundaries. As an extra layer of defense, we added a React <code>19.2.6</code> or later requirement when running <code>vinext init</code> (<a href="https://github.com/cloudflare/vinext/pull/1118">PR #1118</a>, <a href="https://github.com/cloudflare/vinext/pull/1112">PR #1112</a>) to prevent accidentally running a vulnerable version of React with Vinext.</p>
<p><strong>OpenNext on Cloudflare:</strong> OpenNext is an adapter that lets you deploy Next.js apps to the Cloudflare Workers platform. OpenNext itself is not directly vulnerable to the React denial-of-service CVE, but users must update the Next.js version in their application. The OpenNext team has updated the adapter to further harden against these vectors and released a new version of the Cloudflare adapter. Test fixtures and examples have been updated to use patched versions (<a href="https://github.com/opennextjs/opennextjs-cloudflare/pull/1255">PR #1255</a>).</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-summary-of-disclosed-vulnerabilities">Summary of disclosed vulnerabilities</h4>
<table>
<thead>
<tr>
<th>Advisory</th>
<th>Severity</th>
<th>Issue</th>
<th>WAF status</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a></td>
<td>High</td>
<td>Denial of service in Server Components</td>
<td><strong>WAF rules in place:</strong> <code>2694f1610c0b471393b21aef102ec699</code>, <code>aaede80b4d414dc89c443cea61680354</code><br/>Cloudflare is investigating additional managed WAF coverage</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a></td>
<td>High</td>
<td>Middleware bypass via segment-prefetch routes</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a></td>
<td>High</td>
<td>Denial of service via connection exhaustion in Cache Components</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv"><code>GHSA-492v-c6pp-mqqv</code></a></td>
<td>High</td>
<td>Middleware bypass via dynamic route parameter injection</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r"><code>GHSA-c4j6-fc7j-m34r</code></a></td>
<td>High</td>
<td>SSRF via WebSocket upgrades</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5"><code>GHSA-36qx-fr4f-26g5</code></a></td>
<td>High</td>
<td>Middleware bypass in Pages Router i18n</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q"><code>GHSA-ffhc-5mcf-pf4q</code></a></td>
<td>Moderate</td>
<td>XSS via CSP nonces</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h"><code>GHSA-gx5p-jg67-6x7h</code></a></td>
<td>Moderate</td>
<td>XSS in <code>beforeInteractive</code> scripts</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh"><code>GHSA-h64f-5h5j-jqjh</code></a></td>
<td>Moderate</td>
<td>Denial of service in Image Optimization API</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7"><code>GHSA-wfc6-r584-vfw7</code></a></td>
<td>Moderate</td>
<td>Cache poisoning in RSC responses</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949"><code>GHSA-vfv6-92ff-j949</code></a></td>
<td>Low</td>
<td>Cache poisoning via RSC cache-busting collisions</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq"><code>GHSA-3g8h-86w9-wvmq</code></a></td>
<td>Low</td>
<td>Middleware redirect cache poisoning</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
</tbody>
</table>


<h2 id="csv-export-and-adjustable-page-density-for-rfis"><a href="/changelog/post/2026-05-07-CSV-export-for-RFIs/">CSV export and adjustable page density for RFIs</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now export your Requests for Information (RFI) history to a <strong>CSV document</strong> and customize your dashboard view by choosing how many RFI records to load per page.</p>
<h4 id="2026-05-07-CSV-export-for-RFIs-why-this-matters">Why this matters</h4>
These quality-of-life updates focus on data portability and dashboard performance, allowing power users to manage high volumes of requests more efficiently:
<ul>
<li>The new <strong>CSV export</strong> allows you to move RFI data into external tools for custom reporting, internal auditing, or cross-referencing with other security projects without manual data entry</li>
<li>With <strong>adjustable page density</strong>, you can now choose to load more records at once (10, 25 or 50) to scan through history faster</li>
</ul>
<p>Cloudforce One subscribers can find these new options in <a href="https://dash.cloudflare.com/?to=/:account/application-security/threat-intelligence/requests">Cloudflare Dashboard &gt; Application Security &gt; Threat Intelligence &gt; Requests for Information</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/application-security/">Previous</a><span>Page 2 of 9</span><a class="pagination-next" rel="next" href="/changelog/product-group/application-security/3/">Next</a></nav>
