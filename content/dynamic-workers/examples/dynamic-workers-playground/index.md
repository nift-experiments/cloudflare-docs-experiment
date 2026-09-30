---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/
  description: Bundle, execute, and observe Dynamic Workers with real-time logs and timing.
  full_title: Dynamic Workers Playground · Cloudflare Dynamic Workers docs
  head_html: <title>Dynamic Workers Playground · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Bundle, execute, and observe Dynamic Workers with real-time logs and timing."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/index.md"><meta property="og:title" content="Dynamic Workers Playground · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bundle, execute, and observe Dynamic Workers with real-time logs and timing."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Dynamic Workers"><meta name="pcx_tags" content="JavaScript,TypeScript,Logging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/#page","headline":"Dynamic Workers Playground \u00b7 Cloudflare Dynamic Workers docs","description":"Bundle, execute, and observe Dynamic Workers with real-time logs and timing.","url":"https://developers.cloudflare.com/dynamic-workers/examples/dynamic-workers-playground/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JavaScript","TypeScript","Logging"]}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/examples/dynamic-workers-playground/
  schema: 1
---
<p>Try the Dynamic Workers <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">playground</a> to write or import code from GitHub, bundle it at runtime, execute it in a Dynamic Worker, and view real-time logs.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p><img src="/assets/upstream/images/dynamic-workers/dw-playground.png" alt="Dynamic Workers Playground UI" /></p>
<h2 id="what-this-demo-shows">What this demo shows</h2>
<ul>
<li><strong>Runtime bundling</strong> — Uses <a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a> to resolve npm dependencies and compile TypeScript inside a Worker</li>
<li><strong>Dynamic execution</strong> — Loads bundled code into an isolated Dynamic Worker</li>
<li><strong>Caching</strong> — Reuses previously bundled Workers when the source has not changed</li>
<li><strong>Real-time output</strong> — Streams the response body, console logs, execution timing, and bundle metadata back to the client</li>
</ul>
<h2 id="bundling-code-at-runtime">Bundling code at runtime</h2>
<p>The playground uses <a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a> to compile TypeScript, resolve npm dependencies, and produce modules the Worker Loader can execute.</p>
<p>Pass source files and a <code>package.json</code> to <code>createWorker()</code>, which resolves dependencies and returns bundled modules ready to load as a Dynamic Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8451.md")
</div>
<h2 id="caching-dynamic-workers">Caching Dynamic Workers</h2>
<p><code>env.LOADER.load()</code> creates a new Dynamic Worker on every call. To avoid re-bundling unchanged code, use <code>env.LOADER.get(id, callback)</code> instead. The runtime returns an existing Worker on a cache hit, or calls your callback to build one on a miss:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8452.md")
</div>
<p>In the playground, you can see this in action — run the same Dynamic Worker twice and the second request shows a cached result with 0ms cold start, since the build and load phases are skipped entirely.</p>
<h2 id="observability-with-tail-workers">Observability with Tail Workers</h2>
<p>When you run code in the playground, console output from the Dynamic Worker streams back to the browser in real time. Under the hood, this works through a <a href="/workers/observability/logs/tail-workers/">Tail Worker</a> pipeline:</p>
<ol>
<li>A Tail Worker (<code>DynamicWorkerTail</code>) captures <code>console.log</code> output from the Dynamic Worker.</li>
<li>Logs are forwarded to a <code>LogSession</code> Durable Object.</li>
<li>The Durable Object streams them to the client over WebSocket.</li>
</ol>
<p>To wire this up, include the Tail Worker in the <code>tails</code> array when creating the Dynamic Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8453.md")
</div>
<p>For more information on how to capture and stream logs from Dynamic Workers, refer to <a href="/dynamic-workers/usage/observability/">Observability with Dynamic Workers</a>.</p>
<h2 id="running-locally">Running locally</h2>
<p>Clone the repo and start the dev server:</p>
<pre tabindex="0"><code class="language-sh">npm install&#10;npm run dev&#10;</code></pre>
