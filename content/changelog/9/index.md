<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-07-10">Jul 10, 2026</time><div>
<h2 id="post-2026-07-13-markdown-conversion-text-output"><a href="/changelog/post/2026-07-13-markdown-conversion-text-output/">Plain text output for Markdown Conversion</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>The <a href="/workers-ai/features/markdown-conversion/">Markdown Conversion</a> service now supports a new <code>output</code> conversion option that controls the format of the converted content.</p>
<p>Set <code>output.format</code> to <code>text</code> to receive plain text with Markdown syntax removed. The default value is <code>markdown</code>, so existing conversions are unchanged.</p>
<p>Use the <a href="/workers-ai/features/markdown-conversion/usage/binding/"><code>env.AI</code></a> binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17819.md")</div>
<p>Or call the REST API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  &#45;F &#x27;files=@index.html&#x27; \&#10;  &#45;F &#x27;conversionOptions={&quot;output&quot;: {&quot;format&quot;: &quot;text&quot;}}&#x27;&#10;</code></pre>
<p>When you request text output, the <code>format</code> field of each result is set to <code>text</code>. For more details, refer to <a href="/workers-ai/features/markdown-conversion/conversion-options/#output">Conversion Options</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-09">Jul 9, 2026</time><div>
<h2 id="post-2026-07-09-dynamic-retry-delays"><a href="/changelog/post/2026-07-09-dynamic-retry-delays/">Workflows now supports delay functions when retrying</a></h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p>With <a href="/workflows/">Workflows</a>, you can configure built-in retry behavior for each step. Previously, you could configure step retries with fixed delay durations, such as seconds, minutes, or hours, and backoff strategies such as <code>constant</code>, <code>linear</code>, or <code>exponential</code>.</p>
<p>Step retries now support dynamic delay functions. Instead of choosing only a base delay and backoff strategy, pass a function to <code>retries.delay</code> and calculate the next delay from the failed attempt and thrown error.</p>
<p>This is useful when retries should depend on the failure. Your Workflow may need to wait longer after a rate-limit error, but retry sooner after a short network failure. The delay function can also accommodate provider guidance if, for example, a downstream API returns a <code>Retry-After</code> value in its error messaging.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17833.md")</div>
<p>Dynamic delay functions can return a duration string, a number, or a promise that resolves to a duration. Use them to add adaptive retry behavior without writing separate queue or scheduling logic. For more information, refer to <a href="/workflows/build/sleeping-and-retrying/">Sleeping and retrying</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-09">Jul 9, 2026</time><div>
<h2 id="post-2026-07-09-warp-wifi-network-performance-analytics"><a href="/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/">Wi-Fi signal and network performance analytics for Cloudflare One Client devices</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment.</p>
<p>The <strong>Device Monitoring</strong> page now analyzes hardware and network data between a Cloudflare One Client device and Cloudflare's edge, so you can diagnose connectivity and performance issues. Previously, this data was only available in raw DEX Device State Event logs, which required you to build your own analytics to interpret it.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-summary.png" alt="Device Monitoring summary with connection status, connection mode, Wi-Fi signal strength, traffic performance, and device health" /></p>
<p>A summary at the top of the page shows the health of each category at a glance, using <strong>Good</strong>, <strong>Fair</strong>, and <strong>Poor</strong> labels:</p>
<ul>
<li><strong>Connection</strong> — connection status, Cloudflare One Client mode, and tunnel type over time</li>
<li><strong>Wi-Fi signal strength</strong> — signal measured in dBm over time, with thresholds that flag a weak signal</li>
<li><strong>Traffic performance</strong> — upstream and downstream performance, including network throughput on the active interface</li>
<li><strong>Device health</strong> — hardware metrics such as CPU, memory, and disk</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-wifi-network.png" alt="Wi-Fi signal strength and network throughput charts on the Device Monitoring page" /></p>
<p>You can filter by category and adjust the time range to correlate a device's metrics with a user's reported issue.</p>
<p>These analytics are available to all Cloudflare One customers at no additional cost.</p>
<p>To learn more, refer to the <a href="/cloudflare-one/insights/dex/monitoring/">DEX monitoring documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-09">Jul 9, 2026</time><div>
<h2 id="post-2026-07-09-new-dns-firewall-ux"><a href="/changelog/post/2026-07-09-new-dns-firewall-ux/">New DNS Firewall UX with more dashboard settings</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>The DNS Firewall page in the Cloudflare dashboard has been refreshed, bringing several settings that were previously API-only into the UI and modernizing how you view and manage your DNS Firewall clusters.</p>
<p><img src="/assets/upstream/images/changelog/dns/dnsfw-new-ux.png" alt="New DNS Firewall UX" /></p>
<h4 id="2026-07-09-new-dns-firewall-ux-what-is-new">What is new</h4>
<ul>
<li><strong>More settings in the dashboard</strong>: cluster options that were previously only configurable through the API — such as attack mitigation, rate limiting, negative TTL, and resolver subnet — are now available directly in the dashboard.</li>
<li><strong>Better table experience</strong>: the DNS Firewall cluster table has been revised to surface cluster details at a glance, with resizable columns and the option to show or hide columns to tailor the view to your workflow.</li>
<li><strong>New create and edit UX</strong>: adding and editing clusters now uses a modernized form that groups related settings together, making configuration faster and clearer.</li>
</ul>
<h4 id="2026-07-09-new-dns-firewall-ux-availability">Availability</h4>
<p>Available to all DNS Firewall customers as part of their existing subscription.</p>
<h4 id="2026-07-09-new-dns-firewall-ux-where-to-find-it">Where to find it</h4>
<p>In the Cloudflare dashboard, go to the <strong>DNS Firewall</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/dns/dns-firewall/">DNS Firewall</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-09">Jul 9, 2026</time><div>
<h2 id="post-2026-07-09-restrict-new-kv-backed-namespaces"><a href="/changelog/post/2026-07-09-restrict-new-kv-backed-namespaces/">New Durable Object namespaces must use the SQLite storage backend</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>If your account does not already have a key-value (KV) backed Durable Object namespace, you can no longer create new ones. New Durable Object namespaces must use the <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend</a>, which has been recommended for all new Durable Objects since it became <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">generally available</a> in 2024.</p>
<p>Create a new class with a <code>new_sqlite_classes</code> migration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17719.md")</div>
<p>SQLite-backed Durable Objects have feature parity with the key-value backend — including the <a href="/durable-objects/api/sqlite-storage-api/#synchronous-kv-api">key-value storage API</a> — and additionally support relational <a href="/durable-objects/api/sqlite-storage-api/#sql-api">SQL queries</a> and <a href="/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api">point-in-time recovery</a> to restore an object's storage to any point in the past 30 days.</p>
<p>If you attempt to create a new key-value backed namespace (a <code>new_classes</code> migration) on an affected account, the deployment fails with the following error:</p>
<pre><code class="language-txt">Creating new key-value backed Durable Object namespaces is no longer supported on this account. Please create a namespace using a `new_sqlite_classes` migration instead.&#10;</code></pre>
<p>This change only affects accounts that are not already using the key-value storage backend. Accounts with at least one existing key-value backed namespace can still create new ones for now, and the Workers Free plan has only ever supported SQLite-backed Durable Objects. It is part of a broader move toward SQLite as the single storage backend for Durable Objects, ahead of a future migration path for existing key-value backed objects.</p>
<p>For more information, refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Objects migrations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-09">Jul 9, 2026</time><div>
<h2 id="post-2026-07-09-tunnel-routes-and-connections-api-changes"><a href="/changelog/post/2026-07-09-tunnel-routes-and-connections-api-changes/">Zero Trust Networks route endpoints and Cloudflare Tunnel connections field retiring on October 5, 2026</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span><span>mesh</span></div><div class="changelog-body"><p>On <strong>October 5, 2026</strong>, two changes take effect across the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> and <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>: the CIDR-encoded route endpoints are removed, and tunnel list and get responses no longer include the <code>connections</code> field. If you manage private network routes or read tunnel connection details through the API, <code>cloudflared</code>, Terraform, or another integration, review the changes in the following sections and migrate before the removal date.</p>
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
<pre><code class="language-bash">&#35; Before: create a route by URL-encoding the CIDR into the path&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/network/172.16.0.0%2F16 \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: create a route with the network in the request body&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;network&quot;: &quot;172.16.0.0/16&quot;, &quot;tunnel_id&quot;: &quot;&#x27;$TUNNEL_ID&#x27;&quot;, &quot;comment&quot;: &quot;Example comment for this route.&quot;}&#x27;&#10;&#10;&#35; After: update or delete a route using its route_id&#10;curl -X PATCH https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &#x27;Content-Type: application/json&#x27; \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;     &#45;d &#x27;{&quot;comment&quot;: &quot;Updated comment for this route.&quot;}&#x27;&#10;&#10;curl -X DELETE https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/routes/$ROUTE_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
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
<pre><code class="language-bash">&#35; Before: read connections off the tunnel object&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;&#35; After: query connections directly&#10;curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/cfd_tunnel/$TUNNEL_ID/connections \&#10;     &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Update any dashboards, monitoring scripts, or automation that parses <code>connections</code> from the tunnel list or get response. <code>cloudflared</code> and the Cloudflare Terraform provider do not read this field, so no changes are required on their side for this part of the update.</p>
<h4 id="2026-07-09-tunnel-routes-and-connections-api-changes-why-we-are-making-these-changes">Why we are making these changes</h4>
<ul>
<li><strong>Smaller, faster responses.</strong> Cloudflare Tunnel and Cloudflare Mesh nodes with many connections no longer inflate every list and get call — connection detail is only fetched when you need it.</li>
<li><strong>A single way to identify a route.</strong> Consolidating on <code>route_id</code> removes the need to URL-encode CIDR ranges into the path and matches how every other resource in the Zero Trust Networks API is addressed.</li>
<li><strong>Consistency across the API.</strong> Both changes align these endpoints with Cloudflare's standard REST conventions for resource identifiers and nested detail endpoints.</li>
</ul>
<p>To learn more, refer to the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a>, the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a>, and <a href="/cloudflare-one/networks/routes/">Routes</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-09">Jul 9, 2026</time><div>
<h2 id="post-2026-07-07-wrangler-deploy-upload-dependencies-metadata"><a href="/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/">Send npm package dependency metadata with Worker uploads</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now collects npm package dependency information from your project's <code>package.json</code> during <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> and <a href="/workers/wrangler/commands/general/#upload"><code>wrangler versions upload</code></a>, and includes it in the upload metadata sent to the Cloudflare API. This data, each dependency's name, declared version range, and exact installed version, enables dependency analytics and future supply chain security features such as vulnerability alerting.</p>
<p>To opt out, set <a href="/workers/wrangler/configuration/#top-level-only-keys"><code>dependencies_instrumentation.enabled</code></a> to <code>false</code> in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17805.md")</div>
<p>For more details, refer to <a href="/workers/wrangler/configuration/#top-level-only-keys">Wrangler configuration</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-08">Jul 8, 2026</time><div>
<h2 id="post-2026-07-08-ai-search-list-items-key-filter"><a href="/changelog/post/2026-07-08-ai-search-list-items-key-filter/">Filter AI Search list items by exact object key</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>In <a href="/ai-search/">AI Search</a>, you can upload files to an instance, or connect a <a href="/ai-search/configuration/data-source/">data source</a> such as an R2 bucket, to make your content searchable with natural language. Each file becomes an <strong>item</strong> identified by an object <strong>key</strong> (its filename or path). The <a href="/ai-search/api/items/rest-api/">list items endpoint</a> returns the items in an instance.</p>
<p>That endpoint now accepts a <code>key</code> query parameter, so you can look up a single item by its exact object key without paging through the full list. This complements the existing <code>item_id</code> filter for when you know the key but not the ID.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances/&lt;INSTANCE_NAME&gt;/items?key=docs/readme.md&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Keys are unique per data source, so combine <code>key</code> with <code>source</code> (for example, <code>source=builtin</code>) to disambiguate when the same key exists across multiple sources.</p>
<p>For more information, refer to <a href="/ai-search/api/items/rest-api/">managing items</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-08">Jul 8, 2026</time><div>
<h2 id="post-2026-07-08-gif-bmp-image-support"><a href="/changelog/post/2026-07-08-gif-bmp-image-support/">Workers AI toMarkdown and AI Search now supports GIF and BMP image conversion</a></h2>
<div class="changelog-badges"><span>workers-ai</span><span>ai-search</span></div><div class="changelog-body"><p>Workers AI <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> (<code>toMarkdown</code>) now supports <code>.gif</code> and <code>.bmp</code> image files, in addition to the JPEG, PNG, WebP, and SVG formats already supported.</p>
<p>GIF and BMP files run through the same <a href="/workers-ai/features/markdown-conversion/how-it-works/#images">image pipeline</a> as other formats. Each image is resized if needed (and for animated GIFs, only the first frame is used), then passed to an object-detection model to identify what it contains. Those detected objects prompt a vision model that writes a natural-language description of the image, which becomes searchable, machine-readable Markdown.</p>
<p><a href="/ai-search/">AI Search</a> uses <code>toMarkdown</code> automatically to process the files it ingests, so any <code>.gif</code> and <code>.bmp</code> files are included the next time your index syncs, with no configuration changes required. This helps when your content mixes formats, for example a support knowledge base full of screenshots or an archive of BMP scans.</p>
<p>Learn more about <a href="/workers-ai/features/markdown-conversion/">Markdown conversion</a> and the full list of <a href="/ai-search/configuration/data-source/#supported-file-types">AI Search's supported file types</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-08">Jul 8, 2026</time><div>
<h2 id="post-2026-07-08-ipsec-downgrade-protection"><a href="/changelog/post/2026-07-08-ipsec-downgrade-protection/">IPsec downgrade protection (beta)</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Cloudflare IPsec now supports the <a href="https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-downgrade-prevention/"><code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code></a> IKEv2 extension to protect against downgrade attacks on IPsec tunnels.</p>
<p>IKEv2's original authentication design has each endpoint sign only its own outbound messages, not the full handshake transcript. A quantum-capable <a href="https://www.cloudflare.com/learning/security/threats/on-path-attack/">on-path attacker</a> can exploit this to bypass post-quantum key exchange by downgrading the connection to classical cryptography. The <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> extension addresses this by having both peers sign the entire handshake transcript during the authentication exchange, preventing an attacker from manipulating the negotiation without detection.</p>
<p>Key details:</p>
<ul>
<li>Available in beta for Cloudflare WAN and Magic Transit IPsec tunnels.</li>
<li>Cloudflare sends the <code>IKE_SA_INIT_FULL_TRANSCRIPT_AUTH</code> notification unconditionally as a responder when the feature flag is enabled.</li>
<li>Both the initiator (your device) and responder (Cloudflare) must support the extension for downgrade protection to be effective.</li>
<li>This feature is currently gated by a per-account feature flag. Contact your account team to turn it on.</li>
</ul>
<p>Refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#improved-downgrade-protection-beta">Downgrade protection</a> for more details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-08">Jul 8, 2026</time><div>
<h2 id="post-2026-07-08-unified-routing-iplist-ids-sip"><a href="/changelog/post/2026-07-08-unified-routing-iplist-ids-sip/">IP lists, IDS, and SIP rules supported in Unified Routing</a></h2>
<div class="changelog-badges"><span>cloudflare-network-firewall</span><span>magic-transit</span><span>cloudflare-wan</span></div><div class="changelog-body"><p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> IP lists, IDS, and SIP rules are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. These features require a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Threat Intel Lists, Rate Limiting, and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-08">Jul 8, 2026</time><div>
<h2 id="post-2026-07-08-query-r2-sql-from-dashboard"><a href="/changelog/post/2026-07-08-query-r2-sql-from-dashboard/">Query R2 Data Catalog tables with R2 SQL from the dashboard</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>You can now query your <a href="/r2-data-catalog/">R2 Data Catalog</a> tables with <a href="/r2-sql/">R2 SQL</a> directly from the Cloudflare dashboard, without installing a CLI or wiring up a client. This makes it easy to explore your <a href="https://iceberg.apache.org/">Apache Iceberg</a> data, validate queries, and inspect results in one place.</p>
<img src="/assets/upstream/images/r2-sql/r2-sql-studio.png" alt="R2 SQL Query Editor" />
<p>To get started, go to <a href="https://dash.cloudflare.com/?to=/:account/data-catalog/overview">R2 Data Catalog</a> in the Cloudflare dashboard and select <strong>Query data</strong> to launch the built-in SQL editor. From there you can:</p>
<ul>
<li><strong>Write and run queries interactively</strong> — Iterate on R2 SQL directly in the browser with syntax highlighting and autocomplete, instead of re-running commands through Wrangler or the REST API.</li>
<li><strong>Explore your data</strong> — Explore your namespaces and tables alongside the editor so you can discover what's queryable without leaving the page or using other tools.</li>
<li><strong>Understand results and performance</strong> — View result sets with per-query statistics, export them, and get helpful <code>EXPLAIN</code> outputs to see exactly how a query runs.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17743.md")</aside>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-08">Jul 8, 2026</time><div>
<h2 id="post-2026-07-08-cloudflare-drag-and-drop"><a href="/changelog/post/2026-07-08-cloudflare-drag-and-drop/">Cloudflare Drop</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="https://cloudflare.com/drop">Cloudflare Drop</a> lets you deploy a static site to Cloudflare without requiring a Cloudflare account to get started.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-08">Jul 8, 2026</time><div>
<h2 id="post-2026-07-08-moondream3.1-workers-ai"><a href="/changelog/post/2026-07-08-moondream3.1-workers-ai/">Moondream 3.1 now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>Partnering with <a href="https://moondream.ai/">Moondream</a> to bring their latest model <a href="/workers-ai/models/moondream3.1-9B-A2B/"><code>@cf/moondream/moondream3.1-9B-A2B</code></a> to Workers AI. Moondream 3.1 is a fast vision language model built on a mixture-of-experts architecture with 9B total parameters and 2B active, delivering frontier-level visual reasoning while retaining fast, cost-efficient inference.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-08">Jul 8, 2026</time><div>
<h2 id="post-2026-07-07-warp-windows-ga"><a href="/changelog/post/2026-07-07-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.850.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix addresses a Windows authentication issue in the embedded WebView2 browser. Single sign-on could fail to use the Windows primary account, causing users to be prompted for an interactive sign-in. The embedded authentication browser now allows SSO providers to use the OS primary account when available.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-07">Jul 7, 2026</time><div>
<h2 id="post-2026-07-07-workflows-billing-updates"><a href="/changelog/post/2026-07-07-workflows-billing-updates/">Workflows pricing adds per-step billing. Step and storage billing to start no earlier than August 10, 2026.</a></h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> pricing now includes per-step billing. Requests and CPU time billing have been enabled since the initial public beta and is not changing.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-07">Jul 7, 2026</time><div>
<h2 id="post-2026-07-07-rdp-file-transfer-beta"><a href="/changelog/post/2026-07-07-rdp-file-transfer-beta/">File transfer controls for browser-based RDP (beta)</a></h2>
<div class="changelog-badges"><span>access</span><span>cloudflare-one</span></div><div class="changelog-body"><p>You can now configure file transfer controls for browser-based RDP with Cloudflare Access, allowing you to restrict whether users can upload or download files between their local machine and the remote Windows server.</p>
<p><img src="/assets/upstream/images/changelog/access/file-transfer-policy-control.png" alt="File transfer connection settings in the Access policy configuration." /></p>
<p>This feature is useful for organizations that support bring-your-own-device (BYOD) policies or third-party contractors using unmanaged devices. By restricting file transfers, you can prevent sensitive data from being moved out of the remote session to a user's personal device.</p>
<h4 id="2026-07-07-rdp-file-transfer-beta-configuration-options">Configuration options</h4>
<p>File transfer controls are configured per policy within your Access application, alongside existing <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings">text clipboard controls</a>. For each policy, you can select one of the following options:</p>
<ul>
<li><strong>Client to remote RDP session allowed</strong> — Users can upload files from their local machine into the browser-based RDP session.</li>
<li><strong>Remote RDP session to client allowed</strong> — Users can download files from the browser-based RDP session to their local machine.</li>
<li><strong>Both directions allowed</strong> — Users can upload and download files between their local machine and the browser-based RDP session.</li>
<li><strong>Disable copying/pasting</strong> — Users are not allowed to transfer files between their local machine and the browser-based RDP session.</li>
</ul>
<p>By default, file transfer is denied for new policies. For existing Access applications created before this feature was available, file transfer remains denied.</p>
<h4 id="2026-07-07-rdp-file-transfer-beta-how-it-works">How it works</h4>
<p>To upload, drag files into the browser window or select the settings gear icon on the left side of the RDP session. To download, copy a file in the remote session and select the settings gear to download it, download multiple files as a zip, or print PDFs to a local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/clipboard-side-panel.png" alt="The clipboard side panel showing files available for transfer." /></p>
<p><img src="/assets/upstream/images/changelog/access/remote-doc-ready-for-download-or-print-local.png" alt="A remote document ready for download or local printing." /></p>
<p>This feature is in beta and available on all Zero Trust plans. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#transfer-files">File transfer for browser-based RDP</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-07">Jul 7, 2026</time><div>
<h2 id="post-2026-07-07-authorization-proxy-endpoint-support"><a href="/changelog/post/2026-07-07-authorization-proxy-endpoint-support/">Browser Isolation support for authorization proxy endpoints</a></h2>
<div class="changelog-badges"><span>browser-isolation</span><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> now supports Gateway <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">authorization proxy endpoints</a>. You can apply <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">HTTP Isolate policies</a> to traffic routed through authorization proxy endpoints, the same way you can for traffic from the Cloudflare One Client.</p>
<p>Previously, only <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a> supported Browser Isolation, and only with non-identity policies. Because authorization proxy endpoints authenticate users through an identity provider, you can now apply identity-based Isolate policies to PAC file-proxied traffic without requiring the Cloudflare One Client.</p>
<p>To get started, <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">create an authorization proxy endpoint</a> and <a href="/cloudflare-one/remote-browser-isolation/isolation-policies/">build an Isolate policy</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-07">Jul 7, 2026</time><div>
<h2 id="post-2026-07-07-browser-run-accessibility-tree-endpoint"><a href="/changelog/post/2026-07-07-browser-run-accessibility-tree-endpoint/">New Browser Run endpoint for accessibility trees</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> now supports a standalone <code>/accessibilityTree</code> endpoint, giving agent and automation workflows direct access to the browser's accessibility tree for a rendered webpage.</p>
<p>An accessibility tree is the browser's structured view of a rendered page: roles, names, states, values, and hierarchy. It is useful for accessibility tooling, but also for AI agents and automation workflows that need page structure without the noise of raw HTML or the cost of screenshots.</p>
<p>For AI agents, this means less inference from pixels and less parsing HTML. You can provide the page structure directly, helping agents identify available elements and determine which actions they can take.</p>
<p>With the new <code>/accessibilityTree</code> endpoint, you can request the accessibility tree directly when you only need the semantic structure of a page. If you need multiple page formats in a single API call, you can use the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code></a> endpoint, which also returns Markdown, HTML, and screenshots.</p>
<pre><code class="language-bash">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;accountId&gt;/browser-run/accessibilityTree&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;result&quot;: {&#10;		&quot;accessibilityTree&quot;: {&#10;			&quot;role&quot;: &quot;RootWebArea&quot;,&#10;			&quot;name&quot;: &quot;Example Domain&quot;,&#10;			&quot;children&quot;: [&#10;				{&#10;					&quot;role&quot;: &quot;heading&quot;,&#10;					&quot;name&quot;: &quot;Example Domain&quot;,&#10;					&quot;level&quot;: 1&#10;				},&#10;				{&#10;					&quot;role&quot;: &quot;link&quot;,&#10;					&quot;name&quot;: &quot;Learn more&quot;&#10;				}&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use <code>interestingOnly</code> to return only semantically meaningful nodes, or <code>root</code> to capture the accessibility tree for a specific subtree.</p>
<p>Refer to the <a href="/browser-run/quick-actions/accessibility-tree-endpoint/"><code>/accessibilityTree</code> documentation</a> for usage examples and supported parameters.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-07">Jul 7, 2026</time><div>
<h2 id="post-2026-07-07-websocket-analytics-dataset"><a href="/changelog/post/2026-07-07-websocket-analytics-dataset/">New WebSocket Analytics Logpush dataset</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Enterprise customers can now push per-connection WebSocket analytics to any <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a> using the new <code>websocket_analytics</code> dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling.</p>
<p>Key fields include:</p>
<ul>
<li><strong><code>ConnectionCloseReason</code></strong> — why the connection ended: <code>peerReset</code>, <code>peerNoError</code>, <code>timedOut</code>, <code>upstreamReset</code>, <code>protocolViolation</code>, <code>unspecifiedError</code>, or <code>none</code>.</li>
<li><strong><code>ConnectionCloseSource</code></strong> — which side initiated the close: <code>upstream</code>, <code>downstream</code>, <code>me</code>, or <code>both</code>.</li>
<li><strong><code>ConnectionTransportCloseCode</code></strong> — the TLS alert code or TCP-level close code for additional precision.</li>
<li><strong><code>RayID</code></strong> — correlate WebSocket connection events with your existing HTTP Request logs.</li>
</ul>
<p>The dataset also includes directional byte counts (<code>BytesSentClient</code>, <code>BytesReceivedClient</code>, <code>BytesSentOrigin</code>, <code>BytesReceivedOrigin</code>), connection timestamps, client IP, colo code, and request metadata from the original WebSocket upgrade.</p>
<p>This data lets you build alerts on connection close patterns — for example, detecting spikes in TCP resets (<code>ConnectionCloseReason == &quot;peerReset&quot;</code>) grouped by host and data center — directly in your existing log analysis tools.</p>
<p>For the full list of available fields, refer to <a href="/logs/logpush/logpush-job/datasets/zone/websocket_analytics/">WebSocket Analytics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-07">Jul 7, 2026</time><div>
<h2 id="post-2026-07-06-r2-data-catalog-delete-warnings"><a href="/changelog/post/2026-07-06-r2-data-catalog-delete-warnings/">R2 Data Catalog warns before you delete data manually</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built directly into your R2 bucket. Iceberg tracks your data through a tree of metadata files, so every insert, update, and delete must go through a catalog transaction. Manually adding, modifying, or deleting objects outside the catalog can leave pointers referencing files that no longer exist, corrupting the table into an inconsistent state that is difficult to recover from.</p>
<p>To help prevent this, the R2 dashboard and Wrangler now warn you when you attempt a manual delete operation on a Data Catalog-enabled bucket.</p>
<h4 id="2026-07-06-r2-data-catalog-delete-warnings-dashboard">Dashboard</h4>
<p>When you try to delete objects from a bucket that has R2 Data Catalog enabled, the dashboard displays a warning explaining that the operation could leave the catalog in an invalid state, with a link to the documentation for deleting data correctly. You can cancel the operation or choose to proceed anyway.</p>
<p><img src="/assets/upstream/images/r2-data-catalog/data-catalog-delete-warning.png" alt="R2 dashboard warning shown before deleting objects from a Data Catalog-enabled bucket" /></p>
<h4 id="2026-07-06-r2-data-catalog-delete-warnings-wrangler">Wrangler</h4>
<p>Wrangler now checks whether a bucket is Data Catalog-enabled before running a delete and warns you before continuing:</p>
<pre><code class="language-txt">Data Catalog is enabled for this bucket. &#10;Proceeding may leave the data catalog in an invalid state. Continue?&#10;</code></pre>
<p>To learn how to safely manage and delete data in your tables, refer to the <a href="/r2-data-catalog/">R2 Data Catalog documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-06">Jul 6, 2026</time><div>
<h2 id="post-2026-07-06-virtual-appliance-self-serve-ui"><a href="/changelog/post/2026-07-06-virtual-appliance-self-serve-ui/">Self-serve registration of Cloudflare One Virtual Appliance in the dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>You can now register a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Virtual Appliance</a> and generate its license key directly from the dashboard, without contacting your account team.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-06-virtual-appliance-self-serve-ui.gif" alt="Registering a Cloudflare One Virtual Appliance and generating its authentication key from the Connectors page" /></p>
<ul>
<li>On the <strong>Connectors</strong> page, select <strong>Add an appliance</strong> and choose <strong>Virtual appliance</strong> to register a virtual appliance and generate its authentication key.</li>
<li>Use <strong>Regenerate authentication key</strong> from a virtual appliance connector's menu to rotate its key. The previous key is immediately and irrevocably revoked.</li>
<li>The authentication key is shown only once — copy and store it securely.</li>
</ul>
<p>This complements the existing <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#register-a-virtual-appliance-and-generate-a-license-key">API and Terraform self-serve workflow</a> for provisioning virtual appliances. Hardware appliances continue to use the existing account-team fulfillment workflow.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/">Configure a Cloudflare One Virtual Appliance</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-04">Jul 4, 2026</time><div>
<h2 id="post-2026-06-30-declarative-do-class-exports"><a href="/changelog/post/2026-06-30-declarative-do-class-exports/">Declare Durable Object class lifecycle with `exports`</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>A new declarative <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field in your Wrangler configuration file replaces the imperative <a href="/durable-objects/reference/durable-object-class-migrations-legacy/"><code>migrations</code></a> array for managing Durable Object class lifecycle. Instead of writing an ordered list of migration steps with unique tags, you declare each Durable Object class your Worker exports and Cloudflare compares that against what's already deployed to determine what Durable Object state needs to be created, renamed, or deleted.</p>
<p>With legacy migrations, renaming <code>ChatRoom</code> to <code>Room</code> requires retaining both tagged steps:</p>
<pre><code class="language-jsonc">{&#10;	&quot;migrations&quot;: [&#10;		{ &quot;tag&quot;: &quot;v1&quot;, &quot;new_sqlite_classes&quot;: [&quot;ChatRoom&quot;] },&#10;		{&#10;			&quot;tag&quot;: &quot;v2&quot;,&#10;			&quot;renamed_classes&quot;: [{ &quot;from&quot;: &quot;ChatRoom&quot;, &quot;to&quot;: &quot;Room&quot; }],&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p>With <code>exports</code>, you instead declare <code>Room</code> as the current class and mark <code>ChatRoom</code> as renamed:</p>
<pre><code class="language-jsonc">{&#10;	&quot;exports&quot;: {&#10;		&quot;ChatRoom&quot;: {&#10;			&quot;type&quot;: &quot;durable-object&quot;,&#10;			&quot;state&quot;: &quot;renamed&quot;,&#10;			&quot;renamed_to&quot;: &quot;Room&quot;,&#10;		},&#10;		&quot;Room&quot;: { &quot;type&quot;: &quot;durable-object&quot;, &quot;storage&quot;: &quot;sqlite&quot; },&#10;	},&#10;}&#10;</code></pre>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-03">Jul 3, 2026</time><div>
<h2 id="post-2026-07-03-workers-types-v5"><a href="/changelog/post/2026-07-03-workers-types-v5/">Simpler runtime types with @cloudflare/workers-types v5</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We have released version 5 of <a href="https://www.npmjs.com/package/@cloudflare/workers-types"><code>@cloudflare/workers-types</code></a>. This release simplifies the package to expose only the latest runtime types.</p>
<p>We still recommend that you generate types for your Worker using <a href="/workers/wrangler/commands/general/#types"><code>wrangler types</code></a>, but if you want to use the package directly, you can install it with your package manager of choice:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/workers-types@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/workers-types@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The package now exposes two entrypoints:</p>
<ul>
<li><code>@cloudflare/workers-types</code> reflects the latest compatibility date, using the latest stable compatibility flags.</li>
<li><code>@cloudflare/workers-types/experimental</code> reflects APIs behind experimental compatibility flags.</li>
</ul>
<p>The dated entrypoints, such as <code>@cloudflare/workers-types/2022-11-30</code> and <code>@cloudflare/workers-types/2023-03-01</code>, are removed. With runtime type generation in <a href="/workers/wrangler/">Wrangler v4</a>, you can generate these with the <code>wrangler types</code> command to create types locked to your Worker's compatibility date.</p>
<p>For more information, refer to <a href="/workers/languages/typescript/">TypeScript language support</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-02">Jul 2, 2026</time><div>
<h2 id="post-2026-07-02-manage-sync-jobs"><a href="/changelog/post/2026-07-02-manage-sync-jobs/">Manage AI Search sync jobs with Wrangler CLI</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>When you connect a <a href="/ai-search/configuration/data-source/">data source</a> to your <a href="/ai-search/">AI Search</a> instance, AI Search runs sync jobs to keep your index up to date with your content. You can now manage those jobs directly from <a href="/ai-search/wrangler-commands/">Wrangler</a>.</p>
<p>For example, you can trigger a sync job from your CI/CD or automated pipelines with the <code>jobs create</code> command so your index refreshes when you push a change:</p>
<pre><code class="language-sh">wrangler ai-search jobs create my-instance&#10;</code></pre>
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
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/8/">Previous</a><span>Page 9 of 50</span><a class="pagination-next" rel="next" href="/changelog/10/">Next</a></nav>
</div>
