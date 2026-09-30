<p>DNS policies let you control which websites and services your users can reach by inspecting their DNS queries — the lookups that translate domain names into IP addresses. Because DNS policies act at the lookup stage, they work across all protocols and applications, not just web browsers.</p>
<p>When a user makes a DNS request, <a href="/cloudflare-one/traffic-policies/">Gateway</a> matches the request against the DNS policies you have set up for your organization. If the domain does not belong to any blocked categories, or if it matches an Allow or Override policy, the user's client receives an address based on DNS resolution from Cloudflare's public DNS resolver (1.1.1.1). You can also use a <a href="/cloudflare-one/traffic-policies/resolver-policies/">resolver policy</a> to redirect DNS requests to a custom server.</p>
<p>A DNS policy consists of an <strong>Action</strong> as well as a logical expression that determines the scope of the action. To build an expression, you need to choose a <strong>Selector</strong> and an <strong>Operator</strong>, and enter a value or range of values in the <strong>Value</strong> field. You can use <strong>And</strong> and <strong>Or</strong> logical operators to evaluate multiple conditions.</p>
<ul>
<li><a href="#actions">Actions</a></li>
<li><a href="#selectors">Selectors</a></li>
<li><a href="#comparison-operators">Comparison operators</a></li>
<li><a href="#value">Value</a></li>
<li><a href="#logical-operators">Logical operators</a></li>
</ul>
<p>When creating a DNS policy, you can select as many security risk categories and content categories as needed to fully secure your network. Unless a more specific selector is configured in a policy (for example, <em>User Email</em> or <em>Source IP</em>), then the policy will be evaluated against all DNS queries that reach Gateway from your organization.</p>
<p>If a condition in an expression joins a query attribute (such as <em>Source IP</em>) and a response attribute (such as <em>Resolved IP</em>), then the condition will be evaluated when the response is received.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="terraform-provider-v4-precedence-limitation">Terraform provider v4 precedence limitation</h3>
@markup("md", "content/.markup/bodies/6654.md")
</aside>
<h2 id="actions">Actions</h2>
<p>The action determines what Gateway does when a DNS query matches your policy conditions. You can assign one action per policy.</p>
<p>These are the action types you can choose from:</p>
<ul>
<li><a href="#allow">Allow</a></li>
<li><a href="#block">Block</a></li>
<li><a href="#override">Override</a></li>
<li><a href="#safe-search">Safe Search</a></li>
<li><a href="#youtube-restricted-mode">YouTube Restricted Mode</a></li>
</ul>
<h3 id="allow">Allow</h3>
<p>API value: <code>allow</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6655.md")
</div></details>
<p>Policies with Allow actions explicitly permit DNS queries to resolve. Gateway uses a <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">first-match principle</a>, which means that if an Allow policy matches a query at a higher precedence than a Block policy, the query will be allowed to resolve. For example, the following configuration allows DNS queries to reach domains categorized as belonging to the Education content category:</p>
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
<td>Content Categories</td>
<td>in</td>
<td><em>Education</em></td>
<td>Allow</td>
</tr>
</tbody>
</table>
<h4 id="disable-dnssec-validation">Disable DNSSEC validation</h4>
<p>DNSSEC (Domain Name System Security Extensions) verifies that DNS responses have not been tampered with by checking a cryptographic signature attached to the record. When you select <strong>Disable DNSSEC validation</strong>, Gateway will resolve DNS queries even if the signature cannot be validated. We do not recommend disabling DNSSEC validation unless you know that the validation failure is due to DNSSEC configuration issues and not malicious attacks.</p>
<h3 id="block">Block</h3>
<p>API value: <code>block</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6656.md")
</div></details>
<p>Policies with Block actions prevent DNS queries from resolving for destinations you specify within the Selector and Value fields. For example, the following configuration blocks DNS queries from reaching domains categorized as belonging to the Adult Themes content category:</p>
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
<td>Content Categories</td>
<td>in</td>
<td><em>Adult Themes</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<h4 id="custom-block-page">Custom block page</h4>
<p>When choosing the Block action, turn on <strong>Modify Gateway block behavior</strong> to respond to queries with a block page to display to users who go to blocked websites. Optionally, you can override your global block page setting with a URL redirect for the specific DNS policy. For more information, refer to <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">Block page</a>.</p>
<p>If the block page is turned off for a policy, Gateway will respond to blocked queries with an <code>A</code> record (IPv4) of <code>0.0.0.0</code> or an <code>AAAA</code> record (IPv6) of <code>::</code>. Because no server responds at these addresses, the browser will display its default connection error page.</p>
<p>To block the resolution of queries for DNS records with types other than <code>A</code> or <code>AAAA</code>, Gateway will respond with the <code>REFUSED (RCODE:5)</code> DNS return code. Gateway will block the request but will not display a block page.</p>
<h4 id="cloudflare-one-client-block-notifications">Cloudflare One Client block notifications</h4>
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6657.md")
</div></details>
<p>Turn on <p><strong>Display block notification for Cloudflare One Client</strong></p>
to display notifications for Gateway block events. Blocked users will receive an operating system notification from the Cloudflare One Client with a custom message you set. If you do not set a custom message, the Cloudflare One Client will display a default message. Custom messages must be 100 characters or less. The Cloudflare One Client will only display one notification per minute.</p>
<p>Upon selecting the notification, the Cloudflare One Client will direct your users to the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">Gateway block page</a> you have configured. Optionally, you can direct users to a custom URL, such as an internal support form.</p>
<p>When you turn on <strong>Send policy context</strong>, Gateway will append details of the matching request to the redirected URL as a query string. Not every context field will be included. Potential policy context fields include:</p>
<details class="nb-details"><summary>Policy context fields</summary><div class="nb-details-body">
@input("content/.markup/bodies/6658.md")
</div></details>
<div class="nb-data-component" data-cf-component="Render"></div>
<h3 id="override">Override</h3>
<p>API value: <code>override</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6659.md")
</div></details>
<p>Policies with Override actions replace the real DNS answer with a destination you specify. When a user queries a domain that matches the policy, Gateway returns your custom IP address or hostname instead of the actual DNS record. For example, you can provide a custom response IP of <code>1.2.3.4</code> for all queries to <code>www.example.com</code> with the following policy:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
<th>Override Hostname</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hostname</td>
<td>is</td>
<td><code>www.example.com</code></td>
<td>Override</td>
<td><code>1.2.3.4</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6653.md")
</aside>
<h3 id="safe-search">Safe Search</h3>
<p>API value: <code>safesearch</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6660.md")
</div></details>
<p>SafeSearch is a feature of search engines that helps you filter explicit or offensive content. When you enable SafeSearch, the search engine filters explicit or offensive content and returns search results that are safe for children or at work.</p>
<p>You can use Cloudflare Gateway to enable SafeSearch on search engines like Google, Bing, Yandex, YouTube and DuckDuckGo. For example, to enable SafeSearch for Google, you can create the following policy:</p>
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
<td>Domain</td>
<td>is</td>
<td><code>google.com</code></td>
<td>Safe Search</td>
</tr>
</tbody>
</table>
<h3 id="youtube-restricted-mode">YouTube Restricted Mode</h3>
<p>API value: <code>ytrestricted</code></p>
<details class="nb-details"><summary>Available selectors</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6661.md")
</div></details>
<p>Similarly, you can enforce YouTube Restricted mode by choosing the <em>YouTube Restricted</em> action. YouTube Restricted Mode is an automated filter for adult and offensive content built into YouTube. To enable YouTube Restricted Mode, you could set up a policy like the following:</p>
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
<td>DNS Domain</td>
<td>is</td>
<td><code>youtube.com</code></td>
<td>YouTube Restricted</td>
</tr>
</tbody>
</table>
<p>This setup ensures users will be blocked from accessing offensive sites using DNS.</p>
<h2 id="selectors">Selectors</h2>
<p>Gateway matches DNS queries against the following selectors, or criteria.</p>
<p>Each selector is evaluated during a specific phase of the DNS resolution process:</p>
<ul>
<li><strong>Before DNS resolution</strong> — Gateway inspects properties of the incoming query (for example, the domain name or source IP) before looking up the answer.</li>
<li><strong>During DNS resolution</strong> — Gateway inspects information discovered while resolving the query (for example, the authoritative nameserver IP).</li>
<li><strong>After DNS resolution</strong> — Gateway inspects the DNS answer (for example, the resolved IP or CNAME record) after resolution completes.</li>
</ul>
<p>The Override action cannot be used with selectors evaluated during or after DNS resolution, because the override must be applied before the answer is returned. For more information on how evaluation phase interacts with precedence, refer to <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#dns-policies">order of enforcement</a>.</p>
<h3 id="application">Application</h3>
<p>You can apply DNS policies to a growing list of popular web applications. Refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Application and app types</a> for more information.</p>
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
<td>Application</td>
<td><code>any(app.ids[*] in {505})</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="authoritative-nameserver-ip">Authoritative Nameserver IP</h3>
<p>Use this selector to match against the IP address of the authoritative nameserver IP address.</p>
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
<td>Authoritative Nameserver IP</td>
<td><code>dns.authoritative_ns_ips == 198.51.100.0</code></td>
<td>During DNS resolution</td>
</tr>
</tbody>
</table>
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
<p>When using an Allow or Block action, you can optionally <a href="/cloudflare-one/traffic-policies/domain-categories/#filter-traffic-by-resolved-ip-category">block IP addresses</a> or <a href="/cloudflare-one/traffic-policies/domain-categories/#ignore-cname-domain-categories">filter categories for <code>CNAME</code> records</a>.</p>
<h3 id="dns-cname-record">DNS CNAME Record</h3>
<p>Use this selector to filter DNS responses by their <code>CNAME</code> records.</p>
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
<td>DNS CNAME Response Value</td>
<td><code>any(dns.response.cname[*] in {&quot;www.apple.com.edgekey.net&quot;})</code></td>
<td>After DNS resolution</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6652.md")
</aside>
<h3 id="dns-mx-record">DNS MX Record</h3>
<p>Use this selector to filter DNS responses by their <code>MX</code> records.</p>
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
<td>DNS MX Response Value</td>
<td><code>any(dns.response.mx[*] in {&quot;gmail-smtp-in.l.google.com&quot;})</code></td>
<td>After DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="dns-ptr-record">DNS PTR Record</h3>
<p>Use this selector to filter DNS responses by their <code>PTR</code> records.</p>
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
<td>DNS PTR Response Value</td>
<td><code>any(dns.response.ptr[*] in {&quot;255.2.0.192.in-addr.arpa&quot;})</code></td>
<td>After DNS resolution</td>
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
<h3 id="dns-txt-record">DNS TXT Record</h3>
<p>Use this selector to filter DNS responses by their <code>TXT</code> records.</p>
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
<td>DNS TXT Response Value</td>
<td><code>any(dns.response.txt[*] in {&quot;your_text&quot;})</code></td>
<td>After DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="doh-subdomain-dns-over-https">DoH Subdomain (DNS over HTTPS)</h3>
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
@markup("md", "content/.markup/bodies/6651.md")
</aside>
<h3 id="indicator-feeds">Indicator Feeds</h3>
<p>Use this selector to match against custom indicator feeds.</p>
<p>You can use a <a href="/security-center/indicator-feeds/#publicly-available-feeds">publicly available indicator feed</a> or a custom indicator feed assigned to your account by a designated third-party vendor. For more information on indicator feeds, refer to <a href="/security-center/indicator-feeds/">Custom Indicator Feeds</a>.</p>
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
<td>Indicator Feeds</td>
<td><code>dns.indicator_feed</code></td>
<td>Before DNS resolution</td>
</tr>
</tbody>
</table>
<p>When using an Allow or Block action, you can optionally <a href="/cloudflare-one/traffic-policies/domain-categories/#filter-traffic-by-resolved-ip-category">block IP addresses</a> or <a href="/cloudflare-one/traffic-policies/domain-categories/#ignore-cname-domain-categories">filter categories for <code>CNAME</code> records</a>.</p>
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
<h3 id="resolved-continent">Resolved Continent</h3>
<p>Use this selector to filter based on the continent that the query resolves to. Geolocation is determined from the IP address in the response. To specify a continent, enter its two-letter code into the <strong>Value</strong> field:</p>
<ul>
<li>AF - Africa</li>
<li>AN - Antarctica</li>
<li>AS - Asia</li>
<li>EU - Europe</li>
<li>NA - North America</li>
<li>OC - Oceania</li>
<li>SA - South America</li>
</ul>
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
<td>Resolved Continent IP Geolocation</td>
<td><code>dns.dst.geo.continent == &quot;EU&quot;</code></td>
<td>After DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="resolved-country">Resolved Country</h3>
<p>Use this selector to filter based on the country that the query resolves to. Geolocation is determined from the IP address in the response. To specify a country, enter its <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2 code</a> in the <strong>Value</strong> field.</p>
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
<td>Resolved Country IP Geolocation</td>
<td><code>dns.dst.geo.country == &quot;RU&quot;</code></td>
<td>After DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="resolved-ip">Resolved IP</h3>
<p>Use this selector to filter based on the IP addresses that the query resolves to.</p>
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
<td>Resolved IP</td>
<td><code>any(dns.resolved_ips[*] == 198.51.100.0)</code></td>
<td>After DNS resolution</td>
</tr>
</tbody>
</table>
<h3 id="request-context-categories">Request Context Categories</h3>
<p>Use this selector to match a dynamic list of <a href="/cloudflare-one/traffic-policies/domain-categories/#category-and-subcategory-ids">category IDs</a> sent in the <a href="https://datatracker.ietf.org/doc/html/rfc6891">EDNS (Extension Mechanisms for DNS)</a> portion of a DNS query. EDNS allows extra metadata to be attached to a DNS query beyond the standard fields. Gateway reads category IDs from the EDNS OPT code <code>65050</code>.</p>
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
<td>Request Context Categories</td>
<td><code>dns.categories_in_request_context_matches</code></td>
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
<p>When using an Allow or Block action, you can optionally <a href="/cloudflare-one/traffic-policies/domain-categories/#filter-traffic-by-resolved-ip-category">block IP addresses</a> or <a href="/cloudflare-one/traffic-policies/domain-categories/#ignore-cname-domain-categories">filter categories for <code>CNAME</code> records</a>.</p>
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
<h3 id="source-internal-ip">Source Internal IP</h3>
<p>Use this selector to apply policies to the source internal IP address of a DNS query. For example, this could be the private IP address of the hosts behind <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a> (formerly Magic WAN) or <a href="/mesh/">Cloudflare Mesh</a> used by your organization to send queries to Gateway.</p>
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
<td>Source Internal IP</td>
<td><code>dns.src_internal_ip == 10.10.0.1</code></td>
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
<h2 id="limitations">Limitations</h2>
<h3 id="third-party-filtering-conflict">Third-party filtering conflict</h3>
<p>Gateway will not properly filter traffic sent through third-party VPNs or other Internet filtering software, such as <a href="https://support.apple.com/102602">iCloud Private Relay</a> or <a href="https://github.com/GoogleChrome/ip-protection#ip-protection">Google Chrome IP Protection</a>. To ensure your DNS policies apply to your traffic, Cloudflare recommends turning off software that may interfere with Gateway.</p>
<p>To turn off iCloud Private Relay, refer to the Apple user guides for <a href="https://support.apple.com/guide/mac-help/use-icloud-private-relay-mchlecadabe0/">macOS</a> or <a href="https://support.apple.com/guide/iphone/protect-web-browsing-icloud-private-relay-iph499d287c2/">iOS</a>.</p>
<h3 id="cloudflare-wan-forwarding">Cloudflare WAN forwarding</h3>
<p>To apply DNS policies to queries forwarded through <a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a>, you can either point your organization's DNS resolver to an IPv6, DNS over HTTPS (DoH), or DNS over TLS (DoT) endpoint or request a dedicated resolver IPv4 address. For more information, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/">DNS resolver IPs and hostnames</a>.</p>
<h3 id="fallback-dns">Fallback DNS</h3>
<p>Some applications (for example, WhatsApp and Android Studio) have backup DNS servers built into their code. If their primary DNS query is blocked by Gateway, these apps automatically retry the query against their built-in DNS servers (for example, Google's <code>8.8.8.8</code>), which bypasses your policies entirely. To mitigate this behavior, you create a <a href="/cloudflare-one/traffic-policies/network-policies/">Gateway Network policy</a> to block outbound DNS traffic on TCP/UDP port <code>53</code> to the fallback DNS servers. For example, to block Google's fallback DNS servers:</p>
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
<td>Protocol</td>
<td>in</td>
<td><em>TCP</em>, <em>UDP</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Destination Port</td>
<td>in</td>
<td><code>53</code></td>
<td>And</td>
<td></td>
</tr>
<tr>
<td>Destination IP</td>
<td>in</td>
<td><code>8.8.8.8</code>, <code>8.8.4.4</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
