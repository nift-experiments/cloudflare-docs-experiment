<p>Use the GraphQL Analytics API to retrieve Network Flow (formerly Magic Network Monitoring) <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10801.md")
</div>.
<p>Before you begin, you must have an <a href="/analytics/graphql-api/getting-started/authentication/">API token</a>. For additional help getting started with GraphQL Analytics, refer to <a href="/analytics/graphql-api/">GraphQL Analytics API</a>.</p>
<h3 id="obtain-your-cloudflare-account-id">Obtain your Cloudflare Account ID</h3>
<p>To query Network Flow data via GraphQL, you need your Cloudflare Account ID.</p>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>The URL in your browser's address bar should show <code>https://dash.cloudflare.com/</code> followed by a hex string. The hex string is your Cloudflare Account ID.</li>
</ol>
<h2 id="explore-graphql-schema-with-network-flow-example">Explore GraphQL schema with Network Flow example</h2>
<p>Run a test query to retrieve bits and packets aggregated in five-minute intervals. Copy and paste the following code into GraphiQL.</p>
<p>For additional information about the Analytics schema, refer to <a href="/analytics/graphql-api/getting-started/explore-graphql-schema/">Explore the Analytics schema with GraphiQL</a>.</p>
<pre><code class="language-graphql">query MagicNetworkMonitoring($accountTag: string!, $start: Time, $end: Time) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			mnmFlowDataAdaptiveGroups(&#10;				filter: { datetime_gt: $start, datetime_leq: $end }&#10;				limit: 10&#10;				orderBy: [datetimeFiveMinutes_DESC]&#10;			) {&#10;				sum {&#10;					bits&#10;					packets&#10;				}&#10;				dimensions {&#10;					datetimeFiveMinutes&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10800.md")
</aside>
