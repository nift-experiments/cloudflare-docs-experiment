<p>Refer to the following sections to learn how to manage your <a href="/dns/internal-dns/internal-zones/">internal DNS zones</a>.</p>
<h2 id="configuration-conditions">Configuration conditions</h2>
<p>When setting up internal zones, observe the following conditions:</p>
<ul>
<li>Internal zones can contain the same <a href="/dns/manage-dns-records/reference/dns-record-types/">DNS record types</a> that Cloudflare supports for public zones.</li>
<li>An internal zone can have the same name as a public zone in the same account.</li>
<li>Each internal zone can be linked to multiple <a href="/dns/internal-dns/dns-views/">views</a>.<sup>1</sup></li>
<li>There can be several internal zones with the same name in one account. However, two internal zones with the same name cannot be linked to the same view.</li>
<li>Internal zones are not subject to any top-level domain (TLD) restrictions. This means that an internal zone can be created if its TLD is not registered publicly (for example, <code>xyz.local</code>), if it is created on the TLD itself (<code>local</code>), or even if on the root (<code>.</code>).</li>
</ul>
<p><sup>1</sup> Logical groupings of internal DNS zones that are referenced by Gateway resolver policies to define how a specific query should be resolved.</p>
<h2 id="create-an-internal-zone">Create an internal zone</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7753.md")
</div></div>
<h2 id="other-api-actions">Other API actions</h2>
<p>The API endpoints to manage internal zones are the same as for managing public zones. The main difference is that the zone type must be set to <code>internal</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7748.md")
</aside>
<p>Refer to the following API documentation for details:</p>
<ul>
<li><a href="/api/resources/zones/methods/edit/">Update an internal zone</a> (<code>PATCH</code>)</li>
<li><a href="/api/resources/zones/methods/get/">Get internal zone details</a> (<code>GET</code>)</li>
<li><a href="/api/resources/zones/methods/list/">List internal zones</a> (<code>GET</code>)</li>
<li><a href="/api/resources/zones/methods/delete/">Delete an internal zone</a> (<code>DELETE</code>)</li>
</ul>
