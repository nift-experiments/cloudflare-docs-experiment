<h1 id="changelog">Changelog</h1>

<h2 id="workers-for-platforms-dashboard-improvements"><a href="/changelog/post/2025-12-18-dashboard-improvements/">Workers for Platforms - Dashboard Improvements</a></h2>
<p><em>2025-12-18</em></p>
<p><a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> lets you build multi-tenant platforms on <a href="/workers/">Cloudflare Workers</a>, allowing your end users to deploy and run their own code on your platform. It's designed for anyone building an AI vibe coding platform, e-commerce platform, website builder, or any product that needs to securely execute user-generated code at scale.</p>
<p>Previously, setting up Workers for Platforms required using the API. Now, the Workers for Platforms UI supports namespace creation, dispatch worker templates, and tag management, making it easier for Workers for Platforms customers to build and manage multi-tenant platforms directly from the Cloudflare dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers-for-platforms/dashboard-improvements.png" alt="Workers for Platforms Dashboard Improvements" /></p>
<h4 id="2025-12-18-dashboard-improvements-key-improvements">Key improvements</h4>
<ul>
<li><strong>Namespace Management:</strong> You can now create and configure <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dispatch-namespace">dispatch namespaces</a> directly within the dashboard to start a new platform setup.</li>
<li><strong>Dispatch Worker Templates:</strong> New Dispatch Worker templates allow you to quickly define how traffic is routed to individual Workers within your namespace. Refer to the <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dynamic Dispatch documentation</a> for more examples.</li>
<li><strong>Tag Management:</strong> You can now set and update <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/tags/">tags</a> on User Workers, making it easier to group and manage your Workers.</li>
<li><strong>Binding Visibility:</strong> <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">Bindings</a> attached to User Workers are now visible directly within the User Worker view.</li>
<li><strong>Deploy Vibe Coding Platform in one-click:</strong> Deploy a <a href="/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">reference implementation</a> of an AI vibe coding platform directly from the dashboard. Powered by the Cloudflare's <a href="https://github.com/cloudflare/vibesdk">VibeSDK</a>, this starter kit integrates with Workers for Platforms to handle the deployment of AI-generated projects at scale.</li>
</ul>
<p>To get started, go to <strong>Workers for Platforms</strong> under <strong>Compute &amp; AI</strong> in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>


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


<h2 id="automate-worker-deployments-with-a-simplified-sdk-and-more-reliable-terraform-provider"><a href="/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/">Automate Worker deployments with a simplified SDK and more reliable Terraform provider</a></h2>
<p><em>2025-06-19</em></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-simplified-worker-deployments-with-our-sdks">Simplified Worker Deployments with our SDKs</h4>
<p>We've simplified the programmatic deployment of Workers via our <a href="/fundamentals/api/reference/sdks/">Cloudflare SDKs</a>. This update abstracts away the low-level complexities of the <code>multipart/form-data</code> upload process, allowing you to focus on your code while we handle the deployment mechanics.</p>
<p>This new interface is available in:</p>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (4.4.1)</li>
<li><a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (4.3.1)</li>
</ul>
<p>For complete examples, see our guide on <a href="/workers/platform/infrastructure-as-code">programmatic Worker deployments</a>.</p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-the-old-way-manual-api-calls">The Old way: Manual API calls</h4>
<p>Previously, deploying a Worker programmatically required manually constructing a <code>multipart/form-data</code> HTTP request, packaging your code and a separate <code>metadata.json</code> file. This was more complicated and verbose, and prone to formatting errors.</p>
<p>For example, here's how you would upload a Worker script previously with cURL:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/workers/scripts/my-hello-world-script \&#10;  &#45;X PUT \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;F &#x27;metadata={&#10;        &quot;main_module&quot;: &quot;my-hello-world-script.mjs&quot;,&#10;        &quot;bindings&quot;: [&#10;          {&#10;            &quot;type&quot;: &quot;plain_text&quot;,&#10;            &quot;name&quot;: &quot;MESSAGE&quot;,&#10;            &quot;text&quot;: &quot;Hello World!&quot;&#10;          }&#10;        ],&#10;        &quot;compatibility_date&quot;: &quot;$today&quot;&#10;      };type=application/json&#x27; \&#10;  &#45;F &#x27;my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module&#x27; &lt;&lt;EOF&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return new Response(env.MESSAGE, { status: 200 });&#10;  }&#10;};&#10;EOF&#10;</code></pre>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-after-sdk-interface">After: SDK interface</h4>
<p>With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.</p>
<p>This approach allows you to specify metadata like <code>main_module</code>, <code>bindings</code>, and <code>compatibility_date</code> as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.</p>
<p>Here's how you can now programmatically deploy a Worker via the <a href="https://github.com/cloudflare/cloudflare-typescript"><code>cloudflare-typescript</code> SDK</a></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17777.md")</div>
<p>View the complete example here: <a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts">https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts</a></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-terraform-provider-improvements">Terraform provider improvements</h4>
<p>We've also made several fixes and enhancements to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform provider</a>:</p>
<ul>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource in Terraform, which previously was producing a diff even when there were no changes. Now, your <code>terraform plan</code> outputs will be cleaner and more reliable.</li>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace"><code>cloudflare_workers_for_platforms_dispatch_namespace</code></a>, where the provider would attempt to recreate the namespace on a <code>terraform apply</code>. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.</li>
<li>The <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route"><code>cloudflare_workers_route</code></a> resource now allows for the <code>script</code> property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes <a href="/workers/configuration/routing/routes">docs</a>). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.</li>
<li>Using <code>primary_location_hint</code> in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database"><code>cloudflare_d1_database</code></a> resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.</li>
</ul>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-api-improvements">API improvements</h4>
<p>We've also properly documented the <a href="/api/resources/workers/subresources/scripts/subresources/script_and_version_settings">Workers Script And Version Settings</a> in our public OpenAPI spec and SDKs.</p>


<h2 id="fixed-and-documented-workers-routes-and-secrets-api"><a href="/changelog/post/2025-04-15-workers-api-fixes/">Fixed and documented Workers Routes and Secrets API</a></h2>
<p><em>2025-04-15</em></p>
<h4 id="2025-04-15-workers-api-fixes-workers-routes-api">Workers Routes API</h4>
<p>Previously, a request to the Workers <a href="/api/resources/workers/subresources/routes/methods/create/">Create Route API</a> always returned <code>null</code> for &quot;script&quot; and an empty string for &quot;pattern&quot; even if the request was successful.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/$CF_ACCOUNT_ID/workers/routes \&#10;&#45;X PUT \&#10;&#45;H &quot;Authorization: Bearer $CF_API_TOKEN&quot; \&#10;&#45;H &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{ &quot;pattern&quot;: &quot;example.com/*&quot;, &quot;script&quot;: &quot;hello-world-script&quot; }&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;bf153a27ba2b464bb9f04dcf75de1ef9&quot;,&#10;		&quot;pattern&quot;: &quot;&quot;,&#10;		&quot;script&quot;: null,&#10;		&quot;request_limit_fail_open&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>Now, it properly returns all values!</p>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;bf153a27ba2b464bb9f04dcf75de1ef9&quot;,&#10;		&quot;pattern&quot;: &quot;example.com/*&quot;,&#10;		&quot;script&quot;: &quot;hello-world-script&quot;,&#10;		&quot;request_limit_fail_open&quot;: false&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h4 id="2025-04-15-workers-api-fixes-workers-secrets-api">Workers Secrets API</h4>
<p>The <a href="/api/resources/workers/subresources/scripts/subresources/secrets/">Workers</a> and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/subresources/secrets/">Workers for Platforms</a> secrets APIs are now properly documented in the Cloudflare OpenAPI docs. Previously, these endpoints were not publicly documented, leaving users confused on how to directly manage their secrets via the API. Now, you can find the proper endpoints in our public documentation, as well as in our API Library SDKs such as <a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (&gt;4.2.0) and <a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (&gt;4.1.0).</p>
<p>Note the <code>cloudflare_workers_secret</code> and <code>cloudflare_workers_for_platforms_script_secret</code> <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform resources</a> are being removed in a future release. This resource is not recommended for managing secrets. Users should instead use the:</p>
<ul>
<li><a href="/api/resources/secrets_store/">Secrets Store</a> with the &quot;Secrets Store Secret&quot; binding on Workers and Workers for Platforms Script Upload</li>
<li>&quot;Secret Text&quot; Binding on <a href="/api/resources/workers/subresources/scripts/methods/update/">Workers Script Upload</a> and <a href="/api/resources/workers_for_platforms/subresources/dispatch/subresources/namespaces/subresources/scripts/methods/update/">Workers for Platforms Script Upload</a></li>
<li>Workers (and WFP) Secrets API</li>
</ul>


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


<h2 id="workers-for-platforms-instant-dispatch-for-newly-created-user-workers"><a href="/changelog/post/2025-02-20-synchronous-uploads/">Workers for Platforms - Instant dispatch for newly created User Workers</a></h2>
<p><em>2025-02-20T17:00:00+00:00</em></p>
<p><a href="https://developers.cloudflare.com/cloudflare-for-platforms/">Workers for Platforms</a> is an architecture wherein a centralized <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dispatch Worker</a> processes incoming requests and routes them to isolated sub-Workers, called <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers">User Workers</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers-for-platforms/wfp-request.png" alt="Workers for Platforms Requests" /></p>
<p>Previously, when a new User Worker was uploaded, there was a short delay before it became available for dispatch. This meant that even though an API request could return a 200 OK response, the script might not yet be ready to handle requests, causing unexpected failures for platforms that immediately dispatch to new Workers.</p>
<p><strong>With this update, first-time uploads of User Workers are now deployed synchronously</strong>. A 200 OK response guarantees the script is fully provisioned and ready to handle traffic immediately, ensuring more predictable deployments and reducing errors.</p>


<h2 id="workers-for-platforms-now-supports-static-assets"><a href="/changelog/post/2025-01-31-workers-platforms-static-assets/">Workers for Platforms now supports Static Assets</a></h2>
<p><em>2025-01-31</em></p>
<p>Workers for Platforms customers can now attach static assets (HTML, CSS, JavaScript, images) directly to User Workers, removing the need to host separate infrastructure to serve the assets.</p>
<p>This allows your platform to serve entire front-end applications from Cloudflare's global edge, utilizing caching for fast load times, while supporting dynamic logic within the same Worker. Cloudflare automatically scales its infrastructure to handle high traffic volumes, enabling you to focus on building features without managing servers.</p>
<h4 id="2025-01-31-workers-platforms-static-assets-what-you-can-build">What you can build</h4>
<p><strong>Static Sites:</strong> Host and serve HTML, CSS, JavaScript, and media files directly from Cloudflare's network, ensuring fast loading times worldwide. This is ideal for blogs, landing pages, and documentation sites because static assets can be efficiently cached and delivered closer to the user, reducing latency and enhancing the overall user experience.</p>
<p><strong>Full-Stack Applications:</strong> Combine asset hosting with Cloudflare Workers to power dynamic, interactive applications. If you're an e-commerce platform, you can serve your customers' product pages and run inventory checks from within the same Worker.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17821.md")</div>
<p><strong>Get Started:</strong>
Upload static assets using the Workers for Platforms API or Wrangler. For more information, visit our <a href="https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/">Workers for Platforms documentation.</a></p>



