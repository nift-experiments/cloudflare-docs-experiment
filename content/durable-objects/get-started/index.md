---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/get-started/
  description: Create and deploy your first Durable Object with SQLite storage and a companion Worker.
  full_title: Getting started · Cloudflare Durable Objects docs
  head_html: <title>Getting started · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Create and deploy your first Durable Object with SQLite storage and a companion Worker."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/get-started/index.md"><meta property="og:title" content="Getting started · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create and deploy your first Durable Object with SQLite storage and a companion Worker."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/get-started/#page","headline":"Getting started \u00b7 Cloudflare Durable Objects docs","description":"Create and deploy your first Durable Object with SQLite storage and a companion Worker.","url":"https://developers.cloudflare.com/durable-objects/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/get-started/
  schema: 1
---
<p>This guide will instruct you through:</p>
<ul>
<li>Writing a JavaScript class that defines a Durable Object.</li>
<li>Using Durable Objects SQL API to query a Durable Object's private, embedded SQLite database.</li>
<li>Instantiating and communicating with a Durable Object from another Worker.</li>
<li>Deploying a Durable Object and a Worker that communicates with a Durable Object.</li>
</ul>
<p>If you wish to learn more about Durable Objects, refer to <a href="/durable-objects/concepts/what-are-durable-objects/">What are Durable Objects?</a>.</p>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the steps and get started quickly, click on the button below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/hello-world-do-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers. Use this option if you are familiar with Cloudflare Workers, and wish to skip the step-by-step guidance.</p>
<p>You may wish to manually follow the steps if you are new to Cloudflare Workers.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1099.md")
</div></details>
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>You will access your Durable Object from a <a href="/workers/">Worker</a>. Your Worker application is an interface to interact with your Durable Object.</p>
<p>To create a Worker project, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- durable-object-starter</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- durable-object-starter" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare durable-object-starter</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare durable-object-starter" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest durable-object-starter</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest durable-object-starter" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Running <code>create cloudflare@latest</code> will install <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the Workers CLI. You will use Wrangler to test and deploy your project.</p>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker + Durable Objects</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>This will create a new directory, which will include either a <code>src/index.js</code> or <code>src/index.ts</code> file to write your code and a <a href="/workers/wrangler/configuration/"><code>wrangler.jsonc</code></a> configuration file.</p>
<p>Move into your new directory:</p>
<pre tabindex="0"><code class="language-sh">cd durable-object-starter&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="adding-a-durable-object-to-an-existing-worker">Adding a Durable Object to an existing Worker</h3>
@markup("md", "content/.markup/bodies/1098.md")
</aside>
<h2 id="2-write-a-durable-object-class-using-sql-api"><ol start="2">
<li>Write a Durable Object class using SQL API</li>
</ol></h2>
<p>Before you create and access a Durable Object, its behavior must be defined by an ordinary exported JavaScript class.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1097.md")
</aside>
<p>Your <code>MyDurableObject</code> class will have a constructor with two parameters. The first parameter, <code>ctx</code>, passed to the class constructor contains state specific to the Durable Object, including methods for accessing storage. The second parameter, <code>env</code>, contains any bindings you have associated with the Worker when you uploaded it.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1102.md")
</div></div>
<p>Workers communicate with a Durable Object using <a href="/workers/runtime-apis/rpc/#_top">remote-procedure call</a>. Public methods on a Durable Object class are exposed as <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/">RPC methods</a> to be called by another Worker.</p>
<p>Your file should now look like:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1105.md")
</div></div>
<p>In the code above, you have:</p>
<ol>
<li>Defined a RPC method, <code>sayHello()</code>, that can be called by a Worker to communicate with a Durable Object.</li>
<li>Accessed a Durable Object's attached storage, which is a private SQLite database only accessible to the object, using <a href="/durable-objects/api/sqlite-storage-api/#exec">SQL API</a> methods (<code>sql.exec()</code>) available on <code>ctx.storage</code> .</li>
<li>Returned an object representing the single row query result using <code>one()</code>, which checks that the query result has exactly one row.</li>
<li>Return the <code>greeting</code> column from the row object result.</li>
</ol>
<h2 id="3-instantiate-and-communicate-with-a-durable-object"><ol start="3">
<li>Instantiate and communicate with a Durable Object</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1096.md")
</aside>
<p>A Worker is used to <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/">access Durable Objects</a>.</p>
<p>To communicate with a Durable Object, the Worker's fetch handler should look like the following:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1108.md")
</div></div>
<p>In the code above, you have:</p>
<ol>
<li>Exported your Worker's main event handlers, such as the <code>fetch()</code> handler for receiving HTTP requests.</li>
<li>Passed <code>env</code> into the <code>fetch()</code> handler. Bindings are delivered as a property of the environment object passed as the second parameter when an event handler or class constructor is invoked.</li>
<li>Constructed a stub for a Durable Object instance based on the provided name. A stub is a client object used to send messages to the Durable Object.</li>
<li>Called a Durable Object by invoking a RPC method, <code>sayHello()</code>, on the Durable Object, which returns a <code>Hello, World!</code> string greeting.</li>
<li>Received an HTTP response back to the client by constructing a HTTP Response with <code>return new Response()</code>.</li>
</ol>
<p>Refer to <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/">Access a Durable Object from a Worker</a> to learn more about communicating with a Durable Object.</p>
<h2 id="4-configure-durable-object-bindings"><ol start="4">
<li>Configure Durable Object bindings</li>
</ol></h2>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to interact with resources on the Cloudflare developer platform. The Durable Object bindings in your Worker project's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> will include a binding name (for this guide, use <code>MY_DURABLE_OBJECT</code>) and the class name (<code>MyDurableObject</code>).</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1109.md")
</div>
<p>The <code>bindings</code> section contains the following fields:</p>
<ul>
<li><code>name</code> - Required. The binding name to use within your Worker.</li>
<li><code>class_name</code> - Required. The class name you wish to bind to.</li>
<li><code>script_name</code> - Optional. Defaults to the current <a href="/durable-objects/reference/environments/">environment's</a> Worker code.</li>
</ul>
<h2 id="5-configure-durable-object-class-with-sqlite-storage-backend"><ol start="5">
<li>Configure Durable Object class with SQLite storage backend</li>
</ol></h2>
<p>You declare each Durable Object class your Worker exports in the <code>exports</code> field of your Wrangler configuration file. Cloudflare uses this declaration to provision a namespace for the class the first time you deploy, and to manage its lifecycle on later deploys (rename, delete, transfer).</p>
<p>The minimal <code>exports</code> block to register a new Durable Object class with SQLite storage looks like:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1110.md")
</div>
<p>Refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Object class exports</a> to learn more about declaring and managing Durable Object classes. If you have an existing Worker on the legacy <code>migrations</code> array, refer to <a href="/durable-objects/reference/durable-object-class-migrations-legacy/">Durable Object class migrations (legacy)</a>.</p>
<h2 id="6-develop-a-durable-object-worker-locally"><ol start="6">
<li>Develop a Durable Object Worker locally</li>
</ol></h2>
<p>To test your Durable Object locally, run <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>In your console, you should see a<code>Hello world</code> string returned by the Durable Object.</p>
<h2 id="7-deploy-your-durable-object-worker"><ol start="7">
<li>Deploy your Durable Object Worker</li>
</ol></h2>
<p>To deploy your Durable Object Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Once deployed, you should be able to see your newly created Durable Object Worker on the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>Preview your Durable Object Worker at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<h2 id="summary-and-final-code">Summary and final code</h2>
<p>Your final code should look like this:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1113.md")
</div></div>
<p>By finishing this tutorial, you have:</p>
<ul>
<li>Successfully created a Durable Object</li>
<li>Called the Durable Object by invoking a <a href="/workers/runtime-apis/rpc/">RPC method</a></li>
<li>Deployed the Durable Object globally</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/">Create Durable Object stubs</a></li>
<li><a href="/durable-objects/best-practices/access-durable-objects-storage/">Access Durable Objects Storage</a></li>
<li><a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/miniflare">Miniflare</a> - Helpful tools for mocking and testing your Durable Objects.</li>
</ul>
