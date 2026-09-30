---
cp9:
  canonical: https://developers.cloudflare.com/workers/platform/infrastructure-as-code/
  description: Deploy and manage Cloudflare Workers using Terraform, Pulumi, and the Cloudflare API SDKs.
  full_title: Infrastructure as Code (IaC) · Cloudflare Workers docs
  head_html: <title>Infrastructure as Code (IaC) · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy and manage Cloudflare Workers using Terraform, Pulumi, and the Cloudflare API SDKs."><link rel="canonical" href="https://developers.cloudflare.com/workers/platform/infrastructure-as-code/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/platform/infrastructure-as-code/index.md"><meta property="og:title" content="Infrastructure as Code (IaC) · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy and manage Cloudflare Workers using Terraform, Pulumi, and the Cloudflare API SDKs."><meta property="og:url" content="https://developers.cloudflare.com/workers/platform/infrastructure-as-code/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/platform/infrastructure-as-code/#page","headline":"Infrastructure as Code (IaC) \u00b7 Cloudflare Workers docs","description":"Deploy and manage Cloudflare Workers using Terraform, Pulumi, and the Cloudflare API SDKs.","url":"https://developers.cloudflare.com/workers/platform/infrastructure-as-code/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/platform/infrastructure-as-code/
  schema: 1
---
<p>While <a href="/workers/wrangler/configuration">Wrangler</a> makes it easy to upload and manage Workers, there are times when you need a more programmatic approach. This could involve using Infrastructure as Code (IaC) tools or interacting directly with the <a href="/api/resources/workers/">Workers API</a>. Examples include build and deploy scripts, CI/CD pipelines, custom developer tools, and automated testing.</p>
<p>To make this easier, Cloudflare provides SDK libraries for popular languages such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> and <a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a>. For IaC, you can use tools like HashiCorp's Terraform and the <a href="/terraform">Cloudflare Terraform Provider</a> to manage Workers resources.</p>
<p>Below are examples of deploying a Worker using different tools and languages, along with important considerations for managing Workers with IaC.</p>
<p>All of these examples need an <a href="/fundamentals/account/find-account-and-zone-ids">account ID</a> and <a href="/fundamentals/api/get-started/create-token">API token</a> (not Global API key) to work.</p>
<h2 id="workers-bundling">Workers Bundling</h2>
<p>None of the examples below do <a href="/workers/wrangler/bundling">Workers Bundling</a>. This is usually done with Wrangler or a tool like <a href="https://esbuild.github.io">esbuild</a>.</p>
<p>Generally, you'd run this bundling step before applying your Terraform plan or using the API for script upload:</p>
<pre tabindex="0"><code class="language-bash">wrangler deploy --dry-run --outdir build&#10;</code></pre>
<p>When using Wrangler for building and a different method for uploading, make sure to copy all of your config from <code>wrangler.json</code> into your Terraform config or API request. This is especially important with <code>compatibility_date</code> or flags your script relies on.</p>
<h2 id="terraform">Terraform</h2>
<p>In this example, you need a local file named <code>my-script.mjs</code> with script content similar to the below examples. Learn more about the <a href="/terraform/">Cloudflare Terraform Provider</a>, and refer to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/blob/main/examples/resources/cloudflare_workers_script/resource.tf">Workers script resource example</a> for all available resource settings.</p>
<pre tabindex="0"><code class="language-tf">variable &quot;account_id&quot; {&#10;  default = &quot;replace_me&quot;&#10;}&#10;&#10;resource &quot;cloudflare_worker&quot; &quot;my_worker&quot; {&#10;  account_id = var.account_id&#10;  name = &quot;my-worker&quot;&#10;  observability = {&#10;    enabled = true&#10;  }&#10;}&#10;&#10;resource &quot;cloudflare_worker_version&quot; &quot;my_worker_version&quot; {&#10;  account_id = var.account_id&#10;  worker_id = cloudflare_worker.my_worker.id&#10;  compatibility_date = &quot;2025-02-21&quot; # Set this to today&#x27;s date&#10;  main_module = &quot;my-script.mjs&quot;&#10;  modules = [&#10;    {&#10;      name = &quot;my-script.mjs&quot;&#10;      content_type = &quot;application/javascript+module&quot;&#10;      &#35; Replacement (version creation) is triggered whenever this file changes&#10;      content_file = &quot;my-script.mjs&quot;&#10;    }&#10;  ]&#10;}&#10;&#10;resource &quot;cloudflare_workers_deployment&quot; &quot;my_worker_deployment&quot; {&#10;  account_id = var.account_id&#10;  script_name = cloudflare_worker.my_worker.name&#10;  strategy = &quot;percentage&quot;&#10;  versions = [{&#10;    percentage = 100&#10;    version_id = cloudflare_worker_version.my_worker_version.id&#10;  }]&#10;}&#10;</code></pre>
<p>Notice how you do not have to manage all of these resources in Terraform. For example, you could use just the <code>cloudflare_worker</code> resource and seamlessly use Wrangler or your own deployment tools for Versions or Deployments.</p>
<h2 id="bindings-in-terraform">Bindings in Terraform</h2>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Worker to interact with resources on the Cloudflare Developer Platform. In Terraform, bindings are configured differently than in Wrangler. Instead of separate top-level properties for each binding type (like <code>kv_namespaces</code>, <code>r2_buckets</code>, etc.), Terraform uses a single <code>bindings</code> array where each binding has a <code>type</code> property along with type-specific properties.</p>
<p>Below are examples of each binding type and their required properties:</p>
<h3 id="kv-namespace-binding">KV Namespace Binding</h3>
<p>Bind to a <a href="/kv/api/">KV namespace</a> for key-value storage:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;kv_namespace&quot;&#10;  name = &quot;MY_KV&quot;&#10;  namespace_id = &quot;your-kv-namespace-id&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;kv_namespace&quot;</code></li>
<li><code>name</code>: The variable name for the binding, accessible via <code>env.MY_KV</code></li>
<li><code>namespace_id</code>: The ID of your KV namespace</li>
</ul>
<h3 id="r2-bucket-binding">R2 Bucket Binding</h3>
<p>Bind to an <a href="/r2/api/workers/workers-api-reference/">R2 bucket</a> for object storage:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;r2_bucket&quot;&#10;  name = &quot;MY_BUCKET&quot;&#10;  bucket_name = &quot;my-bucket-name&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;r2_bucket&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.MY_BUCKET</code></li>
<li><code>bucket_name</code>: The name of your R2 bucket</li>
</ul>
<h3 id="d1-database-binding">D1 Database Binding</h3>
<p>Bind to a <a href="/d1/worker-api/">D1 database</a> for SQL storage:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;d1&quot;&#10;  name = &quot;DB&quot;&#10;  id = &quot;your-database-id&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;d1&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.DB</code></li>
<li><code>id</code>: The ID of your D1 database</li>
</ul>
<h3 id="durable-object-binding">Durable Object Binding</h3>
<p>Bind to a <a href="/durable-objects/api/">Durable Object</a> class:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;durable_object_namespace&quot;&#10;  name = &quot;MY_DURABLE_OBJECT&quot;&#10;  class_name = &quot;MyDurableObjectClass&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;durable_object_namespace&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.MY_DURABLE_OBJECT</code></li>
<li><code>class_name</code>: The exported class name of the Durable Object</li>
<li><code>script_name</code>: (Optional) The Worker script that exports this Durable Object class. Omit if the class is defined in the same Worker.</li>
</ul>
<h3 id="service-binding">Service Binding</h3>
<p>Bind to another <a href="/workers/runtime-apis/bindings/service-bindings/">Worker</a> for Worker-to-Worker communication:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;service&quot;&#10;  name = &quot;MY_SERVICE&quot;&#10;  service = &quot;other-worker-name&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;service&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.MY_SERVICE</code></li>
<li><code>service</code>: The name of the target Worker</li>
<li><code>entrypoint</code>: (Optional) The named <a href="/workers/runtime-apis/bindings/service-bindings/rpc/#named-entrypoints">entrypoint</a> to bind to</li>
</ul>
<h3 id="queue-binding">Queue Binding</h3>
<p>Bind to a <a href="/queues/configuration/javascript-apis/">Queue</a> for message passing:</p>
<p>For producing messages:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;queue&quot;&#10;  name = &quot;MY_QUEUE&quot;&#10;  queue_name = &quot;my-queue&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;queue&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.MY_QUEUE</code></li>
<li><code>queue_name</code>: The name of your Queue</li>
</ul>
<p>For consuming messages, configure your Worker as a consumer in the queue resource itself, not via bindings.</p>
<h3 id="vectorize-binding">Vectorize Binding</h3>
<p>Bind to a <a href="/vectorize/">Vectorize index</a> for vector search:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;vectorize&quot;&#10;  name = &quot;VECTORIZE_INDEX&quot;&#10;  index_name = &quot;my-index&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;vectorize&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.VECTORIZE_INDEX</code></li>
<li><code>index_name</code>: The name of your Vectorize index</li>
</ul>
<h3 id="workers-ai-binding">Workers AI Binding</h3>
<p>Bind to <a href="/workers-ai/">Workers AI</a> for AI inference:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;ai&quot;&#10;  name = &quot;AI&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;ai&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.AI</code></li>
</ul>
<h3 id="hyperdrive-binding">Hyperdrive Binding</h3>
<p>Bind to a <a href="/hyperdrive/">Hyperdrive</a> configuration for database connection pooling:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;hyperdrive&quot;&#10;  name = &quot;HYPERDRIVE&quot;&#10;  id = &quot;your-hyperdrive-config-id&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;hyperdrive&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.HYPERDRIVE</code></li>
<li><code>id</code>: The ID of your Hyperdrive configuration</li>
</ul>
<h3 id="vpc-service-binding">VPC Service Binding</h3>
<p>Bind to a <a href="/workers-vpc/configuration/vpc-services/">VPC Service</a> for accessing resources in your private network:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;vpc_service&quot;&#10;  name = &quot;PRIVATE_API&quot;&#10;  service_id = &quot;your-vpc-service-id&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;vpc_service&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.PRIVATE_API</code></li>
<li><code>service_id</code>: The ID of your VPC Service (from <code>cloudflare_connectivity_directory_service</code> or the dashboard)</li>
</ul>
<p>You can create the VPC Service with Terraform using the <code>cloudflare_connectivity_directory_service</code> resource. For a full walkthrough, refer to <a href="/workers-vpc/configuration/vpc-services/terraform/">Configure VPC Services with Terraform</a>.</p>
<h3 id="analytics-engine-binding">Analytics Engine Binding</h3>
<p>Bind to an <a href="/analytics/analytics-engine/">Analytics Engine</a> dataset:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;analytics_engine&quot;&#10;  name = &quot;ANALYTICS&quot;&#10;  dataset = &quot;my_dataset&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;analytics_engine&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.ANALYTICS</code></li>
<li><code>dataset</code>: The name of your Analytics Engine dataset</li>
</ul>
<h3 id="environment-variables">Environment Variables</h3>
<p>For plain text environment variables, use the <code>plain_text</code> binding type:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;plain_text&quot;&#10;  name = &quot;MY_VARIABLE&quot;&#10;  text = &quot;my-value&quot;&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;plain_text&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.MY_VARIABLE</code></li>
<li><code>text</code>: The value of the environment variable</li>
</ul>
<h3 id="secret-text-binding">Secret Text Binding</h3>
<p>For encrypted secrets, use the <code>secret_text</code> binding type:</p>
<pre tabindex="0"><code class="language-tf">bindings = [{&#10;  type = &quot;secret_text&quot;&#10;  name = &quot;API_KEY&quot;&#10;  text = var.api_key&#10;}]&#10;</code></pre>
<p><strong>Properties:</strong></p>
<ul>
<li><code>type</code>: <code>&quot;secret_text&quot;</code></li>
<li><code>name</code>: The binding name to access via <code>env.API_KEY</code></li>
<li><code>text</code>: The secret value (will be encrypted)</li>
</ul>
<h3 id="complete-example">Complete Example</h3>
<p>Here's an example combining multiple binding types:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_worker_version&quot; &quot;my_worker_version&quot; {&#10;  account_id = var.account_id&#10;  worker_id = cloudflare_worker.my_worker.id&#10;  compatibility_date = &quot;2025-08-06&quot;&#10;  main_module = &quot;worker.js&quot;&#10;&#10;  modules = [{&#10;    name = &quot;worker.js&quot;&#10;    content_type = &quot;application/javascript+module&quot;&#10;    content_file = &quot;worker.js&quot;&#10;  }]&#10;&#10;  bindings = [&#10;    {&#10;      type = &quot;kv_namespace&quot;&#10;      name = &quot;MY_KV&quot;&#10;      namespace_id = var.kv_namespace_id&#10;    },&#10;    {&#10;      type = &quot;r2_bucket&quot;&#10;      name = &quot;MY_BUCKET&quot;&#10;      bucket_name = &quot;my-bucket&quot;&#10;    },&#10;    {&#10;      type = &quot;d1&quot;&#10;      name = &quot;DB&quot;&#10;      id = var.d1_database_id&#10;    },&#10;    {&#10;      type = &quot;service&quot;&#10;      name = &quot;AUTH_SERVICE&quot;&#10;      service = &quot;auth-worker&quot;&#10;    },&#10;    {&#10;      type = &quot;plain_text&quot;&#10;      name = &quot;ENVIRONMENT&quot;&#10;      text = &quot;production&quot;&#10;    },&#10;    {&#10;      type = &quot;secret_text&quot;&#10;      name = &quot;API_KEY&quot;&#10;      text = var.api_key&#10;    },&#10;    {&#10;      type = &quot;vpc_service&quot;&#10;      name = &quot;PRIVATE_API&quot;&#10;      service_id = var.vpc_service_id&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h2 id="cloudflare-api-libraries">Cloudflare API Libraries</h2>
<p>This example uses the <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> SDK which provides convenient access to the Cloudflare REST API from server-side JavaScript or TypeScript.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16218.md")
</div>
<h2 id="cloudflare-rest-api">Cloudflare REST API</h2>
<p>Open a terminal or create a shell script to upload a Worker and manage versions and deployments with curl. Workers scripts are JavaScript <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules">ES Modules</a>, but we also support <a href="/workers/languages/python/">Python Workers</a> and <a href="/workers/languages/rust/">Rust Workers</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/16217.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workers-esmodule-vs-python"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16221.md")
</div></div>
<h3 id="multipart-form-data-upload-api">multipart/form-data upload API</h3>
<p>This API uses <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST">multipart/form-data</a> to upload a Worker and will implicitly create a version and deployment. The above API is recommended for direct management of versions and deployments.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workers-vs-platforms"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16224.md")
</div></div>
<h3 id="python-workers">Python Workers</h3>
<p><a href="/workers/languages/python/">Python Workers</a> have their own special <code>text/x-python</code> content type and <code>python_workers</code> compatibility flag for uploading using the multipart/form-data API.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/workers/scripts/my-hello-world-script \&#10;  &#45;X PUT \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;F &#x27;metadata={&#10;        &quot;main_module&quot;: &quot;my-hello-world-script.py&quot;,&#10;        &quot;bindings&quot;: [&#10;          {&#10;            &quot;type&quot;: &quot;plain_text&quot;,&#10;            &quot;name&quot;: &quot;MESSAGE&quot;,&#10;            &quot;text&quot;: &quot;Hello World!&quot;&#10;          }&#10;        ],&#10;        &quot;compatibility_date&quot;: &quot;$today&quot;,&#10;        &quot;compatibility_flags&quot;: [&#10;          &quot;python_workers&quot;&#10;        ]&#10;      };type=application/json&#x27; \&#10;  &#45;F &#x27;my-hello-world-script.py=@-;filename=my-hello-world-script.py;type=text/x-python&#x27; &lt;&lt;EOF&#10;from workers import WorkerEntrypoint, Response&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(self.env.MESSAGE)&#10;EOF&#10;</code></pre>
<h2 id="considerations-with-durable-objects">Considerations with Durable Objects</h2>
<p><a href="/durable-objects/">Durable Object</a> migrations are applied with deployments. This means you can't bind to a Durable Object in a Version if a deployment doesn't exist i.e. migrations haven't been applied. For example, running this in Terraform will fail the first time the plan is applied:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_worker&quot; &quot;my_worker&quot; {&#10;  account_id = var.account_id&#10;  name = &quot;my-worker&quot;&#10;}&#10;&#10;resource &quot;cloudflare_worker_version&quot; &quot;my_worker_version&quot; {&#10;  account_id = var.account_id&#10;  worker_id = cloudflare_worker.my_worker.id&#10;  bindings = [&#10;    {&#10;      type = &quot;durable_object_namespace&quot;&#10;      name = &quot;my_durable_object&quot;&#10;      class_name = &quot;MyDurableObjectClass&quot;&#10;    }&#10;  ]&#10;  migrations = {&#10;    new_sqlite_classes = [&#10;      &quot;MyDurableObjectClass&quot;&#10;    ]&#10;  }&#10;  &#35; ...version props omitted for brevity&#10;}&#10;&#10;resource &quot;cloudflare_workers_deployment&quot; &quot;my_worker_deployment&quot; {&#10;  &#35; ...deployment props omitted for brevity&#10;}&#10;</code></pre>
<p>To make this succeed, you first have to comment out the <code>durable_object</code> binding block, apply the plan, uncomment it, comment out the <code>migrations</code> block, then apply again. This time the plan will succeed. This also applies to the API or SDKs. This is an example where it makes sense to just manage the <code>cloudflare_worker</code> and/or <code>cloudflare_workers_deployment</code> resources while using Wrangler for build and Version management.</p>
<h2 id="considerations-with-worker-versions">Considerations with Worker Versions</h2>
<h3 id="resource-immutability">Resource immutability</h3>
<p>Worker versions are immutable at the API level, meaning they cannot be updated after creation, only re-created with any desired changes. This means that meaningful changes to the <code>cloudflare_worker_version</code> Terraform resource will always trigger replacement. When the <code>cloudflare_worker_version</code> resource is replaced, a new version with the desired changes is created, but the previous version is not deleted. This ensures the Worker has a complete version history when managed via Terraform. In other words, versions are both immutable and append-only. When the parent <code>cloudflare_worker</code> resource is deleted, all existing versions associated with the Worker are also deleted.</p>
<h3 id="module-content">Module Content</h3>
<p>Worker version modules support two mutually exclusive ways to provide content:</p>
<ul>
<li><strong><code>content_file</code></strong> - Points to a local file</li>
<li><strong><code>content_base64</code></strong> - Inline base64-encoded content</li>
</ul>
<p>In both cases, changes to the underlying content are tracked using the computed <code>content_sha256</code> attribute. Specifying content using the <code>content_file</code> attribute is preferred in almost all cases, as it avoids storing the content itself in state. Module content may be quite large (up to tens of megabytes), and storing it in state will bloat the state file and negatively affect the performance of Terraform operations. The main use case for the <code>content_base64</code> attribute is importing the <code>cloudflare_worker_version</code> Terraform resource from the API, discussed below.</p>
<h3 id="import-behavior">Import Behavior</h3>
<p><strong>During import, Terraform always populates the <code>content_base64</code> attribute in state</strong>, regardless of the attribute used in your config.</p>
<pre tabindex="0"><code class="language-bash">terraform import cloudflare_worker_version.my_worker_version &lt;account_id&gt;/&lt;worker_id&gt;/&lt;version_id&gt;&#10;</code></pre>
<p>If your config uses <code>content_file</code>, there will be a mismatch after import (state uses <code>content_base64</code>, config uses <code>content_file</code>). This is expected.</p>
<p>Assuming the content of the local file referenced by <code>content_file</code> matches the imported content and their <code>content_sha256</code> values are the same, this will result in an in-place update of the <code>cloudflare_worker_version</code> Terraform resource. This should be an in-place update instead of a replacement because the underlying content is not changing (the <code>content_sha256</code> attribute is the same in both cases), and the resource does not need to be updated at the API level. The only thing that needs to be updated is Terraform state, which will switch from using <code>content_base64</code> to <code>content_file</code> after the update.</p>
<p>If Terraform instead wants to replace the resource, citing a difference in computed <code>content_sha256</code> values, then the content of the local file referenced by <code>content_file</code> does not match the imported content and the resource can't be cleanly imported without updating the local file to match the expected API value.</p>
<h3 id="examples">Examples</h3>
<p><strong>Using <code>content_file</code>:</strong></p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_worker_version&quot; &quot;content_file_example&quot; {&#10;  account_id  = var.account_id&#10;  worker_id   = cloudflare_worker.example.id&#10;  main_module = &quot;worker.js&quot;&#10;  modules = [{&#10;    name         = &quot;worker.js&quot;&#10;    content_type = &quot;application/javascript+module&quot;&#10;    content_file = &quot;build/worker.js&quot;&#10;  }]&#10;}&#10;</code></pre>
<p><strong>Using <code>content_base64</code>:</strong></p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_worker_version&quot; &quot;content_base64_example&quot; {&#10;  account_id  = var.account_id&#10;  worker_id   = cloudflare_worker.example.id&#10;  main_module = &quot;worker.js&quot;&#10;  modules = [{&#10;    name           = &quot;worker.js&quot;&#10;    content_type   = &quot;application/javascript+module&quot;&#10;    content_base64 = base64encode(&quot;export default { async fetch() { return new Response(&#x27;Hello world!&#x27;) } }&quot;)&#10;  }]&#10;}&#10;</code></pre>
