<p>By default, <a href="/workers/">Workers</a> and <a href="/pages/functions/">Pages Functions</a> run in a data center closest to where the request was received. If your Worker makes requests to back-end infrastructure such as databases or APIs, it may be more performant to run that Worker closer to your back-end than the end user.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16607.md")
</div>
<p>Placement can reduce the overall latency of a Worker request by minimizing roundtrip latency of requests between your Worker and back-end services. You can achieve single-digit millisecond latency to databases, APIs, and other services running in legacy cloud infrastructure.</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Best for</th>
<th>Configuration</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Smart</strong></td>
<td>Multiple back-end services, or unknown infrastructure locations</td>
<td><code>mode = &quot;smart&quot;</code></td>
</tr>
<tr>
<td><strong>Region</strong></td>
<td>Single back-end service in a known cloud region</td>
<td><code>region</code></td>
</tr>
<tr>
<td><strong>Host</strong></td>
<td>Single back-end service not in a major cloud provider</td>
<td><code>host</code> or <code>hostname</code></td>
</tr>
</tbody>
</table>
<h2 id="understand-placement">Understand placement</h2>
<p>Consider a user in Sydney, Australia accessing an application running on Workers. This application makes multiple round trips to a database in Frankfurt, Germany.</p>
<p><img src="/assets/upstream/images/workers/platform/workers-smart-placement-disabled.png" alt="A user located in Sydney, AU connecting to a Worker in the same region which then makes multiple round trips to a database located in Frankfurt, DE. " /></p>
<p>The latency from multiple round trips between Sydney and Frankfurt adds up. By placing the Worker near the database, Cloudflare reduces the total request duration.</p>
<p><img src="/assets/upstream/images/workers/platform/workers-smart-placement-enabled.png" alt="A user located in Sydney, AU connecting to a Worker in Frankfurt, DE which then makes multiple round trips to a database also located in Frankfurt, DE. " /></p>
<h2 id="enable-smart-placement">Enable Smart Placement</h2>
<p>Smart Placement automatically analyzes your Worker's traffic patterns and places it in an optimal location. Use Smart Placement when:</p>
<ul>
<li>Your Worker connects to multiple back-end services</li>
<li>You do not know the exact location of your infrastructure</li>
<li>Your back-end services are distributed or replicated</li>
</ul>
<p>Smart Placement is enabled on a per-Worker basis. Once enabled, it analyzes the <a href="/workers/observability/metrics-and-analytics/#request-duration">request duration</a> of the Worker in different Cloudflare locations on a regular basis.</p>
<p>For each candidate location, Smart Placement considers the Worker's performance and the network latency added by forwarding the request. If a candidate location is significantly faster, the request is forwarded there. Otherwise, the Worker runs in the default location closest to the request.</p>
<p>Smart Placement only considers locations where the Worker has previously run. It cannot place your Worker in a location that does not normally receive traffic.</p>
<h3 id="review-limitations">Review limitations</h3>
<ul>
<li>Smart Placement only affects the execution of <a href="/workers/runtime-apis/handlers/fetch/">fetch event handlers</a>. It does not affect <a href="/workers/runtime-apis/rpc/">RPC methods</a> or <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">named entrypoints</a>.</li>
<li>Workers without a fetch event handler are ignored by Smart Placement.</li>
<li><a href="/workers/static-assets/">Static assets</a> are always served from the location nearest to the incoming request. If your code retrieves assets via the <a href="/workers/static-assets/binding/">static assets binding</a>, assets are served from the location where your Worker runs.</li>
</ul>
<h3 id="enable-smart-placement-1">Enable smart placement</h3>
<p>Smart Placement is available on all Workers plans.</p>
<h4 id="configure-with-wrangler">Configure with Wrangler</h4>
<p>Add the following to your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16608.md")
</div>
<p>Smart Placement may take up to 15 minutes to analyze your Worker after deployment.</p>
<h4 id="configure-in-the-dashboard">Configure in the dashboard</h4>
<ol>
<li>Go to <strong>Workers &amp; Pages</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>General</strong>.</li>
<li>Under <strong>Placement</strong>, select <strong>Smart</strong>.</li>
</ol>
<p>Smart Placement requires consistent traffic to the Worker from multiple locations to make a placement decision. The analysis process may take up to 15 minutes.</p>
<h3 id="check-placement-status">Check placement status</h3>
<p>Query your Worker's placement status through the Workers API:</p>
<pre><code class="language-bash">curl -X GET https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/services/$WORKER_NAME \&#10;&#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;&#45;H &quot;Content-Type: application/json&quot; | jq .&#10;</code></pre>
<p>Possible placement states:</p>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>(not present)</em></td>
<td>The Worker has not been analyzed yet. It runs in the default location closest to the request.</td>
</tr>
<tr>
<td><code>SUCCESS</code></td>
<td>The Worker was analyzed and will be optimized by Smart Placement.</td>
</tr>
<tr>
<td><code>INSUFFICIENT_INVOCATIONS</code></td>
<td>The Worker has not received enough requests from multiple locations to make a placement decision.</td>
</tr>
<tr>
<td><code>UNSUPPORTED_APPLICATION</code></td>
<td>Smart Placement made the Worker slower and reverted the placement. This state is rare (fewer than 1% of Workers).</td>
</tr>
</tbody>
</table>
<h3 id="review-request-duration-analytics">Review request duration analytics</h3>
<p>Once Smart Placement is enabled, data about request duration is collected. Request duration is measured at the data center closest to the end user. By default, 1% of requests are not routed with Smart Placement to serve as a baseline for comparison.</p>
<p>View your Worker's <a href="/workers/observability/metrics-and-analytics/#request-duration">request duration analytics</a> to measure the impact of Smart Placement.</p>
<h3 id="check-the-cf-placement-header">Check the <code>cf-placement</code> header</h3>
<p>Cloudflare adds a <code>cf-placement</code> header to all requests when placement is enabled. Use this header to check whether a request was routed with Smart Placement and where the Worker processed the request.</p>
<p>The header value includes a placement type and an airport code indicating the data center location:</p>
<ul>
<li><code>remote-LHR</code> — The request was routed using Smart Placement to a data center near London.</li>
<li><code>local-EWR</code> — The request was not routed using Smart Placement. The Worker ran in the default location near Newark.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16606.md")
</aside>
<h2 id="configure-explicit-placement-hints">Configure explicit Placement Hints</h2>
<p>Placement Hints let you explicitly specify where your Worker runs. Use Placement Hints when:</p>
<ul>
<li>You know the exact location of your back-end infrastructure</li>
<li>Your Worker connects to a single database, API, or service</li>
<li>Your infrastructure is single-homed (not replicated or anycasted)</li>
</ul>
<p>Examples include a primary database, a virtual machine, or a Kubernetes cluster in a specific region. Reducing round-trip latency from 20 to 30 milliseconds per query to 1 to 3 milliseconds improves response times.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16605.md")
</aside>
<h3 id="specify-a-cloud-region">Specify a cloud region</h3>
<p>If your infrastructure runs in AWS, GCP, or Azure, set the <code>placement.region</code> property using the format <code>{provider}:{region}</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16609.md")
</div>
<p>Cloudflare maps your specified cloud region to the data center with the lowest latency to that region. Cloudflare automatically adjusts placement to account for network maintenance or changes, so you do not need to specify failover regions.</p>
<h3 id="specify-a-host-endpoint">Specify a host endpoint</h3>
<p>If your infrastructure is not in a major cloud provider, you can specify an endpoint for Cloudflare to probe. Cloudflare will triangulate the position of your external host and place Workers in a nearby region.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16604.md")
</aside>
<p>Set <code>placement.host</code> to identify a layer 4 service. Cloudflare uses TCP CONNECT checks to measure latency and selects the best data center.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16610.md")
</div>
<p>Set <code>placement.hostname</code> to identify a layer 7 service. Cloudflare uses HTTP HEAD checks to measure latency and selects the best data center.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16611.md")
</div>
<p>Probes are sent from public IP ranges, not Cloudflare IP ranges. Cloudflare rechecks service location at regular intervals. These probes locate single-homed resources and do not work correctly for broadcast, anycast, multicast, or replicated resources.</p>
<h3 id="list-supported-regions">List supported regions</h3>
<p>Placement Hints support Amazon Web Services (AWS), Google Cloud Platform (GCP), and Microsoft Azure region identifiers:</p>
<table>
<thead>
<tr>
<th>Provider</th>
<th>Format</th>
<th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
<td>AWS</td>
<td><code>aws:{region}</code></td>
<td><code>aws:us-east-1</code>, <code>aws:us-west-2</code>, <code>aws:eu-central-1</code></td>
</tr>
<tr>
<td>GCP</td>
<td><code>gcp:{region}</code></td>
<td><code>gcp:us-east4</code>, <code>gcp:europe-west1</code>, <code>gcp:asia-east1</code></td>
</tr>
<tr>
<td>Azure</td>
<td><code>azure:{region}</code></td>
<td><code>azure:westeurope</code>, <code>azure:eastus</code>, <code>azure:southeastasia</code></td>
</tr>
</tbody>
</table>
<p>For a full list of region codes, refer to <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html">AWS regions</a>, <a href="https://cloud.google.com/compute/docs/regions-zones">GCP regions</a>, or <a href="https://learn.microsoft.com/en-us/azure/reliability/regions-list">Azure regions</a>.</p>
<h2 id="placement-behavior">Placement Behavior</h2>
<p>Workers placement behaves in similar fashion when either Smart Placement or Placement Hints are used. The following behavior applies to both.</p>
<h3 id="review-limitations-1">Review limitations</h3>
<p>The following limitations apply to both Smart Placement and Placement Hints:</p>
<ul>
<li>Placement only affects the execution of <a href="/workers/runtime-apis/handlers/fetch/">fetch event handlers</a>. It does not affect <a href="/workers/runtime-apis/rpc/">RPC methods</a> or <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">named entrypoints</a>.
<ul>
<li>Workers without a fetch event handler are ignored by placement.</li>
<li><a href="/workers/static-assets/">Static assets</a> are always served from the location nearest to the incoming request. If your code retrieves assets via the <a href="/workers/static-assets/binding/">static assets binding</a>, assets are served from the location where your Worker runs.</li>
</ul>
</li>
</ul>
<h3 id="cf-placement-header"><code>cf-placement</code> header</h3>
<p>Cloudflare adds a <code>cf-placement</code> header to all requests when placement is enabled. Use this header to check whether a request was routed with placement and where the Worker processed the request.</p>
<p>The header value includes a placement type and an airport code indicating the data center location:</p>
<ul>
<li><code>remote-LHR</code> — The request was routed using Smart Placement to a data center near London.</li>
<li><code>local-EWR</code> — The request was not routed using Smart Placement. The Worker ran in the default location near Newark.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16603.md")
</aside>
<h2 id="multiple-workers">Multiple Workers</h2>
<p>If you are building full-stack applications on Workers, split your edge logic (authentication, routing) and back-end logic (database queries, API calls) into separate Workers. Use <a href="/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> to connect them with type-safe RPC.</p>
<p><img src="/assets/upstream/images/workers/platform/smart-placement-service-bindings.png" alt="Smart Placement and Service Bindings" /></p>
<p>Enable placement on your back-end Worker to invoke it close to your database, while the edge Worker handles authentication close to the user.</p>
<h3 id="example-edge-authentication-with-a-placed-back-end">Example: Edge authentication with a placed back-end</h3>
<p>This example shows two Workers:</p>
<ul>
<li><code>auth-worker</code> — runs at the edge (no placement), handles authentication</li>
<li><code>app-worker</code> — placed near your database, handles data queries</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16616.md")
</div></div>
<p>The <code>auth-worker</code> runs at the edge to reject unauthorized requests quickly. Authenticated requests are forwarded via RPC to <code>app-worker</code>, which runs near your database for fast queries.</p>
<h3 id="durable-objects">Durable Objects</h3>
<p><a href="/durable-objects/">Durable Objects</a> provide automatic placement without configuration. Queries to a Durable Object's embedded <a href="/durable-objects/api/sqlite-storage-api/">SQLite database</a> are effectively <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">zero-latency</a> because compute runs in the same process as the data.</p>
<p>Do as much work as possible within the Durable Object and return a composite result, rather than making multiple round-trips from your Worker:</p>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;type Session = { id: string; user_id: string; created_at: number };&#10;type PromptHistory = {&#10;	id: string;&#10;	session_id: string;&#10;	role: string;&#10;	content: string;&#10;};&#10;&#10;export class AgentHistory extends DurableObject {&#10;	async getSessionContext(sessionId: string) {&#10;		// All queries execute with zero network latency — compute and data are colocated&#10;		const session = this.ctx.storage.sql&#10;			.exec&lt;Session&gt;(&quot;SELECT * FROM sessions WHERE id = ?&quot;, sessionId)&#10;			.one();&#10;		const prompts = this.ctx.storage.sql&#10;			.exec&lt;PromptHistory&gt;(&#10;				&quot;SELECT * FROM prompt_history WHERE session_id = ? ORDER BY created_at&quot;,&#10;				sessionId,&#10;			)&#10;			.toArray();&#10;&#10;		return { session, prompts };&#10;	}&#10;}&#10;</code></pre>
