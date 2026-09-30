<p>The following facilities offer <strong>Direct CNI</strong>, a dedicated physical connection between your network equipment and Cloudflare hardware in a shared data center.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="partner-cni-and-cloud-cni">Partner CNI and Cloud CNI</h3>
@markup("md", "content/.markup/bodies/693.md")
</aside>
<p>For public peering and best-effort interconnection at additional locations, refer to <a href="https://www.peeringdb.com/net/4224">Cloudflare on PeeringDB</a>.</p>
<h2 id="available-locations">Available locations</h2>
<p>The <a href="/network-interconnect/#dataplane">v1</a> and <a href="/network-interconnect/#dataplane">v2</a> columns show the Direct CNI dataplanes offered at each facility.</p>
<p>In this table, a metro has <em>device-level diversity</em> when at least two devices of the same dataplane provide paths to the rest of the Cloudflare network without a shared single point-of-failure device.</p>
<p><code>—</code> means the dataplane is not offered at this time.</p>
<h3 id="locations-in-diverse-metros">Locations in diverse metros</h3>
<p>Values show whether a dataplane is available through one or two connectivity devices in the site. Device-level redundancy can be achieved across multiple devices in different sites, if they are in the same metro. (Between metros, Cloudflare does not yet coordinate maintenances.)</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/698.md")
</div></div>
<h3 id="locations-in-non-diverse-metros">Locations in non-diverse metros</h3>
<p><code>✓</code> means that the dataplane is offered.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/703.md")
</div></div>
