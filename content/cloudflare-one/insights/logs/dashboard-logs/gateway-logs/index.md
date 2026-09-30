<p>Gateway activity logs record the DNS queries, Network packets, and HTTP requests inspected by Gateway. You can also download encrypted <a href="/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/">SSH command logs</a> for sessions proxied by Gateway.</p>
<p>Enterprise users can generate more detailed logs with <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/">Manage PII</a></li></ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="private-source-ip-substitution">Private source IP substitution</h3>
@markup("md", "content/.markup/bodies/4992.md")
</aside>
<h2 id="view-gateway-activity-logs">View Gateway activity logs</h2>
<p>To view Gateway activity logs:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong>.</li>
<li>Choose a type of Gateway log:
<ul>
<li><strong>DNS query logs</strong></li>
<li><strong>Network logs</strong></li>
<li><strong>HTTP request logs</strong></li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="log-viewer-beta">Log viewer (beta)</h3>
@markup("md", "content/.markup/bodies/4991.md")
</aside>
3. (Optional) Filter the logs that display in the log viewer. You can filter logs by their timestamp and event details (such as host, URL, user email, policy action, and more).
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/4990.md")
</aside>
4. Select an individual timestamp to investigate the event in more detail.
<h2 id="selective-logging">Selective logging</h2>
<p>By default, Gateway logs all events, including DNS queries and HTTP requests that are allowed and not a risk. You can choose to disable logging entirely or only log blocked requests.</p>
<p>To customize what Gateway logs:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</p>
</li>
<li>
<p>Under <strong>Traffic logging</strong> &gt; <strong>Log traffic activity</strong>, choose your preference for DNS, Network, and HTTP logs.</p>
</li>
</ol>
<p>These settings only apply to logs displayed in Cloudflare One. Logpush data is unaffected.</p>
<h2 id="dns-logs">DNS logs</h2>
<h3 id="explanation-of-the-fields">Explanation of the fields</h3>
<h4 id="basic-information">Basic information</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Query name</strong></td>
<td>Name of the domain that was queried.</td>
</tr>
<tr>
<td><strong>Query ID</strong></td>
<td>UUID of the query assigned by Cloudflare.</td>
</tr>
<tr>
<td><strong>Email</strong></td>
<td>Email address of the user who registered the Cloudflare One Client where traffic originated from. If a non-identity on-ramp (such as a <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoint</a>) or machine-level authentication (such as a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a>) was used, this value will be <code>non_identity@&lt;team-domain&gt;.cloudflareaccess.com</code>.</td>
</tr>
<tr>
<td><strong>Action</strong></td>
<td>The <a href="/cloudflare-one/traffic-policies/dns-policies/#actions">Action</a> Gateway applied to the query (such as Allow or Block).</td>
</tr>
<tr>
<td><strong>Time</strong></td>
<td>Date and time of the DNS query.</td>
</tr>
<tr>
<td><strong>Resolver decision</strong></td>
<td>The reason why Gateway applied a particular <strong>Action</strong> to the request. Refer to the <a href="#resolver-decisions">list of resolver decisions</a>.</td>
</tr>
<tr>
<td><strong>Resolved IPs</strong></td>
<td>Resolved IP addresses in the response.</td>
</tr>
<tr>
<td><strong>CNAMEs</strong></td>
<td><code>CNAME</code> records in the query.</td>
</tr>
</tbody>
</table>
<h4 id="configuration-information">Configuration information</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>DNS location</strong></td>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">User-configured location</a> from where the DNS query was made.</td>
</tr>
<tr>
<td><strong>Policy name</strong></td>
<td>Name of the matched policy.</td>
</tr>
<tr>
<td><strong>Policy ID</strong></td>
<td>ID of the matched policy.</td>
</tr>
<tr>
<td><strong>Policy description</strong></td>
<td>Description of the matched policy.</td>
</tr>
<tr>
<td><strong>DoH subdomain</strong></td>
<td><span class="nb-interactive-component" data-cf-component="GlossaryTooltip"></td>
</tr>
</tbody>
</table>
@markup("md", "content/.markup/bodies/4993.md")
</div> of the DNS location.                                   |
| **Protocol**           | Protocol that was used to make the DNS query (such as `https`).                                                              |
<h4 id="identities">Identities</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Email</strong></td>
<td>Email address of the user who registered the Cloudflare One Client where traffic originated from.</td>
</tr>
<tr>
<td><strong>User ID</strong></td>
<td>UUID of the user. Each unique email address in your organization will have a UUID associated with it.</td>
</tr>
<tr>
<td><strong>Registration ID</strong></td>
<td>UUID of the user's Cloudflare One Client registration. A unique registration ID is generated each time a device is registered for a particular email. The same physical device may have multiple registration IDs.</td>
</tr>
<tr>
<td><strong>Device name</strong></td>
<td>Display name of the device returned by the operating system to the Cloudflare One Client. Typically this is the hostname of a device. Not all devices will have a device name. Device names are not guaranteed to be unique.</td>
</tr>
<tr>
<td><strong>Device ID</strong></td>
<td>UUID of the device connected with the Cloudflare One Client. Each physical device in your organization will have a UUID.</td>
</tr>
<tr>
<td><strong>Last authenticated</strong></td>
<td>Date and time the user last authenticated their Zero Trust session.</td>
</tr>
</tbody>
</table>
<h4 id="dns-query-details">DNS query details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Query ID</strong></td>
<td>UUID of the query assigned by Cloudflare.</td>
</tr>
<tr>
<td><strong>Query type</strong></td>
<td>Type of <a href="https://en.wikipedia.org/wiki/List_of_DNS_record_types">DNS query</a>.</td>
</tr>
<tr>
<td><strong>Initial query domain categories</strong></td>
<td><a href="/cloudflare-one/traffic-policies/domain-categories/">Content categories</a> that the domain belongs to.</td>
</tr>
<tr>
<td><strong>Matched categories</strong></td>
<td>Name of the Gateway policy category that match the domain.</td>
</tr>
<tr>
<td><strong>Matched indicator feed names</strong></td>
<td>Name of the indicator feeds that matched a Gateway policy.</td>
</tr>
<tr>
<td><strong>Query indicator feed names</strong></td>
<td>Name of the indicator feeds that a matched domain or IP belongs to.</td>
</tr>
<tr>
<td><strong>Resolved continent IP geolocation</strong></td>
<td>Continent code of the resolved IP address.</td>
</tr>
<tr>
<td><strong>Resolved country IP geolocation</strong></td>
<td>Country code of the resolved IP address.</td>
</tr>
<tr>
<td><strong>DoT subdomain</strong></td>
<td>DoT subdomain of the DNS location.</td>
</tr>
<tr>
<td><strong>Source IP</strong></td>
<td>Public source IP address of the DNS query.</td>
</tr>
<tr>
<td><strong>Source IP continent</strong></td>
<td>Continent code of the source IP address.</td>
</tr>
<tr>
<td><strong>Source IP country</strong></td>
<td>Country code of the source IP address.</td>
</tr>
<tr>
<td><strong>Source internal IP</strong></td>
<td>Private IP address assigned by the user's local network.</td>
</tr>
<tr>
<td><strong>Application name</strong></td>
<td>Name of the application that matched the domain.</td>
</tr>
<tr>
<td><strong>Resolver IP</strong></td>
<td>Public IP address of the DNS resolver.</td>
</tr>
<tr>
<td><strong>Port</strong></td>
<td>Port that was used to make the DNS query.</td>
</tr>
<tr>
<td><strong>Location ID</strong></td>
<td>ID of the DNS location where the query originated.</td>
</tr>
<tr>
<td><strong>Scheduling - Time zone</strong></td>
<td>Time zone of the DNS query source.</td>
</tr>
<tr>
<td><strong>Scheduling - Time zone inferred method</strong></td>
<td>Method used to determine the DNS query source's time zone.</td>
</tr>
</tbody>
</table>
<h4 id="dns-response-details">DNS response details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Resolved CNAME categories</strong></td>
<td>Content categories associated with the resolved <code>CNAME</code> records in the response.</td>
</tr>
<tr>
<td><strong>Resolved IP categories</strong></td>
<td>Content categories associated with the resolved IPs in the response.</td>
</tr>
<tr>
<td><strong>Resolved IPs</strong></td>
<td>Resolved IPs in the response.</td>
</tr>
<tr>
<td><strong>Authoritative nameserver IP</strong></td>
<td>IP address of the authoritative nameserver answering the DNS query.</td>
</tr>
<tr>
<td><strong>EDE errors</strong></td>
<td><a href="https://www.rfc-editor.org/rfc/rfc8914.html">Extended DNS error codes</a> in the response.</td>
</tr>
</tbody>
</table>
<h4 id="custom-resolver">Custom resolver</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Address</strong></td>
<td>Address of your custom resolver.</td>
</tr>
<tr>
<td><strong>Policy</strong></td>
<td>Name of the matched resolver policy.</td>
</tr>
<tr>
<td><strong>Response</strong></td>
<td>Status of the custom resolver response.</td>
</tr>
<tr>
<td><strong>Time (in milliseconds)</strong></td>
<td>Duration of time it took for the custom resolver to respond.</td>
</tr>
</tbody>
</table>
<h3 id="resolver-decisions">Resolver decisions</h3>
<table>
<thead>
<tr>
<th>Name</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>blockedByCategory</code></td>
<td><code>3</code></td>
<td>Domain or hostname matched a category in a Block policy.</td>
</tr>
<tr>
<td><code>allowedOnNoLocation</code></td>
<td><code>4</code></td>
<td>Allowed because query did not match a Gateway DNS location.</td>
</tr>
<tr>
<td><code>allowedOnNoPolicyMatch</code></td>
<td><code>5</code></td>
<td>Allowed because query did not match a policy.</td>
</tr>
<tr>
<td><code>blockedAlwaysCategory</code></td>
<td><code>6</code></td>
<td>Domain or hostname is always blocked by Cloudflare.</td>
</tr>
<tr>
<td><code>overrideForSafeSearch</code></td>
<td><code>7</code></td>
<td>Response was overridden by a Safe Search policy.</td>
</tr>
<tr>
<td><code>overrideApplied</code></td>
<td><code>8</code></td>
<td>Response was overridden by an Override policy.</td>
</tr>
<tr>
<td><code>blockedRule</code></td>
<td><code>9</code></td>
<td>IP address in the response matched a Block policy.</td>
</tr>
<tr>
<td><code>allowedRule</code></td>
<td><code>10</code></td>
<td>IP address in the response matched an Allow policy.</td>
</tr>
</tbody>
</table>
<h2 id="network-logs">Network logs</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="failed-connection-logs">Failed connection logs</h3>
@markup("md", "content/.markup/bodies/4989.md")
</aside>
<h3 id="explanation-of-the-fields-1">Explanation of the fields</h3>
<h4 id="basic-information-1">Basic information</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Source IP</strong></td>
<td>IP address of the user sending the packet.</td>
</tr>
<tr>
<td><strong>Source Internal IP</strong></td>
<td>Private IP address assigned by the user's local network.</td>
</tr>
<tr>
<td><strong>Destination IP</strong></td>
<td>IP address of the packet's target.</td>
</tr>
<tr>
<td><strong>Action</strong></td>
<td>The Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/#actions">Action</a> taken based on the first rule that matched (such as Allow or Block).</td>
</tr>
<tr>
<td><strong>Session ID</strong></td>
<td>ID of the unique session.</td>
</tr>
<tr>
<td><strong>Time</strong></td>
<td>Date and time of the session.</td>
</tr>
</tbody>
</table>
<h4 id="matched-policies">Matched policies</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>DNS location</strong></td>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">User-configured location</a> from where the DNS query was made.</td>
</tr>
<tr>
<td><strong>Policy name</strong></td>
<td>Name of the matched policy.</td>
</tr>
<tr>
<td><strong>Policy ID</strong></td>
<td>ID of the policy enforcing the decision Gateway made.</td>
</tr>
<tr>
<td><strong>Policy description</strong></td>
<td>Description of the matched policy.</td>
</tr>
</tbody>
</table>
<h4 id="identities-1">Identities</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Email</strong></td>
<td>Email address of the user sending the packet. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td><strong>User ID</strong></td>
<td>ID of the user sending the packet. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td><strong>Registration ID</strong></td>
<td>ID of the user's device registration. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td><strong>Device name</strong></td>
<td>Name of the device that sent the packet.</td>
</tr>
<tr>
<td><strong>Device ID</strong></td>
<td>ID of the physical device that sent the packet. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td><strong>Last authenticated</strong></td>
<td>Date and time the user last authenticated with Zero Trust.</td>
</tr>
</tbody>
</table>
<h4 id="network-query-details">Network query details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Source IP</strong></td>
<td>IP address of the user sending the packet.</td>
</tr>
<tr>
<td><strong>Source port</strong></td>
<td>Source port number for the packet.</td>
</tr>
<tr>
<td><strong>Source country</strong></td>
<td>Country code for the packet source.</td>
</tr>
<tr>
<td><strong>Source IP continent</strong></td>
<td>Continent code of the source IP address.</td>
</tr>
<tr>
<td><strong>Source IP country</strong></td>
<td>Country code of the source IP address.</td>
</tr>
<tr>
<td><strong>Destination IP</strong></td>
<td>IP address of the packet's target.</td>
</tr>
<tr>
<td><strong>Destination port</strong></td>
<td>Destination port number for the packet.</td>
</tr>
<tr>
<td><strong>Destination IP continent</strong></td>
<td>Continent code of the IP address for the packet's destination.</td>
</tr>
<tr>
<td><strong>Destination IP country</strong></td>
<td>Country code of the IP address for the packet's destination.</td>
</tr>
<tr>
<td><strong>Transport protocol</strong></td>
<td>Protocol over which the packet was sent.</td>
</tr>
<tr>
<td><strong>Detected Protocol</strong></td>
<td>The detected <a href="/cloudflare-one/traffic-policies/network-policies/protocol-detection/">network protocol</a>.</td>
</tr>
<tr>
<td><strong>SNI</strong></td>
<td>Host whose Server Name Indication (SNI) header Gateway will filter traffic against.</td>
</tr>
<tr>
<td><strong>Virtual Network</strong></td>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual network</a> that the client is connected to.</td>
</tr>
<tr>
<td><strong>Category details</strong></td>
<td>Category or categories associated with the packet.</td>
</tr>
<tr>
<td><strong>Proxy endpoint</strong></td>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC file proxy endpoint</a> Gateway forwarded traffic to, if applicable.</td>
</tr>
<tr>
<td><strong>Application ID</strong></td>
<td>ID of the application that matched the domain.</td>
</tr>
<tr>
<td><strong>Application name</strong></td>
<td>Name of the application that matched the domain.</td>
</tr>
</tbody>
</table>
<h2 id="http-logs">HTTP logs</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4988.md")
</aside>
<h3 id="explanation-of-the-fields-2">Explanation of the fields</h3>
<h4 id="basic-information-2">Basic information</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Host</strong></td>
<td>Hostname in the HTTP header for the HTTP request. Gateway will log the SNI in this field if it responded to the request with a Do Not Inspect action. If Gateway does not receive the SNI, this field will be empty.</td>
</tr>
<tr>
<td><strong>Email</strong></td>
<td>Email address of the user who made the HTTP request. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td><strong>Action</strong></td>
<td>The Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/#actions">Action</a> taken based on the first rule that matched (such as Allow or Block).</td>
</tr>
<tr>
<td><strong>Request ID</strong></td>
<td>Unique ID of the request.</td>
</tr>
<tr>
<td><strong>Time</strong></td>
<td>Date and time of the HTTP request.</td>
</tr>
<tr>
<td><strong>Source internal IP</strong></td>
<td>Private IP address assigned by the user's local network.</td>
</tr>
<tr>
<td><strong>User agent</strong></td>
<td>User agent header sent in the request by the originating device.</td>
</tr>
<tr>
<td><strong>Policy details</strong></td>
<td>Policy corresponding to the decision Gateway made based on the traffic criteria of the request.</td>
</tr>
<tr>
<td><strong>DLP profiles</strong></td>
<td>Name of the matched <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profile</a>.</td>
</tr>
<tr>
<td><strong>DLP profile entries</strong></td>
<td>Name of the matched entry within the DLP profile.</td>
</tr>
<tr>
<td><strong>Uploaded/downloaded file</strong></td>
<td>Information about the file transferred in the request found by <a href="#enhanced-file-detection">enhanced file detection</a>. Details include: <ul><li>File name</li><li>File type</li><li>File size</li><li>File hash (for Allowed requests only)</li><li>Content type</li><li>Direction (Upload/Download)</li><li>Action (Block/Allow)</li></ul></td>
</tr>
</tbody>
</table>
<h4 id="matched-policies-1">Matched policies</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>DNS location</strong></td>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">User-configured location</a> from where the DNS query was made.</td>
</tr>
<tr>
<td><strong>Policy name</strong></td>
<td>Name of the matched policy.</td>
</tr>
<tr>
<td><strong>Policy ID</strong></td>
<td>ID of the matched policy.</td>
</tr>
<tr>
<td><strong>Policy description</strong></td>
<td>Description of the matched policy.</td>
</tr>
<tr>
<td><strong>Matched category ID</strong></td>
<td>ID of the category matched in the policy.</td>
</tr>
<tr>
<td><strong>Matched category name</strong></td>
<td>Name of the category matched in the policy.</td>
</tr>
</tbody>
</table>
<h4 id="identities-2">Identities</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Email</strong></td>
<td>Email address of the user who made the HTTP request. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td><strong>User ID</strong></td>
<td>ID of the user who made the request. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td><strong>Registration ID</strong></td>
<td>ID of the user's device registration. This is generated by the Cloudflare One Client.</td>
</tr>
<tr>
<td><strong>Device name</strong></td>
<td>Name of the device that made the request.</td>
</tr>
<tr>
<td><strong>Device ID</strong></td>
<td>ID of the physical device that made the request. This is generated by the Cloudflare One Client on the device that created the request.</td>
</tr>
<tr>
<td><strong>Last authenticated</strong></td>
<td>Date and time the user last authenticated with Zero Trust.</td>
</tr>
</tbody>
</table>
<h4 id="http-query-details">HTTP query details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>HTTP Version</strong></td>
<td>HTTP version of the origin that Gateway connected to on behalf of the user.</td>
</tr>
<tr>
<td><strong>HTTP Method</strong></td>
<td>HTTP method used for the request (such as <code>GET</code> or <code>POST</code>).</td>
</tr>
<tr>
<td><strong>HTTP Status Code</strong></td>
<td><a href="/support/troubleshooting/http-status-codes/">HTTP status code</a> returned in the response.</td>
</tr>
<tr>
<td><strong>URL</strong></td>
<td>Full URL of the HTTP request.</td>
</tr>
<tr>
<td><strong>Referer</strong></td>
<td>Referer request header containing the address of the page making the request.</td>
</tr>
<tr>
<td><strong>Source IP</strong></td>
<td>Public source IP address of the HTTP request.</td>
</tr>
<tr>
<td><strong>Source Port</strong></td>
<td>Port that was used to make the HTTP request.</td>
</tr>
<tr>
<td><strong>Source IP continent</strong></td>
<td>Continent code of the HTTP request.</td>
</tr>
<tr>
<td><strong>Source IP country</strong></td>
<td>Country code of the HTTP request.</td>
</tr>
<tr>
<td><strong>Destination IP</strong></td>
<td>Public IP address of the destination requested.</td>
</tr>
<tr>
<td><strong>Destination Port</strong></td>
<td>Port of the destination requested.</td>
</tr>
<tr>
<td><strong>Destination IP continent</strong></td>
<td>Continent code of the destination requested.</td>
</tr>
<tr>
<td><strong>Destination IP country</strong></td>
<td>Country code of the destination requested.</td>
</tr>
<tr>
<td><strong>Blocked file reason</strong></td>
<td>Reason why the file was blocked if a file transfer occurred or was attempted.</td>
</tr>
<tr>
<td><strong>Category details</strong></td>
<td>Detailed information on the category the blocked file belongs to.</td>
</tr>
<tr>
<td><strong>Application ID</strong></td>
<td>ID of the application that matched the domain.</td>
</tr>
<tr>
<td><strong>Application name</strong></td>
<td>Name of the application that matched the domain.</td>
</tr>
<tr>
<td><strong>Categories</strong></td>
<td><a href="/cloudflare-one/traffic-policies/domain-categories/">Content categories</a> that the domain belongs to.</td>
</tr>
<tr>
<td><strong>Proxy endpoint</strong></td>
<td><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC file proxy endpoint</a> Gateway forwarded traffic to, if applicable.</td>
</tr>
<tr>
<td><strong>Virtual Network</strong></td>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">Virtual network</a> that the client is connected to.</td>
</tr>
<tr>
<td><strong>Sandbox scanned</strong></td>
<td>Status of the <a href="/cloudflare-one/traffic-policies/http-policies/file-sandboxing/">file quarantine</a>.</td>
</tr>
</tbody>
</table>
<h4 id="file-detection-details">File detection details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Name</strong></td>
<td>Name of the detected file.</td>
</tr>
<tr>
<td><strong>Type</strong></td>
<td>File type of the detected file.</td>
</tr>
<tr>
<td><strong>Size</strong></td>
<td>Size of the detected file.</td>
</tr>
<tr>
<td><strong>Hash</strong></td>
<td>Hash of the detected file, generated by DLP.</td>
</tr>
<tr>
<td><strong>Content type</strong></td>
<td>MIME type of the detected file.</td>
</tr>
<tr>
<td><strong>Direction</strong></td>
<td>Upload or download direction of the detected file.</td>
</tr>
<tr>
<td><strong>Action</strong></td>
<td>The Action Gateway applied to the request.</td>
</tr>
</tbody>
</table>
<h3 id="enhanced-file-detection">Enhanced file detection</h3>
<p>Enhanced file detection is an optional feature that extracts more file information from HTTP traffic. When turned on, Gateway reads file information from the HTTP body rather than the HTTP headers, providing greater accuracy and reliability. This feature may have a minor impact on performance for file-heavy organizations.</p>
<p>To turn on enhanced file detection:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>In <strong>Proxy and inspection settings</strong>, turn on <strong>Inspect HTTPS requests with TLS decryption</strong>.</li>
<li>In <strong>Policy settings</strong>, turn on <strong>Allow enhanced file detection</strong>.</li>
</ol>
<h3 id="isolate-requests">Isolate requests</h3>
<p>When a user creates an <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">isolation policy</a>, Gateway logs isolation-related requests in two stages:</p>
<ol>
<li><strong>Initial request</strong> — The request that triggers isolation is logged with an Isolate action. Because this request is not yet isolated, the <code>is_isolated</code> field returns <code>false</code>.</li>
<li><strong>Subsequent requests</strong> — After Zero Trust returns the result to the user in an isolated browser, Gateway logs all subsequent requests in the isolated browser with the action (such as Allow or Block), and the <code>is_isolated</code> field returns <code>true</code>.</li>
</ol>
<h2 id="limitations">Limitations</h2>
<p>If a connection closes before Gateway inspects and filters the traffic, Gateway logs the event with an Unknown action.</p>
<p>Gateway activity logs are not available in the dashboard if you turn on the <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary (CMB)</a> within Cloudflare Data Localization Suite (DLS). CMB restricts where customer traffic metadata and logs are stored by region. Enterprise users with CMB turned on can still export logs via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>. For more information, refer to <a href="/data-localization/compatibility/#zero-trust">DLS product compatibility</a>.</p>
