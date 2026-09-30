<p>Cache Reserve Analytics provides insights regarding your Cache Reserve usage. It allows you to check what content is stored in Cache Reserve, how often it is being accessed, how long it has been there and how much egress from your origin it is saving you.</p>
<p>You have access to the following metrics:</p>
<ul>
<li><strong>Egress savings (bandwidth)</strong> - is an estimation based on response bytes served from Cache Reserve that did not need to be served from your origin server. These are represented as cache hits.</li>
<li><strong>Requests served by Cache Reserve</strong> - is the number of requests served by Cache Reserve (total).</li>
<li><strong>Data storage summary</strong> - is based on a representative sample of requests. Refer to <a href="/analytics/graphql-api/sampling/">Sampling</a> for more details about how Cloudflare samples data.
<ul>
<li><strong>Current data stored</strong> - is the data stored (currently) over time.</li>
<li><strong>Aggregate storage usage</strong> - is the total of storage used for the selected timestamp.</li>
</ul>
</li>
<li><strong>Operations</strong> - Class A (writes) and Class B (reads) operations over time.</li>
</ul>
