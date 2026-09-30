---
cp9:
  canonical: https://developers.cloudflare.com/d1/tutorials/build-a-comments-api/
  description: Use D1 to add comments to a static blog site. Create a D1 database and build a JSON API with Hono that allows the creation and retrieval of comments.
  full_title: Build a Comments API · Cloudflare D1 docs
  head_html: <title>Build a Comments API · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Use D1 to add comments to a static blog site. Create a D1 database and build a JSON API with Hono that allows the creation and retrieval of comments."><link rel="canonical" href="https://developers.cloudflare.com/d1/tutorials/build-a-comments-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/tutorials/build-a-comments-api/index.md"><meta property="og:title" content="Build a Comments API · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use D1 to add comments to a static blog site. Create a D1 database and build a JSON API with Hono that allows the creation and retrieval of comments."><meta property="og:url" content="https://developers.cloudflare.com/d1/tutorials/build-a-comments-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="Hono,TypeScript,SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/tutorials/build-a-comments-api/#page","headline":"Build a Comments API \u00b7 Cloudflare D1 docs","description":"Use D1 to add comments to a static blog site. Create a D1 database and build a JSON API with Hono that allows the creation and retrieval of comments.","url":"https://developers.cloudflare.com/d1/tutorials/build-a-comments-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Hono","TypeScript","SQL"]}</script>
  markdown: true
  noindex: false
  route: /d1/tutorials/build-a-comments-api/
  schema: 1
---
<p>In this tutorial, you will use D1 and <a href="https://hono.dev/">Hono</a> to build a JSON API that stores and retrieves comments for a blog. You will create a D1 database, define a schema, and wire up <code>GET</code> and <code>POST</code> endpoints that read from and write to the database.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7309.md")
</div></details>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7310.md")
</div>
<h2 id="2-install-hono"><ol start="2">
<li>Install Hono</li>
</ol></h2>
<p>Install <a href="https://hono.dev/">Hono</a>, a lightweight web framework for building APIs on Workers:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add hono" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="3-create-a-database"><ol start="3">
<li>Create a database</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7312.md")
</div>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like D1 databases, KV namespaces, and R2 buckets, using a variable name in code. Your D1 database is accessible in your Worker on <code>env.DB</code>.</p>
<h2 id="4-create-a-schema-and-seed-the-database"><ol start="4">
<li>Create a schema and seed the database</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7313.md")
</div>
<h2 id="5-initialize-the-hono-application"><ol start="5">
<li>Initialize the Hono application</li>
</ol></h2>
<p>Replace the contents of <code>src/index.ts</code> with the following code. This sets up a Hono application with a typed <code>Bindings</code> interface so that <code>env.DB</code> is correctly typed as a <code>D1Database</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7314.md")
</div>
<h2 id="6-query-comments"><ol start="6">
<li>Query comments</li>
</ol></h2>
<p>Add the logic for the <code>GET</code> endpoint to retrieve comments for a given post. This uses the D1 <a href="/d1/worker-api/">Workers Binding API</a> to prepare and execute a parameterized query:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7315.md")
</div>
<p>The code uses <a href="/d1/worker-api/d1-database/#prepare"><code>prepare</code></a> to create a parameterized statement, <a href="/d1/worker-api/prepared-statements/#bind"><code>bind</code></a> to safely pass the slug value (preventing SQL injection), and <a href="/d1/worker-api/prepared-statements/#run"><code>run</code></a> to execute the query.</p>
<h2 id="7-insert-comments"><ol start="7">
<li>Insert comments</li>
</ol></h2>
<p>Add the <code>POST</code> endpoint to create new comments. This validates the request body before inserting a row:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7316.md")
</div>
<h2 id="8-optional-add-cors-support"><ol start="8">
<li>(Optional) Add CORS support</li>
</ol></h2>
<p>If you plan to call this API from a front-end application on a different origin, add CORS middleware. Import the <code>cors</code> module from Hono and add it before your routes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7317.md")
</div>
<p>When you make requests to <code>/api/*</code>, Hono will automatically generate and add CORS headers to responses from your API.</p>
<h2 id="9-deploy-your-application"><ol start="9">
<li>Deploy your application</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7318.md")
</div>
<h2 id="full-example">Full example</h2>
<p>The complete <code>src/index.ts</code> with all routes and CORS support:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7319.md")
</div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Refer to the <a href="/d1/worker-api/">D1 Workers Binding API</a> for a full list of available methods.</li>
<li>Learn about <a href="/d1/best-practices/local-development/">D1 local development</a> for testing your database without deploying.</li>
<li>Explore <a href="/d1/reference/community-projects/">community projects built on D1</a>.</li>
</ul>
