<p>Configuring a Worker with assets requires specifying a <a href="/workers/static-assets/binding/#directory">directory</a> and, optionally, an <a href="/workers/static-assets/binding/">assets binding</a>, in your Worker's Wrangler file. The <a href="/workers/static-assets/binding/">assets binding</a> allows you to dynamically fetch assets from within your Worker script (e.g. <code>env.ASSETS.fetch()</code>), similarly to how you might with a make a <code>fetch()</code> call with a <a href="/workers/runtime-apis/bindings/service-bindings/http/">Service binding</a>.</p>
<p>Only one collection of static assets can be configured in each Worker.</p>
<h2 id="directory"><code>directory</code></h2>
<p>The folder of static assets to be served. For many frameworks, this is the <code>./public/</code>, <code>./dist/</code>, or <code>./build/</code> folder.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16110.md")
</div>
<h3 id="ignoring-assets">Ignoring assets</h3>
<p>Sometime there are files in the asset directory that should not be uploaded.</p>
<p>In this case, create a <code>.assetsignore</code> file in the root of the assets directory.
This file takes the same format as <code>.gitignore</code>.</p>
<p>Wrangler will not upload asset files that match lines in this file.</p>
<p><strong>Example</strong></p>
<p>You are migrating from a Pages project where the assets directory is <code>dist</code>.
You do not want to upload the server-side Worker code nor Pages configuration files as public client-side assets.
Add the following <code>.assetsignore</code> file:</p>
<pre><code class="language-txt">_worker.js&#10;_redirects&#10;_headers&#10;</code></pre>
<p>Now Wrangler will not upload these files as client-side assets when deploying the Worker.</p>
<h2 id="run-worker-first"><code>run_worker_first</code></h2>
<p>Controls whether to invoke the Worker script regardless of a request which would have otherwise matched an asset. <code>run_worker_first = false</code> (default) will serve any static asset matching a request, while <code>run_worker_first = true</code> will unconditionally <a href="/workers/static-assets/routing/worker-script/#run-your-worker-script-first">invoke your Worker script</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16111.md")
</div>
<p>You can also specify <code>run_worker_first</code> as an array of route patterns to selectively run the Worker script first only for specific routes.</p>
<p>The array supports glob patterns with <code>*</code> for deep matching and negative patterns with <code>!</code> prefix.</p>
<p>Negative patterns have precedence over non-negative patterns. The Worker will run first when a non-negative pattern matches and none of the negative pattern matches.</p>
<p>The order in which the patterns are listed is not significant.</p>
<p><code>run_worker_first</code> is often paired with the <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control"><code>not_found_handling = &quot;single-page-application&quot;</code> setting</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16112.md")
</div>
<p>In this configuration, requests to <code>/api/*</code> routes will invoke the Worker script first, except for <code>/api/docs/*</code> which will follow the default asset-first routing behavior.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16109.md")
</aside>
<p>Common uses for <code>run_worker_first</code> include authentication checks, A/B testing, and <a href="/workers/examples/spa-shell/">injecting bootstrap data into your SPA shell</a>.</p>
<h2 id="binding"><code>binding</code></h2>
<p>Configuring the optional <a href="/workers/runtime-apis/bindings">binding</a> gives you access to the collection of assets from within your Worker script.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16113.md")
</div>
<p>In the example above, assets would be available through <code>env.ASSETS</code>.</p>
<h3 id="runtime-api-reference">Runtime API Reference</h3>
<h4 id="fetch"><code>fetch()</code></h4>
<p><strong>Parameters</strong></p>
<ul>
<li><code>request: Request | URL | string</code> Pass a <a href="/workers/runtime-apis/request/">Request object</a>, URL object, or URL string. Requests made through this method have <code>html_handling</code> and <code>not_found_handling</code> configuration applied to them.</li>
</ul>
<p><strong>Response</strong></p>
<ul>
<li><code>Promise&lt;Response&gt;</code> Returns a static asset response for the given request.</li>
</ul>
<p><strong>Example</strong></p>
<p>Your dynamic code can make new, or forward incoming requests to your project's static assets using the assets binding. For example, <code>env.ASSETS.fetch(request)</code>, <code>env.ASSETS.fetch(new URL('https://assets.local/my-file'))</code> or <code>env.ASSETS.fetch('https://assets.local/my-file')</code>. The hostname used in the URL (for example, <code>assets.local</code>) is not meaningful — any valid hostname will work. Only the URL pathname is used to match assets.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16108.md")
</aside>
<p>Take the following example that configures a Worker script to return a response under all requests headed for <code>/api/</code>. Otherwise, the Worker script will pass the incoming request through to the asset binding. In this case, because a Worker script is only invoked when the requested route has not matched any static assets, this will always evaluate <a href="/workers/static-assets/#routing-behavior"><code>not_found_handling</code></a> behavior.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16116.md")
</div></div>
<h2 id="routing-configuration">Routing configuration</h2>
<p>For the various static asset routing configuration options, refer to <a href="/workers/static-assets/routing/">Routing</a>.</p>
<h2 id="smart-placement">Smart Placement</h2>
<p><a href="/workers/configuration/placement/">Smart Placement</a> can be used to place a Worker's code close to your back-end infrastructure. Smart Placement will only have an effect if you specified a <code>main</code>, pointing to your Worker code.</p>
<h3 id="smart-placement-with-worker-code-first">Smart Placement with Worker Code First</h3>
<p>If you desire to run your <a href="/workers/static-assets/routing/worker-script/#run-your-worker-script-first">Worker code ahead of assets</a> by setting <code>run_worker_first=true</code>, all requests must first travel to your Smart-Placed Worker. As a result, you may experience increased latency for asset requests.</p>
<p>Use Smart Placement with <code>run_worker_first=true</code> when you need to integrate with other backend services, authenticate requests before serving any assets, or if you want to make modifications to your assets before serving them.</p>
<p>If you want some assets served as quickly as possible to the user, but others to be served behind a smart-placed Worker, considering splitting your app into multiple Workers and <a href="/workers/configuration/placement/#multiple-workers">using service bindings to connect them</a>.</p>
<h3 id="smart-placement-with-assets-first">Smart Placement with Assets First</h3>
<p>Enabling Smart Placement with <code>run_worker_first=false</code> (or not specifying it) lets you serve assets from as close as possible to your users, but moves your Worker logic to run most efficiently (such as near a database).</p>
<p>Use Smart Placement with <code>run_worker_first=false</code> (or not specifying it) when prioritizing fast asset delivery.</p>
<p>This will not impact the <a href="/workers/static-assets/#routing-behavior">default routing behavior</a>.</p>
