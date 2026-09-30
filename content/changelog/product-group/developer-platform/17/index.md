---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/developer-platform/17/
  description: '2025-09-05'
  full_title: Developer platform changelog - page 17 | Cloudflare Docs
  head_html: <title>Developer platform changelog - page 17 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-09-05"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/developer-platform/17/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Developer platform changelog - page 17"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-09-05"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/developer-platform/17/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/developer-platform/17/#page","headline":"Developer platform changelog - page 17 | Cloudflare Docs","description":"2025-09-05","url":"https://developers.cloudflare.com/changelog/product-group/developer-platform/17/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/developer-platform/17/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="introducing-embeddinggemma-from-google-on-workers-ai"><a href="/changelog/post/2025-09-05-embeddinggemma/">Introducing EmbeddingGemma from Google on Workers AI</a></h2>
<p><em>2025-09-05</em></p>
<p>We're excited to be a launch partner alongside <a href="https://developers.googleblog.com/en/introducing-embeddinggemma/">Google</a> to bring their newest embedding model, <strong>EmbeddingGemma</strong>, to Workers AI that delivers best-in-class performance for its size, enabling RAG and semantic search use cases.</p>
<p><a href="/workers-ai/models/embeddinggemma-300m/"><code>@cf/google/embeddinggemma-300m</code></a> is a 300M parameter embedding model from Google, built from Gemma 3 and the same research used to create Gemini models. This multilingual model supports 100+ languages, making it ideal for RAG systems, semantic search, content classification, and clustering tasks.</p>
<p><strong>Using EmbeddingGemma in AI Search:</strong>
Now you can leverage EmbeddingGemma directly through AI Search for your RAG pipelines. EmbeddingGemma's multilingual capabilities make it perfect for global applications that need to understand and retrieve content across different languages with exceptional accuracy.</p>
<p>To use EmbeddingGemma for your AI Search projects:</p>
<ol>
<li>Go to <strong>Create</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/ai/ai-search">AI Search dashboard</a></li>
<li>Follow the setup flow for your new RAG instance</li>
<li>In the <strong>Generate Index</strong> step, open up <strong>More embedding models</strong> and select <code>@cf/google/embeddinggemma-300m</code> as your embedding model</li>
<li>Complete the setup to create an AI Search</li>
</ol>
<p>Try it out and let us know what you think!</p>


<h2 id="increased-static-asset-limits-for-workers"><a href="/changelog/post/2025-09-02-increased-static-asset-limits/">Increased static asset limits for Workers</a></h2>
<p><em>2025-09-04</em></p>
<p>You can now upload up to <strong>100,000 static assets</strong> per Worker version</p>
<ul>
<li>Paid and Workers for Platforms users can now upload up to <strong>100,000 static assets</strong> per Worker version, a 5x increase from the previous limit of 20,000.</li>
<li>Customers on the free plan still have the same limit as before — 20,000 static assets per version of your Worker</li>
<li>The individual file size limit of 25 MiB remains unchanged for all customers.</li>
</ul>
<p>This increase allows you to build larger applications with more static assets without hitting limits.</p>
<h4 id="2025-09-02-increased-static-asset-limits-wrangler">Wrangler</h4>
<p>To take advantage of the increased limits, you must use <strong>Wrangler version 4.34.0 or higher</strong>.
Earlier versions of Wrangler will continue to enforce the previous 20,000 file limit.</p>
<h4 id="2025-09-02-increased-static-asset-limits-learn-more">Learn more</h4>
<p>For more information about Workers static assets, see the <a href="/workers/static-assets/">Static Assets documentation</a> and <a href="/workers/platform/limits/#static-assets">Platform Limits</a>.</p>


<h2 id="a-new-simpler-rest-api-for-cloudflare-workers-beta"><a href="/changelog/post/2025-09-03-new-workers-api/">A new, simpler REST API for Cloudflare Workers (Beta)</a></h2>
<p><em>2025-09-04</em></p>
<p>You can now manage <a href="/api/resources/workers/subresources/beta/subresources/workers/methods/create/"><strong>Workers</strong></a>, <a href="/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)"><strong>Versions</strong></a>, and <a href="/api/resources/workers/subresources/scripts/subresources/content/methods/update/"><strong>Deployments</strong></a> as separate resources with a new, resource-oriented API (Beta).</p>
<p>This new API is supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a> and the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare Typescript SDK</a>, allowing platform teams to manage a Worker's infrastructure in Terraform, while development teams handle code deployments from a separate repository or workflow. We also designed this API with AI agents in mind, as a clear, predictable structure is essential for them to reliably build, test, and deploy applications.</p>
<h4 id="2025-09-03-new-workers-api-try-it-out">Try it out</h4>
- [**New beta API endpoints**](/api/resources/workers/subresources/beta/)
- [**Cloudflare TypeScript SDK v5.0.0**](https://github.com/cloudflare/cloudflare-typescript)
- [**Cloudflare Go SDK v6.0.0**](https://github.com/cloudflare/cloudflare-go)
- [**Terraform provider v5.9.0**](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs): [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) , [`cloudflare_worker_version`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version), and [`cloudflare_workers_deployments`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_deployment) resources.
- See full examples in our [Infrastructure as Code (IaC) guide](/workers/platform/infrastructure-as-code)
<h4 id="2025-09-03-new-workers-api-before-eight-endpoints-with-mixed-responsibilities">Before: Eight+ endpoints with mixed responsibilities</h4>
<img src="/assets/upstream/images/workers/platform/api-before.png" alt="Before">
<p>The existing API was originally designed for simple, one-shot script uploads:</p>
<pre tabindex="0"><code class="language-sh">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/scripts/$SCRIPT_NAME&quot; \&#10;    &#45;H &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;    &#45;H &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;    &#45;H &quot;Content-Type: multipart/form-data&quot; \&#10;    &#45;F &#x27;metadata={&#10;      &quot;main_module&quot;: &quot;worker.js&quot;,&#10;      &quot;compatibility_date&quot;: &quot;$today$&quot;&#10;    }&#x27; \&#10;    &#45;F &quot;worker.js=@worker.js;type=application/javascript+module&quot;&#10;</code></pre>
<p>This API worked for creating a basic Worker, uploading all of its code, and deploying it immediately — but came with challenges:</p>
<ul>
<li>
<p><strong>A Worker couldn't exist without code</strong>: To create a Worker, you had to upload its code in the same API request. This meant platform teams couldn't provision Workers with the proper settings, and then hand them off to development teams to deploy the actual code.</p>
</li>
<li>
<p><strong>Several endpoints implicitly created deployments</strong>: Simple updates like adding a secret or changing a script's content would implicitly create a new version and immediately deploy it.</p>
</li>
<li>
<p><strong>Updating a setting was confusing</strong>: Configuration was scattered across eight endpoints with overlapping responsibilities.  This ambiguity made it difficult for human developers (and even more so for AI agents) to reliably update a Worker via API.</p>
</li>
<li>
<p><strong>Scripts used names as primary identifiers</strong>: This meant simple renames could turn into a risky migration, requiring you to create a brand new Worker and update every reference. If you were using Terraform, this could inadvertently destroy your Worker altogether.</p>
</li>
</ul>
<h4 id="2025-09-03-new-workers-api-after-three-resources-with-clear-boundaries">After: Three resources with clear boundaries</h4>
<img src="/assets/upstream/images/workers/platform/api-after.png" alt="After">
The new API introduces cleaner resource management with three core resources: [**Worker**](/api/resources/workers/subresources/beta/subresources/workers/methods/create/), [**Versions**](/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)), and [**Deployment**](/api/resources/workers/subresources/scripts/subresources/content/methods/update/).
<p>All endpoints now use simple JSON payloads, with script content embedded as <code>base64</code>-encoded strings -- a more consistent and reliable approach than the previous <code>multipart/form-data</code> format.</p>
<ul>
<li>
<p><strong>Worker</strong>: The parent resource representing your application. It has a stable UUID and holds persistent settings like <code>name</code>, <code>tags</code>, and <code>logpush</code>. You can now create a Worker to establish its identity and settings <strong>before</strong> any code is uploaded.</p>
</li>
<li>
<p><strong>Version</strong>: An immutable snapshot of your code and its specific configuration, like bindings and <code>compatibility_date</code>. Creating a new version is a safe action that doesn't affect live traffic.</p>
</li>
<li>
<p><strong>Deployment</strong>: An explicit action that directs traffic to a specific version.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17786.md")</aside>
<h4 id="2025-09-03-new-workers-api-why-this-matters">Why this matters</h4>
<h4 id="2025-09-03-new-workers-api-you-can-now-create-workers-before-uploading-code">You can now create Workers before uploading code</h4>
<p>Workers are now standalone resources that can be created and configured without any code. Platform teams can provision Workers with the right settings, then hand them off to development teams for implementation.</p>
<h4 id="2025-09-03-new-workers-api-example-typescript-sdk">Example: Typescript SDK</h4>
<pre tabindex="0"><code class="language-ts">// Step 1: Platform team creates the Worker resource (no code needed)&#10;const worker = await client.workers.beta.workers.create({&#10;  name: &quot;payment-service&quot;,&#10;  account_id: &quot;...&quot;,&#10;  observability: {&#10;    enabled: true,&#10;  },&#10;});&#10;<p>// Step 2: Development team adds code and creates a version later&#10;const version = await client.workers.beta.workers.versions.create(worker.id, {&#10;account_id: &quot;...&quot;,&#10;main_module: &quot;worker.js&quot;,&#10;compatibility_date: &quot;$today&quot;,&#10;bindings: [ /<em>...</em>/ ],&#10;modules: [&#10;{&#10;name: &quot;worker.js&quot;,&#10;content_type: &quot;application/javascript+module&quot;,&#10;content_base64: Buffer.from(scriptContent).toString(&quot;base64&quot;),&#10;},&#10;],&#10;});</p>&#10;<p>// Step 3: Deploy explicitly when ready&#10;const deployment = await client.workers.scripts.deployments.create(worker.name, {&#10;account_id: &quot;...&quot;,&#10;strategy: &quot;percentage&quot;,&#10;versions: [&#10;{&#10;percentage: 100,&#10;version_id: version.id,&#10;},&#10;],&#10;});&#10;</code></pre></p>
<h4 id="2025-09-03-new-workers-api-example-terraform">Example: Terraform</h4>
If you use Terraform, you can now declare the Worker in your Terraform configuration and manage configuration outside of Terraform in your Worker's [`wrangler.jsonc` file](/workers/wrangler/configuration/) and deploy code changes using [Wrangler](/workers/wrangler/).
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_worker&quot; &quot;my_worker&quot; {&#10;  account_id = &quot;...&quot;&#10;  name = &quot;my-important-service&quot;&#10;}&#10;&#35; Manage Versions and Deployments here or outside of Terraform&#10;&#35; resource &quot;cloudflare_worker_version&quot; &quot;my_worker_version&quot; {}&#10;&#35; resource &quot;cloudflare_workers_deployment&quot; &quot;my_worker_deployment&quot; {}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-deployments-are-always-explicit-never-implicit">Deployments are always explicit, never implicit</h4>
<p>Creating a version and deploying it are now always explicit, separate actions - never implicit side effects. To update version-specific settings (like bindings), you create a new version with those changes. The existing deployed version remains unchanged until you explicitly deploy the new one.</p>
<pre tabindex="0"><code class="language-sh">&#35; Step 1: Create a new version with updated settings (doesn&#x27;t affect live traffic)&#10;POST /workers/workers/{id}/versions&#10;{&#10;  &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;  &quot;bindings&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;MY_NEW_ENV_VAR&quot;,&#10;      &quot;text&quot;: &quot;new_value&quot;,&#10;      &quot;type&quot;: &quot;plain_text&quot;&#10;    }&#10;  ],&#10;  &quot;modules&quot;: [...]&#10;}&#10;&#10;&#35; Step 2: Explicitly deploy when ready (now affects live traffic)&#10;POST /workers/scripts/{script_name}/deployments&#10;{&#10;  &quot;strategy&quot;: &quot;percentage&quot;,&#10;  &quot;versions&quot;: [&#10;    {&#10;      &quot;percentage&quot;: 100,&#10;      &quot;version_id&quot;: &quot;new_version_id&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-settings-are-clearly-organized-by-scope">Settings are clearly organized by scope</h4>
Configuration is now logically divided: [**Worker settings**](/api/resources/workers/subresources/beta/subresources/workers/) (like `name` and `tags`) persist across all versions, while [**Version settings**](/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/) (like `bindings` and `compatibility_date`) are specific to each code snapshot.
<pre tabindex="0"><code class="language-sh">&#35; Worker settings (the parent resource)&#10;PUT /workers/workers/{id}&#10;{&#10;  &quot;name&quot;: &quot;payment-service&quot;,&#10;  &quot;tags&quot;: [&quot;production&quot;],&#10;  &quot;logpush&quot;: true,&#10;}&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Version settings (the &quot;code&quot;)&#10;POST /workers/workers/{id}/versions&#10;{&#10;  &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;  &quot;bindings&quot;: [...],&#10;  &quot;modules&quot;: [...]&#10;}&#10;</code></pre>
<h4 id="2025-09-03-new-workers-api-workers-api-endpoints-now-support-uuids-in-addition-to-names"><code>/workers</code> API endpoints now support UUIDs (in addition to names)</h4>
<p>The <code>/workers/workers/</code> path now supports addressing a Worker by both its immutable UUID and its mutable name.</p>
<pre tabindex="0"><code class="language-sh">&#35; Both work for the same Worker&#10;GET /workers/workers/29494978e03748669e8effb243cf2515  # UUID (stable for automation)&#10;GET /workers/workers/payment-service                  # Name (convenient for humans)&#10;</code></pre>
<p>This dual approach means:</p>
<ul>
<li>Developers can use readable names for debugging.</li>
<li>Automation can rely on stable UUIDs to prevent errors when Workers are renamed.</li>
<li>Terraform can rename Workers without destroying and recreating them.</li>
</ul>
<h4 id="2025-09-03-new-workers-api-learn-more">Learn more</h4>
- [Infrastructure as Code (IaC) guide](/workers/platform/infrastructure-as-code)
- [API documentation](/api/resources/workers/subresources/beta/)
- [Versions and Deployments overview](/workers/versions-and-deployments/)
<h4 id="2025-09-03-new-workers-api-technical-notes">Technical notes</h4>
<ul>
<li>The pre-existing Workers REST API remains fully supported. Once the new API exits beta, we'll provide a migration timeline with ample notice and comprehensive migration guides.</li>
<li>Existing Terraform resources and SDK methods will continue to be fully supported through the current major version.</li>
<li>While the Deployments API currently remains on the <code>/scripts/</code> endpoint, we plan to introduce a new Deployments endpoint under <code>/workers/</code> to match the new API structure.</li>
</ul>


<h2 id="cloudflare-tunnel-and-networks-api-will-no-longer-return-deleted-resources-by-default-starting-december-1-2025"><a href="/changelog/post/2025-09-02-tunnel-networks-list-endpoints-new-default/">Cloudflare Tunnel and Networks API will no longer return deleted resources by default starting December 1, 2025</a></h2>
<p><em>2025-09-02</em></p>
<p>Starting <strong>December 1, 2025</strong>, list endpoints for the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> will no longer return deleted tunnels, routes, subnets and virtual networks by default. This change makes the API behavior more intuitive by only returning active resources unless otherwise specified.</p>
<p>No action is required if you already explicitly set <code>is_deleted=false</code> or if you only need to list active resources.</p>
<p>This change affects the following API endpoints:</p>
<ul>
<li>List all tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/methods/list/"><code>GET /accounts/{account_id}/tunnels</code></a></li>
<li>List <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnels</a>: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/cloudflared/methods/list/"><code>GET /accounts/{account_id}/cfd_tunnel</code></a></li>
<li>List <a href="/mesh/">WARP Connector</a> tunnels: <a href="/api/resources/zero_trust/subresources/tunnels/subresources/warp_connector/methods/list/"><code>GET /accounts/{account_id}/warp_connector</code></a></li>
<li>List tunnel routes: <a href="/api/resources/zero_trust/subresources/networks/subresources/routes/methods/list/"><code>GET /accounts/{account_id}/teamnet/routes</code></a></li>
<li>List subnets: <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/methods/list/"><code>GET /accounts/{account_id}/zerotrust/subnets</code></a></li>
<li>List virtual networks: <a href="/api/resources/zero_trust/subresources/networks/subresources/virtual_networks/methods/list/"><code>GET /accounts/{account_id}/teamnet/virtual_networks</code></a></li>
</ul>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-what-is-changing">What is changing?</h4>
<p>The default behavior of the <code>is_deleted</code> query parameter will be updated.</p>
<table>
<thead>
<tr>
<th align="left">Scenario</th>
<th align="left">Previous behavior (before December 1, 2025)</th>
<th align="left">New behavior (from December 1, 2025)</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>is_deleted</code> parameter is omitted</td>
<td align="left">Returns <strong>active &amp; deleted</strong> tunnels, routes, subnets and virtual networks</td>
<td align="left">Returns <strong>only active</strong> tunnels, routes, subnets and virtual networks</td>
</tr>
</tbody>
</table>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-action-required">Action required</h4>
<p>If you need to retrieve deleted (or all) resources, please update your API calls to explicitly include the <code>is_deleted</code> parameter before <strong>December 1, 2025</strong>.</p>
<p>To get a list of only deleted resources, you must now explicitly add the <code>is_deleted=true</code> query parameter to your request:</p>
<pre tabindex="0"><code class="language-bash">&#35; Example: Get ONLY deleted Tunnels&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/tunnels?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;&#10;&#35; Example: Get ONLY deleted Virtual Networks&#10;curl &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/teamnet/virtual_networks?is_deleted=true&quot; \&#10;     &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>Following this change, retrieving a complete list of both active and deleted resources will require two separate API calls: one to get active items (by omitting the parameter or using <code>is_deleted=false</code>) and one to get deleted items (<code>is_deleted=true</code>).</p>
<h4 id="2025-09-02-tunnel-networks-list-endpoints-new-default-why-we-re-making-this-change">Why we’re making this change</h4>
This update is based on user feedback and aims to:
* **Create a more intuitive default:** Aligning with common API design principles where list operations return only active resources by default.
* **Reduce unexpected results:** Prevents users from accidentally operating on deleted resources that were returned unexpectedly.
* **Improve performance:** For most users, the default query result will now be smaller and more relevant.
<p>To learn more, please visit the <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> and <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> documentation.</p>


<h2 id="terraform-v5-9-now-available"><a href="/changelog/post/2025-08-29-terrform-v5.9-provider/">Terraform v5.9 now available</a></h2>
<p><em>2025-08-29</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare community related to the v5 release. We have committed to releasing improvements on a 2 week cadence to ensure its stability and reliability, including the v5.9 release. We have also pivoted from an issue-to-issue approach to a resource-per-resource approach - we will be focusing on specific resources for every release, stabilizing the release, and closing all associated bugs with that resource before moving onto resolving migration issues.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<p>This release includes a new resource, <code>cloudflare_snippet</code>, which replaces <code>cloudflare_snippets</code>. <code>cloudflare_snippet</code> is now considered deprecated but can still be used. Please utilize <code>cloudflare_snippet</code> as soon as possible.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_zone_setting`
  - `cloudflare_worker_script`
  - `cloudflare_worker_route`
  - `tiered_cache`
- **NEW** resource `cloudflare_snippet` which should be used in place of `cloudflare_snippets`. `cloudflare_snippets` is now deprecated. This enables the management of Cloudflare's snippet functionality through Terraform.
- DNS Record Improvements: Enhanced handling of DNS record drift detection
- Load Balancer Fixes: Resolved `created_on` field inconsistencies and improved pool configuration handling
- Bot Management: Enhanced auto-update model state consistency and fight mode configurations
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the
<a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.9.0">changelog</a> in GitHub.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-issues-closed">Issues Closed</h4>
- [#5921: In cloudflare_ruleset removing an existing rule causes recreation of later rules](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5921)
- [#5904: cloudflare_zero_trust_access_application is not idempotent](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5904)
- [#5898: (cloudflare_workers_script) Durable Object migrations not applied](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5898)
- [#5892: cloudflare_workers_script secret_text environment variable gets replaced on every deploy](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5892)
- [#5891: cloudflare_zone suddenly started showing drift](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5891)
- [#5882: cloudflare_zero_trust_list always marked for change due to read only attributes](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5882)
- [#5879: cloudflare_zero_trust_gateway_certificate unable to manage resource (cant mark as active/inactive)](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5879)
- [#5858: cloudflare_dns_records is always updated in-place](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5858)
- [#5839: Recurring change on cloudflare_zero_trust_gateway_policy after upgrade to V5 provider & also setting expiration fails](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5839)
- [#5811: Reusable policies are imported as inline type for cloudflare_zero_trust_access_application](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5811)
- [#5795: cloudflare_zone_setting inconsistent value of "editable" upon apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5795)
- [#5789: Pagination issue fetching all policies in "cloudflare_zero_trust_access_policies" data source](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5789)
- [#5770: cloudflare_zero_trust_access_application type warp diff on every apply](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5770)
- [#5765: V5 / cloudflare_zone_dnssec fails with HTTP/400 "Malformed request body"](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5765)
- [#5755: Unable to manage Cloudflare managed WAF rules via Terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5755)
- [#5738: v4 to v5 upgrade failing Error: no schema available AND Unable to Read Previously Saved State for UpgradeResourceState](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5738)
- [#5727: cloudflare_ruleset http_request_cache_settings bypass mismatch between dashboard and terraform](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5727)
- [#5700: cloudflare_account_member invalid type 'string' for field 'roles'](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5700)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new issue if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This help will you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating from v4 to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test
your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-29-terrform-v5.9-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub Repository</a></li>
</ul>


<h2 id="deepgram-and-leonardo-partner-models-now-available-on-workers-ai"><a href="/changelog/post/2025-08-27-partner-models/">Deepgram and Leonardo partner models now available on Workers AI</a></h2>
<p><em>2025-08-27</em></p>
<p>New state-of-the-art models have landed on Workers AI! This time, we're introducing new <strong>partner models</strong> trained by our friends at <a href="https://deepgram.com">Deepgram</a> and <a href="https://leonardo.ai">Leonardo</a>, hosted on Workers AI infrastructure.</p>
<p>As well, we're introuding a new turn detection model that enables you to detect when someone is done speaking — useful for building voice agents!</p>
<p>Read the <a href="https://blog.cloudflare.com/workers-ai-partner-models">blog</a> for more details and check out some of the new models on our platform:</p>
<ul>
<li><a href="/workers-ai/models/aura-1"><code>@cf/deepgram/aura-1</code></a> is a text-to-speech model that allows you to input text and have it come to life in a customizable voice</li>
<li><a href="/workers-ai/models/nova-3"><code>@cf/deepgram/nova-3</code></a> is speech-to-text model that transcribes multilingual audio at a blazingly fast speed</li>
<li><a href="/workers-ai/models/smart-turn-v2"><code>@cf/pipecat-ai/smart-turn-v2</code></a> helps you detect when someone is done speaking</li>
<li><a href="/workers-ai/models/lucid-origin"><code>@cf/leonardo/lucid-origin</code></a> is a text-to-image model that generates images with sharp graphic design, stunning full-HD renders, or highly specific creative direction</li>
<li><a href="/workers-ai/models/phoenix-1.0"><code>@cf/leonardo/phoenix-1.0</code></a> is a text-to-image model with exceptional prompt adherence and coherent text</li>
</ul>
<p>You can filter out new partner models with the <code>Partner</code> capability on our <a href="/workers-ai/models">Models</a> page.</p>
<p>As well, we're introducing WebSocket support for some of our audio models, which you can filter though the <code>Realtime</code> capability on our <a href="/workers-ai/models">Models</a> page. WebSockets allows you to create a bi-directional connection to our inference server with low latency — perfect for those that are building voice agents.</p>
<p>An example python snippet on how to use WebSockets with our new Aura model:</p>
<pre tabindex="0"><code>import json&#10;import os&#10;import asyncio&#10;import websockets&#10;&#10;uri = f&quot;wss://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/deepgram/aura-1&quot;&#10;&#10;input = [&#10;    &quot;Line one, out of three lines that will be provided to the aura model.&quot;,&#10;    &quot;Line two, out of three lines that will be provided to the aura model.&quot;,&#10;    &quot;Line three, out of three lines that will be provided to the aura model. This is a last line.&quot;,&#10;]&#10;&#10;&#10;async def text_to_speech():&#10;    async with websockets.connect(uri, additional_headers={&quot;Authorization&quot;: os.getenv(&quot;CF_TOKEN&quot;)}) as websocket:&#10;        print(&quot;connection established&quot;)&#10;        for line in input:&#10;            print(f&quot;sending `{line}`&quot;)&#10;            await websocket.send(json.dumps({&quot;type&quot;: &quot;Speak&quot;, &quot;text&quot;: line}))&#10;&#10;            print(&quot;line was sent, flushing&quot;)&#10;            await websocket.send(json.dumps({&quot;type&quot;: &quot;Flush&quot;}))&#10;            print(&quot;flushed, recving&quot;)&#10;            resp = await websocket.recv()&#10;            print(f&quot;response received {resp}&quot;)&#10;&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    asyncio.run(text_to_speech())&#10;</code></pre>


<h2 id="list-all-vectors-in-a-vectorize-index-with-the-new-list-vectors-operation"><a href="/changelog/post/2025-08-26-vectorize-list-vectors/">List all vectors in a Vectorize index with the new list-vectors operation</a></h2>
<p><em>2025-08-26</em></p>
<p>You can now list all vector identifiers in a Vectorize index using the new <code>list-vectors</code> operation. This enables bulk operations, auditing, and data migration workflows through paginated requests that maintain snapshot consistency.</p>
<p>The operation is available via Wrangler CLI and REST API. Refer to the <a href="/vectorize/best-practices/list-vectors/">list-vectors best practices guide</a> for detailed usage guidance.</p>


<h2 id="manage-and-deploy-your-ai-provider-keys-through-bring-your-own-key-byok-with-ai-gateway-now-powered-by-cloudflare-secrets-store"><a href="/changelog/post/2025-08-25-secrets-store-ai-gateway/">Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</a></h2>
<p><em>2025-08-25T11:00:00+00:00</em></p>
<p>Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through <a href="https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Key</a>. Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.</p>
<p>You can now create a secret directly from your AI Gateway <a href="http://dash.cloudflare.com/?to=/:account/ai-gateway">in the dashboard</a> by navigating into your gateway -&gt; <strong>Provider Keys</strong> -&gt; <strong>Add</strong>.</p>
<p><img src="/assets/upstream/images/ssl/add-secret-ai-gateway.png" alt="Import repo or choose template" /></p>
<p>You can also create your secret with the newly available <strong>ai_gateway</strong> scope via <a href="https://developers.cloudflare.com/workers/wrangler/commands/">wrangler</a>, the <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">Secrets Store dashboard</a>, or the <a href="https://developers.cloudflare.com/api/resources/secrets_store/">API</a>.</p>
<p>Then, pass the key in the request header using its Secrets Store reference:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic/v1/messages \&#10; &#45;-header &#x27;cf-aig-authorization: ANTHROPIC_KEY_1 \&#10; &#45;-header &#x27;anthropic-version: 2023-06-01&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-data  &#x27;{&quot;model&quot;: &quot;claude-3-opus-20240229&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Or, using Javascript:</p>
<pre tabindex="0"><code>import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;&#10;const anthropic = new Anthropic({&#10; apiKey: &quot;ANTHROPIC_KEY_1&quot;,&#10; baseURL: &quot;https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic&quot;,&#10;});&#10;&#10;&#10;const message = await anthropic.messages.create({&#10; model: &#x27;claude-3-opus-20240229&#x27;,&#10; messages: [{role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot;}],&#10; max_tokens: 1024&#10;});&#10;</code></pre>
<p>For more information, check out the <a href="https://blog.cloudflare.com/ai-gateway-aug-2025-refresh">blog</a>!</p>


<h2 id="content-type-returned-in-workers-assets-for-javascript-files-is-now-text-javascript"><a href="/changelog/post/2025-08-25-workers-assets-javascript-content-type/">Content type returned in Workers Assets for Javascript files is now `text/javascript`</a></h2>
<p><em>2025-08-25</em></p>
<p>JavaScript asset responses have been updated to use the <code>text/javascript</code> Content-Type header instead of <code>application/javascript</code>. While both MIME types are widely supported by browsers, the HTML Living Standard explicitly recommends <code>text/javascript</code> as the preferred type going forward.</p>
<p>This change improves:</p>
<ul>
<li>Standards alignment: Ensures consistency with the HTML spec and modern web platform guidance.</li>
<li>Interoperability: Some developer tools, validators, and proxies expect text/javascript and may warn or behave inconsistently with application/javascript.</li>
<li>Future-proofing: By following the spec-preferred MIME type, we reduce the risk of deprecation warnings or unexpected behavior in evolving browser environments.</li>
<li>Consistency: Most frameworks, CDNs, and hosting providers now default to text/javascript, so this change matches common ecosystem practice.</li>
</ul>
<p>Because all major browsers accept both MIME types, this update is backwards compatible and should not cause breakage.</p>
<p>Users will see this change on the next deployment of their assets.</p>


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


<h2 id="build-durable-multi-step-applications-in-python-with-workflows-now-in-beta"><a href="/changelog/post/2025-08-22-workflows-python-beta/">Build durable multi-step applications in Python with Workflows (now in beta)</a></h2>
<p><em>2025-08-22</em></p>
<p>You can now build <a href="/workflows/">Workflows</a> using Python. With Python Workflows, you get automatic retries, state persistence, and the ability to run multi-step operations that can span minutes, hours, or weeks using Python’s familiar syntax and the <a href="/workers/languages/python/">Python Workers</a> runtime.</p>
<p>Python Workflows use the same step-based execution model as JavaScript Workflows, but with Python syntax and access to Python’s ecosystem. Python Workflows also enable <a href="/workflows/python/dag/">DAG (Directed Acyclic Graph) workflows</a>, where you can define complex dependencies between steps using the depends parameter.</p>
<p>Here’s a simple example:</p>
<pre tabindex="0"><code class="language-python">from workers import Response, WorkflowEntrypoint&#10;&#10;class PythonWorkflowStarter(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do(&quot;my first step&quot;)&#10;        async def my_first_step():&#10;            &#35; do some work&#10;            return &quot;Hello Python!&quot;&#10;&#10;        await my_first_step()&#10;&#10;        await step.sleep(&quot;my-sleep-step&quot;, &quot;10 seconds&quot;)&#10;&#10;        @step.do(&quot;my second step&quot;)&#10;        async def my_second_step():&#10;            &#35; do some more work&#10;            return &quot;Hello again!&quot;&#10;&#10;        await my_second_step()&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        await self.env.MY_WORKFLOW.create()&#10;        return Response(&quot;Hello Workflow creation!&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17831.md")</aside>
<p>Python Workflows support the same core capabilities as JavaScript Workflows, including sleep scheduling, event-driven workflows, and built-in error handling with configurable retry policies.</p>
<p>To learn more and get started, refer to <a href="/workflows/python/">Python Workflows documentation</a>.</p>


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


<h2 id="easier-debugging-in-workers-with-improved-wrangler-error-screen"><a href="/changelog/post/2025-08-19-improved-wrangler-error-screen/">Easier debugging in Workers with improved Wrangler error screen</a></h2>
<p><em>2025-08-19</em></p>
<p>Wrangler's error screen has received several improvements to enhance your debugging experience!</p>
<p>The error screen now features a refreshed design thanks to <a href="https://www.npmjs.com/package/youch">youch</a>, with support for both light and dark themes, improved source map resolution logic that handles missing source files more reliably, and better error cause display.</p>
<table>
<thead>
<tr>
<th>Before</th>
<th>After (Light)</th>
<th>After (Dark)</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="/assets/upstream/images/workers/changelog/old-error-screen.png" alt="Old error screen" /></td>
<td><img src="/assets/upstream/images/workers/changelog/new-error-screen-light.png" alt="New light theme error screen" /></td>
<td><img src="/assets/upstream/images/workers/changelog/new-error-screen-dark.png" alt="New dark theme error screen" /></td>
</tr>
</tbody>
</table>
<p>Try it out now with <code>npx wrangler@latest dev</code> in your Workers project.</p>


<h2 id="terraform-v5-8-4-now-available"><a href="/changelog/post/2025-08-15-terraform-v5.8.4-provider/">Terraform v5.8.4 now available</a></h2>
<p><em>2025-08-15</em></p>
<p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare Community related to the v5 release. We have committed to releasing improvements on a two week cadence to ensure stability and reliability.</p>
<p>One key change we adopted in recent weeks is a pivot to more comprehensive, test-driven development. We are still evaluating individual issues, but are also investing in much deeper testing to drive our stabilization efforts. We will subsequently be investing in comprehensive migration scripts. As a result, you will see several of the highest traffic APIs have been stabilized in the most recent release, and are supported by comprehensive acceptance tests.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_argo_smart_routing`
  - `cloudflare_bot_management`
  - `cloudflare_list`
  - `cloudflare_list_item`
  - `cloudflare_load_balancer`
  - `cloudflare_load_balancer_monitor`
  - `cloudflare_load_balancer_pool`
  - `cloudflare_spectrum_application`
  - `cloudflare_managed_transforms`
  - `cloudflare_url_normalization_settings`
  - `cloudflare_snippet`
  - `cloudflare_snippet_rules`
  - `cloudflare_zero_trust_access_application`
  - `cloudflare_zero_trust_access_group`
  - `cloudflare_zero_trust_access_identity_provider`
  - `cloudflare_zero_trust_access_mtls_certificate`
  - `cloudflare_zero_trust_access_mtls_hostname_settings`
  - `cloudflare_zero_trust_access_policy`
  - `cloudflare_zone`
- Multipart handling restored for `cloudflare_snippet`
- `cloudflare_bot_management` diff issues resolves when running `terraform plan` and `terraform apply`
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.4">changelog</a> in GitHub.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-issues-closed">Issues Closed</h4>
- [#5017: 'Uncaught Error: No such module' using cloudflare_snippets](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5017)
- [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5640: cloudflare_argo_smart_routing importing doesn't read the actual value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5640)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This will help you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These migration scripts do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="the-node-js-and-web-file-system-apis-in-workers"><a href="/changelog/post/2025-08-15-nodejs-fs/">The Node.js and Web File System APIs in Workers</a></h2>
<p><em>2025-08-15</em></p>
<p>Implementations of the <a href="https://nodejs.org/docs/latest/api/fs.html"><code>node:fs</code> module</a> and the <a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API">Web File System API</a> are now available in Workers.</p>
<h4 id="2025-08-15-nodejs-fs-using-the-node-fs-module">Using the <code>node:fs</code> module</h4>
<p>The <code>node:fs</code> module provides access to a virtual file system in Workers. You can use it to read and write files, create directories, and perform other file system operations.</p>
<p>The virtual file system is ephemeral with each individual request havig its own isolated temporary file space. Files written to the file system will not persist across requests and will not be shared across requests or across different Workers.</p>
<p>Workers running with the <code>nodejs_compat</code> compatibility flag will have access to the <code>node:fs</code> module by default when the compatibility date is set to <code>2025-09-01</code> or later. Support for the API can also be enabled using the <code>enable_nodejs_fs_module</code> compatibility flag together with the <code>nodejs_compat</code> flag. The <code>node:fs</code> module can be disabled using the <code>disable_nodejs_fs_module</code> compatibility flag.</p>
<pre tabindex="0"><code class="language-js">import fs from &quot;node:fs&quot;;&#10;&#10;const config = JSON.parse(fs.readFileSync(&quot;/bundle/config.json&quot;, &quot;utf-8&quot;));&#10;&#10;export default {&#10;	async fetch(request) {&#10;		return new Response(`Config value: ${config.value}`);&#10;	},&#10;};&#10;</code></pre>
<p>There are a number of initial limitations to the <code>node:fs</code> implementation:</p>
<ul>
<li>The glob APIs (e.g. <code>fs.globSync(...)</code>) are not implemented.</li>
<li>The file watching APIs (e.g. <code>fs.watch(...)</code>) are not implemented.</li>
<li>The file timestamps (modified time, access time, etc) are only partially supported. For now, these will always return the Unix epoch.</li>
</ul>
<p>Refer to the <a href="https://nodejs.org/docs/latest/api/fs.html">Node.js documentation</a> for more information on the <code>node:fs</code> module and its APIs.</p>
<h4 id="2025-08-15-nodejs-fs-the-web-file-system-api">The Web File System API</h4>
<p>The Web File System API provides access to the same virtual file system as the <code>node:fs</code> module, but with a different API surface. The Web File System API is only available in Workers running with the <code>enable_web_file_system</code> compatibility flag. The <code>nodejs_compat</code> compatibility flag is not required to use the Web File System API.</p>
<pre tabindex="0"><code class="language-js">const root = navigator.storage.getDirectory();&#10;&#10;export default {&#10;	async fetch(request) {&#10;		const tmp = await root.getDirectoryHandle(&quot;/tmp&quot;);&#10;		const file = await tmp.getFileHandle(&quot;data.txt&quot;, { create: true });&#10;		const writable = await file.createWritable();&#10;		const writer = writable.getWriter();&#10;		await writer.write(&quot;Hello, World!&quot;);&#10;		await writer.close();&#10;&#10;		return new Response(&quot;File written successfully!&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>As there are still some parts of the Web File System API that are not fully standardized, there may be some differences between the Workers implementation and the implementations in browsers.</p>


<h2 id="workers-static-assets-corrected-handling-of-double-slashes-in-redirect-rule-paths"><a href="/changelog/post/2025-08-15-static-assets-redirect-url/">Workers Static Assets: Corrected handling of double slashes in redirect rule paths</a></h2>
<p><em>2025-08-15</em></p>
<p><a href="/workers/static-assets/">Static Assets</a>: Fixed a bug in how <a href="https://developers.cloudflare.com/workers/static-assets/redirects/">redirect rules</a> defined in your Worker's <code>_redirects</code> file are processed.</p>
<p>If you're serving Static Assets with a <code>_redirects</code> file containing a rule like <code>/ja/* /:splat</code>, paths with double slashes were previously misinterpreted as external URLs. For example, visiting <code>/ja//example.com</code> would incorrectly redirect to <code>https://example.com</code> instead of <code>/example.com</code> on your domain. This has been fixed and double slashes now correctly resolve as local paths. Note: <a href="/pages/">Cloudflare Pages</a> was not affected by this issue.</p>


<h2 id="workers-per-branch-preview-urls-now-support-long-branch-names"><a href="/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/">Workers per-branch preview URLs now support long branch names</a></h2>
<p><em>2025-08-14T01:00:00+00:00</em></p>
<p>We've updated <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> for Cloudflare Workers to support long branch names.</p>
<p>Previously, branch and Worker names exceeding the 63-character DNS limit would cause alias generation to fail, leaving pull requests without aliased preview URLs. This particularly impacted teams relying on descriptive branch naming.</p>
<p>Now, Cloudflare automatically truncates long branch names and appends a unique hash, ensuring every pull request gets a working preview link.</p>
<h4 id="2025-08-08-support-long-branch-names-preview-aliases-how-it-works">How it works</h4>
<ul>
<li><strong>63 characters or less</strong>: <code>&lt;branch-name&gt;-&lt;worker-name&gt;</code> → Uses actual branch name as is</li>
<li><strong>64 characters or more</strong>: <code>&lt;truncated-branch-name&gt;--&lt;hash&gt;-&lt;worker-name&gt;</code> → Uses truncated name with 4-character hash</li>
<li><strong>Hash generation</strong>: The hash is derived from the full branch name to ensure uniqueness</li>
<li><strong>Stable URLs</strong>: The same branch always generates the same hash across all commits</li>
</ul>
<h4 id="2025-08-08-support-long-branch-names-preview-aliases-requirements-and-compatibility">Requirements and compatibility</h4>
<ul>
<li><strong>Wrangler 4.30.0 or later</strong>: This feature requires updating to wrangler@4.30.0+</li>
<li><strong>No configuration needed</strong>: Works automatically with existing preview URL setups</li>
</ul>


<h2 id="python-workers-handlers-now-live-in-an-entrypoint-class"><a href="/changelog/post/2025-08-14-new-python-handlers/">Python Workers handlers now live in an entrypoint class</a></h2>
<p><em>2025-08-14</em></p>
<p>We are changing how Python Workers are structured by default. Previously, handlers were defined at the top-level of a module as <code>on_fetch</code>, <code>on_scheduled</code>, etc. methods, but now they live in an entrypoint class.</p>
<p>Here's an example of how to now define a Worker with a fetch handler:</p>
<pre tabindex="0"><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(&quot;Hello World!&quot;)&#10;</code></pre>
<p>To keep using the old-style handlers, you can specify the <code>disable_python_no_global_handlers</code> compatibility flag in your wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17785.md")</div>
<p>Consult the <a href="/workers/languages/python/">Python Workers documentation</a> for more details.</p>


<h2 id="terraform-provider-improvements-python-workers-support-smaller-plan-diffs-and-api-sdk-fixes"><a href="/changelog/post/2025-08-14-workers-terraform-and-sdk-improvements/">Terraform provider improvements — Python Workers support, smaller plan diffs, and API SDK fixes</a></h2>
<p><em>2025-08-14</em></p>
<p>The recent <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script">Cloudflare Terraform Provider</a> and SDK releases (such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a>) bring significant improvements to the Workers developer experience. These updates focus on reliability, performance, and adding <a href="/workers/languages/python/">Python Workers</a> support.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-terraform-improvements">Terraform Improvements</h4>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-fixed-unwarranted-plan-diffs">Fixed Unwarranted Plan Diffs</h4>
<p>Resolved several issues with the <code>cloudflare_workers_script</code> resource that resulted in unwarranted plan diffs, including:</p>
<ul>
<li>Using Durable Objects migrations</li>
<li>Using some bindings such as <code>secret_text</code></li>
<li>Using smart placement</li>
</ul>
<p>A resource should never show a plan diff if there isn't an actual change. This fix reduces unnecessary noise in your Terraform plan and is available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-improved-file-management">Improved File Management</h4>
<p>You can now specify <code>content_file</code> and <code>content_sha256</code> instead of <code>content</code>. This prevents the Workers script content from being stored in the state file which greatly reduces plan diff size and noise. If your workflow synced plans remotely, this should now happen much faster since there is less data to sync. This is available in Cloudflare Terraform Provider 5.7.0.</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id      = &quot;123456789&quot;&#10;  script_name     = &quot;my_worker&quot;&#10;  main_module     = &quot;worker.mjs&quot;&#10;  content_file    = &quot;worker.mjs&quot;&#10;  content_sha256  = filesha256(&quot;worker.mjs&quot;)&#10;}&#10;</code></pre>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-assets-headers-and-redirects-support">Assets Headers and Redirects Support</h4>
<p>Fixed the <code>cloudflare_workers_script</code> resource to properly support headers and redirects for Assets:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id      = &quot;123456789&quot;&#10;  script_name     = &quot;my_worker&quot;&#10;  main_module     = &quot;worker.mjs&quot;&#10;  content_file    = &quot;worker.mjs&quot;&#10;  content_sha256  = filesha256(&quot;worker.mjs&quot;)&#10;  assets = {&#10;    config = {&#10;      headers = file(&quot;_headers&quot;)&#10;      redirects = file(&quot;_redirects&quot;)&#10;    }&#10;    &#35; Completion jwt from:&#10;    &#35; https://developers.cloudflare.com/api/resources/workers/subresources/assets/subresources/upload/&#10;    jwt = &quot;jwt&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-python-workers-support">Python Workers Support</h4>
<p>Added support for uploading <a href="/workers/languages/python/">Python Workers</a> (beta) in Terraform. You can now deploy Python Workers with:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_workers_script&quot; &quot;my_worker&quot; {&#10;  account_id       = &quot;123456789&quot;&#10;  script_name      = &quot;my_worker&quot;&#10;  content_file     = &quot;worker.py&quot;&#10;  content_sha256   = filesha256(&quot;worker.py&quot;)&#10;  content_type     = &quot;text/x-python&quot;&#10;}&#10;</code></pre>
<p>Available in Cloudflare Terraform Provider 5.8.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-sdk-enhancements">SDK Enhancements</h4>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-improved-file-upload-api">Improved File Upload API</h4>
<p>Fixed an issue where Workers script versions in the SDK did not allow uploading files. This now works, and also has an improved files upload interface:</p>
<pre tabindex="0"><code class="language-js">const scriptContent = `&#10;  export default {&#10;    async fetch(request, env, ctx) {&#10;      return new Response(&#x27;Hello World!&#x27;, { status: 200 });&#10;    }&#10;  };&#10;`;&#10;&#10;client.workers.scripts.versions.create(&#x27;my-worker&#x27;, {&#10;  account_id: &#x27;123456789&#x27;,&#10;  metadata: {&#10;    main_module: &#x27;my-worker.mjs&#x27;,&#10;  },&#10;  files: [&#10;    await toFile(&#10;      Buffer.from(scriptContent),&#10;      &#x27;my-worker.mjs&#x27;,&#10;      {&#10;        type: &quot;application/javascript+module&quot;,&#10;      }&#10;    )&#10;  ]&#10;});&#10;</code></pre>
<p>Will be available in cloudflare-typescript 4.6.0. A similar change will be available in cloudflare-python 4.4.0.</p>
<h4 id="2025-08-14-workers-terraform-and-sdk-improvements-fixed-updating-kv-values">Fixed updating KV values</h4>
<p>Previously when creating a KV value like this:</p>
<pre tabindex="0"><code class="language-js">await cf.kv.namespaces.values.update(&quot;my-kv-namespace&quot;, &quot;key1&quot;, {&#10;  account_id: &quot;123456789&quot;,&#10;  metadata: &quot;my metadata&quot;,&#10;  value: JSON.stringify({&#10;    hello: &quot;world&quot;&#10;  })&#10;});&#10;</code></pre>
<p>...and recalling it in your Worker like this:</p>
<pre tabindex="0"><code class="language-ts">const value = await c.env.KV.get&lt;{hello: string}&gt;(&quot;key1&quot;, &quot;json&quot;);&#10;</code></pre>
<p>You'd get back this: <code>{metadata:'my metadata', value:&quot;{'hello':'world'}&quot;}</code> instead of the correct value of <code>{hello: 'world'}</code></p>
<p>This is fixed in cloudflare-typescript 4.5.0 and will be fixed in cloudflare-python 4.4.0.</p>


<h2 id="messagechannel-and-messageport"><a href="/changelog/post/2025-08-11-messagechannel/">MessageChannel and MessagePort</a></h2>
<p><em>2025-08-11T01:00:00+00:00</em></p>
<p>A minimal implementation of the <a href="https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel">MessageChannel API</a> is now available in Workers. This means that you can use <code>MessageChannel</code> to send messages between different parts of your Worker, but not across different Workers.</p>
<p>The <code>MessageChannel</code> and <code>MessagePort</code> APIs will be available by default at the global scope
with any worker using a compatibility date of <code>2025-08-15</code> or later. It is also available
using the <code>expose_global_message_channel</code> compatibility flag, or can be explicitly disabled
using the <code>no_expose_global_message_channel</code> compatibility flag.</p>
<pre tabindex="0"><code class="language-js">const { port1, port2 } = new MessageChannel();&#10;&#10;port2.onmessage = (event) =&gt; {&#10;	console.log(&#x27;Received message:&#x27;, event.data);&#10;};&#10;&#10;port2.postMessage(&#x27;Hello from port2!&#x27;);&#10;</code></pre>
<p>Any value that can be used with the <code>structuredClone(...)</code> API can be sent over the port.</p>
<h4 id="2025-08-11-messagechannel-differences">Differences</h4>
<p>There are a number of key limitations to the <code>MessageChannel</code> API in Workers:</p>
<ul>
<li>Transfer lists are currently not supported. This means that you will not be able to transfer
ownership of objects like <code>ArrayBuffer</code> or <code>MessagePort</code> between ports.</li>
<li>The <code>MessagePort</code> is not yet serializable. This means that you cannot send a <code>MessagePort</code> object
through the <code>postMessage</code> method or via JSRPC calls.</li>
<li>The <code>'messageerror'</code> event is only partially supported. If the <code>'onmessage'</code> handler throws an
error, the <code>'messageerror'</code> event will be triggered, however, it will not be triggered when there
are errors serializing or deserializing the message data. Instead, the error will be thrown when
the <code>postMessage</code> method is called on the sending port.</li>
<li>The <code>'close'</code> event will be emitted on both ports when one of the ports is closed, however it
will not be emitted when the Worker is terminated or when one of the ports is garbage collected.</li>
</ul>


<h2 id="wrangler-and-the-cloudflare-vite-plugin-support-env-files-in-local-development"><a href="/changelog/post/2025-08-08-dot-env-in-local-dev/">Wrangler and the Cloudflare Vite plugin support `.env` files in local development</a></h2>
<p><em>2025-08-08T01:00:00+00:00</em></p>
<p>Now, you can use <code>.env</code> files to provide secrets and override environment variables on the <code>env</code> object during local development with Wrangler and the Cloudflare Vite plugin.</p>
<p>Previously in local development, if you wanted to provide secrets or environment variables during local development, you had to use <code>.dev.vars</code> files.
This is still supported, but you can now also use <code>.env</code> files, which are more familiar to many developers.</p>
<h4 id="2025-08-08-dot-env-in-local-dev-using-env-files-in-local-development">Using <code>.env</code> files in local development</h4>
<p>You can create a <code>.env</code> file in your project root to define environment variables that will be used when running <code>wrangler dev</code> or <code>vite dev</code>. The <code>.env</code> file should be formatted like a <code>dotenv</code> file, such as <code>KEY=&quot;VALUE&quot;</code>:</p>
<pre tabindex="0"><code class="language-bash">TITLE=&quot;My Worker&quot;&#10;API_TOKEN=&quot;dev-token&quot;&#10;</code></pre>
<p>When you run <code>wrangler dev</code> or <code>vite dev</code>, the environment variables defined in the <code>.env</code> file will be available in your Worker code via the <code>env</code> object:</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		const title = env.TITLE; // &quot;My Worker&quot;&#10;		const apiToken = env.API_TOKEN; // &quot;dev-token&quot;&#10;		const response = await fetch(&#10;			`https://api.example.com/data?token=${apiToken}`,&#10;		);&#10;		return new Response(`Title: ${title} - ` + (await response.text()));&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-08-08-dot-env-in-local-dev-multiple-environments-with-env-files">Multiple environments with <code>.env</code> files</h4>
<p>If your Worker defines multiple <a href="/workers/wrangler/environments/">environments</a>, you can set different variables for each environment (ex: production or staging) by creating files named <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you use <code>wrangler &lt;command&gt; --env &lt;environment-name&gt;</code> or <code>CLOUDFLARE_ENV=&lt;environment-name&gt; vite dev</code>, the corresponding environment-specific file will also be loaded and merged with the <code>.env</code> file.</p>
<p>For example, if you want to set different environment variables for the <code>staging</code> environment, you can create a file named <code>.env.staging</code>:</p>
<pre tabindex="0"><code class="language-bash">API_TOKEN=&quot;staging-token&quot;&#10;</code></pre>
<p>When you run <code>wrangler dev --env staging</code> or <code>CLOUDFLARE_ENV=staging vite dev</code>, the environment variables from <code>.env.staging</code> will be merged onto those from <code>.env</code>.</p>
<pre tabindex="0"><code class="language-javascript">export default {&#10;	async fetch(request, env) {&#10;		const title = env.TITLE; // &quot;My Worker&quot; (from `.env`)&#10;		const apiToken = env.API_TOKEN; // &quot;staging-token&quot; (from `.env.staging`, overriding the value from `.env`)&#10;		const response = await fetch(&#10;			`https://api.example.com/data?token=${apiToken}`,&#10;		);&#10;		return new Response(`Title: ${title} - ` + (await response.text()));&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-08-08-dot-env-in-local-dev-find-out-more">Find out more</h4>
<p>For more information on how to use <code>.env</code> files with Wrangler and the Cloudflare Vite plugin, see the following documentation:</p>
<ul>
<li><a href="/workers/local-development/environment-variables">Environment variables and secrets</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler">Wrangler Documentation</a></li>
<li><a href="https://developers.cloudflare.com/workers/wrangler/vite">Cloudflare Vite Plugin Documentation</a></li>
</ul>


<h2 id="introducing-observability-and-metrics-for-stream-live-inputs"><a href="/changelog/post/2025-08-08-stream-live-observability/">Introducing observability and metrics for Stream Live Inputs</a></h2>
<p><em>2025-08-08</em></p>
<p>New information about broadcast metrics and events is now available in
<a href="/stream/">Cloudflare Stream</a> in the Live Input details of the Dashboard.</p>
<p><img src="/assets/upstream/images/changelog/stream/2025-08-05-live-input-metrics.png" alt="Live Input details showing metrics" /></p>
<p>You can now easily understand broadcast-side health and performance with new
observability, which can help when troubleshooting common issues, particularly
for new customers who are just getting started, and platform customers who may
have limited visibility into how their end-users configure their encoders.</p>
<p>To get started, start a live stream (<a href="/stream/examples/obs-from-scratch/">just getting started?</a>), then visit the Live Input details page in Dash.</p>
<p>See our new live <a href="/stream/stream-live/troubleshooting/">Troubleshooting</a> guide
to learn what these metrics mean and how to use them to address common broadcast
issues.</p>


<h2 id="directly-import-waituntil-in-workers-for-easily-spawning-background-tasks"><a href="/changelog/post/2025-08-08-add-waituntil-cloudflare-workers/">Directly import `waitUntil` in Workers for easily spawning background tasks</a></h2>
<p><em>2025-08-08</em></p>
<p>You can now import <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a> from <code>cloudflare:workers</code> to extend your Worker's execution beyond the request lifecycle from anywhere in your code.</p>
<p>Previously, <code>waitUntil</code> could only be accessed through the <a href="/workers/runtime-apis/context/">execution context</a> (<code>ctx</code>) parameter passed to your Worker's handler functions. This meant that if you needed to schedule background tasks from deeply nested functions or utility modules, you had to pass the <code>ctx</code> object through multiple function calls to access <code>waitUntil</code>.</p>
<p>Now, you can import <code>waitUntil</code> directly and use it anywhere in your Worker without needing to pass <code>ctx</code> as a parameter:</p>
<pre tabindex="0"><code class="language-js">import { waitUntil } from &quot;cloudflare:workers&quot;;&#10;&#10;export function trackAnalytics(eventData) {&#10;	const analyticsPromise = fetch(&quot;https://analytics.example.com/track&quot;, {&#10;		method: &quot;POST&quot;,&#10;		body: JSON.stringify(eventData),&#10;	});&#10;&#10;	// Extend execution to ensure analytics tracking completes&#10;	waitUntil(analyticsPromise);&#10;}&#10;</code></pre>
<p>This is particularly useful when you want to:</p>
<ul>
<li>Schedule background tasks from utility functions or modules</li>
<li>Extend execution for analytics, logging, or cleanup operations</li>
<li>Avoid passing the execution context through multiple layers of function calls</li>
</ul>
<pre tabindex="0"><code class="language-js">import { waitUntil } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Background task that should complete even after response is sent&#10;		cleanupTempData(env.KV_NAMESPACE);&#10;		return new Response(&quot;Hello, World!&quot;);&#10;	}&#10;};&#10;&#10;function cleanupTempData(kvNamespace) {&#10;	// This function can now use waitUntil without needing ctx&#10;	const deletePromise = kvNamespace.delete(&quot;temp-key&quot;);&#10;	waitUntil(deletePromise);&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17784.md")</aside>
<p>For more information, see the <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code> documentation</a>.</p>


<h2 id="requests-made-from-cloudflare-workers-can-now-force-a-revalidation-of-their-cache-with-the-origin"><a href="/changelog/post/2025-08-07-cache-no-cache/">Requests made from Cloudflare Workers can now force a revalidation of their cache with the origin</a></h2>
<p><em>2025-08-07</em></p>
<p>By setting the value of the <code>cache</code> property to <code>no-cache</code>, you can force <a href="/workers/reference/how-the-cache-works/">Cloudflare's
cache</a> to revalidate its contents with the origin when
making subrequests from <a href="/workers">Cloudflare Workers</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17783.md")</div>
<p>When <code>no-cache</code> is set, the Worker request will first look for a match in Cloudflare's cache, then:</p>
<ul>
<li>If there is a match, a conditional request is sent to the origin, regardless of whether or not the match is fresh or stale. If the resource has not changed, the
cached version is returned. If the resource has changed, it will be downloaded from the origin, updated in the cache, and returned.</li>
<li>If there is no match, Workers will make a standard request to the origin and cache the response.</li>
</ul>
<p>This increases compatibility with NPM packages and JavaScript frameworks that rely on setting the
<a href="/workers/runtime-apis/request/#options"><code>cache</code></a> property, which is a cross-platform standard part
of the <a href="/workers/runtime-apis/request/"><code>Request</code></a> interface. Previously, if you set the <code>cache</code>
property on <code>Request</code> to <code>'no-cache'</code>, the Workers runtime threw an exception.</p>
<ul>
<li>Learn <a href="/workers/reference/how-the-cache-works/">how the Cache works with Cloudflare Workers</a></li>
<li>Enable <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> for your Cloudflare Worker</li>
<li>Explore <a href="/workers/runtime-apis/">Runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">Bindings</a> available in Cloudflare Workers</li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/16/">Previous</a><span>Page 17 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/18/">Next</a></nav>
