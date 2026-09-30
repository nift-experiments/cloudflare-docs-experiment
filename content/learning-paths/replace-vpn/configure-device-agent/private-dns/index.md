<p>By default, all DNS requests on the user device are resolved by Cloudflare's <a href="/1.1.1.1/">public DNS resolver</a> except for common top level domains used for local resolution (such as <code>localhost</code>). To allow users to connect to internal server names or domains that do not resolve on the public Internet, you have two options:</p>
<ul>
<li><a href="#local-domain-fallback">Add internal domains to Local Domain Fallback</a></li>
<li><a href="#resolver-policies">Build custom resolver policies</a></li>
</ul>
<h2 id="local-domain-fallback">Local Domain Fallback</h2>
<p>Local Domain Fallback tells the Cloudflare One Client to send specific DNS requests to your private DNS resolver instead of to Cloudflare's public DNS resolver. This method was the primary delivery mechanism for private DNS for a long time, and is the simplest option, but it has two shortcomings: you cannot deterministically route private DNS queries to different resolvers based on specific attributes, and you cannot apply Gateway DNS policies to this traffic because Cloudflare is not resolving it.</p>
<p>To learn more about how Local Domain Fallback works, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#how-the-warp-client-handles-dns-requests">How the Cloudflare One Client handles DNS requests</a>.</p>
<h3 id="add-a-domain">Add a domain</h3>
<p>To add a domain to the Local Domain Fallback list:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9935.md")
</div></div>
<p>The Cloudflare One Client tries all servers and always uses the fastest response, even if that response is <code>no records found</code>. We recommend specifying at least one DNS server for each domain. If a value is not specified, the Cloudflare One Client will try to identify the DNS server (or servers) used on the device before it started, and use that server for each domain in the Local Domain Fallback list.</p>
<h3 id="route-traffic-to-fallback-server">Route traffic to fallback server</h3>
<p>The Cloudflare One Client routes DNS traffic to your <a href="#add-a-domain">Local Domain Fallback server</a> according to your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel configuration</a>. To ensure that queries can reach your private DNS server:</p>
<ul>
<li>
<p>If your DNS server is only reachable inside of the WARP tunnel (for example, via <code>cloudflared</code> or Cloudflare WAN):</p>
<ol>
<li>
<p>Go to <strong>Networking</strong> &gt; <strong>Routes</strong> and verify that the DNS server is connected to Cloudflare. To connect a DNS server, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/">Private networks</a>.</p>
</li>
<li>
<p>In your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnel configuration</a>, verify that the DNS server IP routes through the WARP tunnel.</p>
</li>
</ol>
</li>
<li>
<p>If your DNS server is only reachable outside of the WARP tunnel (for example, via a third-party VPN), verify that the DNS server IP is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">excluded from the WARP tunnel</a>.</p>
</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/#how-the-warp-client-handles-dns-requests">How the Cloudflare One Client handles DNS requests</a>.</p>
<h2 id="resolver-policies">Resolver policies</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9932.md")
</aside>
<p><a href="/cloudflare-one/traffic-policies/resolver-policies/">Resolver policies</a> provide similar functionality to Local Domain Fallback but occur in Cloudflare Gateway rather than on the local device. This option is recommended if you want more granular control over private DNS resolution. For example, you can ensure that all users in a specific geography use the private DNS server closest to them, ensure that specific conditions are met before resolving private DNS traffic, and apply <a href="/cloudflare-one/traffic-policies/dns-policies/">Gateway DNS policies</a> to private DNS traffic.</p>
<h3 id="create-a-resolver-policy">Create a resolver policy</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="virtual-network-limitation">Virtual network limitation</h3>
@markup("md", "content/.markup/bodies/9931.md")
</aside>
<p>To create a resolver policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9938.md")
</div></div>
<p>When a user's query matches a resolver policy, Gateway will send the query to your listed resolvers in the following order:</p>
<ol>
<li>Public resolvers</li>
<li>Private resolvers behind the default virtual network for your account</li>
<li>Private resolvers behind a custom virtual network</li>
</ol>
<p>Gateway will cache the fastest resolver for use in subsequent queries. Resolver priority is cached on a per user basis for each data center.</p>
