<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6616.md")
</aside>
<p>Many third-party services (for example, a bank or partner API) only allow connections from a known list of IP addresses. By default, traffic that exits through Cloudflare Gateway shares a source IP address with all other Cloudflare One Client users, so upstream services cannot identify your organization by IP alone.</p>
<p><a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">Dedicated egress IPs</a> solve this problem. They are static IP addresses assigned only to your account, which you can add to upstream allowlists.</p>
<p>Egress policies control which dedicated egress IP is used for a given connection. You can match traffic on attributes such as user identity, source or destination IP address, and geolocation. Traffic that does not match an egress policy defaults to the most performant dedicated egress IP.</p>
<p>Cloudflare does not publish Cloudflare One Client egress IP ranges. Cloudflare One Client egress IPs are not listed at <a href="https://cloudflare.com/ips">Cloudflare's IP Ranges</a>. To obtain a dedicated Cloudflare One Client egress IP, contact your account team.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="terraform-provider-v4-precedence-limitation">Terraform provider v4 precedence limitation</h3>
@markup("md", "content/.markup/bodies/6615.md")
</aside>
<h2 id="load-balancing">Load balancing</h2>
<p>Traffic that does not match any egress policy exits from the closest Cloudflare data center using a default Gateway egress IP. This applies whether your account uses dedicated egress IPs or the default shared IPs.</p>
<p>If two data centers are equally close to the user, Gateway splits traffic between them. The load balancer keeps each user on the same egress IP regardless of which data center handles the request.</p>
<h2 id="force-ip-version">Force IP version</h2>
<p>Some upstream services only accept connections over a specific IP version. To force all egress traffic to use IPv4 or IPv6 only, first verify you are <a href="/cloudflare-one/traffic-policies/get-started/dns/">filtering DNS traffic</a>, then create a DNS policy to <a href="/cloudflare-one/traffic-policies/dns-policies/common-policies/#control-ip-version">block AAAA or A records</a>.</p>
<h2 id="example-policies">Example policies</h2>
<p>The following egress policy configures all traffic destined for a third-party network to use a static source IP:</p>
<table>
<thead>
<tr>
<th>Policy name</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Egress method</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access third-party provider</td>
<td>Destination IP</td>
<td>is</td>
<td><code>198.51.100.158</code></td>
<td>Dedicated Cloudflare egress IPs</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Primary IPv4 address</th>
<th>IPv6 address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>203.0.113.88</code></td>
<td><code>2001:db8::/32</code></td>
</tr>
</tbody>
</table>
<h3 id="secure-access-to-saas-applications">Secure access to SaaS applications</h3>
<p>Many SaaS providers (for example, Microsoft 365, Salesforce, or Workday) allow you to restrict access to connections from specific IP addresses. You can use dedicated egress IPs with Gateway to enforce this restriction:</p>
<ol>
<li><strong>Obtain dedicated egress IPs</strong> from your account team and note the assigned IPv4 and IPv6 addresses.</li>
<li><strong>Create an egress policy</strong> that routes traffic destined for the SaaS provider through your dedicated egress IP. Use the Destination IP selector with the published IP ranges of the provider. Alternatively, use the Application selector (Beta) to match the provider by name.</li>
<li><strong>Add the egress IPs to the SaaS provider's allowlist</strong> so the provider only accepts connections from your organization's IPs.</li>
<li><strong>Pair with HTTP policies</strong> to add deeper controls. For example, block file uploads to personal accounts, enforce DLP profiles to prevent sensitive data from leaving the organization, or require <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a> before allowing access.</li>
</ol>
<p>This pattern ensures that access to the SaaS application is limited to traffic that passes through Gateway, where your security policies are enforced, and that the SaaS provider can verify traffic originates from your organization.</p>
<h3 id="catch-all-policy">Catch-all policy</h3>
<p>Without a catch-all policy, any traffic that does not match an explicit egress policy will attempt to use the closest dedicated egress IP location. To avoid unexpected IP assignments and maintain the best performance, create a catch-all policy that routes remaining traffic through the default Zero Trust IP range:</p>
<table>
<thead>
<tr>
<th>Policy name</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Egress method</th>
</tr>
</thead>
<tbody>
<tr>
<td>Default egress policy</td>
<td>Protocol</td>
<td>in</td>
<td><code>All options (Protocol)</code></td>
<td>Cloudflare default egress method</td>
</tr>
</tbody>
</table>
<p>Gateway policies evaluate from <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">top to bottom</a> in the UI. Place the catch-all policy at the bottom of the list so that more specific policies are evaluated first.</p>
<h2 id="egress-methods">Egress methods</h2>
<p>When you configure your egress policy, you can choose whether to egress traffic using the default Cloudflare egress method or dedicated egress IPs.</p>
<h3 id="use-default-cloudflare-egress-method">Use default Cloudflare egress method</h3>
<p><strong>Use default Cloudflare egress method</strong> routes traffic through the default source IP range shared across all Zero Trust accounts. Traffic exits from the nearest Cloudflare data center, which provides the best performance.</p>
<h3 id="use-dedicated-egress-ips">Use dedicated egress IPs</h3>
<p><strong>Use dedicated egress IPs (Cloudflare or BYOIP)</strong> routes traffic through the primary IPv4 address and IPv6 range you select in the dropdown menus.
When creating egress policies with dedicated egress IPs, you must set a secondary IPv4 address to ensure traffic resilience. You can set the secondary IPv4 address to <code>0.0.0.0</code> or a specific Cloudflare location different from your primary IPv4 address. If you set the secondary IPv4 address to <code>0.0.0.0</code>, Gateway will route traffic to the location closest to the user. If the physical location of your primary IPv4 address is not available, Gateway will route traffic to either the default Cloudflare egress range or the secondary location specified.</p>
<p>If the data center associated with your primary IPv4 address goes down, Gateway fails over to the secondary data center to prevent traffic drops. A secondary IPv6 address is not required because IPv6 traffic can exit from any Cloudflare data center. You can use IPs provided by Cloudflare or <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">bring your own IP addresses (BYOIP)</a>.</p>
<p>To learn more about IPv4 and IPv6 egress behavior, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#egress-location">Egress locations</a>.</p>
<h2 id="selectors">Selectors</h2>
<p>Selectors are the criteria that Gateway uses to match egress traffic against a policy. Gateway evaluates the following selectors:</p>
<h3 id="application">Application <span class="nb-badge">Beta</span></h3>
<p>You can apply egress policies to a growing list of popular web applications. Refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Application and app types</a> for more information.</p>
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
<p>This selector is only available for traffic onboarded to Traffic and DNS mode, PAC files, or Browser Isolation. For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">Selector prerequisites</a>.</p>
<h3 id="content-categories">Content Categories <span class="nb-badge">Beta</span></h3>
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
<p>This selector is only available for traffic onboarded to Traffic and DNS mode, PAC files, or Browser Isolation. For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">Selector prerequisites</a>.</p>
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
<h3 id="domain">Domain <span class="nb-badge">Beta</span></h3>
<p>Use this selector to match against a domain and all subdomains. For example, you can match <code>example.com</code> and its subdomains, such as <code>www.example.com</code>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td><code>any(net.fqdn.domains[*] == &quot;example.com&quot;)</code></td>
</tr>
</tbody>
</table>
<p>Gateway policies do not support domains with non-Latin characters directly. To use a domain with non-Latin characters, add it to a <a href="/cloudflare-one/reusable-components/lists/">list</a>.</p>
<p>This selector is only available for traffic onboarded to Traffic and DNS mode, PAC files, or Browser Isolation. For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">Selector prerequisites</a>.</p>
<h3 id="host">Host</h3>
<p>Use this selector to match against only the hostname specified. For example, you can match <code>test.example.com</code> but not <code>example.com</code> or <code>www.test.example.com</code>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td><code>net.fqdn.host == &quot;example.com&quot;</code></td>
</tr>
</tbody>
</table>
<p>Gateway policies do not support hostnames with non-Latin characters directly. To use a hostname with non-Latin characters, add it to a <a href="/cloudflare-one/reusable-components/lists/">list</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6614.md")
</aside>
<p>This selector is only available for traffic onboarded to Traffic and DNS mode, PAC files, or Browser Isolation. For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/#selector-prerequisites">Selector prerequisites</a>.</p>
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
<p>Use this selector to apply egress policies to a private IP address, assigned by a user's local network, that requests arrive to Gateway from.</p>
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
<h2 id="value">Value</h2>
<p>You can input a single value or use regular expressions to specify a range of values.</p>
<p>Gateway uses Rust to evaluate regular expressions. The Rust implementation is slightly different than regex libraries used elsewhere. To evaluate if your regex matches, you can use <a href="https://rustexp.lpil.uk/">Rustexp</a>.</p>
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
<h2 id="limitations">Limitations</h2>
<h3 id="selector-prerequisites">Selector prerequisites</h3>
<p>The <a href="#application">Application</a>, <a href="#content-categories">Content Categories</a>, <a href="#domain">Domain</a>, and <a href="#host">Host</a> selectors require additional setup before they work in egress policies. Before deploying policies with these selectors, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors">Host selectors</a>.</p>
<p>These selectors also resolve the destination IP address when Gateway processes the DNS query, not when the egress policy is applied. If the resolved destination IP and your egress IP are in different regions, connections to destinations that enforce geo-restriction or IP-allowlisting may fail. Refer to <a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/#dns-resolution-location">DNS resolution location</a> for details.</p>
