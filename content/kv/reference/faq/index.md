<p>Frequently asked questions regarding Workers KV.</p>
<h2 id="general">General</h2>
<h3 id="can-i-use-workers-kv-without-using-workers">Can I use Workers KV without using Workers?</h3>
<p>Yes, you can use Workers KV outside of Workers by using the <a href="/api/resources/kv/">REST API</a> or the associated <a href="/fundamentals/api/reference/sdks/">Cloudflare SDKs</a> for the REST API. It is important to note the <a href="/fundamentals/api/reference/limits/">limits of the REST API</a> that apply.</p>
<h3 id="what-are-the-key-considerations-when-choosing-how-to-access-kv">What are the key considerations when choosing how to access KV?</h3>
<p>When choosing how to access Workers KV, consider the following:</p>
<ul>
<li><strong>Performance</strong>: Accessing Workers KV via the <a href="/kv/api/write-key-value-pairs/">Workers Binding API</a> is generally faster than using the <a href="/api/resources/kv/">REST API</a>, as it avoids the overhead of HTTP requests.</li>
<li><strong>Rate Limits</strong>: Be aware of the different rate limits for each access method. <a href="/api/resources/kv/">REST API</a> has a lower write rate limit compared to Workers Binding API. Refer to <a href="/kv/reference/faq/#what-is-the-rate-limit-of-workers-kv">What is the rate limit of Workers KV?</a></li>
</ul>
<h3 id="why-can-i-not-immediately-see-the-updated-value-of-a-key-value-pair">Why can I not immediately see the updated value of a key-value pair?</h3>
<p>Workers KV heavily caches data across the Cloudflare network. Therefore, it is possible that you read a cached value for up to the <a href="/kv/api/read-key-value-pairs/#cachettl-parameter">cache TTL</a> duration.</p>
<h3 id="is-workers-kv-eventually-consistent-or-strongly-consistent">Is Workers KV eventually consistent or strongly consistent?</h3>
<p>Workers KV is eventually consistent.</p>
<p>Workers KV stores data in central stores and replicates the data to all Cloudflare locations through a hybrid push/pull replication approach. This means that the previous value of the key-value pair may be seen in a location for as long as the <a href="/kv/api/read-key-value-pairs/#cachettl-parameter">cache TTL</a>. This means that Workers KV is eventually consistent.</p>
<p>Refer to <a href="/kv/concepts/how-kv-works/">How KV works</a>.</p>
<h3 id="if-a-worker-makes-a-bulk-request-to-workers-kv-would-each-individual-key-get-counted-against-the-worker-subrequest-limit-of-1000-kv-platform-limits">If a Worker makes a bulk request to Workers KV, would each individual key get counted against the <a href="/kv/platform/limits/">Worker subrequest limit (of 1000)</a>?</h3>
<p>No. A bulk request to Workers KV, regardless of the amount of keys included in the request, will count as a single operation. For example, you could make
500 bulk KV requests and 500 R2 requests for a total of 1000 operations.</p>
<h3 id="what-is-the-rate-limit-of-workers-kv">What is the rate limit of Workers KV?</h3>
<p>Workers KV's rate limit differs depending on the way you access it.</p>
<p>Operations to Workers KV via the <a href="/api/resources/kv/">REST API</a> are bound by the same <a href="/fundamentals/api/reference/limits/">limits of the REST API</a>. This limit is shared across all Cloudflare REST API requests.</p>
<p>When writing to Workers KV via the <a href="/kv/api/write-key-value-pairs/">Workers Binding API</a>, the write rate limit is 1 write per second, per key, unlimited across KV keys.</p>
<h2 id="pricing">Pricing</h2>
<h3 id="when-writing-via-workers-kv-s-rest-api-api-resources-kv-subresources-namespaces-subresources-keys-methods-bulk-update-how-are-writes-charged">When writing via Workers KV's <a href="/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_update/">REST API</a>, how are writes charged?</h3>
<p>Each key-value pair in the <code>PUT</code> request is counted as a single write, identical to how each call to <code>PUT</code> in the Workers API counts as a write. Writing 5,000 keys via the REST API incurs the same write costs as making 5,000 <code>PUT</code> calls in a Worker.</p>
<h3 id="do-queries-i-issue-from-the-dashboard-or-wrangler-the-cli-count-as-billable-usage">Do queries I issue from the dashboard or wrangler (the CLI) count as billable usage?</h3>
<p>Yes, any operations via the Cloudflare dashboard or wrangler, including updating (writing) keys, deleting keys, and listing the keys in a namespace count as billable Workers KV usage.</p>
<h3 id="does-workers-kv-charge-for-data-transfer-egress">Does Workers KV charge for data transfer / egress?</h3>
<p>No.</p>
<h3 id="are-key-expirations-billed-as-delete-operations">Are key expirations billed as delete operations?</h3>
<p>No. Key expirations are not billable operations.</p>
