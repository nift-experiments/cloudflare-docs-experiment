<p>The full list of API methods that are supported by an Ethereum Gateway
is given below. The gateway returns a <code>403</code> if a method is specified that is not
supported.</p>
<p>For a full list of JSON-RPC API methods, refer to the <a href="https://github.com/ethereum/execution-apis">JSON-RPC specification</a>.</p>
<table>
<thead>
<tr>
<th>JSON-RPC method</th>
<th align="center">Cloudflare Ethereum Gateway support</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#web3_clientversion">web3_clientVersion</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#web3_sha3">web3_sha3</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#net_version">net_version</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#net_listening">net_listening</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_syncing">eth_syncing</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_mining">eth_mining</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gasprice">eth_gasPrice</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://github.com/ethereum/execution-apis">eth_feeHistory</a><sup><a href="#footnote-2">2</a></sup></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_blocknumber">eth_blockNumber</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://github.com/ethereum/execution-apis">eth_chainId</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getbalance">eth_getBalance</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getstorageat">eth_getStorageAt</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactioncount">eth_getTransactionCount</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getblocktransactioncountbyhash">eth_getBlockTransactionCountByHash</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getblocktransactioncountbynumber">eth_getBlockTransactionCountByNumber</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getunclecountbyblockhash">eth_getUncleCountByBlockHash</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getunclecountbyblocknumber">eth_getUncleCountByBlockNumber</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getcode">eth_getCode</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_sendrawtransaction">eth_sendRawTransaction</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_call">eth_call</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_estimategas">eth_estimateGas</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getblockbyhash">eth_getBlockByHash</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getblockbynumber">eth_getBlockByNumber</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactionbyhash">eth_getTransactionByHash</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactionbyblockhashandindex">eth_getTransactionByBlockHashAndIndex</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactionbyblocknumberandindex">eth_getTransactionByBlockNumberAndIndex</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_gettransactionreceipt">eth_getTransactionReceipt</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getunclebyblockhashandindex">eth_getUncleByBlockHashAndIndex</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getunclebyblocknumberandindex">eth_getUncleByBlockNumberAndIndex</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getlogs">eth_getLogs</a><sup><a href="#footnote-1">1</a></sup></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getwork">eth_getWork</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.github.io/execution-apis/api-documentation/">eth_getProof</a></td>
<td align="center">✅</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#net_peercount">net_peerCount</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_protocolversion">eth_protocolVersion</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_coinbase">eth_coinbase</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_hashrate">eth_hashrate</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_accounts">eth_accounts</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_sign">eth_sign</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_sendtransaction">eth_sendTransaction</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getcompilers">eth_getCompilers</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_compilelll">eth_compileLLL</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_compile_solidity">eth_compileSolidity</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_compileserpent">eth_compileSerpent</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_newfilter">eth_newFilter</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_newblockfilter">eth_newBlockFilter</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_newpendingtransactionfilter">eth_newPendingTransactionFilter</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_uninstallfilter">eth_uninstallFilter</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getfilterchanges">eth_getFilterChanges</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_getfilterlogs">eth_getFilterLogs</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_submitwork">eth_submitWork</a></td>
<td align="center">❌</td>
</tr>
<tr>
<td><a href="https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_submithashrate">eth_submitHashrate</a></td>
<td align="center">❌</td>
</tr>
</tbody>
</table>
<h2 id="trace-methods">Trace methods</h2>
<p>EVM traces are a way to track the execution of smart contracts on the Ethereum blockchain. It records all the steps taken by the Ethereum Virtual Machine (EVM) as it runs the smart contract. This includes information like the specific operation that was executed, how much gas it cost, and any changes made to the blockchain as a result. The trace module is a tool that allows developers to access and analyze these traces, which can be useful for debugging, testing, and monitoring smart contracts. It can be used to identify and fix errors, optimize performance, and gain insight into how the smart contract is interacting with the blockchain.</p>
<h3 id="trace-filter">trace_filter</h3>
<p>The <code>trace_filter</code> method retrieves the traces of multiple transactions in a single request. This method is particularly useful for debugging and monitoring specific addresses on the Ethereum blockchain.</p>
<h4 id="request-parameters">Request Parameters</h4>
<ul>
<li><code>fromBlock</code>: <code>Quantity</code> or <code>Tag</code> - (optional) The block number to start receiving traces from.</li>
<li><code>toBlock</code>: <code>Quantity</code> or <code>Tag</code> - (optional) The block number to stop receiving traces at.</li>
<li><code>fromAddress</code>: <code>Array</code> - (optional) An array of addresses to start receiving traces from.</li>
<li><code>toAddress</code>: <code>Address</code> - (optional) An array of addresses to stop retrieving traces at.</li>
<li><code>after</code>: <code>Quantity</code> - (optional) The offset trace number</li>
<li><code>count</code>: <code>Quantity</code> - (optional) The amount of traces to return.</li>
</ul>
<h4 id="returns">Returns</h4>
<p>This method returns an <code>Array</code> of traces matching the given filter.</p>
<h4 id="example">Example</h4>
<pre><code class="language-sh">curl https://web3-trial.cloudflare-eth.com/v1/mainnet \&#10;&#45;X POST \&#10;&#45;H &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;    &quot;jsonrpc&quot;:&quot;2.0&quot;,&#10;    &quot;method&quot;:&quot;trace_filter&quot;,&#10;    &quot;params&quot;:[&#10;        {&#10;            &quot;count&quot;: 200,&#10;            &quot;fromBlock&quot;: &quot;0xccb943&quot;,&#10;            &quot;toBlock&quot;: &quot;0xccbc62&quot;,&#10;            &quot;fromAddress&quot;: [&#10;                &quot;0xEdC763b3e418cD14767b3Be02b667619a6374076&quot;&#10;            ]&#10;        }&#10;    ],&#10;    &quot;id&quot;:1&#10;    }&#x27;&#10;</code></pre>
<h4 id="response">Response</h4>
<pre><code class="language-json">{&#10;	&quot;jsonrpc&quot;: &quot;2.0&quot;,&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;action&quot;: {&#10;				&quot;from&quot;: &quot;0xedc763b3e418cd14767b3be02b667619a6374076&quot;,&#10;				&quot;callType&quot;: &quot;call&quot;,&#10;				&quot;gas&quot;: &quot;0x8462&quot;,&#10;				&quot;input&quot;: &quot;0x095ea7b30000000000000000000000007a250d5630b4cf539739df2c5dacb4c659f2488dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff&quot;,&#10;				&quot;to&quot;: &quot;0x7ff4169a6b5122b664c51c95727d87750ec07c84&quot;,&#10;				&quot;value&quot;: &quot;0x0&quot;&#10;			},&#10;			&quot;blockHash&quot;: &quot;0x351e7c06ec010c8f7e7358eb580238dd23e1e129be96822aa93ebb6da08558e6&quot;,&#10;			&quot;blockNumber&quot;: 13416771,&#10;			&quot;result&quot;: {&#10;				&quot;gasUsed&quot;: &quot;0x6009&quot;,&#10;				&quot;output&quot;: &quot;0x0000000000000000000000000000000000000000000000000000000000000001&quot;&#10;			},&#10;			&quot;subtraces&quot;: 0,&#10;			&quot;traceAddress&quot;: [],&#10;			&quot;transactionHash&quot;: &quot;0x054bbb9fbb855bf23f755e548c7409f45fc5eff8a824b2ad06380bc038d7b049&quot;,&#10;			&quot;transactionPosition&quot;: 54,&#10;			&quot;type&quot;: &quot;call&quot;&#10;		}&#10;	],&#10;	&quot;id&quot;: 1&#10;}&#10;</code></pre>
<h3 id="limitations">Limitations</h3>
<p>The <code>trace_filter</code> method has some limitations to ensure that our nodes are not overloaded.</p>
<ul>
<li>The block range for the <code>trace_filter</code> method is limited to 800 blocks.</li>
<li>The trace <code>count</code> is limited to 200</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">**Limitations**: Max block range of 800 blocks.</li>
<li id="footnote-2">**Limitations**: Max block count of 10.</li></ol></section>
