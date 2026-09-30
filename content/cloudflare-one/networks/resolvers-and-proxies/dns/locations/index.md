<div class="nb-glossary-definition"><p>DNS locations are a collection of DNS endpoints which can be mapped to physical entities such as offices, homes, or data centers.</p></div>
<p>The fastest way to start filtering DNS queries from a location is by changing the DNS resolvers at the router.</p>
<h2 id="add-a-dns-location">Add a DNS location</h2>
<p>To add a DNS location to Gateway:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong> &gt; <strong>DNS locations</strong>.</li>
<li>Select <strong>Add a location</strong>.</li>
<li>Choose a name for your DNS location.</li>
<li>Choose at least one <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#dns-endpoints">DNS endpoint</a> to resolve your organization's DNS queries.</li>
<li>(Optional) Toggle the following settings:
<ul>
<li><strong>Enable EDNS client subnet</strong> sends a user's IP geolocation to authoritative DNS nameservers. <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
</li>
</ol>
@markup("md", "content/.markup/bodies/5886.md")
</div> helps reduce latency by routing the user to the closest origin server. Cloudflare enables EDNS in a privacy preserving way by not sending the user's exact IP address but rather the first `/24` range of the larger range that contains their IP address. This `/24` range will share the same geographic location as the user's exact IP address.
   - **Set as Default DNS Location** sets this location as the default DoH endpoint for DNS queries.
6. Select **Continue**.
7. (Optional) Turn on source IP filtering for your configured endpoints, then add any source IPv4/IPv6 addresses to validate.
   - Endpoint authentication is required for standard IPv4 addresses and optional for dedicated IPv4 addresses.
   - **DoH endpoint filtering & authentication** lets you restrict DNS resolution to only valid identities or user tokens in addition to IPv4/IPv6 addresses.
8. Select **Continue**.
9. Review the settings for your DNS location, then choose **Done**.
<ol start="10">
<li>Change the DNS resolvers on your router, browser, or OS by following the setup instructions in the UI.</li>
<li>Select <strong>Go to DNS Location</strong>. Your location will appear in your list of locations.</li>
</ol>
<p>You can now apply <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a> to your location using the <a href="/cloudflare-one/traffic-policies/dns-policies/#location">Location selector</a>.</p>
<h2 id="dns-endpoints">DNS endpoints</h2>
<h3 id="ipv4-and-ipv6-dns">IPv4 and IPv6 DNS</h3>
<p>Cloudflare will prefill the <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#source-ip"><strong>Source IPv4 Address</strong></a> based on the network you are on. Additionally, Enterprise users can use <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#dns-resolver-ip">dedicated DNS resolver IP addresses</a> assigned to their account or <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip">resolver IP addresses they provide (BYOIP)</a>.</p>
<p>You do not need to configure the IPv4 DNS endpoint if:</p>
<ul>
<li>Your network only uses IPv6.</li>
<li>Your users will send all DNS requests from this location using <a href="#dns-over-https-doh">DNS over HTTPS</a> via a browser.</li>
<li>You will deploy the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="your-ipv4-address-is-taken-error">Your IPv4 address is taken error</h3>
@markup("md", "content/.markup/bodies/5885.md")
</aside>
<h3 id="dns-over-tls-dot">DNS over TLS (DoT)</h3>
<div class="nb-glossary-definition"><p>DNS over TLS (DoT) is a standard for encrypting DNS traffic using its own port (<code>853</code>) and TLS encryption.</p></div>
<p>For more information, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/">DNS over TLS</a>.</p>
<h3 id="dns-over-https-doh">DNS over HTTPS (DoH)</h3>
<div class="nb-glossary-definition"><p>DNS over HTTPS (DoH) is a standard for encrypting DNS traffic via the HTTPS protocol, preventing tracking and spoofing of DNS queries.</p></div>
<p>Gateway requires a DoH endpoint for default DNS locations. For more information, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-https/">DNS over HTTPS</a>.</p>
<h2 id="secure-dns-locations">Secure DNS locations</h2>
<p>Secure DNS locations provide additional protection against malicious domains for use in services such as <a href="/reference-architecture/diagrams/sase/gateway-for-protective-dns/">protective DNS (PDNS)</a>. For a DNS location to be considered secure, Gateway requires that:</p>
<ul>
<li>Your IPv4 and IPv6 endpoints use your <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/dns-resolver-ips/#bring-your-own-dns-resolver-ip">BYOIP addresses</a> (if any).</li>
<li><a href="/cloudflare-one/traffic-policies/network-policies/">Source network filtering</a> is configured for your IPv4, IPv6, and DoT endpoints.</li>
<li>Source network filtering or token authentication are configured for your DoH endpoints.</li>
<li>Any enabled endpoints for a DNS location meet security permissions.</li>
</ul>
<p>You can assign users the <a href="/cloudflare-one/roles-permissions/#zero-trust-roles"><strong>Cloudflare Zero Trust DNS Locations Write</strong> role</a> to grant them the permission to create and edit secure DNS locations. To allow users to view locations, you must also assign the <strong>Cloudflare Zero Trust Read Only</strong> role. Users with these roles can view any DNS location, but can only create or edit secure locations.</p>
<p>Roles that supersede <strong>Cloudflare Zero Trust DNS Locations Write</strong> include:</p>
<ul>
<li>Cloudflare Gateway</li>
<li>Cloudflare Zero Trust</li>
<li>Super Administrator</li>
</ul>
<h2 id="limitations">Limitations</h2>
<h3 id="captive-portals">Captive portals</h3>
<p>Deploying Gateway DNS filtering using static IP addresses may prevent users from connecting to public Wi-Fi networks through captive portals. If users are experiencing connectivity issues related to captive portals, they should:</p>
<ol>
<li>Remove the static IP addresses from the device.</li>
<li>Connect to the Wi-Fi network.</li>
<li>Once the connection has been established, add the static IP addresses back.</li>
</ol>
<p>To avoid this issue, use the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> to connect your devices to Cloudflare One.</p>
<h3 id="third-party-filtering">Third-party filtering</h3>
<p>Gateway will not properly filter traffic sent through third-party VPNs or other Internet filtering software, such as <a href="https://support.apple.com/102602">iCloud Private Relay</a> or <a href="https://github.com/GoogleChrome/ip-protection#ip-protection">Google Chrome IP Protection</a>. To ensure your DNS policies apply to your traffic, Cloudflare recommends turning off software that may interfere with Gateway.</p>
<p>To turn off iCloud Private Relay, refer to the Apple user guides for <a href="https://support.apple.com/guide/mac-help/use-icloud-private-relay-mchlecadabe0/">macOS</a> or <a href="https://support.apple.com/guide/iphone/protect-web-browsing-icloud-private-relay-iph499d287c2/">iOS</a>.</p>
