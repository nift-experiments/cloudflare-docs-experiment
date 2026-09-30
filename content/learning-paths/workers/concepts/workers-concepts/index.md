---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/workers/concepts/workers-concepts/
  description: Learn Workers runtime and execution model.
  full_title: Cloudflare Workers · Cloudflare Learning Paths
  head_html: <title>Cloudflare Workers · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn Workers runtime and execution model."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/workers/concepts/workers-concepts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/workers/concepts/workers-concepts/index.md"><meta property="og:title" content="Cloudflare Workers · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn Workers runtime and execution model."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/workers/concepts/workers-concepts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/workers/concepts/workers-concepts/#page","headline":"Cloudflare Workers \u00b7 Cloudflare Learning Paths","description":"Learn Workers runtime and execution model.","url":"https://developers.cloudflare.com/learning-paths/workers/concepts/workers-concepts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/workers/concepts/workers-concepts/
  schema: 1
---
<p>Cloudflare Workers gives developers the power to deploy serverless code instantly to Cloudflare's global network.</p>
<p>Cloudflare Workers significantly differs from other serverless computing providers in its execution model and architecture.</p>
<h2 id="what-you-can-do-with-workers">What you can do with Workers</h2>
<p>A single Worker project can have logic as complex or as simple as the developer desires. A project of smaller scale might look like a Worker that <a href="/workers/examples/return-html/">returns a small HTML page</a> on a single route. A more complex Worker project would span multiple domains, multiple routes for each domain, and different logic for each route. The developer decides the architectural complexity of their Worker project.</p>
<p>Your application can be made up of multiple Workers that work together and deliver a single experience to end users. Workers can also integrate with other Cloudflare Developer Platform functionality such as storage, media and AI. You will learn more about this in the <a href="/learning-paths/workers/devplat/">Developer Platform module</a>.</p>
<h2 id="runtime">Runtime</h2>
<p>The <a href="https://blog.cloudflare.com/workerd-open-source-workers-runtime">Workers runtime</a> is designed to be JavaScript-standards compliant and web-interoperable. The Workers runtime uses the V8 engine — the same engine used by Chromium and Node.js, and has an open-source version, <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>.</p>
<h2 id="execution">Execution</h2>
<p>The Cloudflare Workers runtime runs in every data center of <a href="https://www.cloudflare.com/network/">Cloudflare's global network</a>. Every Worker run within its own isolate. Isolate architecture is what makes Workers efficient.</p>
<h3 id="isolates">Isolates</h3>
<p>Workers uses <a href="/workers/reference/how-workers-works/#isolates">isolates</a>: lightweight contexts that provide your code with variables it can access and a safe environment to be executed within. You could even consider an isolate a sandbox for your function to run in.</p>
<p>A single instance of the runtime can run hundreds or thousands of isolates, seamlessly switching between them. Each isolate's memory is completely isolated, so each piece of code is protected from other untrusted or user-written code on the runtime. Isolates are also designed to start very quickly. Instead of creating a virtual machine for each function, an isolate is created within an existing environment. This model eliminates the cold starts of the virtual machine model.</p>
<p>Unlike other serverless providers which use <a href="https://www.cloudflare.com/learning/serverless/serverless-vs-containers/">containerized processes</a> each running an instance of a language runtime, Workers pays the overhead of a JavaScript runtime once on the start of a container. Workers processes are able to run essentially limitless scripts with almost no individual overhead. Any given isolate can start around a hundred times faster than a Node process on a container or virtual machine. Notably, on startup isolates consume an order of magnitude less memory.</p>
<div class="nb-interactive-component" data-cf-component="WorkersArchitectureDiagram"></div>
<h2 id="compute-per-request">Compute per request</h2>
<p>Most Workers are a variation on the default Workers flow:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10292.md")
</div></div>
<p>For Workers written in <a href="/workers/reference/migrate-to-module-workers/">ES modules syntax</a>, when a request to your <code>*.workers.dev</code> subdomain or to your Cloudflare-managed domain is received by any of Cloudflare's data centers, the request invokes the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a> defined in your Worker code with the given request. You can respond to the request by returning a <a href="/workers/runtime-apis/response/"><code>Response</code></a> object.</p>
<h2 id="summary">Summary</h2>
<p>By reading this page, you have learned:</p>
<ul>
<li>The basics of how Worker projects are organized.</li>
<li>The fundamentals of how Workers execute on the Cloudflare network.</li>
<li>How the request to response flow executes.</li>
</ul>
<p>In the next module, you build and deploy your first Worker to the Cloudflare global network.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/cloud-computing-without-containers">Cloud computing without containers</a> - A blog post detailing the containers versus isolates difference in the context of Cloudflare.</li>
<li><a href="/workers/reference/how-workers-works/">How Workers works</a> - Learn the difference between the Workers runtime versus traditional browsers and Node.js.</li>
<li><a href="/workers/reference/how-the-cache-works/">How the cache works</a> - Learn how Workers interacts with the Cloudflare cache.</li>
</ul>
<h2 id="feedback">Feedback</h2>
<p>To improve this learning path or report any missing or incorrect information, <a href="https://github.com/cloudflare/cloudflare-docs/issues/new/choose">file an issue on GitHub</a>.</p>
<h2 id="community">Community</h2>
<p>Connect with the <a href="https://discord.cloudflare.com">Cloudflare Developer Platform community on Discord</a> to ask questions, share what you are building, and discuss the platform with other developers.</p>
