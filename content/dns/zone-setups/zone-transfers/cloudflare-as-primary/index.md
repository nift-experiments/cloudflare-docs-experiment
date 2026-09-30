<p>With outgoing zone transfers, you can use Cloudflare as your primary DNS provider and configure one or more peer DNS servers as secondary DNS providers.</p>
<p>When you <a href="/dns/manage-dns-records/how-to/create-dns-records/">make edits</a> to Cloudflare DNS, those DNS records will be transferred from Cloudflare to your secondary provider via zone transfer using <a href="https://datatracker.ietf.org/doc/html/rfc5936">AXFR</a> or <a href="https://datatracker.ietf.org/doc/html/rfc1995">IXFR</a></p>
<p><img src="/assets/upstream/images/dns/cloudflare-as-primary.png" alt="With Cloudflare as your primary provider in a multi-provider setup, Cloudflare periodically transfers records to your secondary DNS provider." /></p>
<h2 id="how-to">How to</h2>
<ul>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/setup/">Set up outgoing zone transfers</a></li>
</ul>
<h2 id="availability">Availability</h2>
<p>Outgoing zone transfers are available to Enterprise customers who are currently using Cloudflare as their <a href="/dns/zone-setups/full-setup/">authoritative DNS provider</a>. For more details on activation and pricing, contact your account team.</p>
<h2 id="notes">Notes</h2>
<p>If you use <a href="/load-balancing/">Cloudflare Load Balancing</a>, only proxied Load Balancer DNS records will be transferred.</p>
