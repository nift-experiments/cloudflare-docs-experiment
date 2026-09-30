---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/
  description: Use Prisma ORM with Hyperdrive to query PostgreSQL databases from Cloudflare Workers.
  full_title: Prisma ORM · Cloudflare Hyperdrive docs
  head_html: <title>Prisma ORM · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Prisma ORM with Hyperdrive to query PostgreSQL databases from Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/index.md"><meta property="og:title" content="Prisma ORM · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Prisma ORM with Hyperdrive to query PostgreSQL databases from Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Hyperdrive,Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/#page","headline":"Prisma ORM \u00b7 Cloudflare Hyperdrive docs","description":"Use Prisma ORM with Hyperdrive to query PostgreSQL databases from Cloudflare Workers.","url":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/examples/connect-to-postgres/postgres-drivers-and-libraries/prisma-orm/
  schema: 1
---
<p><a href="https://www.prisma.io/docs">Prisma ORM</a> is a Node.js and TypeScript ORM with a focus on type safety and developer experience. This example demonstrates how to use Prisma ORM with PostgreSQL via Cloudflare Hyperdrive in a Workers application.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account with Workers access</li>
<li>A PostgreSQL database (such as <a href="https://www.prisma.io/postgres">Prisma Postgres</a>)</li>
<li>A <a href="/hyperdrive/get-started/#3-connect-hyperdrive-to-a-database">Hyperdrive configuration to your PostgreSQL database</a></li>
<li>An existing <a href="/workers/get-started/guide/">Worker project</a></li>
</ul>
<h2 id="1-install-prisma-orm"><ol>
<li>Install Prisma ORM</li>
</ol></h2>
<p>Install Prisma CLI as a dev dependency:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add prisma" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Install the <code>pg</code> driver and Prisma driver adapter for use with Hyperdrive:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i pg@&gt;8.13.0 @prisma/adapter-pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i pg@&gt;8.13.0 @prisma/adapter-pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add pg@&gt;8.13.0 @prisma/adapter-pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add pg@&gt;8.13.0 @prisma/adapter-pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add pg@&gt;8.13.0 @prisma/adapter-pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add pg@&gt;8.13.0 @prisma/adapter-pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add pg@&gt;8.13.0 @prisma/adapter-pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add pg@&gt;8.13.0 @prisma/adapter-pg" aria-label="Copy to clipboard">Copy</button></div></div>
<p>If using TypeScript, install the types package:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @types/pg" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9164.md")
</div>
<h2 id="2-configure-prisma-orm"><ol start="2">
<li>Configure Prisma ORM</li>
</ol></h2>
<h3 id="2-1-initialize-prisma">2.1. Initialize Prisma</h3>
<p>Initialize Prisma in your application:</p>
<pre tabindex="0"><code class="language-sh">npx prisma init&#10;</code></pre>
<p>This creates a <code>prisma</code> folder with a <code>schema.prisma</code> file and an <code>.env</code> file.</p>
<h3 id="2-2-define-a-schema">2.2. Define a schema</h3>
<p>Define your database schema in the <code>prisma/schema.prisma</code> file:</p>
<pre tabindex="0"><code class="language-prisma">generator client {&#10;  provider        = &quot;prisma-client-js&quot;&#10;  previewFeatures = [&quot;driverAdapters&quot;]&#10;}&#10;&#10;datasource db {&#10;  provider = &quot;postgresql&quot;&#10;  url      = env(&quot;DATABASE_URL&quot;)&#10;}&#10;&#10;model User {&#10;  id        Int      @id @default(autoincrement())&#10;  name      String&#10;  email     String   @unique&#10;  createdAt DateTime @default(now())&#10;}&#10;</code></pre>
<h3 id="2-3-set-up-environment-variables">2.3. Set up environment variables</h3>
<p>Add your database connection string to the <code>.env</code> file created by Prisma:</p>
<pre tabindex="0"><code class="language-txt">DATABASE_URL=&quot;postgres://user:password@host:port/database&quot;&#10;</code></pre>
<p>Add helper scripts to your <code>package.json</code>:</p>
<pre tabindex="0"><code class="language-json">&quot;scripts&quot;: {&#10;  &quot;migrate&quot;: &quot;npx prisma migrate dev&quot;,&#10;  &quot;generate&quot;: &quot;npx prisma generate --no-engine&quot;,&#10;  &quot;studio&quot;: &quot;npx prisma studio&quot;&#10;}&#10;</code></pre>
<h3 id="2-4-generate-prisma-client">2.4. Generate Prisma Client</h3>
<p>Generate the Prisma client with driver adapter support:</p>
<pre tabindex="0"><code class="language-sh">npm run generate&#10;</code></pre>
<h3 id="2-5-run-migrations">2.5. Run migrations</h3>
<p>Generate and apply the database schema:</p>
<pre tabindex="0"><code class="language-sh">npm run migrate&#10;</code></pre>
<p>When prompted, provide a name for the migration (for example, <code>init</code>).</p>
<h2 id="3-connect-prisma-orm-to-hyperdrive"><ol start="3">
<li>Connect Prisma ORM to Hyperdrive</li>
</ol></h2>
<p>Use your Hyperdrive configuration when using Prisma ORM. Update your <code>src/index.ts</code> file:</p>
<pre tabindex="0"><code class="language-ts">import { PrismaPg } from &quot;@prisma/adapter-pg&quot;;&#10;import { PrismaClient } from &quot;@prisma/client&quot;;&#10;&#10;export interface Env {&#10;	HYPERDRIVE: Hyperdrive;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create Prisma client using driver adapter with Hyperdrive connection string&#10;		const adapter = new PrismaPg({ connectionString: env.HYPERDRIVE.connectionString });&#10;		const prisma = new PrismaClient({ adapter });&#10;&#10;		// Sample query to create and fetch users&#10;		const user = await prisma.user.create({&#10;			data: {&#10;				name: &quot;John Doe&quot;,&#10;				email: `john.doe.${Date.now()}@example.com`,&#10;			},&#10;		});&#10;&#10;		const allUsers = await prisma.user.findMany();&#10;&#10;		return Response.json({&#10;			newUser: user,&#10;			allUsers: allUsers,&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9163.md")
</aside>
<h2 id="4-deploy-your-worker"><ol start="4">
<li>Deploy your Worker</li>
</ol></h2>
<p>Deploy your Worker:</p>
<pre tabindex="0"><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
