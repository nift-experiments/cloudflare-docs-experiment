<p>Use the GraphQL Analytics API to review data for Cloudflare Network Firewall (formerly Magic Firewall) network traffic related to rules matching your traffic. This contains both rules you configured in the Network Firewall dashboard, and the rules managed by Cloudflare as a part of <a href="/cloudflare-network-firewall/how-to/enable-managed-rulesets/">Network Firewall Managed rules</a> and <a href="/cloudflare-network-firewall/about/ids/">Network Firewall IDS</a> features.</p>
<p>Before you begin, you must have an <a href="/analytics/graphql-api/getting-started/authentication/">API token</a>. For additional help getting started with GraphQL Analytics, refer to <a href="/analytics/graphql-api/">GraphQL Analytics API</a>.</p>
<h2 id="obtain-cloudflare-account-id">Obtain Cloudflare Account ID</h2>
<p>To construct a Network Firewall GraphQL query for an object, you will need a Cloudflare Account ID</p>
<h3 id="obtain-your-cloudflare-account-id">Obtain your Cloudflare Account ID</h3>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account.</li>
<li>The URL in your browser's address bar should show <code>https://dash.cloudflare.com/</code> followed by a hex string. The hex string is your Cloudflare Account ID.</li>
</ol>
<h3 id="obtain-the-rule-id-for-a-firewall-rule">Obtain the rule ID for a firewall rule</h3>
<p>To construct queries to gather analytics for a particular rule, you need the rule ID for each firewall rule.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <a href="https://dash.cloudflare.com/?to=/:account/network-security/magic_firewall">Firewall Policies</a> page.</li>
<li>In the <strong>Custom policies</strong> tab, locate the rule you need the rule ID for from the list and select the three dots &gt; <strong>Edit</strong>.</li>
<li>Locate the <strong>ID</strong> and select the copy button.</li>
<li>Select <strong>Cancel</strong> to return to the <strong>Firewall Policies</strong> page.</li>
</ol>
<h2 id="explore-graphql-schema-with-cloudflare-network-firewall-query-example">Explore GraphQL schema with Cloudflare Network Firewall query example</h2>
<p>In this section, you will run a test query to retrieve a five minute count of all configured Network Firewall rules within five minute intervals. You can copy and paste the code below into GraphiQL.</p>
<p>For additional information about the Analytics schema, refer to <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">Explore the Analytics schema with GraphiQL</a>.</p>
<pre><code class="language-graphql">query MagicFirewallExample($accountTag: string!, $start: Time, $end: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			magicFirewallSamplesAdaptiveGroups(&#10;				filter: { datetime_geq: $start, datetime_leq: $end }&#10;				limit: 2&#10;				orderBy: [datetimeFiveMinute_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					datetimeFiveMinute&#10;					ruleId&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h2 id="example-queries-for-cloudflare-network-firewall">Example queries for Cloudflare Network Firewall</h2>
<h3 id="obtain-analytics-for-a-specific-rule">Obtain analytics for a specific rule</h3>
<p>Use the example below to display the total number of packets and bits for the top ten suspected malicious traffic streams within the last hour. After receiving the results, you can sort by packet rates with a five minute average.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4233.md")
</aside>
<p>For each stream, display the:</p>
<ul>
<li>Source and destination IP addresses</li>
<li>Ingress Cloudflare data centers that received it</li>
<li>Total traffic volume in bits and packets received within the hour</li>
<li>Actions taken by the firewall rule</li>
</ul>
<pre><code class="language-graphql">query MagicFirewallObtainRules(&#10;	$accountId: string!&#10;	$ruleId: string&#10;	$start: Time&#10;	$end: Time&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountId }) {&#10;			magicFirewallNetworkAnalyticsAdaptiveGroups(&#10;				filter: { ruleId: $ruleId, datetime_geq: $start, datetime_leq: $end }&#10;				limit: 10&#10;				orderBy: [avg_packetRateFiveMinutes_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					coloCity&#10;					ipDestinationAddress&#10;					ipSourceAddress&#10;					outcome&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="obtain-ids-analytics">Obtain IDS analytics</h3>
<p>Use the example below to display the total number of packets and bits for the top 10 traffic streams that Network Firewall IDS has detected in the last hour.</p>
<p>By setting <code>verdict</code> to <code>drop</code> and <code>outcome</code> as <code>pass</code>, we are filtering for traffic that was marked as a detection (i.e. verdict was drop) but was not dropped (for example, outcome was <code>pass</code>). This is because currently, Network Firewall IDS only detects malicious traffic but does not drop the traffic.</p>
<p>For each stream, display the:</p>
<ul>
<li>Source and destination IP addresses.</li>
<li>Ingress Cloudflare data centers that received it.</li>
<li>Total traffic volume in bits and packets received within the hour.</li>
</ul>
<pre><code class="language-graphql">query MagicFirewallObtainIDS($accountTag: string!, $start: Time, $end: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			magicIDPSNetworkAnalyticsAdaptiveGroups(&#10;				filter: {&#10;					datetime_geq: $start&#10;					datetime_leq: $end&#10;					verdict: drop&#10;					outcome: pass&#10;				}&#10;				limit: 10&#10;				orderBy: [avg_packetRateFiveMinutes_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					coloCity&#10;					ipDestinationAddress&#10;					ipSourceAddress&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Alternatively, to inspect all traffic that was analyzed, but grouped into malicious traffic and other traffic, the example below can be used. The response will contain two entries for each five minute timestamp. <code>verdict</code> will be set to <code>drop</code> for malicious traffic, and <code>verdict</code> will be set to <code>pass</code> for traffic that did not match any of the IDS rules.</p>
<pre><code class="language-graphql">query MagicFirewallTraffic($accountTag: string!, $start: Time, $end: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			magicIDPSNetworkAnalyticsAdaptiveGroups(&#10;				filter: { datetime_geq: $start, datetime_leq: $end }&#10;				limit: 10&#10;				orderBy: [avg_packetRateFiveMinutes_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					coloCity&#10;					ipDestinationAddress&#10;					ipSourceAddress&#10;					verdict&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
