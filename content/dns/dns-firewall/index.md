<div class="nb-description">
@markup("md", "content/.markup/bodies/7702.md")
</div>
<div class="nb-plan">
<p>Enterprise-only paid add-on</p>
</div>
<p>Cloudflare DNS Firewall proxies all DNS queries to your nameservers through Cloudflare’s global network. This action protects upstream nameservers from DDoS attacks and reduces load by caching DNS responses.</p>
<p><img src="/assets/upstream/images/dns/dns-firewall-overview.png" alt="Diagram showing protection provided by DNS Firewall. For more details, read further." /></p>
<p>DNS Firewall is for customers who need to speed up and protect entire authoritative nameservers. If you need to speed up and protect individual zones, refer to Cloudflare DNS <a href="/dns/zone-setups/">Setups</a>.</p>
<hr />
<h2 id="how-dns-firewall-works">How DNS Firewall works</h2>
<p>When a DNS query for your domain takes place:</p>
<ol>
<li>Queries go to the Cloudflare data center that is closest to the website visitor. This is determined by the location of the DNS resolver.</li>
<li>Cloudflare tries to return a DNS response from cache.</li>
<li>If the response is not available in cache, Cloudflare queries the upstream authoritative nameservers.</li>
<li>After returning the response from the nameservers, Cloudflare temporarily caches it for subsequent DNS queries.</li>
</ol>
<hr />
<h2 id="benefits">Benefits</h2>
<p>DNS Firewall provides the following benefits while allowing your organization total control over your authoritative nameservers:</p>
<ul>
<li>DDoS mitigation</li>
<li>High availability</li>
<li>Global distribution</li>
<li>Enhanced performance</li>
<li>Bandwidth savings</li>
<li><a href="/dns/dns-firewall/setup/#additional-options">Rate limiting per data center</a></li>
<li>Minimum and maximum cache TTL specification</li>
<li>DNS <a href="https://datatracker.ietf.org/doc/html/rfc8482">ANY</a> query type block</li>
</ul>
