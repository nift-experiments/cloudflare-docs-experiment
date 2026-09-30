<p>When you create a tunnel, Cloudflare generates a subdomain at <code>&lt;UUID&gt;.cfargotunnel.com</code>. You point a CNAME record at this subdomain to route traffic from your hostname to the tunnel.</p>
<p>The <code>cfargotunnel.com</code> subdomain only proxies traffic for DNS records in the same Cloudflare account. If someone discovers your tunnel UUID, they cannot create a DNS record in another account to proxy traffic through it.</p>
<h2 id="create-a-dns-record">Create a DNS record</h2>
<p>To create a DNS record for a Cloudflare Tunnel:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5286.md")
</div></div>
<p>The DNS record and the tunnel are independent. You can create DNS records that point to a tunnel that is not running. If a tunnel stops, the DNS record is not deleted — visitors will see a <code>1016</code> error.</p>
<p>You can also create multiple DNS records pointing to the same tunnel subdomain. If you route traffic from multiple hostnames to multiple services, create a CNAME entry for each hostname. All entries share the same target.</p>
<h2 id="cloudflare-settings">Cloudflare settings</h2>
<p>Published applications inherit the Cloudflare settings for their hostname, including <a href="/cache/how-to/cache-rules/">cache rules</a>, <a href="/waf/">WAF rules</a>, and other <a href="/rules/">Rules</a> configurations. You can change these settings for each hostname in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
<p>If you use a load balancer, settings are applied to the load balancer hostname instead.</p>
