<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>January 1, 2026</time><h2 id="post-title">Build microfrontend applications on Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now deploy microfrontends to Cloudflare, splitting a single application into smaller, independently deployable units that render as one cohesive application. This lets different teams using different frameworks develop, test, and deploy each microfrontend without coordinating releases.</p>
<p>Microfrontends solve several challenges for large-scale applications:</p>
<ul>
<li><strong>Independent deployments</strong>: Teams deploy updates on their own schedule without redeploying the entire application</li>
<li><strong>Framework flexibility</strong>: Build multi-framework applications (for example, Astro, Remix, and Next.js in one app)</li>
<li><strong>Gradual migration</strong>: Migrate from a monolith to a distributed architecture incrementally</li>
</ul>
<p>Create a microfrontend project:</p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This template automatically creates a router worker with pre-configured routing logic, and lets you configure <a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a> to Workers you have already deployed to your Cloudflare account. The router Worker analyzes incoming requests, matches them against configured routes, and forwards requests to the appropriate microfrontend via service bindings. The router automatically rewrites HTML, CSS, and headers to ensure assets load correctly from each microfrontend's mount path. The router includes advanced features like preloading for faster navigation between microfrontends, smooth page transitions using the View Transitions API, and automatic path rewriting for assets, redirects, and cookies.</p>
<p>Each microfrontend can be a full-framework application, a static site with Workers Static Assets, or any other Worker-based application.</p>
<p>Get started with the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe">microfrontends template</a>, or read the <a href="/workers/framework-guides/web-apps/microfrontends/">microfrontends documentation</a> for implementation details.</p>
</div></article></div>
