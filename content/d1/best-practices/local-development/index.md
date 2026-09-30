---
cp9:
  canonical: https://developers.cloudflare.com/d1/best-practices/local-development/
  description: Run D1 locally with Wrangler to test your Worker and database before deploying to production.
  full_title: Local development · Cloudflare D1 docs
  head_html: <title>Local development · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Run D1 locally with Wrangler to test your Worker and database before deploying to production."><link rel="canonical" href="https://developers.cloudflare.com/d1/best-practices/local-development/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/best-practices/local-development/index.md"><meta property="og:title" content="Local development · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run D1 locally with Wrangler to test your Worker and database before deploying to production."><meta property="og:url" content="https://developers.cloudflare.com/d1/best-practices/local-development/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/best-practices/local-development/#page","headline":"Local development \u00b7 Cloudflare D1 docs","description":"Run D1 locally with Wrangler to test your Worker and database before deploying to production.","url":"https://developers.cloudflare.com/d1/best-practices/local-development/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/best-practices/local-development/
  schema: 1
---
<p>D1 has fully-featured support for local development, running the same version of D1 as Cloudflare runs globally. Local development uses <a href="/workers/wrangler/install-and-update/">Wrangler</a>, the command-line interface for Workers, to manage local development sessions and state.</p>
<h2 id="start-a-local-development-session">Start a local development session</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7401.md")
</aside>
<p>Local development sessions create a standalone, local-only environment that mirrors the production environment D1 runs in so that you can test your Worker and D1 <em>before</em> you deploy to production.</p>
<p>An existing <a href="/workers/wrangler/configuration/#d1-databases">D1 binding</a> of <code>DB</code> would be available to your Worker when running locally.</p>
<p>To start a local development session:</p>
<ol>
<li>Confirm you are using wrangler v3.0+.</li>
</ol>
<pre tabindex="0"><code class="language-sh">wrangler --version&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">⛅️ wrangler 3.0.0&#10;</code></pre>
<ol start="2">
<li>Start a local development session</li>
</ol>
<pre tabindex="0"><code class="language-sh">wrangler dev&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#45;-----------------&#10;wrangler dev now uses local mode by default, powered by 🔥 Miniflare and 👷 workerd.&#10;To run an edge preview session for your Worker, use wrangler dev --remote&#10;Your worker has access to the following bindings:&#10;&#45; D1 Databases:&#10;	&#45; DB: test-db (c020574a-5623-407b-be0c-cd192bab9545)&#10;⎔ Starting local server...&#10;&#10;[mf:inf] Ready on http://127.0.0.1:8787/&#10;[b] open a browser, [d] open Devtools, [l] turn off local mode, [c] clear console, [x] to exit&#10;</code></pre>
<p>In this example, the Worker has access to local-only D1 database. The corresponding D1 binding in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> would resemble the following:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7402.md")
</div>
<p>Note that <code>wrangler dev</code> separates local and production (remote) data. A local session does not have access to your production data by default. To access your production (remote) database, set <code>&quot;remote&quot; : true</code> in the D1 binding configuration. Refer to the <a href="/workers/local-development/#remote-bindings">remote bindings documentation</a> for more information. Any changes you make when running against a remote database cannot be undone.</p>
<p>Refer to the <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code> documentation</a> to learn more about how to configure a local development session.</p>
<h2 id="develop-locally-with-pages">Develop locally with Pages</h2>
<p>You can only develop against a <em>local</em> D1 database when using <a href="/pages/">Cloudflare Pages</a> by creating a minimal <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> in the root of your Pages project. This can be useful when creating schemas, seeding data or otherwise managing a D1 database directly, without adding to your application logic.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="local-development-for-remote-databases">Local development for remote databases</h3>
@markup("md", "content/.markup/bodies/7400.md")
</aside>
<p>Your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> should resemble the following:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7403.md")
</div>
<p>You can then execute queries and/or run migrations against a local database as part of your local development process by passing the <code>--local</code> flag to wrangler:</p>
<pre tabindex="0"><code class="language-bash">wrangler d1 execute YOUR_DATABASE_NAME \&#10;  &#45;-local --command &quot;CREATE TABLE IF NOT EXISTS users ( user_id INTEGER PRIMARY KEY, email_address TEXT, created_at INTEGER, deleted INTEGER, settings TEXT);&quot;&#10;</code></pre>
<p>The preceding command would execute queries the <strong>local only</strong> version of your D1 database. Without the <code>--local</code> flag, the commands are executed against the remote version of your D1 database running on Cloudflare's network.</p>
<h2 id="persist-data">Persist data</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7399.md")
</aside>
<p>Use <code>wrangler dev --persist-to=/path/to/file</code> to persist data to a specific location. This can be useful when working in a team (allowing you to share) the same copy, when deploying via CI/CD (to ensure the same starting state), or as a way to keep data when migrating across machines.</p>
<p>Users of wrangler <code>2.x</code> must use the <code>--persist</code> flag: previous versions of wrangler did not persist data by default.</p>
<h2 id="test-programmatically">Test programmatically</h2>
<h3 id="miniflare">Miniflare</h3>
<p><a href="https://miniflare.dev/">Miniflare</a> allows you to simulate a Workers and resources like D1 using the same underlying runtime and code as used in production.</p>
<p>You can use Miniflare's <a href="https://miniflare.dev/storage/d1">support for D1</a> to create D1 databases you can use for testing:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7404.md")
</div>
<pre tabindex="0"><code class="language-js">const mf = new Miniflare({&#10;	d1Databases: {&#10;		DB: &quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>You can then use the <code>getD1Database()</code> method to retrieve the simulated database and run queries against it as if it were your real production D1 database:</p>
<pre tabindex="0"><code class="language-js">const db = await mf.getD1Database(&quot;DB&quot;);&#10;&#10;const stmt = db.prepare(&quot;SELECT name, age FROM users LIMIT 3&quot;);&#10;const { results } = await stmt.run();&#10;&#10;console.log(results);&#10;</code></pre>
<h3 id="unstable-dev"><code>unstable_dev</code></h3>
<p>Wrangler exposes an <a href="/workers/wrangler/api/"><code>unstable_dev()</code></a> that allows you to run a local HTTP server for testing Workers and D1. Run <a href="/d1/reference/migrations/">migrations</a> against a local database by setting a <code>preview_database_id</code> in your Wrangler configuration.</p>
<p>Given the below Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7405.md")
</div>
<p>Migrations can be run locally as part of your CI/CD setup by passing the <code>--local</code> flag to <code>wrangler</code>:</p>
<pre tabindex="0"><code class="language-sh">wrangler d1 migrations apply your-database --local&#10;</code></pre>
<h3 id="usage-example">Usage example</h3>
<p>The following example shows how to use Wrangler's <code>unstable_dev()</code> API to:</p>
<ul>
<li>Run migrations against your local test database, as defined by <code>preview_database_id</code>.</li>
<li>Make a request to an endpoint defined in your Worker. This example uses <code>/api/users/?limit=2</code>.</li>
<li>Validate the returned results match, including the <code>Response.status</code> and the JSON our API returns.</li>
</ul>
<pre tabindex="0"><code class="language-ts">import { unstable_dev } from &quot;wrangler&quot;;&#10;import type { UnstableDevWorker } from &quot;wrangler&quot;;&#10;&#10;describe(&quot;Test D1 Worker endpoint&quot;, () =&gt; {&#10;	let worker: UnstableDevWorker;&#10;&#10;	beforeAll(async () =&gt; {&#10;		// Optional: Run any migrations to set up your `--local` database&#10;		// By default, this will default to the preview_database_id&#10;		execSync(`NO_D1_WARNING=true wrangler d1 migrations apply db --local`);&#10;&#10;		worker = await unstable_dev(&quot;src/index.ts&quot;, {&#10;			experimental: { disableExperimentalWarning: true },&#10;		});&#10;	});&#10;&#10;	afterAll(async () =&gt; {&#10;		await worker.stop();&#10;	});&#10;&#10;	it(&quot;should return an array of users&quot;, async () =&gt; {&#10;		// Our expected results&#10;		const expectedResults = `{&quot;results&quot;: [{&quot;user_id&quot;: 1234, &quot;email&quot;: &quot;foo@example.com&quot;},{&quot;user_id&quot;: 6789, &quot;email&quot;: &quot;bar@example.com&quot;}]}`;&#10;		// Pass an optional URL to fetch to trigger any routing within your Worker&#10;		const resp = await worker.fetch(&quot;/api/users/?limit=2&quot;);&#10;		if (resp) {&#10;			// https://jestjs.io/docs/expect#tobevalue&#10;			expect(resp.status).toBe(200);&#10;			const data = await resp.json();&#10;			// https://jestjs.io/docs/expect#tomatchobjectobject&#10;			expect(data).toMatchObject(expectedResults);&#10;		}&#10;	});&#10;});&#10;</code></pre>
<p>Review the <a href="/workers/wrangler/api/#usage"><code>unstable_dev()</code></a> documentation for more details on how to use the API within your tests.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Use <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> to run your Worker and D1 locally and debug issues before deploying.</li>
<li>Learn <a href="/d1/observability/debug-d1/">how to debug D1</a>.</li>
<li>Understand how to <a href="/workers/observability/logs/">access logs</a> generated from your Worker and D1.</li>
</ul>
