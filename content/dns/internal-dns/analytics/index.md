<p>Internal DNS leverages <a href="/cloudflare-one/insights/analytics/gateway/">Gateway analytics</a>. Below you can find information about specific fields and different methods you can use to access this data.</p>
<h2 id="graphql">GraphQL</h2>
<p>For detailed metrics, use the <a href="/analytics/graphql-api/">GraphQL API</a>. Refer to the GraphQL Analytics API documentation for guidance on how to <a href="/analytics/graphql-api/getting-started/">get started</a>.</p>
<p>The <a href="/analytics/graphql-api/getting-started/querying-basics/">fields</a> added to cover Internal DNS are the following:</p>
<ul>
<li><code>InternalDNSFallbackStrategy</code>: The fallback strategy applied to the internal DNS response. Empty if no fallback strategy was applied.</li>
<li><code>InternalDNSRCode</code>: The response code sent back by the internal DNS service.</li>
<li><code>InternalDNSViewID</code>: The view identifier that was sent to the internal DNS service.</li>
<li><code>InternalDNSZoneID</code>: The internal zone identifier returned by the internal DNS service.</li>
</ul>
<h2 id="logs">Logs</h2>
<p>Leverage Logpush jobs for <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#internaldnsfallbackstrategy">Gateway DNS</a>. For help setting up Logpush, refer to <a href="/logs/logpush/">Logpush</a> documentation.</p>
<p>You can also set up <a href="/logs/logpush/logpush-job/filters/">Logpush filters</a> to only push logs related to a specific <a href="/dns/internal-dns/internal-zones/">internal zone</a> or <a href="/dns/internal-dns/dns-views/">view</a> ID.</p>
