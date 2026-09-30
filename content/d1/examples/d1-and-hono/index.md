<p class="article-summary">Query D1 from the Hono web framework</p>
<p>Hono is a fast web framework for building API-first applications, and it includes first-class support for both <a href="/workers/">Workers</a> and <a href="/pages/">Pages</a>.</p>
<p>When using Workers:</p>
<ul>
<li>Ensure you have configured your <a href="/d1/get-started/#3-bind-your-worker-to-your-d1-database">Wrangler configuration file</a> to bind your D1 database to your Worker.</li>
<li>You can access your D1 databases via Hono's <a href="https://hono.dev/api/context"><code>Context</code></a> parameter: <a href="https://hono.dev/getting-started/cloudflare-workers#bindings">bindings</a> are exposed on <code>context.env</code>. If you configured a <a href="/pages/functions/bindings/#d1-databases">binding</a> named <code>DB</code>, then you would access <a href="/d1/worker-api/prepared-statements/">D1 Workers Binding API</a> methods via <code>c.env.DB</code>.</li>
<li>Refer to the Hono documentation for <a href="https://hono.dev/getting-started/cloudflare-workers">Cloudflare Workers</a>.</li>
</ul>
<p>If you are using <a href="/pages/functions/">Pages Functions</a>:</p>
<ol>
<li>Bind a D1 database to your <a href="/pages/functions/bindings/#d1-databases">Pages Function</a>.</li>
<li>Pass the <code>--d1 BINDING_NAME=DATABASE_ID</code> flag to <code>wrangler dev</code> when developing locally. <code>BINDING_NAME</code> should match what call in your code, and <code>DATABASE_ID</code> should match the <code>database_id</code> defined in your Wrangler configuration file: for example, <code>--d1 DB=xxxx-xxxx-xxxx-xxxx-xxxx</code>.</li>
<li>Refer to the Hono guide for <a href="https://hono.dev/getting-started/cloudflare-pages">Cloudflare Pages</a>.</li>
</ol>
<p>The following examples show how to access a D1 database bound to <code>DB</code> from both a Workers script and a Pages Function:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7365.md")
</div></div>
