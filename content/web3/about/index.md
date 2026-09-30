<p>Cloudflare Web3 gateways let your application interact with decentralized networks (IPFS and Ethereum) using standard HTTP requests. Instead of running your own IPFS or Ethereum node, you point your domain at Cloudflare and the gateway handles network communication on your behalf.</p>
<p>When you <a href="/web3/how-to/manage-gateways/#create-a-gateway">create a gateway</a>, Cloudflare automatically creates and adds specific <a href="/web3/reference/gateway-dns-records/">DNS records</a> to your Cloudflare account. When the hostname associated with your gateway receives requests, its DNS records route these requests to a Cloudflare Workers script that communicates with the underlying network.</p>
<p><img src="/assets/upstream/images/web3/web3-gateway-flow-diagram.png" alt="Cloudflare's Web3 gateways provide HTTP-accessible interfaces to the IPFS and Ethereum networks. For more details, continue reading." /></p>
<h2 id="read-operations">Read operations</h2>
<p>When your application sends a read request (for example, fetching a file from IPFS or querying an Ethereum account balance), the gateway checks whether the response is already cached at a nearby Cloudflare data center.</p>
<ul>
<li>If cached, the gateway returns the content immediately over HTTP, without contacting the underlying network.</li>
<li>If not cached, the gateway fetches the content from Cloudflare's own IPFS or Ethereum nodes, caches it for future requests, and returns it over HTTP.</li>
</ul>
<h2 id="write-operations">Write operations</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/91.md")
</aside>
<p>Write operations submit new data to the network. For example, sending a transaction or deploying a smart contract. The gateway forwards your request to one of Cloudflare's Ethereum nodes, which places the transaction in its mempool (a queue of pending transactions waiting to be included in a block).</p>
<p>From there, the network's validators select transactions from the mempool, group them into a block, and reach consensus on the block's validity. Once the block is accepted, it becomes part of the permanent blockchain record. The gateway returns a transaction ID so your application can track the result.</p>
