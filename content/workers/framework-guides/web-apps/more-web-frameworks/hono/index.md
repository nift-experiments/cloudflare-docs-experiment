<p><strong>Start from CLI</strong> - scaffold a full-stack app with a Hono API, React SPA and the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> for lightning-fast development.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-hono-app --template=cloudflare/templates/vite-react-template</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-hono-app --template=cloudflare/templates/vite-react-template" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-hono-app --template=cloudflare/templates/vite-react-template</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-hono-app --template=cloudflare/templates/vite-react-template" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-hono-app --template=cloudflare/templates/vite-react-template</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-hono-app --template=cloudflare/templates/vite-react-template" aria-label="Copy to clipboard">Copy</button></div></div>
---
<p><strong>Or just deploy</strong> - create a full-stack app using Hono, React and Vite, with CI/CD and previews all set up for you.</p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create/deploy-to-workers&amp;repository=https://github.com/cloudflare/templates/tree/main/vite-react-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<h2 id="what-is-hono">What is Hono?</h2>
<p><a href="https://hono.dev/">Hono</a> is an ultra-fast, lightweight framework for building web applications, and works fantastically with Cloudflare Workers.
With Workers Assets, you can easily combine a Hono API running on Workers with a SPA to create a full-stack app.</p>
<h2 id="creating-a-full-stack-hono-app-with-a-react-spa">Creating a full-stack Hono app with a React SPA</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16979.md")
</div>
<hr />
<h2 id="bindings">Bindings</h2>
<p>The <a href="https://hono.dev/docs/getting-started/cloudflare-workers#bindings">Hono documentation</a> provides information on how you can access bindings in your Hono app.</p>
<p>With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.</p>
<p><a class="nb-card nb-link-card" href="/workers/runtime-apis/bindings/"><h3 id="card-bindings-workers-runtime-apis-bindings">Bindings</h3><p>Access to compute, storage, AI and more.</p></a></p>
