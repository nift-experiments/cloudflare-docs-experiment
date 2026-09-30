<p class="article-summary">Query a D1 database from a SvelteKit application.</p>
<p><a href="https://kit.svelte.dev/">SvelteKit</a> is a full-stack framework that combines the Svelte front-end framework with Vite for server-side capabilities and rendering. You can query D1 from SvelteKit by configuring a <a href="https://kit.svelte.dev/docs/routing#server">server endpoint</a> with a binding to your D1 database(s).</p>
<p>To set up a new SvelteKit site on Cloudflare Pages that can query D1:</p>
<ol>
<li><strong>Refer to <a href="/pages/framework-guides/deploy-a-svelte-kit-site/">the SvelteKit guide</a> and Svelte's <a href="https://kit.svelte.dev/docs/adapter-cloudflare">Cloudflare adapter</a></strong>.</li>
<li>Install the Cloudflare adapter within your SvelteKit project: <code>npm i -D @sveltejs/adapter-cloudflare</code>.</li>
<li>Bind a D1 database <a href="/pages/functions/bindings/#d1-databases">to your Pages Function</a>.</li>
<li>Pass the <code>--d1 BINDING_NAME=DATABASE_ID</code> flag to <code>wrangler dev</code> when developing locally. <code>BINDING_NAME</code> should match what call in your code, and <code>DATABASE_ID</code> should match the <code>database_id</code> defined in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>: for example, <code>--d1 DB=xxxx-xxxx-xxxx-xxxx-xxxx</code>.</li>
</ol>
<p>The following example shows you how to create a server endpoint configured to query D1.</p>
<ul>
<li>Bindings are available on the <code>platform</code> parameter passed to each endpoint, via <code>platform.env.BINDING_NAME</code>.</li>
<li>With SvelteKit's <a href="https://kit.svelte.dev/docs/routing">file-based routing</a>, the server endpoint defined in <code>src/routes/api/users/+server.ts</code> is available at <code>/api/users</code> within your SvelteKit app.</li>
</ul>
<p>The example also shows you how to configure both your app-wide types within <code>src/app.d.ts</code> to recognize your <code>D1Database</code> binding, import the <code>@sveltejs/adapter-cloudflare</code> adapter into <code>svelte.config.js</code>, and configure it to apply to all of your routes.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7359.md")
</div></div>
