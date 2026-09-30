<p>This article presents examples of queries you can use to populate your own dashboard.</p>
<ul>
<li><a href="#parameters-and-filters">Parameters and filters</a></li>
<li><a href="#timeseries-graph">Timeseries graph</a></li>
<li><a href="#activity-log">Activity log</a></li>
<li><a href="#top-n-cards---source">Top N cards - source</a></li>
<li><a href="#top-n-cards---destination">Top N cards - destination</a></li>
<li><a href="#tcp-flags">TCP Flags</a></li>
<li><a href="#executive-summary">Executive summary</a></li>
</ul>
<p>Use this workflow to build and test queries:</p>
<ul>
<li>Install and configure the <a href="https://www.gatsbyjs.com/docs/how-to/querying-data/running-queries-with-graphiql/">GraphiQL</a> app to authenticate to the Cloudflare Analytics GraphQL API. Cloudflare recommends token authentication. Refer to <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">Configure an Analytics API token</a>, for more information.</li>
<li>Construct the queries in the GraphiQL. You can use the introspective documentation in the GraphQL client to explore the nodes available. For further information about queries, refer to <a href="/analytics/graphql-api/getting-started/querying-basics/">Querying basics</a>.</li>
<li>Test your queries by running them from GraphiQL or by passing them as the payload in a cURL request to the GraphQL API endpoint.</li>
<li>Use the queries in your application to provide data for your dashboard widgets.</li>
</ul>
<h2 id="parameters-and-filters">Parameters and filters</h2>
<p>These examples use the account ID for the Cloudflare account that you are querying. You can define this as a variable (<code>accountTag</code>) and reference it in your queries.</p>
<p>The queries also use a filter to specify the time interval that you want to query. The filter uses a start time and end time to define the time interval. You use different attributes to specify the start and end times, depending on the time period that you want to query. Refer to <a href="/analytics/graphql-api/features/filtering/">Filtering</a> for further information about filters.</p>
<p>The following example queries for data with dates greater than or equal to <code>date_geq</code> and less than or equal to <code>date_leq</code>:</p>
<pre><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;{account-id}&quot;,&#10;	&quot;filter&quot;: {&#10;		&quot;AND&quot;: [{ &quot;date_geq&quot;: &quot;2020-01-19&quot; }, { &quot;date_leq&quot;: &quot;2020-01-20&quot; }]&#10;	}&#10;}&#10;</code></pre>
<p>This table lists Network Analytics datasets (nodes) and the <code>datetimeDimension</code> that you should use when querying data for a given time selection.</p>
<p>When you want an aggregated view of data, use the <code>Groups</code> query nodes. For example, the <code>ipFlows1mAttacksGroups</code> dataset represents minute-wise rollup reports of attack activity. For more detail, refer to <a href="/analytics/graphql-api/features/data-sets/">Datasets</a>.</p>
<table>
<thead>
<tr>
<th>
				<strong>Time Selection</strong>
</th>
<th>
				<strong>Query node</strong>
</th>
<th>
				<strong>datetimeDimension</strong>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>Last week</td>
<td>ipFlows1dGroups</td>
<td>date</td>
</tr>
<tr>
<td>Last month</td>
<td>ipFlows1dGroups</td>
<td>date</td>
</tr>
<tr>
<td>24 hours</td>
<td>ipFlows1mGroups</td>
<td>datetimeFifteenMinutes</td>
</tr>
<tr>
<td>12 hours</td>
<td>ipFlows1mGroups</td>
<td>datetimeFifteenMinutes</td>
</tr>
<tr>
<td>6 hours</td>
<td>ipFlows1mGroups</td>
<td>datetimeFiveMinutes</td>
</tr>
<tr>
<td>30 mins</td>
<td>ipFlows1mGroups</td>
<td>datetimeMinute</td>
</tr>
<tr>
<td>Custom range</td>
<td>Dependent on range selected</td>
<td>Dependent on range selected</td>
</tr>
</tbody>
</table>
<p>The table below lists the start and end time attributes that are valid for query nodes representing different time ranges.</p>
<table>
<thead>
<tr>
<th>
				<strong>Query node</strong>
</th>
<th>
				<strong>Start day / time filter</strong>
</th>
<th>
				<strong>End day / time filter</strong>
</th>
</tr>
</thead>
<tbody>
<tr>
<td>ipFlows1mGroups</td>
<td>datetimeMinute_geq</td>
<td>datetimeMinute_leq</td>
</tr>
<tr>
<td>ipFlows1mAttacksGroups</td>
<td>date_geq</td>
<td>date_leq</td>
</tr>
<tr>
<td>ipFlows1hGroups</td>
<td>datetimeHour_geq</td>
<td>datetimeHour_leq</td>
</tr>
<tr>
<td>ipFlows1dGroups</td>
<td>date_geq</td>
<td>date_leq</td>
</tr>
</tbody>
</table>
<h2 id="timeseries-graph">Timeseries graph</h2>
<p>Use the following query to build the timeseries graph in network analytics:</p>
<pre><code class="language-graphql">query ipFlowTimeseries(&#10;	$accountTag: string&#10;	$filter: AccountIpFlows1mGroupsFilter_InputObject&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			ipFlows1mGroups(&#10;				limit: 1000&#10;				filter: $filter&#10;				orderBy: datetimeMinute_ASC&#10;			) {&#10;				dimensions {&#10;					timestamp: datetimeMinute&#10;					attackMitigationType&#10;					attackId&#10;				}&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="activity-log">Activity log</h2>
<p>This query returns an activity log summarizing minute-wise rollups of attack traffic in IP flows. The query groups the data by the fields listed in the <code>dimensions</code> object.</p>
<pre><code class="language-graphql">query ipFlowEventLog(&#10;	$accountTag: string&#10;	$filter: AccountIpFlows1mAttacksGroupsFilter_InputObject&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			ipFlows1mAttacksGroups(&#10;				limit: 10&#10;				filter: $filter&#10;				orderBy: [min_datetimeMinute_ASC]&#10;			) {&#10;				dimensions {&#10;					attackId&#10;					attackDestinationIP&#10;					attackDestinationPort&#10;					attackMitigationType&#10;					attackSourcePort&#10;					attackType&#10;				}&#10;				avg {&#10;					bitsPerSecond&#10;					packetsPerSecond&#10;				}&#10;				min {&#10;					datetimeMinute&#10;					bitsPerSecond&#10;					packetsPerSecond&#10;				}&#10;				max {&#10;					datetimeMinute&#10;					bitsPerSecond&#10;					packetsPerSecond&#10;				}&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="top-n-cards-source">Top N cards - source</h2>
<p>This query returns data about the top source IPs.
The <code>limit</code> parameter controls the amount of records returned for each node. In the following code, the highlighted lines indicate where you configure <code>limit</code>.</p>
<pre><code class="language-graphql">query GetTopNBySource(&#10;    $accountTag: string&#10;    $filter: AccountIpFlows1mGroupsFilter_InputObject&#10;    $portFilter: AccountIpFlows1mGroupsFilter_InputObject&#10;  ) {&#10;    viewer {&#10;      accounts(filter: { accountTag: $accountTag }) {&#10;        topNPorts: ipFlows1mGroups(&#10;        limit: 5&#10;        filter: $portFilter&#10;        orderBy: [sum_(bits/packets)_DESC]&#10;      ) {&#10;        sum {&#10;          count: (bits/packets)&#10;        }&#10;        dimensions {&#10;          metric: sourcePort&#10;          ipProtocol&#10;        }&#10;      }&#10;      topNASN: ipFlows1mGroups(&#10;        limit: 5&#10;        filter: $filter&#10;        orderBy: [sum_(bits/packets)_DESC]&#10;      ) {&#10;        sum {&#10;          count: (bits/packets)&#10;        }&#10;        dimensions {&#10;          metric: sourceIPAsn&#10;          description: sourceIPASNDescription&#10;        }&#10;      }&#10;        topNIPs: ipFlows1mGroups(&#10;        limit: 5&#10;        filter: $filter&#10;        orderBy: [sum_(bits/packets)_DESC]&#10;      ) {&#10;        sum {&#10;          count: (bits/packets)&#10;        }&#10;        dimensions {&#10;          metric: sourceIP&#10;        }&#10;      }&#10;        topNColos: ipFlows1mGroups(&#10;          limit: 10&#10;          filter: $filter&#10;          orderBy: [sum_(bits/packets)_DESC]&#10;        ) {&#10;          sum {&#10;            count: (bits/packets)&#10;          }&#10;          dimensions {&#10;            metric: coloCity&#10;            coloCode&#10;          }&#10;        }&#10;        topNCountries: ipFlows1mGroups(&#10;          limit: 10&#10;          filter: $filter&#10;          orderBy: [sum_(bits/packets)_DESC]&#10;        ) {&#10;          sum {&#10;            count: (bits/packets)&#10;          }&#10;          dimensions {&#10;            metric: coloCountry&#10;          }&#10;        }&#10;        topNIPVersions: ipFlows1mGroups(&#10;          limit: 2&#10;          filter: $filter&#10;          orderBy: [sum_(bits/packets)_DESC]&#10;        ) {&#10;          sum {&#10;            count: (bits/packets)&#10;          }&#10;          dimensions {&#10;            metric: ipVersion&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&#10;</code></pre>
<h2 id="top-n-cards-destination">Top N cards - destination</h2>
<p>This query returns data about the top destination IPs. The <code>limit</code> parameter controls the amount of records returned. In the following code, the highlighted lines indicate that the query returns the five highest results.</p>
<pre><code class="language-graphql">query GetTopNByDestination(&#10;    $accountTag: string&#10;    $filter: AccountIpFlows1mGroupsFilter_InputObject&#10;    $portFilter: AccountIpFlows1mGroupsFilter_InputObject&#10;  ) {&#10;    viewer {&#10;      accounts(filter: { accountTag: $accountTag }) {&#10;        topNIPs: ipFlows1mGroups(&#10;          filter: $filter&#10;          limit: 5&#10;          orderBy: [sum_(bits/packets)_DESC]&#10;        ) {&#10;          sum {&#10;            count: (bits/packets)&#10;          }&#10;          dimensions {&#10;            metric: destinationIP&#10;          }&#10;        }&#10;        topNPorts: ipFlows1mGroups(&#10;          filter: $portFilter&#10;          limit: 5&#10;          orderBy: [sum_(bits/packets)_DESC]&#10;        ) {&#10;          sum {&#10;            count: (bits/packets)&#10;          }&#10;          dimensions {&#10;            metric: destinationPort&#10;            ipProtocol&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&#10;</code></pre>
<h2 id="tcp-flags">TCP Flags</h2>
<p>This query extracts the number of TCP packets from the minute-wise rollups of IP flows, and groups the results by TCP flag value. It uses <code>limit: 8</code> to display the top eight results, and presents them in descending order.</p>
<p>Add the following line to the filter to indicate that you want to view TCP data:</p>
<pre><code class="language-json">{ &quot;ipProtocol&quot;: &quot;TCP&quot; }&#10;</code></pre>
<pre><code class="language-graphql">query GetTCPFlags(&#10;    $accountTag: string&#10;    $filter: AccountIpFlows1mGroupsFilter_InputObject&#10;  ) {&#10;    viewer {&#10;      accounts(filter: { accountTag: $accountTag }) {&#10;        tcpFlags: ipFlows1mGroups(&#10;          filter: $filter&#10;          limit: 8&#10;          orderBy: [sum_(bits/packets)_DESC]&#10;        ) {&#10;          sum {&#10;            count: (bits/packets)&#10;          }&#10;          dimensions {&#10;            tcpFlags&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&#10;</code></pre>
<h2 id="executive-summary">Executive summary</h2>
<p>The executive summary query summarizes overall activity, therefore it only filters by the selected time interval, and ignores all filters applied to the analytics.
Use different queries, depending on the time interval you want to examine and what kind of traffic the account is seeing.</p>
<p>If the time interval is absolute, for example March 25th 09:00 to March 25th 17:00, then execute a query for attacks within those times. <a href="#parameters-and-filters">Use the appropriate query node</a>, for example <code>ipFlows1dGroups</code>, for the time interval.</p>
<pre><code class="language-graphql">query GetPreviousAttacks($accountTag: string, $filter: filter) {&#10;  viewer {&#10;    accounts(filter: {accountTag: $accountTag}) {&#10;      ${queryNode}(limit: 1000, filter: $filter) {&#10;        dimensions {&#10;          attackId&#10;        }&#10;        sum {&#10;          packets&#10;          bits&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>If the time interval is relative to the current time, for example the last 24 hours or the last 30 minutes, then make a query to the <code>ipFlows1mGroup</code> node to check whether there were attacks in the past five minutes. Attacks within the past five minutes are classed as ongoing: the Activity Log displays <code>Present</code>.
The query response lists the <code>attackID</code> values of ongoing attacks.</p>
<pre><code class="language-graphql">query GetOngoingAttackIds($accountTag: string, $filter: filter) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			ipFlows1mGroups(limit: 1000, filter: $filter) {&#10;				dimensions {&#10;					attackId&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>If there are ongoing attacks, query the <code>ipFlows1mAttacksGroups</code> node, filtering with the <code>attackID</code> values from the previous query. The query below returns the maximum bit and packet rates.</p>
<pre><code class="language-graphql">query GetOngoingAttacks($accountTag: string, $filter: filter) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			ipFlows1mAttacksGroups(limit: 1000, filter: $filter) {&#10;				dimensions {&#10;					attackId&#10;				}&#10;				max {&#10;					bitsPerSecond&#10;					packetsPerSecond&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>If there are no ongoing attacks, use the <code>GetPreviousAttacks</code> query to display data for attacks within an absolute time interval.</p>
