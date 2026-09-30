---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/20/
  description: 2025-05-09 12:00:00 UTC
  full_title: Developer platform changelog - page 20 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 20 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-05-09 12:00:00 UTC"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/20/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 20"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-05-09 12:00:00 UTC"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/20/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/20/#page","headline":"Developer platform changelog - page 20 | Cloudflare Docs","description":"2025-05-09 12:00:00 UTC","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/20/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/20/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="publish-messages-to-queues-directly-via-http"><a href="/changelog/post/2025-05-09-publish-to-queues-via-http/">Publish messages to Queues directly via HTTP</a></h2>
<p><em>2025-05-09 12:00:00 UTC</em></p>
<p>You can now publish messages to <a href="/queues/">Cloudflare Queues</a> directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within <a href="/workers/">Cloudflare Workers</a>. You can already consume from queues via Workers or <a href="/queues/configuration/pull-consumers/">HTTP pull consumers</a>, and now publishing is just as flexible.</p>
<p>Publishing via HTTP requires a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API token</a> with <code>Queues Edit</code> permissions for authentication. Here's a simple example:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/queues/&lt;queue_id&gt;/messages&quot; \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-data &#x27;{ &quot;body&quot;: { &quot;greeting&quot;: &quot;hello&quot;, &quot;timestamp&quot;:  &quot;2025-07-24T12:00:00Z&quot;} }&#x27;&#10;</code></pre>
<p>You can also use our <a href="/fundamentals/api/reference/sdks/">SDKs</a> for TypeScript, Python, and Go.</p>
<p>To get started with HTTP publishing, check out our <a href="/queues/examples/publish-to-a-queue-via-http/">step-by-step example</a> and the full API documentation in our <a href="/api/resources/queues/subresources/messages/methods/push/">API reference</a>.</p>


<h2 id="improved-memory-efficiency-for-webassembly-workers"><a href="/changelog/post/2025-05-08-finalization-registry/">Improved memory efficiency for WebAssembly Workers</a></h2>
<p><em>2025-05-08</em></p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry">FinalizationRegistry</a> is now available in Workers. You can opt-in using the <a href="/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref"><code>enable_weak_ref</code></a> compatibility flag.</p>
<p>This can reduce memory leaks when using WebAssembly-based Workers, which includes <a href="/workers/languages/python/">Python Workers</a> and <a href="/workers/languages/rust/">Rust Workers</a>. The FinalizationRegistry works by enabling toolchains such as <a href="https://emscripten.org/">Emscripten</a> and <a href="https://wasm-bindgen.github.io/wasm-bindgen/">wasm-bindgen</a> to automatically free WebAssembly heap allocations. If you are using WASM and seeing Exceeded Memory errors and cannot determine a cause using <a href="/workers/observability/dev-tools/memory-usage/">memory profiling</a>, you may want to enable the FinalizationRegistry.</p>
<p>For more information refer to the <a href="/workers/configuration/compatibility-flags/#enable-finalizationregistry-and-weakref"><code>enable_weak_ref</code></a> compatibility flag documentation.</p>


<h2 id="terraform-v5-4-0-now-available"><a href="/changelog/post/2025-05-06-terraform-v5.4.0-provider/">Terraform v5.4.0 now available</a></h2>
<p><em>2025-05-06</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. Unlike the earlier Terraform providers, v5 is automatically generated based on the OpenAPI Schemas for our REST APIs. Since launch, we have seen an unexpectedly high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by customers. These issues currently impact about 15% of resources. We have been working diligently to address these issues across the company, and have released the v5.4.0 release which includes a number of bug fixes. Please keep an eye on this changelog for more information about upcoming releases.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-changes">Changes</h4>
<ul>
<li>
<p>Removes the <code>worker_platforms_script_secret</code> resource from the provider (see <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade#cloudflare_worker_secret">migration guide</a> for alternatives—applicable to both Workers and Workers for Platforms)</p>
</li>
<li>
<p>Removes duplicated fields in <code>cloudflare_cloud_connector_rules</code> resource</p>
</li>
<li>
<p>Fixes <code>cloudflare_workers_route</code> id issues <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5134">#5134</a> <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5501">#5501</a></p>
</li>
<li>
<p>Fixes issue around refreshing resources that have unsupported response types</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre tabindex="0"><code>  &lt;li&gt;`cloudflare_certificate_pack`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_registrar_domain`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_download`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_stream_webhook`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_user`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_kv`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_script`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixes <code>cloudflare_workers_kv</code> state refresh issues</p>
</li>
<li>
<p>Fixes issues around configurability of nested properties without computed values for the following resources</p>
<details>
<pre><code>&lt;summary&gt;Affected resources&lt;/summary&gt;
&lt;ul&gt;
</code></pre>
<pre tabindex="0"><code>  &lt;li&gt;`cloudflare_account`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_dns_settings`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_account_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_api_token`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_cloud_connector_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_custom_ssl`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_d1_database`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_dns_record`&lt;/li&gt;&#10;  &lt;li&gt;`email_security_trusted_domains`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_hyperdrive_config`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_keyless_certificate`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_list_item`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_load_balancer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_logpush_dataset_job`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_network_monitoring_configuration`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_lan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_transit_site_wan`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_magic_wan_static_route`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_notification_policy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_pages_project`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_queue_consumer`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_cors`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_event_notification`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lifecycle`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_lock`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_r2_bucket_sippy`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_ruleset`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippet_rules`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_snippets`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_spectrum_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_workers_deployment`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_application`&lt;/li&gt;&#10;  &lt;li&gt;`cloudflare_zero_trust_access_group`&lt;/li&gt;&#10;</code></pre>
<pre><code>&lt;/ul&gt;
</code></pre>
</details>
</li>
<li>
<p>Fixed defaults that made <code>cloudflare_workers_script</code> fail when using Assets</p>
</li>
<li>
<p>Fixed Workers Logpush setting in <code>cloudflare_workers_script</code> mistakenly being readonly</p>
</li>
<li>
<p>Fixed <code>cloudflare_pages_project</code> broken when using &quot;source&quot;</p>
</li>
</ul>
<p>The detailed <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.4.0">changelog</a> is available on GitHub.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-upgrading">Upgrading</h4>
<p>If you are evaluating a move from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition, although these do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues either by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>, or by opening a <a href="https://www.support.cloudflare.com/s/?language=en_US">support ticket</a>.</p>
<h4 id="2025-05-06-terraform-v5.4.0-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="r2-dashboard-experience-gets-new-updates"><a href="/changelog/post/2025-05-01-r2-dashboard-updates/">R2 Dashboard experience gets new updates</a></h2>
<p><em>2025-05-01</em></p>
<p>We're excited to announce several improvements to the <a href="/r2/">Cloudflare R2</a> dashboard experience that make managing your object storage easier and more intuitive:</p>
<p><img src="/assets/upstream/images/r2/r2-dashboard-updates.png" alt="Cloudflare R2 Dashboard" /></p>
<h4 id="2025-05-01-r2-dashboard-updates-all-new-settings-page">All-new settings page</h4>
<p>We've redesigned the bucket settings page, giving you a centralized location to manage all your bucket configurations in one place.</p>
<h4 id="2025-05-01-r2-dashboard-updates-improved-navigation-and-sharing">Improved navigation and sharing</h4>
<ul>
<li>Deeplink support for prefix directories: Navigate through your bucket hierarchy without losing your state. Your browser's back button now works as expected, and you can share direct links to specific prefix directories with teammates.</li>
<li>Objects as clickable links: Objects are now proper links that you can copy or <code>CMD + Click</code> to open in a new tab.</li>
</ul>
<h4 id="2025-05-01-r2-dashboard-updates-clearer-public-access-controls">Clearer public access controls</h4>
<ul>
<li>Renamed &quot;r2.dev domain&quot; to &quot;Public Development URL&quot; for better clarity when exposing bucket contents for non-production workloads.</li>
<li>Public Access status now clearly displays &quot;Enabled&quot; when your bucket is exposed to the internet (via Public Development URL or Custom Domains).</li>
</ul>
<p>We've also made numerous other usability improvements across the board to make your R2 experience smoother and more productive.</p>


<h2 id="cron-triggers-are-now-supported-in-python-workers"><a href="/changelog/post/2025-04-22-python-worker-cron-triggers/">Cron triggers are now supported in Python Workers</a></h2>
<p><em>2025-04-24</em></p>
<p>You can now create Python Workers which are executed via a cron trigger.</p>
<p>This is similar to how it's done in JavaScript Workers, simply define a scheduled event
listener in your Worker:</p>
<pre tabindex="0"><code class="language-python">from workers import handler&#10;&#10;@handler&#10;async def on_scheduled(event, env, ctx):&#10;  print(&quot;cron processed&quot;)&#10;</code></pre>
<p>Define a cron trigger configuration in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17772.md")</div>
<p>Then test your new handler by using Wrangler with the <code>--test-scheduled</code> flag and
making a request to <code>/cdn-cgi/local/scheduled?cron=*+*+*+*+*</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev --test-scheduled&#10;&#10;curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<p>Consult the <a href="/workers/configuration/cron-triggers/">Workers Cron Triggers page</a> for full details on cron triggers in Workers.</p>


<h2 id="metadata-filtering-and-multitenancy-support-in-autorag"><a href="/changelog/post/2025-04-23-autorag-metadata-filtering/">Metadata filtering and multitenancy support in AutoRAG</a></h2>
<p><em>2025-04-23</em></p>
<p>You can now filter <a href="/ai-search/">AutoRAG</a> search results by <code>folder</code> and <code>timestamp</code> using <a href="/ai-search/configuration/indexing/metadata/">metadata filtering</a> to narrow down the scope of your query.</p>
<p>This makes it easy to build <a href="/ai-search/how-to/per-tenant-search/">multitenant experiences</a> where each user can only access their own data. By organizing your content into per-tenant folders and applying a <code>folder</code> filter at query time, you ensure that each tenant retrieves only their own documents.</p>
<p><strong>Example folder structure:</strong></p>
<pre tabindex="0"><code class="language-bash">customer-a/logs/&#10;customer-a/contracts/&#10;customer-b/contracts/&#10;</code></pre>
<p><strong>Example query:</strong></p>
<pre tabindex="0"><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;When did I sign my agreement contract?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;folder&quot;,&#10;		value: &quot;customer-a/contracts/&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>You can use metadata filtering by creating a new AutoRAG or reindexing existing data. To reindex all content in an existing AutoRAG, update any chunking setting and select <strong>Sync index</strong>. Metadata filtering is available for all data indexed on or after <strong>April 21, 2025</strong>.</p>
<p>If you are new to AutoRAG, get started with the <a href="/ai-search/get-started/">Get started AutoRAG guide</a>.</p>


<h2 id="increased-limits-for-queues-pull-consumers"><a href="/changelog/post/2025-04-17-pull-consumer-limits/">Increased limits for Queues pull consumers</a></h2>
<p><em>2025-04-17 12:00:00 UTC</em></p>
<p><a href="/queues/configuration/pull-consumers/">Queues pull consumers</a> can now pull and acknowledge up to <strong>5,000 messages / second per queue</strong>. Previously, pull consumers were rate limited to 1,200 requests / 5 minutes, aggregated across all queues.</p>
<p>Pull consumers allow you to consume messages over HTTP from any environment—including outside of <a href="/workers">Cloudflare Workers</a>. They’re also useful when you need fine-grained control over how quickly messages are consumed.</p>
<p>To setup a new queue with a pull based consumer using <a href="/workers/wrangler/">Wrangler</a>, run:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler queues create my-queue&#10;npx wrangler queues consumer http add my-queue&#10;</code></pre>
<p>You can also configure a pull consumer using the <a href="/api/resources/queues/subresources/consumers/methods/create/">REST API</a> or the Queues dashboard.</p>
<p>Once configured, you can pull messages from the queue using any HTTP client. You'll need a <a href="/fundamentals/api/get-started/create-token/">Cloudflare API Token</a> with <code>queues_read</code> and <code>queues_write</code> permissions. For example:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull&quot; \&#10;&#45;-header &quot;Authorization: Bearer ${API_TOKEN}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{ &quot;visibility_timeout&quot;: 10000, &quot;batch_size&quot;: 2 }&#x27;&#10;</code></pre>
<p>To learn more about how to acknowledge messages, pull batches at once, and setup multiple consumers, refer to the <a href="/queues/configuration/pull-consumers">pull consumer documentation</a>.</p>
<p>As always, Queues doesn't charge for data egress. Pull operations continue to be billed at the <a href="/queues/platform/pricing">existing rate</a>, of $0.40 / million operations. The increased limits are available now, on all new and existing queues. If you're new to Queues, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>


<h2 id="read-multiple-keys-from-workers-kv-with-bulk-reads"><a href="/changelog/post/2025-04-10-kv-bulk-reads/">Read multiple keys from Workers KV with bulk reads</a></h2>
<p><em>2025-04-17</em></p>
<p>You can now retrieve up to 100 keys in a single bulk read request made to Workers KV using the binding.</p>
<p>This makes it easier to request multiple KV pairs within a single Worker invocation. Retrieving many key-value pairs using the bulk read operation is more performant than making individual requests since bulk read operations are not affected by <a href="/workers/platform/limits/#simultaneous-open-connections">Workers simultaneous connection limits</a>.</p>
<pre tabindex="0"><code class="language-js">// Read single key&#10;const key = &quot;key-a&quot;;&#10;const value = await env.NAMESPACE.get(key);&#10;&#10;// Read multiple keys&#10;const keys = [&quot;key-a&quot;, &quot;key-b&quot;, &quot;key-c&quot;, ...] // up to 100 keys&#10;const values : Map&lt;string, string?&gt; = await env.NAMESPACE.get(keys);&#10;&#10;// Print the value of &quot;key-a&quot; to the console.&#10;console.log(`The first key is ${values.get(&quot;key-a&quot;)}.`)&#10;</code></pre>
<p>Consult the <a href="/kv/api/read-key-value-pairs/">Workers KV Read key-value pairs API</a> for full details on Workers KV's new bulk reads support.</p>


<h2 id="fixed-and-documented-workers-routes-and-secrets-api"><a href="/changelog/post/2025-04-15-workers-api-fixes/">Fixed and documented Workers Routes and Secrets API</a></h2>
<p><em>2025-04-15</em></p>
<h4 id="2025-04-15-workers-api-fixes-workers-routes-api">Workers Routes API</h4>
<p>Previously, a request to the Workers <a href="/api/resources/workers/subresources/routes/methods/create/">Create Route API</a> always returned <code>null</code> for &quot;script&quot; and an empty string for &quot;pattern&quot; even if the request was successful.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/$CF_ACCOUNT_ID/workers/routes \&#10;&#45;X PUT \&#10;&#45;H &quot;Authorization: Bearer $CF_API_TOKEN&quot; \&#10;&#45;H &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{ &quot;pattern&quot;: &quot;example.com/*&quot;, &quot;script&quot;: &quot;hello-world-script&quot; }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;bf153a27ba2b464bb9f04dcf75de1ef9&quot;,&#10;		&quot;pattern&quot;: &quot;&quot;,&#10;		&quot;script&quot;: null,&#10;		&quot;request_limit_fail_open&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Now, it properly returns all values!</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;bf153a27ba2b464bb9f04dcf75de1ef9&quot;,&#10;		&quot;pattern&quot;: &quot;example.com/*&quot;,&#10;		&quot;script&quot;: &quot;hello-world-script&quot;,&#10;		&quot;request_limit_fail_open&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h4 id="2025-04-15-workers-api-fixes-workers-secrets-api">Workers Secrets API</h4>
<p>The <a href="/api/resources/workers/subresources/scripts/subresources/secrets/">Workers</a> and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/">Workers for Platforms</a> secrets APIs are now properly documented in the Cloudflare OpenAPI docs. Previously, these endpoints were not publicly documented, leaving users confused on how to directly manage their secrets via the API. Now, you can find the proper endpoints in our public documentation, as well as in our API Library SDKs such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (&gt;4.2.0) and <a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (&gt;4.1.0).</p>
<p>Note the <code>cloudflare_workers_secret</code> and <code>cloudflare_workers_for_platforms_script_secret</code> <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform resources</a> are being removed in a future release. This resource is not recommended for managing secrets. Users should instead use the:</p>
<ul>
<li><a href="/api/resources/secrets_store/">Secrets Store</a> with the &quot;Secrets Store Secret&quot; binding on Workers and Workers for Platforms Script Upload</li>
<li>&quot;Secret Text&quot; Binding on <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script Upload</a> and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/">Workers for Platforms Script Upload</a></li>
<li>Workers (and WFP) Secrets API</li>
</ul>


<h2 id="signed-urls-and-infrastructure-improvements-on-stream-live-webrtc-beta"><a href="/changelog/post/2025-04-14-webrtc-beta-signed-urls/">Signed URLs and Infrastructure Improvements on Stream Live WebRTC Beta</a></h2>
<p><em>2025-04-11</em></p>
<p>Cloudflare <a href="/stream/">Stream</a> has completed an infrastructure upgrade for our <a href="/stream/webrtc-beta/">Live WebRTC beta</a> support which brings increased scalability and improved playback performance to all customers. WebRTC allows broadcasting directly from a browser (or supported WHIP client) with ultra-low latency to tens of thousands of concurrent viewers across the globe.</p>
<p>Additionally, as part of this upgrade, the WebRTC beta now supports Signed URLs to protect playback, just like our standard live stream options (HLS/DASH).</p>
<p>For more information, learn about the <a href="/stream/webrtc-beta/">Stream Live WebRTC beta</a>.</p>


<h2 id="workers-ai-for-developer-week-faster-inference-new-models-async-batch-api-expanded-lora-support"><a href="/changelog/post/2025-04-11-new-models-faster-inference/">Workers AI for Developer Week - faster inference, new models, async batch API, expanded LoRA support</a></h2>
<p><em>2025-04-11</em></p>
<p>Happy Developer Week 2025! Workers AI is excited to announce a couple of new features and improvements available today. Check out our <a href="https://blog.cloudflare.com/workers-ai-improvements">blog</a> for all the announcement details.</p>
<h4 id="2025-04-11-new-models-faster-inference-faster-inference-new-models">Faster inference + New models</h4>
<p>We’re rolling out some in-place improvements to our models that can help speed up inference by 2-4x! Users of the models below will enjoy an automatic speed boost starting today:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a> gets a speed boost of 2-4x, leveraging techniques like speculative decoding, prefix caching, and an updated inference backend.</li>
<li><a href="/workers-ai/models/bge-small-en-v1.5/"><code>@cf/baai/bge-small-en-v1.5</code></a>, <a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code></a>, <a href="/workers-ai/models/bge-large-en-v1.5/"><code>@cf/baai/bge-large-en-v1.5</code></a> get an updated back end, which should improve inference times by 2x.
<ul>
<li>With the <code>bge</code> models, we’re also announcing a new parameter called <code>pooling</code> which can take <code>cls</code> or <code>mean</code> as options. We highly recommend using <code>pooling: cls</code> which will help generate more accurate embeddings. However, embeddings generated with cls pooling are not backwards compatible with mean pooling. For this to not be a breaking change, the default remains as mean pooling. Please specify <code>pooling: cls</code> to enjoy more accurate embeddings going forward.</li>
</ul>
</li>
</ul>
<p>We’re also excited to launch a few new models in our catalog to help round out your experience with Workers AI. We’ll be deprecating some older models in the future, so stay tuned for a deprecation announcement. Today’s new models include:</p>
<ul>
<li><a href="/workers-ai/models/mistral-small-3.1-24b-instruct/"><code>@cf/mistralai/mistral-small-3.1-24b-instruct</code></a>: a 24B parameter model achieving state-of-the-art capabilities comparable to larger models, with support for vision and tool calling.</li>
<li><a href="/workers-ai/models/gemma-3-12b-it/"><code>@cf/google/gemma-3-12b-it</code></a>: well-suited for a variety of text generation and image understanding tasks, including question answering, summarization and reasoning, with a 128K context window, and multilingual support in over 140 languages.</li>
<li><a href="/workers-ai/models/qwq-32b/"><code>@cf/qwen/qwq-32b</code></a>: a medium-sized reasoning model, which is capable of achieving competitive performance against state-of-the-art reasoning models, e.g., DeepSeek-R1, o1-mini.</li>
<li><a href="/workers-ai/models/qwen2.5-coder-32b-instruct/"><code>@cf/qwen/qwen2.5-coder-32b-instruct</code></a>: the current state-of-the-art open-source code LLM, with its coding abilities matching those of GPT-4o.</li>
</ul>
<h4 id="2025-04-11-new-models-faster-inference-batch-inference">Batch Inference</h4>
<p>Introducing a new batch inference feature that allows you to send us an array of requests, which we will fulfill as fast as possible and send them back as an array. This is really helpful for large workloads such as summarization, embeddings, etc. where you don’t have a human-in-the-loop. Using the batch API will guarantee that your requests are fulfilled eventually, rather than erroring out if we don’t have enough capacity at a given time.</p>
<p>Check out the <a href="/workers-ai/features/batch-api/">tutorial</a> to get started! Models that support batch inference today include:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a></li>
<li><a href="/workers-ai/models/bge-small-en-v1.5/"><code>@cf/baai/bge-small-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-base-en-v1.5/"><code>@cf/baai/bge-base-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-large-en-v1.5/"><code>@cf/baai/bge-large-en-v1.5</code></a></li>
<li><a href="/workers-ai/models/bge-m3/"><code>@cf/baai/bge-m3</code></a></li>
<li><a href="/workers-ai/models/m2m100-1.2b/"><code>@cf/meta/m2m100-1.2b</code></a></li>
</ul>
<h4 id="2025-04-11-new-models-faster-inference-expanded-lora-support">Expanded LoRA support</h4>
<p>We’ve upgraded our LoRA experience to include 8 newer models, and can support ranks of up to 32 with a 300MB safetensors file limit (previously limited to rank of 8 and 100MB safetensors) Check out our <a href="/workers-ai/features/fine-tunes/loras/">LoRAs page</a> to get started. Models that support LoRAs now include:</p>
<ul>
<li><a href="/workers-ai/models/llama-3.2-11b-vision-instruct/"><code>@cf/meta/llama-3.2-11b-vision-instruct</code></a></li>
<li><a href="/workers-ai/models/llama-3.3-70b-instruct-fp8-fast/"><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></a></li>
<li><a href="/workers-ai/models/llama-guard-3-8b/"><code>@cf/meta/llama-guard-3-8b</code></a></li>
<li><a href="/workers-ai/models/llama-3.1-8b-instruct-fast/"><code>@cf/meta/llama-3.1-8b-instruct-fast</code></a> (coming soon)</li>
<li><a href="/workers-ai/models/deepseek-r1-distill-qwen-32b/"><code>@cf/deepseek-ai/deepseek-r1-distill-qwen-32b</code></a> (coming soon)</li>
<li><a href="/workers-ai/models/qwen2.5-coder-32b-instruct/"><code>@cf/qwen/qwen2.5-coder-32b-instruct</code></a></li>
<li><a href="/workers-ai/models/qwq-32b/"><code>@cf/qwen/qwq-32b</code></a></li>
<li><a href="/workers-ai/models/mistral-small-3.1-24b-instruct/"><code>@cf/mistralai/mistral-small-3.1-24b-instruct</code></a></li>
<li><a href="/workers-ai/models/gemma-3-12b-it/"><code>@cf/google/gemma-3-12b-it</code></a></li>
</ul>


<h2 id="d1-read-replication-public-beta"><a href="/changelog/post/2025-04-10-d1-read-replication-beta/">D1 Read Replication Public Beta</a></h2>
<p><em>2025-04-10</em></p>
<p>D1 read replication is available in public beta to help lower average latency and increase overall throughput for read-heavy applications like e-commerce websites or content management tools.</p>
<p>Workers can leverage read-only database copies, called read replicas, by using D1 <a href="/d1/best-practices/read-replication">Sessions API</a>. A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. With Sessions API, D1 queries in a session are guaranteed to be <a href="/d1/best-practices/read-replication/#replica-lag-and-consistency-model">sequentially consistent</a> to avoid data consistency pitfalls. D1 <a href="/d1/reference/time-travel/#bookmarks">bookmarks</a> can be used from a previous session to ensure logical consistency between sessions.</p>
<pre tabindex="0"><code class="language-ts">// retrieve bookmark from previous session stored in HTTP header&#10;const bookmark = request.headers.get(&quot;x-d1-bookmark&quot;) ?? &quot;first-unconstrained&quot;;&#10;&#10;const session = env.DB.withSession(bookmark);&#10;const result = await session&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run();&#10;// store bookmark for a future session&#10;response.headers.set(&quot;x-d1-bookmark&quot;, session.getBookmark() ?? &quot;&quot;);&#10;</code></pre>
<p>Read replicas are automatically created by Cloudflare (currently one in each supported <a href="/d1/best-practices/read-replication/#read-replica-locations">D1 region</a>), are active/inactive based on query traffic, and are transparently routed to by Cloudflare at no additional cost.</p>
<p>To checkout D1 read replication, deploy the following Worker code using Sessions API, which will prompt you to create a D1 database and enable read replication on said database.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>To learn more about how read replication was implemented, go to our <a href="https://blog.cloudflare.com/d1-read-replication-beta">blog post</a>.</p>


<h2 id="cloudflare-pipelines-now-available-in-beta"><a href="/changelog/post/2025-04-10-launching-pipelines/">Cloudflare Pipelines now available in beta</a></h2>
<p><em>2025-04-10</em></p>
<p><a href="/pipelines">Cloudflare Pipelines</a> is now available in beta, to all users with a <a href="/workers/platform/pricing">Workers Paid</a> plan.</p>
<p>Pipelines let you ingest high volumes of real time data, without managing the underlying infrastructure. A single pipeline can ingest up to 100 MB of data per second, via HTTP or from a <a href="/workers">Worker</a>. Ingested data is automatically batched, written to output files, and delivered to an <a href="/r2">R2 bucket</a> in your account. You can use Pipelines to build a data lake of clickstream data, or to store events from a Worker.</p>
<p>Create your first pipeline with a single command:</p>
<pre tabindex="0"><code class="language-bash">$ npx wrangler@latest pipelines create my-clickstream-pipeline --r2-bucket my-bucket&#10;&#10;🌀 Authorizing R2 bucket &quot;my-bucket&quot;&#10;🌀 Creating pipeline named &quot;my-clickstream-pipeline&quot;&#10;✅ Successfully created pipeline my-clickstream-pipeline&#10;&#10;Id:    0e00c5ff09b34d018152af98d06f5a1xvc&#10;Name:  my-clickstream-pipeline&#10;Sources:&#10;  HTTP:&#10;    Endpoint:        https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&#10;    Authentication:  off&#10;    Format:          JSON&#10;  Worker:&#10;    Format:  JSON&#10;Destination:&#10;  Type:         R2&#10;  Bucket:       my-bucket&#10;  Format:       newline-delimited JSON&#10;  Compression:  GZIP&#10;Batch hints:&#10;  Max bytes:     100 MB&#10;  Max duration:  300 seconds&#10;  Max records:   100,000&#10;&#10;🎉 You can now send data to your pipeline!&#10;&#10;Send data to your pipeline&#x27;s HTTP endpoint:&#10;curl &quot;https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&quot; -d &#x27;[{ ...JSON_DATA... }]&#x27;&#10;&#10;To send data to your pipeline from a Worker, add the following configuration to your config file:&#10;{&#10;  &quot;pipelines&quot;: [&#10;    {&#10;      &quot;pipeline&quot;: &quot;my-clickstream-pipeline&quot;,&#10;      &quot;binding&quot;: &quot;PIPELINE&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Head over to our <a href="/pipelines/getting-started">getting started guide</a> for an in-depth tutorial to building with Pipelines.</p>


<h2 id="r2-data-catalog-is-a-managed-apache-iceberg-data-catalog-built-directly-into-r2-buckets"><a href="/changelog/post/2025-04-10-r2-data-catalog-beta/">R2 Data Catalog is a managed Apache Iceberg data catalog built directly into R2 buckets</a></h2>
<p><em>2025-04-10</em></p>
<p>Today, we are launching <a href="/r2-data-catalog/">R2 Data Catalog</a> in open beta, a managed Apache Iceberg catalog built directly into your <a href="/r2/">Cloudflare R2</a> bucket.</p>
<p>If you are not already familiar with it, <a href="https://iceberg.apache.org/">Apache Iceberg</a> is an open table format designed to handle large-scale analytics datasets stored in object storage, offering ACID transactions and schema evolution. R2 Data Catalog exposes a standard Iceberg REST catalog interface, so you can connect engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, and <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> to start querying your tables using the tools you already know.</p>
<p>To enable a data catalog on your R2 bucket, find <strong>R2 Data Catalog</strong> in your buckets settings in the dashboard, or run:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler r2 bucket catalog enable my-bucket&#10;</code></pre>
<p>And that's it. You'll get a catalog URI and warehouse you can plug into your favorite Iceberg engines.</p>
<p>Visit our <a href="/r2-data-catalog/get-started/">getting started guide</a> for step-by-step instructions on enabling R2 Data Catalog, creating tables, and running your first queries.</p>


<h2 id="hyperdrive-now-supports-custom-tls-ssl-certificates"><a href="/changelog/post/2025-04-09-hyperdrive-custom-certificate-support/">Hyperdrive now supports custom TLS/SSL certificates</a></h2>
<p><em>2025-04-09</em></p>
<p>Hyperdrive now supports more SSL/TLS security options for your database connections:</p>
<ul>
<li>Configure Hyperdrive to verify server certificates with <code>verify-ca</code> or <code>verify-full</code> SSL modes and protect against man-in-the-middle attacks</li>
<li>Configure Hyperdrive to provide client certificates to the database server to authenticate itself (mTLS) for stronger security beyond username and password</li>
</ul>
<p>Use the new <code>wrangler cert</code> commands to create certificate authority (CA) certificate bundles or client certificate pairs:</p>
<pre tabindex="0"><code class="language-bash">&#35; Create CA certificate bundle&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create client certificate pair&#10;npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name your-client-cert-name&#10;</code></pre>
<p>Then create a Hyperdrive configuration with the certificates and desired SSL mode:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;postgres://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-mtls-certificate-id &lt;CLIENT_CERT_ID&gt;&#10;  &#45;-sslmode verify-full&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">configuring SSL/TLS certificates for Hyperdrive</a> to enhance your database security posture.</p>


<h2 id="cloudflare-secrets-store-now-available-in-beta"><a href="/changelog/post/2025-04-09-secrets-store-beta/">Cloudflare Secrets Store now available in Beta</a></h2>
<p><em>2025-04-09</em></p>
<p>Cloudflare Secrets Store is available today in Beta. You can now store, manage, and deploy account level secrets from a secure, centralized platform to your Workers.</p>
<p><img src="/assets/upstream/images/ssl/secrets-store-landing-page.png" alt="Import repo or choose template" /></p>
<p>To spin up your Cloudflare Secrets Store, simply click the new Secrets Store tab <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">in the dashboard</a> or use this Wrangler command:</p>
<pre tabindex="0"><code class="language-sh">wrangler secrets-store store create &lt;name&gt; --remote&#10;</code></pre>
<p>The following are supported in the Secrets Store beta:</p>
<ul>
<li>Secrets Store UI &amp; API: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Workers UI: bind a new or existing account level secret to a Worker and deploy in code</li>
<li>Wrangler: create your store &amp; create, duplicate, update, scope, and delete a secret</li>
<li>Account Management UI &amp; API: assign Secrets Store permissions roles &amp; view audit logs for actions taken in Secrets Store core platform</li>
</ul>
<p>For instructions on how to get started, visit our <a href="/secrets-store/">developer documentation</a>.</p>


<h2 id="investigate-your-workers-with-the-query-builder-in-the-new-observability-dashboard"><a href="/changelog/post/2025-04-09-qb-workers-logs-ga/">Investigate your Workers with the Query Builder in the new Observability dashboard</a></h2>
<p><em>2025-04-09</em></p>
<p>The <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> offers a single place to investigate and explore your <a href="/workers/observability/logs/workers-logs">Workers Logs</a>.</p>
<p>The <strong>Overview</strong> tab shows logs from all your Workers in one place. The <strong>Invocations</strong> view groups logs together by invocation, which refers to the specific trigger that started the execution of the Worker (i.e. fetch). The <strong>Events</strong> view shows logs in the order they were produced, based on timestamp. Previously, you could only view logs for a single Worker.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-workers-observability-overview.png" alt="Workers Observability Overview Tab" /></p>
<p>The <strong>Investigate</strong> tab presents a Query Builder, which helps you write structured queries to investigate and visualize your logs. The Query Builder can help answer questions such as:</p>
<ul>
<li>Which paths are experiencing the most 5XX errors?</li>
<li>What is the wall time distribution by status code for my Worker?</li>
<li>What are the slowest requests, and where are they coming from?</li>
<li>Who are my top N users?</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-query-builder.png" alt="Workers Observability Overview Tab" /></p>
<p>The Query Builder can use any field that you store in your logs as a key to visualize, filter, and group by. Use the Query Builder to quickly access your data, build visualizations, save queries, and share them with your team.</p>
<h4 id="2025-04-09-qb-workers-logs-ga-workers-logs-is-now-generally-available">Workers Logs is now Generally Available</h4>
<p><a href="/workers/observability/logs/workers-logs">Workers Logs</a> is now Generally Available. With a <a href="/workers/observability/logs/workers-logs/#enable-workers-logs">small change</a> to your Wrangler configuration, Workers Logs ingests, indexes, and stores all logs emitted from your Workers for up to 7 days.</p>
<p>We've introduced a number of changes during our beta period, including:</p>
<ul>
<li>Dashboard enhancements with customizable fields as columns in the Logs view and support for invocation-based grouping</li>
<li>Performance improvements to ensure no adverse impact</li>
<li>Public <a href="https://developers.cloudflare.com/api/resources/workers/subresources/observability/">API endpoints</a> for broader consumption</li>
</ul>
<p>The API documents three endpoints: list the keys in the telemetry dataset, run a query, and list the unique values for a key. For more, visit our <a href="https://developers.cloudflare.com/api/resources/workers/subresources/observability/">REST API documentation</a>.</p>
<p>Visit the <a href="/workers/observability/query-builder">docs</a> to learn more about the capabilities and methods exposed by the Query Builder. Start using Workers Logs and the Query Builder today by enabling observability for your Workers:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17771.md")</div>


<h2 id="cpu-time-and-wall-time-now-published-for-workers-invocations"><a href="/changelog/post/2025-04-09-workers-timing/">CPU time and Wall time now published for Workers Invocations</a></h2>
<p><em>2025-04-09</em></p>
<p>You can now observe and investigate the CPU time and Wall time for every Workers Invocations.</p>
<ul>
<li>For <a href="/workers/observability/logs/workers-logs">Workers Logs</a>, CPU time and Wall time are surfaced in the <a href="/workers/observability/logs/workers-logs/#invocation-logs">Invocation Log</a>..</li>
<li>For <a href="/workers/observability/logs/tail-workers">Tail Workers</a>, CPU time and Wall time are surfaced at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">Workers Trace Events object</a>.</li>
<li>For <a href="/workers/observability/logs/logpush">Workers Logpush</a>, CPU and Wall time are surfaced at the top level of the <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events">Workers Trace Events object</a>. All new jobs will have these new fields included by default. Existing jobs need to be updated to include CPU time and Wall time.</li>
</ul>
<p>You can use a Workers Logs filter to search for logs where Wall time exceeds 100ms.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-wall-time-filter.png" alt="Workers Logs Wall Time Filter" /></p>
<p>You can also use the Workers Observability <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/investigate">Query Builder</a> to find the median CPU time and median Wall time for all of your Workers.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2025-04-09-query-builder.png" alt="Query Builder filter" /></p>


<h2 id="deploy-a-workers-application-in-seconds-with-one-click"><a href="/changelog/post/2025-04-08-deploy-to-cloudflare-button/">Deploy a Workers application in seconds with one-click</a></h2>
<p><em>2025-04-08 00:00:00 UTC</em></p>
<p>You can now add a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare</a> button to the README of your Git repository containing a Workers application — making it simple for other developers to quickly set up and deploy your project!</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/saas-admin-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>The Deploy to Cloudflare button:</p>
<ol>
<li><strong>Creates a new Git repository on your GitHub/ GitLab account</strong>: Cloudflare will automatically clone and create a new repository on your account, so you can continue developing.</li>
<li><strong>Automatically provisions resources the app needs</strong>: If your repository requires Cloudflare primitives like a <a href="/kv/">Workers KV namespace</a>, a <a href="/d1/">D1 database</a>, or an <a href="/r2/">R2 bucket</a>, Cloudflare will automatically provision them on your account and bind them to your Worker upon deployment.</li>
<li><strong>Configures Workers Builds (CI/CD)</strong>: Every new push to your production branch on your newly created repository will automatically build and deploy courtesy of <a href="/workers/ci-cd/builds/">Workers Builds</a>.</li>
<li><strong>Adds preview URLs to each pull request</strong>: If you'd like to test your changes before deploying, you can push changes to a <a href="/workers/ci-cd/builds/build-branches/#configure-non-production-branch-builds">non-production branch</a> and <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> will be generated and <a href="/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment">posted back to GitHub as a comment</a>.</li>
</ol>
<p><img src="/assets/upstream/images/workers/dtw-user-flow.png" alt="Import repo or choose template" /></p>
<p>To create a Deploy to Cloudflare button in your README, you can add the following snippet, including your Git repository URL:</p>
<pre tabindex="0"><code class="language-md">[<img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare">](https://deploy.workers.cloudflare.com/?url=&lt;YOUR_GIT_REPO_URL&gt;)&#10;</code></pre>
<p>Check out our <a href="/workers/platform/deploy-buttons/">documentation</a> for more information on how to set up a deploy button for your application and best practices to ensure a successful deployment for other developers.</p>


<h2 id="local-development-support-for-email-workers"><a href="/changelog/post/2025-04-08-local-development/">Local development support for Email Workers</a></h2>
<p><em>2025-04-08</em></p>
<p>Email Workers enables developers to programmatically take action on anything that hits their email inbox. If you're building with Email Workers, you can now test the behavior of an Email Worker script, receiving, replying and sending emails in your local environment using <code>wrangler dev</code>.</p>
<p>Below is an example that shows you how you can receive messages using the <code>email()</code> handler and parse them using <a href="https://www.npmjs.com/package/postal-mime">postal-mime</a>:</p>
<pre tabindex="0"><code class="language-ts">import * as PostalMime from &quot;postal-mime&quot;;&#10;&#10;export default {&#10;	async email(message, env, ctx) {&#10;		const parser = new PostalMime.default();&#10;		const rawEmail = new Response(message.raw);&#10;		const email = await parser.parse(await rawEmail.arrayBuffer());&#10;		console.log(email);&#10;	},&#10;};&#10;</code></pre>
<p>Now when you run <code>npx wrangler dev</code>, wrangler will expose a local <code>/cdn-cgi/local/email</code> endpoint that you can <code>POST</code> email messages to and trigger your Worker's <code>email()</code> handler:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &#x27;http://localhost:8787/cdn-cgi/local/email&#x27; \&#10;  &#45;-url-query &#x27;from=sender@example.com&#x27; \&#10;  &#45;-url-query &#x27;to=recipient@example.com&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data-raw &#x27;Received: from smtp.example.com (127.0.0.1)&#10;        by cloudflare-email.com (unknown) id 4fwwffRXOpyR&#10;        for &lt;recipient@example.com&gt;; Tue, 27 Aug 2024 15:50:20 +0000&#10;From: &quot;John&quot; &lt;sender@example.com&gt;&#10;Reply-To: sender@example.com&#10;To: recipient@example.com&#10;Subject: Testing Email Workers Local Dev&#10;Content-Type: text/html; charset=&quot;windows-1252&quot;&#10;X-Mailer: Curl&#10;Date: Tue, 27 Aug 2024 08:49:44 -0700&#10;Message-ID: &lt;6114391943504294873000@ZSH-GHOSTTY&gt;&#10;&#10;Hi there&#x27;&#10;</code></pre>
<p>This is what you get in the console:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;headers&quot;: [&#10;		{&#10;			&quot;key&quot;: &quot;received&quot;,&#10;			&quot;value&quot;: &quot;from smtp.example.com (127.0.0.1) by cloudflare-email.com (unknown) id 4fwwffRXOpyR for &lt;recipient@example.com&gt;; Tue, 27 Aug 2024 15:50:20 +0000&quot;&#10;		},&#10;		{ &quot;key&quot;: &quot;from&quot;, &quot;value&quot;: &quot;\&quot;John\&quot; &lt;sender@example.com&gt;&quot; },&#10;		{ &quot;key&quot;: &quot;reply-to&quot;, &quot;value&quot;: &quot;sender@example.com&quot; },&#10;		{ &quot;key&quot;: &quot;to&quot;, &quot;value&quot;: &quot;recipient@example.com&quot; },&#10;		{ &quot;key&quot;: &quot;subject&quot;, &quot;value&quot;: &quot;Testing Email Workers Local Dev&quot; },&#10;		{ &quot;key&quot;: &quot;content-type&quot;, &quot;value&quot;: &quot;text/html; charset=\&quot;windows-1252\&quot;&quot; },&#10;		{ &quot;key&quot;: &quot;x-mailer&quot;, &quot;value&quot;: &quot;Curl&quot; },&#10;		{ &quot;key&quot;: &quot;date&quot;, &quot;value&quot;: &quot;Tue, 27 Aug 2024 08:49:44 -0700&quot; },&#10;		{&#10;			&quot;key&quot;: &quot;message-id&quot;,&#10;			&quot;value&quot;: &quot;&lt;6114391943504294873000@ZSH-GHOSTTY&gt;&quot;&#10;		}&#10;	],&#10;	&quot;from&quot;: { &quot;address&quot;: &quot;sender@example.com&quot;, &quot;name&quot;: &quot;John&quot; },&#10;	&quot;to&quot;: [{ &quot;address&quot;: &quot;recipient@example.com&quot;, &quot;name&quot;: &quot;&quot; }],&#10;	&quot;replyTo&quot;: [{ &quot;address&quot;: &quot;sender@example.com&quot;, &quot;name&quot;: &quot;&quot; }],&#10;	&quot;subject&quot;: &quot;Testing Email Workers Local Dev&quot;,&#10;	&quot;messageId&quot;: &quot;&lt;6114391943504294873000@ZSH-GHOSTTY&gt;&quot;,&#10;	&quot;date&quot;: &quot;2024-08-27T15:49:44.000Z&quot;,&#10;	&quot;html&quot;: &quot;Hi there\n&quot;,&#10;	&quot;attachments&quot;: []&#10;}&#10;</code></pre>
<p>Local development is a critical part of the development flow, and also works for sending, replying and forwarding emails. See <a href="/email-service/local-development/routing/">our documentation</a> for more information.</p>


<h2 id="hyperdrive-free-plan-makes-fast-global-database-access-available-to-all"><a href="/changelog/post/2025-04-08-hyperdrive-free-plan/">Hyperdrive Free plan makes fast, global database access available to all</a></h2>
<p><em>2025-04-08</em></p>
<p>Hyperdrive is now available on the Free plan of Cloudflare Workers, enabling you to build Workers that connect to PostgreSQL or MySQL databases without compromise.</p>
<p>Low-latency access to SQL databases is critical to building full-stack Workers applications. We want you to be able to build on fast, global apps on Workers,
regardless of the tools you use. So we made Hyperdrive available for all, to make it easier to build Workers that connect to PostgreSQL and MySQL.</p>
<p>If you want to learn more about how Hyperdrive works, read the <a href="https://blog.cloudflare.com/how-hyperdrive-speeds-up-database-access">deep dive</a> on how Hyperdrive can make your database queries up to 4x faster.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-global-placement.png" alt="Hyperdrive provides edge connection setup and global connection pooling for optimal latencies." /></p>
<p>Visit the docs to <a href="/hyperdrive/get-started/">get started</a> with Hyperdrive for PostgreSQL or MySQL.</p>


<h2 id="hyperdrive-introduces-support-for-mysql-and-mysql-compatible-databases"><a href="/changelog/post/2025-04-08-hyperdrive-mysql-support/">Hyperdrive introduces support for MySQL and MySQL-compatible databases</a></h2>
<p><em>2025-04-08</em></p>
<p>Hyperdrive now supports connecting to MySQL and MySQL-compatible databases, including Amazon RDS and Aurora MySQL, Google Cloud SQL for MySQL, Azure Database for MySQL, PlanetScale and MariaDB.</p>
<p>Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.</p>
<p>Best of all, you can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, no code changes required.</p>
<pre tabindex="0"><code class="language-ts">import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export interface Env {&#10;	HYPERDRIVE: Hyperdrive;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;			disableEval: true, // Required for Workers compatibility&#10;		});&#10;&#10;		const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;		ctx.waitUntil(connection.end());&#10;&#10;		return new Response(JSON.stringify({ results, fields }), {&#10;			headers: {&#10;				&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				&quot;Access-Control-Allow-Origin&quot;: &quot;*&quot;,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a> and <a href="/hyperdrive/get-started/">get started building Workers that connect to MySQL with Hyperdrive</a>.</p>


<h2 id="full-stack-frameworks-are-now-generally-available-on-cloudflare-workers"><a href="/changelog/post/2025-04-08-fullstack-on-workers/">Full-stack frameworks are now Generally Available on Cloudflare Workers</a></h2>
<p><em>2025-04-08</em></p>
<img src="/assets/upstream/images/changelog/workers/fullstack-on-workers.png" alt="Full-stack on Cloudflare Workers" />
<p>The following full-stack frameworks now have Generally Available (&quot;GA&quot;) adapters for Cloudflare Workers, and are ready for you to use in production:</p>
<ul>
<li><a href="/workers/framework-guides/web-apps/react-router/">React Router v7 (Remix)</a></li>
<li><a href="/workers/framework-guides/web-apps/astro/">Astro</a></li>
<li><a href="/workers/framework-guides/web-apps/more-web-frameworks/hono/">Hono</a></li>
<li><a href="/workers/framework-guides/web-apps/vue/">Vue.js</a></li>
<li><a href="/workers/framework-guides/web-apps/more-web-frameworks/nuxt/">Nuxt</a></li>
<li><a href="/workers/framework-guides/web-apps/sveltekit/">Svelte (SvelteKit)</a></li>
<li>And <a href="/workers/framework-guides/">more</a>.</li>
</ul>
<p>The following frameworks are now in <strong>beta</strong>, with GA support coming very soon:</p>
<ul>
<li><a href="/workers/framework-guides/web-apps/nextjs/">Next.js</a>, supported through <a href="https://opennext.js.org/cloudflare">@opennextjs/cloudflare</a> is now <code>v1.0-beta</code>.</li>
<li><a href="/workers/framework-guides/web-apps/more-web-frameworks/angular/">Angular</a></li>
<li><a href="/workers/framework-guides/web-apps/more-web-frameworks/solid/">SolidJS (SolidStart)</a></li>
</ul>
<p>You can also build complete full-stack apps on Workers <strong>without a framework</strong>:</p>
<ul>
<li>You can <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">“just use Vite&quot;</a> and React together, and build a back-end API in the same Worker. Follow our <a href="/workers/vite-plugin/tutorial/">React SPA with an API tutorial</a> to learn how.</li>
</ul>
<p><strong>Get started building today with our <a href="/workers/framework-guides/">framework guides</a></strong>, or read our <a href="https://blog.cloudflare.com/full-stack-development-on-cloudflare-workers">Developer Week 2025 blog post</a> about all the updates to building full-stack applications on Workers.</p>


<h2 id="improved-support-for-node-js-crypto-and-tls-apis-in-workers"><a href="/changelog/post/2025-04-08-nodejs-crypto-and-tls/">Improved support for Node.js Crypto and TLS APIs in Workers</a></h2>
<p><em>2025-04-08</em></p>
<p>When using a Worker with the <a href="/workers/runtime-apis/nodejs/"><code>nodejs_compat</code></a> compatibility flag enabled,
the following Node.js APIs are now available:</p>
<ul>
<li><a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code></a></li>
<li><a href="/workers/runtime-apis/nodejs/tls/"><code>node:tls</code></a></li>
</ul>
<p>This make it easier to reuse existing Node.js code in Workers or use npm packages that depend on these APIs.</p>
<h4 id="2025-04-08-nodejs-crypto-and-tls-node-crypto">node:crypto</h4>
<p>The full <a href="https://nodejs.org/api/crypto.html"><code>node:crypto</code></a> API is now available in Workers.</p>
<p>You can use it to verify and sign data:</p>
<pre tabindex="0"><code class="language-js">import { sign, verify } from &quot;node:crypto&quot;;&#10;&#10;const signature = sign(&quot;sha256&quot;, &quot;-data to sign-&quot;, env.PRIVATE_KEY);&#10;const verified = verify(&quot;sha256&quot;, &quot;-data to sign-&quot;, env.PUBLIC_KEY, signature);&#10;</code></pre>
<p>Or, to encrypt and decrypt data:</p>
<pre tabindex="0"><code class="language-js">import { publicEncrypt, privateDecrypt } from &quot;node:crypto&quot;;&#10;&#10;const encrypted = publicEncrypt(env.PUBLIC_KEY, &quot;some data&quot;);&#10;const plaintext = privateDecrypt(env.PRIVATE_KEY, encrypted);&#10;</code></pre>
<p>See the <a href="/workers/runtime-apis/nodejs/crypto/"><code>node:crypto</code> documentation</a> for more information.</p>
<h4 id="2025-04-08-nodejs-crypto-and-tls-node-tls">node:tls</h4>
<p>The following APIs from <code>node:tls</code> are now available:</p>
<ul>
<li><a href="https://nodejs.org/api/tls.html#tlsconnectoptions-callback"><code>connect</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#class-tlstlssocket"><code>TLSSocket</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscheckserveridentityhostname-cert"><code>checkServerIdentity</code></a></li>
<li><a href="https://nodejs.org/api/tls.html#tlscreatesecurecontextoptions"><code>createSecureContext</code></a></li>
</ul>
<p>This enables secure connections over TLS (Transport Layer Security) to external services.</p>
<pre tabindex="0"><code class="language-js">import { connect } from &quot;node:tls&quot;;&#10;&#10;// ... in a request handler ...&#10;const connectionOptions = { key: env.KEY, cert: env.CERT };&#10;const socket = connect(url, connectionOptions, () =&gt; {&#10;	if (socket.authorized) {&#10;		console.log(&quot;Connection authorized&quot;);&#10;	}&#10;});&#10;&#10;socket.on(&quot;data&quot;, (data) =&gt; {&#10;	console.log(data);&#10;});&#10;&#10;socket.on(&quot;end&quot;, () =&gt; {&#10;	console.log(&quot;server ends connection&quot;);&#10;});&#10;</code></pre>
<p>See the <a href="/workers/runtime-apis/nodejs/tls/"><code>node:tls</code> documentation</a> for more information.</p>


<h2 id="the-cloudflare-vite-plugin-is-now-generally-available"><a href="/changelog/post/2025-04-08-vite-plugin/">The Cloudflare Vite plugin is now Generally Available</a></h2>
<p><em>2025-04-08</em></p>
<p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> has <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">reached v1.0</a> and is now Generally Available (&quot;GA&quot;).</p>
<p>When you use <code>@cloudflare/vite-plugin</code>, you can use Vite's local development server and build tooling, while ensuring that while developing, your code runs in <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>, the open-source Workers runtime.</p>
<p>This lets you get the best of both worlds for a full-stack app — you can use <a href="https://vite.dev/guide/features.html#hot-module-replacement">Hot Module Replacement</a> from Vite right alongside <a href="/durable-objects/">Durable Objects</a> and other runtime APIs and bindings that are unique to Cloudflare Workers.</p>
<p><code>@cloudflare/vite-plugin</code> is made possible by the new <a href="https://vite.dev/guide/api-environment">environment API</a> in Vite, and was built <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">in partnership with the Vite team</a>.</p>
<h4 id="2025-04-08-vite-plugin-framework-support">Framework support</h4>
<p>You can build any type of application with <code>@cloudflare/vite-plugin</code>, using any rendering mode, from single page applications (SPA) and static sites to server-side rendered (SSR) pages and API routes.</p>
<p><a href="/workers/framework-guides/web-apps/react-router/">React Router v7 (Remix)</a> is the first full-stack framework to provide full support for Cloudflare Vite plugin, allowing you to use all parts of Cloudflare's developer platform, without additional build steps.</p>
<p>You can also build complete full-stack apps on Workers <strong>without a framework</strong> — <a href="https://blog.cloudflare.com/introducing-the-cloudflare-vite-plugin">&quot;just use Vite&quot;</a> and React together, and build a back-end API in the same Worker. Follow our <a href="/workers/vite-plugin/tutorial/">React SPA with an API tutorial</a> to learn how.</p>
<h4 id="2025-04-08-vite-plugin-configuration">Configuration</h4>
<p>If you're already using <a href="https://vite.dev/">Vite</a> in your build and development toolchain, you can start using our plugin with minimal changes to your <code>vite.config.ts</code>:</p>
<pre tabindex="0"><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [cloudflare()],&#10;});&#10;</code></pre>
<p>Take a look at the <a href="/workers/vite-plugin/">documentation for our Cloudflare Vite plugin</a> for more information!</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/19/">Previous</a><span>Page 20 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/21/">Next</a></nav>
