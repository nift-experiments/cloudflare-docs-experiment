<p>Similar to the network onboarding practices in the <a href="/learning-paths/replace-vpn/connect-private-network/">Replace your VPN</a> implementation guide, there are a number of ways to on-ramp your network traffic to the Cloudflare global network. This guide will quickly explore all of the options to on-ramp traffic to Cloudflare Gateway to inspect, apply policies, and filter.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10058.md")
</aside>
<h2 id="device-on-ramps">Device on-ramps</h2>
<p>The most common way to protect and filter your end-user traffic is by using a device client. The standard Cloudflare device client supports a number of operating systems and deployment methodologies, but there can still be scenarios in which an alternative path makes sense.</p>
<h3 id="cloudflare-one-client">Cloudflare One Client</h3>
<p>The Cloudflare One Client is the most common onramp to send user traffic to Gateway. It is a lightweight device client, which builds proxy tunnels using either Wireguard or MASQUE, and builds a DNS proxy using DNS-over-HTTPS. It supports all major operating systems, supports all common forms of endpoint management tooling, and has a robust series of management parameters and profiles to accurately scope the needs of a diverse user base. It has flexible operating modes and can control device traffic as a proxy, control device DNS traffic as a DNS proxy, or both. It is the most common method to send traffic from user devices to be filtered and decrypted by Cloudflare Gateway.</p>
<h3 id="pac-files-enterprise-only">PAC files (Enterprise only)</h3>
<p>Cloudflare supports filtering HTTP/S traffic sent via a PAC file on a user device. PAC files configured to send traffic to Cloudflare target a domain specific to your account tenant, and receive and process all URL traffic for that device that fits the proxy profile. PAC files are most commonly used in scenarios in which the device client is not appropriate or cannot be installed -- specifically Windows pre-2008 and Windows Server 2012, and devices which cannot install client software at all.</p>
<h3 id="clientless-browser-isolation">Clientless Browser Isolation</h3>
<p>Cloudflare Browser Isolation runs a headless, Chromium-based browser for your users to accomplish their secure browsing needs. It can be activated via an Access application, a Gateway policy, or by using link-based isolation (reverse proxy). In this model, your users can connect from any device to a proxy website to browse the Internet while applying all your Gateway HTTP policies and inspection requirements.</p>
<table>
<thead>
<tr>
<th></th>
<th>Cloudflare One Client</th>
<th>PAC Files</th>
<th>Clientless Browser Isolation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Supported OS</td>
<td>macOS, Windows, Linux, iOS, Android</td>
<td>All desktop OS</td>
<td>All OS (with HTML5 compliant browser)</td>
</tr>
<tr>
<td>Configurable via MDM</td>
<td>Yes</td>
<td>Yes</td>
<td>N/A</td>
</tr>
<tr>
<td>Gateway policy types supported</td>
<td>DNS, Network, HTTP, Resolver, Egress</td>
<td>HTTP</td>
<td>DNS, Network, HTTP, Resolver, Egress</td>
</tr>
<tr>
<td>Identity-based policies supported</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Network Session Logs</a></td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="network-on-ramps">Network on-ramps</h2>
<p>The primary ways to source multi-device or network traffic to Cloudflare Gateway are via Cloudflare WAN (formerly Magic WAN) using GRE or IPsec tunnels, via <a href="#cloudflare-mesh">Cloudflare Mesh</a> as a software-defined all-ports traffic proxy, or via upstream DNS for a whole network using <a href="#dns-filtering-locations">DNS filtering locations</a>.</p>
<h3 id="cloudflare-wan">Cloudflare WAN</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10057.md")
</aside>
<p><a href="/cloudflare-wan/">Cloudflare WAN</a> is Cloudflare's offering most analogous to a traditional SD-WAN. Cloudflare WAN is typically deployed via an IPsec or GRE tunnel terminating on customer devices (such as firewalls or routers), or via our Cloudflare One Appliance hardware device. You can also deploy Cloudflare WAN using <a href="/network-interconnect/">Cloudflare Network Interconnect</a> (CNI) at private peering locations or some public cloud instances (where compatible).</p>
<p>Cloudflare WAN on-ramps traffic via your connections and can send all network and HTTP traffic through Cloudflare Gateway for inspection.</p>
<p>For more information on how Cloudflare WAN integrates with Zero Trust, refer to <a href="/cloudflare-wan/zero-trust/">Zero Trust integration</a>.</p>
<h3 id="cloudflare-mesh">Cloudflare Mesh <span class="nb-badge">Beta</span></h3>
<p><a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector), a software agent similar to our device client, functions as a virtual device to establish a connection between your network and the Cloudflare global network. You can install Cloudflare Mesh on a dedicated Linux server or virtual machine.</p>
<p>Cloudflare Mesh supports egressing traffic from your private network to the Internet as a gateway. This means it can allow traffic initiated from a network to be on-ramped to Cloudflare for either public or private destinations. You can use Cloudflare Mesh to establish a secure egress path for servers or users on a network which may not each be able to run the Cloudflare One Client and still apply Gateway network and HTTP inspection policies. This connection is most analogous to proxy server connectivity or site-to-site VPN.</p>
<p>For more information on setting up Cloudflare Mesh, refer to <a href="/mesh/">Set up Cloudflare Mesh</a>.</p>
<h3 id="dns-filtering-locations">DNS filtering locations</h3>
<div class="nb-glossary-definition"><p>DNS locations are a collection of DNS endpoints which can be mapped to physical entities such as offices, homes, or data centers.</p></div>
<p>The fastest way to start filtering DNS queries from a location is by changing the DNS resolvers at the router or updating the upstream resolution to Cloudflare DNS resolution endpoints. This can also be accomplished from individual devices, or an network or subnet which sets resolver IPs for clients via DHCP.</p>
<p>For more information on setting up DNS locations, refer to <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">Add locations</a>.</p>
<table>
<thead>
<tr>
<th></th>
<th>Cloudflare WAN</th>
<th>Cloudflare Mesh</th>
<th>DNS Locations</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gateway policy types supported</td>
<td>Network, HTTP, Egress</td>
<td>Network, HTTP, Egress</td>
<td>DNS, Resolver</td>
</tr>
</tbody>
</table>
