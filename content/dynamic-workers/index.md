---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/
  description: Spin up isolated Workers on demand to execute code.
  full_title: Dynamic Workers · Cloudflare Dynamic Workers docs
  head_html: <title>Dynamic Workers · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Spin up isolated Workers on demand to execute code."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/index.md"><meta property="og:title" content="Dynamic Workers · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Spin up isolated Workers on demand to execute code."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Dynamic Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/dynamic-workers/#page","headline":"Dynamic Workers \u00b7 Cloudflare Dynamic Workers docs","description":"Spin up isolated Workers on demand to execute code.","url":"https://developers.cloudflare.com/dynamic-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/1072.md")
</div>
<p>Dynamic Workers let you spin up an unlimited number of Workers to execute arbitrary code specified at runtime. Dynamic Workers can be used as a lightweight alternative to containers for securely sandboxing code you don't trust.</p>
<p>Dynamic Workers are the lowest-level primitive for spinning up a Worker, giving you full control over defining how the Worker is composed, which bindings it receives, whether it can reach the network, and more.</p>
<h3 id="get-started">Get started</h3>
<p>Deploy the <a href="https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground">Dynamic Workers Playground</a> to create and run Workers dynamically from code you write or import from GitHub, with real-time logs and observability.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/dinasaur404/dynamic-workers-playground"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<h2 id="use-dynamic-workers-for">Use Dynamic Workers for</h2>
<p>Use this pattern when code needs to run quickly in a secure, isolated environment.</p>
<ul>
<li><strong>AI Agent &quot;Code Mode&quot;</strong>: LLMs are trained to write code. Instead of supplying an agent with tool calls to perform tasks, give it an API and let it write and execute code. Save up to 80% in inference tokens and cost by allowing the agent to programmatically process data instead of sending it all through the LLM.</li>
<li><strong>AI-generated applications / &quot;Vibe Code&quot;</strong>: Run generated code for prototypes, projects, and automations in a secure, isolated sandboxed environment.</li>
<li><strong>Fast development and previews</strong>: Load prototypes, previews, and playgrounds in milliseconds.</li>
<li><strong>Custom automations</strong>: Create custom tools on the fly that execute a task, call an integration, or automate a workflow.</li>
<li><strong>Platforms</strong>: Run applications uploaded by your users.</li>
</ul>
<h2 id="features">Features</h2>
<p>Because you compose the Worker that runs the code at runtime, you control how that Worker is configured and what it can access.</p>
<ul>
<li><strong><a href="/dynamic-workers/usage/bindings/">Bindings</a></strong>: Decide which bindings and structured data the dynamic Worker receives.</li>
<li><strong><a href="/dynamic-workers/usage/observability/">Observability</a></strong>: Attach Tail Workers and capture logs for each run.</li>
<li><strong><a href="/dynamic-workers/usage/egress-control/">Network access</a></strong>: Intercept or block Internet access for outbound requests.</li>
<li><strong><a href="/dynamic-workers/usage/limits/">Limits</a></strong>: Enforce custom limits on the dynamic Worker's resource usage.</li>
<li><strong><a href="/dynamic-workers/usage/durable-object-facets/">Durable Object Facets</a></strong>: Run dynamically-loaded code as a Durable Object with its own isolated SQLite storage.</li>
</ul>
