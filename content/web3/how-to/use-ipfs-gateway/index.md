<p>Once you have an IPFS gateway — meaning that you <a href="/web3/how-to/manage-gateways/#create-a-gateway">create a new gateway</a> with a <code>target</code> of <strong>IPFS</strong> — you can get data from the IPFS network by using a URL.</p>
<h2 id="read-from-the-network">Read from the network</h2>
<p>Every time you access a piece of content through Cloudflare's IPFS Gateway, you need a URL with two parts: the gateway hostname and the request path.</p>
<h3 id="gateway-hostname">Gateway hostname</h3>
<p>Your gateway hostname will be the <strong>Hostname</strong> value you supplied when you <a href="/web3/how-to/manage-gateways/#create-a-gateway">created the gateway</a>.</p>
<h3 id="request-path">Request path</h3>
<p>The request path will vary based on the type of content you are serving.</p>
<p>If a request path is <code>/ipfs/&lt;CID_HASH&gt;</code>, that tells the gateway that you want the content with the Content Identifier (CID) that immediately follows. Because the content is addressed by CID, the gateway's response is immutable and will never change. An example would be <code>https://cloudflare-ipfs.com/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/</code>, which is a mirror of Wikipedia and an immutable <code>/ipfs/</code> link.</p>
<p>If a request path is <code>/ipns/&lt;DOMAIN&gt;</code>, that tells the gateway that you want it to lookup the CID associated with a given domain in DNS and then serve whatever content corresponds to the CID it happens to find. Because DNS can change over time, so will the gateway's response. An example would be <code>https://cloudflare-ipfs.com/ipns/ipfs.tech/</code>, which is IPFS's marketing site and can be changed at any time by modifying the <a href="/web3/ipfs-gateway/concepts/dnslink/">DNSLink record</a> associated with the <code>ipfs.tech</code> domain.</p>
<h2 id="write-to-the-network">Write to the network</h2>
<p>Cloudflare's IPFS Gateway is currently limited to read-only access.</p>
