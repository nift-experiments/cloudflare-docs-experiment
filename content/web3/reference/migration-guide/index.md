<p>As announced in <a href="https://blog.cloudflare.com/ea-web3-gateways/">our blog post</a>, Cloudflare is deprecating legacy hostnames that point to our public gateway endpoints at <code>cloudflare-eth.com</code> and <code>cloudflare-ipfs.com</code>.</p>
<p>If you created a hostname pointing to these gateways during the <a href="https://blog.cloudflare.com/announcing-web3-gateways/">private beta</a>, you should migrate to use our new Web3 gateways to avoid a disruption in service.</p>
<hr />
<h2 id="migration-guide">Migration guide</h2>
<p>The migration is a simple process.</p>
<p>First, create a <a href="/fundamentals/account/create-account/">Cloudflare account</a>.</p>
<p>Then create a new <a href="/web3/how-to/manage-gateways/#create-a-gateway">Web3 custom gateway</a> with your existing hostname.</p>
<p>Alternatively, you could also create a <a href="/web3/how-to/manage-gateways/#create-a-gateway">Web3 custom gateway</a> for a new hostname and then modify your application to use your newly created hostname (<a href="/web3/how-to/use-ipfs-gateway/">IPFS</a> or <a href="/web3/how-to/use-ethereum-gateway/">Ethereum</a>).</p>
