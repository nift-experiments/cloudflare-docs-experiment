<p>With zone custom nameservers (ZCNS), each custom nameserver name must be a subdomain of the zone where the custom nameservers are configured.</p>
<p>For example, for a zone <code>domain.test</code>, the ZCNS can be <code>ns1.domain.test</code> and <code>ns2.domain.test</code> but they cannot use a different TLD (<code>ns1.domain.org</code>) nor a different domain (<code>ns1.example.com</code>).</p>
<h2 id="availability">Availability</h2>
<p>Zone custom nameservers are available for zones on Business or Enterprise plans. Via API or on the dashboard.</p>
<h2 id="use-zone-custom-nameservers">Use zone custom nameservers</h2>
<h3 id="primary-zones-full-setup">Primary zones (full setup)</h3>
<p>To create zone custom nameservers:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7864.md")
</div></div>
<p>Cloudflare will assign an IPv4 and an IPv6 address to each ZCNS name and automatically create the associated <code>A</code> or <code>AAAA</code> records.</p>
<p>The next step depends on whether you are using <a href="/registrar/">Cloudflare Registrar</a> for your domain:</p>
<ul>
<li>If you are using Cloudflare Registrar for your domain, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> to add the custom nameservers and IP addresses as glue records to the domain.</li>
<li>If you are not using Cloudflare Registrar for your domain, add the zone custom nameservers at your registrar as your authoritative nameservers and as glue (A and AAAA) records (<a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>). If you do not add these records, DNS lookups for your domain will fail.</li>
</ul>
<h3 id="secondary-zones">Secondary zones</h3>
<p>If you are using <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Cloudflare as a secondary DNS provider</a>, you can still set up zone custom nameservers. After following the <a href="/dns/nameservers/custom-nameservers/zone-custom-nameservers/#primary-zones-full-setup">steps above</a> to create zone custom nameservers, do the following:</p>
<ol>
<li>Get the ZCNS IPs. You can find them on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page or you can use the <a href="/api/resources/zones/methods/get/">Zone details endpoint</a> to get the <code>vanity_name_servers_ips</code>.</li>
<li>At your primary DNS provider, add <a href="/dns/manage-dns-records/reference/dns-record-types/#ns"><code>NS</code> records</a> and, on the subdomains that you used as ZCNS names, add <code>A/AAAA</code> records.</li>
<li>At your registrar, add the zone custom nameservers as your authoritative nameservers and as glue (A and AAAA) records (<a href="https://www.rfc-editor.org/rfc/rfc1912.html">RFC 1912</a>).</li>
</ol>
<h2 id="remove-zone-custom-nameservers">Remove zone custom nameservers</h2>
<p>To remove zone custom nameservers (and their associated, read-only DNS records):</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7867.md")
</div></div>
<p>Cloudflare will remove your ZCNS and their associated read-only <code>A</code> or <code>AAAA</code> records.</p>
<p>If you are not using Cloudflare Registrar for your domain, make sure to adjust your nameservers at the registrar, parent zone, or Primary DNS provider accordingly.</p>
