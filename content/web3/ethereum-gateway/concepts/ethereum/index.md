<p>The Ethereum network is a decentralized platform for running programs called smart contracts. A smart contract is a program stored at a unique address on the network that executes automatically when triggered by a transaction. Because smart contracts run on Ethereum, they can handle any computation that a general-purpose programming language can express.</p>
<p>When a smart contract runs, every node in the network independently verifies the result. The network then reaches consensus — all nodes agree on the outcome — and the result becomes part of the permanent record.</p>
<h2 id="smart-contracts">Smart contracts</h2>
<p>Running a smart contract requires paying a fee in Ethereum's currency, ETH. This fee (called &quot;gas&quot;) compensates the network's validators for the computational work of executing your transaction and adding it to the blockchain.</p>
<p>If the smart contract transfers ETH between accounts, those balance changes are also recorded in the blockchain. The blockchain therefore represents a complete, verifiable record of the network's current state — including every account balance and every smart contract's stored data.</p>
<h2 id="addressing">Addressing</h2>
<p>Transactions are grouped into blocks, and blocks are chained together in sequence to form the blockchain — a complete history of every transaction since the network started.</p>
<p>Each block has a unique hash identifier (a long hexadecimal string like <code>0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3q</code>), and each transaction within a block has its own hash as well. You can use either hash to look up and inspect specific blocks or transactions.</p>
<p>When a new block is added, it is broadcast to every node in the network. Because all transactions are public and verifiable, the blockchain provides a transparent and accountable record of the network's state.</p>
<h2 id="read-and-write-content">Read and write content</h2>
<p>To read data from Ethereum — such as checking account balances or querying smart contract state — you need access to an Ethereum node. You can run a node yourself (for example, using <a href="https://github.com/ethereum/go-ethereum/">go-ethereum</a>) or use a gateway like Cloudflare's. Reads are performed through the <a href="https://github.com/ethereum/wiki/wiki/JSON-RPC">JSON-RPC API</a>, a standard interface for sending queries to the network.</p>
<p>To write data — such as sending a transaction or deploying a smart contract — you also use the JSON-RPC API, but you must additionally provide ETH to pay for the transaction fee and sign the transaction with the private key from your <a href="https://www.ethereum.org/use/#_3-what-is-a-wallet-and-which-one-should-i-use">Ethereum wallet</a>. Once submitted, the transaction is broadcast to the network and included in the blockchain.</p>
<h2 id="connect-your-website-to-the-gateway">Connect your website to the gateway</h2>
<p>To access the Ethereum network from a custom domain name — without running your own node — you can <a href="/web3/how-to/manage-gateways/#create-a-gateway">create an Ethereum Gateway</a> through Cloudflare.</p>
<h2 id="related-resources">Related resources</h2>
<p>If you’re interested in learning more, you can read the official <a href="https://github.com/ethereum/wiki/wiki/JSON-RPC">RPC
documentation</a>, along with the
official documentation <a href="https://www.ethereum.org/use/">provided by Ethereum</a>.</p>
