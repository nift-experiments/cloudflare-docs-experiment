<p><strong>Start from CLI</strong>: Scaffold an Astro project on Workers, and pick your template.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-astro-app --framework=astro</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-astro-app --framework=astro" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-astro-app --framework=astro</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-astro-app --framework=astro" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-astro-app --framework=astro</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-astro-app --framework=astro" aria-label="Copy to clipboard">Copy</button></div></div>
<hr />
<p><strong>Or just deploy</strong>: Create a static blog with Astro and deploy it on Cloudflare Workers, with CI/CD and previews all set up for you.</p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create/deploy-to-workers&amp;repository=https://github.com/cloudflare/templates/tree/main/astro-blog-starter-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<h2 id="what-is-astro">What is Astro?</h2>
<p><a href="https://astro.build/">Astro</a> is a JavaScript web framework designed for creating websites that display large amounts of content (such as blogs, documentation sites, or online stores).</p>
<p>Astro emphasizes performance through minimal client-side JavaScript - by default, it renders as much content as possible at build time, or <a href="https://docs.astro.build/en/guides/on-demand-rendering/">on-demand</a> on the &quot;server&quot; - this can be a Cloudflare Worker. <a href="https://docs.astro.build/en/concepts/islands/">“Islands”</a> of JavaScript are added only where interactivity or personalization is needed.</p>
<p>Astro is also framework-agnostic, and supports every major UI framework, including React, Preact, Svelte, Vue, SolidJS, via its official <a href="https://astro.build/integrations/">integrations</a>.</p>
<h2 id="deploy-a-new-astro-project-on-workers">Deploy a new Astro project on Workers</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16960.md")
</div>
<h2 id="deploy-an-existing-astro-project-on-workers">Deploy an existing Astro project on Workers</h2>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="automatic-configuration">Automatic configuration</h3>
@markup("md", "content/.markup/bodies/16958.md")
</aside>
<div class="nb-interactive-component" data-cf-component="AutoconfigDiagram"></div>
<h2 id="manual-configuration">Manual configuration</h2>
<p>If you prefer to configure your project manually, follow the steps below.</p>
<h3 id="if-you-have-a-static-site">If you have a static site</h3>
<p>If your Astro project is entirely pre-rendered, follow these steps:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16963.md")
</div>
<h3 id="if-your-site-uses-on-demand-rendering">If your site uses on demand rendering</h3>
<p>If your Astro project uses <a href="https://docs.astro.build/en/guides/on-demand-rendering/">on demand rendering (also known as SSR)</a>, follow these steps:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16967.md")
</div>
<h2 id="bindings">Bindings</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16957.md")
</aside>
<p>With bindings, your Astro application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more. Refer to the <a href="/workers/runtime-apis/bindings/">bindings overview</a> for more information on what's available and how to configure them.</p>
<p>The <a href="https://docs.astro.build/en/guides/integrations-guide/cloudflare/#cloudflare-runtime">Astro docs</a> provide information about how you can access them in your <code>locals</code>.</p>
<h2 id="sessions">Sessions</h2>
<p>Astro's <a href="https://docs.astro.build/en/guides/sessions/">Sessions API</a> allows you to store user data between requests, such as user preferences, shopping carts, or authentication credentials. When using the Cloudflare adapter, Astro automatically configures <a href="/kv/">Workers KV</a> for session storage.</p>
<p>Wrangler automatically provisions a KV namespace named <code>SESSION</code> when you deploy, so no manual setup is required.</p>
<pre><code class="language-astro">&#45;--&#10;export const prerender = false;&#10;const cart = await Astro.session?.get(&quot;cart&quot;);&#10;&#45;--&#10;&#10;&lt;a href=&quot;/checkout&quot;&gt;{cart?.length ?? 0} items&lt;/a&gt;&#10;</code></pre>
<p>You can customize the KV binding name with the <a href="https://docs.astro.build/en/guides/integrations-guide/cloudflare/#sessionkvbindingname"><code>sessionKVBindingName</code></a> adapter option if you want to use a different binding name.</p>
<h2 id="custom-404-pages">Custom 404 pages</h2>
<p>To serve a custom 404 page for your Astro site, add <code>not_found_handling</code> to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16968.md")
</div>
<p>This tells Cloudflare to serve your custom 404 page (for example, <code>src/pages/404.astro</code>) when a route is not found. Read more about <a href="/workers/static-assets/routing/">static asset routing behavior</a>.</p>
<h2 id="astro-s-build-configuration">Astro's build configuration</h2>
<p>The Astro Cloudflare adapter sets the build output configuration to <code>output: 'server'</code>, which means all pages are rendered on-demand in your Cloudflare Worker. If there are certain pages that <em>don't</em> need on demand rendering/SSR, for example static pages such as a privacy policy, you should set <code>export const prerender = true</code> for that page or route to pre-render it. You can read more about on-demand rendering <a href="https://docs.astro.build/en/guides/on-demand-rendering/">in the Astro docs</a>.</p>
<p>If you want to use Astro as a static site generator, you do not need the Astro Cloudflare adapter. Astro will pre-render all pages at build time by default, and you can simply upload those static assets to be served by Cloudflare.</p>
<h2 id="node-js-requirements">Node.js requirements</h2>
<p>Astro 5.x supports Node.js 18.20.8, Node.js 20.3.0 and later 20.x releases, or Node.js 22.0.0 or later. Astro 6.x and 7.x require Node.js 22.12.0 or later. If you use <a href="/workers/ci-cd/builds/">Workers Builds</a>, its default Node.js version meets these requirements. If you override the default, select a version that meets <a href="https://docs.astro.build/en/install-and-setup/#prerequisites">Astro's Node.js requirements</a>.</p>
