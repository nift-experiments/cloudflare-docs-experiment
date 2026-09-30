<p>The Cloudflare Vite plugin enables a full-featured integration between <a href="https://vite.dev/">Vite</a> and the <a href="/workers/runtime-apis/">Workers runtime</a>.
Your Worker code runs inside <a href="https://github.com/cloudflare/workerd">workerd</a>, matching the production behavior as closely as possible and providing confidence as you develop and deploy your applications.</p>
<h2 id="features">Features</h2>
<ul>
<li>Uses the Vite <a href="https://vite.dev/guide/api-environment">Environment API</a> to integrate Vite with the Workers runtime</li>
<li>Provides direct access to <a href="/workers/runtime-apis/">Workers runtime APIs</a> and <a href="/workers/runtime-apis/bindings/">bindings</a></li>
<li>Builds your front-end assets for deployment to Cloudflare, enabling you to build static sites, SPAs, and full-stack applications</li>
<li>Official support for <a href="https://tanstack.com/start/">TanStack Start</a> and <a href="https://reactrouter.com/">React Router v8</a> with server-side rendering</li>
<li>Leverages Vite's hot module replacement for consistently fast updates</li>
<li>Supports <code>vite preview</code> for previewing your build output in the Workers runtime prior to deployment</li>
</ul>
<h2 id="use-cases">Use cases</h2>
<ul>
<li><a href="https://tanstack.com/start/">TanStack Start</a></li>
<li><a href="https://reactrouter.com/">React Router v8</a></li>
<li>Static sites, such as single-page applications, with or without an integrated backend API</li>
<li>Standalone Workers</li>
<li>Multi-Worker applications</li>
</ul>
<h2 id="get-started">Get started</h2>
<p>To create a new application from a ready-to-go template, refer to the <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start</a>, <a href="/workers/framework-guides/web-apps/react-router/">React Router</a>, <a href="/workers/framework-guides/web-apps/react/">React</a> or <a href="/workers/framework-guides/web-apps/vue/">Vue</a> framework guides.</p>
<p>To create a standalone Worker from scratch, refer to <a href="/workers/vite-plugin/get-started/">Get started</a>.</p>
<p>For a more in-depth look at adapting an existing Vite project and an introduction to key concepts, refer to the <a href="/workers/vite-plugin/tutorial/">Tutorial</a>.</p>
