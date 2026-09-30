<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4388.md")
</aside>
<p>By default, Gateway sends DNS requests to <a href="/1.1.1.1/">1.1.1.1</a>, Cloudflare's public DNS resolver, for resolution. Enterprise users can instead create Gateway policies to route DNS queries to custom resolvers.</p>
<pre><code class="language-mermaid">flowchart TD&#10;    %% Accessibility&#10;    accTitle: How Gateway routes DNS queries&#10;    accDescr: Flowchart describing the order Cloudflare Gateway routes a DNS query from an endpoint through DNS and resolver policies back to the user.&#10;&#10;    %% Flowchart&#10;    user([&quot;User&quot;])--&gt;endpoint[/&quot;Gateway DNS endpoint&quot;/]&#10;&#10;    endpoint--&gt;query[&quot;DNS policy (query)&quot;]&#10;&#10;    query--&gt;resolver[&quot;Resolver policy&quot;]&#10;&#10;    resolver--&quot;Routes to &lt;/br&gt;custom resolver&quot;--&gt;response[&quot;DNS policy (response)&quot;]&#10;&#10;    response--&quot;Returns response&quot;--&gt;user&#10;</code></pre>
<p>Gateway will route user traffic to your configured DNS resolver based on the matching policy, even if your resolvers' IP addresses overlap.</p>
<h2 id="use-cases">Use cases</h2>
<p>You may use resolver policies if you require access to non-publicly routed domains, such as private network services or internal resources. You may also use resolver policies if you need to access a protected DNS service or want to simplify DNS management for multiple locations.</p>
<h3 id="internal-dns">Internal DNS</h3>
<p><a href="/dns/internal-dns/">Cloudflare Internal DNS</a> allows you to manage DNS records for internal resources on a private network. DNS zones configured in Internal DNS can only be queried by the Gateway resolver. With resolver policies, you can determine how Gateway resolves your organization's DNS queries to resolve to internal resources based on the context of the query, such as known source IPs for a geographic location.</p>
<p>To get started with resolving internal DNS queries with resolver policies, refer to <a href="/dns/internal-dns/get-started/">Get started</a>.</p>
<h3 id="local-domain-fallback">Local Domain Fallback</h3>
<p>Use resolver policies when your DNS server is reachable from Cloudflare's network — for example, through a Cloudflare Tunnel, IPsec/GRE tunnel, or the public Internet. Use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">Local Domain Fallback</a> when the DNS server is only reachable from the user's device.</p>
<p>If both Local Domain Fallback and resolver policies are configured for the same device, Cloudflare will apply your client-side Local Domain Fallback rules first. If you onboard DNS queries to Gateway with the Cloudflare One Client and route them with resolver policies, the source IP of the queries will be the IP address assigned by the Cloudflare One Client.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="local-domain-fallback-or-gateway-resolver-policies">Local Domain Fallback or Gateway Resolver policies?</h3>
@markup("md", "content/.markup/bodies/4387.md")
</aside>
<h2 id="resolver-connections">Resolver connections</h2>
<p>Resolver policies support TCP and UDP connections. Custom resolvers can point to the Internet via IPv4 or IPv6, or to a private network service, such as a <a href="/magic-transit/how-to/configure-tunnel-endpoints/">Magic tunnel</a>. Policies default to port <code>53</code>. You can change which port your resolver uses by customizing it in your policy.</p>
<p>You can protect your authoritative nameservers from DDoS attacks by enabling <a href="/dns/dns-firewall/">DNS Firewall</a>.</p>
<h3 id="cloudflare-tunnel">Cloudflare Tunnel</h3>
<p>You can configure connections to a private resolver connected to Cloudflare with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>. To ensure <code>cloudflared</code> can route UDP traffic to your resolver, connect your tunnel via <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#protocol">QUIC</a>.</p>
<p>For more information on connecting a private DNS resolver to Cloudflare with Cloudflare Tunnel, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/">Private DNS</a>.</p>
<h3 id="cloudflare-wan">Cloudflare WAN</h3>
<p>To enable connections to a private resolver connected to Cloudflare via <a href="/cloudflare-wan/">Cloudflare WAN</a>, contact your account team.</p>
<h3 id="available-dns-endpoints">Available DNS endpoints</h3>
<p>Resolver policies can route queries for resolution from the following DNS endpoints:</p>
<ul>
<li>IPv4</li>
<li>IPv6</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/">DNS over HTTPS (DoH)</a></li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/">DNS over TLS (DoT)</a></li>
<li>DNS queries generated by Cloudflare <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> and <a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/">Clientless Web Isolation</a></li>
<li>DNS queries generated by <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints</a></li>
</ul>
<p>Gateway will filter, resolve, and log your queries regardless of endpoint.</p>
<h2 id="create-a-resolver-policy">Create a resolver policy</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="virtual-network-limitation">Virtual network limitation</h3>
@markup("md", "content/.markup/bodies/4385.md")
</aside>
<p>To create a resolver policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4391.md")
</div></div>
<p>When a user's query matches a resolver policy, Gateway will send the query to your listed resolvers in the following order:</p>
<ol>
<li>Public resolvers</li>
<li>Private resolvers behind the default virtual network for your account</li>
<li>Private resolvers behind a custom virtual network</li>
</ol>
<p>Gateway will cache the fastest resolver for use in subsequent queries. Resolver priority is cached on a per user basis for each data center.</p>
<p>For more information on creating a DNS policy, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="terraform-provider-v4-precedence-limitation">Terraform provider v4 precedence limitation</h3>
@markup("md", "content/.markup/bodies/4384.md")
</aside>
<h2 id="send-dns-queries-sourced-from-dedicated-egress-ips">Send DNS queries sourced from dedicated egress IPs <span class="nb-badge">Closed beta</span></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4383.md")
</aside>
<p>By default, DNS requests that Gateway sends to your custom resolvers use shared Cloudflare source IP addresses. If your upstream resolver restricts access by source IP, you can configure a resolver policy to send those requests from your <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a> instead.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>Your account must have dedicated egress IPs provisioned.</li>
<li>The resolver policy must include at least one public resolver. Dedicated egress IPs cannot be used when all resolvers route through private networks.</li>
</ul>
<h3 id="enable-dedicated-egress-on-a-resolver-policy">Enable dedicated egress on a resolver policy</h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/one">Cloudflare One dashboard</a>, go to <strong>Traffic policies</strong> &gt; <strong>Resolver policies</strong>.</li>
<li>Create or edit a resolver policy that uses custom DNS resolvers.</li>
<li>Under the custom resolver configuration, turn on <strong>Use dedicated egress IPs for DNS requests to custom resolvers</strong>.</li>
<li>Select a <strong>Primary IPv4</strong>, <strong>IPv6</strong>, and optionally a <strong>Secondary IPv4</strong> address from the available dedicated egress IPs.</li>
<li>Save the policy.</li>
</ol>
<h3 id="api-configuration">API configuration</h3>
<p>To configure dedicated egress on a resolver policy via the API, add an <code>egress</code> object to <code>rule_settings</code>:</p>
<pre><code class="language-json">{&#10;	&quot;rule_settings&quot;: {&#10;		&quot;dns_resolvers&quot;: {&#10;			&quot;ipv4&quot;: [{ &quot;ip&quot;: &quot;198.51.100.1&quot; }]&#10;		},&#10;		&quot;egress&quot;: {&#10;			&quot;ipv4&quot;: &quot;104.30.133.232&quot;,&#10;			&quot;ipv6&quot;: &quot;2a09:bac0:1000:3ec::/64&quot;,&#10;			&quot;ipv4_fallback&quot;: &quot;104.30.134.156&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>The <code>egress</code> object uses the same schema as <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a>.</p>
<h2 id="selectors">Selectors</h2>
<h3 id="content-categories">Content Categories</h3>
<p>Use this selector to filter domains belonging to specific <a href="/cloudflare-one/traffic-policies/domain-categories/#content-categories">content categories</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content Categories</td>
<td><code>any(dns.content_category[*] in {1})</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="dns-resolver-ip">DNS Resolver IP</h3>
<p>Use this selector to apply policies to DNS queries that arrived to your Gateway Resolver IP address aligned with a registered DNS location. For most Gateway customers, this is an IPv4 anycast address and policies created using this IPv4 address will apply to all DNS locations. However, each DNS location has a dedicated IPv6 address and some Gateway customers have been supplied with a dedicated IPv4 address — these both can be used to apply policies to specific registered DNS locations.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>DNS Resolver IP</td>
<td><code>any(dns.resolved_ip[*] == 198.51.100.0)</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="doh-subdomain">DoH Subdomain</h3>
<p>Use this selector to match against DNS queries that arrive via DNS-over-HTTPS (DoH) destined for the DoH endpoint configured for each DNS location. For example, you can use a DNS location with a DoH endpoint of <code>abcdefg.cloudflare-gateway.com</code> by choosing the DoH Subdomain selector and inputting a value of <code>abcdefg</code>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>DOH Subdomain</td>
<td><code>dns.doh_subdomain == &quot;abcdefg&quot;</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="domain">Domain</h3>
<p>Use this selector to match against a domain and all subdomains. For example, you can match <code>example.com</code> and its subdomains, such as <code>www.example.com</code>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Domain</td>
<td><code>any(dns.domains[*] == &quot;example.com&quot;)</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<p>Gateway policies do not support domains with non-Latin characters directly. To use a domain with non-Latin characters, add it to a <a href="/cloudflare-one/reusable-components/lists/">list</a>.</p>
<h3 id="host">Host</h3>
<p>Use this selector to match against only the hostname specified. For example, you can match <code>test.example.com</code> but not <code>example.com</code> or <code>www.test.example.com</code>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Host</td>
<td><code>dns.fqdn == &quot;example.com&quot;</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<p>Gateway policies do not support hostnames with non-Latin characters directly. To use a hostname with non-Latin characters, add it to a <a href="/cloudflare-one/reusable-components/lists/">list</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4382.md")
</aside>
<h3 id="location">Location</h3>
<p>Use this selector to apply policies to a specific <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">Gateway DNS location</a> or set of locations.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Location</td>
<td><code>dns.location in {&quot;location_uuid_1&quot; &quot;location_uuid_2&quot;}</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="query-record-type">Query Record Type</h3>
<p>Use this selector to choose the DNS resource record type that you would like to apply policies against. For example, you can match <code>A</code> records for a domain but not <code>MX</code> records.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Query Record Type</td>
<td><code>dns.query_rtype == &quot;TXT&quot;</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="security-categories">Security Categories</h3>
<p>Use this selector to match domains (and optionally, <a href="/cloudflare-one/traffic-policies/domain-categories/#filter-traffic-by-resolved-ip-category">IP addresses</a>) belonging to specific <a href="/cloudflare-one/traffic-policies/domain-categories/#security-categories">security categories</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Security Categories</td>
<td><code>any(dns.security_category[*] in {1})</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="source-continent">Source Continent</h3>
<p>Use this selector to filter based on the continent where the query arrived to Gateway from.</p>
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
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Continent IP Geolocation</td>
<td><code>dns.src.geo.continent == &quot;North America&quot;</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="source-country">Source Country</h3>
<p>Use this selector to filter based on the country where the query arrived to Gateway from.</p>
<p>Geolocation is determined from the device's public IP address (typically assigned by the user's ISP). To specify a country, enter its <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha-2 code</a> in the <strong>Value</strong> field.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source Country IP Geolocation</td>
<td><code>dns.src.geo.country == &quot;RU&quot;</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="source-ip">Source IP</h3>
<p>Use this selector to apply policies to the source IP address of DNS queries. For example, this could be the WAN IP address of the stub resolver used by your organization to send queries to Gateway.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>Source IP</td>
<td><code>dns.src_ip == 198.51.100.0</code></td>
<td>Before DNS resolution</td>
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
<th>Evaluation phase</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Email</td>
<td><code>identity.email == &quot;user@example.com&quot;</code></td>
<td>Before DNS resolution</td>
</tr>
<tr>
<td>User Name</td>
<td><code>identity.name == &quot;Test User&quot;</code></td>
<td>Before DNS resolution</td>
</tr>
<tr>
<td>User Group IDs</td>
<td><code>any(identity.groups[*].id in {&quot;group_id&quot;})</code></td>
<td>Before DNS resolution</td>
</tr>
<tr>
<td>User Group Names</td>
<td><code>any(identity.groups[*].name in {&quot;group_name&quot;})</code></td>
<td>Before DNS resolution</td>
</tr>
<tr>
<td>User Group Emails</td>
<td><code>any(identity.groups[*].email in {&quot;group@example.com&quot;})</code></td>
<td>Before DNS resolution</td>
</tr>
<tr>
<td>SAML Attributes</td>
<td><code>any(identity.saml_attributes[&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name&quot;] in {&quot;Test User&quot;})</code></td>
<td>Before DNS resolution</td>
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
<p>In the <strong>Value</strong> field, you can input a single value when using an equality comparison operator (such as <em>is</em>) or multiple values when using a containment comparison operator (such as <em>in</em>). Additionally, you can use <a href="#regular-expressions">regular expressions</a> (or regex) to specify a range of values for supported selectors.</p>
<h3 id="regular-expressions">Regular expressions</h3>
<p>Regular expressions are evaluated using Rust. The Rust implementation is slightly different than regex libraries used elsewhere. For more information, refer to our guide for <a href="/cloudflare-one/access-controls/policies/app-paths/#wildcards">Wildcards</a>. To evaluate if your regex matches, you can use <a href="https://rustexp.lpil.uk/">Rustexp</a>.</p>
<p>If you want to match multiple values, you can use the pipe symbol (<code>|</code>) as an OR operator. You do not need to use an escape character (<code>\</code>) before the pipe symbol. For example, the following expression evaluates to true when the hostname matches either <code>.*whispersystems.org</code> or <code>.*signal.org</code>:</p>
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
<td>Host</td>
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
<p>The <strong>Or</strong> operator will only work with conditions in the same expression group. For example, you cannot compare conditions in <strong>Traffic</strong> with conditions in <p>Identity</p>
.</p>
