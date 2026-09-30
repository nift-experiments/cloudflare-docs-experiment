<p>When you set up <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">incoming zone transfers</a> on a secondary zone, you cannot enable the proxy on any transferred DNS records by default.</p>
<p>With Secondary DNS override, you can use Cloudflare as your secondary DNS provider but still get the <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">performance and security benefits</a> of Cloudflare's proxy. Additionally it lets you override any A and AAAA records on your zone apex with a CNAME record.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8043.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you set up Secondary DNS override, make sure that you have:</p>
<ul>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/">Set up a secondary DNS zone</a> and confirmed your DNS records are transferred correctly.</li>
<li>Set your <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings/">DNSSEC with Secondary DNS</a> option to either <strong>Unsigned</strong> or <strong>Live Signing</strong>. If set to <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/#set-up-pre-signed-dnssec">Pre-signed</a>, Cloudflare will treat all your DNS records as unproxied (DNS only).</li>
<li>Removed all nameservers from your registrar except for those provided by Cloudflare (highly recommended).</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8042.md")
</aside>
<h2 id="set-up-secondary-dns-override">Set up Secondary DNS override</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8046.md")
</div></div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="zone-transfers-interaction">Zone transfers interaction</h3>
@markup("md", "content/.markup/bodies/8041.md")
</aside>
<h2 id="proxied-a-and-aaaa-records">Proxied A and AAAA records</h2>
<p>After proxying (orange clouding) a Secondary DNS record, any additional records under that hostname transferred from the primary DNS provider are automatically proxied. This applies to all A and AAAA records under that domain.</p>
<h2 id="cname-record-on-the-zone-apex">CNAME record on the zone apex</h2>
<p>You can also add a CNAME record on the zone apex (supported through <a href="/dns/cname-flattening/">CNAME Flattening</a>) and either proxy that record or keep it on DNS Only.</p>
<p>Once you create a CNAME record at the apex, existing A or AAAA records on the zone apex will be deactivated. You can view those deactivated records by clicking <strong>View Inactive Records</strong>. To re-activate the A or AAAA records at the root, remove the CNAME record.</p>
<h2 id="verify-that-your-records-are-proxied">Verify that your records are proxied</h2>
<p>Query DNS at your assigned Secondary DNS nameserver to confirm the DNS response Cloudflare returns. Records proxied by Cloudflare return <a href="https://www.cloudflare.com/ips/">Cloudflare IPs</a>.</p>
