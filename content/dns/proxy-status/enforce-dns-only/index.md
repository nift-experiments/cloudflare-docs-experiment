<p>The enforce DNS-only setting is an account-level break-glass mechanism that allows you to bypass Cloudflare's reverse proxy for all zones in your account in a single action. When enabled, Cloudflare responds to DNS queries with the underlying record content — origin IP addresses for proxied <code>A</code> and <code>AAAA</code> records, and CNAME targets for proxied <code>CNAME</code> records — instead of Cloudflare's anycast IP addresses, effectively setting all <a href="/dns/proxy-status/">proxied DNS records</a> to DNS-only without modifying the records themselves.</p>
<p>This setting is intended for emergency situations only, such as during an outage when you need to quickly route traffic directly to your origins.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7596.md")
</aside>
<h2 id="key-characteristics">Key characteristics</h2>
<ul>
<li>Account-level: Affects all zones in the account simultaneously.</li>
<li>Non-destructive: Does not modify your DNS records. Disabling the setting restores normal proxy behavior.</li>
<li>API-only: Available through the API only, not in the Cloudflare dashboard.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="auto-ttl-for-proxied-records">Auto TTL for proxied records</h3>
@markup("md", "content/.markup/bodies/7595.md")
</aside>
<h2 id="zone-types">Zone types</h2>
<p>Enforce DNS-only works across all zone setup types:</p>
<ul>
<li><a href="/dns/zone-setups/full-setup/">Full setup</a>: Proxied records in the zone are generally affected, considering a few <a href="/dns/proxy-status/enforce-dns-only/#excluded">exceptions</a>.</li>
<li><a href="/dns/zone-setups/partial-setup/">Partial (CNAME) setup</a>: Proxied records in the zone are generally affected, considering a few <a href="/dns/proxy-status/enforce-dns-only/#excluded">exceptions</a>.</li>
<li><a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/">Secondary zones</a>: If Secondary DNS Overrides is enabled and you have manually set a record's proxy status to proxied, that record will be affected. This also applies to any other <code>A</code> or <code>AAAA</code> records on the same name. Refer to <a href="/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/">Secondary DNS Overrides</a> for details.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="zone-transfers-interaction">Zone transfers interaction</h3>
@markup("md", "content/.markup/bodies/7594.md")
</aside>
<h2 id="preparation">Preparation</h2>
<p>Before relying on enforce DNS-only as part of your incident response plan, you should:</p>
<ul>
<li>Verify origin server capacity: Without Cloudflare proxying, your origin servers handle all traffic directly, including traffic that Cloudflare would normally cache or filter. Ensure your infrastructure can sustain this load.</li>
<li>Review exposed record content: When enforce DNS-only is active, all origin IPs configured in proxied <code>A</code> and <code>AAAA</code> records, as well as the targets of proxied <code>CNAME</code> records, become publicly visible through DNS queries. If your origins rely on IP obscurity for security, plan accordingly.</li>
<li>Test in advance: Use the API in a staging or test account to confirm that you understand the behavior before you need it in an emergency.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="verify-ssl-certificates">Verify SSL certificates</h3>
@markup("md", "content/.markup/bodies/7593.md")
</aside>
<h2 id="enable-enforce-dns-only">Enable enforce DNS-only</h2>
<p>Use the <a href="/api/resources/dns/subresources/settings/subresources/account/methods/edit/">Update DNS Settings</a> endpoint to enable enforce DNS-only for your account:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/dns_settings \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;enforce_dns_only&quot;: true&#10;}&#x27;</code></pre>
<p>Once enabled, Cloudflare responds to DNS queries for all proxied records with the underlying record content — your configured origin IP addresses for <code>A</code> and <code>AAAA</code> records, and the configured CNAME target for <code>CNAME</code> records — instead of Cloudflare's anycast IPs.</p>
<h2 id="disable-enforce-dns-only">Disable enforce DNS-only</h2>
<p>To restore normal proxy behavior, set <code>enforce_dns_only</code> to <code>false</code>:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/dns_settings \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;enforce_dns_only&quot;: false&#10;}&#x27;</code></pre>
<p>After you disable the setting, Cloudflare resumes responding to DNS queries with anycast IP addresses for proxied records and all proxy-based features are restored.</p>
<h2 id="other-cloudflare-products">Other Cloudflare products</h2>
<p>Refer to the sections below in case you use other Cloudflare products that rely on DNS records.</p>
<h3 id="included">Included</h3>
<p>Enforce DNS-only affects the following records:</p>
<ul>
<li><a href="/load-balancing/">Load Balancing</a>: proxied LB records visible on the DNS records table but managed through the <a href="/load-balancing/load-balancers/create-load-balancer/">Load Balancing configurations</a>.</li>
<li>Proxied DNS records that match a <a href="/workers/configuration/routing/routes/">Worker route</a>.</li>
<li><a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> fallback origin: The proxied DNS record you designate as the <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin">fallback origin</a> for custom hostnames.</li>
</ul>
<h3 id="excluded">Excluded</h3>
<p>Enforce DNS-only does not affect the following records:</p>
<ul>
<li><a href="/r2/">R2</a> custom domains: Read-only proxied records added to the DNS records table when you set up <a href="/r2/buckets/public-buckets/#connect-a-bucket-to-a-custom-domain">R2 custom domains</a>.</li>
<li><a href="/spectrum/">Spectrum</a> applications: DNS records managed by the Spectrum application.</li>
<li><a href="/tunnel/">Tunnel</a>: CNAME records pointing to a tunnel subdomain. Refer to <a href="/tunnel/concepts/routing/#create-a-dns-record">Tunnel routing</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/">Cloudflare One</a> for details.</li>
<li><a href="/web3/">Web3 gateways</a>: Read-only proxied records managed by the <a href="/web3/reference/gateway-dns-records/">Web3 gateway configuration</a>.</li>
<li><a href="/workers/">Workers</a> custom domains: Read-only proxied records added to the DNS records table when you set up Workers <a href="/workers/configuration/routing/custom-domains/">custom domains</a>.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-domain-or-route-match">Custom domain or route match</h3>
@markup("md", "content/.markup/bodies/7592.md")
</aside>
<h2 id="what-to-expect">What to expect</h2>
<ul>
<li>Changes take effect immediately at Cloudflare's edge — there is no DNS propagation delay.</li>
<li>Functionally equivalent to setting all proxied records to DNS-only.</li>
</ul>
<h2 id="check-current-status">Check current status</h2>
<p>Use the <a href="/api/resources/dns/subresources/settings/subresources/account/methods/get/">Show DNS Settings</a> endpoint to verify the current value:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/dns_settings \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/dns/proxy-status/">Proxy status</a> - Understand how proxied and DNS-only records behave.</li>
<li><a href="/dns/manage-dns-records/how-to/batch-record-changes/#edit-proxy-status-in-bulk">Batch record changes</a> - Change proxy status for multiple records in bulk within a single zone.</li>
</ul>
