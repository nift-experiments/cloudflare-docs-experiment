<p>This page describes expected limitations when <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/7576.md")
</div>. For further information about proxying, refer to [How Cloudflare DNS works](/fundamentals/concepts/how-cloudflare-works/).
<p>For guidance on when to proxy records and when to use DNS only, refer to <a href="/dns/proxy-status/use-cases/">Use cases</a>.</p>
<h2 id="proxy-eligibility">Proxy eligibility</h2>
<p>Only A, AAAA, and CNAME records that serve HTTP or HTTPS traffic can be proxied. Other DNS record types cannot be proxied.</p>
<p>If you encounter a <a href="/dns/manage-dns-records/reference/dns-record-types/#cname">CNAME record</a> that you cannot proxy — usually associated with another CDN provider — a proxied version of that record will cause connectivity errors. Cloudflare is purposely preventing that record from being proxied to protect you from a misconfiguration.</p>
<details class="nb-details"><summary>Non-proxiable targets</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7577.md")
</div></details>
<h3 id="pre-signed-dnssec">Pre-signed DNSSEC</h3>
<p>If you use Cloudflare as your <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">secondary DNS provider</a> and leverage <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">Secondary DNS Overrides</a> to set records to proxied, note that opting for <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/">Pre-signed DNSSEC</a> will cause Cloudflare to treat your records as DNS-only.</p>
<h2 id="ports-and-protocols">Ports and protocols</h2>
<p>To proxy HTTP/HTTPS traffic on <a href="/fundamentals/reference/network-ports/">non-standard ports</a> or to proxy a TCP or UDP based application, use <a href="/spectrum/">Cloudflare Spectrum</a>.</p>
<h2 id="pending-domains">Pending domains</h2>
<p>When you <a href="/fundamentals/manage-domains/add-site/">add a domain</a> to Cloudflare, Cloudflare protection will be in a <a href="/dns/zone-setups/reference/domain-status/">pending state</a> until we can verify ownership. This could take up to 24 hours to complete.</p>
<p>This means that DNS records — even those set to <a href="#proxy-eligibility">proxy traffic through Cloudflare</a> — will be <a href="/dns/proxy-status/#dns-only-records">DNS-only</a> until your zone has been activated and any requests to your DNS records will return your origin server's IP address.</p>
<p>If this warning is still present after 24 hours, refer to <a href="/dns/troubleshooting/">Troubleshooting</a>.</p>
<p>For enhanced security, we recommend rolling your origin IP addresses at your hosting provider after your zone has been activated. This action prevents your origin IPs from being leaked during onboarding.</p>
<h2 id="windows-authentication">Windows authentication</h2>
<p>Because Microsoft Integrated Windows Authentication, NTLM, and Kerberos violate HTTP/1.1 specifications, they are not compatible with proxied DNS records. NTLM authenticates at the TCP connection level (Layer 4), and Cloudflare does not guarantee that consecutive requests from the same client reuse the same TCP connection to the origin. This can cause repeated authentication prompts or authentication loops.</p>
