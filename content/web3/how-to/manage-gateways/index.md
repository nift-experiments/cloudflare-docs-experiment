<p>A Cloudflare Web3 gateway provides HTTP-accessible interfaces to various Web3 networks. You can interact with a gateway in several ways.</p>
<h2 id="create-a-gateway">Create a gateway</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15784.md")
</div></div>
<p>When you create a gateway, Cloudflare automatically:</p>
<ul>
<li>Creates and adds <a href="/web3/reference/gateway-dns-records/">records to your Cloudflare DNS</a> so your gateway can receive and route traffic appropriately.</li>
<li><a href="/dns/proxy-status/">Proxies</a> traffic to that hostname.</li>
<li>Issues an SSL/TLS certificate to cover the specified hostname.</li>
</ul>
<hr />
<h2 id="edit-a-gateway">Edit a gateway</h2>
<p>Once you have <a href="#create-a-gateway">created a gateway</a>, you can only edit the <strong>Gateway Description</strong> and — if it is an <strong>IPFS</strong> gateway — also edit the value for the <a href="/web3/ipfs-gateway/concepts/dnslink/">DNSLink</a> field.</p>
<p>If you need to edit other fields, <a href="#delete-a-gateway">delete the gateway</a> and create a new one.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15787.md")
</div></div>
<hr />
<h2 id="refresh-a-gateway">Refresh a gateway</h2>
<p>When your gateway is stuck in an <strong>Error</strong> <a href="/web3/reference/gateway-status/">status</a>, you should try refreshing the gateway, which attempts to re-create the associated DNS records for the hostname.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15790.md")
</div></div>
<hr />
<h2 id="update-blocklist">Update blocklist</h2>
<p>When you set up a <a href="/web3/ipfs-gateway/concepts/universal-gateway/">IPFS Universal Path gateway</a>, you may want to add items to the gateway blocklist, which allows you to block access to specific content.</p>
<p>You have the ability to block access to one or more:</p>
<ul>
<li>CIDs (<code>QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB</code>)</li>
<li>IPFS content paths (<code>/ipfs/QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/readme</code>)</li>
<li>IPNS content paths (<code>/ipns/example.com</code>)</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15793.md")
</div></div>
<hr />
<h2 id="delete-a-gateway">Delete a gateway</h2>
<p>When you delete a gateway, Cloudflare will automatically remove all associated hostname DNS records. This action will impact your traffic and cannot be undone.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15796.md")
</div></div>
