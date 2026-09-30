<p><strong>Start from CLI</strong>: Scaffold a full-stack app with <a href="https://reactrouter.com/">React Router v8</a> and the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> for lightning-fast development.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-react-router-app --framework=react-router</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-react-router-app --framework=react-router" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-react-router-app --framework=react-router</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-react-router-app --framework=react-router" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-react-router-app --framework=react-router</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-react-router-app --framework=react-router" aria-label="Copy to clipboard">Copy</button></div></div>
<p><strong>Or just deploy</strong>: Create a full-stack app using React Router v8, with CI/CD and previews all set up for you.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/react-router-starter-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16936.md")
</aside>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="already-have-a-react-router-project">Already have a React Router project?</h3>
@markup("md", "content/.markup/bodies/16935.md")
</aside>
<div class="nb-interactive-component" data-cf-component="AutoconfigDiagram"></div>
<h2 id="what-is-react-router">What is React Router?</h2>
<p><a href="https://reactrouter.com/">React Router v8</a> is a full-stack React framework for building web applications.
It combines with the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> to provide a first-class experience for developing, building and deploying your apps on Cloudflare.</p>
<h2 id="creating-a-full-stack-react-router-app">Creating a full-stack React Router app</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16940.md")
</div>
<h2 id="use-bindings-with-react-router">Use bindings with React Router</h2>
<p>With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.</p>
<p>Once you have configured the bindings in the Wrangler configuration file, they are then available within <code>context.cloudflare</code> in your loader or action functions:</p>
<pre><code class="language-ts">export function loader({ context }: Route.LoaderArgs) {&#10;	return { message: context.cloudflare.env.VALUE_FROM_CLOUDFLARE };&#10;}&#10;&#10;export default function Home({ loaderData }: Route.ComponentProps) {&#10;	return &lt;Welcome message={loaderData.message} /&gt;;&#10;}&#10;</code></pre>
<p>As you have direct access to your Worker entry file (<code>workers/app.ts</code>), you can also add additional exports such as <a href="/durable-objects/">Durable Objects</a> and <a href="/workflows/">Workflows</a></p>
<details class="nb-details"><summary>Example: Using Workflows</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16942.md")
</div></details>
<p>With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.</p>
<p><a class="nb-card nb-link-card" href="/workers/runtime-apis/bindings/"><h3 id="card-bindings-workers-runtime-apis-bindings">Bindings</h3><p>Access to compute, storage, AI and more.</p></a></p>
