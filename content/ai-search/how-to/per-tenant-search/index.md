---
cp9:
  canonical: https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/
  description: Keep each tenant's data isolated in AI Search using a separate instance per tenant or a shared instance with metadata filtering.
  full_title: Multitenancy · Cloudflare AI Search docs
  head_html: <title>Multitenancy · Cloudflare AI Search docs</title><meta name="generator" content="Nift"><meta name="description" content="Keep each tenant&#x27;s data isolated in AI Search using a separate instance per tenant or a shared instance with metadata filtering."><link rel="canonical" href="https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/index.md"><meta property="og:title" content="Multitenancy · Cloudflare AI Search docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Keep each tenant&#x27;s data isolated in AI Search using a separate instance per tenant or a shared instance with metadata filtering."><meta property="og:url" content="https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Search"><meta name="algolia_product_filter" content="AI Search"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="AI Search"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/#page","headline":"Multitenancy \u00b7 Cloudflare AI Search docs","description":"Keep each tenant's data isolated in AI Search using a separate instance per tenant or a shared instance with metadata filtering.","url":"https://developers.cloudflare.com/ai-search/how-to/per-tenant-search/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-search/how-to/per-tenant-search/
  schema: 1
---
<p>In a multi-tenant application, each tenant must only ever see their own data. AI Search supports two ways to isolate search per tenant: give each tenant its own instance, or share one instance and filter by tenant at query time.</p>
<h2 id="choose-an-approach">Choose an approach</h2>
<table>
<thead>
<tr>
<th>Approach</th>
<th>How it isolates</th>
<th>Choose it when</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#option-1-one-instance-per-tenant">Instance per tenant</a> (recommended)</td>
<td>Each tenant gets a separate instance with its own storage and index</td>
<td>You need strong isolation, or you create and delete tenants at runtime</td>
</tr>
<tr>
<td><a href="#option-2-shared-instance-with-metadata-filtering-on-retrieval">Shared instance with filtering</a></td>
<td>One instance holds every tenant; a metadata filter scopes each query</td>
<td>You have many small tenants and want the simplest setup</td>
</tr>
</tbody>
</table>
<h2 id="prerequisites">Prerequisites</h2>
<p>Both approaches use a Cloudflare Worker. Create the project first, then follow the option you chose.</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3011.md")
</div></details>
<h2 id="create-a-worker-project">Create a Worker project</h2>
<p>Create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>tenant-search</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- tenant-search</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- tenant-search" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare tenant-search</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare tenant-search" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest tenant-search</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest tenant-search" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Go to your application directory:</p>
<pre tabindex="0"><code class="language-sh">cd tenant-search&#10;</code></pre>
<h2 id="option-1-one-instance-per-tenant">Option 1: One instance per tenant</h2>
<p>This is the <strong>recommended</strong> approach. Each tenant gets a separate instance with its own storage and search index, so one tenant can never retrieve another tenant's documents.</p>
<p>Create an isolated AI Search instance for each tenant at runtime using the <a href="/ai-search/concepts/namespaces/">namespace binding</a>.</p>
<div class="nb-interactive-component" data-cf-component="AiSearchNamespacesDiagram"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3010.md")
</aside>
<p>Add the namespace binding to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3012.md")
</div>
<p>The <code>remote</code> option lets <code>wrangler dev</code> proxy requests to your deployed instances, since AI Search does not run locally.</p>
<h3 id="built-in-storage">Built-in storage</h3>
<p>Each tenant's instance holds documents that you upload directly to it, with no external data source.</p>
<p>Update <code>src/index.ts</code>. This Worker identifies the tenant from a request header, then creates, populates, searches, and deletes that tenant's instance.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3013.md")
</div>
<p>Start a local development server:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Then onboard a tenant, upload a document to their instance, search it, and offboard. The <code>x-tenant-id</code> header scopes every request to that tenant's instance:</p>
<pre tabindex="0"><code class="language-sh">&#35; Create an isolated instance for tenant &quot;acme&quot;&#10;curl -X POST http://localhost:8787/onboard -H &quot;x-tenant-id: acme&quot;&#10;&#10;&#35; Upload a document to acme&#x27;s instance&#10;curl -X POST http://localhost:8787/upload -H &quot;x-tenant-id: acme&quot; -F &quot;file=@./handbook.pdf&quot;&#10;&#10;&#35; Search acme&#x27;s instance&#10;curl &quot;http://localhost:8787/search?q=vacation+policy&quot; -H &quot;x-tenant-id: acme&quot;&#10;&#10;&#35; Delete acme&#x27;s instance and all of its data&#10;curl -X DELETE http://localhost:8787/offboard -H &quot;x-tenant-id: acme&quot;&#10;</code></pre>
<p>AI Search indexes uploads asynchronously, so wait a moment after uploading before you search.</p>
<h3 id="r2">R2</h3>
<p>If your tenants' data already lives in <a href="/ai-search/configuration/data-source/r2/">R2</a>, back each tenant's instance with R2 instead of uploading documents to built-in storage. Change the <code>/onboard</code> route from the <a href="#built-in-storage">built-in storage</a> example to create an R2-backed instance. How you configure it depends on how the data is organized.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3009.md")
</aside>
<p><strong>A bucket per tenant:</strong> if each tenant's data is already in its own bucket, point the instance at that whole bucket:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.TENANTS.create({&#10;	id: `tenant-${tenantId}`,&#10;	type: &quot;r2&quot;,&#10;	source: `tenant-${tenantId}-bucket`,&#10;});&#10;</code></pre>
<p><strong>A shared bucket:</strong> if every tenant's data lives in one bucket, organized by folder:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/3014.md")&#10;&#10;&#10;</pre>
<p>Scope each instance to that tenant's folder with <a href="/ai-search/configuration/indexing/path-filtering/">path filtering</a>, so it only ever indexes and searches that tenant's objects:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.TENANTS.create({&#10;	id: `tenant-${tenantId}`,&#10;	type: &quot;r2&quot;,&#10;	source: &quot;my-bucket&quot;,&#10;	source_params: {&#10;		include_items: [`/customers/${tenantId}/**`],&#10;	},&#10;});&#10;</code></pre>
<p>With either layout, AI Search indexes each tenant's objects on the next <a href="/ai-search/configuration/indexing/syncing/">sync</a>. Add documents by writing them to R2 rather than uploading through the Worker, and keep the search and offboard routes from the built-in storage example: each instance only ever returns its own tenant's results, and deleting an instance removes its search index while leaving the R2 objects untouched.</p>
<p>To try it, run <code>npx wrangler dev</code> and use the same <code>onboard</code>, <code>search</code>, and <code>offboard</code> requests as <a href="#built-in-storage">built-in storage</a>. Skip the upload step, since AI Search indexes each tenant's objects directly from R2.</p>
<h2 id="option-2-shared-instance-with-metadata-filtering-on-retrieval">Option 2: Shared instance with metadata filtering on retrieval</h2>
<p>Use a single AI Search instance and organize content by tenant using folder paths. This approach works with both <a href="/ai-search/configuration/data-source/r2/">R2 buckets</a> and <a href="/ai-search/configuration/data-source/built-in-storage/">built-in storage</a>. Apply <a href="/ai-search/configuration/retrieval/filtering/">metadata filters</a> at query time so each tenant only retrieves their own documents.</p>
<p>This option searches an existing instance, so create one named <code>shared-instance</code> and add your content first. Refer to <a href="/ai-search/get-started/">Get started</a>.</p>
<p>Add the instance binding to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3015.md")
</div>
<p>Organize your content by tenant using unique folder paths:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/3016.md")&#10;&#10;&#10;</pre>
<p>Update <code>src/index.ts</code> to filter by the tenant's folder at query time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/3017.md")
</div>
<p>This example uses a <a href="/ai-search/configuration/retrieval/filtering/#starts-with-filter-for-folders">&quot;starts with&quot; filter</a> to match all files under the tenant's folder, including subfolders.</p>
<p>Start a local development server:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Send a request as each tenant. The Worker scopes the search to that tenant's folder, so the results never overlap:</p>
<pre tabindex="0"><code class="language-sh">curl http://localhost:8787/ -H &quot;x-tenant-id: customer-a&quot;&#10;curl http://localhost:8787/ -H &quot;x-tenant-id: customer-b&quot;&#10;</code></pre>
<h2 id="deploy">Deploy</h2>
<p>Log in with your Cloudflare account, then deploy your Worker to make it accessible on the Internet:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login&#10;npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-namespaces-ai-search-concepts-namespaces"><a href="/ai-search/concepts/namespaces/">Namespaces</a></h3><p>Group instances and manage them dynamically from a binding.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-filtering-ai-search-configuration-retrieval-filtering"><a href="/ai-search/configuration/retrieval/filtering/">Filtering</a></h3><p>Filter search results by metadata attributes at query time.</p></div>
