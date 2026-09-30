<p>You can upload static assets (HTML, CSS, images and other files) as part of your Worker, and Cloudflare will handle caching and serving them to web browsers.</p>
<p><strong>Start from CLI</strong> - Scaffold a React SPA with an API Worker, and use the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-react-app --framework=react</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-react-app --framework=react" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-react-app --framework=react</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-react-app --framework=react" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-react-app --framework=react</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-react-app --framework=react" aria-label="Copy to clipboard">Copy</button></div></div>
---
<p><strong>Or just deploy to Cloudflare</strong></p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create/deploy-to-workers&amp;repository=https://github.com/cloudflare/templates/tree/main/vite-react-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Learn more about supported frameworks on Workers.</p>
<p><a class="nb-card nb-link-card" href="/workers/framework-guides/"><h3 id="card-supported-frameworks-workers-framework-guides">Supported frameworks</h3><p>Start building on Workers with our framework guides.</p></a></p>
<h3 id="how-it-works">How it works</h3>
<p>When you deploy your project, Cloudflare deploys both your Worker code and your static assets in a single operation. This deployment operates as a tightly integrated &quot;unit&quot; running across Cloudflare's network, combining static file hosting, custom logic, and global caching.</p>
<p>The <strong>assets directory</strong> specified in your <a href="/workers/wrangler/configuration/#assets">Wrangler configuration file</a> is central to this design. During deployment, Wrangler automatically uploads the files from this directory to Cloudflare's infrastructure. Once deployed, requests for these assets are routed efficiently to locations closest to your users.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16089.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16088.md")
</aside>
<p>By adding an <a href="/workers/static-assets/binding/#binding"><strong>assets binding</strong></a>, you can directly fetch and serve assets within your Worker code.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16092.md")
</div></div>
<h3 id="routing-behavior">Routing behavior</h3>
<p>By default, if a requested URL matches a file in the static assets directory, that file will be served — without invoking Worker code. If no matching asset is found and a Worker script is present, the request will be processed by the Worker. The Worker can return a response or choose to defer again to static assets by using the <a href="/workers/static-assets/binding/">assets binding</a> (e.g. <code>env.ASSETS.fetch(request)</code>). If no Worker script is present, a <code>404 Not Found</code> response is returned.</p>
<p>The default behavior for requests which don't match a static asset can be changed by setting the <a href="/workers/wrangler/configuration/#assets"><code>not_found_handling</code> option under <code>assets</code></a> in your Wrangler configuration file:</p>
<ul>
<li><a href="/workers/static-assets/routing/single-page-application/"><code>not_found_handling = &quot;single-page-application&quot;</code></a>: Sets your application to return a <code>200 OK</code> response with <code>index.html</code> for requests which don't match a static asset. Use this if you have a Single Page Application. We recommend pairing this with selective routing using <code>run_worker_first</code> for <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control">advanced routing control</a>.</li>
<li><a href="/workers/static-assets/routing/static-site-generation/#custom-404-pages"><code>not_found_handling = &quot;404-page&quot;</code></a>: Sets your application to return a <code>404 Not Found</code> response with the nearest <code>404.html</code> for requests which don't match a static asset.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16093.md")
</div>
<p>If you want the Worker code to execute before serving assets, you can use the <code>run_worker_first</code> option. This can be set to <code>true</code> to invoke the Worker script for all requests, or configured as an array of route patterns for selective Worker-script-first routing:</p>
<p><strong>Invoking your Worker script on specific paths:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16094.md")
</div>
<p>For a more advanced pattern, refer to <a href="/workers/examples/spa-shell/">SPA shell with bootstrap data</a>, which uses HTMLRewriter to inject prefetched API data into the HTML stream.</p>
<p><a class="nb-card nb-link-card" href="/workers/static-assets/routing/"><h3 id="card-routing-options-workers-static-assets-routing">Routing options</h3><p>Learn more about how you can customize routing behavior.</p></a></p>
<h3 id="caching-behavior">Caching behavior</h3>
<p>Cloudflare provides automatic caching for static assets across its network, ensuring fast delivery to users worldwide. When a static asset is requested, it is automatically cached for future requests.</p>
<ul>
<li>
<p><strong>First Request:</strong> When an asset is requested for the first time, it is fetched from storage and cached at the nearest Cloudflare location.</p>
</li>
<li>
<p><strong>Subsequent Requests:</strong> If a request for the same asset reaches a data center that does not have it cached, Cloudflare's <a href="/cache/how-to/tiered-cache/">tiered caching system</a> allows it to be retrieved from a nearby cache rather than going back to storage. This improves cache hit ratio, reduces latency, and reduces unnecessary origin fetches.</p>
</li>
</ul>
<h2 id="try-it-out">Try it out</h2>
<p><a class="nb-card nb-link-card" href="/workers/vite-plugin/tutorial/"><h3 id="card-vite-react-spa-tutorial-workers-vite-plugin-tutorial">Vite + React SPA tutorial</h3><p>Learn how to build and deploy a full-stack Single Page Application with static assets and API routes.</p></a></p>
<h2 id="learn-more">Learn more</h2>
<p><a class="nb-card nb-link-card" href="/workers/framework-guides/"><h3 id="card-supported-frameworks-workers-framework-guides-1">Supported frameworks</h3><p>Start building on Workers with our framework guides.</p></a></p>
<p><a class="nb-card nb-link-card" href="/workers/static-assets/billing-and-limitations/"><h3 id="card-billing-and-limitations-workers-static-assets-billing-and-limitations">Billing and limitations</h3><p>Learn more about how requests are billed, current limitations, and troubleshooting.</p></a></p>
