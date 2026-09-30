---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/usage/static-assets/
  description: Serve static files alongside Dynamic Worker code.
  full_title: Static assets · Cloudflare Dynamic Workers docs
  head_html: <title>Static assets · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve static files alongside Dynamic Worker code."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/usage/static-assets/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/usage/static-assets/index.md"><meta property="og:title" content="Static assets · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve static files alongside Dynamic Worker code."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/usage/static-assets/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Dynamic Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dynamic-workers/usage/static-assets/#page","headline":"Static assets \u00b7 Cloudflare Dynamic Workers docs","description":"Serve static files alongside Dynamic Worker code.","url":"https://developers.cloudflare.com/dynamic-workers/usage/static-assets/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/usage/static-assets/
  schema: 1
---
<p>Dynamic Workers can serve static assets like HTML pages, JavaScript bundles, images, and other files alongside your Worker code. This is useful when you need a Dynamic Worker to serve a full-stack application.</p>
<p>Static assets for Dynamic Workers work differently from <a href="/workers/static-assets/">static assets in regular Workers</a>. Instead of uploading assets at deploy time, you provide them at runtime through the Worker Loader <code>get()</code> callback, sourcing them from R2, KV, or another storage backend.</p>
<h2 id="how-it-works">How it works</h2>
<p>There are three parts to setting up static assets for Dynamic Workers:</p>
<ol>
<li><strong>Store the assets</strong> — Upload static files to a KV namespace, keyed by project ID and pathname.</li>
<li><strong>Define an asset binding in the loader Worker</strong> — Create a class that handles requests for static files by reading them from KV and returning them with the correct headers.</li>
<li><strong>Pass the binding to the Dynamic Worker</strong> — The Dynamic Worker uses it to serve static files by calling <code>env.ASSETS.fetch(request)</code>.</li>
</ol>
<h2 id="store-the-static-assets">Store the static assets</h2>
<p>Static assets are stored in a KV namespace, separated by project ID so each project's files are isolated from each other:</p>
<pre tabindex="0"><code>project/{projectId}/assets/index.html      →  file content&#10;project/{projectId}/assets/app.js          →  file content&#10;project/{projectId}/manifest               →  asset manifest&#10;</code></pre>
<p>When a user deploys their project through your platform's upload API, store each file in KV under its pathname:</p>
<pre tabindex="0"><code class="language-ts">await env.KV_ASSETS.put(`project/${projectId}/assets${pathname}`, fileContent);&#10;</code></pre>
<p>You also need to store a manifest, a mapping that tells the asset handler which files exist and what their content types are. Use <code>buildAssetManifest()</code> from <code>@cloudflare/worker-bundler</code> to generate it from your assets:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8435.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8434.md")
</aside>
<h2 id="add-bindings-to-the-loader-worker">Add bindings to the loader Worker</h2>
<p>Grant the loader Worker access to the KV namespace where you stored the assets:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8436.md")
</div>
<h2 id="define-the-asset-binding">Define the asset binding</h2>
<p>Create a class in the loader Worker that extends <code>WorkerEntrypoint</code> and define a <code>fetch()</code> method. <code>WorkerEntrypoint</code> makes this method callable from the Dynamic Worker using RPC. When the Dynamic Worker calls <code>env.ASSETS.fetch(request)</code>, it runs this method in the loader Worker, where the KV binding and your asset-serving logic live.</p>
<p>The class takes a <code>projectId</code> prop so it knows which project's assets to look up. When <code>fetch()</code> is called, it:</p>
<ol>
<li>Loads the project's asset manifest from KV.</li>
<li>Resolves the request pathname to a file.</li>
<li>Fetches the file content from KV.</li>
<li>Returns a <code>Response</code> with the correct <code>Content-Type</code> header.</li>
</ol>
<h3 id="use-cloudflare-worker-bundler-to-handle-static-asset-serving">Use <code>@cloudflare/worker-bundler</code> to handle static asset serving</h3>
<p>Instead of writing your own logic to match request paths to files, detect content types, and set cache headers, use the <code>@cloudflare/worker-bundler</code> package to handle static asset serving. In your <code>fetch()</code> method, pass <code>handleAssetRequest()</code> two things:</p>
<ul>
<li>A <strong>manifest</strong>, the path-to-content-type mapping you stored in KV during upload, built with <code>buildAssetManifest()</code>. This tells <code>handleAssetRequest()</code> which files exist and what their content types are.</li>
<li>A <strong>storage object</strong>, tells <code>handleAssetRequest()</code> how to read files from your KV namespace. It has one method, <code>get(pathname)</code>, which reads and returns the content for a given file path.</li>
</ul>
<p><code>handleAssetRequest()</code> serves the file if it finds a match in the manifest, with the correct headers for content type and caching.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8437.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8433.md")
</aside>
<p>Once <code>AssetBinding</code> is exported, it becomes available on <code>ctx.exports</code> in the loader Worker's <code>fetch()</code> handler. <code>ctx</code> is the handler's third parameter, after <code>request</code> and <code>env</code>. This is how you pass it to the Dynamic Worker in the next step.</p>
<h2 id="pass-the-asset-binding-to-the-dynamic-worker">Pass the asset binding to the Dynamic Worker</h2>
<p>When you call <code>get()</code> to create the Dynamic Worker, include the <code>AssetBinding</code> in the <code>env</code> object so the Dynamic Worker can use it to serve static files. To reference the <code>AssetBinding</code> class you defined in the previous step, use <code>ctx.exports.AssetBinding()</code> and pass the <code>projectId</code> as a prop so it knows which project's assets to serve. This works the same way as custom bindings — <code>props</code> is how you pass information to the class, and the class reads it at <code>this.ctx.props</code> when it runs.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8438.md")
</div>
<p>The Dynamic Worker sees <code>ASSETS</code> as a binding and can call <code>env.ASSETS.fetch(request)</code> because that is the method you defined on <code>AssetBinding</code>. When the Dynamic Worker calls that method, it runs in the loader Worker, where your <code>AssetBinding</code> class reads the manifest and file content from KV.</p>
<h2 id="use-the-asset-binding-in-the-dynamic-worker">Use the asset binding in the Dynamic Worker</h2>
<p>From the Dynamic Worker's perspective, <code>env.ASSETS</code> works like any other binding. The user writes their server code and calls <code>env.ASSETS.fetch()</code> to serve static files:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8439.md")
</div>
<p>When the Dynamic Worker calls <code>env.ASSETS.fetch(request)</code>, the call goes through RPC to the loader Worker's <code>AssetBinding</code>, which looks up the file in the manifest and reads it from KV. The Dynamic Worker does not need to handle any of this — it calls <code>env.ASSETS.fetch(request)</code> and gets back the file with the correct headers, ready to return to the client.</p>
