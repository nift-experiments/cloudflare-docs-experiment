---
cp9:
  canonical: https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/
  description: Deploy a TanStack Start application to Cloudflare Workers.
  full_title: TanStack Start · Cloudflare Workers docs
  head_html: <title>TanStack Start · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy a TanStack Start application to Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/index.md"><meta property="og:title" content="TanStack Start · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy a TanStack Start application to Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="full-stack"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/#page","headline":"TanStack Start \u00b7 Cloudflare Workers docs","description":"Deploy a TanStack Start application to Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["full-stack"]}</script>
  markdown: true
  noindex: false
  route: /workers/framework-guides/web-apps/tanstack-start/
  schema: 1
---
<p><a href="https://tanstack.com/start">TanStack Start</a> is a full-stack framework for building web applications with server-side rendering, streaming, server functions, and bundling.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="already-have-a-tanstack-start-project">Already have a TanStack Start project?</h3>
@markup("md", "content/.markup/bodies/16902.md")
</aside>
<div class="nb-interactive-component" data-cf-component="AutoconfigDiagram"></div>
<h2 id="create-a-new-application">Create a new application</h2>
<p>Create a TanStack Start application pre-configured for Cloudflare Workers:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Start a local development server to preview your project during development:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm run dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn run dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm run dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm run dev" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="configure-an-existing-application">Configure an existing application</h2>
<p>If you have an existing TanStack Start application, configure it to run on Cloudflare Workers:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16905.md")
</div>
<h2 id="deploy">Deploy</h2>
<p>Deploy to a <code>*.workers.dev</code> subdomain or a <a href="/workers/configuration/routing/custom-domains/">custom domain</a> from your machine or any CI/CD system, including <a href="/workers/ci-cd/builds/">Workers Builds</a>.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm run deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm run deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn run deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn run deploy" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm run deploy</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm run deploy" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16901.md")
</aside>
<h2 id="custom-entrypoints">Custom entrypoints</h2>
<p>TanStack Start uses <code>@tanstack/react-start/server-entry</code> as your default entrypoint. Create a custom server entrypoint to add additional Workers handlers such as <a href="/queues/">Queues</a> and <a href="/workers/configuration/cron-triggers/">Cron Triggers</a>. This is also where you can add additional exports such as <a href="/durable-objects/">Durable Objects</a> and <a href="/workflows/">Workflows</a>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16908.md")
</div>
<h3 id="test-scheduled-handlers-locally">Test scheduled handlers locally</h3>
<p>Test your scheduled handler locally using the <code>/cdn-cgi/local/scheduled</code> endpoint:</p>
<pre tabindex="0"><code class="language-sh">curl &quot;http://localhost:3000/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot;&#10;</code></pre>
<details class="nb-details"><summary>Example: Using Workflows</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16911.md")
</div></details>
<details class="nb-details"><summary>Example: Using Service Bindings</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16914.md")
</div></details>
<h2 id="bindings">Bindings</h2>
<p>Your TanStack Start application can be fully integrated with the Cloudflare Developer Platform, in both local development and in production, by using <a href="/workers/runtime-apis/bindings/">bindings</a>.</p>
<p>Access bindings by <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global">importing the <code>env</code> object</a> in your server-side code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16915.md")
</div>
<p>Generate TypeScript types for your bindings based on your Wrangler configuration:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm run cf-typegen</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm run cf-typegen" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn run cf-typegen</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn run cf-typegen" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm run cf-typegen</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm run cf-typegen" aria-label="Copy to clipboard">Copy</button></div></div>
<p>With bindings, your application can be fully integrated with the Cloudflare Developer Platform, giving you access to compute, storage, AI and more.</p>
<div class="nb-card nb-link-card"><h3 id="card-bindings-workers-runtime-apis-bindings"><a href="/workers/runtime-apis/bindings/">Bindings</a></h3><p>Access to compute, storage, AI and more.</p></div>
<h3 id="use-r2-in-a-server-function">Use R2 in a server function</h3>
<p>Add an <a href="/r2/api/workers/workers-api-usage/#4-bind-your-bucket-to-a-worker">R2 bucket binding</a> to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16916.md")
</div>
<p>Access the bucket in a server function:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16917.md")
</div>
<h2 id="static-prerendering">Static prerendering</h2>
<p>Prerender your application to static HTML at build time and serve as <a href="/workers/static-assets/">static assets</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16918.md")
</div>
<p>For more options, refer to <a href="https://tanstack.com/start/latest/docs/framework/react/guide/static-prerendering">TanStack Start static prerendering</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16900.md")
</aside>
<h3 id="prerendering-data-sources">Prerendering data sources</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16899.md")
</aside>
<p>To prerender with production data, use <a href="/workers/local-development/#remote-bindings">remote bindings</a>.</p>
<p>In CI environments, environment variables or secrets may not be available during the build. To make them accessible:</p>
<ul>
<li>Set <code>CLOUDFLARE_INCLUDE_PROCESS_ENV=true</code> in your CI environment and provide the required values as environment variables.</li>
<li>If using <a href="/workers/ci-cd/builds/">Workers Builds</a>, update your <a href="/workers/ci-cd/builds/configuration/#build-settings">build settings</a>.</li>
</ul>
