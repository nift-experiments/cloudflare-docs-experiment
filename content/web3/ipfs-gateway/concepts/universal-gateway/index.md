<p>A Universal Path gateway is a gateway without a DNSLink record. It allows users to access any content hosted on the IPFS network by specifying a CID or IPNS path in the URL.</p>
<p>This differs from a <a href="/web3/ipfs-gateway/concepts/dnslink/">restricted gateway</a>, which limits the gateway to a single piece of content (a specific CID or IPNS hostname).</p>
<h2 id="how-is-it-used-with-cloudflare">How is it used with Cloudflare?</h2>
<p>You can set up a Universal Path gateway the same way you <a href="/web3/how-to/manage-gateways/">create any gateway</a>.</p>
<p>Because a Universal Path gateway is open by default, you may want to use the <a href="/web3/how-to/manage-gateways/#update-blocklist">gateway blocklist</a> to prevent access to specific content. You can block one or more:</p>
<ul>
<li>CIDs (<code>QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB</code>)</li>
<li>IPFS content paths (<code>/ipfs/QmYwAPJzv5CZsnA625s3Xf2nemtYgPpHdWEz79ojWnPbdG/readme</code>)</li>
<li>IPNS content paths (<code>/ipns/example.com</code>)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15800.md")
</aside>
