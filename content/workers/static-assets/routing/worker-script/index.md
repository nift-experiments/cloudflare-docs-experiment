<p>If you have both static assets and a Worker script configured, Cloudflare will first attempt to serve static assets if one matches the incoming request. You can read more about how we match assets in the <a href="/workers/static-assets/routing/advanced/html-handling/">HTML handling docs</a>.</p>
<p>If an appropriate static asset if not found, Cloudflare will invoke your Worker script.</p>
<p>This allows you to easily combine together these two features to create powerful applications (e.g. a <a href="/workers/static-assets/routing/full-stack-application/">full-stack application</a>, or a <a href="/workers/static-assets/routing/single-page-application/">Single Page Application (SPA)</a> or <a href="/workers/static-assets/routing/static-site-generation/">Static Site Generation (SSG) application</a> with an API).</p>
<h2 id="cloudflare-access-context">Cloudflare Access context</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17270.md")
</aside>
<h2 id="run-your-worker-script-first">Run your Worker script first</h2>
<p>You can configure the <a href="/workers/static-assets/binding/#run_worker_first"><code>assets.run_worker_first</code> setting</a> to control when your Worker script runs relative to static asset serving. This gives you more control over exactly how and when those assets are served and can be used to implement &quot;middleware&quot; for requests.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17269.md")
</aside>
<h3 id="run-worker-before-each-request">Run Worker before each request</h3>
<p>If you need to always run your Worker script before serving static assets (for example, you wish to log requests, perform some authentication checks, use <a href="/workers/runtime-apis/html-rewriter/">HTMLRewriter</a>, or otherwise transform assets before serving), set <code>run_worker_first</code> to <code>true</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17271.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17272.md")
</div>
<h3 id="run-worker-first-for-selective-paths">Run Worker first for selective paths</h3>
<p>You can also configure selective Worker-first routing using an array of route patterns, often paired with the <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control"><code>single-page-application</code> setting</a>. This allows you to run the Worker first only for specific routes while letting other requests follow the default asset-first behavior:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17273.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17274.md")
</div>
