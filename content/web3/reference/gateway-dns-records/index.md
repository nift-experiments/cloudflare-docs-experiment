<p>Once you <a href="/web3/how-to/manage-gateways/#create-a-gateway">create a gateway</a>, Cloudflare automatically creates and adds records to your Cloudflare DNS so your gateway can receive and route traffic appropriately:</p>
<ul>
<li><strong>Ethereum gateways</strong>: Creates a <a href="/dns/proxy-status/">proxied</a> <code>CNAME</code> record pointing your hostname to <code>ethereum.cloudflare.com</code>.</li>
<li><strong>IPFS gateways</strong>: Creates a <a href="/dns/proxy-status/">proxied</a> <code>CNAME</code> record pointing your hostname to <code>ipfs.cloudflare.com</code> and a <code>TXT</code> record with the value specified for its <a href="/web3/ipfs-gateway/concepts/dnslink/#how-is-it-used-with-cloudflare">DNSLink</a>.</li>
</ul>
<p>These records cannot be edited within Cloudflare DNS. To make edits, you will have to <a href="/web3/how-to/manage-gateways/#edit-a-gateway">edit the gateway configuration</a> itself.</p>
<h2 id="existing-dns-records">Existing DNS records</h2>
<p>When you <a href="/web3/how-to/manage-gateways/#create-a-gateway">create a gateway</a> using a hostname with pre-existing DNS records, Cloudflare automatically overwrites your existing records to make them apply to your Web3 gateway.</p>
