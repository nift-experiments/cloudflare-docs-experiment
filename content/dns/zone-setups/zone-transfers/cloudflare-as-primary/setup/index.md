<p>With <a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/">outgoing zone transfers</a>, you can keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure your account team has enabled your zone for outgoing zone transfers.</p>
<p>Consider the <a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/">expected behaviors</a> for different record types, and review your <a href="/dns/manage-dns-records/how-to/create-dns-records/">existing DNS records</a> to make sure all of them have the desired <strong>Proxy status</strong>.</p>
<p>If using the API, you may also want to <a href="/fundamentals/account/find-account-and-zone-ids/">locate your Zone and Account IDs</a>.</p>
<hr />
<h2 id="1-create-tsig-optional"><ol>
<li>Create TSIG (optional)</li>
</ol></h2>
<p>A Transaction Signature (TSIG) authenticates communication between a primary and secondary DNS server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8063.md")
</aside>
<p>While optional, this step is highly recommended.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8066.md")
</div></div>
<h2 id="2-create-peer-dns-server-optional"><ol start="2">
<li>Create Peer DNS Server (optional)</li>
</ol></h2>
<p>You only need to create a peer DNS server if you want:</p>
<ul>
<li>Your secondary nameservers to receive <strong>NOTIFYs</strong> for changes to your Cloudflare DNS records.</li>
<li>A <strong>TSIG</strong> to sign zone transfer requests and <strong>NOTIFYs</strong>.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8069.md")
</div></div>
<h2 id="3-link-peer-to-primary-zone-optional"><ol start="3">
<li>Link peer to primary zone (optional)</li>
</ol></h2>
<p>If you previously <a href="#2-create-peer-dns-server-optional">created a peer DNS server</a>, you should link it to your primary zone.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8062.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8072.md")
</div></div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="multiple-peers-and-tsig">Multiple peers and TSIG</h3>
@markup("md", "content/.markup/bodies/8061.md")
</aside>
<h2 id="4-update-your-secondary-dns-provider"><ol start="4">
<li>Update your secondary DNS provider</li>
</ol></h2>
<p>Your secondary DNS provider should send zone transfer requests (via AXFR or IXFR) to <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/#transfer-ip">this IP</a> on port 53 and from the IP address specified in your <a href="#2-create-peer-dns-server-optional">peer configuration</a>.</p>
<p>It should also have updated <a href="/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/#allow-range">Access Control Lists (ACLs)</a> to prevent NOTIFY messages sent from Cloudflare IP ranges from being blocked.</p>
<h2 id="5-add-secondary-nameservers-within-cloudflare"><ol start="5">
<li>Add secondary nameservers within Cloudflare</li>
</ol></h2>
<p>Using the information from your secondary DNS provider, <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">create NS records</a> on your zone apex listing your secondary nameservers.</p>
<p>By default, Cloudflare ignores NS records added to the zone apex. To modify this behavior, enable <a href="/dns/nameservers/nameserver-options/#multi-provider-dns">multi-provider DNS</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8060.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8075.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8059.md")
</aside>
<h2 id="6-enable-outgoing-zone-transfers"><ol start="6">
<li>Enable outgoing zone transfers</li>
</ol></h2>
<p>When you enable outgoing zone transfers, this will send a DNS NOTIFY message to your secondary DNS provider.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8078.md")
</div></div>
<h2 id="7-add-secondary-nameservers-to-registrar"><ol start="7">
<li>Add secondary nameservers to registrar</li>
</ol></h2>
<p>At your registrar, add the nameservers of your secondary DNS provider.</p>
