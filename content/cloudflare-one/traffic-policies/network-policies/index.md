<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6426.md")
</aside>
<p>Network policies control TCP and UDP traffic between your users and network destinations. Use them to allow or block non-HTTP traffic such as SSH, RDP, and database connections based on IP addresses, ports, and protocols.</p>
<p>Because Cloudflare One <a href="/cloudflare-one/integrations/identity-providers/">integrates with your identity provider</a>, you can also create identity-based network policies. This allows you to control access to non-HTTP resources on a per-user basis regardless of the user's location or device.</p>
<p>A network policy consists of an <strong>Action</strong> and a logical expression that determines the scope of the action. To build an expression, choose a <strong>Selector</strong> and an <strong>Operator</strong>, then enter a value or range of values in the <strong>Value</strong> field. You can use <strong>And</strong> and <strong>Or</strong> logical operators to evaluate multiple conditions.</p>
<ul>
<li><a href="#actions">Actions</a></li>
<li><a href="#selectors">Selectors</a></li>
<li><a href="#comparison-operators">Comparison operators</a></li>
<li><a href="#value">Value</a></li>
<li><a href="#logical-operators">Logical operators</a></li>
</ul>
<p>If a condition in an expression joins a query attribute (such as <em>Source IP</em>) and a response attribute (such as <em>Resolved IP</em>), then the condition will be evaluated when the response is received.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="terraform-provider-v4-precedence-limitation">Terraform provider v4 precedence limitation</h3>
@markup("md", "content/.markup/bodies/6425.md")
</aside>
<h2 id="actions">Actions</h2>
<p>Like actions in DNS and HTTP policies, actions in network policies define which decision you want to apply to a given set of elements. You can assign one action per policy.</p>
<h3 id="allow">Allow</h3>
<p>API value: <code>allow</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6427.md")
</div></details>
<p>Policies with Allow actions allow network traffic to reach certain IPs or ports. In a default-block configuration, Allow policies define the exceptions — traffic that does not match an Allow policy will be blocked by a lower-priority catch-all Block policy. For example, the following configuration allows specific users to reach a given IP address:</p>
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
<td>Destination IP</td>
<td>in</td>
<td><code>92.100.02.102</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>Email</td>
<td>in</td>
<td><code>*@example.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="block">Block</h3>
<p>API value: <code>block</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6428.md")
</div></details>
<p>Policies with Block actions block network traffic from reaching certain IPs or ports. For example, the following configuration blocks all traffic directed to port 443:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination Port</td>
<td>in</td>
<td><code>443</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<h4 id="cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</h4>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6429.md")
</div></details>
<p>Turn on <p><strong>Display block notification for Cloudflare One Client</strong></p>
to display notifications for Gateway block events. Blocked users will receive an operating system notification from the Cloudflare One Client with a custom message you set. If you do not set a custom message, the Cloudflare One Client will display a default message. Custom messages must be 100 characters or less. The Cloudflare One Client will only display one notification per minute.</p>
<p>Upon selecting the notification, the Cloudflare One Client will direct your users to the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">Gateway block page</a> you have configured. Optionally, you can direct users to a custom URL, such as an internal support form.</p>
<p>When you turn on <strong>Send policy context</strong>, Gateway will append details of the matching request to the redirected URL as a query string. Not every context field will be included. Potential policy context fields include:</p>
<details class="nb-details"><summary>Policy context fields</summary><div class="nb-details-body">
@input("content/.markup/bodies/6430.md")
</div></details>
<div class="nb-data-component" data-cf-component="Render"></div>
<h3 id="network-override">Network Override</h3>
<p>API value: <code>l4_override</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6431.md")
</div></details>
<p>Policies with Network Override actions override traffic directed to or coming from certain IPv4/IPv6 addresses or ports. Destination IPs can be public IPs or private IPs connected to your Zero Trust network. For example, the following configuration overrides traffic sent to a public IP with a private IP based on a user's identity:</p>
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
<td>Destination IP</td>
<td>in</td>
<td><code>95.92.143.151</code></td>
<td>And</td>
<td>Network Override</td>
</tr>
<tr>
<td>User Email</td>
<td>in</td>
<td><code>*@example.com</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Override IP</td>
<td></td>
<td><code>10.0.0.1</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6424.md")
</aside>
<p>Gateway will only log successful override connections in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/#network-logs">network logs</a>.</p>
<h2 id="selectors">Selectors</h2>
<p>Gateway matches network traffic against the following selectors, or criteria.</p>
<h3 id="access-infrastructure-target">Access Infrastructure Target</h3>
<p>All <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target">targets</a> secured by an <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access infrastructure application</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access Infrastructure Target</td>
<td><code>access.target</code></td>
</tr>
</tbody>
</table>
<h3 id="access-private-app">Access Private App</h3>
<p>All destination IPs and hostnames secured by an <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access self-hosted private application</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Self-hosted Access App with Private Address</td>
<td><code>access.private_app</code></td>
</tr>
</tbody>
</table>
<h3 id="application">Application</h3>
<p>You can apply network policies to a growing list of popular web applications. Refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Application and app types</a> for more information.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Application</td>
<td><code>any(app.ids[*] in {505})</code></td>
</tr>
</tbody>
</table>
<h3 id="browser-isolation">Browser Isolation <span class="nb-badge">Beta</span></h3>
<p>Whether the current session is running inside <a href="/cloudflare-one/remote-browser-isolation/">Remote Browser Isolation</a>. Use this selector to apply different policy behavior to isolated and non-isolated traffic.</p>
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
<h3 id="content-categories">Content Categories</h3>
<p>Applications within a specific <a href="/cloudflare-one/traffic-policies/domain-categories/#content-categories">security category</a> as categorized by <a href="/radar/glossary/#content-categories">Cloudflare Radar</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content Categories</td>
<td><code>any(net.fqdn.content_category[*] in {1})</code></td>
</tr>
</tbody>
</table>
<h3 id="destination-continent">Destination Continent</h3>
<p>The continent where the request is destined. Geolocation is determined from the target IP address. To specify a continent, enter its two-letter code into the <strong>Value</strong> field:</p>
<table>
<thead>
<tr>
<th>Continent</th>
<th>Code</th>
</tr>
</thead>
<tbody>
<tr>
<td>Africa</td>
<td><code>AF</code></td>
</tr>
<tr>
<td>Antarctica</td>
<td><code>AN</code></td>
</tr>
<tr>
<td>Asia</td>
<td><code>AS</code></td>
</tr>
<tr>
<td>Europe</td>
<td><code>EU</code></td>
</tr>
<tr>
<td>North America</td>
<td><code>NA</code></td>
</tr>
<tr>
<td>Oceania</td>
<td><code>OC</code></td>
</tr>
<tr>
<td>South America</td>
<td><code>SA</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination Continent IP Geolocation</td>
<td><code>net.dst.geo.continent == &quot;EU&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="destination-country">Destination Country</h3>
<p>The country that the request is destined for. Geolocation is determined from the target IP address. To specify a country, enter its <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2 code</a> in the <strong>Value</strong> field.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination Country IP Geolocation</td>
<td><code>net.dst.geo.country == &quot;RU&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="destination-ip">Destination IP</h3>
<p>The IP address of the request's target.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination IP</td>
<td><code>any(net.dst.ip[*] in {10.0.0.0/8})</code></td>
</tr>
</tbody>
</table>
<h3 id="destination-port">Destination Port</h3>
<p>The port number of the request's target.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination Port</td>
<td><code>net.dst.port == 2222</code></td>
</tr>
</tbody>
</table>
<h3 id="detected-protocol">Detected Protocol</h3>
<p>The inferred network protocol based on Cloudflare's <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">protocol detection</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Detected Protocol</td>
<td><code>net.protocol.detection == &quot;ssh&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="device-posture">Device Posture</h3>
<p>With the Device Posture selector, admins can use signals from end-user devices to secure access to their internal and external resources. For example, a security admin can choose to limit all access to internal applications based on whether specific software is installed on a device and/or if the device or software are configured in a particular way.</p>
<p>For more information on device posture checks, refer to <a href="/cloudflare-one/reusable-components/posture-checks/">Device posture</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Passed Device Posture Checks</td>
<td><code>any(device_posture.checks.failed[*] in {&quot;1308749e-fcfb-4ebc-b051-fe022b632644&quot;})</code>, <code>any(device_posture.checks.passed[*] in {&quot;1308749e-fcfb-4ebc-b051-fe022b632644&quot;})&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="protocol">Protocol</h3>
<p>The protocol used to send the packet.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Protocol</td>
<td><code>net.protocol == &quot;tcp&quot;</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6423.md")
</aside>
<h3 id="proxy-endpoint">Proxy Endpoint</h3>
<p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy server</a> where your browser forwards HTTP traffic.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Proxy Endpoint</td>
<td><code>proxy.endpoint == &quot;3ele0ss56t.proxy.cloudflare-gateway.com&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="security-categories">Security Categories</h3>
<p>Applications within a specific <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security category</a> as categorized by <a href="/radar/glossary/#content-categories">Cloudflare Radar</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Categories</td>
<td><code>any(net.fqdn.security_category[*] in {1})</code></td>
</tr>
</tbody>
</table>
<h3 id="sni">SNI</h3>
<p>Server Name Indication (SNI) is the hostname a client sends during the TLS handshake, before encryption begins. Gateway reads the SNI to identify the destination of encrypted traffic. The SNI selector matches the exact hostname.</p>
<p>By default, SNI selectors only apply to HTTPS traffic on port <code>443</code>. To inspect traffic on every port, turn on <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">protocol detection</a> and choose to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">inspect on all ports</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>SNI</td>
<td><code>net.sni.host == &quot;www.example.com&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="sni-domain">SNI Domain</h3>
<p>The domain whose Server Name Indication (SNI) header Gateway will filter traffic against. For example, a rule for <code>example.com</code> will match <code>example.com</code>, <code>www.example.com</code>, and <code>my.test.example.com</code>.</p>
<p>By default, SNI selectors only apply to HTTPS traffic on port <code>443</code>. To inspect traffic on every port, turn on <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">protocol detection</a> and choose to <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/#inspect-on-all-ports">inspect on all ports</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>SNI Domain</td>
<td><code>net.sni.domains == &quot;example.com&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="source-continent">Source Continent</h3>
<p>The continent of the user making the request.</p>
<p>Geolocation is determined from the device's public IP address (typically assigned by the user's ISP). To specify a continent, enter its two-letter code into the <strong>Value</strong> field:</p>
<table>
<thead>
<tr>
<th>Continent</th>
<th>Code</th>
</tr>
</thead>
<tbody>
<tr>
<td>Africa</td>
<td><code>AF</code></td>
</tr>
<tr>
<td>Antarctica</td>
<td><code>AN</code></td>
</tr>
<tr>
<td>Asia</td>
<td><code>AS</code></td>
</tr>
<tr>
<td>Europe</td>
<td><code>EU</code></td>
</tr>
<tr>
<td>North America</td>
<td><code>NA</code></td>
</tr>
<tr>
<td>Oceania</td>
<td><code>OC</code></td>
</tr>
<tr>
<td>South America</td>
<td><code>SA</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Continent IP Geolocation</td>
<td><code>net.src.geo.continent == &quot;North America&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="source-country">Source Country</h3>
<p>The country of the user making the request.</p>
<p>Geolocation is determined from the device's public IP address (typically assigned by the user's ISP). To specify a country, enter its <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha-2 code</a> in the <strong>Value</strong> field.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Country IP Geolocation</td>
<td><code>net.src.geo.country == &quot;RU&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="source-internal-ip">Source Internal IP</h3>
<p>Use this selector to apply network policies to a private IP address, assigned by a user's local network, that requests arrive to Gateway from.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Internal IP</td>
<td><code>net.src.internal_src_ip == &quot;192.168.86.0/27&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="source-ip">Source IP</h3>
<p>The originating IP address or addresses of a device proxied by Gateway.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source IP</td>
<td><code>net.src.ip[*] in {10.0.0.0/8}</code></td>
</tr>
</tbody>
</table>
<h3 id="source-port">Source Port</h3>
<p>The originating port of a device proxied by Gateway.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Port</td>
<td><code>net.src.port == &quot;2222&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="traffic-source">Traffic Source <span class="nb-badge">Beta</span></h3>
<p>The method used to on-ramp traffic to Cloudflare. Use this selector to apply policies based on how traffic reaches Gateway.</p>
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
<p>Available values: <code>device_client</code> (Device client), <code>mesh</code> (Mesh), <code>cloudflare_wan</code> (Cloudflare WAN), <code>clientless_rdp</code> (Clientless RDP), <code>proxy_endpoint</code> (Proxy endpoint), <code>agentless_biso</code> (Clientless Browser Isolation), <code>mcp_portal</code> (MCP portal).</p>
<h3 id="users">Users</h3>
<p>Use these selectors to match against identity attributes.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Email</td>
<td><code>identity.email == &quot;user@example.com&quot;</code></td>
</tr>
<tr>
<td>User Name</td>
<td><code>identity.name == &quot;Test User&quot;</code></td>
</tr>
<tr>
<td>User Group IDs</td>
<td><code>any(identity.groups[*].id in {&quot;group_id&quot;})</code></td>
</tr>
<tr>
<td>User Group Names</td>
<td><code>any(identity.groups[*].name in {&quot;group_name&quot;})</code></td>
</tr>
<tr>
<td>User Group Emails</td>
<td><code>any(identity.groups[*].email in {&quot;group@example.com&quot;})</code></td>
</tr>
<tr>
<td>SAML Attributes</td>
<td><code>any(identity.saml_attributes[&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name&quot;] in {&quot;Test User&quot;})</code></td>
</tr>
</tbody>
</table>
<h3 id="virtual-network">Virtual Network</h3>
<p>Use this selector to match all traffic routed through a specific <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual Network</a> via the Cloudflare One Client.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Virtual Network</td>
<td><code>net.vnet_id == &quot;957fc748-591a-e96s-a15d-1j90204a7923&quot;</code></td>
</tr>
</tbody>
</table>
<h2 id="comparison-operators">Comparison operators</h2>
<p>Comparison operators are the way Gateway matches traffic to a selector. When you choose a <strong>Selector</strong> in the dashboard policy builder, the <strong>Operator</strong> dropdown menu will display the available options for that selector.</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>is</td>
<td>equals the defined value</td>
</tr>
<tr>
<td>is not</td>
<td>does not equal the defined value</td>
</tr>
<tr>
<td>in</td>
<td>matches at least one of the defined values</td>
</tr>
<tr>
<td>not in</td>
<td>does not match any of the defined values</td>
</tr>
<tr>
<td>in list</td>
<td>in a pre-defined <a href="/cloudflare-one/reusable-components/lists/">list</a> of values</td>
</tr>
<tr>
<td>not in list</td>
<td>not in a pre-defined <a href="/cloudflare-one/reusable-components/lists/">list</a> of values</td>
</tr>
<tr>
<td>matches regex</td>
<td>regex evaluates to true</td>
</tr>
<tr>
<td>does not match regex</td>
<td>regex evaluates to false</td>
</tr>
<tr>
<td>greater than</td>
<td>exceeds the defined number</td>
</tr>
<tr>
<td>greater than or equal to</td>
<td>exceeds or equals the defined number</td>
</tr>
<tr>
<td>less than</td>
<td>below the defined number</td>
</tr>
<tr>
<td>less than or equal to</td>
<td>below or equals the defined number</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6422.md")
</aside>
<h2 id="value">Value</h2>
<p>In the <strong>Value</strong> field, you can input a single value when using an equality comparison operator (such as <em>is</em>) or multiple values when using a containment comparison operator (such as <em>in</em>). Additionally, you can use <a href="#regular-expressions">regular expressions</a> (or regex) to specify a range of values for supported selectors.</p>
<h3 id="regular-expressions">Regular expressions</h3>
<p>Regular expressions are evaluated using Rust. The Rust implementation is slightly different than regex libraries used elsewhere. For more information, refer to our guide for <a href="/cloudflare-one/access-controls/policies/app-paths/#wildcards">Wildcards</a>. To evaluate if your regex matches, you can use <a href="https://rustexp.lpil.uk/">Rustexp</a>.</p>
<p>If you want to match multiple values, you can use the pipe symbol (<code>|</code>) as an OR operator. You do not need to use an escape character (<code>\</code>) before the pipe symbol. For example, the following expression evaluates to true when the SNI host matches either <code>.*whispersystems.org</code> or <code>.*signal.org</code>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>SNI</td>
<td>matches regex</td>
<td><code>.*whispersystems.org|.*signal.org</code></td>
</tr>
</tbody>
</table>
<p>In addition to regular expressions, you can use <a href="#logical-operators">logical operators</a> to match multiple values.</p>
<h2 id="logical-operators">Logical operators</h2>
<p>To evaluate multiple conditions in an expression, select the <strong>And</strong> logical operator. These expressions can be compared further with the <strong>Or</strong> logical operator.</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>And</td>
<td>match all of the conditions in the expression</td>
</tr>
<tr>
<td>Or</td>
<td>match any of the conditions in the expression</td>
</tr>
</tbody>
</table>
<p>The <strong>Or</strong> operator will only work with conditions in the same expression group. For example, you cannot compare conditions in <strong>Traffic</strong> with conditions in <p><strong>Identity</strong> or <strong>Device Posture</strong></p>
.</p>
