<p>In early 2020, Cloudflare released the first version of the Network Analytics dashboard and its corresponding API. The second version (Network Analytics v2) was made available on 2021-09-13.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3181.md")
</aside>
<h2 id="before-you-start">Before you start</h2>
<p>Learn more about the <a href="/analytics/network-analytics/understand/concepts/">concepts introduced in Network Analytics v2</a>.</p>
<h2 id="feature-comparison">Feature comparison</h2>
<p>The following table compares the features of NAv1 and NAv2:</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>NAv1</th>
<th>NAv2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sampling rate</td>
<td>1/8,192 packets</td>
<td>Varies between 1/100 and 1/1,000,000 packets,<br/> depending on the mitigation service.</td>
</tr>
<tr>
<td>Sampling method</td>
<td>Core Sample Enrichment</td>
<td>Edge Sample Enrichment</td>
</tr>
<tr>
<td>Historical data retention method</td>
<td>Aggregated roll-ups</td>
<td>Adaptive Bit Rate</td>
</tr>
<tr>
<td>Retention period</td>
<td>1-min roll-ups: 30 days<br/>1-hour roll-ups: 6 months<br/>1-day roll-ups: 1 year<br/>Attack roll-ups: 1 year</td>
<td>All nodes: 16 weeks</td>
</tr>
<tr>
<td>Attack mitigation systems</td>
<td><code>dosd</code></td>
<td><code>dosd</code>, <code>flowtrackd</code>*, and Cloudflare Network Firewall*</td>
</tr>
<tr>
<td>Examples of new fields</td>
<td>n/a</td>
<td>Rule ID<br/>GRE tunnel ID<br/>Packet size</td>
</tr>
</tbody>
</table>
<p>* <em>Applicable only for Magic Transit customers.</em></p>
<p>For more information on the differences in terms of sampling method and historical data retention, refer to <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/differences/">Main differences between Network Analytics v1 and v2</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3180.md")
</aside>
<h2 id="node-comparison">Node comparison</h2>
<p>NAv2 uses the same API endpoint but makes use of new nodes. While NAv1 has three nodes for aggregated roll-ups for all traffic and attacks, and one node for attacks, NAv2 has one node for all traffic and attacks, and four separate nodes for attacks that vary based on the mitigation system.</p>
<table>
<thead>
<tr>
<th>Node type</th>
<th>NAv1</th>
<th>NAv2 for Magic Transit</th>
<th>NAv2 for Spectrum</th>
</tr>
</thead>
<tbody>
<tr>
<td>Main node(s)</td>
<td><code>ipFlows1mGroups</code><br/><code>ipFlows1hGroups</code><br/><code>ipFlows1dGroups</code></td>
<td><code>magicTransitNetworkAnalyticsAdaptiveGroups</code></td>
<td><code>spectrumNetworkAnalyticsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Attack node(s)</td>
<td><code>ipFlows1mAttacksGroups</code></td>
<td><code>dosdNetworkAnalyticsAdaptiveGroups</code><br/> <code>dosdAttackAnalyticsGroups</code><br/> <code>flowtrackdNetworkAnalyticsAdaptiveGroups</code><br/> <code>magicFirewallNetworkAnalyticsAdaptiveGroups</code></td>
<td><code>dosdNetworkAnalyticsAdaptiveGroups</code><br/> <code>dosdAttackAnalyticsGroups</code></td>
</tr>
</tbody>
</table>
<p>Each row represents one packet sample. The data is sampled at Cloudflare’s edge at <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/">various rates</a>. You can also query the sample rate from the nodes using the <code>sample_interval</code> field.</p>
<p>For reference information on NAv2 nodes, refer to the <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/">NAv2 node reference</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="obtaining-data-for-ingress-traffic-only">Obtaining data for ingress traffic only</h3>
@markup("md", "content/.markup/bodies/3179.md")
</aside>
<h2 id="schema-comparison">Schema comparison</h2>
<p>Refer to <a href="/analytics/graphql-api/migration-guides/network-analytics-v2/schema-map/">NAv1 to NAv2 schema map</a> for a mapping of schema fields from NAv1 nodes to NAv2 nodes. Follow this recommended mapping when migrating to NAv2.</p>
<h2 id="example">Example</h2>
<p>The following example queries the top 20 logs of traffic dropped by mitigation systems different from Cloudflare Network Firewall within a given time range, ordered by destination IP address.</p>
<pre><code class="language-graphql">{&#10;	viewer {&#10;		accounts(filter: { accountTag: &quot;&lt;REDACTED&gt;&quot; }) {&#10;			magicTransitNetworkAnalyticsAdaptiveGroups(&#10;				filter: {&#10;					datetime_gt: &quot;2021-10-01T00:00:00Z&quot;&#10;					datetime_lt: &quot;2021-10-05T00:00:00Z&quot;&#10;					outcome_like: &quot;drop&quot;&#10;					mitigationSystem_neq: &quot;magic-firewall&quot;&#10;				}&#10;				limit: 20&#10;				orderBy: [ipDestinationAddress_ASC]&#10;			) {&#10;				dimensions {&#10;					outcome&#10;					mitigationSystem&#10;					ipSourceAddress&#10;					ipDestinationAddress&#10;					ipProtocol&#10;					destinationPort&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="final-remarks">Final remarks</h2>
<p>The <code>mitigationSystem</code> field can take one the following values:</p>
<ul>
<li><code>dosd</code> for <a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a> (Network-layer DDoS Attack Protection or HTTP DDoS Attack Protection).</li>
<li><code>flowtrackd</code> for <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a>.</li>
<li><code>magic-firewall</code> for <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>.</li>
<li>Empty string for unmitigated traffic.</li>
</ul>
