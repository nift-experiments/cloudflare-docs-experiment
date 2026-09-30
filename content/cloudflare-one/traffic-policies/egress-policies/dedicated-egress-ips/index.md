<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6634.md")
</aside>
<p>Many third-party services require you to allowlist specific source IP addresses before they accept connections. Dedicated egress IPs are static IP addresses assigned exclusively to your account — no other Cloudflare customer shares them.</p>
<p>Each dedicated egress IP consists of an IPv4 address and an IPv6 range, both tied to a specific Cloudflare data center. Cloudflare provisions your account with at least two dedicated egress IPs in two different cities.</p>
<p>You can request additional dedicated egress IPs at any time. Contact your account team to schedule a service window.</p>
<h2 id="turn-on-egress-ips">Turn on egress IPs</h2>
<p>To start routing traffic through dedicated egress IPs:</p>
<ol>
<li>Contact your account team to obtain a dedicated egress IP.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Turn on <strong>Allow Secure Web Gateway to proxy traffic</strong>.</li>
<li>Select <strong>TCP</strong>.</li>
<li>(Optional) Select <strong>UDP</strong>. This will allow HTTP/3 traffic to egress with your dedicated IPs.</li>
</ol>
<p>Dedicated egress IPs are now turned on for all network and HTTP traffic proxied by Gateway. To selectively turn on dedicated egress IPs for a subset of your traffic, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a>.</p>
<h2 id="verify-egress-ips">Verify egress IPs</h2>
<p>To check if your device is using the correct dedicated egress IP:</p>
<ol>
<li>Verify that the device is connected to your Zero Trust organization through the Cloudflare One Client.</li>
<li>Determine the source IPv4 address of your device by going to <code>https://ipv4.icanhazip.com/</code>.</li>
<li>Determine the source IPv6 address of your device by going to <code>https://ipv6.icanhazip.com/</code>.</li>
<li>Verify that the source IPv4 and IPv6 addresses match your dedicated egress IP.</li>
</ol>
<p>When testing against another origin, you may see either an IPv4 or IPv6 address. Gateway does not control which protocol is used — some origins only support one protocol, and when both are available, the client operating system and browser decide. For example, Windows <a href="https://learn.microsoft.com/troubleshoot/windows-server/networking/configure-ipv6-in-windows">favors IPv6 by default</a>.</p>
<h2 id="ips">IPs</h2>
<h3 id="bring-your-own-ip-address-byoip">Bring your own IP address (BYOIP)</h3>
<p>If your organization already owns IPv4 or IPv6 addresses from a regional Internet registry, you can use them as dedicated egress IPs instead of Cloudflare-provided addresses. To obtain an IPv6 range, refer to <a href="https://www.arin.net/resources/guide/ipv6/first_request/">American Registry for Internet Numbers (ARIN)</a> or <a href="https://www.ripe.net/manage-ips-and-asns/ipv6/request-ipv6/">Regional Internet Registry for Europe, Middle East and Central Asia (RIPE NCC)</a>.</p>
<p>After you onboard your IP addresses, they appear as options when you create an <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policy</a> and choose <strong>Use dedicated egress IPs (Cloudflare or BYOIP)</strong> as the <a href="/cloudflare-one/traffic-policies/egress-policies/#egress-methods">egress method</a>. BYOIP dedicated egress IPs do not support <a href="#ip-geolocation">IP geolocation</a>.</p>
<p>For more information, refer to <a href="/byoip/">Cloudflare BYOIP</a> or contact your account team.</p>
<h3 id="cloudflare-ips">Cloudflare IPs</h3>
<p>If you do not have your own authority-provided IPv4 and IPv6 addresses, you can use dedicated egress IPs with a Cloudflare IP address.</p>
<p>You can find your leased Gateway dedicated egress IPs on the dashboard under <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Address space</strong> &gt; <strong>Leased IPs</strong></a>.</p>
<h2 id="limitations">Limitations</h2>
<h3 id="concurrent-connections">Concurrent connections</h3>
<p>Each dedicated egress IP supports up to 40,000 concurrent connections per unique combination of destination IP and destination port. You can configure multiple origins for each combination of dedicated egress IP and source port.</p>
<h3 id="unsupported-traffic">Unsupported traffic</h3>
<p>Dedicated egress IPs do not apply to the following traffic types. These connections use the default shared IPs because Cloudflare identifies them by other means (for example, tunnel ID or account context) rather than source IP.</p>
<ul>
<li>Private networks connected to Zero Trust via Cloudflare Tunnel</li>
<li>Traffic destined for private networks connected to Zero Trust via <a href="/cloudflare-wan/">Cloudflare WAN</a></li>
<li>ICMP traffic (for example, <code>ping</code>)</li>
</ul>
<p>By default, DNS queries that Gateway sends to custom resolvers use shared Cloudflare source IP addresses. You can <a href="/cloudflare-one/traffic-policies/resolver-policies/#send-dns-queries-sourced-from-dedicated-egress-ips">configure a resolver policy to send these queries from dedicated egress IPs</a>.</p>
<h3 id="traffic-resilience">Traffic resilience</h3>
<p>To improve traffic resilience, assign your dedicated egress IPs to different Cloudflare data center locations. If you have multiple IPs in the same city, choose different data centers within that city. For more information, contact your account team.</p>
<p>When creating egress policies with dedicated egress IPs, you must set a secondary IPv4 address to ensure traffic resilience. You can set the secondary IPv4 address to <code>0.0.0.0</code> or a specific Cloudflare location different from your primary IPv4 address. If you set the secondary IPv4 address to <code>0.0.0.0</code>, Gateway will route traffic to the location closest to the user. If the physical location of your primary IPv4 address is not available, Gateway will route traffic to either the default Cloudflare egress range or the secondary location specified.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="fallback-egress-ips">Fallback egress IPs</h3>
@markup("md", "content/.markup/bodies/6633.md")
</aside>
<h3 id="ip-geolocation">IP geolocation</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6632.md")
</aside>
<p>Websites and services use third-party IP geolocation databases to determine where a visitor is located. When you turn on dedicated egress IPs, Gateway updates these databases so they associate your new IPs with the correct city. Until the databases finish updating, services like Google Search may show incorrect regional content — for example, directing users in India to the United States landing page.</p>
<p>Your egress traffic geolocates to the city selected in your <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a>. Traffic that does not match an egress policy defaults to the closest dedicated egress location. Create a <a href="/cloudflare-one/traffic-policies/egress-policies/#catch-all-policy">catch-all egress policy</a> before dedicated egress IPs are assigned to your account to prevent incorrect geolocation while databases update.</p>
<p>To verify that the IP geolocation has updated, check your dedicated egress IP in one of the supported databases:</p>
<details class="nb-details"><summary>Supported IP geolocation databases</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6635.md")
</div></details>
<h3 id="egress-location">Egress location</h3>
<p>Where your users' traffic physically exits the Cloudflare network depends on whether the connection uses IPv4 or IPv6.</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Destination proxied by Cloudflare</th>
<th>Physical egress location</th>
<th>IP geolocation</th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4</td>
<td>No</td>
<td>Data center with dedicated egress IP</td>
<td>Matches dedicated egress IP location</td>
</tr>
<tr>
<td>IPv4</td>
<td>Yes</td>
<td>Locally connected data center</td>
<td>Matches dedicated egress IP location</td>
</tr>
<tr>
<td>IPv6</td>
<td>No</td>
<td>Locally connected data center</td>
<td>Matches dedicated egress IP location</td>
</tr>
<tr>
<td>IPv6</td>
<td>Yes</td>
<td>Locally connected data center</td>
<td>Matches dedicated egress IP location</td>
</tr>
</tbody>
</table>
<h4 id="ipv4">IPv4</h4>
<p>IPv4 addresses are scarce, so Cloudflare must physically route IPv4 traffic to the data center where your dedicated address is provisioned. The user connects to the nearest Cloudflare data center, and Cloudflare internally routes the traffic to the dedicated egress location configured in your <a href="/cloudflare-one/traffic-policies/egress-policies/">egress policies</a>. As a result, the data center shown in the user's Cloudflare One Client preferences may differ from the actual egress location.</p>
<p>Performance is better when users visit domains proxied by Cloudflare (<a href="/dns/proxy-status/">orange-clouded</a> domains). In this case, IPv4 traffic physically exits from the most performant data center while still appearing to originate from your dedicated egress location.</p>
<p>For example, assume you have a primary dedicated egress IP in Los Angeles and a secondary dedicated egress IP in New York. A user in Las Vegas would see Las Vegas as their connected data center. If they go to a site not proxied by Cloudflare (<a href="/dns/proxy-status/#dns-only-records">gray-clouded</a>), such as <code>espn.com</code>, they will egress from Los Angeles (or whichever city is in the matching egress policy). If they go to an orange-clouded site such as <code>cloudflare.com</code>, they will physically egress from Las Vegas but use Los Angeles as their IP geolocation.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="ipv4-and-ipv6-behavior">IPv4 and IPv6 behavior</h3>
@markup("md", "content/.markup/bodies/6631.md")
</aside>
<h4 id="ipv6">IPv6</h4>
<p>Unlike IPv4, IPv6 traffic physically exits from the user's connected data center while still appearing to originate from the dedicated egress IP geolocation. This works because IPv6 has enough address space for Cloudflare to assign IPv6 ranges from all possible geolocations to every data center. Each account receives a /64 IPv6 range.</p>
<p>In the example above, the Las Vegas user would physically egress from Las Vegas but their traffic would IP geolocate to Los Angeles. This means:</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Physical egress</td>
<td>User's closest Cloudflare data center (Las Vegas)</td>
</tr>
<tr>
<td>IP geolocation</td>
<td>Dedicated egress IP location configured in your egress policy (Los Angeles)</td>
</tr>
<tr>
<td>Logs</td>
<td>Correct IP geolocation (Los Angeles) even though the physical egress is from a different location (Las Vegas)</td>
</tr>
</tbody>
</table>
<h2 id="frequently-asked-questions-faq">Frequently asked questions (FAQ)</h2>
<h3 id="can-i-provision-the-same-egress-ip-address-to-multiple-data-centers">Can I provision the same egress IP address to multiple data centers?</h3>
<p>No, egress IPs are limited to a single data center.</p>
<h3 id="can-my-users-in-different-locations-egress-from-their-closest-data-center-via-a-single-egress-ip">Can my users in different locations egress from their closest data center via a single egress IP?</h3>
<p>No, traffic exits from the data center where the egress IP is provisioned. If your users are spread across multiple regions, reserve multiple egress IPs in different data centers and assign each user group to the closest one.</p>
<h3 id="can-i-use-dedicated-egress-ips-with-traffic-proxied-via-pac-files-cloudflare-one-networks-resolvers-and-proxies-proxy-endpoints">Can I use dedicated egress IPs with traffic proxied via <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC files</a>?</h3>
<p>Yes, your users will egress via their provisioned IP address.</p>
<h3 id="what-happens-when-i-use-dedicated-egress-ips-with-cloudflare-browser-isolation-cloudflare-one-remote-browser-isolation">What happens when I use dedicated egress IPs with <a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a>?</h3>
<p>Your users will connect to the nearest data center, where the remote browser session will load. The remote browser will then egress via the data center with their provisioned egress IP.</p>
<h3 id="do-dedicated-egress-ips-work-on-the-cloudflare-china-network-china-network">Do dedicated egress IPs work on the <a href="/china-network/">Cloudflare China Network</a>?</h3>
<p>No, Gateway does not support dedicated egress IPs on the China Network.</p>
