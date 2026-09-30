<p>For a deep-dive on how sampling at Cloudflare works, see <a href="/analytics/sampling/">Understanding sampling in Cloudflare Analytics</a>.</p>
<h2 id="overview">Overview</h2>
<p>In a small number of cases, the analytics provided on the Cloudflare dashboard and GraphQL Analytics API are based on a <strong>sample</strong> — a subset of the dataset. In these cases, Cloudflare Analytics returns an estimate derived from the sampled value. For example, suppose that during an attack the sampling rate is 10% and 5,000 events are sampled. Cloudflare will estimate 50,000 total events (5,000 × 10) and report this value in Analytics.</p>
<h2 id="sampled-datasets">Sampled datasets</h2>
<p>Cloudflare GraphQL API exposes datasets that powered by adaptive sampling. These
nodes have <strong>Adaptive</strong> in the name and can be discovered through
<a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>The presence of sampled data is also called out in the Cloudflare dashboard and
in the description of the dataset in the API.</p>
<h2 id="why-sampling-is-applied">Why sampling is applied</h2>
<p>Analytics is designed to provide requested data, at the appropriate level of detail, as quickly as possible. Sampling allows Cloudflare to deliver analytics within seconds, even when datasets scale quickly and unpredictably, such as a burst of Firewall events generated during an attack. And because the volume of underlying data is large, the value estimated from the sample should still be statistically significant – meaning you can rely on sampled data with a high degree of confidence. Without sampling, it might take several minutes or longer to answer a query — a long time to wait when validating mitigation efforts.</p>
<h2 id="types-of-sampling">Types of sampling</h2>
<h3 id="adaptive-sampling">Adaptive sampling</h3>
<p>Cloudflare almost always uses <strong>adaptive sampling</strong>, which means the sample rate fluctuates depending on the volume of data ingested or queried. If the number of records is relatively small, sampling is not used. However, as the volume of records grows larger, progressively lower sample rates are applied. Security Events (also known as Firewall Events) and the Security Event Log follow this model. Data nodes that use adaptive sampling are easy to identify by the <code>Adaptive</code> suffix in the node name, as in <code>firewallEventsAdaptive</code>.</p>
<h3 id="fixed-sampling">Fixed sampling</h3>
<p>The following data nodes are based on fixed sampling, where the sample rate does not vary:</p>
<table>
<thead>
<tr>
<th align="left">Data set</th>
<th align="right">Rate</th>
<th align="left">Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Firewall Rules Preview<br /><p><b>Nodes:</b><br /><code>firewallRulePreviewGroups</code></p></td>
<td align="right">1%</td>
<td align="left">Use with caution. A 1% sample rate does not provide accurate estimates for datasets smaller than a certain threshold, a scenario the Cloudflare dashboard calls out explicitly but the API does not.</td>
</tr>
<tr>
<td align="left">Network Analytics<br /><p><b>Nodes:</b><br /><code>ipFlows1mGroups</code><br /><code>ipFlows1hGroups</code><br /><code>ipFlows1dGroups</code><br /><code>ipFlows1mAttacksGroups</code></p></td>
<td align="right">0.012%</td>
<td align="left">Sampling rate is in terms of packet count (1 of every 8,192 packets).</td>
</tr>
</tbody>
</table>
<h2 id="access-to-raw-data">Access to raw data</h2>
<p>Because sampling is primarily adaptive and automatically adjusts to provide an accurate estimate, the sampling rate cannot be directly controlled. Enterprise customers have access to raw data via Cloudflare Logs.</p>
