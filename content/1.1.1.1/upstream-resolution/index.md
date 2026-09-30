<p>When 1.1.1.1 does not have an answer in its cache, it contacts authoritative nameservers on your behalf. Authoritative nameservers are the DNS servers that hold the actual records for a domain. This page describes how 1.1.1.1 selects which nameserver to query, what happens when a nameserver is unreachable, and how the final response is determined.</p>
<h2 id="query-name-minimization">Query name minimization</h2>
<p>When resolving a multi-level domain name like <code>foo.bar.example.com</code>, 1.1.1.1 does not reveal the full name to every server in the chain. Instead, it sends only the minimum information each server needs. For example, when asking the <code>.com</code> TLD server, 1.1.1.1 only discloses that it needs to find <code>example.com</code> — the subdomain parts (<code>foo.bar</code>) are not included. This limits the amount of information exposed to intermediary servers and reduces privacy leakage.</p>
<h2 id="root-zone">Root zone</h2>
<p>1.1.1.1 uses <a href="https://blog.cloudflare.com/f-root/">locally hosted copies of the root zone file</a> instead of querying remote root servers for every lookup. The root zone file contains the addresses of all top-level domain (TLD) servers. By hosting it locally, 1.1.1.1 avoids a network round trip to root servers, which reduces latency, improves privacy, and decreases load on the global DNS root server system.</p>
<h2 id="nameserver-selection">Nameserver selection</h2>
<p>Most domains have multiple authoritative nameservers for redundancy. When 1.1.1.1 needs to query one, it chooses based on measured performance. The resolver tracks metrics for each nameserver — including round-trip time (how long a query takes to travel to the server and back) and response quality — then picks the nameserver that has historically been fastest and most reliable from the data center handling your request.</p>
<p>If the selected nameserver does not respond in time or returns an error, 1.1.1.1 retries against a different nameserver for the same zone. Refer to <a href="#retry-behavior">Retry behavior</a> for details.</p>
<p>A small percentage of queries are also sent to alternative nameservers so that performance measurements stay current. This allows a previously slow server to be re-evaluated if its performance improves. For more background on the system that powers this selection, refer to the <a href="https://blog.cloudflare.com/big-pineapple-intro/">BigPineapple architecture blog post</a>.</p>
<h2 id="retry-behavior">Retry behavior</h2>
<p>If a nameserver does not respond in time or returns a temporary error, 1.1.1.1 retries the query against a different authoritative nameserver for the same zone. The unresponsive server is deprioritized so that subsequent queries prefer healthier alternatives. 1.1.1.1 periodically re-checks deprioritized servers to detect recovery.</p>
<p>When multiple clients request the same domain at the same time, 1.1.1.1 deduplicates the upstream queries so that a single in-flight request serves all waiting clients. The exact retry timing and ranking logic are tuned over time and may change.</p>
<h2 id="response-selection">Response selection</h2>
<p>For a given query, 1.1.1.1 returns only one answer to the client. When authoritative nameservers disagree, which response 1.1.1.1 selects depends on the type of responses received.</p>
<p>The following DNS response codes are relevant:</p>
<ul>
<li><strong><code>NOERROR</code></strong> — The query succeeded. The response contains the requested records, or indicates that the name exists but has no records of the requested type (sometimes called <code>NODATA</code>).</li>
<li><strong><code>NXDOMAIN</code></strong> — The domain name does not exist.</li>
<li><strong><code>SERVFAIL</code></strong> — The nameserver encountered an internal error and could not answer.</li>
<li><strong><code>REFUSED</code></strong> — The nameserver refused to answer the query.</li>
</ul>
<p>How 1.1.1.1 handles disagreements between nameservers:</p>
<ul>
<li><strong><code>NOERROR</code> versus <code>NXDOMAIN</code>:</strong> Both are valid authoritative answers. 1.1.1.1 returns whichever response it receives first and does not query remaining nameservers to compare. Authoritative nameservers for the same zone are expected to be consistent. If one returns <code>NXDOMAIN</code> and another returns <code>NOERROR</code> for the same name, that indicates a misconfiguration on the authoritative side.</li>
<li><strong>Timeout versus a valid response:</strong> A timeout is not an answer. 1.1.1.1 retries against another nameserver and returns the first valid response it receives.</li>
<li><strong><code>SERVFAIL</code> or <code>REFUSED</code> versus a valid response:</strong> Temporary failures are treated as upstream errors, not authoritative answers. 1.1.1.1 retries against another nameserver and returns the first valid response. Only if all nameservers return errors does 1.1.1.1 return a failure to the client — typically <code>SERVFAIL</code>, or <code>REFUSED</code> if that is what the nameservers consistently returned.</li>
</ul>
