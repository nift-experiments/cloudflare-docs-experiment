---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/storage/3/
  description: '2026-02-23'
  full_title: Storage changelog - page 3 | Cloudflare Docs
  head_html: <title>Storage changelog - page 3 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-02-23"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/storage/3/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Storage changelog - page 3"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-02-23"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/storage/3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/storage/3/#page","headline":"Storage changelog - page 3 | Cloudflare Docs","description":"2026-02-23","url":"https://developers.cloudflare.com/changelog/product-group/storage/3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/storage/3/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="hyperdrive-no-longer-caches-queries-using-stable-postgresql-functions"><a href="/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/">Hyperdrive no longer caches queries using STABLE PostgreSQL functions</a></h2>
<p><em>2026-02-23</em></p>
<p>Hyperdrive now treats queries containing PostgreSQL <code>STABLE</code> functions as uncacheable, in addition to <code>VOLATILE</code> functions.</p>
<p>Previously, only functions <a href="https://www.postgresql.org/docs/current/xfunc-volatility.html">that PostgreSQL categorizes</a> as <code>VOLATILE</code> (for example, <code>RANDOM()</code>, <code>LASTVAL()</code>) were detected as uncacheable. <code>STABLE</code> functions (for example, <code>NOW()</code>, <code>CURRENT_TIMESTAMP</code>, <code>CURRENT_DATE</code>) were incorrectly allowed to be cached.</p>
<p>Because <code>STABLE</code> functions can return different results across different SQL statements within the same transaction, caching their results could serve stale or incorrect data. This change aligns Hyperdrive's caching behavior with PostgreSQL's function volatility semantics.</p>
<p>If your queries use <code>STABLE</code> functions, and you were relying on them being cached, move the function call to your application code and pass the result as a query parameter. For example, instead of <code>WHERE created_at &gt; NOW()</code>, compute the timestamp in your Worker and pass it as <code>WHERE created_at &gt; $1</code>.</p>
<p>Hyperdrive uses text-based pattern matching to detect uncacheable functions. References to function names like <code>NOW()</code> in SQL comments also cause the query to be marked as uncacheable.</p>
<p>For more information, refer to <a href="/hyperdrive/concepts/query-caching/">Query caching</a> and <a href="/hyperdrive/observability/troubleshooting/">Troubleshoot and debug</a>.</p>


<h2 id="cloudflare-queues-now-available-on-workers-free-plan"><a href="/changelog/post/2026-02-04-queues-free-plan/">Cloudflare Queues now available on Workers Free plan</a></h2>
<p><em>2026-02-04</em></p>
<p><a href="/queues">Cloudflare Queues</a> is now part of the Workers free plan, offering guaranteed message delivery across up to <strong>10,000 queues</strong> to either <a href="/workers">Cloudflare Workers</a> or <a href="/queues/configuration/pull-consumers">HTTP pull consumers</a>. Every Cloudflare account now includes <strong>10,000 operations per day</strong> across reads, writes, and deletes. For more details on how each operation is defined, refer to <a href="https://developers.cloudflare.com/workers/platform/pricing/#queues">Queues pricing</a>.</p>
<p>All features of the existing Queues functionality are available on the free plan, including unlimited <a href="/queues/event-subscriptions/">event subscriptions</a>. Note that the maximum retention period on the free tier, however, is 24 hours rather than 14 days.</p>
<p>If you are new to Cloudflare Queues, follow <a href="https://developers.cloudflare.com/queues/get-started/">this guide</a> or try one of our <a href="/queues/tutorials/">tutorials</a> to get started.</p>


<h2 id="improve-global-upload-performance-with-r2-local-uploads-now-in-open-beta"><a href="/changelog/post/2026-02-03-r2-local-uploads/">Improve Global Upload Performance with R2 Local Uploads - Now in Open Beta</a></h2>
<p><em>2026-02-03</em></p>
<p><a href="/r2/buckets/local-uploads/">Local Uploads</a> is now available in open beta. Enable it on your <a href="/r2/">R2</a> bucket to improve upload performance when clients upload data from a different region than your bucket. With Local Uploads enabled, object data is written to storage infrastructure near the client, then asynchronously replicated to your bucket. The object is immediately accessible and remains strongly consistent throughout. Refer to <a href="/r2/how-r2-works/">How R2 works</a> for details on how data is written to your bucket.</p>
<p>In our tests, we observed <strong>up to 75% reduction in Time to Last Byte (TTLB)</strong> for upload requests when Local Uploads is enabled.</p>
<p><img src="/assets/upstream/images/r2/local-uploads-latency.png" alt="Local Uploads latency comparison showing p50 TTLB dropping from around 2 seconds to 500ms after enabling Local Uploads" /></p>
<p>This feature is ideal when:</p>
<ul>
<li>Your users are globally distributed</li>
<li>Upload performance and reliability is critical to your application</li>
<li>You want to optimize write performance without changing your bucket's primary location</li>
</ul>
<p>To enable Local Uploads on your bucket, find <strong>Local Uploads</strong> in your bucket settings in the <a href="https://dash.cloudflare.com/?to=/:account/r2/overview">Cloudflare Dashboard</a>, or run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket local-uploads enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>Enabling Local Uploads on a bucket is seamless: existing uploads will complete as expected and there’s no interruption to traffic. There is no additional cost to enable Local Uploads. Upload requests incur the standard <a href="/r2/pricing/">Class A operation costs</a> same as upload requests made without Local Uploads.</p>
<p>For more information, refer to <a href="/r2/buckets/local-uploads/">Local Uploads</a>.</p>


<h2 id="reduced-minimum-cache-ttl-for-workers-kv-to-30-seconds"><a href="/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/">Reduced minimum cache TTL for Workers KV to 30 seconds</a></h2>
<p><em>2026-01-30T12:00:00+00:00</em></p>
<p>The minimum <code>cacheTtl</code> parameter for Workers KV has been reduced from 60 seconds to 30 seconds. This change applies to both <code>get()</code> and <code>getWithMetadata()</code> methods.</p>
<p>This reduction allows you to maintain more up-to-date cached data and have finer-grained control over cache behavior. Applications requiring faster data refresh rates can now configure cache durations as low as 30 seconds instead of the previous 60-second minimum.</p>
<p>The <code>cacheTtl</code> parameter defines how long a KV result is cached at the global network location it is accessed from:</p>
<pre tabindex="0"><code class="language-js">// Read with custom cache TTL&#10;const value = await env.NAMESPACE.get(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds (previously 60)&#10;});&#10;&#10;// getWithMetadata also supports the reduced cache TTL&#10;const valueWithMetadata = await env.NAMESPACE.getWithMetadata(&quot;my-key&quot;, {&#10;	cacheTtl: 30, // Cache for minimum 30 seconds&#10;});&#10;</code></pre>
<p>The default cache TTL remains unchanged at 60 seconds. Upgrade to the latest version of Wrangler to be able to use 30 seconds <code>cacheTtl</code>.</p>
<p>This change affects all KV read operations using the binding API. For more information, consult the <a href="/kv/api/read-key-value-pairs/#cachettl-parameter">Workers KV cache TTL documentation</a>.</p>


<h2 id="vectorize-indexes-now-support-up-to-10-million-vectors"><a href="/changelog/post/2026-01-23-increased-index-capacity/">Vectorize indexes now support up to 10 million vectors</a></h2>
<p><em>2026-01-23</em></p>
<p>You can now store up to 10 million vectors in a single Vectorize index, doubling the previous limit of 5 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>


<h2 id="new-workers-kv-dashboard-ui"><a href="/changelog/post/2026-01-20-kv-dash-ui-homepage/">New Workers KV Dashboard UI</a></h2>
<p><em>2026-01-20</em></p>
<p><a href="/kv/">Workers KV</a> has an updated dashboard UI with new dashboard styling that makes it easier to navigate and see analytics and settings for a KV namespace.</p>
<p>The new dashboard features a <strong>streamlined homepage</strong> for easy access to your namespaces and key operations, with consistent design with the rest of the dashboard UI updates. It also provides an <strong>improved analytics view</strong>.</p>
<p><img src="/assets/upstream/images/changelog/kv/kv-dash-ui-homepage.png" alt="New KV Dashboard Homepage" /></p>
<p>The updated dashboard is now available for all Workers KV users. Log in to the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a> to start exploring the new interface.</p>


<h2 id="get-notified-when-your-workers-builds-succeed-or-fail"><a href="/changelog/post/2025-12-11-builds-event-subscriptions/">Get notified when your Workers builds succeed or fail</a></h2>
<p><em>2026-01-09</em></p>
<p>You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using <a href="/queues/event-subscriptions/">Event Subscriptions</a>.</p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> publishes events to a <a href="/queues/">Queue</a> that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.</p>
<p>You can deploy <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template">this Worker</a> to your own Cloudflare account to send build notifications to Slack:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The template includes:</p>
<ul>
<li>Build status with Preview/Live URLs for successful deployments</li>
<li>Inline error messages for failed builds</li>
<li>Branch, commit hash, and author name</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/builds-notifications-slack.png" alt="Slack notifications showing build events" /></p>
<p>For setup instructions, refer to the <a href="https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme">template README</a> or the <a href="/queues/event-subscriptions/manage-event-subscriptions/">Event Subscriptions documentation</a>.</p>


<h2 id="r2-data-catalog-now-supports-automatic-snapshot-expiration"><a href="/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/">R2 Data Catalog now supports automatic snapshot expiration</a></h2>
<p><em>2025-12-18</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> now supports automatic snapshot expiration for Apache Iceberg tables.</p>
<p>In Apache Iceberg, a snapshot is metadata that represents the state of a table at a given point in time. Every mutation creates a new snapshot which enable powerful features like time travel queries and rollback capabilities but will accumulate over time.</p>
<p>Without regular cleanup, these accumulated snapshots can lead to:</p>
<ul>
<li>Metadata overhead</li>
<li>Slower table operations</li>
<li>Increased storage costs.</li>
</ul>
<p>Snapshot expiration in R2 Data Catalog automatically removes old table snapshots based on your configured retention policy, improving performance and storage costs.</p>
<pre tabindex="0"><code class="language-bash">&#35; Enable catalog-level snapshot expiration&#10;&#35; Expire snapshots older than 7 days, always retain at least 10 recent snapshots&#10;npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \&#10;  &#45;-older-than-days 7 \&#10;  &#45;-retain-last 10&#10;</code></pre>
<p>Snapshot expiration uses two parameters to determine which snapshots to remove:</p>
<ul>
<li><code>--older-than-days</code>: age threshold in days</li>
<li><code>--retain-last</code>: minimum snapshot count to retain</li>
</ul>
<p>Both conditions must be met before a snapshot is expired, ensuring you always retain recent snapshots even if they exceed the age threshold.</p>
<p>This feature complements <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a>, which optimizes query performance by combining small data files into larger ones. Together, these automatic maintenance operations keep your Iceberg tables performant and cost-efficient without manual intervention.</p>
<p>For more information, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a> or <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>


<h2 id="new-best-practices-guide-for-durable-objects"><a href="/changelog/post/2025-12-15-rules-of-durable-objects/">New Best Practices guide for Durable Objects</a></h2>
<p><em>2025-12-15</em></p>
<p>A new <a href="/durable-objects/best-practices/rules-of-durable-objects/">Rules of Durable Objects</a> guide is now available, providing opinionated best practices for building effective Durable Objects applications. This guide covers design patterns, storage strategies, concurrency, and common anti-patterns to avoid.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Design around your &quot;atom&quot; of coordination</strong> — Create one Durable Object per logical unit (chat room, game session, user) instead of a global singleton that becomes a bottleneck.</li>
<li><strong>Use SQLite storage with RPC methods</strong> — SQLite-backed Durable Objects with typed RPC methods provide the best developer experience and performance.</li>
<li><strong>Understand input and output gates</strong> — Learn how Cloudflare's runtime prevents data races by default, how write coalescing works, and when to use <code>blockConcurrencyWhile()</code>.</li>
<li><strong>Leverage Hibernatable WebSockets</strong> — Reduce costs for real-time applications by allowing Durable Objects to sleep while maintaining WebSocket connections.</li>
</ul>
<p>The <a href="/durable-objects/examples/testing-with-durable-objects/">testing documentation</a> has also been updated with modern patterns using <code>@cloudflare/vitest-pool-workers</code>, including examples for testing SQLite storage, alarms, and direct instance access:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17718.md")</div>


<h2 id="billing-for-sqlite-storage"><a href="/changelog/post/2025-12-12-durable-objects-sqlite-storage-billing/">Billing for SQLite Storage</a></h2>
<p><em>2025-12-12</em></p>
<p>Storage billing for SQLite-backed Durable Objects will be enabled in January 2026, with a target date of January 7, 2026 (no earlier).</p>
<p>To view your SQLite storage usage, go to the <strong>Durable Objects</strong> page</p>
<div class="nb-dash-button"></div>
<p>If you do not want to incur costs, please take action such as optimizing queries or deleting unnecessary stored data in order to reduce your SQLite storage usage ahead of the January 7th target. Only usage on and after the billing target date will incur charges.</p>
<p>Developers on the Workers Paid plan with Durable Object's SQLite storage usage beyond included limits will incur charges according to <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">SQLite storage pricing</a> announced in September 2024 with the <a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">public beta</a>. Developers on the Workers Free plan will not be charged.</p>
<p>Compute billing for SQLite-backed Durable Objects has been enabled since the initial public beta. SQLite-backed Durable Objects currently incur <a href="/durable-objects/platform/pricing/#compute-billing">charges for requests and duration</a>, and no changes are being made to compute billing.</p>
<p>For more information about SQLite storage pricing and limits, refer to the <a href="/durable-objects/platform/pricing/#sqlite-storage-backend">Durable Objects pricing documentation</a>.</p>


<h2 id="connect-to-remote-databases-during-local-development-with-wrangler-dev"><a href="/changelog/post/2025-12-04-hyperdrive-remote-database-local-dev/">Connect to remote databases during local development with wrangler dev</a></h2>
<p><em>2025-12-04</em></p>
<p>You can now connect directly to remote databases and databases requiring TLS with <code>wrangler dev</code>.
This lets you run your Worker code locally while connecting to remote databases, without needing to use <code>wrangler dev --remote</code>.</p>
<p>The <code>localConnectionString</code> field and <code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code> environment variable can be used to configure the connection string used by <code>wrangler dev</code>.</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;  &quot;hyperdrive&quot;: [&#10;    {&#10;      &quot;binding&quot;: &quot;HYPERDRIVE&quot;,&#10;      &quot;id&quot;: &quot;your-hyperdrive-id&quot;,&#10;      &quot;localConnectionString&quot;: &quot;postgres://user:password@remote-host.example.com:5432/database?sslmode=require&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/local-development/">local development with Hyperdrive</a>.</p>


<h2 id="mount-r2-buckets-in-containers"><a href="/changelog/post/2025-11-21-fuse-support-in-containers/">Mount R2 buckets in Containers</a></h2>
<p><em>2025-11-21</em></p>
<p><a href="/containers/">Containers</a> now support mounting R2 buckets as FUSE (Filesystem in Userspace) volumes, allowing applications to interact with <a href="/r2/">R2</a> using standard filesystem operations.</p>
<p>Common use cases include:</p>
<ul>
<li>Bootstrapping containers with datasets, models, or dependencies for <a href="/sandbox/">sandboxes</a> and <a href="/agents/">agent</a> environments</li>
<li>Persisting user configuration or application state without managing downloads</li>
<li>Accessing large static files without bloating container images or downloading at startup</li>
</ul>
<p>FUSE adapters like <a href="https://github.com/tigrisdata/tigrisfs">tigrisfs</a>, <a href="https://github.com/s3fs-fuse/s3fs-fuse">s3fs</a>, and <a href="https://github.com/GoogleCloudPlatform/gcsfuse">gcsfuse</a> can be installed in your container image and configured to mount buckets at startup.</p>
<pre tabindex="0"><code class="language-dockerfile">FROM alpine:3.20&#10;&#10;&#35; Install FUSE and dependencies&#10;RUN apk update &amp;&amp; \&#10;    apk add --no-cache ca-certificates fuse curl bash&#10;&#10;&#35; Install tigrisfs&#10;RUN ARCH=$(uname -m) &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;x86_64&quot; ]; then ARCH=&quot;amd64&quot;; fi &amp;&amp; \&#10;    if [ &quot;$ARCH&quot; = &quot;aarch64&quot; ]; then ARCH=&quot;arm64&quot;; fi &amp;&amp; \&#10;    VERSION=$(curl -s https://api.github.com/repos/tigrisdata/tigrisfs/releases/latest | grep -o &#x27;&quot;tag_name&quot;: &quot;[^&quot;]*&#x27; | cut -d&#x27;&quot;&#x27; -f4) &amp;&amp; \&#10;    curl -L &quot;https://github.com/tigrisdata/tigrisfs/releases/download/${VERSION}/tigrisfs_${VERSION#v}_linux_${ARCH}.tar.gz&quot; -o /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    tar -xzf /tmp/tigrisfs.tar.gz -C /usr/local/bin/ &amp;&amp; \&#10;    rm /tmp/tigrisfs.tar.gz &amp;&amp; \&#10;    chmod +x /usr/local/bin/tigrisfs&#10;&#10;&#35; Create startup script that mounts bucket&#10;RUN printf &#x27;#!/bin/sh\n\&#10;    set -e\n\&#10;    mkdir -p /mnt/r2\n\&#10;    R2_ENDPOINT=&quot;https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com&quot;\n\&#10;    /usr/local/bin/tigrisfs --endpoint &quot;${R2_ENDPOINT}&quot; -f &quot;${BUCKET_NAME}&quot; /mnt/r2 &amp;\n\&#10;    sleep 3\n\&#10;    ls -lah /mnt/r2\n\&#10;    &#x27; &gt; /startup.sh &amp;&amp; chmod +x /startup.sh&#10;&#10;CMD [&quot;/startup.sh&quot;]&#10;</code></pre>
<p>See the <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a> example for a complete guide on mounting R2 buckets and/or other S3-compatible storage buckets within your containers.</p>


<h2 id="d1-can-restrict-data-localization-with-jurisdictions"><a href="/changelog/post/2025-11-05-d1-jurisdiction/">D1 can restrict data localization with jurisdictions</a></h2>
<p><em>2025-11-05</em></p>
<p>You can now set a <a href="/d1/configuration/data-location/">jurisdiction</a> when creating a D1 database to guarantee where your database runs and stores data. Jurisdictions can help you comply with data localization regulations such as GDPR. Supported jurisdictions include <code>eu</code> and <code>fedramp</code>.</p>
<p>A jurisdiction can only be set at database creation time via wrangler, REST API or the UI and cannot be added/updated after the database already exists.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction eu&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/d1/database&quot; \&#10;     &#45;H &quot;Authorization: Bearer $TOKEN&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;-data &#x27;{&quot;name&quot;: &quot;db-with-jurisdiction&quot;, &quot;jurisdiction&quot;: &quot;eu&quot; }&#x27;&#10;</code></pre>
<p>To learn more, visit D1's data location <a href="/d1/configuration/data-location/">documentation</a>.</p>


<h2 id="workers-websocket-message-size-limit-increased-from-1-mib-to-32-mib"><a href="/changelog/post/2025-10-31-increased-websocket-message-size-limit/">Workers WebSocket message size limit increased from 1 MiB to 32 MiB</a></h2>
<p><em>2025-10-31</em></p>
<p>Workers, including those using <a href="/durable-objects/">Durable Objects</a> and <a href="/browser-run/">Browser Rendering</a>, may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.</p>
<p>This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.</p>
<p>For more information, please see the <a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">Durable Objects startup limits</a>.</p>


<h2 id="view-and-edit-durable-object-data-in-ui-with-data-studio-beta"><a href="/changelog/post/2025-10-16-durable-objects-data-studio/">View and edit Durable Object data in UI with Data Studio (Beta)</a></h2>
<p><em>2025-10-16</em></p>
<p><img src="/assets/upstream/images/workers/changelog/do-data-studio.png" alt="Screenshot of Durable Objects Data Studio" /></p>
<p>You can now view and write to each Durable Object's storage using a UI editor on the Cloudflare dashboard. Only Durable Objects using <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage</a> can use Data Studio.</p>
<div class="nb-dash-button"></div>
<p>Data Studio unlocks easier data access with Durable Objects for prototyping application data models to debugging production storage usage. Before, querying your Durable Objects data required deploying a Worker.</p>
<p>To access a Durable Object, you can provide an object's unique name or ID generated by Cloudflare. Data Studio requires you to have at least the <code>Workers Platform Admin</code> role, and all queries are captured with audit logging for your security and compliance needs. Queries executed by Data Studio send requests to your remote, deployed objects and incur normal usage billing.</p>
<p>To learn more, visit the Data Studio <a href="/durable-objects/observability/data-studio/">documentation</a>. If you have feedback or suggestions for the new Data Studio, please share your experience on <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord</a></p>


<h2 id="r2-data-catalog-table-level-compaction"><a href="/changelog/post/2025-10-06-data-catalog-table-compaction/">R2 Data Catalog table-level compaction</a></h2>
<p><em>2025-10-06</em></p>
<p>You can now enable compaction for individual <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>, giving you fine-grained control over different workloads.</p>
<pre tabindex="0"><code class="language-bash">&#35; Enable compaction for a specific table (no token required)&#10;npx wrangler r2 bucket catalog compaction enable &lt;BUCKET&gt; &lt;NAMESPACE&gt; &lt;TABLE&gt; --target-size 256&#10;</code></pre>
<p>This allows you to:</p>
<ul>
<li>Apply different target file sizes per table</li>
<li>Disable compaction for specific tables</li>
<li>Optimize based on table-specific access patterns</li>
</ul>
<p>Learn more at <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>


<h2 id="r2-data-catalog-now-supports-compaction"><a href="/changelog/post/2025-09-25-data-catalog-compaction/">R2 Data Catalog now supports compaction</a></h2>
<p><em>2025-09-25</em></p>
<p>You can now enable automatic compaction for <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a> to improve query performance.</p>
<p>Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.</p>
<p>To enable automatic compaction in R2 Data Catalog, find it under <strong>R2 Data Catalog</strong> in your R2 bucket settings in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/r2/compaction.png" alt="compaction-dash" /></p>
<p>Or with <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 bucket catalog compaction enable &lt;BUCKET_NAME&gt;  --target-size 128 --token &lt;API_TOKEN&gt;&#10;</code></pre>
<p>To get started with compaction, check out <a href="/r2-data-catalog/manage-catalogs/">manage catalogs</a>. For best practices and limitations, refer to <a href="/r2-data-catalog/table-maintenance/">about compaction</a>.</p>


<h2 id="d1-automatically-retries-read-only-queries"><a href="/changelog/post/2025-09-11-d1-automatic-read-retries/">D1 automatically retries read-only queries</a></h2>
<p><em>2025-09-11</em></p>
<p>D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors. You can access the number of execution attempts in the returned <a href="/d1/worker-api/return-object/#d1result">response metadata</a> property <code>total_attempts</code>.</p>
<p>At the moment, only read-only queries are retried, that is, queries containing only the following SQLite keywords: <code>SELECT</code>, <code>EXPLAIN</code>, <code>WITH</code>. Queries containing any <a href="https://sqlite.org/lang_keywords.html">SQLite keyword</a> that leads to database writes are not retried.</p>
<p>The retry success ratio among read-only retryable errors varies from 5% all the way up to 95%, depending on the underlying error and its duration (like network errors or other internal errors).</p>
<p>The retry success ratio among all retryable errors is lower, indicating that there are write-queries that could be retried. Therefore, we recommend D1 users to continue applying <a href="/d1/best-practices/retry-queries/">retries in their own code</a> for queries that are not read-only but are idempotent according to the business logic of the application.</p>
<p><img src="/assets/upstream/images/changelog/d1/d1-auto-retry-success-ratio.png" alt="D1 automatically query retries success ratio" /></p>
<p>D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing changes slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.</p>
<p>The read-only query detection heuristics are simple for now, and there is room for improvement to capture more cases of queries that can be retried, so this is just the beginning.</p>


<h2 id="list-all-vectors-in-a-vectorize-index-with-the-new-list-vectors-operation"><a href="/changelog/post/2025-08-26-vectorize-list-vectors/">List all vectors in a Vectorize index with the new list-vectors operation</a></h2>
<p><em>2025-08-26</em></p>
<p>You can now list all vector identifiers in a Vectorize index using the new <code>list-vectors</code> operation. This enables bulk operations, auditing, and data migration workflows through paginated requests that maintain snapshot consistency.</p>
<p>The operation is available via Wrangler CLI and REST API. Refer to the <a href="/vectorize/best-practices/list-vectors/">list-vectors best practices guide</a> for detailed usage guidance.</p>


<h2 id="workers-kv-completes-hybrid-storage-provider-rollout-for-improved-performance-fault-tolerance"><a href="/changelog/post/2025-08-22-kv-performance-improvements/">Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance</a></h2>
<p><em>2025-08-22 12:00:00 UTC</em></p>
<p>Workers KV has completed rolling out performance improvements across all KV namespaces, providing a significant latency reduction on read operations for all KV users. This is due to architectural changes to KV's underlying storage infrastructure, which introduces a new metadata later and substantially improves redundancy.</p>
<p><img src="/assets/upstream/images/kv/changelog/kv-hybrid-providers-performance-improvements.png" alt="Workers KV latency improvements showing P95 and P99 performance gains in Europe, Asia, Africa and Middle East regions as measured within KV's internal storage gateway worker." /></p>
<h4 id="2025-08-22-kv-performance-improvements-performance-improvements">Performance improvements</h4>
<p>The new hybrid architecture delivers substantial latency reductions throughout Europe, Asia, Middle East, Africa regions. Over the past 2 weeks, we have observed the following:</p>
<ul>
<li><strong>p95 latency</strong>: Reduced from ~150ms to ~50ms (67% decrease)</li>
<li><strong>p99 latency</strong>: Reduced from ~350ms to ~250ms (29% decrease)</li>
</ul>


<h2 id="new-getbyname-api-to-access-durable-objects"><a href="/changelog/post/2025-08-21-durable-objects-get-by-name/">New getByName() API to access Durable Objects</a></h2>
<p><em>2025-08-21</em></p>
<p>You can now create a client (a <a href="/durable-objects/api/stub/">Durable Object stub</a>) to a Durable Object with the new <code>getByName</code> method, removing the need to convert Durable Object names to IDs and then create a stub.</p>
<pre tabindex="0"><code class="language-js">// Before: (1) translate name to ID then (2) get a client &#10;const objectId = env.MY_DURABLE_OBJECT.idFromName(&quot;foo&quot;); // or .newUniqueId()&#10;const stub = env.MY_DURABLE_OBJECT.get(objectId); &#10;&#10;// Now: retrieve client to Durable Object directly via its name &#10;const stub = env.MY_DURABLE_OBJECT.getByName(&quot;foo&quot;);&#10;&#10;// Use client to send request to the remote Durable Object&#10;const rpcResponse = await stub.sayHello();&#10;</code></pre>
<p>Each Durable Object has a globally-unique name, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together. You can have billions of Durable Objects, providing isolation between application tenants.</p>
<p>To learn more, visit the Durable Objects <a href="/durable-objects/api/namespace/#getbyname">API Documentation</a> or the <a href="/durable-objects/get-started/">getting started guide</a>.</p>


<h2 id="subscribe-to-events-from-cloudflare-services-with-queues"><a href="/changelog/post/2025-08-19-event-subscriptions/">Subscribe to events from Cloudflare services with Queues</a></h2>
<p><em>2025-08-19 12:00:00 UTC</em></p>
<p>You can now subscribe to events from other Cloudflare services (for example, <a href="/kv/">Workers KV</a>, <a href="/workers-ai">Workers AI</a>, <a href="/workers">Workers</a>) and consume those events via <a href="/queues/">Queues</a>, allowing you to build custom workflows, integrations, and logic in response to account activity.</p>
<p><img src="/assets/upstream/images/queues/queues-event-subscriptions.png" alt="Event subscriptions architecture" /></p>
<p>Event subscriptions allow you to receive messages when events occur across your Cloudflare account. Cloudflare products can publish structured events to a queue, which you can then consume with <a href="/workers/">Workers</a> or <a href="/queues/configuration/pull-consumers/">pull via HTTP from anywhere</a>.</p>
<p>To create a subscription, use the dashboard or <a href="/workers/wrangler/commands/queues/#queues-subscription-create">Wrangler</a>:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler queues subscription create my-queue --source r2 --events bucket.created&#10;</code></pre>
<p>An event is a structured record of something happening in your Cloudflare account – like a Workers AI batch request being queued, a Worker build completing, or an R2 bucket being created. Events follow a consistent structure:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;type&quot;: &quot;cf.r2.bucket.created&quot;,&#10;  &quot;source&quot;: {&#10;    &quot;type&quot;: &quot;r2&quot;&#10;  },&#10;  &quot;payload&quot;: {&#10;    &quot;name&quot;: &quot;my-bucket&quot;,&#10;    &quot;location&quot;: &quot;WNAM&quot;&#10;  },&#10;  &quot;metadata&quot;: {&#10;    &quot;accountId&quot;: &quot;f9f79265f388666de8122cfb508d7776&quot;,&#10;    &quot;eventTimestamp&quot;: &quot;2025-07-28T10:30:00Z&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Current <a href="/queues/event-subscriptions/events-schemas/">event sources</a> include <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/workers-ai/">Workers AI</a>, <a href="/workers/ci-cd/builds/">Workers Builds</a>, <a href="/vectorize/">Vectorize</a>, <a href="/r2/data-migration/super-slurper/">Super Slurper</a>, and <a href="/workflows/">Workflows</a>. More sources and events are on the way.</p>
<p>For more information on event subscriptions, available events, and how to get started, refer to our <a href="/queues/event-subscriptions/">documentation</a>.</p>


<h2 id="hyperdrive-now-supports-configuring-the-amount-of-database-connections"><a href="/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/">Hyperdrive now supports configuring the amount of database connections</a></h2>
<p><em>2025-07-03</em></p>
<p>You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.</p>
<p>All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the <a href="/hyperdrive/platform/limits/">Hyperdrive limits of your Workers plan</a>.</p>
<p>This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.</p>
<p>Refer to the <a href="/hyperdrive/concepts/connection-pooling/">Hyperdrive configuration documentation</a> for more information.</p>


<h2 id="cloudflare-actors-library-sdk-for-durable-objects-in-beta"><a href="/changelog/post/2025-06-25-actors-package-alpha/">@cloudflare/actors library - SDK for Durable Objects in beta</a></h2>
<p><em>2025-06-25</em></p>
<p>The new <a href="https://www.npmjs.com/package/@cloudflare/actors">@cloudflare/actors</a> library is now in beta!</p>
<p>The <code>@cloudflare/actors</code> library is a new SDK for Durable Objects and provides a powerful set of abstractions for building real-time, interactive, and multiplayer applications on top of Durable Objects. With beta usage and feedback, <code>@cloudflare/actors</code> will become the recommended way to build on Durable Objects and draws upon Cloudflare's experience building products/features on Durable Objects.</p>
<p>The name &quot;actors&quot; originates from the <a href="/durable-objects/concepts/what-are-durable-objects/#actor-programming-model">actor programming model</a>, which closely ties to how Durable Objects are modelled.</p>
<p>The <code>@cloudflare/actors</code> library includes:</p>
<ul>
<li>Storage helpers for querying embeddeded, per-object SQLite storage</li>
<li>Storage helpers for managing SQL schema migrations</li>
<li>Alarm helpers for scheduling multiple alarms provided a date, delay in seconds, or cron expression</li>
<li><code>Actor</code> class for using Durable Objects with a defined pattern</li>
<li>Durable Objects <a href="https://developers.cloudflare.com/durable-objects/api/base/">Workers API</a> is always available for your application as needed</li>
</ul>
<p>Storage and alarm helper methods can be combined with <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#storage--alarms-with-durableobject-class">any Javascript class</a> that defines your Durable Object, i.e, ones that extend <code>DurableObject</code> including the <code>Actor</code> class.</p>
<pre tabindex="0"><code class="language-js">import { Storage } from &quot;@cloudflare/actors/storage&quot;;&#10;&#10;export class ChatRoom extends DurableObject&lt;Env&gt; {&#10;    storage: Storage;&#10;&#10;    constructor(ctx: DurableObjectState, env: Env) {&#10;        super(ctx, env)&#10;        this.storage = new Storage(ctx.storage);&#10;        this.storage.migrations = [{&#10;            idMonotonicInc: 1,&#10;            description: &quot;Create users table&quot;,&#10;            sql: &quot;CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)&quot;&#10;        }]&#10;    }&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        // Run migrations before executing SQL query&#10;        await this.storage.runMigrations();&#10;&#10;        // Query with SQL template&#10;        let userId = new URL(request.url).searchParams.get(&quot;userId&quot;);&#10;        const query = this.storage.sql`SELECT * FROM users WHERE id = ${userId};`&#10;        return new Response(`${JSON.stringify(query)}`);&#10;    }&#10;}&#10;</code></pre>
<p><code>@cloudflare/actors</code> library introduces the <code>Actor</code> class pattern. <code>Actor</code> lets you access Durable Objects without writing the Worker that communicates with your Durable Object (the Worker is created for you). By default, requests are routed to a Durable Object named &quot;default&quot;.</p>
<pre tabindex="0"><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(&#x27;Hello, World!&#x27;)&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>You can <a href="/durable-objects/get-started/#3-instantiate-and-communicate-with-a-durable-object">route</a> to different Durable Objects by name within your <code>Actor</code> class using <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#actor-with-custom-name"><code>nameFromRequest</code></a>.</p>
<pre tabindex="0"><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    static nameFromRequest(request: Request): string {&#10;        let url = new URL(request.url);&#10;        return url.searchParams.get(&quot;userId&quot;) ?? &quot;foo&quot;;&#10;    }&#10;&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(`Actor identifier (Durable Object name): ${this.identifier}`);&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>For more examples, check out the library <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#getting-started">README</a>. <code>@cloudflare/actors</code> library is a place for more helpers and built-in patterns, like retry handling and Websocket-based applications, to reduce development overhead for common Durable Objects functionality. Please share feedback and what more you would like to see on our <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord channel</a>.</p>


<h2 id="automate-worker-deployments-with-a-simplified-sdk-and-more-reliable-terraform-provider"><a href="/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/">Automate Worker deployments with a simplified SDK and more reliable Terraform provider</a></h2>
<p><em>2025-06-19</em></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-simplified-worker-deployments-with-our-sdks">Simplified Worker Deployments with our SDKs</h4>
<p>We've simplified the programmatic deployment of Workers via our <a href="/fundamentals/api/reference/sdks/">Cloudflare SDKs</a>. This update abstracts away the low-level complexities of the <code>multipart/form-data</code> upload process, allowing you to focus on your code while we handle the deployment mechanics.</p>
<p>This new interface is available in:</p>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (4.4.1)</li>
<li><a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (4.3.1)</li>
</ul>
<p>For complete examples, see our guide on <a href="/workers/platform/infrastructure-as-code">programmatic Worker deployments</a>.</p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-the-old-way-manual-api-calls">The Old way: Manual API calls</h4>
<p>Previously, deploying a Worker programmatically required manually constructing a <code>multipart/form-data</code> HTTP request, packaging your code and a separate <code>metadata.json</code> file. This was more complicated and verbose, and prone to formatting errors.</p>
<p>For example, here's how you would upload a Worker script previously with cURL:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/workers/scripts/my-hello-world-script \&#10;  &#45;X PUT \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;F &#x27;metadata={&#10;        &quot;main_module&quot;: &quot;my-hello-world-script.mjs&quot;,&#10;        &quot;bindings&quot;: [&#10;          {&#10;            &quot;type&quot;: &quot;plain_text&quot;,&#10;            &quot;name&quot;: &quot;MESSAGE&quot;,&#10;            &quot;text&quot;: &quot;Hello World!&quot;&#10;          }&#10;        ],&#10;        &quot;compatibility_date&quot;: &quot;$today&quot;&#10;      };type=application/json&#x27; \&#10;  &#45;F &#x27;my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module&#x27; &lt;&lt;EOF&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return new Response(env.MESSAGE, { status: 200 });&#10;  }&#10;};&#10;EOF&#10;</code></pre>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-after-sdk-interface">After: SDK interface</h4>
<p>With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.</p>
<p>This approach allows you to specify metadata like <code>main_module</code>, <code>bindings</code>, and <code>compatibility_date</code> as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.</p>
<p>Here's how you can now programmatically deploy a Worker via the <a href="https://github.com/cloudflare/cloudflare-typescript"><code>cloudflare-typescript</code> SDK</a></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17777.md")</div>
<p>View the complete example here: <a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts">https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts</a></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-terraform-provider-improvements">Terraform provider improvements</h4>
<p>We've also made several fixes and enhancements to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform provider</a>:</p>
<ul>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource in Terraform, which previously was producing a diff even when there were no changes. Now, your <code>terraform plan</code> outputs will be cleaner and more reliable.</li>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace"><code>cloudflare_workers_for_platforms_dispatch_namespace</code></a>, where the provider would attempt to recreate the namespace on a <code>terraform apply</code>. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.</li>
<li>The <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route"><code>cloudflare_workers_route</code></a> resource now allows for the <code>script</code> property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes <a href="/workers/configuration/routing/routes">docs</a>). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.</li>
<li>Using <code>primary_location_hint</code> in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database"><code>cloudflare_d1_database</code></a> resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.</li>
</ul>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-api-improvements">API improvements</h4>
<p>We've also properly documented the <a href="/api/resources/workers/subresources/scripts/subresources/script_and_version_settings">Workers Script And Version Settings</a> in our public OpenAPI spec and SDKs.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/storage/2/">Previous</a><span>Page 3 of 5</span><a class="pagination-next" rel="next" href="/changelog/product-group/storage/4/">Next</a></nav>
