---
cp9:
  canonical: https://developers.cloudflare.com/d1/get-started/
  description: Create your first D1 database, define a schema, and query it from a Cloudflare Worker.
  full_title: Getting started · Cloudflare D1 docs
  head_html: <title>Getting started · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Create your first D1 database, define a schema, and query it from a Cloudflare Worker."><link rel="canonical" href="https://developers.cloudflare.com/d1/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/get-started/index.md"><meta property="og:title" content="Getting started · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create your first D1 database, define a schema, and query it from a Cloudflare Worker."><meta property="og:url" content="https://developers.cloudflare.com/d1/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/get-started/#page","headline":"Getting started \u00b7 Cloudflare D1 docs","description":"Create your first D1 database, define a schema, and query it from a Cloudflare Worker.","url":"https://developers.cloudflare.com/d1/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/get-started/
  schema: 1
---
<p>This guide instructs you through:</p>
<ul>
<li>Creating your first database using D1, Cloudflare's native serverless SQL database.</li>
<li>Creating a schema and querying your database via the command-line.</li>
<li>Connecting a <a href="/workers/">Cloudflare Worker</a> to your D1 database using bindings, and querying your D1 database programmatically.</li>
</ul>
<p>You can perform these tasks through the CLI or through the Cloudflare dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1189.md")
</aside>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the steps and get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/d1-get-started/d1/d1-get-started"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers. Use this option if you are familiar with Cloudflare Workers, and wish to skip the step-by-step guidance.</p>
<p>You may wish to manually follow the steps if you are new to Cloudflare Workers.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1190.md")
</div></details>
<h2 id="1-create-a-worker"><ol>
<li>Create a Worker</li>
</ol></h2>
<p>Create a new Worker as the means to query your database.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1196.md")
</div></div>
<h2 id="2-create-a-database"><ol start="2">
<li>Create a database</li>
</ol></h2>
<p>A D1 database is conceptually similar to many other SQL databases: a database may contain one or more tables, the ability to query those tables, and optional indexes. D1 uses the familiar <a href="https://www.sqlite.org/lang.html">SQL query language</a> (as used by SQLite).</p>
<p>To create your first D1 database:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1201.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1186.md")
</aside>
<h2 id="3-bind-your-worker-to-your-d1-database"><ol start="3">
<li>Bind your Worker to your D1 database</li>
</ol></h2>
<p>You must create a binding for your Worker to connect to your D1 database. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like D1, on the Cloudflare developer platform.</p>
<p>To bind your D1 database to your Worker:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1207.md")
</div></div>
<h2 id="4-run-a-query-against-your-d1-database"><ol start="4">
<li>Run a query against your D1 database</li>
</ol></h2>
<h3 id="populate-your-d1-database">Populate your D1 database</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1212.md")
</div></div>
<h3 id="write-queries-within-your-worker">Write queries within your Worker</h3>
<p>After you have set up your database, run an SQL query from within your Worker.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1220.md")
</div></div>
<h2 id="5-deploy-your-application"><ol start="5">
<li>Deploy your application</li>
</ol></h2>
<p>Deploy your application on Cloudflare's global network.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1225.md")
</div></div>
<h2 id="6-optional-develop-locally-with-wrangler"><ol start="6">
<li>(Optional) Develop locally with Wrangler</li>
</ol></h2>
<p>If you are using D1 with Wrangler, you can test your database locally. While in your project directory:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1226.md")
</div>
<p>If successful, the browser displays your data.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1183.md")
</aside>
<h2 id="7-optional-delete-your-database"><ol start="7">
<li>(Optional) Delete your database</li>
</ol></h2>
<p>To delete your database:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1230.md")
</div></div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1182.md")
</aside>
<p>If you want to delete your Worker:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1234.md")
</div></div>
<h2 id="summary">Summary</h2>
<p>In this tutorial, you have:</p>
<ul>
<li>Created a D1 database</li>
<li>Created a Worker to access that database</li>
<li>Deployed your project globally</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p>If you have any feature requests or notice any bugs, share your feedback directly with the Cloudflare team by joining the <a href="https://discord.cloudflare.com">Cloudflare Developers community on Discord</a>.</p>
<ul>
<li>See supported <a href="/workers/wrangler/commands/d1/">Wrangler commands for D1</a>.</li>
<li>Learn how to use <a href="/d1/worker-api/">D1 Worker Binding APIs</a> within your Worker, and test them from the <a href="/d1/worker-api/#api-playground">API playground</a>.</li>
<li>Explore <a href="/d1/reference/community-projects/">community projects built on D1</a>.</li>
</ul>
