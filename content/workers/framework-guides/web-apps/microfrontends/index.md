---
cp9:
  canonical: https://developers.cloudflare.com/workers/framework-guides/web-apps/microfrontends/
  description: Split a single application into independently deployable frontends, using a router worker and service bindings
  full_title: Microfrontends · Cloudflare Workers docs
  head_html: <title>Microfrontends · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Split a single application into independently deployable frontends, using a router worker and service bindings"><link rel="canonical" href="https://developers.cloudflare.com/workers/framework-guides/web-apps/microfrontends/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/framework-guides/web-apps/microfrontends/index.md"><meta property="og:title" content="Microfrontends · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Split a single application into independently deployable frontends, using a router worker and service bindings"><meta property="og:url" content="https://developers.cloudflare.com/workers/framework-guides/web-apps/microfrontends/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/framework-guides/web-apps/microfrontends/#page","headline":"Microfrontends \u00b7 Cloudflare Workers docs","description":"Split a single application into independently deployable frontends, using a router worker and service bindings","url":"https://developers.cloudflare.com/workers/framework-guides/web-apps/microfrontends/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/framework-guides/web-apps/microfrontends/
  schema: 1
---
<p>Microfrontends let you split a single application into smaller, independently deployable units that render as one cohesive application. Different teams using different technologies can develop, test, and deploy each microfrontend.</p>
<p>Use microfrontends when you want to:</p>
<ul>
<li>Enable many teams to deploy independently without coordinating releases</li>
<li>Gradually migrate from a monolith to a distributed architecture</li>
<li>Build multi-framework applications (for example, Astro, Remix, and Next.js in one app)</li>
</ul>
<h2 id="get-started">Get started</h2>
<p>Create a microfrontend project:</p>
<p><a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create?type=vmfe"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This template automatically creates a router worker with pre-configured routing logic, and lets you configure <a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a> to Workers you have already deployed to your Cloudflare account. The code or this template is available on GitHub at <a href="https://github.com/cloudflare/templates/tree/main/microfrontend-template">cloudflare/templates</a>.</p>
<h2 id="how-it-works">How it works</h2>
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;    A[Browser Request] --&gt; B[Router Worker]&#10;    B --&gt;|Service Binding| C[Microfrontend A]&#10;    B --&gt;|Service Binding| D[Microfrontend B]&#10;    B --&gt;|Service Binding| E[Microfrontend C]&#10;</code></pre>
<p>The router worker:</p>
<ol>
<li>Analyzes the incoming request path</li>
<li>Matches it against configured routes</li>
<li>Forwards the request to the appropriate microfrontend via service binding</li>
<li>Rewrites HTML, CSS, and headers to ensure assets load correctly</li>
<li>Returns the response to the browser</li>
</ol>
<p>Each microfrontend can be:</p>
<ul>
<li>A full-framework application (Next.js, SvelteKit, Astro, etc.)</li>
<li>A static site with <a href="/workers/static-assets/">Workers Static Assets</a></li>
<li>Built with different frameworks and technologies</li>
</ul>
<h2 id="routing-logic">Routing logic</h2>
<p>The router worker uses a <code>ROUTES</code> <a href="/workers/configuration/environment-variables/">environment variable</a> to determine which microfrontend handles each path. Routes are matched by specificity, with longer paths taking precedence.</p>
<p>Example <code>ROUTES</code> configuration:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;routes&quot;: [&#10;		{ &quot;path&quot;: &quot;/app-a&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_A&quot;, &quot;preload&quot;: true },&#10;		{ &quot;path&quot;: &quot;/app-b&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_B&quot;, &quot;preload&quot;: true },&#10;		{ &quot;path&quot;: &quot;/&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_HOME&quot; }&#10;	],&#10;	&quot;smoothTransitions&quot;: true&#10;}&#10;</code></pre>
<p>Each route requires:</p>
<ul>
<li><code>path</code>: The mount path for the microfrontend (must be distinct from other routes)</li>
<li><code>binding</code>: The name of the service binding in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></li>
<li><code>preload</code> (optional): Whether to prefetch this microfrontend for faster navigation</li>
</ul>
<p>When a request comes in for <code>/app-a/dashboard</code>, the router:</p>
<ol>
<li>Matches it to the <code>/app-a</code> route</li>
<li>Forwards the request to <code>MICROFRONTEND_A</code></li>
<li>Strips the <code>/app-a</code> prefix, so the microfrontend receives <code>/dashboard</code></li>
</ol>
<p>The router includes path matching logic that supports:</p>
<pre tabindex="0"><code class="language-typescript">// Static paths&#10;{ &quot;path&quot;: &quot;/dashboard&quot; }&#10;&#10;// Dynamic parameters&#10;{ &quot;path&quot;: &quot;/users/:id&quot; }&#10;&#10;// Wildcard matching (zero or more segments)&#10;{ &quot;path&quot;: &quot;/docs/:path*&quot; }&#10;&#10;// Required segments (one or more segments)&#10;{ &quot;path&quot;: &quot;/api/:path+&quot; }&#10;</code></pre>
<h2 id="path-rewriting">Path rewriting</h2>
<p>The router worker uses <a href="/workers/runtime-apis/html-rewriter/">HTMLRewriter</a> to automatically rewrite HTML attributes to include the mount path prefix, ensuring assets load from the correct location.</p>
<p>When a microfrontend mounted at <code>/app-a</code> returns HTML:</p>
<pre tabindex="0"><code class="language-html">&lt;link rel=&quot;stylesheet&quot; href=&quot;/assets/styles.css&quot; /&gt;&#10;&lt;script src=&quot;/assets/app.js&quot;&gt;&lt;/script&gt;&#10;&lt;img src=&quot;/static/logo.png&quot; /&gt;&#10;</code></pre>
<p>The router rewrites it to:</p>
<pre tabindex="0"><code class="language-html">&lt;link rel=&quot;stylesheet&quot; href=&quot;/app-a/assets/styles.css&quot; /&gt;&#10;&lt;script src=&quot;/app-a/assets/app.js&quot;&gt;&lt;/script&gt;&#10;&lt;img src=&quot;/app-a/static/logo.png&quot; /&gt;&#10;</code></pre>
<p>The rewriter handles these attributes across all HTML elements:</p>
<ul>
<li><code>href</code>, <code>src</code>, <code>poster</code>, <code>action</code>, <code>srcset</code></li>
<li><code>data-*</code> attributes like <code>data-src</code>, <code>data-href</code>, <code>data-background</code></li>
<li>Framework-specific attributes like <code>astro-component-url</code></li>
</ul>
<p>The router only rewrites paths that start with configured asset prefixes to avoid breaking external URLs:</p>
<pre tabindex="0"><code class="language-javascript">// Default asset prefixes&#10;const DEFAULT_ASSET_PREFIXES = [&#10;	&quot;/assets/&quot;,&#10;	&quot;/static/&quot;,&#10;	&quot;/build/&quot;,&#10;	&quot;/_astro/&quot;,&#10;	&quot;/fonts/&quot;,&#10;];&#10;</code></pre>
<p>Most frameworks work with the default prefixes. For frameworks with different build outputs (like Next.js which uses <code>/_next/</code>), you can configure custom prefixes using the <code>ASSET_PREFIXES</code> <a href="/workers/configuration/environment-variables/">environment variable</a>:</p>
<pre tabindex="0"><code class="language-json">[&quot;/_next/&quot;, &quot;/public/&quot;]&#10;</code></pre>
<h2 id="asset-handling">Asset handling</h2>
<p>The router also rewrites CSS files to ensure <code>url()</code> references work correctly. When a microfrontend mounted at <code>/app-a</code> returns CSS:</p>
<pre tabindex="0"><code class="language-css">.hero {&#10;	background: url(/assets/hero.jpg);&#10;}&#10;&#10;.icon {&#10;	background: url(&quot;/static/icon.svg&quot;);&#10;}&#10;</code></pre>
<p>The router rewrites it to:</p>
<pre tabindex="0"><code class="language-css">.hero {&#10;	background: url(/app-a/assets/hero.jpg);&#10;}&#10;&#10;.icon {&#10;	background: url(&quot;/app-a/static/icon.svg&quot;);&#10;}&#10;</code></pre>
<p>The router also handles:</p>
<ul>
<li><strong>Redirect headers</strong>: Rewrites <code>Location</code> headers to include the mount path</li>
<li><strong>Cookie paths</strong>: Updates <code>Set-Cookie</code> headers to scope cookies to the mount path</li>
</ul>
<h2 id="route-preloading">Route Preloading</h2>
<p>When <code>preload: true</code> is set on a static mount route, the router automatically preloads those routes to enable faster navigation. The router uses <strong>browser-specific optimization</strong> to provide the best performance for each browser:</p>
<h3 id="chromium-browsers-chrome-edge-opera-brave">Chromium Browsers (Chrome, Edge, Opera, Brave)</h3>
<p>For Chromium-based browsers, the router uses the <strong>Speculation Rules API</strong> - a modern, browser-native prefetching mechanism:</p>
<ul>
<li>Injects <code>&lt;script type=&quot;speculationrules&quot;&gt;</code> into the <code>&lt;head&gt;</code> element</li>
<li>Browser handles prefetching automatically with optimal priority management</li>
<li>Respects user preferences (battery saver, data saver modes)</li>
<li>Uses per-document in-memory cache for faster access</li>
<li>Not blocked by Cache-Control headers</li>
<li>More efficient than JavaScript-based fetching</li>
</ul>
<p><strong>Example injected speculation rules:</strong></p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;prefetch&quot;: [&#10;		{&#10;			&quot;urls&quot;: [&quot;/app1&quot;, &quot;/app2&quot;, &quot;/dashboard&quot;]&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h2 id="smooth-transitions">Smooth transitions</h2>
<p>You can enable smooth page transitions between microfrontends using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API">View Transitions API</a>.</p>
<p>To enable smooth transitions, set <code>&quot;smoothTransitions&quot;: true</code> in your <code>ROUTES</code> configuration:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;routes&quot;: [&#10;		{ &quot;path&quot;: &quot;/app-a&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_A&quot; },&#10;		{ &quot;path&quot;: &quot;/app-b&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_B&quot; }&#10;	],&#10;	&quot;smoothTransitions&quot;: true&#10;}&#10;</code></pre>
<p>The router automatically injects CSS into HTML responses:</p>
<pre tabindex="0"><code class="language-css">@supports (view-transition-name: none) {&#10;	::view-transition-old(root),&#10;	::view-transition-new(root) {&#10;		animation-duration: 0.3s;&#10;		animation-timing-function: ease-in-out;&#10;	}&#10;	main {&#10;		view-transition-name: main-content;&#10;	}&#10;	nav {&#10;		view-transition-name: navigation;&#10;	}&#10;}&#10;</code></pre>
<p>This feature only works in browsers that support the View Transitions API. Browsers without support will navigate normally without animations.</p>
<h2 id="add-a-new-microfrontend">Add a new microfrontend</h2>
<p>To add a new microfrontend to your application after initial setup:</p>
<ol>
<li>
<p><strong>Create and deploy the new microfrontend worker</strong></p>
<p>Deploy your new microfrontend as a separate Worker. This can be a <a href="/workers/framework-guides/">framework application</a> (Next.js, Astro, etc.) or a static site with <a href="/workers/static-assets/">Workers Static Assets</a>.</p>
</li>
<li>
<p><strong>Add a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> in your router's Wrangler configuration file</strong></p>
</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16954.md")
</div>
<ol start="3">
<li>
<p><strong>Update the <code>ROUTES</code> environment variable</strong></p>
<p>Add your new route to the <code>ROUTES</code> configuration:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;routes&quot;: [&#10;		{ &quot;path&quot;: &quot;/app-a&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_A&quot;, &quot;preload&quot;: true },&#10;		{ &quot;path&quot;: &quot;/app-b&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_B&quot;, &quot;preload&quot;: true },&#10;		{ &quot;path&quot;: &quot;/app-c&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_C&quot;, &quot;preload&quot;: true },&#10;		{ &quot;path&quot;: &quot;/&quot;, &quot;binding&quot;: &quot;MICROFRONTEND_HOME&quot; }&#10;	]&#10;}&#10;</code></pre>
<ol start="4">
<li><strong>Redeploy the router worker</strong></li>
</ol>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your new microfrontend is now accessible at the configured path (for example, <code>/app-c</code>).</p>
<h2 id="local-development">Local development</h2>
<p>During development, you can test your microfrontend architecture locally using Wrangler's service binding support. Run the router Worker locally using <code>wrangler dev</code>, and then in separate terminals run each of the microfrontends.</p>
<p>If you only need to work on one of the microfrontends, you can run the others remotely using <a href="/workers/local-development/#remote-bindings">remote bindings</a>, without needing to have access to the source code or run a local dev server.</p>
<p>For each microfrontend you want to run remotely while in local dev, configure its service binding with the remote flag:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16955.md")
</div>
<h2 id="deployment">Deployment</h2>
<p>Each microfrontend can be deployed independently without redeploying the router or other microfrontends. This enables teams to:</p>
<ul>
<li>Deploy updates on their own schedule</li>
<li>Roll back individual microfrontends without affecting others</li>
<li>Test and release features independently</li>
</ul>
<p>When you deploy a microfrontend worker, the router automatically routes requests to the latest version via the service binding. No router changes are required unless you are adding new routes or updating the <code>ROUTES</code> configuration.</p>
<p>To deploy to production, you can use <a href="/workers/configuration/routing/custom-domains/">custom domains</a> for your router worker, and configure <a href="/workers/ci-cd/builds/">Workers Builds</a> for continuous deployment from your Git repository.</p>
