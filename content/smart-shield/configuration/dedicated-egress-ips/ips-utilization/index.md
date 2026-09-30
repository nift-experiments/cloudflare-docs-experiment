<p>Use the <a href="/analytics/graphql-api/">GraphQL API</a> to get aggregate data and monitor your dedicated IPs capacity (formerly known as Aegis).</p>
<p>Each Dedicated CDN Egress IP can support 40,000 concurrent connections per origin IP port. For example, if you have one dedicated IP and two origins (A and B), this single IP can support 40,000 concurrent connections to origin A, while simultaneously supporting 40,000 concurrent connections to origin B.</p>
<p>Refer to the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API documentation</a> for further guidance, or consider the  <a href="#example">example</a> below for a quickstart.</p>
<h2 id="graphql-schema">GraphQL schema</h2>
<p>The specific schema to get Dedicated CDN Egress IPs data is called <code>aegisIpUtilizationAdaptiveGroups</code>.</p>
<p>You can get average (<code>avg</code>) or maximum (<code>max</code>) utilization values (in percentage), and use the following dimensions:</p>
<ul>
<li>
<p><code>datetimeFiveMinutes</code> <span class="nb-type">time</span></p>
<ul>
<li>Timestamp truncated to five minutes. For example, <code>2025-01-10T00:05:00Z</code>.</li>
</ul>
</li>
<li>
<p><code>popName</code> <span class="nb-type">string</span></p>
<ul>
<li>The Cloudflare point of presence (PoP). For example, <code>sjc</code>.</li>
</ul>
</li>
<li>
<p><code>egressIp</code> <span class="nb-type">string</span></p>
<ul>
<li>Your assigned Dedicated CDN Egress IP. For example, <code>192.0.2.1</code>.</li>
</ul>
</li>
<li>
<p><code>origin</code> <span class="nb-type">string</span></p>
<ul>
<li>Origin IP and port. For example, <code>203.0.113.150:443</code>.</li>
</ul>
</li>
<li>
<p><code>popUtilizationKey</code> <span class="nb-type">string</span></p>
<ul>
<li>The Cloudflare point of presence (PoP), the Dedicated CDN Egress IP, and the origin IP and port. For example, <code>sjc 192.0.2.1 203.0.113.150:443</code>.</li>
</ul>
</li>
</ul>
<h2 id="example">Example</h2>
<p>Refer to the query below to learn how to get average utilization and maximum utilization by point of presence, and filter the results.</p>
<p>You can also select the button at the bottom to use this query for your account via the <a href="https://graphql.cloudflare.com/explorer">Cloudflare GraphQL API Explorer</a>. Make sure to provide your account ID and timestamps, and replace the placeholders for <code>popName</code>, <code>egressIp</code>, and <code>origin</code> as needed.</p>
<pre><code class="language-graphql">query AegisIpUtilizationQuery(&#10;  $accountTag: string&#10;  $datetimeStart: string&#10;  $datetimeEnd: string&#10;) {&#10;  viewer {&#10;    utilization: accounts(filter: { accountTag: $accountTag }) {&#10;      avgByPopUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        avg {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;&#10;      maxByPopUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        max {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;&#10;      filterPopUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;          popName: &quot;&lt;CLOUDFLARE_POP&gt;&quot;&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        max {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;&#10;      filterIPUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;          egressIp: &quot;&lt;YOUR_EGRESS_IP&gt;&quot;&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        max {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;&#10;      filterOriginUtilization: aegisIpUtilizationAdaptiveGroups(&#10;        limit: 100&#10;        filter: {&#10;          datetimeFiveMinutes_geq: $datetimeStart&#10;          datetimeFiveMinutes_leq: $datetimeEnd&#10;          origin: &quot;&lt;ORIGIN_IP_AND_PORT&gt;&quot;&#10;        }&#10;        orderBy: [datetimeFiveMinutes_ASC]&#10;      ) {&#10;        max {&#10;          utilization&#10;        }&#10;        dimensions {&#10;          datetimeFiveMinutes&#10;          popUtilizationKey&#10;        }&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
