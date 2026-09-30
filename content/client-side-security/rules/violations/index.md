<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3961.md")
</aside>
<p>A rule violation occurs when a browser loads a resource that is not covered by one of your <a href="/client-side-security/rules/">content security rules</a>. For log rules, the resource loads normally but is reported. For allow rules, the browser blocks the resource.</p>
<p>Shortly after you configure content security rules, the Cloudflare dashboard will start displaying any violations of those rules. This information is available for rules with any <a href="/client-side-security/rules/#rule-actions">action</a> (<em>Allow</em> and <em>Log</em>).</p>
<p>Information about rule violations is also available via <a href="#get-rule-violations-via-graphql-api">GraphQL API</a> and <a href="#get-rule-violations-via-logpush">Logpush</a>.</p>
<h2 id="review-rule-violations-in-the-dashboard">Review rule violations in the dashboard</h2>
<p>To view rule violation information:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>(Optional) Filter by <strong>Content security rules</strong>.</li>
</ol>
<p>The displayed information includes the following:</p>
<ul>
<li>A sparkline next to the rule name, showing violations in the past seven days.</li>
<li>For content security rules with associated violations, an expandable details section for each rule, with the top resources present in violation events and a sparkline per top resource.</li>
</ul>
<h2 id="get-rule-violations-via-graphql-api">Get rule violations via GraphQL API</h2>
<p>Use the <a href="/analytics/graphql-api/">Cloudflare GraphQL API</a> to obtain rule violation information through the following dataset:</p>
<ul>
<li><code>pageShieldReportsAdaptiveGroups</code></li>
</ul>
<p>You can query the dataset for rule violations that occurred in the past 30 days.</p>
<p>Use <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a> to explore the available fields the GraphQL schema. For more information, refer to <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">Explore the GraphQL schema</a>.</p>
<p>For an introduction to GraphQL querying, refer to <a href="/analytics/graphql-api/getting-started/querying-basics/">Querying basics</a>.</p>
<h3 id="example">Example</h3>
<pre><code class="language-graphql">query PageShieldReports(&#10;	$zoneTag: string&#10;	$datetimeStart: Time&#10;	$datetimeEnd: Time&#10;) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			pageShieldReportsAdaptiveGroups(&#10;				limit: 100&#10;				orderBy: [datetime_ASC]&#10;				filter: { datetime_geq: $datetimeStart, datetime_leq: $datetimeEnd }&#10;			) {&#10;				avg {&#10;					sampleInterval&#10;				}&#10;				count&#10;				dimensions {&#10;					policyID&#10;					datetime&#10;					datetimeMinute&#10;					datetimeFiveMinutes&#10;					datetimeFifteenMinutes&#10;					datetimeHalfOfHour&#10;					datetimeHour&#10;					url&#10;					urlHost&#10;					host&#10;					resourceType&#10;					pageURL&#10;					action&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<details class="nb-details"><summary>Example curl request</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3962.md")
</div></details>
<h2 id="get-rule-violations-via-logpush">Get rule violations via Logpush</h2>
<p><a href="/logs/logpush/">Cloudflare Logpush</a> supports pushing logs to storage services, <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3963.md")
</div>, and log management providers.
<p>Information about rule violations is available in the <a href="/logs/logpush/logpush-job/datasets/zone/page_shield_events/"><code>page_shield_events</code> dataset</a>.</p>
<p>For more information on configuring Logpush jobs, refer to <a href="/logs/logpush/">Logpush</a> documentation.</p>
