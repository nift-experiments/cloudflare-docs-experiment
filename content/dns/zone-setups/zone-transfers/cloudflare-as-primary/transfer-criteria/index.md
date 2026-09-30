<p>Consider the sections below to understand the expected behaviors, depending on DNS record type and proxied status.</p>
<h2 id="proxied-records">Proxied records</h2>
<p>For each <a href="/dns/proxy-status/">proxied DNS record</a> in your zone, Cloudflare will transfer out two <code>A</code> and two <code>AAAA</code> records.</p>
<p>These records correspond to the <a href="https://www.cloudflare.com/ips">Cloudflare IP addresses</a> used for proxying traffic.</p>
<h2 id="dns-only-cname-records">DNS-only CNAME records</h2>
<p>As explained in <a href="/dns/manage-dns-records/reference/dns-record-types/#cname">DNS record types</a>, Cloudflare uses a process called <a href="/dns/cname-flattening/">CNAME flattening</a> to return the final IP address instead of the CNAME target. CNAME flattening improves performance and is also what allows you to set a CNAME record on the zone apex.</p>
<p>Depending on the <a href="/dns/cname-flattening/set-up-cname-flattening/">settings</a> you have, when you use DNS-only CNAME records with outgoing zone transfers, you can expect the following:</p>
<ul>
<li>For DNS-only CNAME records on the zone apex, Cloudflare will always transfer out the flattened IP addresses.</li>
<li>For DNS-only CNAME records on subdomains, Cloudflare will only transfer out flattened IP addresses if the setting <a href="/dns/cname-flattening/set-up-cname-flattening/#for-all-cname-records"><strong>CNAME flattening for all CNAME records</strong></a> is enabled.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="per-record-cname-flattening">Per-record CNAME flattening</h3>
@markup("md", "content/.markup/bodies/8058.md")
</aside>
<h2 id="records-that-are-not-transferred">Records that are not transferred</h2>
<p>The following records are not transferred out when you use Cloudflare as primary:</p>
<ul>
<li><a href="/ssl/edge-certificates/caa-records/">CAA records</a></li>
<li>TXT records used for TLS certificate validation</li>
<li>DNS-only <a href="/load-balancing/load-balancers/dns-records/">Load Balancing</a> records</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8057.md")
</aside>
