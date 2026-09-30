<p class="article-summary">Query your D1 database from a Remix application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7360.md")
</aside>
<p>Remix is a full-stack web framework that operates on both client and server. You can query your D1 database(s) from Remix using Remix's <a href="https://remix.run/docs/en/main/guides/data-loading">data loading</a> API with the <a href="https://remix.run/docs/en/main/hooks/use-loader-data"><code>useLoaderData</code></a> hook.</p>
<p>To set up a new Remix site on Cloudflare Pages that can query D1:</p>
<ol>
<li><strong>Refer to <a href="/pages/framework-guides/deploy-a-remix-site/">the Remix guide</a></strong>.</li>
<li>Bind a D1 database to your <a href="/pages/functions/bindings/#d1-databases">Pages Function</a>.</li>
<li>Pass the <code>--d1 BINDING_NAME=DATABASE_ID</code> flag to <code>wrangler dev</code> when developing locally. <code>BINDING_NAME</code> should match what call in your code, and <code>DATABASE_ID</code> should match the <code>database_id</code> defined in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>: for example, <code>--d1 DB=xxxx-xxxx-xxxx-xxxx-xxxx</code>.</li>
</ol>
<p>The following example shows you how to define a Remix <a href="https://remix.run/docs/en/main/route/loader"><code>loader</code></a> that has a binding to a D1 database.</p>
<ul>
<li>Bindings are passed through on the <code>context.cloudflare.env</code> parameter passed to a <code>LoaderFunction</code>.</li>
<li>If you configured a <a href="/pages/functions/bindings/#d1-databases">binding</a> named <code>DB</code>, then you would access <a href="/d1/worker-api/prepared-statements/">D1 Workers Binding API</a> methods via <code>context.cloudflare.env.DB</code>.</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7362.md")
</div></div>
