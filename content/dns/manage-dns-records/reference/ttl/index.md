<p><strong>Time to Live (TTL)</strong> is a field on <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> that controls how long each record is cached and — as a result — how long it takes for record updates to reach your end users.</p>
<p>Longer TTLs speed up <a href="https://www.cloudflare.com/learning/dns/what-is-dns/">DNS lookups</a> by increasing the chance of cached results, but a longer TTL also means that updates to your records take longer to go into effect.</p>
<h2 id="proxied-records">Proxied records</h2>
<p>By default, all <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7790.md")
</div> have a TTL of **Auto**, which is set to 300 seconds. This value cannot be edited.
<p>Since only <a href="/dns/manage-dns-records/reference/dns-record-types/#ip-address-resolution">records used for IP address resolution</a> can be proxied, this setting ensures that potential changes to the assigned <a href="/fundamentals/concepts/cloudflare-ip-addresses/">anycast IP address</a> will take effect quickly, as recursive resolvers will not cache them for longer than 300 seconds (five minutes).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7789.md")
</aside>
<h2 id="unproxied-records">Unproxied records</h2>
<p>For <strong>DNS only</strong> records, you can choose a TTL between <strong>30 seconds</strong> (Enterprise) or <strong>60 seconds</strong> (non-Enterprise) and <strong>1 day</strong>.</p>
<p>A TTL of <strong>Auto</strong> is set to 300 seconds (five minutes).</p>
<h2 id="nameserver-ttl">Nameserver TTL</h2>
<p><a href="/dns/nameservers/nameserver-options/#nameserver-ttl">Nameserver TTL</a> is a separate feature and only affects Cloudflare nameservers and custom nameservers. For other <a href="/dns/manage-dns-records/reference/dns-record-types/#ns">NS records</a> on your DNS records table, TTL is controlled by their respective TTL fields.</p>
