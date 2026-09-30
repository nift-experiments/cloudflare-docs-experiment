---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/5/
  description: '2026-07-10'
  full_title: Developer platform changelog - page 5 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 5 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-07-10"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/5/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 5"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-07-10"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/5/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/5/#page","headline":"Developer platform changelog - page 5 | Cloudflare Docs","description":"2026-07-10","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/5/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/5/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="plain-text-output-for-markdown-conversion"><a href="/changelog/post/2026-07-13-markdown-conversion-text-output/">Plain text output for Markdown Conversion</a></h2>
<p><em>2026-07-10</em></p>
<p>The <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service now supports a new <code>output</code> conversion option that controls the format of the converted content.</p>
<p>Set <code>output.format</code> to <code>text</code> to receive plain text with Markdown syntax removed. The default value is <code>markdown</code>, so existing conversions are unchanged.</p>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17819.md")</div>
<p>Or call the REST API:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;output&quot;: {&quot;format&quot;: &quot;text&quot;}}&#x27;&#10;</code></pre>
<p>When you request text output, the <code>format</code> field of each result is set to <code>text</code>. For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/#output">Conversion Options</a>.</p>


<h2 id="workflows-now-supports-delay-functions-when-retrying"><a href="/changelog/post/2026-07-09-dynamic-retry-delays/">Workflows now supports delay functions when retrying</a></h2>
<p><em>2026-07-09 12:00:00 UTC</em></p>
<p>With <a href="/workflows/">Workflows</a>, you can configure built-in retry behavior for each step. Previously, you could configure step retries with fixed delay durations, such as seconds, minutes, or hours, and backoff strategies such as <code>constant</code>, <code>linear</code>, or <code>exponential</code>.</p>
<p>Step retries now support dynamic delay functions. Instead of choosing only a base delay and backoff strategy, pass a function to <code>retries.delay</code> and calculate the next delay from the failed attempt and thrown error.</p>
<p>This is useful when retries should depend on the failure. Your Workflow may need to wait longer after a rate-limit error, but retry sooner after a short network failure. The delay function can also accommodate provider guidance if, for example, a downstream API returns a <code>Retry-After</code> value in its error messaging.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17833.md")</div>
<p>Dynamic delay functions can return a duration string, a number, or a promise that resolves to a duration. Use them to add adaptive retry behavior without writing separate queue or scheduling logic. For more information, refer to <a href="/workflows/build/sleeping-and-retrying/">Sleeping and retrying</a>.</p>


<h2 id="new-durable-object-namespaces-must-use-the-sqlite-storage-backend"><a href="/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/">New Durable Object namespaces must use the SQLite storage backend</a></h2>
<p><em>2026-07-09</em></p>
<p>If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend</a>, which has been recommended for all new Durable Objects since it became <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">generally available</a> in 2024.</p>
<p>Create a new class with a <code>new_sqlite_classes</code> migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17719.md")</div>
<p>SQLite-backed Durable Objects have feature parity with the key-value backend — including the <a href="/durable-objects/api/sqlite-storage-api/#synchronous-kv-api">key-value storage API</a> — and additionally support relational <a href="/durable-objects/api/sqlite-storage-api/#sql-api">SQL queries</a> and <a href="/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api">point-in-time recovery</a> to restore an object's storage to any point in the past 30 days.</p>
<p>If you attempt to create a new key-value backed namespace (a <code>new_classes</code> migration) on an affected account, the deployment fails with the following error:</p>
<pre tabindex="0"><code class="language-txt">Creating new key-value backed Durable Object namespaces is no longer supported on this account. Please create a namespace using a `new_sqlite_classes` migration instead.&#10;</code></pre>
<p>This change only affects accounts that are not already using the key-value storage backend. Accounts with at least one existing key-value backed namespace can still create new ones for now, and the Workers Free plan has only ever supported SQLite-backed Durable Objects. It is part of a broader move toward SQLite as the single storage backend for Durable Objects, ahead of a future migration path for existing key-value backed objects.</p>
<p>For more information, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Objects migrations</a>.</p>


<h2 id="zero-trust-networks-route-endpoints-and-cloudflare-tunnel-connections-field-retiring-on-october-5-2026"><a href="/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/">Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026</a></h2>
<p><em>2026-07-09</em></p>
<p>On <strong>October 5, 2026</strong>, two changes take effect across the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> and <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>: the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the <code>connections</code> field. If you manage private network routes or read tunnel connection details through the API, <code>cloudflared</code>, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-route-endpoints">Route endpoints</h4>
<p>The CIDR-encoded route endpoints are deprecated in favor of the standard, <code>route_id</code>-based endpoints that already exist today. Both sets of endpoints route a private network through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or <a href="/mesh/">Cloudflare Mesh</a> (the API still refers to Mesh nodes as <code>warp_connector</code>) — only the request shape changes.</p>
<p><strong>Deprecated endpoints (removed October 5, 2026):</strong></p>
<ul>
<li>Create a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/create/"><code>POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
<li>Update a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/edit/"><code>PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
<li>Delete a tunnel route (CIDR Endpoint): <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/subresources/networks/methods/delete/"><code>DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></a></li>
</ul>
<p><strong>Replacement endpoints:</strong></p>
<ul>
<li>Create a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/create/"><code>POST /accounts/{account_id}/teamnet/routes</code></a></li>
<li>Update a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/edit/"><code>PATCH /accounts/{account_id}/teamnet/routes/{route_id}</code></a></li>
<li>Delete a tunnel route: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/delete/"><code>DELETE /accounts/{account_id}/teamnet/routes/{route_id}</code></a></li>
</ul>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-what-is-changing">What is changing</h4>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="left">Deprecated (CIDR-encoded path)</th>
<th align="left">Replacement</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Route identifier</td>
<td align="left">URL-encoded CIDR in the path (<code>/network/{ip_network_encoded}</code>)</td>
<td align="left"><code>route_id</code> in the path (<code>network</code> moves to the request body on create)</td>
</tr>
<tr>
<td align="left">Create</td>
<td align="left"><code>POST .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>POST .../teamnet/routes</code> with <code>network</code> and <code>tunnel_id</code> in the body</td>
</tr>
<tr>
<td align="left">Update</td>
<td align="left"><code>PATCH .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>PATCH .../teamnet/routes/{route_id}</code></td>
</tr>
<tr>
<td align="left">Delete</td>
<td align="left"><code>DELETE .../teamnet/routes/network/{ip_network_encoded}</code></td>
<td align="left"><code>DELETE .../teamnet/routes/{route_id}</code></td>
</tr>
</tbody>
</table>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-action-required">Action required</h4>
<ol>
<li>Capture each route's <code>route_id</code> by calling <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/">List tunnel routes</a>, or read it from the response the first time you create a route with the replacement endpoint.</li>
<li>Update any scripts, backend services, or CI/CD pipelines that call the CIDR-encoded endpoints directly.</li>
<li>If you manage routes with the <code>cloudflared tunnel route ip add | delete</code> commands, upgrade <code>cloudflared</code> to the <a href="https://github.com/cloudflare/cloudflared/releases">latest version</a>.</li>
<li>If you manage routes with Terraform, make sure you are on a current version of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/zero_trust_tunnel_cloudflared_route"><code>cloudflare_zero_trust_tunnel_cloudflared_route</code></a> resource and the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a>.</li>
</ol>
<pre tabindex="0"><code class="language-bash">&#35; Before: create a route by URL-encoding the CIDR into the path&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: create a route with the network in the request body&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;network&quot;: &quot;172.16.0.0/16&quot;, &quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: update or delete a route using its route_id&#10;curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;comment&quot;: &quot;Updated comment for this route.&quot;}&#x27;&#10;&#10;curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-cloudflare-tunnel-and-cloudflare-mesh-connections">Cloudflare Tunnel and Cloudflare Mesh connections</h4>
<p>Starting the same day, the <code>connections</code> array is removed from list and get responses for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> nodes (the <code>cfd_tunnel</code> and <code>warp_connector</code> API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.</p>
<p>This affects:</p>
<ul>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a> — <code>connections</code> removed from each item in <code>result</code></li>
<li><a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}</code></a> — <code>connections</code> removed from <code>result</code></li>
</ul>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-action-required-1">Action required</h4>
<p>Fetch connection details from the tunnel-specific connections endpoint instead of parsing it off the list or get response. For Cloudflare Tunnel, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections</code></a>. For Cloudflare Mesh, call <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/subresources/connections/methods/get/"><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections</code></a>.</p>
<pre tabindex="0"><code class="language-bash">&#35; Before: read connections off the tunnel object&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;&#35; After: query connections directly&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Update any dashboards, monitoring scripts, or automation that parses <code>connections</code> from the tunnel list or get response. <code>cloudflared</code> and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-why-we-are-making-these-changes">Why we are making these changes</h4>
<ul>
<li><strong>Smaller, faster responses.</strong> Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.</li>
<li><strong>A single way to identify a route.</strong> Consolidating on <code>route_id</code> removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.</li>
<li><strong>Consistency across the API.</strong> Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.</li>
</ul>
<p>To learn more, refer to the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a>, the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>, and <a href="/cloudflare-one/networks/routes/">Routes</a> documentation.</p>


<h2 id="send-npm-package-dependency-metadata-with-worker-uploads"><a href="/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/">Send npm package dependency metadata with Worker uploads</a></h2>
<p><em>2026-07-09</em></p>
<p>Wrangler now collects npm package dependency information from your project's <code>package.json</code> during <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> and <a href="/workers/wrangler/commands/general/#upload"><code>wrangler versions upload</code></a>, and includes it in the upload metadata sent to the Cloudflare API. This data, each dependency's name, declared version range, and exact installed version, enables dependency analytics and future supply chain security features such as vulnerability alerting.</p>
<p>To opt out, set <a href="/workers/wrangler/configuration/#top-level-only-keys"><code>dependencies_instrumentation.enabled</code></a> to <code>false</code> in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17805.md")</div>
<p>For more details, refer to <a href="/workers/wrangler/configuration/#top-level-only-keys">Wrangler configuration</a>.</p>


<h2 id="filter-ai-search-list-items-by-exact-object-key"><a href="/changelog/post/2026-07-08-ai-search-list-items-key-filter/">Filter AI Search list items by exact object key</a></h2>
<p><em>2026-07-08</em></p>
<p>In <a href="/ai-search/">AI Search</a>, you can upload files to an instance, or connect a <a href="/ai-search/configuration/data-source/">data source</a> such as an R2 bucket, to make your content searchable with natural language. Each file becomes an <strong>item</strong> identified by an object <strong>key</strong> (its filename or path). The <a href="/ai-search/api/items/rest-api/">list items endpoint</a> returns the items in an instance.</p>
<p>That endpoint now accepts a <code>key</code> query parameter, so you can look up a single item by its exact object key without paging through the full list. This complements the existing <code>item_id</code> filter for when you know the key but not the ID.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances/&lt;INSTANCE_NAME&gt;/items?key=docs/readme.md&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Keys are unique per data source, so combine <code>key</code> with <code>source</code> (for example, <code>source=builtin</code>) to disambiguate when the same key exists across multiple sources.</p>
<p>For more information, refer to <a href="/ai-search/api/items/rest-api/">managing items</a>.</p>


<h2 id="workers-ai-tomarkdown-and-ai-search-now-supports-gif-and-bmp-image-conversion"><a href="/changelog/post/2026-07-08-gif-bmp-image-support/">Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion</a></h2>
<p><em>2026-07-08</em></p>
<p>Workers AI <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> (<code>toMarkdown</code>) now supports <code>.gif</code> and <code>.bmp</code> image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.</p>
<p>GIF and BMP files run through the same <a href="/workers-ai/features/markdown-conversion/how-it-works/#images">image pipeline</a> as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.</p>
<p><a href="/ai-search/">AI Search</a> uses <code>toMarkdown</code> automatically to process the files it ingests, so any <code>.gif</code> and <code>.bmp</code> files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.</p>
<p>Learn more about <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> and the full list of <a href="/ai-search/configuration/data-source/#supported-file-types">AI Search's supported file types</a>.</p>


<h2 id="query-r2-data-catalog-tables-with-r2-sql-from-the-dashboard"><a href="/changelog/post/2026-07-08-query-r2-sql-from-dashboard/">Query R2 Data Catalog tables with R2 SQL from the dashboard</a></h2>
<p><em>2026-07-08</em></p>
<p>You can now query your <a href="/r2-data-catalog/">R2 Data Catalog</a> tables with <a href="/r2-sql/">R2 SQL</a> directly from the Cloudflare dashboard, without installing a CLI or wiring up a client. This makes it easy to explore your <a href="https://iceberg.apache.org/">Apache Iceberg</a> data, validate queries, and inspect results in one place.</p>
<img src="/assets/upstream/images/r2-sql/r2-sql-studio.png" alt="R2 SQL Query Editor" />
<p>To get started, go to <a href="https://dash.cloudflare.com/?to=/:account/data-catalog/overview">R2 Data Catalog</a> in the Cloudflare dashboard and select <strong>Query data</strong> to launch the built-in SQL editor. From there you can:</p>
<ul>
<li><strong>Write and run queries interactively</strong> — Iterate on R2 SQL directly in the browser with syntax highlighting and autocomplete, instead of re-running commands through Wrangler or the REST API.</li>
<li><strong>Explore your data</strong> — Explore your namespaces and tables alongside the editor so you can discover what's queryable without leaving the page or using other tools.</li>
<li><strong>Understand results and performance</strong> — View result sets with per-query statistics, export them, and get helpful <code>EXPLAIN</code> outputs to see exactly how a query runs.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17743.md")</aside>


<h2 id="cloudflare-drop"><a href="/changelog/post/2026-07-08-cloudflare-drag-and-drop/">Cloudflare Drop</a></h2>
<p><em>2026-07-08</em></p>
<p><a href="https://cloudflare.com/drop">Cloudflare Drop</a> lets you deploy a static site to Cloudflare without requiring a Cloudflare account to get started.</p>
<p><img src="/assets/upstream/images/workers/changelog/cloudflare-drag-and-drop-upload.png" alt="Cloudflare Drag and Drop upload screen for browsing folders or ZIP files" /></p>
<p>Upload a folder or zip file of static assets (static HTML, CSS, JavaScript, images, and fonts) and get a temporary live preview that stays live for 1 hour. During that window, you can test the site, share the preview URL, or <a href="/workers/platform/claim-deployments/">claim the deployment</a> to keep it.</p>
<p><img src="/assets/upstream/images/workers/changelog/cloudflare-drag-and-drop-preview.png" alt="Cloudflare Drag and Drop temporary live preview screen with claim and copy claim link actions" /></p>
<p>When you are ready to make the deployment permanent, click <strong>Claim</strong> to sign in or create a Cloudflare account. You can claim the site into an existing Cloudflare account or create a new account for the deployment.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17806.md")</aside>
<p><img src="/assets/upstream/images/workers/changelog/cloudflare-drag-and-drop-claim.png" alt="Cloudflare Drag and Drop claim account screen with a countdown before the claim link expires" /></p>
<p>After claiming the site, you can:</p>
<ul>
<li><strong>Add a domain</strong>: <a href="/workers/configuration/routing/custom-domains/">Connect</a> an existing domain or purchase a new one for your site.</li>
<li><strong>Enable <a href="/workers/observability/">observability</a></strong>: Monitor your site's performance and usage.</li>
<li><strong>Enable <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a></strong>: Allow AI agents to access your site's content in Markdown.</li>
<li><strong>Control access</strong>: Make your site <a href="/cloudflare-one/access-controls/policies/">private</a> and choose who can view it.</li>
</ul>
<p><img src="/assets/upstream/images/workers/changelog/cloudflare-drag-and-drop-post-claim.png" alt="Claimed Cloudflare Drag and Drop site setup screen showing options to add a domain, control access, enable observability, and enable Markdown for agents" /></p>


<h2 id="moondream-3-1-now-available-on-workers-ai"><a href="/changelog/post/2026-07-08-moondream3.1-workers-ai/">Moondream 3.1 now available on Workers AI</a></h2>
<p><em>2026-07-08</em></p>
<p>Partnering with <a href="https://moondream.ai/">Moondream</a> to bring their latest model <a href="/workers-ai/models/moondream3.1-9B-A2B/"><code>@cf/moondream/moondream3.1-9B-A2B</code></a> to Workers AI. Moondream 3.1 is a fast vision language model built on a mixture-of-experts architecture with 9B total parameters and 2B active, delivering frontier-level visual reasoning while retaining fast, cost-efficient inference.</p>
<p>Moondream 3.1 is designed for real-world vision tasks, with a 32K token context window for handling complex queries and structured outputs.</p>
<h4 id="2026-07-08-moondream3.1-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Query</strong> — ask open-ended questions about an image, with an optional reasoning parameter</li>
<li><strong>Caption</strong> — generate short, normal, or long descriptions of an image</li>
<li><strong>Point</strong> — return coordinates for objects matching a target phrase</li>
<li><strong>Detect</strong> — return bounding boxes for objects matching a target phrase</li>
</ul>
<h4 id="2026-07-08-moondream3.1-workers-ai-real-time-vision-at-the-edge">Real-time vision at the edge</h4>
<p>Vision workloads like live camera feeds, robotics, content moderation, and interactive agents need answers in milliseconds, not seconds. Moondream 3.1's small active footprint (2B active parameters) pairs well with Workers AI's serverless, globally distributed inference: requests run close to your users, and streaming responses start returning tokens almost immediately.</p>
<p>In our testing, first tokens streamed back in roughly 20–30 ms, and results were fast across every task. The example end-to-end times below (client-observed median, including network round trip) are for a simple, single-subject image. Actual latency depends heavily on the image and how much detail you ask for.</p>
<table>
<thead>
<tr>
<th>Task</th>
<th>End-to-end (p50)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>query</code></td>
<td>~770 ms</td>
</tr>
<tr>
<td><code>caption</code></td>
<td>~480 ms</td>
</tr>
<tr>
<td><code>point</code></td>
<td>~145 ms</td>
</tr>
<tr>
<td><code>detect</code></td>
<td>~160 ms</td>
</tr>
</tbody>
</table>
<p>At these speeds you can call the model inline while handling a request rather than pushing the work to a background queue or a separate service. That opens up use cases where a slow response breaks the experience: moderating user-uploaded images before they are stored, locating an object in a video frame to drive a live overlay, extracting fields from a document during a form submission, or letting an agent inspect a screenshot and decide its next step within a single turn.</p>
<h4 id="2026-07-08-moondream3.1-workers-ai-get-started">Get started</h4>
<p>Use Moondream 3.1 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>) or the REST API at <code>/ai/run</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/moondream3.1-9B-A2B/">Moondream 3.1 model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="workflows-pricing-adds-per-step-billing-step-and-storage-billing-to-start-no-earlier-than-august-10-2026"><a href="/changelog/post/2026-07-07-workflows-billing-updates/">Workflows pricing adds per-step billing. Step and storage billing to start no earlier than August 10, 2026.</a></h2>
<p><em>2026-07-07T12:00:00</em></p>
<p><a href="/workflows/">Workflows</a> pricing now includes per-step billing. Requests and CPU time billing have been enabled since the initial public beta and is not changing.</p>
<h4 id="2026-07-07-workflows-billing-updates-workflows-adds-step-billing">Workflows adds step billing</h4>
<p>A step is each unit of work executed by a Workflow, including step operations such as <a href="/workflows/build/sleeping-and-retrying/">sleeping</a> or <a href="/workflows/build/events-and-parameters/">waiting for events</a>.</p>
<p>You can query Workflows analytics, including <code>stepCount</code> for a Workflow instance, with the <a href="/workflows/observability/metrics-analytics/#query-via-the-graphql-api">GraphQL Analytics API</a>.</p>
<h4 id="2026-07-07-workflows-billing-updates-steps-and-storage-billing-to-take-effect-august-10th-2026">Steps and storage billing to take effect August 10th, 2026</h4>
<p>Starting no earlier than August 10th, 2026, Cloudflare will begin billing for step and storage usage on Workers Paid plans.</p>
<p>Storage pricing has been published since Workflows became generally available and is not changing.  Storage is measured as persisted Workflow state in GB-months.</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Steps</td>
<td>3,000 included per day</td>
<td>500,000 included per month, then $0.80 per additional 100,000 steps</td>
</tr>
<tr>
<td>Storage</td>
<td>1 GB-month included</td>
<td>1 GB-month included, then $0.20 per additional GB-month</td>
</tr>
</tbody>
</table>
<p>Developers on the Workers Free plan will not be charged for steps or storage beyond the included amounts.</p>
<p>Cloudflare will not bill step and storage usage before August 10, 2026.</p>
<p>You can review Workflows usage in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> before this change takes effect. To reduce costs, consider reducing the number of steps per Workflow or improving the memory efficiency of your stored state.</p>
<p>Refer to the <a href="/workflows/reference/pricing/">Workflows pricing</a> page for full details.</p>


<h2 id="new-browser-run-endpoint-for-accessibility-trees"><a href="/changelog/post/2026-07-07-browser-run-accessibility-tree-endpoint/">New Browser Run endpoint for accessibility trees</a></h2>
<p><em>2026-07-07</em></p>
<p><a href="/browser-run/">Browser Run</a> now supports a standalone <code>/accessibilityTree</code> endpoint, giving agent and automation workflows direct access to the browser's accessibility tree for a rendered webpage.</p>
<p>An accessibility tree is the browser's structured view of a rendered page: roles, names, states, values, and hierarchy. It is useful for accessibility tooling, but also for AI agents and automation workflows that need page structure without the noise of raw HTML or the cost of screenshots.</p>
<p>For AI agents, this means less inference from pixels and less parsing HTML. You can provide the page structure directly, helping agents identify available elements and determine which actions they can take.</p>
<p>With the new <code>/accessibilityTree</code> endpoint, you can request the accessibility tree directly when you only need the semantic structure of a page. If you need multiple page formats in a single API call, you can use the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code></a> endpoint, which also returns Markdown, HTML, and screenshots.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-run/accessibilityTree&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;accessibilityTree&quot;: {&#10;			&quot;role&quot;: &quot;RootWebArea&quot;,&#10;			&quot;name&quot;: &quot;Example Domain&quot;,&#10;			&quot;children&quot;: [&#10;				{&#10;					&quot;role&quot;: &quot;heading&quot;,&#10;					&quot;name&quot;: &quot;Example Domain&quot;,&#10;					&quot;level&quot;: 1&#10;				},&#10;				{&#10;					&quot;role&quot;: &quot;link&quot;,&#10;					&quot;name&quot;: &quot;Learn more&quot;&#10;				}&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use <code>interestingOnly</code> to return only semantically meaningful nodes, or <code>root</code> to capture the accessibility tree for a specific subtree.</p>
<p>Refer to the <a href="/browser-run/quick-actions/accessibility-tree-endpoint/"><code>/accessibilityTree</code> documentation</a> for usage examples and supported parameters.</p>


<h2 id="r2-data-catalog-warns-before-you-delete-data-manually"><a href="/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/">R2 Data Catalog warns before you delete data manually</a></h2>
<p><em>2026-07-07</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built directly into your R2 bucket. Iceberg tracks your data through a tree of metadata files, so every insert, update, and delete must go through a catalog transaction. Manually adding, modifying, or deleting objects outside the catalog can leave pointers referencing files that no longer exist, corrupting the table into an inconsistent state that is difficult to recover from.</p>
<p>To help prevent this, the R2 dashboard and Wrangler now warn you when you attempt a manual delete operation on a Data Catalog-enabled bucket.</p>
<h4 id="2026-07-06-r2-data-catalog-delete-warnings-dashboard">Dashboard</h4>
<p>When you try to delete objects from a bucket that has R2 Data Catalog enabled, the dashboard displays a warning explaining that the operation could leave the catalog in an invalid state, with a link to the documentation for deleting data correctly. You can cancel the operation or choose to proceed anyway.</p>
<p><img src="/assets/upstream/images/r2-data-catalog/data-catalog-delete-warning.png" alt="R2 dashboard warning shown before deleting objects from a Data Catalog-enabled bucket" /></p>
<h4 id="2026-07-06-r2-data-catalog-delete-warnings-wrangler">Wrangler</h4>
<p>Wrangler now checks whether a bucket is Data Catalog-enabled before running a delete and warns you before continuing:</p>
<pre tabindex="0"><code class="language-txt">Data Catalog is enabled for this bucket. &#10;Proceeding may leave the data catalog in an invalid state. Continue?&#10;</code></pre>
<p>To learn how to safely manage and delete data in your tables, refer to the <a href="/r2-data-catalog/">R2 Data Catalog documentation</a>.</p>


<h2 id="declare-durable-object-class-lifecycle-with-exports"><a href="/changelog/post/2026-06-30-declarative-do-class-exports/">Declare Durable Object class lifecycle with `exports`</a></h2>
<p><em>2026-07-04</em></p>
<p>A new declarative <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field in your Wrangler configuration file replaces the imperative <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array for managing Durable Object class lifecycle. Instead of writing an ordered list of migration steps with unique tags, you declare each Durable Object class your Worker exports and Cloudflare compares that against what's already deployed to determine what Durable Object state needs to be created, renamed, or deleted.</p>
<p>With legacy migrations, renaming <code>ChatRoom</code> to <code>Room</code> requires retaining both tagged steps:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;migrations&quot;: [&#10;		{ &quot;tag&quot;: &quot;v1&quot;, &quot;new_sqlite_classes&quot;: [&quot;ChatRoom&quot;] },&#10;		{&#10;			&quot;tag&quot;: &quot;v2&quot;,&#10;			&quot;renamed_classes&quot;: [{ &quot;from&quot;: &quot;ChatRoom&quot;, &quot;to&quot;: &quot;Room&quot; }],&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>With <code>exports</code>, you instead declare <code>Room</code> as the current class and mark <code>ChatRoom</code> as renamed:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;exports&quot;: {&#10;		&quot;ChatRoom&quot;: {&#10;			&quot;type&quot;: &quot;durable-object&quot;,&#10;			&quot;state&quot;: &quot;renamed&quot;,&#10;			&quot;renamed_to&quot;: &quot;Room&quot;,&#10;		},&#10;		&quot;Room&quot;: { &quot;type&quot;: &quot;durable-object&quot;, &quot;storage&quot;: &quot;sqlite&quot; },&#10;	},&#10;}&#10;</code></pre>
<p>Each entry is keyed by class name. The <code>state</code> field carries the lifecycle (<code>created</code> by default — a live class — plus tombstone states <code>deleted</code>, <code>renamed</code>, and <code>transferred</code>, and the <code>expecting-transfer</code> receiving state for cross-Worker transfers).</p>
<p>Key improvements over the legacy <code>migrations</code> array:</p>
<ul>
<li><strong>No migration tags.</strong> The current <code>exports</code> map is the source of truth — there is no historical chain of <code>v1</code>, <code>v2</code>, <code>v3</code> entries to maintain.</li>
<li><strong>Structured deployment output.</strong> Wrangler reports when it creates, updates, deletes, renames, or transfers Durable Object classes. It also identifies stale configuration entries that are safe to remove. Deployments with no changes or notices do not print this output.</li>
<li><strong>Zero-downtime rename and transfer patterns are first-class.</strong> Tombstones may coexist with the source class still in code, enabling a <a href="/durable-objects/reference/durable-objects-migrations/#avoid-downtime-during-a-rename">three-deploy rename</a> and a <a href="/durable-objects/reference/durable-objects-migrations/#transfer-a-durable-object-class-between-workers">four-deploy cross-Worker transfer</a> without runtime errors during the rollout window.</li>
<li><strong>Cross-Worker safety.</strong> When you delete or rename a class, Cloudflare lists every other Worker in your account whose bindings still reference the namespace, so you can redeploy them before the change goes live.</li>
</ul>
<p>Existing Workers using the legacy <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array continue to work unchanged. To move to <code>exports</code>, refer to the <a href="/durable-objects/reference/durable-objects-migrations/#migrate-from-the-legacy-migrations-flow">migration guide</a>. <code>exports</code> and <code>migrations</code> are mutually exclusive within a single Worker.</p>
<p>For the full reference, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Object class exports</a>.</p>


<h2 id="simpler-runtime-types-with-cloudflare-workers-types-v5"><a href="/changelog/post/2026-07-03-workers-types-v5/">Simpler runtime types with @cloudflare/workers-types v5</a></h2>
<p><em>2026-07-03</em></p>
<p>We have released version 5 of <a href="https://www.npmjs.com/package/@cloudflare/workers-types"><code>@cloudflare/workers-types</code></a>. This release simplifies the package to expose only the latest runtime types.</p>
<p>We still recommend that you generate types for your Worker using <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a>, but if you want to use the package directly, you can install it with your package manager of choice:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The package now exposes two entrypoints:</p>
<ul>
<li><code>@cloudflare/workers-types</code> reflects the latest compatibility date, using the latest stable compatibility flags.</li>
<li><code>@cloudflare/workers-types/experimental</code> reflects APIs behind experimental compatibility flags.</li>
</ul>
<p>The dated entrypoints, such as <code>@cloudflare/workers-types/2022-11-30</code> and <code>@cloudflare/workers-types/2023-03-01</code>, are removed. With runtime type generation in <a href="/workers/wrangler/">Wrangler v4</a>, you can generate these with the <code>wrangler types</code> command to create types locked to your Worker's compatibility date.</p>
<p>For more information, refer to <a href="/workers/languages/typescript/">TypeScript language support</a>.</p>


<h2 id="manage-ai-search-sync-jobs-with-wrangler-cli"><a href="/changelog/post/2026-07-02-manage-sync-jobs/">Manage AI Search sync jobs with Wrangler CLI</a></h2>
<p><em>2026-07-02</em></p>
<p>When you connect a <a href="/ai-search/configuration/data-source/">data source</a> to your <a href="/ai-search/">AI Search</a> instance, AI Search runs sync jobs to keep your index up to date with your content. You can now manage those jobs directly from <a href="/ai-search/wrangler-commands/">Wrangler</a>.</p>
<p>For example, you can trigger a sync job from your CI/CD or automated pipelines with the <code>jobs create</code> command so your index refreshes when you push a change:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search jobs create my-instance&#10;</code></pre>
<p>This creates an asynchronous sync job that checks for changes in your data source, and sends new, modified, or deleted files to be indexed.
The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search jobs create</code></td>
<td>Trigger a new sync job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs list</code></td>
<td>List sync jobs for an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs get</code></td>
<td>Get details for a job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs cancel</code></td>
<td>Cancel a running job</td>
</tr>
<tr>
<td><code>wrangler ai-search jobs logs</code></td>
<td>View log entries for a job</td>
</tr>
</tbody>
</table>
<p>All commands accept <code>--namespace</code>/<code>-n</code> (defaults to <code>default</code>) and <code>--json</code> for structured output that automation and AI agents can parse directly. The <code>list</code> and <code>logs</code> commands also support <code>--page</code> and <code>--per-page</code> for pagination, and <code>cancel</code> prompts for confirmation unless you pass <code>-y</code>/<code>--force</code>.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>


<h2 id="work-across-multiple-accounts-with-wrangler-auth-profiles"><a href="/changelog/post/2026-07-02-wrangler-auth-profiles/">Work across multiple accounts with Wrangler auth profiles</a></h2>
<p><em>2026-07-02</em></p>
<p><a href="/workers/wrangler/">Wrangler CLI</a> now supports auth profiles: named logins that you scope to specific Cloudflare accounts and switch between automatically, based on the directory you are working in.</p>
<p>A profile is a named OAuth login bound to a directory. Commands run in that directory, and its subdirectories, use the matching account — so you can move between accounts without re-running <code>wrangler login</code>.</p>
<p>Use profiles to keep a separate login for each client when working at an agency, or to separate staging and production into different accounts. Pair a profile with an <code>account_id</code> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> so a command cannot reach the wrong account.</p>
<pre tabindex="0"><code class="language-sh">&#35; Create a profile for each account, choosing which accounts it can reach&#10;wrangler auth create client-a&#10;wrangler auth activate client-a ~/clients/client-a&#10;&#10;wrangler auth create client-b&#10;wrangler auth activate client-b ~/clients/client-b&#10;</code></pre>
<p>Use the <code>--profile</code> flag to run a single command with a specific profile:</p>
<pre tabindex="0"><code class="language-sh">wrangler deploy --profile personal&#10;</code></pre>
<p>In CI and other automated environments, <code>CLOUDFLARE_API_TOKEN</code> still takes precedence over all profiles.</p>
<p>For setup, the resolution order, and the full command reference, refer to <a href="/workers/wrangler/profiles/">Authentication profiles</a>.</p>


<h2 id="use-google-artifact-registry-images-with-containers"><a href="/changelog/post/2026-07-01-google-artifact-registry-images/">Use Google Artifact Registry images with Containers</a></h2>
<p><em>2026-07-01</em></p>
<p>Containers now support <a href="https://cloud.google.com/artifact-registry">Google Artifact Registry</a> images. After you configure credentials, you can use a fully qualified Google Artifact Registry image reference in your <a href="/workers/wrangler/configuration/#containers">Wrangler configuration</a> instead of first pushing the image to Cloudflare Registry.</p>
<p>Provide the service account email with <code>--gar-email</code> and pipe the service account JSON key through <code>stdin</code>:</p>
<pre tabindex="0"><code class="language-bash">cat &lt;PATH_TO_KEY&gt; | npx wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt; --secret-name=&lt;SECRET_NAME&gt;&#10;</code></pre>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17714.md")</div>
<p>Only <code>*-docker.pkg.dev</code> hosts are supported. To configure credentials, refer to <a href="/containers/guides/image-management/#use-private-google-artifact-registry-images">Use private Google Artifact Registry images</a>.</p>
<p>For more information, refer to <a href="/containers/guides/image-management/">Image management</a>.</p>


<h2 id="images-binding-is-now-billed-per-unique-transformation"><a href="/changelog/post/2026-07-01-binding-unique-transformations/">Images binding is now billed per unique transformation</a></h2>
<p><em>2026-07-01</em></p>
<p>The <a href="/images/optimization/binding/">Images binding</a> is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.</p>
<p>Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.</p>
<p>Calls to <a href="/images/optimization/binding/#infostream"><code>.info()</code></a> are no longer billed.</p>
<p>For more information, refer to <a href="/images/pricing/#images-transformed">Images pricing</a> and the <a href="/images/optimization/binding/">Images binding documentation</a>.</p>


<h2 id="reduced-end-to-end-latency-for-vector-changes"><a href="/changelog/post/2026-06-30-improved-wal-throughput/">Reduced end-to-end latency for vector changes</a></h2>
<p><em>2026-07-01</em></p>
<p>We have greatly improved the throughput of the Vectorize <a href="https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/#the-wal">write-ahead log (WAL)</a>. As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes.</p>
<p><img src="/assets/upstream/images/vectorize/vectorize-p99-wal-batch-end-to-end-latency-improvement.png" alt="Vectorize p99 WAL batch end-to-end latency improved" /></p>
<p>This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads. You do not need to change your code or configuration to benefit from this improvement.</p>
<p>For more information, refer to the <a href="/vectorize/">Vectorize documentation</a>.</p>


<h2 id="track-memory-usage-for-workers-and-durable-objects-in-the-dashboard"><a href="/changelog/post/2026-06-30-memory-usage-metrics/">Track memory usage for Workers and Durable Objects in the dashboard</a></h2>
<p><em>2026-06-30</em></p>
<p>You can now monitor how much memory your <a href="/workers/">Workers</a> and <a href="/durable-objects/">Durable Objects</a> consume across invocations with the new <strong>Memory Usage</strong> chart in the Workers Metrics tab, broken down by P50, P90, P99, and P999 percentiles.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-06-26-memory-usage.png" alt="Memory usage chart showing P50, P90, P99, and P999 percentiles with deployment markers" /></p>
<p>Memory usage measures the V8 <a href="/workers/reference/how-workers-works/#isolates">isolate</a> memory at the time of each invocation, subject to the <a href="/workers/platform/limits/#memory">128 MB per-isolate limit</a> — a single isolate can handle many concurrent requests and shares memory across them.</p>
<p>Use the Memory Usage chart to:</p>
<ul>
<li><strong>Track memory trends</strong> — Spot gradual increases that may indicate a memory leak before they cause <code>Exceeded Memory</code> errors.</li>
<li><strong>Correlate with deployments</strong> — Deployment markers on the chart help you identify whether a new version introduced a memory regression.</li>
<li><strong>Right-size your Worker</strong> — Understand your baseline memory footprint and how much headroom you have before hitting the 128 MB limit.</li>
</ul>
<p>For Durable Objects, memory usage reflects the in-memory state an object holds (class properties, caches, active WebSocket connections), which persists across invocations until the object is <a href="/durable-objects/concepts/durable-object-lifecycle/">hibernated or evicted</a>. This state is not preserved across eviction, hibernation, or a crash, so persist anything important to <a href="/durable-objects/best-practices/access-durable-objects-storage/">storage</a>.</p>
<p>To view memory usage, open the <strong>Metrics</strong> tab for your <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics">Worker</a> or <a href="https://dash.cloudflare.com/?to=/:account/workers/durable-objects">Durable Object namespace</a>. For Durable Objects, you can filter by DO ID or name to drill down into memory usage for a specific object. You can also query memory usage programmatically via the <a href="/analytics/graphql-api/tutorials/querying-workers-metrics/">GraphQL Analytics API</a> using the <code>workersInvocationsAdaptive</code> dataset — the <code>quantiles.memoryUsageBytesP50</code> through <code>quantiles.memoryUsageBytesP999</code> fields return percentile values in bytes.</p>
<p>For local memory debugging, you can also <a href="/workers/observability/dev-tools/memory-usage/">profile memory with DevTools</a> to take heap snapshots and identify specific objects causing high memory usage.</p>


<h2 id="workers-fetch-requests-now-support-cf-vary"><a href="/changelog/post/2026-06-28-cf-vary-request-option/">Workers fetch requests now support cf.vary</a></h2>
<p><em>2026-06-28</em></p>
<p>Workers <code>fetch()</code> requests now support the <code>cf.vary</code> request option. Use <code>cf.vary</code> to control how Cloudflare caches origin responses with a <code>Vary</code> header for a single subrequest.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17804.md")</div>
<p>For more information, refer to <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a>.</p>


<h2 id="agents-sdk-adds-background-sub-agents-and-a-unified-turn-entry-point"><a href="/changelog/post/2026-06-26-agents-sdk-v0.17.0/">Agents SDK adds background sub-agents and a unified turn entry point</a></h2>
<p><em>2026-06-26</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> makes it easier to run long work in the background, drive turns through one entry point, and keep chat agents working through deploys, evictions, and reconnects.</p>
<p>This release adds first-class detached (background) sub-agent runs with live progress and durable milestones, a single <code>runTurn</code> turn-admission entry point, and a large round of recovery and reliability fixes that continue converging <code>@cloudflare/think</code> and <code>@cloudflare/ai-chat</code> onto one model.</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-background-sub-agents-with-progress-and-milestones">Background sub-agents with progress and milestones</h4>
<p><code>runAgentTool</code> can now dispatch a sub-agent without blocking the calling turn. A detached run returns a handle immediately and is owned by a durable, eviction-surviving backbone instead of being abandoned when the dispatching turn ends.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17675.md")</div>
<p>Highlights:</p>
<ul>
<li><strong>Durable, exactly-once-on-the-happy-path completion</strong> via a warm fast path plus a self-scheduling reconcile backbone that survives eviction and deploys.</li>
<li><strong>Bounded.</strong> An absolute <code>maxBudgetMs</code> ceiling (default 24h) and <code>cancelAgentTool(runId)</code> keep abandoned runs from holding a concurrency slot forever.</li>
<li><strong><code>detached: { notify: true }</code></strong> lets a finished background run inject a message back into the chat so the model reacts to the result — no hand-wired <code>onFinish</code> needed.</li>
</ul>
<p>Sub-agents can also report mid-run progress that rides their own turn stream back to the parent's connected clients:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17676.md")</div>
<p>Progress surfaces on <code>AgentToolRunState.progress</code> via <code>useAgentToolEvents</code>, so a background-runs tray can render a live bar without drilling in, and the latest snapshot is persisted for inspection after eviction. Naming a <code>milestone</code> promotes a signal to a durable, replayable row, and <code>detached: { onMilestones }</code> can surface a milestone as a synthetic chat message (<code>&quot;narrate&quot;</code> for a cheap status line, or <code>&quot;react&quot;</code> to drive a model turn).</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-one-entry-point-for-turns-runturn">One entry point for turns: <code>runTurn</code></h4>
<p><code>@cloudflare/think</code> adds a public <code>runTurn(options)</code> facade that unifies turn admission behind a single <code>mode</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17677.md")</div>
<p><code>stream</code> mode accepts array and function inputs to match <code>wait</code> mode, and all entry points now route through a shared internal admission path that throws a clear error on nested blocking admissions that previously could deadlock.</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-recovery-and-reliability">Recovery and reliability</h4>
<p>A large part of this release continues hardening recovery and converging <code>@cloudflare/think</code> and <code>@cloudflare/ai-chat</code> onto one model:</p>
<ul>
<li><strong>Stream stall watchdog.</strong> <code>AIChatAgent</code> can detect and recover from a hung model/transport stream via the opt-in <code>chatStreamStallTimeoutMs</code> watchdog. With <code>chatRecovery</code> enabled the stall routes into the same bounded-recovery machinery a deploy or eviction uses; otherwise it surfaces as a terminal stream error so the spinner clears.</li>
<li><strong>Interrupted tool-call repair.</strong> <code>AIChatAgent</code> now repairs a transcript with a dead server-tool call before re-entering inference (parity with <code>@cloudflare/think</code>), so a recovered turn no longer fails with <code>AI_MissingToolResultsError</code>. An overridable <code>repairInterruptedToolPart(part)</code> hook lets apps customize the repaired shape.</li>
<li><strong>Stuck status after reconnect.</strong> Fixed AI SDK <code>status</code> getting stuck when a reconnect races a turn that has been accepted but has not started streaming yet, so the UI now renders the in-flight turn instead of settling on <code>ready</code>.</li>
<li><strong>Live &quot;recovering…&quot; on connect.</strong> <code>AIChatAgent</code> now replays the recovering status to a client that connects mid-recovery, so <code>useAgentChat</code>'s <code>isRecovering</code> reflects in-progress recovery immediately instead of appearing frozen.</li>
<li><strong>Terminal connection failures.</strong> The client stops reconnecting on terminal WebSocket close events and exposes them via <code>connectionError</code> / <code>onConnectionError</code> on <code>AgentClient</code>, <code>useAgent</code>, and <code>useAgentChat</code>.</li>
<li><strong>Agent-tool child recovery.</strong> A healthy long-running sub-agent run is no longer abandoned as <code>interrupted</code> after a deploy (both <code>@cloudflare/think</code> and <code>AIChatAgent</code>).</li>
<li><strong>Workflows from sub-agent facets.</strong> Agent Workflows can now start from sub-agent facets, with callbacks and Workflow RPC routed back to the originating facet.</li>
<li>Plus forward-progress crediting convergence, broadcast-first give-up ordering, an event-driven auto-continuation barrier, and structured row-size compaction in <code>AIChatAgent</code>.</li>
</ul>
<h4 id="2026-06-26-agents-sdk-v0.17.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Shared chat React core.</strong> A new <code>agents/chat/react</code> entry exposes <code>useAgentChat</code>, transport helpers, and shared wire types, with <code>syncMessagesToServer</code> for server-authoritative transcript storage. <code>@cloudflare/think/react</code> and <code>@cloudflare/ai-chat/react</code> are now thin wrappers over it.</li>
<li><strong>Optional <code>ai</code> peer.</strong> The root <code>agents</code> and <code>@cloudflare/codemode</code> runtimes no longer reference AI SDK types, so they bundle without <code>ai</code> / <code>zod</code> installed; AI-specific entry points still require the peer when imported. <code>just-bash</code> likewise moves to an optional peer used only by the skills bash runner.</li>
<li><strong>Code Mode.</strong> The default <code>DynamicWorkerExecutor</code> timeout increases from 30s to 60s, executions now dispose the dynamically-loaded Worker and its RPC stub after each run (fixing a flaky isolate-shutdown assertion), connector imports are cleaned up, and the outer MCP tool-call context is passed to <code>openApiMcpServer</code> request callbacks.</li>
<li><strong>Voice.</strong> Voice turns now support AI SDK <code>fullStream</code> responses (and warn when <code>textStream</code> is used).</li>
<li><strong>MCP.</strong> <code>McpAgent</code> server-to-client requests can now be sent from callbacks that do not inherit the agent's async context, including callbacks reached through Worker Loader RPC.</li>
<li><strong>Experimental: server actions and channels.</strong> This release lays groundwork for guarded server actions (<code>action()</code> / <code>getActions()</code> with a durable replay ledger and approvals) and a unified channels surface (<code>configureChannels()</code>, <code>deliverNotice()</code>). Both are experimental and their APIs may change, so we don't recommend depending on them yet.</li>
</ul>
<h4 id="2026-06-26-agents-sdk-v0.17.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/harnesses/think/">Think documentation</a>, <a href="/agents/tools/codemode/">Code Mode documentation</a>, and <a href="/agents/">Agents documentation</a> for more information.</p>


<h2 id="new-us-jurisdiction-for-durable-objects"><a href="/changelog/post/2026-06-26-durable-objects-us-jurisdiction/">New `us` jurisdiction for Durable Objects</a></h2>
<p><em>2026-06-26</em></p>
<p>Durable Objects now supports a <code>us</code> <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a>, letting you create Durable Objects that only run and store data within the United States. Use the <code>us</code> jurisdiction when you need to keep a Durable Object's compute and storage inside the United States to meet data residency requirements.</p>
<p>Create a namespace restricted to the <code>us</code> jurisdiction the same way as any other jurisdiction:</p>
<pre tabindex="0"><code class="language-js">// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const usSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction(&quot;us&quot;);&#10;		const stub = usSubnamespace.getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>Workers may still access Durable Objects constrained to the <code>us</code> jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data.</p>
<p>For the full list of supported jurisdictions, refer to <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">Data location — Restrict Durable Objects to a jurisdiction</a>.</p>


<h2 id="test-durable-object-eviction-with-new-cloudflare-test-helpers"><a href="/changelog/post/2026-06-25-durable-object-eviction-test-helpers/">Test Durable Object eviction with new cloudflare:test helpers</a></h2>
<p><em>2026-06-25</em></p>
<p>The <code>@cloudflare/vitest-pool-workers</code> package now includes <code>evictDurableObject</code> and <code>evictAllDurableObjects</code> test helpers, exported from <code>cloudflare:test</code>.</p>
<p>These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.</p>
<p>For more context, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
<pre tabindex="0"><code class="language-ts">import { evictDurableObject, evictAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;const id = env.COUNTER.idFromName(&quot;my-counter&quot;);&#10;const stub = env.COUNTER.get(id);&#10;&#10;// Evict the Durable Object instance pointed to by a specific stub&#10;await evictDurableObject(stub);&#10;&#10;// Close WebSockets instead of hibernating them&#10;await evictDurableObject(stub, { webSockets: &quot;close&quot; });&#10;&#10;// Evict all currently-running Durable Objects in evictable namespaces&#10;await evictAllDurableObjects();&#10;</code></pre>
<p>These helpers are available in <code>@cloudflare/vitest-pool-workers@0.16.20</code> and later.</p>
<p>Learn more in the <a href="/workers/testing/vitest-integration/test-apis/#durable-objects">Test APIs reference</a> and the <a href="/durable-objects/examples/testing-with-durable-objects/#testing-eviction">Testing Durable Objects guide</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/4/">Previous</a><span>Page 5 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/6/">Next</a></nav>
