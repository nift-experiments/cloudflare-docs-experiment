<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 4, 2025</time><h2 id="post-title">A new, simpler REST API for Cloudflare Workers (Beta)</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now manage <a href="/api/resources/workers/subresources/beta/subresources/workers/methods/create/"><strong>Workers</strong></a>, <a href="/api/resources/workers/subresources/beta/subresources/workers/models/worker/#(schema)"><strong>Versions</strong></a>, and <a href="/api/resources/workers/subresources/scripts/subresources/content/methods/update/"><strong>Deployments</strong></a> as separate resources with a new, resource-oriented API (Beta).</p>
<p>This new API is supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider</a> and the <a href="https://github.com/cloudflare/cloudflare-typescript">Cloudflare Typescript SDK</a>, allowing platform teams to manage a Worker's infrastructure in Terraform, while development teams handle code deployments from a separate repository or workflow. We also designed this API with AI agents in mind, as a clear, predictable structure is essential for them to reliably build, test, and deploy applications.</p>
<h4 id="try-it-out">Try it out</h4>
- [**New beta API endpoints**](/api/resources/workers/subresources/beta/)
- [**Cloudflare TypeScript SDK v5.0.0**](https://github.com/cloudflare/cloudflare-typescript)
- [**Cloudflare Go SDK v6.0.0**](https://github.com/cloudflare/cloudflare-go)
- [**Terraform provider v5.9.0**](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs): [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) , [`cloudflare_worker_version`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version), and [`cloudflare_workers_deployments`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_deployment) resources.
- See full examples in our [Infrastructure as Code (IaC) guide](/workers/platform/infrastructure-as-code)
<h4 id="before-eight-endpoints-with-mixed-responsibilities">Before: Eight+ endpoints with mixed responsibilities</h4>
<img src="/assets/upstream/images/workers/platform/api-before.png" alt="Before">
<p>The existing API was originally designed for simple, one-shot script uploads:</p>
<pre><code class="language-sh">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/workers/scripts/$SCRIPT_NAME&quot; \&#10;    &#45;H &quot;X-Auth-Email: $CLOUDFLARE_EMAIL&quot; \&#10;    &#45;H &quot;X-Auth-Key: $CLOUDFLARE_API_KEY&quot; \&#10;    &#45;H &quot;Content-Type: multipart/form-data&quot; \&#10;    &#45;F &#x27;metadata={&#10;      &quot;main_module&quot;: &quot;worker.js&quot;,&#10;      &quot;compatibility_date&quot;: &quot;$today$&quot;&#10;    }&#x27; \&#10;    &#45;F &quot;worker.js=@worker.js;type=application/javascript+module&quot;&#10;</code></pre>
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
<h4 id="after-three-resources-with-clear-boundaries">After: Three resources with clear boundaries</h4>
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
<h4 id="why-this-matters">Why this matters</h4>
<h4 id="you-can-now-create-workers-before-uploading-code">You can now create Workers before uploading code</h4>
<p>Workers are now standalone resources that can be created and configured without any code. Platform teams can provision Workers with the right settings, then hand them off to development teams for implementation.</p>
<h4 id="example-typescript-sdk">Example: Typescript SDK</h4>
<pre><code class="language-ts">// Step 1: Platform team creates the Worker resource (no code needed)&#10;const worker = await client.workers.beta.workers.create({&#10;  name: &quot;payment-service&quot;,&#10;  account_id: &quot;...&quot;,&#10;  observability: {&#10;    enabled: true,&#10;  },&#10;});&#10;<p>// Step 2: Development team adds code and creates a version later&#10;const version = await client.workers.beta.workers.versions.create(worker.id, {&#10;account_id: &quot;...&quot;,&#10;main_module: &quot;worker.js&quot;,&#10;compatibility_date: &quot;$today&quot;,&#10;bindings: [ /<em>...</em>/ ],&#10;modules: [&#10;{&#10;name: &quot;worker.js&quot;,&#10;content_type: &quot;application/javascript+module&quot;,&#10;content_base64: Buffer.from(scriptContent).toString(&quot;base64&quot;),&#10;},&#10;],&#10;});</p>&#10;<p>// Step 3: Deploy explicitly when ready&#10;const deployment = await client.workers.scripts.deployments.create(worker.name, {&#10;account_id: &quot;...&quot;,&#10;strategy: &quot;percentage&quot;,&#10;versions: [&#10;{&#10;percentage: 100,&#10;version_id: version.id,&#10;},&#10;],&#10;});&#10;</code></pre></p>
<h4 id="example-terraform">Example: Terraform</h4>
If you use Terraform, you can now declare the Worker in your Terraform configuration and manage configuration outside of Terraform in your Worker's [`wrangler.jsonc` file](/workers/wrangler/configuration/) and deploy code changes using [Wrangler](/workers/wrangler/).
<pre><code class="language-tf">resource &quot;cloudflare_worker&quot; &quot;my_worker&quot; {&#10;  account_id = &quot;...&quot;&#10;  name = &quot;my-important-service&quot;&#10;}&#10;&#35; Manage Versions and Deployments here or outside of Terraform&#10;&#35; resource &quot;cloudflare_worker_version&quot; &quot;my_worker_version&quot; {}&#10;&#35; resource &quot;cloudflare_workers_deployment&quot; &quot;my_worker_deployment&quot; {}&#10;</code></pre>
<h4 id="deployments-are-always-explicit-never-implicit">Deployments are always explicit, never implicit</h4>
<p>Creating a version and deploying it are now always explicit, separate actions - never implicit side effects. To update version-specific settings (like bindings), you create a new version with those changes. The existing deployed version remains unchanged until you explicitly deploy the new one.</p>
<pre><code class="language-sh">&#35; Step 1: Create a new version with updated settings (doesn&#x27;t affect live traffic)&#10;POST /workers/workers/{id}/versions&#10;{&#10;  &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;  &quot;bindings&quot;: [&#10;    {&#10;      &quot;name&quot;: &quot;MY_NEW_ENV_VAR&quot;,&#10;      &quot;text&quot;: &quot;new_value&quot;,&#10;      &quot;type&quot;: &quot;plain_text&quot;&#10;    }&#10;  ],&#10;  &quot;modules&quot;: [...]&#10;}&#10;&#10;&#35; Step 2: Explicitly deploy when ready (now affects live traffic)&#10;POST /workers/scripts/{script_name}/deployments&#10;{&#10;  &quot;strategy&quot;: &quot;percentage&quot;,&#10;  &quot;versions&quot;: [&#10;    {&#10;      &quot;percentage&quot;: 100,&#10;      &quot;version_id&quot;: &quot;new_version_id&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h4 id="settings-are-clearly-organized-by-scope">Settings are clearly organized by scope</h4>
Configuration is now logically divided: [**Worker settings**](/api/resources/workers/subresources/beta/subresources/workers/) (like `name` and `tags`) persist across all versions, while [**Version settings**](/api/resources/workers/subresources/beta/subresources/workers/subresources/versions/) (like `bindings` and `compatibility_date`) are specific to each code snapshot.
<pre><code class="language-sh">&#35; Worker settings (the parent resource)&#10;PUT /workers/workers/{id}&#10;{&#10;  &quot;name&quot;: &quot;payment-service&quot;,&#10;  &quot;tags&quot;: [&quot;production&quot;],&#10;  &quot;logpush&quot;: true,&#10;}&#10;</code></pre>
<pre><code class="language-sh">&#35; Version settings (the &quot;code&quot;)&#10;POST /workers/workers/{id}/versions&#10;{&#10;  &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;  &quot;bindings&quot;: [...],&#10;  &quot;modules&quot;: [...]&#10;}&#10;</code></pre>
<h4 id="workers-api-endpoints-now-support-uuids-in-addition-to-names"><code>/workers</code> API endpoints now support UUIDs (in addition to names)</h4>
<p>The <code>/workers/workers/</code> path now supports addressing a Worker by both its immutable UUID and its mutable name.</p>
<pre><code class="language-sh">&#35; Both work for the same Worker&#10;GET /workers/workers/29494978e03748669e8effb243cf2515  # UUID (stable for automation)&#10;GET /workers/workers/payment-service                  # Name (convenient for humans)&#10;</code></pre>
<p>This dual approach means:</p>
<ul>
<li>Developers can use readable names for debugging.</li>
<li>Automation can rely on stable UUIDs to prevent errors when Workers are renamed.</li>
<li>Terraform can rename Workers without destroying and recreating them.</li>
</ul>
<h4 id="learn-more">Learn more</h4>
- [Infrastructure as Code (IaC) guide](/workers/platform/infrastructure-as-code)
- [API documentation](/api/resources/workers/subresources/beta/)
- [Versions and Deployments overview](/workers/versions-and-deployments/)
<h4 id="technical-notes">Technical notes</h4>
<ul>
<li>The pre-existing Workers REST API remains fully supported. Once the new API exits beta, we'll provide a migration timeline with ample notice and comprehensive migration guides.</li>
<li>Existing Terraform resources and SDK methods will continue to be fully supported through the current major version.</li>
<li>While the Deployments API currently remains on the <code>/scripts/</code> endpoint, we plan to introduce a new Deployments endpoint under <code>/workers/</code> to match the new API structure.</li>
</ul>
</div></article></div>
