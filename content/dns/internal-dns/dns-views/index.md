<p>Internal DNS views are logical groupings of <a href="/dns/internal-dns/internal-zones/">internal DNS zones</a>. As explained in the <a href="/dns/internal-dns/#architecture-overview">architecture overview</a>, DNS views are referenced by <a href="/cloudflare-one/traffic-policies/resolver-policies/">Gateway resolver policies</a> to define how a specific query should be resolved.</p>
<p>Refer to the sections below for details on how to manage your DNS views, or consider the <a href="/dns/internal-dns/get-started/">get started</a> for a complete workflow.</p>
<h2 id="configuration-conditions">Configuration conditions</h2>
<p>When setting up DNS views, observe the following conditions:</p>
<ul>
<li>DNS views can be empty, with no <a href="/dns/internal-dns/internal-zones/">internal zones</a> linked to them.</li>
<li>A DNS view cannot contain public DNS zones.<sup>1</sup></li>
<li>Each internal DNS zone name must be unique within a given DNS view.</li>
<li>Each DNS view name must be unique within a given Cloudflare account.</li>
</ul>
<p><sup>1</sup> DNS zones that contain public DNS records and are accessible by public resolvers.</p>
<h2 id="create-a-view">Create a view</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7657.md")
</div></div>
<h2 id="delete-a-view">Delete a view</h2>
<p>DNS views can be deleted even if they still have internal zones linked to them. The internal DNS zones will continue to exist but will be unlinked once the view is deleted.</p>
<p>It is also possible to delete a DNS view that is being referenced by a Gateway resolver policy. In this case, queries matching the policy will return SERVFAIL.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7660.md")
</div></div>
<h2 id="other-api-actions">Other API actions</h2>
<ul>
<li><a href="/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/edit/">Update a DNS view</a> (<code>PATCH</code>)</li>
<li><a href="/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/get/">Get view details</a> (<code>GET</code>)</li>
<li><a href="/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/list/">List DNS views</a> (<code>GET</code>)</li>
</ul>
