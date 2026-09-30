<p>Ethereum nodes are the computers that store blockchain data and process queries. There are three types, each with different trade-offs between storage requirements and query capabilities.</p>
<h2 id="full-nodes">Full nodes</h2>
<p>Full nodes store the current state of the blockchain and validate new blocks as they are produced. Once fully synced with the network, a full node can answer queries about any current blockchain data. Full nodes do not retain every historical state — they can recalculate past states when needed, but this requires additional computation.</p>
<h2 id="light-nodes">Light nodes</h2>
<p>Light nodes store only block headers (summaries of each block) rather than the full blockchain state. They can query the Ethereum network but rely on full nodes to provide and verify the underlying data. This makes them much smaller and faster to set up, but less self-sufficient.</p>
<h2 id="archive-nodes">Archive nodes</h2>
<p>Archive nodes are full nodes that also store every historical state of the blockchain. Because they keep this data readily available in local storage, they can answer queries about past states (such as &quot;what was this account's balance at block 5,000,000?&quot;) much faster than a full node, which would need to recalculate that state.</p>
<h2 id="nodes-at-cloudflare">Nodes at Cloudflare</h2>
<p>Cloudflare's Ethereum Gateway provides access to full and archive nodes.</p>
<p>The archive nodes serve requests for the following <a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#state_methods">RPC state methods</a> when the block number parameter is before the most recent 128 blocks or the default block parameter is set to <code>earliest</code>:</p>
<ul>
<li><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getbalance">eth_getBalance</a></li>
<li><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getcode">eth_getCode</a></li>
<li><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactioncount">eth_getTransactionCount</a></li>
<li><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getstorageat">eth_getStorageAt</a></li>
<li><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_call">eth_call</a></li>
</ul>
