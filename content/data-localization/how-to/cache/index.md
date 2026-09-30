<p>The following sections describe how to configure Cache with Regional Services and Customer Metadata Boundary to control where cached content is stored and served from.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare) through Cloudflare and ensure that <a href="/cache/concepts/default-cache-behavior/">eligible assets</a> are cached only in-region, follow these steps for the dashboard or API configuration:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7452.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7449.md")
</aside>
<h3 id="egress-to-origin">Egress to origin</h3>
<p>Regional Services controls where user traffic is decrypted and processed within Cloudflare's network. It does not by itself guarantee the geolocation of the egress IPs used by the Cloudflare CDN when connecting to your origin server. Egress IPs to your origin are site-local IPs from the in-region data center where the request was processed.</p>
<p>If you need guaranteed egress IP geolocation — for example, to allowlist Cloudflare IPs on your origin from a specific country — use <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> in combination with Regional Services.</p>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p><a href="/cache/performance-review/cache-analytics/">Cache Analytics</a>, Generic Global Tiered Cache and Custom Tiered Cache are compatible with Customer Metadata Boundary. With Customer Metadata Boundary set to EU, the <strong>Caching</strong> &gt; <strong>Tiered Cache</strong> tab in the zone dashboard will not be populated.</p>
<p>For more information on CDN and caching, refer to the <a href="/cache/">Cache documentation</a>.</p>
