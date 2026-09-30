<p>Organizations may lack visibility into Model Context Protocol (MCP) traffic, which can allow employees to connect to remote MCP servers outside of IT oversight. These connections risk the exfiltration of sensitive internal data and credentials, tool injection attacks or software supply chain risks.</p>
<p>As an IT administrator, you want to identify shadow MCP traffic to prevent unauthorized data exfiltration while still supporting governed use cases. In this tutorial, you will use the Cloudflare GraphQL Analytics API to scan Gateway HTTP logs for MCP traffic patterns, create DLP profiles that detect MCP JSON-RPC methods, and classify traffic to differentiate between authorized traffic sent to MCP server portals and traffic sent to &quot;shadow&quot; remote MCP servers.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account with a <a href="/cloudflare-one/setup/">Zero Trust organization</a></li>
<li><a href="/cloudflare-one/traffic-policies/">Gateway</a> with HTTP filtering enabled and actively proxying user traffic</li>
<li>An <a href="/fundamentals/api/get-started/create-token/">API token</a> with the following permissions:
<ul>
<li>Account-level <code>Zero Trust: Read</code></li>
<li>Account-level <code>DLP: Write</code></li>
<li>Account-level <code>Gateway: Write</code></li>
</ul>
</li>
<li>Your Cloudflare account ID (available in the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> under <strong>Account Home</strong>)</li>
<li>Familiarity with <a href="/analytics/graphql-api/">GraphQL Analytics API</a> queries</li>
<li>A working knowledge of TypeScript and REST APIs</li>
</ul>
<h2 id="1-review-the-gateway-http-dataset"><ol>
<li>Review the Gateway HTTP dataset</li>
</ol></h2>
<p>The <code>gatewayHttpRequestsAdaptiveGroups</code> dataset in the GraphQL Analytics API provides aggregated Gateway HTTP log data. Use this dataset to query for MCP-related traffic patterns:</p>
<ul>
<li><strong>Dimensions</strong>: <code>httpHost</code>, <code>httpRequestURI</code>, <code>action</code>, <code>users</code>, <code>dlpProfiles</code></li>
<li><strong>Time range</strong>: Up to 30 days of historical data</li>
<li><strong>Grouping</strong>: Aggregates results by dimension values</li>
<li><strong>Filtering</strong>: Supports <code>OR</code>, <code>AND</code>, and <code>like</code> operators</li>
</ul>
<h2 id="2-build-the-mcp-detection-query"><ol start="2">
<li>Build the MCP detection query</li>
</ol></h2>
<p>MCP traffic can be identified by three signals:</p>
<ol>
<li><strong>Domain patterns</strong>: Hostnames containing <code>mcp</code> (for example, <code>mcp.datadog.com</code>)</li>
<li><strong>URL paths</strong>: Standard MCP endpoints such as <code>/mcp</code>, <code>/mcp/sse</code>, and <code>/sse</code></li>
<li><strong>DLP matches</strong>: JSON-RPC methods in request bodies (covered in a later step)</li>
</ol>
<p>The following GraphQL query scans Gateway logs for the first two signals:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4306.md")
</div>
<p>Replace <code>&lt;YOUR_ACCOUNT_ID&gt;</code> with your Cloudflare account ID. Replace <code>&lt;START_DATE&gt;</code> and <code>&lt;END_DATE&gt;</code> with ISO-8601 timestamps covering your desired time range (up to 30 days).</p>
<h2 id="3-process-the-query-results"><ol start="3">
<li>Process the query results</li>
</ol></h2>
<p>Each group in the response represents aggregated traffic for a specific <code>httpHost</code> and <code>action</code> combination. Parse the results to identify unblocked MCP connections:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4307.md")
</div>
<p>Key insights from the data:</p>
<ul>
<li><strong>Unblocked traffic</strong> (<code>action</code> = <code>allow</code>) - Active MCP connections that need investigation or blocking</li>
<li><strong>Blocked traffic</strong> (<code>action</code> = <code>block</code>) - Your existing policies are working</li>
<li><strong>User attribution</strong> - This indicates which employees are connecting to MCP servers</li>
</ul>
<h2 id="4-create-dlp-profiles-for-mcp-json-rpc-detection"><ol start="4">
<li>Create DLP profiles for MCP JSON-RPC detection</li>
</ol></h2>
<p>Gateway HTTP policies can match domains and URL paths, but they cannot inspect request bodies. DLP profiles scan <code>POST</code> body content for patterns, which is useful for shadow MCP detection, since MCP uses JSON-RPC over HTTP and has several detectable hallmarks.</p>
<p>Every MCP request contains a <code>&quot;method&quot;</code> field:</p>
<pre><code class="language-json">{&#10;	&quot;jsonrpc&quot;: &quot;2.0&quot;,&#10;	&quot;id&quot;: 1,&#10;	&quot;method&quot;: &quot;tools/call&quot;,&#10;	&quot;params&quot;: { &quot;name&quot;: &quot;read_file&quot;, &quot;arguments&quot;: { &quot;path&quot;: &quot;/etc/passwd&quot; } }&#10;}&#10;</code></pre>
<p>An attacker could run an MCP server on a non-standard domain (for example, <code>internal-tools.company.com/api/assistant</code>) without triggering domain-based or path-based rules. You can use DLP scans of the <code>POST</code> body for <code>&quot;method&quot;: &quot;tools/call&quot;</code> and other MCP-specific patterns to provide more robust protection of MCP traffic.</p>
<h3 id="review-dlp-constraints">Review DLP constraints</h3>
<p>Before building detection patterns, note the following DLP limitations:</p>
<ul>
<li><strong>Regex syntax</strong> — Rust regex (differs slightly from JavaScript and PCRE)</li>
<li><strong>Scan depth</strong> — First 1,024 bytes of the request body only</li>
<li><strong>POST only</strong> — DLP only scans <code>POST</code> requests</li>
<li><strong>Performance</strong> — Regex patterns must be efficient to avoid catastrophic backtracking</li>
</ul>
<h3 id="build-mcp-detection-patterns">Build MCP detection patterns</h3>
<p>MCP indicators can be found in JSON-RPC method fields. The following regex patterns cover the core MCP protocol methods:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4308.md")
</div>
<p>Pattern explanation:</p>
<ul>
<li><code>\\s{0,5}</code> — Allows zero to five whitespace characters to handle both minified and pretty-printed JSON</li>
<li><code>&quot;method&quot;</code> — Double quotes are literal because JSON requires them</li>
<li><code>&quot;tools/call&quot;</code> — Matches the exact MCP method name</li>
<li><code>202[4-9]</code> — Matches MCP protocol versions 2024 through 2029</li>
</ul>
<h3 id="create-the-dlp-profile-via-api">Create the DLP profile via API</h3>
<p>Send a <code>POST</code> request to create a custom DLP profile containing all detection patterns:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4309.md")
</div>
<p>Replace <code>${accountId}</code> with your Cloudflare account ID and <code>${apiToken}</code> with your API token.</p>
<h3 id="reference-the-dlp-profile-in-a-gateway-rule">Reference the DLP profile in a Gateway rule</h3>
<p>After the DLP profile exists, create a Gateway HTTP policy that blocks requests matching the profile:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4310.md")
</div>
<p>This rule triggers when the DLP profile matches any of the regex patterns in the request body.</p>
<h2 id="5-classify-portal-traffic-and-shadow-mcp-traffic"><ol start="5">
<li>Classify Portal traffic and shadow MCP traffic</li>
</ol></h2>
<p>Cloudflare <a href="/cloudflare-one/">MCP Server Portals</a> provide governed infrastructure for approved MCP access within your organization, including:</p>
<ul>
<li><strong>Governed access</strong> — Centralized MCP infrastructure managed by your IT team</li>
<li><strong>Audit trails</strong> — All MCP requests logged through Gateway with user attribution</li>
<li><strong>Policy enforcement</strong> — Zero Trust policies apply automatically, including authentication and DLP</li>
<li><strong>Approved tools</strong> — A curated set of MCP tools and resources vetted by security</li>
</ul>
<p>When analyzing Gateway logs, it is helpful to differentiate between two types of MCP traffic:</p>
<table>
<thead>
<tr>
<th>Traffic type</th>
<th>Characteristics</th>
<th>Risk level</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>MCP Portal traffic</td>
<td><code>httpHost</code> matches your portal domain (for example, <code>mcp.yourcompany.com</code> or <code>mcp-portal.pages.dev</code>)</td>
<td>Authorized</td>
<td>Monitor</td>
</tr>
<tr>
<td>Shadow MCP traffic</td>
<td><code>httpHost</code> does not match any portal domain (for example, <code>mcp.datadog.com</code>, <code>api.stripe.com/mcp</code>)</td>
<td>Investigate</td>
<td>Block, redirect or review</td>
</tr>
</tbody>
</table>
<p>Extend the query processing from <a href="#3-process-the-query-results">Process the query results</a> to classify traffic by comparing hostnames against your list of approved portal domains:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4311.md")
</div>
<p>Replace the <code>portalDomains</code> array with the actual domains of your approved MCP Server Portals.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/">Zero Trust documentation</a></li>
<li><a href="/cloudflare-one/traffic-policies/">Gateway policies</a></li>
<li><a href="/cloudflare-one/data-loss-prevention/">DLP profiles</a></li>
<li><a href="/analytics/graphql-api/">GraphQL Analytics API</a></li>
<li><a href="/ruleset-engine/rules-language/">Rules language and wirefilter expressions</a></li>
<li><a href="/pages/functions/">Pages Functions</a></li>
<li><a href="/logs/logpush/">Logpush</a></li>
</ul>
