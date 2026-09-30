---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/getting-started/
  description: Load and run a dynamic Worker.
  full_title: Getting started · Cloudflare Dynamic Workers docs
  head_html: <title>Getting started · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Load and run a dynamic Worker."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/getting-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/getting-started/index.md"><meta property="og:title" content="Getting started · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Load and run a dynamic Worker."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/getting-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Dynamic Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dynamic-workers/getting-started/#page","headline":"Getting started \u00b7 Cloudflare Dynamic Workers docs","description":"Load and run a dynamic Worker.","url":"https://developers.cloudflare.com/dynamic-workers/getting-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/getting-started/
  schema: 1
---
<p>You can create a Worker that spins up other Workers, called Dynamic Workers, at runtime to execute code on-demand in a secure, sandboxed environment. You provide the code, choose which bindings the Dynamic Worker can access, and control whether the Dynamic Worker can reach the network.</p>
<p>Dynamic Workers support two loading modes:</p>
<ul>
<li><code>load(code)</code> creates a fresh Dynamic Worker for one-time execution.</li>
<li><code>get(id, callback)</code> caches a Dynamic Worker by ID so it can stay warm across requests.</li>
</ul>
<p><code>load()</code> is best for one-time code execution, for example when using <a href="/agents/tools/codemode/">Code Mode</a>. <code>get(id, callback)</code> is better when the same code will receive subsequent requests, for example when you are building applications.</p>
<h3 id="try-it-out">Try it out</h3>
<h4 id="dynamic-workers-starter">Dynamic Workers Starter</h4>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>Use this &quot;hello world&quot; <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers">starter</a> to get a Worker deployed that can load and execute Dynamic Workers.</p>
<h4 id="dynamic-workers-playground">Dynamic Workers Playground</h4>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>You can also deploy the <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">Dynamic Workers Playground</a>, where you can write or import code, bundle it at runtime with <code>@cloudflare/worker-bundler</code>, execute it through a Dynamic Worker, and see real-time responses and execution logs.</p>
<h2 id="configure-worker-loader">Configure Worker Loader</h2>
<p>In order for a Worker to be able to create Dynamic Workers, it needs a Worker Loader binding. Unlike most Workers bindings, this binding doesn't point at any external resource in particular; it simply provides access to the Worker Loader API.</p>
<p>Configure it like so, in your Worker's <code>wrangler.jsonc</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1073.md")
</div>
<p>Your Worker will then have access to the Worker Loader API via <code>env.LOADER</code>.</p>
<h2 id="run-a-dynamic-worker">Run a Dynamic Worker</h2>
<p>Use <code>env.LOADER.load()</code> to create a Dynamic Worker and run it:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1074.md")
</div>
<p>In this example, <code>env.LOADER.load()</code> creates a Dynamic Worker from the code defined in <code>modules</code> and returns a stub that represents it.</p>
<p><code>worker.getEntrypoint().fetch(request)</code> sends the incoming request to the Dynamic Worker's <code>fetch()</code> handler, which processes it and returns a response.</p>
<h3 id="reusing-a-dynamic-worker-across-requests">Reusing a Dynamic Worker across requests</h3>
<p>If you expect to load the exact same Worker more than once, use <a href="/dynamic-workers/api-reference/#get"><code>get(id, callback)</code></a> instead of <code>load()</code>. The <code>id</code> should be a unique string identifying the particular code you intend to load. When the runtime sees the same <code>id</code> again, it can reuse the existing Worker instead of creating a new one, if it hasn't been evicted yet.</p>
<p>The callback you provide will only be called if the Worker is not already loaded. This lets you skip loading the code from storage when the Worker is already running.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1075.md")
</div>
<h2 id="supported-languages">Supported languages</h2>
<p>Dynamic Workers support JavaScript (ES modules and CommonJS), Python, and WebAssembly (Wasm) modules. Pass JavaScript and Python code as strings in the <code>modules</code> object. Pass compiled Wasm binaries as <code>{ wasm: ArrayBuffer }</code> module objects.</p>
<p>There is no build step, so languages like TypeScript must be compiled to JavaScript before being passed to <code>load()</code> or <code>get()</code>.</p>
<p>For the full list of supported module types, refer to the <a href="/dynamic-workers/api-reference/#modules">API reference</a>.</p>
<h3 id="python-workers">Python Workers</h3>
To run Python code in a Dynamic Worker, you must include the `python_workers` compatibility flag. Without this flag, the Dynamic Worker will fail to load the Python runtime.
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1076.md")
</div>
<h3 id="using-typescript-and-npm-dependencies">Using TypeScript and npm dependencies</h3>
<p>If your Dynamic Worker needs TypeScript compilation or npm dependencies, the code must be transpiled and bundled before passing to the Worker Loader.</p>
<p><a href="https://www.npmjs.com/package/@cloudflare/worker-bundler"><code>@cloudflare/worker-bundler</code></a> is a library that handles this for you. Use it to bundle source files into a format that <code>load()</code> and <code>get()</code> accept:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1077.md")
</div>
<p><code>createWorker()</code> handles TypeScript compilation, dependency resolution from npm, and bundling. It returns <code>mainModule</code> and <code>modules</code> ready to pass directly to <code>load()</code> or <code>get()</code>.</p>
