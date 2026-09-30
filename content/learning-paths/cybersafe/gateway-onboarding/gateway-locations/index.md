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
@markup("md", "content/.markup/bodies/9712.md")
</div> helps reduce latency by routing the user to the closest origin server. Cloudflare enables EDNS in a privacy preserving way by not sending the user's exact IP address but rather the first `/24` range of the larger range that contains their IP address. This `/24` range will share the same geographic location as the user's exact IP address.
   - **Set as Default DNS Location** sets this location as the default DoH endpoint for DNS queries.
6. Select **Continue**.
7. (Optional) Turn on source IP filtering for your configured endpoints, then add any source IPv4/IPv6 addresses to validate.
   - Endpoint authentication is required for standard IPv4 addresses and optional for dedicated IPv4 addresses.
   - **DoH endpoint filtering & authentication** lets you restrict DNS resolution to only valid identities or user tokens in addition to IPv4/IPv6 addresses.
8. Select **Continue**.
9. Review the settings for your DNS location, then choose **Done**.
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="captive-portal-limitation">Captive portal limitation</h3>
@markup("md", "content/.markup/bodies/9711.md")
</aside>
