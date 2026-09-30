<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-one-client-for-linux-version-2026-7-1343-0"><a href="/changelog/post/2026-08-19-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.7.1343.0)</a></h2>
<p><em>2026-08-19</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.</li>
<li>When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Fixed the client not allowing login to another organization when currently showing &quot;Device not in organization.&quot;</li>
<li>A DNS search domain parsing failure no longer prevents connection.</li>
<li>Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.</li>
<li>Fixed missing certificate error display due to a race condition.</li>
<li>Fixed empty black window after transitioning from docked dual displays to undocked/internal display.</li>
<li>Fixed hostname routes not working for Cloudflare Mesh when the IP addresses of the hostnames are local addresses.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.</li>
</ul>
<p>For Zero Trust documentation please see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation please see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>


<h2 id="configure-origin-application-settings-for-cloudflare-tunnel-in-the-dashboard"><a href="/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/">Configure origin application settings for Cloudflare Tunnel in the dashboard</a></h2>
<p><em>2026-08-18</em></p>
<p>You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a <a href="/tunnel/">Cloudflare Tunnel</a>. These settings control how <code>cloudflared</code> connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-origin-settings-dashboard.gif" alt="Configure origin application settings in the Cloudflare dashboard" /></p>
<p>When editing a published application, expand <strong>Additional application settings</strong> to configure parameters organized into three categories:</p>
<ul>
<li><strong>HTTP</strong> — Set a custom HTTP Host header or disable chunked encoding.</li>
<li><strong>TLS</strong> — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.</li>
<li><strong>Connection</strong> — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For the full list of origin parameters, refer to <a href="/tunnel/reference/origin-parameters/">Origin parameters</a>.</p>


<h2 id="post-quantum-key-exchange-for-mx-deployments"><a href="/changelog/post/2026-08-17-post-quantum-key-exchange-mx/">Post-quantum key exchange for MX deployments</a></h2>
<p><em>2026-08-17T09:00:00+00:00</em></p>
<p>Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement.</p>
<p>Inbound MX connections and outbound delivery connections now negotiate the <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a> hybrid key agreement when the peer supports it, protecting SMTP traffic against <a href="https://blog.cloudflare.com/pq-2024/">harvest-now, decrypt-later</a> attacks.</p>
<p>Support is backwards compatible and enabled automatically for all customers. Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.</p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>


<h2 id="load-balancing-analytics-now-filters-by-pool-name"><a href="/changelog/post/2026-08-17-pool-name-analytics-filter/">Load balancing analytics now filters by pool name</a></h2>
<p><em>2026-08-17</em></p>
<p>Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.</p>
<p>Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.</p>
<p>The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:</p>
<ul>
<li><strong>Requests over time</strong>, filtering the chart series to the selected pool.</li>
<li><strong>Pool distribution</strong>, showing only the selected pool segment.</li>
<li><strong>Top endpoints</strong>, displaying cards for origins in the selected pool.</li>
<li><strong>Latency</strong>, showing latency data for the selected pool.</li>
</ul>
<p>The <strong>Logs</strong> view and health event filtering are unchanged.</p>
<p>To use this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same pool filter appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>For more information about analytics filters and metrics, refer to <a href="/load-balancing/reference/load-balancing-analytics/">Load Balancing Analytics</a>.</p>


<h2 id="you-can-now-enable-access-on-a-worker-or-all-workers-at-once"><a href="/changelog/post/2026-08-14-workers-access/">You can now enable Access on a Worker or all Workers at once</a></h2>
<p><em>2026-08-14</em></p>
<p>You now have two new ways to protect your <a href="/workers/">Workers</a> with <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p><strong>Protect an application across all its domains at once</strong></p>
<p>Until now, if a Worker was reachable on a route, a Custom Domain, and a <code>workers.dev</code> URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.</p>
<p>Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-one-worker.png" alt="Access setting for protecting a single Worker" /></p>
<p><strong>Protect all new and existing Workers by default</strong></p>
<p>Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-all-workers.png" alt="Account-wide Access setting that protects all Workers" /></p>
<p>If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.</p>
<p><img src="/assets/upstream/images/changelog/workers/make-worker-public.png" alt="Make a Worker public when all Workers are protected" /></p>
<p>Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.</p>
<p>For more advanced policy options, edit the policy in <a href="https://dash.cloudflare.com/?to=/:account/one/access/apps">Zero Trust</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/choose-who-can-sign-in.png" alt="Access policy configuration for controlling who can sign in" /></p>
<p><strong>View all of your Worker Access policies</strong></p>
<p>You can view and manage all of your Access policies in the <strong>Access</strong> tab of the Workers &amp; Pages section in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/access-policies.png" alt="Access tab showing all configured Access policies" /></p>
<p><strong>See who is accessing your Worker</strong></p>
<p>When Access is enabled on your Worker, every authenticated request includes <code>ctx.access</code>. Call <a href="/workers/runtime-apis/context/#access"><code>ctx.access.getIdentity()</code></a> to get the user's email, name, and groups — no manual JWT validation required.</p>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    if (!ctx.access) {&#10;      return new Response(&quot;Access did not run&quot;, { status: 401 });&#10;    }&#10;&#10;    const identity = await ctx.access.getIdentity();&#10;    return Response.json({ aud: ctx.access.aud, email: identity?.email });&#10;  },&#10;};&#10;</code></pre>
<p><strong>Test Access locally</strong></p>
<p>You can now test Cloudflare Access locally with <code>wrangler dev</code>. Add a <code>dev</code> block to your <code>wrangler.jsonc</code>:</p>
<pre><code class="language-json">{&#10;  &quot;access&quot;: {&#10;    &quot;dev&quot;: {&#10;      &quot;aud&quot;: &quot;my-app&quot;,&#10;      &quot;identity&quot;: { &quot;email&quot;: &quot;admin@example.com&quot; }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Your Worker will receive this identity through <code>ctx.access</code> and <code>ctx.access.getIdentity()</code>, letting you test authenticated and unauthenticated flows without deploying. Remove the <code>dev</code> block to simulate unauthenticated requests.</p>
<p><strong>API and programmatic access</strong></p>
<p>You can also set up these policies through the <a href="/workers/configuration/cloudflare-access/">Workers API</a> instead of the dashboard.</p>


<h2 id="detect-and-control-software-package-downloads-with-package-registry-security"><a href="/changelog/post/2026-08-13-package-protection/">Detect and control software package downloads with package registry security</a></h2>
<p><em>2026-08-13</em></p>
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


<h2 id="block-emails-by-content-with-blocked-content-rules"><a href="/changelog/post/2026-08-12-blocked-content-rules/">Block emails by content with blocked content rules</a></h2>
<p><em>2026-08-12 09:00:00 UTC</em></p>
<p>Cloudflare Email security now lets administrators write their own content-based blocking rules. A new <strong>Blocked content</strong> area under <strong>Policies &amp; rules</strong> lets you define a plaintext string or a regular expression, choose whether to scan the message subject, body, or both, and automatically block any message that matches.</p>
<ul>
<li>Create rules using either <strong>plaintext</strong> matches or <strong>regular expressions</strong> — useful for blocking targeted phishing campaigns, known-bad phrases, or content patterns unique to your organization.</li>
<li>Choose the <strong>search location</strong> for each rule: <strong>subject</strong>, <strong>body</strong>, or <strong>subject and body</strong>.</li>
<li>Use the built-in <strong>regular expression checker</strong> to validate your pattern against sample text before saving, so you can confirm the rule matches what you expect and avoid false positives.</li>
<li>Matching messages are marked with a malicious <a href="/cloudflare-one/email-security/reference/dispositions-and-attributes/">disposition</a> and prevented from reaching users' inboxes.</li>
</ul>
<p>Blocked content rules currently only support the block action.</p>
<p>This feature is available for the following Email security packages:</p>
<ul>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-content/">Blocked content</a>.</p>


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


<h2 id="cloudflare-one-client-for-windows-version-2026-6-905-0"><a href="/changelog/post/2026-08-10-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.905.0)</a></h2>
<p><em>2026-08-11</em></p>
<p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix addresses an uncommon and intermittent case on Windows devices where the device is unable to reconnect after the device is woken from sleep.</p>


<h2 id="stream-live-logs-from-cloudflare-tunnel-in-the-dashboard"><a href="/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/">Stream live logs from Cloudflare Tunnel in the dashboard</a></h2>
<p><em>2026-08-10</em></p>
<p>Real-time Tunnel log streaming is now available in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong>. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-live-logs-core-dashboard.gif" alt="Stream live logs from a tunnel in the Cloudflare dashboard" /></p>
<p>In the tunnel detail view, a new <strong>Live logs</strong> tab lets you:</p>
<ul>
<li><strong>Stream logs from single or multiple connectors</strong> — In <a href="/tunnel/configuration/#replicas-and-high-availability">highly available</a> deployments with multiple <code>cloudflared</code> replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.</li>
<li><strong>Filter by log level, event type, and HTTP method</strong> — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or <code>cloudflared</code> internal), at any log level.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/tunnel/observability/#remote-log-streaming">Tunnel observability</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a>.</p>


<h2 id="load-balancing-health-notifications-now-resolve-automatically"><a href="/changelog/post/2026-08-07-stateful-health-notifications/">Load Balancing health notifications now resolve automatically</a></h2>
<p><em>2026-08-07</em></p>
<p><a href="/load-balancing/">Load Balancing</a> health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.</p>
<p>As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.</p>
<p>This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by <a href="/health-checks/">Health Checks</a> notifications.</p>
<p>Two things to keep in mind:</p>
<ul>
<li>A recovery notification is matched to the earlier unhealthy notification for the <strong>same pool or endpoint</strong>. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.</li>
<li>If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.</li>
</ul>
<p>Refer to <a href="/load-balancing/additional-options/pagerduty-integration/">Integrate with PagerDuty</a> to learn more about routing Load Balancing health notifications to an incident management tool.</p>


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


<h2 id="identity-aware-controls-are-now-available-in-ai-gateway"><a href="/changelog/post/2026-08-05-access-user-id-metadata/">Identity-aware controls are now available in AI Gateway</a></h2>
<p><em>2026-08-05</em></p>
<p>AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:</p>
<ul>
<li><strong>Protect your gateway endpoint.</strong> Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.</li>
<li><strong>Identity-aware controls.</strong> When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.</li>
</ul>
<p>With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as <code>cf.user_id</code>.</p>
<p>For setup instructions, refer to <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>.</p>


<h2 id="control-authorization-cookies-for-multi-domain-access-applications"><a href="/changelog/post/2026-08-03-eager-redirect-cookie-setting/">Control authorization cookies for multi-domain Access applications</a></h2>
<p><em>2026-08-03</em></p>
<p>Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.</p>
<p>Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.</p>
<p>The new <strong>Eager redirect cookie</strong> setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a <code>CF_Authorization</code> cookie. This supports applications that need to make requests across hostnames before the user visits each one.</p>
<p>For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.</p>
<p>To configure the setting, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie">Authorization cookie</a>.</p>


<h2 id="see-fallback-pool-traffic-separately-in-load-balancing-analytics"><a href="/changelog/post/2026-08-03-fallback-pool-analytics/">See fallback pool traffic separately in load balancing analytics</a></h2>
<p><em>2026-08-03</em></p>
<p>Load balancing analytics now shows traffic served by your <a href="/load-balancing/understand-basics/health-details/#fallback-pools">fallback pool</a> separately from traffic routed to the same pool by normal steering.</p>
<p>Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.</p>
<p>Fallback traffic is now labeled with the pool name followed by <code>(Fallback)</code>. A pool named <code>eu-west</code>, for example, is shown as <code>eu-west (Fallback)</code>. This label appears as its own entry in:</p>
<ul>
<li><strong>Requests over time</strong>, as a separate series in the chart.</li>
<li><strong>Pool distribution</strong>, as a separate segment.</li>
<li><strong>Top endpoints</strong>, as a separate card for the pool.</li>
</ul>
<p>The <strong>Latency</strong> view and the health event <strong>Logs</strong> are unchanged.</p>
<p>To see this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same breakdown appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>Refer to <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a> to learn more.</p>


<h2 id="static-oauth-client-credentials-for-mcp-server-portals"><a href="/changelog/post/2026-07-31-mcp-portal-manual-oauth/">Static OAuth client credentials for MCP server portals</a></h2>
<p><em>2026-07-31</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.</p>
<p>When adding an MCP server, administrators can enter the client ID and client secret from an OAuth application registered with the upstream provider. The configuration also supports custom OAuth endpoints, scopes, and the <code>client_secret_post</code> and <code>client_secret_basic</code> token endpoint authentication methods.</p>
<p>Cloudflare stores the client secret encrypted. Users still authenticate to the upstream server with their own accounts when they connect through a portal.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials">Configure manual OAuth credentials</a>.</p>


<h2 id="cloudflare-one-client-for-macos-version-2026-7-1210-1"><a href="/changelog/post/2026-07-31-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.7.1210.1)</a></h2>
<p><em>2026-07-31</em></p>
<p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.</li>
<li>Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.</li>
<li>A <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search domain</a> parsing failure no longer prevents connection.</li>
<li>Fixed a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a> issue where the tunnel could stall while uploading at a high rate.</li>
<li>Fixed being unable to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">switch organizations</a> when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed the Home Screen dropdown popup not anchoring correctly.</li>
<li>Fixed a crash during dialog dismissal.</li>
<li>Increased tolerance for configurations with a large number of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.</li>
<li>Fixed the WARP client stealing window focus (for example, during reauth).</li>
<li>Fixed a client crash when connecting to a captive portal over Wi-Fi.</li>
<li>Fixed the system tray icon showing &quot;disconnected&quot; while the UI showed &quot;connected&quot;.</li>
<li>A successful re-authentication will cause the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> to be re-evaluated.</li>
<li>Improved <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">dashboard-managed client updates</a> by running the updater only when needed.</li>
</ul>


<h2 id="cloudflare-one-client-for-windows-version-2026-7-1210-1"><a href="/changelog/post/2026-07-31-warp-windows-beta/">Cloudflare One Client for Windows (version 2026.7.1210.1)</a></h2>
<p><em>2026-07-31</em></p>
<p>A new Beta release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.</li>
<li>Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.</li>
<li>A <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search domain</a> parsing failure no longer prevents connection.</li>
<li>Fixed a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a> issue where the tunnel could stall while uploading at a high rate.</li>
<li>Fixed being unable to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">switch organizations</a> when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed the Home Screen dropdown popup not anchoring correctly.</li>
<li>Fixed a crash during dialog dismissal.</li>
<li>Increased tolerance for configurations with a large number of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.</li>
<li>Fixed a networking issue where IPv6 multicast routes were being assigned to the WARP tunnel interface.</li>
<li>Fixed fatal errors on UI load on Windows 10.</li>
<li>Fixed a crash during Windows notification initialization.</li>
<li>Made the Windows <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/">domain-joined posture check</a> more reliable.</li>
<li>Fixed orphaned credentials left behind on multi-user uninstall.</li>
<li>A successful re-authentication will cause the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> to be re-evaluated.</li>
<li>Improved <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">dashboard-managed client updates</a> by running the updater only when needed.</li>
</ul>


<h2 id="admins-can-turn-on-code-mode-by-default-for-mcp-portal-users"><a href="/changelog/post/2026-07-30-mcp-portal-code-mode-policies/">Admins can turn on Code Mode by default for MCP portal users</a></h2>
<p><em>2026-07-30</em></p>
<p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> now support four Code Mode policies: <em>Off</em>, <em>Opt-in</em>, <em>On by default</em>, and <em>Enforced</em>. Admins can choose whether Code Mode is unavailable, optional, enabled by default, or required for every session.</p>
<p>Existing portals retain their current behavior. Portals that previously allowed Code Mode use <em>Opt-in</em>, while portals that did not allow Code Mode use <em>Off</em>. New portals also use <em>Opt-in</em> by default.</p>
<p>Clients turn on Code Mode for an <em>Opt-in</em> portal with <code>?codemode=search_and_execute</code>. The <em>On by default</em> policy lets clients opt out with <code>?codemode=off</code>, which avoids nested code execution when a client runs its own Code Mode implementation. The <em>Off</em> and <em>Enforced</em> policies ignore client overrides.</p>
<p>The Cloudflare API exposes these policies through the <code>code_mode</code> field:</p>
<pre><code class="language-json">{&#10;	&quot;code_mode&quot;: &quot;default_on&quot;&#10;}&#10;</code></pre>
<p>The supported values are <code>off</code>, <code>opt_in</code>, <code>default_on</code>, and <code>enforced</code>. The previous <code>allow_code_mode</code> boolean is deprecated.</p>
<p>For configuration details and client behavior, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies">Code Mode policies</a>.</p>


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


<h2 id="cloudflare-one-client-for-linux-version-2026-6-880-0"><a href="/changelog/post/2026-07-21-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.880.0)</a></h2>
<p><em>2026-07-22</em></p>
<p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<h2 id="cloudflare-one-client-for-macos-version-2026-6-880-0"><a href="/changelog/post/2026-07-21-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.6.880.0)</a></h2>
<p><em>2026-07-22</em></p>
<p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/cloudflare-one/">Previous</a><span>Page 2 of 13</span><a class="pagination-next" rel="next" href="/changelog/product-group/cloudflare-one/3/">Next</a></nav>
