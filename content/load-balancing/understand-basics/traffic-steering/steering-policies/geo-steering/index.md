<p><strong>Geo steering</strong> directs traffic to pools tied to specific countries, regions, or — for Enterprise customers only — data centers.</p>
<p>This option is extremely useful when you want site visitors to access the endpoint closest to them, which improves page-loading performance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10456.md")
</aside>
<h2 id="pool-assignment">Pool assignment</h2>
<p>You can assign multiple pools to the same area and the load balancer will use them in failover order. Any options not explicitly defined — whether in data centers, countries, or regions — will fall back to using default pools and failover.</p>
<h3 id="region-steering">Region steering</h3>
<p>Cloudflare has <a href="/load-balancing/reference/region-mapping-api/#list-of-load-balancer-regions">13 geographic regions</a> that span the world. The region of a client is determined by the region of the Cloudflare data center that answers the client’s DNS query.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10455.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10459.md")
</div></div>
<h3 id="country-steering">Country steering</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10462.md")
</div></div>
<h3 id="pop-steering">PoP steering</h3>
<p>When creating a load balancer <a href="/api/resources/load_balancers/methods/create/">via the API</a>, include the <code>pop_pools</code> object to map Cloudflare data centers to a list of pool IDs (ordered by their failover priority).</p>
<p>For help finding data center identifiers, refer to <a href="https://community.cloudflare.com/t/is-there-a-way-to-retrieve-cloudflare-pops-list-and-locations-programmatically/234643">this community thread</a>.</p>
<p>Any data center not explicitly defined will fall back to using the corresponding <code>country_pool</code>, then <code>region_pool</code> mapping (if it exists), and finally to associated default pools.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10454.md")
</aside>
<h3 id="failover-behavior">Failover behavior</h3>
<p>A fallback pool will be used if there is only one pool in the same region and it is unavailable.
If there are multiple pools in the same region, the order of the pools will be respected. For example, if the first pool is unavailable, the second pool will be used.</p>
