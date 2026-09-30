<p><a href="https://react.dev/">React</a> is a framework for building user interfaces. It allows you to create reusable UI components and manage the state of your application efficiently. You can use React to build a single-page application (SPA), and combine it with a backend API running on Cloudflare Workers to create a full-stack application.</p>
<p>This guide shows you how to deploy a React + Vite application to Cloudflare Workers. You can either create a new project using the <code>create-cloudflare</code> CLI (C3) or adapt an existing React + Vite project.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16934.md")
</div></div>
<hr />
<h2 id="asset-routing">Asset Routing</h2>
<p>If you're using React as a SPA, you will want to set <code>not_found_handling = &quot;single-page-application&quot;</code> in your Wrangler configuration file.</p>
<p>By default, Cloudflare first tries to match a request path against a static asset path, which is based on the file structure of the uploaded asset directory. This is either the directory specified by <code>assets.directory</code> in your Wrangler config or, in the case of the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>, the output directory of the client build. Failing that, we invoke a Worker if one is present. If there is no Worker, or the Worker then uses the asset binding, Cloudflare will fallback to the behaviour set by <a href="/workers/static-assets/#routing-behavior"><code>not_found_handling</code></a>.</p>
<p>Refer to the <a href="/workers/static-assets/routing/">routing documentation</a> for more information about how routing works with static assets, and how to customize this behavior.</p>
<h2 id="use-bindings-with-react">Use bindings with React</h2>
<p>Your project can also contain a Worker at <code>./worker/index.ts</code>, which you can use as a backend API for your React application. While your React application cannot directly access Workers bindings, it can interact with them through this Worker. You can make <a href="/workers/runtime-apis/fetch/"><code>fetch()</code> requests</a> from your React application to the Worker, which can then handle the request and use bindings. Learn how to <a href="/workers/runtime-apis/bindings/">configure Workers bindings</a>.</p>
<p>With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.</p>
<p><a class="nb-card nb-link-card" href="/workers/runtime-apis/bindings/"><h3 id="card-bindings-workers-runtime-apis-bindings">Bindings</h3><p>Access to compute, storage, AI and more.</p></a></p>
