<p>To connect to Cloudflare Gateway resolver - which is <a href="/dns/internal-dns/#architecture-overview">required to reach private resources in Internal DNS</a> - you can use the following options:</p>
<ul>
<li>DNS endpoints supported with <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">DNS locations</a>
<ul>
<li>DNS over UDP/TCP port 53 (IPv4 or IPv6)</li>
<li>DNS over TLS</li>
<li>DNS over HTTPS</li>
</ul>
</li>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">Proxy Auto-Configuration (PAC) files</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">WARP device client</a></li>
<li><a href="/cloudflare-one/remote-browser-isolation/setup/clientless-browser-isolation/#filter-dns-queries">Clientless browser isolation</a></li>
<li><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Cloudflare WAN</a></li>
</ul>
