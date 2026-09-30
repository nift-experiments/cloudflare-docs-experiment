<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-03-23">Mar 23, 2026</time><div>
<h2 id="post-2026-03-23-agents-sdk-v0.8.0"><a href="/changelog/post/2026-03-23-agents-sdk-v0.8.0/">Agents SDK v0.8.0: readable state, idempotent schedules, typed AgentClient, and Zod 4</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> exposes agent state as a readable property, prevents duplicate schedule rows across Durable Object restarts, brings full TypeScript inference to <code>AgentClient</code>, and migrates to Zod 4.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-readable-state-on-useagent-and-agentclient">Readable <code>state</code> on <code>useAgent</code> and <code>AgentClient</code></h4>
<p>Both <code>useAgent</code> (React) and <code>AgentClient</code> (vanilla JS) now expose a <code>state</code> property that reflects the current agent state. Previously, reading state required manually tracking it through the <code>onStateUpdate</code> callback.</p>
<p><strong>React (<code>useAgent</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17655.md")</div>
<p><code>agent.state</code> is reactive — the component re-renders when state changes from either the server or a client-side <code>setState()</code> call.</p>
<p><strong>Vanilla JS (<code>AgentClient</code>)</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17656.md")</div>
<p>State starts as <code>undefined</code> and is populated when the server sends the initial state on connect (from <code>initialState</code>) or when <code>setState()</code> is called. Use optional chaining (<code>agent.state?.field</code>) for safe access. The <code>onStateUpdate</code> callback continues to work as before — the new <code>state</code> property is additive.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-idempotent-schedule">Idempotent <code>schedule()</code></h4>
<p><code>schedule()</code> now supports an <code>idempotent</code> option that deduplicates by <code>(type, callback, payload)</code>, preventing duplicate rows from accumulating when called in places that run on every Durable Object restart such as <code>onStart()</code>.</p>
<p><strong>Cron schedules are idempotent by default.</strong> Calling <code>schedule(&quot;0 * * * *&quot;, &quot;tick&quot;)</code> multiple times with the same callback, expression, and payload returns the existing schedule row instead of creating a new one. Pass <code>{ idempotent: false }</code> to override.</p>
<p>Delayed and date-scheduled types support opt-in idempotency:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17657.md")</div>
<p>Two new warnings help catch common foot-guns:</p>
<ul>
<li>Calling <code>schedule()</code> inside <code>onStart()</code> without <code>{ idempotent: true }</code> emits a <code>console.warn</code> with actionable guidance (once per callback; skipped for cron and when <code>idempotent</code> is set explicitly).</li>
<li>If an alarm cycle processes 10 or more stale one-shot rows for the same callback, the SDK emits a <code>console.warn</code> and a <code>schedule:duplicate_warning</code> diagnostics channel event.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-typed-agentclient-with-call-inference-and-stub-proxy">Typed <code>AgentClient</code> with <code>call</code> inference and <code>stub</code> proxy</h4>
<p><code>AgentClient</code> now accepts an optional agent type parameter for full type inference on RPC calls, matching the typed experience already available with <code>useAgent</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17658.md")</div>
<p>State is automatically inferred from the agent type, so <code>onStateUpdate</code> is also typed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17659.md")</div>
<p>Existing untyped usage continues to work without changes. The RPC type utilities (<code>AgentMethods</code>, <code>AgentStub</code>, <code>RPCMethods</code>) are now exported from <code>agents/client</code> for advanced typing scenarios.
<code>agents</code>, <code>@cloudflare/ai-chat</code>, and <code>@cloudflare/codemode</code> now require <code>zod ^4.0.0</code>. Zod v3 is no longer supported.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Turn serialization</strong> — <code>onChatMessage()</code> and <code>_reply()</code> work is now queued so user requests, tool continuations, and <code>saveMessages()</code> never stream concurrently.</li>
<li><strong>Duplicate messages on stop</strong> — Clicking stop during an active stream no longer splits the assistant message into two entries.</li>
<li><strong>Duplicate messages after tool calls</strong> — Orphaned client IDs no longer leak into persistent storage.</li>
</ul>
<h4 id="2026-03-23-agents-sdk-v0.8.0-keepalive-and-keepalivewhile-are-no-longer-experimental"><code>keepAlive()</code> and <code>keepAliveWhile()</code> are no longer experimental</h4>
<p><code>keepAlive()</code> now uses a lightweight in-memory ref count instead of schedule rows. Multiple concurrent callers share a single alarm cycle. The <code>@experimental</code> tag has been removed from both <code>keepAlive()</code> and <code>keepAliveWhile()</code>.</p>
<h4 id="2026-03-23-agents-sdk-v0.8.0-cloudflare-codemode-tanstack-ai-integration"><code>@cloudflare/codemode</code>: TanStack AI integration</h4>
<p>A new entry point <code>@cloudflare/codemode/tanstack-ai</code> adds support for <a href="https://tanstack.com/ai">TanStack AI's</a> <code>chat()</code> as an alternative to the Vercel AI SDK's <code>streamText()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17660.md")</div>
<h4 id="2026-03-23-agents-sdk-v0.8.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-23">Mar 23, 2026</time><div>
<h2 id="post-2026-03-23-ai-search-new-rest-api"><a href="/changelog/post/2026-03-23-ai-search-new-rest-api/">New AI Search REST API endpoints for /search and /chat/completions</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now offers new <a href="/ai-search/api/search/rest-api/">REST API</a> endpoints for search and chat that use an OpenAI compatible format. This means you can use the familiar <code>messages</code> array structure that works with existing OpenAI SDKs and tools. The messages array also lets you pass previous messages within a session, so the model can maintain context across multiple turns.</p>
<table>
<thead>
<tr>
<th>Endpoint</th>
<th>Path</th>
</tr>
</thead>
<tbody>
<tr>
<td>Chat Completions</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/chat/completions</code></td>
</tr>
<tr>
<td>Search</td>
<td><code>POST /accounts/{account_id}/ai-search/instances/{name}/search</code></td>
</tr>
</tbody>
</table>
<p>Here is an example request to the Chat Completions endpoint using the new <code>messages</code> array format:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/chat/completions \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful documentation assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;How do I get started?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/rest-api/">AI Search REST API guide</a>.</p>
<h4 id="2026-03-23-ai-search-new-rest-api-migration-from-existing-autorag-api-recommended">Migration from existing AutoRAG API (recommended)</h4>
<p>If you are using the previous AutoRAG API endpoints (<code>/autorag/rags/</code>), we recommend migrating to the new endpoints. The previous AutoRAG API endpoints will continue to be fully supported.</p>
<p>Refer to the <a href="/ai-search/api/migration/rest-api/">migration guide</a> for step-by-step instructions.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-23">Mar 23, 2026</time><div>
<h2 id="post-2026-03-23-ai-search-public-endpoint-and-snippets"><a href="/changelog/post/2026-03-23-ai-search-public-endpoint-and-snippets/">AI Search UI snippets and MCP support</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports public endpoints, UI snippets, and MCP, making it easy to add search to your website or connect AI agents.</p>
<p>Public endpoints allow you to expose AI Search capabilities without requiring API authentication. To enable public endpoints:</p>
<ol>
<li>Go to <strong>AI Search</strong> in the Cloudflare dashboard.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your instance, and turn on **Public Endpoint** in **Settings**.
   For more details, refer to [Public endpoint configuration](/ai-search/configuration/retrieval/public-endpoint/).
<h4 id="2026-03-23-ai-search-public-endpoint-and-snippets-ui-snippets">UI snippets</h4>
<p>UI snippets are pre-built search and chat components you can embed in your website. Visit <a href="https://search.ai.cloudflare.com/">search.ai.cloudflare.com</a> to configure and preview components for your AI Search instance.</p>
<p><img src="/assets/upstream/images/ai-search/ui-snippet-search-modal.png" alt="Example of the search-modal-snippet component" /></p>
<p>To add a search modal to your page:</p>
<pre><code class="language-html">&lt;script&#10;	type=&quot;module&quot;&#10;	src=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/assets/v0.0.25/search-snippet.es.js&quot;&#10;&gt;&lt;/script&gt;&#10;&#10;&lt;search-modal-snippet&#10;	api-url=&quot;https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/&quot;&#10;	placeholder=&quot;Search...&quot;&#10;&gt;&#10;&lt;/search-modal-snippet&gt;&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/configuration/retrieval/public-endpoint/embed-search-snippets/">UI snippets documentation</a>.</p>
<h4 id="2026-03-23-ai-search-public-endpoint-and-snippets-mcp">MCP</h4>
<p>The MCP endpoint allows AI agents to search your content via the Model Context Protocol. Connect your MCP client to:</p>
<pre><code class="language-txt">https://&lt;PUBLIC_ENDPOINT_ID&gt;.search.ai.cloudflare.com/mcp&#10;</code></pre>
<p>For more details, refer to the <a href="/ai-search/api/search/mcp/">MCP documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-23">Mar 23, 2026</time><div>
<h2 id="post-2026-03-23-custom-metadata-filtering"><a href="/changelog/post/2026-03-23-custom-metadata-filtering/">Custom metadata filtering for AI Search</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports custom metadata filtering, allowing you to define your own metadata fields and filter search results based on attributes like category, version, or any custom field you define.</p>
<h4 id="2026-03-23-custom-metadata-filtering-define-a-custom-metadata-schema">Define a custom metadata schema</h4>
<p>You can define up to 5 custom metadata fields per AI Search instance. Each field has a name and data type (<code>text</code>, <code>number</code>, or <code>boolean</code>):</p>
<pre><code class="language-bash">curl -X POST https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-instance&quot;,&#10;    &quot;type&quot;: &quot;r2&quot;,&#10;    &quot;source&quot;: &quot;my-bucket&quot;,&#10;    &quot;custom_metadata&quot;: [&#10;      { &quot;field_name&quot;: &quot;category&quot;, &quot;data_type&quot;: &quot;text&quot; },&#10;      { &quot;field_name&quot;: &quot;version&quot;, &quot;data_type&quot;: &quot;number&quot; },&#10;      { &quot;field_name&quot;: &quot;is_public&quot;, &quot;data_type&quot;: &quot;boolean&quot; }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-03-23-custom-metadata-filtering-add-metadata-to-your-documents">Add metadata to your documents</h4>
<p>How you attach metadata depends on your data source:</p>
<ul>
<li><strong>R2 bucket</strong>: Set metadata using S3-compatible custom headers (<code>x-amz-meta-*</code>) when uploading objects. Refer to <a href="/ai-search/configuration/data-source/r2/#custom-metadata">R2 custom metadata</a> for examples.</li>
<li><strong>Website</strong>: Add <code>&lt;meta&gt;</code> tags to your HTML pages. Refer to <a href="/ai-search/configuration/data-source/website/custom-metadata/">Website custom metadata</a> for details.</li>
</ul>
<h4 id="2026-03-23-custom-metadata-filtering-filter-search-results">Filter search results</h4>
<p>Use custom metadata fields in your search queries alongside built-in attributes like <code>folder</code> and <code>timestamp</code>:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai-search/instances/{NAME}/search \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer {API_TOKEN}&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;content&quot;: &quot;How do I configure authentication?&quot;,&#10;        &quot;role&quot;: &quot;user&quot;&#10;      }&#10;    ],&#10;    &quot;ai_search_options&quot;: {&#10;      &quot;retrieval&quot;: {&#10;        &quot;filters&quot;: {&#10;          &quot;category&quot;: &quot;documentation&quot;,&#10;          &quot;version&quot;: { &quot;$gte&quot;: 2.0 }&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Learn more in the <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-23">Mar 23, 2026</time><div>
<h2 id="post-2026-03-23-web-assets-graphql-fields"><a href="/changelog/post/2026-03-23-web-assets-graphql-fields/">Web Assets fields now available in GraphQL Analytics API</a></h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>Two new fields are now available in the <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code> <a href="/analytics/graphql-api/">GraphQL Analytics API</a> datasets:</p>
<ul>
<li><code>webAssetsOperationId</code> — the ID of the <a href="/api-shield/management-and-monitoring/">saved endpoint</a> that matched the incoming request.</li>
<li><code>webAssetsLabelsManaged</code> — the <a href="/api-shield/management-and-monitoring/endpoint-labels/#managed-labels">managed labels</a> mapped to the matched operation at the time of the request (for example, <code>cf-llm</code>, <code>cf-log-in</code>). At most 10 labels are returned per request.</li>
</ul>
<p>Both fields are empty when no operation matched. <code>webAssetsLabelsManaged</code> is also empty when no managed labels are assigned to the matched operation.</p>
<p>These fields allow you to determine, per request, which Web Assets operation was matched and which managed labels were active. This is useful for troubleshooting downstream security detection verdicts — for example, understanding why <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> did or did not flag a request.</p>
<p>Refer to <a href="/api-shield/management-and-monitoring/endpoint-labels/#analytics">Endpoint labeling service</a> for GraphQL query examples.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-23">Mar 23, 2026</time><div>
<h2 id="post-2026-03-23-expanded-sql-functions-expressions-complex-types"><a href="/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/">R2 SQL now supports over 190 new functions, expressions, and complex types</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p><a href="/r2-sql/">R2 SQL</a> now supports an expanded SQL grammar so you can write richer analytical queries without exporting data. This release adds CASE expressions, column aliases, arithmetic in clauses, 163 scalar functions, 33 aggregate functions, EXPLAIN, Common Table Expressions (CTEs),and full struct/array/map access. R2 SQL is Cloudflare's serverless, distributed, analytics query engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. This page documents the supported SQL syntax.</p>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-highlights">Highlights</h4>
<ul>
<li><strong>Column aliases</strong> — <code>SELECT col AS alias</code> now works in all clauses</li>
<li><strong>CASE expressions</strong> — conditional logic directly in SQL (searched and simple forms)</li>
<li><strong>Scalar functions</strong> — 163 new functions across math, string, datetime, regex, crypto, encoding, and type inspection categories</li>
<li><strong>Aggregate functions</strong> — statistical (variance, stddev, correlation, regression), bitwise, boolean, and positional aggregates join the existing basic and approximate functions</li>
<li><strong>Complex types</strong> — query struct fields with bracket notation, use 46 array functions, and extract map keys/values</li>
<li><strong>Common table expressions (CTEs)</strong> — use <code>WITH ... AS</code> to define named temporary result sets. Chained CTEs are supported. All CTEs must reference the same single table.</li>
<li><strong>Full expression support</strong> — arithmetic, type casting (<code>CAST</code>, <code>TRY_CAST</code>, <code>::</code> shorthand), and <code>EXTRACT</code> in SELECT, WHERE, GROUP BY, HAVING, and ORDER BY</li>
</ul>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-examples">Examples</h4>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-case-expressions-with-statistical-aggregates">CASE expressions with statistical aggregates</h4>
<pre><code class="language-sql">SELECT source,&#10;    CASE&#10;        WHEN AVG(price) &gt; 30 THEN &#x27;premium&#x27;&#10;        WHEN AVG(price) &gt; 10 THEN &#x27;mid-tier&#x27;&#10;        ELSE &#x27;budget&#x27;&#10;    END AS tier,&#10;    round(stddev(price), 2) AS price_volatility,&#10;    approx_percentile_cont(price, 0.95) AS p95_price&#10;FROM my_namespace.sales_data&#10;GROUP BY source&#10;</code></pre>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-struct-and-array-access">Struct and array access</h4>
<pre><code class="language-sql">SELECT product_name,&#10;    pricing[&#x27;price&#x27;] AS price,&#10;    array_to_string(tags, &#x27;, &#x27;) AS tag_list&#10;FROM my_namespace.products&#10;WHERE array_has(tags, &#x27;Action&#x27;)&#10;ORDER BY pricing[&#x27;price&#x27;] DESC&#10;LIMIT 10&#10;</code></pre>
<h4 id="2026-03-23-expanded-sql-functions-expressions-complex-types-chained-ctes-with-time-series-analysis">Chained CTEs with time-series analysis</h4>
<pre><code class="language-sql">WITH monthly AS (&#10;    SELECT date_trunc(&#x27;month&#x27;, sale_timestamp) AS month,&#10;        department,&#10;        COUNT(*) AS transactions,&#10;        round(AVG(total_amount), 2) AS avg_amount&#10;    FROM my_namespace.sales_data&#10;    WHERE sale_timestamp BETWEEN &#x27;2025-01-01T00:00:00Z&#x27; AND &#x27;2025-12-31T23:59:59Z&#x27;&#10;    GROUP BY date_trunc(&#x27;month&#x27;, sale_timestamp), department&#10;),&#10;ranked AS (&#10;    SELECT month, department, transactions, avg_amount,&#10;        CASE&#10;            WHEN avg_amount &gt; 1000 THEN &#x27;high-value&#x27;&#10;            WHEN avg_amount &gt; 500 THEN &#x27;mid-value&#x27;&#10;            ELSE &#x27;standard&#x27;&#10;        END AS tier&#10;    FROM monthly&#10;    WHERE transactions &gt; 100&#10;)&#10;SELECT * FROM ranked&#10;ORDER BY month, avg_amount DESC&#10;</code></pre>
<p>For the full function reference and syntax details, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For limitations and best practices, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-23">Mar 23, 2026</time><div>
<h2 id="post-2026-03-23-waf-release"><a href="/changelog/post/2026-03-23-waf-release/">WAF Release - 2026-03-23</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on new improvements to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="54ad0465c30d4cd2ac7a707197321c6c">97321c6c</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - URI Vector</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b31c34a7b29b4aaf9be6883d1eb7a999">1eb7a999</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - Header Vector</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="155bb67d1061479e995a38510677175f">0677175f</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 9 - Body Vector</td>
<td>Log</td>
<td>Disabled</td>      
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="55fb1c76f0304f6a9d935d03479da68f">479da68f</code>
</td>
<td>N/A</td>
<td>PHP, vBulletin, jQuery File Upload - Code Injection, Dangerous File Upload - CVE:CVE-2018-9206, CVE:CVE-2019-17132 (beta)</td>
<td>Log</td>
<td>Block</td>
<td>This rule has been merged into the original rule "PHP, vBulletin, jQuery File Upload - Code Injection, Dangerous File Upload - CVE:CVE-2018-9206, CVE:CVE-2019-17132" (ID: <code class="nb-rule-id" title="0f2da91cec674eb58006929e824b817c">824b817c</code>)</td>
</tr>
</tbody>    
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-20">Mar 20, 2026</time><div>
<h2 id="post-2026-03-20-managed-oauth"><a href="/changelog/post/2026-03-20-managed-oauth/">Managed OAuth for Cloudflare Access</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access supports managed OAuth, which allows non-browser clients — such as CLIs, AI agents, SDKs, and scripts — to authenticate with Access-protected applications using a standard OAuth 2.0 authorization code flow.</p>
<p>Previously, non-browser clients that attempted to access a protected application received a <code>302</code> redirect to a login page they could not complete. The established workaround was <code>cloudflared access curl</code>, which required installing additional tooling.</p>
<p>With managed OAuth, clients instead receive a <code>401</code> response with a <code>WWW-Authenticate</code> header that points to Access's OAuth discovery endpoints (<a href="https://datatracker.ietf.org/doc/html/rfc8414">RFC 8414</a> and <a href="https://datatracker.ietf.org/doc/html/rfc9728">RFC 9728</a>). The client opens the end user's browser to the Access login page. The end user authenticates with their identity provider, and the client receives an OAuth access token for subsequent requests.</p>
<p>Access enforces the same policies as a browser login; the OAuth layer is a new transport mechanism, not a separate authentication path.</p>
<p>Managed OAuth can be enabled on any self-hosted Access application or <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a>. It is opt-in for existing applications to avoid interfering with those that run their own OAuth servers and rely on their own <code>WWW-Authenticate</code> headers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17618.md")</aside>
<p>To enable managed OAuth, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>, edit the application, and turn on <strong>Managed OAuth</strong> under <strong>Advanced settings</strong>.</p>
<p>You can also enable it via the API by setting <code>oauth_configuration.enabled</code> to <code>true</code> on the <a href="/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/">Access applications endpoint</a>.</p>
<p><img src="/assets/upstream/images/changelog/access/managed-oauth.png" alt="Managed OAuth settings in the Cloudflare dashboard" /></p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/">Enable managed OAuth</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-20">Mar 20, 2026</time><div>
<h2 id="post-2026-03-20-mcp-portal-gateway-routing"><a href="/changelog/post/2026-03-20-mcp-portal-gateway-routing/">Route MCP server portal traffic through Cloudflare Gateway</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now route traffic through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for richer HTTP request logging and data loss prevention (DLP) scanning.</p>
<p>When Gateway routing is turned on, portal traffic appears in your <a href="/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/">Gateway HTTP logs</a>. You can create <a href="/cloudflare-one/traffic-policies/">Gateway HTTP policies</a> with <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/">DLP profiles</a> to detect and block sensitive data sent to upstream MCP servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17619.md")</aside>
<p>To enable Gateway routing, go to <strong>Access controls</strong> &gt; <strong>AI controls</strong>, edit the portal, and turn on <strong>Route traffic through Cloudflare Gateway</strong> under <strong>Basic information</strong>.</p>
<p><img src="/assets/upstream/images/changelog/access/portal-route-through-gateway.png" alt="Route MCP server portal traffic through Cloudflare Gateway" /></p>
<p>For more details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#route-portal-traffic-through-gateway">Route traffic through Gateway</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-20">Mar 20, 2026</time><div>
<h2 id="post-2026-03-20-dns-analytics-cmb-eu"><a href="/changelog/post/2026-03-20-dns-analytics-cmb-eu/">DNS Analytics for Customer Metadata Boundary set to EU region</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>DNS Analytics is now available for customers with <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) set to EU. Query your DNS analytics data while keeping metadata stored in the EU region.</p>
<p>This update includes:</p>
<ul>
<li><strong>DNS Analytics</strong> — Access the same DNS analytics experience for zones in CMB=EU accounts.</li>
<li><strong>EU data residency</strong> — Analytics data is stored and queried from the EU region, meeting data localization requirements.</li>
<li><strong>DNS Firewall Analytics</strong> — DNS Firewall analytics is now supported for CMB=EU customers.</li>
</ul>
<h4 id="2026-03-20-dns-analytics-cmb-eu-availability">Availability</h4>
<p>Available to customers with the <a href="/data-localization/">Data Localization Suite</a> who have Customer Metadata Boundary configured for the EU region.</p>
<h4 id="2026-03-20-dns-analytics-cmb-eu-where-to-find-it">Where to find it</h4>
<ul>
<li><strong>Authoritative DNS:</strong> In the Cloudflare dashboard, select your zone and go to the <strong>Analytics</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li><strong>DNS Firewall:</strong> In the Cloudflare dashboard, go to the <strong>DNS Firewall Analytics</strong> page.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/dns/additional-options/analytics/">DNS Analytics</a> and <a href="/dns/dns-firewall/analytics/">DNS Firewall Analytics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-20">Mar 20, 2026</time><div>
<h2 id="post-2026-03-20-tunnel-replica-overview-and-multi-log-streaming"><a href="/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/">Stream logs from multiple replicas of Cloudflare Tunnel simultaneously</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> of that tunnel and supports streaming logs from multiple replicas at once.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-multiconn.gif" alt="View replicas and stream logs from multiple connectors" /></p>
<p>Previously, you could only stream logs from one replica at a time. With this update:</p>
<ul>
<li><strong>Replicas on the tunnel overview</strong> — All active replicas for the selected tunnel now appear on that tunnel's overview page under <strong>Connectors</strong>. Select any replica to stream its logs.</li>
<li><strong>Multi-connector log streaming</strong> — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Networks</strong> &gt; <strong>Connectors</strong> &gt; <strong>Cloudflare Tunnels</strong>. Select <strong>View logs</strong> next to the tunnel you want to monitor.</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/">Deploy replicas</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-20">Mar 20, 2026</time><div>
<h2 id="post-2026-03-20-metrics-and-settings-dashboard"><a href="/changelog/post/2026-03-20-metrics-and-settings-dashboard/">Observability for Workers VPC Services</a></h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p>Each VPC Service now has a <strong>Metrics</strong> tab so you can monitor connection health and debug failures without leaving the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers-vpc/2026-03-20-metrics-dashboard.png" alt="Workers VPC Metrics dashboard showing connections, latency, and errors charts" /></p>
<ul>
<li><strong>Connections</strong> — See successful and failed connections over time, broken down by what is responsible: your origin (Bad Upstream), your configuration (Client), or Cloudflare (Internal).</li>
<li><strong>Latency</strong> — Track connection and DNS resolution latency trends.</li>
<li><strong>Errors</strong> — Drill into specific error codes grouped by category, with filters to isolate upstream, client, or internal failures.</li>
</ul>
<p>You can also view and edit your VPC Service configuration, host details, and port assignments from the <strong>Settings</strong> tab.</p>
<p>For a full list of error codes and what they mean, refer to <a href="/workers-vpc/reference/troubleshooting/">Troubleshooting</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-19">Mar 19, 2026</time><div>
<h2 id="post-2026-03-19-service-key-authentication-deprecated"><a href="/changelog/post/2026-03-19-service-key-authentication-deprecated/">Service Key authentication deprecated</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Service Key authentication for the Cloudflare API is deprecated. Service Keys will stop working on September 30, 2026.</p>
<p><a href="/fundamentals/api/get-started/create-token/">API Tokens</a> replace Service Keys with fine-grained permissions, expiration, and revocation.</p>
<h4 id="2026-03-19-service-key-authentication-deprecated-what-you-need-to-do">What you need to do</h4>
<p>Replace any use of the <code>X-Auth-User-Service-Key</code> header with an <a href="/fundamentals/api/get-started/create-token/">API Token</a> scoped to the permissions your integration requires.</p>
<p>If you use <code>cloudflared</code>, update to a version from November 2022 or later. These versions already use API Tokens.</p>
<p>If you use <a href="https://github.com/cloudflare/origin-ca-issuer">origin-ca-issuer</a>, update to a version that supports API Token authentication.</p>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-19">Mar 19, 2026</time><div>
<h2 id="post-2026-03-19-hyperdrive-mysql-custom-certificate-support"><a href="/changelog/post/2026-03-19-hyperdrive-mysql-custom-certificate-support/">Hyperdrive now supports custom TLS/SSL certificates for MySQL</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now supports custom TLS/SSL certificates for MySQL databases, bringing the same certificate options previously available for PostgreSQL to MySQL connections.</p>
<p>You can now configure:</p>
<ul>
<li><strong>Server certificate verification</strong> with <code>VERIFY_CA</code> or <code>VERIFY_IDENTITY</code> SSL modes to verify that your MySQL database server's certificate is signed by the expected certificate authority (CA).</li>
<li><strong>Client certificates</strong> (mTLS) for Hyperdrive to authenticate itself to your MySQL database with credentials beyond username and password.</li>
</ul>
<p>Create a Hyperdrive configuration with custom certificates for MySQL:</p>
<pre><code class="language-bash">&#35; Upload a CA certificate&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create a Hyperdrive with VERIFY_IDENTITY mode&#10;npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;mysql://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-sslmode VERIFY_IDENTITY&#10;</code></pre>
<p>For more information, refer to <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">SSL/TLS certificates for Hyperdrive</a> and <a href="/hyperdrive/examples/connect-to-mysql/">MySQL TLS/SSL modes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-19">Mar 19, 2026</time><div>
<h2 id="post-2026-03-19-wrangler-tunnel-commands"><a href="/changelog/post/2026-03-19-wrangler-tunnel-commands/">Manage Cloudflare Tunnels with Wrangler</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>workers</span></div><div class="changelog-body"><p>You can now manage <a href="/tunnel/">Cloudflare Tunnels</a> directly from <a href="/workers/wrangler/">Wrangler</a>, the CLI for the Cloudflare Developer Platform. The new <a href="/workers/wrangler/commands/tunnel/"><code>wrangler tunnel</code></a> commands let you create, run, and manage tunnels without leaving your terminal.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/wrangler-tunnel.gif" alt="Wrangler tunnel commands demo" /></p>
<p>Available commands:</p>
<ul>
<li><code>wrangler tunnel create</code> — Create a new remotely managed tunnel.</li>
<li><code>wrangler tunnel list</code> — List all tunnels in your account.</li>
<li><code>wrangler tunnel info</code> — Display details about a specific tunnel.</li>
<li><code>wrangler tunnel delete</code> — Delete a tunnel.</li>
<li><code>wrangler tunnel run</code> — Run a tunnel using the cloudflared daemon.</li>
<li><code>wrangler tunnel quick-start</code> — Start a free, temporary tunnel without an account using <a href="/tunnel/get-started/#quick-tunnels-development">Quick Tunnels</a>.</li>
</ul>
<p>Wrangler handles downloading and managing the <a href="/tunnel/downloads/">cloudflared</a> binary automatically. On first use, you will be prompted to download <code>cloudflared</code> to a local cache directory.</p>
<p>These commands are currently experimental and may change without notice.</p>
<p>To get started, refer to the <a href="/workers/wrangler/commands/tunnel/">Wrangler tunnel commands documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-19">Mar 19, 2026</time><div>
<h2 id="post-2026-03-19-kimi-k2-5-workers-ai"><a href="/changelog/post/2026-03-19-kimi-k2-5-workers-ai/">Moonshot AI Kimi K2.5 now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Workers AI is officially in the big models game. <a href="/workers-ai/models/kimi-k2.5/"><code>@cf/moonshotai/kimi-k2.5</code></a> is the first frontier-scale open-source model on our AI inference platform — a large model with a full 256k context window, multi-turn tool calling, vision inputs, and structured outputs. By bringing a frontier-scale model directly onto the Cloudflare Developer Platform, you can now run the entire agent lifecycle on a single, unified platform.</p>
<p>The model has proven to be a fast, efficient alternative to larger proprietary models without sacrificing quality. As AI adoption increases, the volume of inference is skyrocketing — now you can access frontier intelligence at a fraction of the cost.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>256,000 token context window</strong> for retaining full conversation history, tool definitions, and entire codebases across long-running agent sessions</li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Structured outputs</strong> with JSON mode and JSON Schema support for reliable downstream parsing</li>
<li><strong>Function calling</strong> for integrating external tools and APIs into agent workflows</li>
</ul>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-prefix-caching-and-session-affinity">Prefix caching and session affinity</h4>
<p>When an agent sends a new prompt, it resends all previous prompts, tools, and context from the session. The delta between consecutive requests is usually just a few new lines of input. Prefix caching avoids reprocessing the shared context, saving time and compute from the prefill stage. This means faster Time to First Token (TTFT) and higher Tokens Per Second (TPS) throughput.</p>
<p>Workers AI has done prefix caching, but we are now surfacing cached tokens as a usage metric and offering a discount on cached tokens compared to input tokens (pricing is listed on the <a href="/workers-ai/models/kimi-k2.5/">model page</a>).</p>
<pre><code class="language-bash">curl -X POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/moonshotai/kimi-k2.5&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;x-session-affinity: ses_12345678&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;system&quot;,&#10;        &quot;content&quot;: &quot;You are a helpful assistant.&quot;&#10;      },&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is prefix caching and why does it matter?&quot;&#10;      }&#10;    ],&#10;    &quot;max_tokens&quot;: 2400,&#10;    &quot;stream&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>Some clients like <a href="https://opencode.ai">OpenCode</a> implement session affinity automatically. The <a href="https://github.com/cloudflare/agents">Agents SDK</a> starter also sets up the wiring for you.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-redesigned-asynchronous-api">Redesigned asynchronous API</h4>
<p>For volumes of requests that exceed synchronous rate limits, you can submit batches of inferences to be completed asynchronously. We have revamped the <a href="/workers-ai/features/batch-api/">Asynchronous Batch API</a> with a pull-based system that processes queued requests as soon as capacity is available. With internal testing, async requests usually execute within 5 minutes, but this depends on live traffic.</p>
<p>The async API is the best way to avoid capacity errors in durable workflows. It is ideal for use cases that are not real-time, such as code scanning agents or research agents.</p>
<p>To use the asynchronous API, pass <code>queueRequest: true</code>:</p>
<pre><code class="language-js">// 1. Push a batch of requests into the queue&#10;const res = await env.AI.run(&#10;	&quot;@cf/moonshotai/kimi-k2.5&quot;,&#10;	{&#10;		requests: [&#10;			{&#10;				messages: [{ role: &quot;user&quot;, content: &quot;Tell me a joke&quot; }],&#10;			},&#10;			{&#10;				messages: [{ role: &quot;user&quot;, content: &quot;Explain the Pythagoras theorem&quot; }],&#10;			},&#10;		],&#10;	},&#10;	{ queueRequest: true },&#10;);&#10;&#10;// 2. Grab the request ID&#10;const requestId = res.request_id;&#10;&#10;// 3. Poll for the result&#10;const result = await env.AI.run(&quot;@cf/moonshotai/kimi-k2.5&quot;, {&#10;	request_id: requestId,&#10;});&#10;&#10;if (result.status === &quot;queued&quot; || result.status === &quot;running&quot;) {&#10;	// Retry by polling again&#10;} else {&#10;	return Response.json(result);&#10;}&#10;</code></pre>
<p>You can also set up <a href="/workers-ai/platform/event-subscriptions/">event notifications</a> to know when inference is complete instead of polling.</p>
<h4 id="2026-03-19-kimi-k2-5-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.5 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, <a href="/ai-gateway/">AI Gateway</a>, or via the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.5/">Kimi K2.5 model page</a>, <a href="/workers-ai/platform/pricing/">pricing</a>, and <a href="/workers-ai/features/prompt-caching/">prompt caching</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-18">Mar 18, 2026</time><div>
<h2 id="post-2026-03-17-scim-authentik-support"><a href="/changelog/post/2026-03-17-scim-authentik-support/">SCIM provisioning for Authentik is now Generally Available</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare dashboard SCIM provisioning now supports <a href="https://goauthentik.io/">Authentik</a> as an identity provider, joining Okta and Microsoft Entra ID as explicitly supported providers.</p>
<p>Customers can now sync users and group information from Authentik to Cloudflare, apply Permission Policies to those groups, and manage the lifecycle of users &amp; groups directly from your Authentik Identity Provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17730.md")</aside>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning overview</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/authentik/">Provision with Authentik</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-18">Mar 18, 2026</time><div>
<h2 id="post-2026-03-18-scim-audit-logging"><a href="/changelog/post/2026-03-18-scim-audit-logging/">SCIM audit logging Support</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare dashboard SCIM provisioning operations are now captured in <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2</a>, giving you visibility into user and group changes made by your identity provider.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-03-18-scim-audit-logging.png" alt="SCIM audit logging" /></p>
<p><strong>Logged actions:</strong></p>
<table>
<thead>
<tr>
<th>Action Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Create SCIM User</td>
<td>User provisioned from IdP</td>
</tr>
<tr>
<td>Replace SCIM User</td>
<td>User fully replaced (PUT)</td>
</tr>
<tr>
<td>Update SCIM User</td>
<td>User attributes modified (PATCH)</td>
</tr>
<tr>
<td>Delete SCIM User</td>
<td>Member deprovisioned</td>
</tr>
<tr>
<td>Create SCIM Group</td>
<td>Group provisioned from IdP</td>
</tr>
<tr>
<td>Update SCIM Group</td>
<td>Group membership or attributes modified</td>
</tr>
<tr>
<td>Delete SCIM Group</td>
<td>Group deprovisioned</td>
</tr>
</tbody>
</table>
<p>For more details, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs v2 documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-18">Mar 18, 2026</time><div>
<h2 id="post-2026-03-18-worker-timing-field"><a href="/changelog/post/2026-03-18-worker-timing-field/">Worker execution timing field now available in Rules</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><p>The <code>cf.timings.worker_msec</code> field is now available in the Ruleset Engine. This field reports the wall-clock time that a Cloudflare Worker spent handling a request, measured in milliseconds.</p>
<p>You can use this field to identify slow Worker executions, detect performance regressions, or build rules that respond differently based on Worker processing time, such as logging requests that exceed a latency threshold.</p>
<h4 id="2026-03-18-worker-timing-field-field-details">Field details</h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.timings.worker_msec</code></td>
<td>Integer</td>
<td>The time spent executing a Cloudflare Worker in milliseconds. Returns <code>0</code> if no Worker was invoked.</td>
</tr>
</tbody>
</table>
<p>Example filter expression:</p>
<pre><code>cf.timings.worker_msec &gt; 500&#10;</code></pre>
<p>For more information, refer to the <a href="/ruleset-engine/rules-language/fields/reference/cf.timings.worker_msec/">Fields reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-18">Mar 18, 2026</time><div>
<h2 id="post-2026-03-18-brand-protection-logo-match-preview"><a href="/changelog/post/2026-03-18-brand-protection-logo-match-preview/">Real-time logo match preview</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>We are introducing <strong>Logo Match Preview</strong>, bringing the same pre-save visibility to visual assets that was previously only available for string-based queries. This update allows you to fine-tune your brand detection strategy before committing to a live monitor.</p>
<h4 id="2026-03-18-brand-protection-logo-match-preview-what-s-new">What’s new:</h4>
<ul>
<li>Upload your brand logo and immediately see a sample of potential matches from recently detected sites before finalizing the query</li>
<li>Adjust your similarity score (from 75% to 100%) and watch the results refresh in real-time to find the balance between broad detection and noise reduction</li>
<li>Review the specific logos triggered by your current settings to ensure your query is capturing the right level of brand infringement</li>
</ul>
<p>If you are ready to test your brand assets, go to the <a href="https://developers.cloudflare.com/security-center/brand-protection/">Brand Protection dashboard</a> to try the new preview tool.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-18">Mar 18, 2026</time><div>
<h2 id="post-2026-03-18-media-transformations-workers-binding"><a href="/changelog/post/2026-03-18-media-transformations-workers-binding/">Media Transformations binding for Workers</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now use a Workers binding to transform videos with Media Transformations. This allows you to resize, crop, extract frames, and extract audio from videos stored anywhere, even in private locations like R2 buckets.</p>
<p>The Media Transformations binding is useful when you want to:</p>
<ul>
<li>Transform videos stored in private or protected sources</li>
<li>Optimize videos and store the output directly back to R2 for re-use</li>
<li>Extract still frames for classification or description with Workers AI</li>
<li>Extract audio tracks for transcription using Workers AI</li>
</ul>
<p>To get started, add the Media binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17754.md")</div>
<p>Then use the binding in your Worker to transform videos:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17755.md")</div>
<p>Output modes include <code>video</code> for optimized MP4 clips, <code>frame</code> for still images, <code>spritesheet</code> for multiple frames, and <code>audio</code> for M4A extraction.</p>
<p>For more information, refer to the <a href="/stream/transform-videos/bindings/">Media Transformations binding documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-17">Mar 17, 2026</time><div>
<h2 id="post-2026-03-17-codemode-sdk-v0.2.1"><a href="/changelog/post/2026-03-17-codemode-sdk-v0.2.1/">@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest releases of <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> add a new MCP barrel export, remove <code>ai</code> and <code>zod</code> as required peer dependencies from the main entry point, and give you more control over the sandbox.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-new-cloudflare-codemode-mcp-export">New <code>@cloudflare/codemode/mcp</code> export</h4>
<p>A new <code>@cloudflare/codemode/mcp</code> entry point provides two functions that wrap MCP servers with Code Mode:</p>
<ul>
<li><strong><code>codeMcpServer({ server, executor })</code></strong> — wraps an existing MCP server with a single <code>code</code> tool where each upstream tool becomes a typed <code>codemode.*</code> method.</li>
<li><strong><code>openApiMcpServer({ spec, executor, request })</code></strong> — creates <code>search</code> and <code>execute</code> MCP tools from an OpenAPI spec with host-side request proxying and automatic <code>$ref</code> resolution.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17652.md")</div>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-zero-dependency-main-entry-point">Zero-dependency main entry point</h4>
<p><strong>Breaking change in v0.2.0:</strong> <code>generateTypes</code> and the <code>ToolDescriptor</code> / <code>ToolDescriptors</code> types have moved to <code>@cloudflare/codemode/ai</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17653.md")</div>
<p>The main entry point (<code>@cloudflare/codemode</code>) no longer requires the <code>ai</code> or <code>zod</code> peer dependencies. It now exports:</p>
<table>
<thead>
<tr>
<th>Export</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sanitizeToolName</code></td>
<td>Sanitize tool names into valid JS identifiers</td>
</tr>
<tr>
<td><code>normalizeCode</code></td>
<td>Normalize LLM-generated code into async arrow functions</td>
</tr>
<tr>
<td><code>generateTypesFromJsonSchema</code></td>
<td>Generate TypeScript type definitions from plain JSON Schema</td>
</tr>
<tr>
<td><code>jsonSchemaToType</code></td>
<td>Convert a single JSON Schema to a TypeScript type string</td>
</tr>
<tr>
<td><code>DynamicWorkerExecutor</code></td>
<td>Sandboxed code execution via Dynamic Worker Loader</td>
</tr>
<tr>
<td><code>ToolDispatcher</code></td>
<td>RPC target for dispatching tool calls from sandbox to host</td>
</tr>
</tbody>
</table>
<p>The <code>ai</code> and <code>zod</code> peer dependencies are now optional — only required when importing from <code>@cloudflare/codemode/ai</code>.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-custom-sandbox-modules">Custom sandbox modules</h4>
<p><code>DynamicWorkerExecutor</code> now accepts an optional <code>modules</code> option to inject custom ES modules into the sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17654.md")</div>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-internal-normalization-and-sanitization">Internal normalization and sanitization</h4>
<p><code>DynamicWorkerExecutor</code> now normalizes code and sanitizes tool names internally. You no longer need to call <code>normalizeCode()</code> or <code>sanitizeToolName()</code> before passing code and functions to <code>execute()</code>.</p>
<h4 id="2026-03-17-codemode-sdk-v0.2.1-upgrade">Upgrade</h4>
<pre><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for the full API reference.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-17">Mar 17, 2026</time><div>
<h2 id="post-2026-03-17-collect-log-payload-header"><a href="/changelog/post/2026-03-17-collect-log-payload-header/">Log AI Gateway request metadata without storing payloads</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway now supports the <code>cf-aig-collect-log-payload</code> header, which controls whether request and response bodies are stored in logs. By default, this header is set to <code>true</code> and payloads are stored alongside metadata. Set this header to <code>false</code> to skip payload storage while still logging metadata such as token counts, model, provider, status code, cost, and duration.</p>
<p>This is useful when you need usage metrics but do not want to persist sensitive prompt or response data.</p>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/$ACCOUNT_ID/$GATEWAY_ID/openai/chat/completions \&#10;  &#45;-header &quot;Authorization: Bearer $TOKEN&quot; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-header &#x27;cf-aig-collect-log-payload: false&#x27; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;gpt-4o-mini&quot;,&#10;    &quot;messages&quot;: [&#10;      {&#10;        &quot;role&quot;: &quot;user&quot;,&#10;        &quot;content&quot;: &quot;What is the email address and phone number of user123?&quot;&#10;      }&#10;    ]&#10;  }&#x27;&#10;</code></pre>
<p>For more information, refer to <a href="/ai-gateway/observability/logging/#collect-log-payload-cf-aig-collect-log-payload">Logging</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-17">Mar 17, 2026</time><div>
<h2 id="post-2026-03-17-new-security-overview-ui"><a href="/changelog/post/2026-03-17-new-security-overview-ui/">New Security Overview UI</a></h2>
<div class="changelog-badges"><span>security-overview</span></div><div class="changelog-body"><p>The Security Overview has been updated to provide Application Security customers with more actionable insights and a clearer view of their security posture.</p>
<p>Key improvements include:</p>
<ul>
<li><strong>Criticality for all Insights</strong>: Every insight now includes a criticality rating, allowing you to prioritize the most impactful security action items first.</li>
<li><strong>Detection Tools Section</strong>: A new section displays the security detection tools available to you, indicating which are currently enabled and which can be activated to strengthen your defenses.</li>
<li><strong>Industry Peer Comparison</strong> (Enterprise customers): A new module from Security Reports benchmarks your security posture against industry peers, highlighting relative strengths and areas for improvement.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-overview/overview-ui.png" alt="New Security Overview UI" /></p>
<p>For more information, refer to <a href="/security/overview/">Security Overview</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-03-16">Mar 16, 2026</time><div>
<h2 id="post-2026-03-16-topk-limit-increased-to-50"><a href="/changelog/post/2026-03-16-topk-limit-increased-to-50/">Return up to 50 query results with values or metadata</a></h2>
<div class="changelog-badges"><span>vectorize</span></div><div class="changelog-body"><p>You can now set <code>topK</code> up to <code>50</code> when a Vectorize query returns values or full metadata. This raises the previous limit of <code>20</code> for queries that use <code>returnValues: true</code> or <code>returnMetadata: &quot;all&quot;</code>.</p>
<p>Use the higher limit when you need more matches in a single query response without dropping values or metadata. Refer to the <a href="/vectorize/reference/client-api/">Vectorize API reference</a> for query options and current <code>topK</code> limits.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/21/">Previous</a><span>Page 22 of 50</span><a class="pagination-next" rel="next" href="/changelog/23/">Next</a></nav>
</div>
