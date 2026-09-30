---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/
  description: Use Drizzle ORM with Hyperdrive to query PostgreSQL databases from Cloudflare Workers.
  full_title: Drizzle ORM · Cloudflare Hyperdrive docs
  head_html: <title>Drizzle ORM · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Drizzle ORM with Hyperdrive to query PostgreSQL databases from Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/index.md"><meta property="og:title" content="Drizzle ORM · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Drizzle ORM with Hyperdrive to query PostgreSQL databases from Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Hyperdrive,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/#page","headline":"Drizzle ORM \u00b7 Cloudflare Hyperdrive docs","description":"Use Drizzle ORM with Hyperdrive to query PostgreSQL databases from Cloudflare Workers.","url":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/drizzle-orm/
  schema: 1
---
<p><a href="https://orm.drizzle.team/">Drizzle ORM</a> is a lightweight TypeScript ORM with a focus on type safety. This example demonstrates how to use Drizzle ORM with PostgreSQL via Cloudflare Hyperdrive in a Workers application.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account with Workers access</li>
<li>A PostgreSQL database</li>
<li>A <a href="/hyperdrive/get-started/#3-connect-hyperdrive-to-a-database">Hyperdrive configuration to your PostgreSQL database</a></li>
</ul>
<h2 id="1-install-drizzle"><ol>
<li>Install Drizzle</li>
</ol></h2>
<p>Install the Drizzle ORM and its dependencies such as the <a href="https://node-postgres.com/">node-postgres</a> (<code>pg</code>) driver:</p>
<pre tabindex="0"><code class="language-sh">npm i drizzle-orm pg dotenv&#10;npm i -D drizzle-kit tsx @types/pg @types/node&#10;</code></pre>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9173.md")
</div>
<h2 id="2-configure-drizzle"><ol start="2">
<li>Configure Drizzle</li>
</ol></h2>
<h3 id="2-1-define-a-schema">2.1. Define a schema</h3>
<p>With Drizzle ORM, we define the schema in TypeScript rather than writing raw SQL.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9174.md")
</div>
<h3 id="2-2-connect-drizzle-orm-to-the-database-with-hyperdrive">2.2. Connect Drizzle ORM to the database with Hyperdrive</h3>
<p>Use your Hyperdrive configuration for your database when using the Drizzle ORM.</p>
<p>Populate your <code>index.ts</code> file as shown below.</p>
<pre tabindex="0"><code class="language-ts">// src/index.ts&#10;import { Client } from &quot;pg&quot;;&#10;import { drizzle } from &quot;drizzle-orm/node-postgres&quot;;&#10;import { users } from &quot;./db/schema&quot;;&#10;&#10;export interface Env {&#10;	HYPERDRIVE: Hyperdrive;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new client instance for each request.&#10;		const client = new Client({&#10;			connectionString: env.HYPERDRIVE.connectionString,&#10;		});&#10;&#10;		// Connect to the database&#10;		await client.connect();&#10;&#10;		// Create the Drizzle client with the node-postgres connection&#10;		const db = drizzle(client);&#10;&#10;		// Sample query to get all users&#10;		const allUsers = await db.select().from(users);&#10;&#10;		return Response.json(allUsers);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9172.md")
</aside>
<h3 id="2-3-configure-drizzle-kit-for-migrations-optional">2.3. Configure Drizzle-Kit for migrations (optional)</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9171.md")
</aside>
<p>You can generate and run SQL migrations on your database based on your schema using Drizzle Kit CLI. Refer to <a href="https://orm.drizzle.team/docs/get-started/postgresql-new">Drizzle ORM docs</a> for additional guidance.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9175.md")
</div>
<h2 id="3-deploy-your-worker"><ol start="3">
<li>Deploy your Worker</li>
</ol></h2>
<p>Deploy your Worker.</p>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
