<p>Labels add use-case context to operations. Security detections can use labels to extend relevant focus on traffic with a specific application use case.</p>
<h2 id="managed-labels">Managed labels</h2>
<p>Cloudflare defines managed labels. They identify common operation types, such as login flows, sign-up flows, and AI-powered operations.</p>
<p>Some managed labels can be discovered automatically. Automatic discovery currently applies only to selected managed labels and selected plans.</p>
<p>The following managed labels are available:</p>
<table>
<thead>
<tr>
<th>Label</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf-api-endpoint</code></td>
<td>Operations that serve machine-readable data or facilitate programmatic interaction.</td>
</tr>
<tr>
<td><code>cf-llm</code></td>
<td>Operations that receive requests for services powered by Large Language Models (LLMs).</td>
</tr>
<tr>
<td><code>cf-mcp</code></td>
<td>Operations that implement the <a href="/agents/model-context-protocol/">Model Context Protocol (MCP)</a> for AI tool and data access.</td>
</tr>
<tr>
<td><code>cf-contains-ads</code></td>
<td>Operations that serve web pages containing advertisements.</td>
</tr>
<tr>
<td><code>cf-log-in</code></td>
<td>Operations that accept user credentials.</td>
</tr>
<tr>
<td><code>cf-sign-up</code></td>
<td>Operations that create user accounts.</td>
</tr>
<tr>
<td><code>cf-content</code></td>
<td>Operations that provide unique content, such as product details, reviews, or pricing.</td>
</tr>
<tr>
<td><code>cf-purchase</code></td>
<td>Operations that complete a purchase.</td>
</tr>
<tr>
<td><code>cf-password-reset</code></td>
<td>Operations that participate in password reset flows.</td>
</tr>
<tr>
<td><code>cf-add-cart</code></td>
<td>Operations that add items to a cart or verify item availability.</td>
</tr>
<tr>
<td><code>cf-add-payment</code></td>
<td>Operations that accept credit card or bank account details.</td>
</tr>
<tr>
<td><code>cf-check-value</code></td>
<td>Operations that check rewards points, in-game currency, or other stored value.</td>
</tr>
<tr>
<td><code>cf-add-post</code></td>
<td>Operations that post messages, reviews, or similar user-generated content.</td>
</tr>
<tr>
<td><code>cf-account-update</code></td>
<td>Operations that update user account or profile details.</td>
</tr>
<tr>
<td><code>cf-rss-feed</code></td>
<td>Operations that expect traffic from RSS clients.</td>
</tr>
<tr>
<td><code>cf-web-page</code></td>
<td>Operations that serve HTML pages.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13836.md")
</aside>
<h2 id="available-detections">Available detections</h2>
<p>Some detections use labels to decide which operations to inspect. The following detections can use operation labels:</p>
<table>
<thead>
<tr>
<th>Label</th>
<th>Related detection</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf-llm</code></td>
<td><a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a></td>
</tr>
<tr>
<td><code>cf-log-in</code></td>
<td><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a> and <a href="/bots/account-abuse-protection/">account abuse protection</a></td>
</tr>
<tr>
<td><code>cf-sign-up</code></td>
<td><a href="/bots/account-abuse-protection/">Account abuse protection</a></td>
</tr>
</tbody>
</table>
<p>Some detections may still require product-specific configuration. For an end-to-end workflow, refer to <a href="/security/web-assets/define-security-protections/">Define security protections</a>.</p>
<h2 id="custom-labels">Custom labels</h2>
<p>Custom labels help you organize operations by owner, application, environment, and business flow.</p>
<h2 id="apply-labels">Apply labels</h2>
<p>Apply labels to operations from Web Assets.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13837.md")
</div>
<h2 id="use-labels-in-analytics-and-logs">Use labels in analytics and logs</h2>
<p>You can review matched operations and managed labels in Security Analytics. You can also query or export this data.</p>
<h3 id="graphql-analytics-api">GraphQL Analytics API</h3>
<p>You can query matched operation and managed label data using the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. The <code>webAssetsOperationId</code> and <code>webAssetsLabelsManaged</code> fields are available in the <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code> datasets.</p>
<p><code>webAssetsLabelsManaged</code> returns at most 10 labels per request.</p>
<p>The following query returns request counts by operation ID and managed label set for traffic carrying the <code>cf-llm</code> managed label:</p>
<pre><code class="language-graphql">query GetAdaptiveGroups($zoneTag: string, $start: DateTime!, $end: DateTime!) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			httpRequestsAdaptiveGroups(&#10;				filter: {&#10;					datetime_geq: $start&#10;					datetime_leq: $end&#10;					requestSource: &quot;eyeball&quot;&#10;					webAssetsLabelsManaged_hasany: [&quot;cf-llm&quot;]&#10;				}&#10;				limit: 25&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					webAssetsOperationId&#10;					webAssetsLabelsManaged&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Replace <code>cf-llm</code> with another <a href="#managed-labels">managed label</a>. You can also use <code>webAssetsOperationId</code> as the only dimension to group traffic by matched operation.</p>
<h3 id="logpush">Logpush</h3>
<p>You can export per-request Web Assets data to your storage or <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/13838.md")
</div> using [Logpush](/logs/logpush/). The `WebAssetsOperationID` and `WebAssetsLabelsManaged` fields are available in the [HTTP requests dataset](/logs/logpush/logpush-job/datasets/zone/http_requests/#webassetslabelsmanaged/).
