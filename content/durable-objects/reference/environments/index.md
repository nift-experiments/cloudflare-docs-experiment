---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/reference/environments/
  description: Configure Durable Object bindings across Wrangler environments for staging, production, and custom deployments.
  full_title: Environments · Cloudflare Durable Objects docs
  head_html: <title>Environments · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Durable Object bindings across Wrangler environments for staging, production, and custom deployments."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/reference/environments/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/reference/environments/index.md"><meta property="og:title" content="Environments · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Durable Object bindings across Wrangler environments for staging, production, and custom deployments."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/reference/environments/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/reference/environments/#page","headline":"Environments \u00b7 Cloudflare Durable Objects docs","description":"Configure Durable Object bindings across Wrangler environments for staging, production, and custom deployments.","url":"https://developers.cloudflare.com/durable-objects/reference/environments/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/reference/environments/
  schema: 1
---
<p>Environments provide isolated spaces where your code runs with specific dependencies and configurations. This can be useful for a number of reasons, such as compatibility testing or version management. Using different environments can help with code consistency, testing, and production segregation, which reduces the risk of errors when deploying code.</p>
<h2 id="wrangler-environments">Wrangler environments</h2>
<p><a href="/workers/wrangler/install-and-update/">Wrangler</a> allows you to deploy the same Worker application with different configuration for each <a href="/workers/wrangler/environments/">environment</a>.</p>
<p>If you are using Wrangler environments, you must specify any <a href="/workers/runtime-apis/bindings/">Durable Object bindings</a> you wish to use on a per-environment basis.</p>
<p>Durable Object bindings are not inherited. For example, you can define an environment named <code>staging</code> as below:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8099.md")
</div>
<p>Because Wrangler appends the <a href="/workers/wrangler/environments/">environment name</a> to the top-level name when publishing, for a Worker named <code>worker-name</code> the above example is equivalent to:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8100.md")
</div>
<p><code>&quot;EXAMPLE_CLASS&quot;</code> in the staging environment is bound to a different Worker code name compared to the top-level <code>&quot;EXAMPLE_CLASS&quot;</code> binding, and will therefore access different Durable Objects with different persistent storage.</p>
<p>If you want an environment-specific binding that accesses the same Objects as the top-level binding, specify the top-level Worker code name explicitly using <code>script_name</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8101.md")
</div>
<h3 id="migration-environments">Migration environments</h3>
<p>You can define a Durable Object migration for each environment, as well as at the top level. Migrations at the environment-level override migrations at the top level.</p>
<p>For more information, refer to <a href="/durable-objects/reference/durable-object-class-migrations-legacy/#migration-wrangler-configuration">Migration Wrangler Configuration</a>.</p>
<h2 id="local-development">Local development</h2>
<p>Local development sessions create a standalone, local-only environment that mirrors the production environment, so that you can test your Worker and Durable Objects before you deploy to production.</p>
<p>An existing Durable Object binding of <code>DB</code> would be available to your Worker when running locally.</p>
<p>Refer to Workers <a href="/workers/local-development/bindings-per-env/">Local development</a>.</p>
<h2 id="remote-development">Remote development</h2>
<p>KV-backed Durable Objects support remote development using the dashboard playground. The dashboard playground uses a browser version of Visual Studio Code, allowing you to rapidly iterate on your Worker entirely in your browser.</p>
<p>To start remote development:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select an existing Worker.
3. Select the **Edit code** icon located on the upper-right of the screen.
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8098.md")
</aside>
