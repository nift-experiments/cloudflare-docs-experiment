<p><strong>Start from CLI</strong>: Scaffold a Docusaurus project on Workers, and pick your template.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-docusaurus-app --framework=docusaurus</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-docusaurus-app --framework=docusaurus" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-docusaurus-app --framework=docusaurus</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-docusaurus-app --framework=docusaurus" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-docusaurus-app --framework=docusaurus</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-docusaurus-app --framework=docusaurus" aria-label="Copy to clipboard">Copy</button></div></div>
<p><strong>Or just deploy</strong>: Create a documentation site with Docusaurus and deploy it on Cloudflare Workers, with CI/CD and previews all set up for you.</p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create/deploy-to-workers&amp;repository=https://github.com/cloudflare/templates/tree/staging/astro-blog-starter-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<h2 id="what-is-docusaurus">What is Docusaurus?</h2>
<p><a href="https://docusaurus.io/">Docusaurus</a> is an open-source framework for building, deploying, and maintaining documentation websites. It is built on React and provides an intuitive way to create static websites with a focus on documentation.</p>
<p>Docusaurus is designed to be easy to use and customizable, making it a popular choice for developers and organizations looking to create documentation sites quickly.</p>
<h2 id="deploy-a-new-docusaurus-project-on-workers">Deploy a new Docusaurus project on Workers</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16981.md")
</div>
<h2 id="deploy-an-existing-docusaurus-project-on-workers">Deploy an existing Docusaurus project on Workers</h2>
<h3 id="if-you-have-a-static-site">If you have a static site</h3>
<p>If your Docusaurus project is entirely pre-rendered (which it usually is), follow these steps:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16984.md")
</div>
<h2 id="use-bindings-with-docusaurus">Use bindings with Docusaurus</h2>
<p>Bindings are a way to connect your Docusaurus project to other Cloudflare services, enabling you to store and retrieve data within your application.</p>
<p>With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.</p>
<p><a class="nb-card nb-link-card" href="/workers/runtime-apis/bindings/"><h3 id="card-bindings-workers-runtime-apis-bindings">Bindings</h3><p>Access to compute, storage, AI and more.</p></a></p>
