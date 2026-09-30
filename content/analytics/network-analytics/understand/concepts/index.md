<h2 id="adaptive-bit-rate-sampling">Adaptive Bit Rate sampling</h2>
<p>With Adaptive Bit Rate (ABR) sampling, every analytics query that supports ABR will be calculated at a resolution matching the query. Depending on the size of your query, the ABR mechanism will choose the best sampling rate and fetch a response from one of the sample tables encapsulated behind each <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/">Network Analytics node</a>. The cardinality and accuracy are preserved even for historical data.</p>
<p>For more background information on Adaptive Bit Rate sampling, refer to the <a href="https://blog.cloudflare.com/explaining-cloudflares-abr-analytics/">Explaining Cloudflare's ABR Analytics</a> blog post.</p>
<h2 id="edge-sample-enrichment">Edge Sample Enrichment</h2>
<p>Network Analytics can provide accurate data due to the sample rate and to Edge Sample Enrichment.</p>
<p>Sample rates vary depending on the mitigation service. For example:</p>
<ul>
<li>The sample rate for <code>dosd</code> changes dynamically from 1/100 to 1/10,000 packets based on the volume of packets.</li>
<li>The sample rate for Network Firewall events changes dynamically from 1/100 to 1/1,000,000 packets based on the number of packets.</li>
<li>The sample rate for <code>flowtrackd</code> is 1/10,000 packets.</li>
</ul>
<p>NA uses a data logging pipeline that relies on Edge Sample Enrichment. By delegating the packet sample enrichment and cross-referencing to the global data centers, the data pipeline’s resilience and tolerance against congestion are improved. Using this method, enriched packet samples are immediately stored in Cloudflare's core data centers as soon as they arrive.</p>
