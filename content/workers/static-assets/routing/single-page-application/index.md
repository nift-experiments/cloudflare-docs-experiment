<p>Single Page Applications (SPAs) are web applications which are client-side rendered (CSR). They are often built with a framework such as <a href="/workers/framework-guides/web-apps/react/">React</a>, <a href="/workers/framework-guides/web-apps/vue/">Vue</a> or <a href="/workers/framework-guides/web-apps/sveltekit/">Svelte</a>. The build process of these frameworks will produce a single <code>/index.html</code> file and accompanying client-side resources (e.g. JavaScript bundles, CSS stylesheets, images, fonts, etc.). Typically, data is fetched by the client from an API with client-side requests.</p>
<p>When you configure <code>single-page-application</code> mode, Cloudflare provides default routing behavior that automatically serves your <code>/index.html</code> file for navigation requests (those with <code>Sec-Fetch-Mode: navigate</code> headers) which don't match any other asset. For more control over which paths invoke your Worker script, you can use <a href="#advanced-routing-control">advanced routing control</a>.</p>
<h2 id="configuration">Configuration</h2>
<p>In order to deploy a Single Page Application to Workers, you must configure the <code>assets.directory</code> and <code>assets.not_found_handling</code> options in your <a href="/workers/wrangler/configuration/#assets">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17282.md")
</div>
<p>Configuring <code>assets.not_found_handling</code> to <code>single-page-application</code> overrides the default serving behavior of Workers for static assets. When an incoming request does not match a file in the <code>assets.directory</code>, Workers will serve the contents of the <code>/index.html</code> file with a <code>200 OK</code> status.</p>
<h3 id="navigation-requests">Navigation requests</h3>
<p>If you have a Worker script (<code>main</code>), have configured <code>assets.not_found_handling</code>, and use the <a href="/workers/configuration/compatibility-flags/#navigation-requests-prefer-asset-serving"><code>assets_navigation_prefers_asset_serving</code> compatibility flag</a> (or set a compatibility date of <code>2025-04-01</code> or greater), <em>navigation requests</em> will not invoke the Worker script. A <em>navigation request</em> is a request made with the <code>Sec-Fetch-Mode: navigate</code> header, which browsers automatically attach when navigating to a page. This reduces billable invocations of your Worker script, and is particularly useful for client-heavy applications which would otherwise invoke your Worker script very frequently and unnecessarily.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17281.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17280.md")
</aside>
<h4 id="client-side-callbacks">Client-side callbacks</h4>
<p>In some cases, you might need to pass a value from a navigation request to your Worker script. For example, if you are acting as an OAuth callback, you might expect to see requests made to some route such as <code>/oauth/callback?code=...</code>. With the <code>assets_navigation_prefers_asset_serving</code> flag, your HTML assets will be server, rather than your Worker script. In this case, we recommend, either as part of your client application for this appropriate route, or with a slimmed-down endpoint-specific HTML file, passing the value to the server with client-side JavaScript.</p>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;title&gt;OAuth callback&lt;/title&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;		&lt;p&gt;Loading...&lt;/p&gt;&#10;		&lt;script&gt;&#10;			(async () =&gt; {&#10;				const response = await fetch(&quot;/api/oauth/callback&quot; + window.location.search);&#10;				if (response.ok) {&#10;					window.location.href = &#x27;/&#x27;;&#10;				} else {&#10;					document.querySelector(&#x27;p&#x27;).textContent = &#x27;Error: &#x27; + (await response.json()).error;&#10;				}&#10;			})();&#10;		&lt;/script&gt;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17283.md")
</div>
<h2 id="advanced-routing-control">Advanced routing control</h2>
<p>For more explicit control over SPA routing behavior, you can use <code>run_worker_first</code> with an array of route patterns. This approach disables the automatic <code>Sec-Fetch-Mode: navigate</code> detection and gives you explicit control over which requests should be handled by your Worker script vs served as static assets.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17279.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17284.md")
</div>
<p>This configuration provides explicit routing control without relying on browser navigation headers, making it ideal for complex SPAs that need fine-grained routing behavior. Your Worker script can then handle the matched routes and (optionally using <a href="/workers/static-assets/binding/#binding">the assets binding</a>) and serve dynamic content.</p>
<p><strong>For example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17285.md")
</div>
<p>You can also use <code>run_worker_first</code> to inject data into your SPA shell before it reaches the browser. For a full example using HTMLRewriter to prefetch API data and embed it in the HTML stream, refer to <a href="/workers/examples/spa-shell/">SPA shell with bootstrap data</a>.</p>
<h2 id="local-development">Local Development</h2>
<p>If you are using a Vite-powered SPA framework, you might be interested in using our <a href="/workers/vite-plugin/">Vite plugin</a> which offers a Vite-native developer experience.</p>
<h3 id="reference">Reference</h3>
<p>In most cases, configuring <code>assets.not_found_handling</code> to <code>single-page-application</code> will provide the desired behavior. If you are building your own framework, or have specialized needs, the following diagram can provide insight into exactly how the routing decisions are made.</p>
<details>
<summary>Full routing decision diagram</summary>
<pre class="mermaid">&#10;<p>{`flowchart&#10;Request@{ shape: stadium, label: &quot;Incoming request&quot; }&#10;Request--&gt;RunWorkerFirst&#10;RunWorkerFirst@{ shape: diamond, label: &quot;Run Worker script first?&quot; }&#10;RunWorkerFirst--&gt;|Request matches run_worker_first path|WorkerScriptInvoked&#10;RunWorkerFirst--&gt;|Request matches run_worker_first negative path|AssetServing&#10;RunWorkerFirst--&gt;|No matches|RequestMatchesAsset&#10;RequestMatchesAsset@{ shape: diamond, label: &quot;Request matches asset?&quot; }&#10;RequestMatchesAsset--&gt;|Yes|AssetServing&#10;RequestMatchesAsset--&gt;|No|WorkerScriptPresent&#10;WorkerScriptPresent@{ shape: diamond, label: &quot;Worker script present?&quot; }&#10;WorkerScriptPresent--&gt;|No|AssetServing&#10;WorkerScriptPresent--&gt;|Yes|RequestNavigation&#10;RequestNavigation@{ shape: diamond, label: &quot;Request is navigation request?&quot; }&#10;RequestNavigation--&gt;|No|WorkerScriptInvoked&#10;WorkerScriptInvoked@{ shape: rect, label: &quot;Worker script invoked&quot; }&#10;WorkerScriptInvoked-.-&gt;|Asset binding|AssetServing&#10;RequestNavigation--&gt;|Yes|AssetServing</p>&#10;<pre><code>subgraph Asset serving&#10;	AssetServing@{ shape: diamond, label: &quot;Request matches asset?&quot; }&#10;	AssetServing--&gt;|Yes|AssetServed&#10;	AssetServed@{ shape: stadium, label: &quot;**200 OK**&lt;br /&gt;asset served&quot; }&#10;	AssetServing--&gt;|No|NotFoundHandling&#10;&#10;	subgraph single-page-application&#10;		NotFoundHandling@{ shape: rect, label: &quot;Request rewritten to /index.html&quot; }&#10;		NotFoundHandling--&gt;SPAExists&#10;		SPAExists@{ shape: diamond, label: &quot;HTML Page exists?&quot; }&#10;		SPAExists--&gt;|Yes|SPAServed&#10;		SPAExists--&gt;|No|Generic404PageServed&#10;		Generic404PageServed@{ shape: stadium, label: &quot;**404 Not Found**&lt;br /&gt;null-body response served&quot; }&#10;		SPAServed@{ shape: stadium, label: &quot;**200 OK**&lt;br /&gt;/index.html page served&quot; }&#10;	end&#10;&#10;end`}&#10;</code></pre>
</pre>
</details>
<p>Requests are only billable if a Worker script is invoked. From there, it is possible to serve assets using the assets binding (depicted as the dotted line in the diagram above).</p>
<p>Although unlikely to impact how a SPA is served, you can read more about how we match assets in the <a href="/workers/static-assets/routing/advanced/html-handling/">HTML handling docs</a>.</p>
