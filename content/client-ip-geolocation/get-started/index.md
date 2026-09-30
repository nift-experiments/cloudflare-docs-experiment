<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1356.md")
</aside>
<p>There are several things you can do to best handle traffic from Cloudflare VPN and forward-proxy users:</p>
<ul>
<li><strong>Origin operators</strong>:
<ul>
<li>Do not block IP addresses associated with our VPN and proxy products (see the <a href="/client-ip-geolocation/about/">About section</a> for more details)</li>
<li>To get even more accurate geolocation data, ensure your origin is <a href="/client-ip-geolocation/faq/">reachable via IPv6</a></li>
</ul>
</li>
<li><strong>Geolocation data providers</strong>:
<ul>
<li>Regularly pull updated geolocation data from the <a href="https://api.cloudflare.com/local-ip-ranges.csv">Cloudflare API</a></li>
</ul>
</li>
<li><strong>Users of WARP and 1.1.1.1</strong>:
<ul>
<li>Review the <a href="/client-ip-geolocation/faq/#cloudflare-vpn-users">FAQs</a> and <a href="/client-ip-geolocation/about/">About section</a> to learn exactly how, how much, and why we share geolocation data</li>
</ul>
</li>
</ul>
