---
cp9:
  canonical: https://developers.cloudflare.com/d1/tutorials/d1-and-prisma-orm/
  description: This tutorial shows you how to set up and deploy a Cloudflare Worker that is accessing a D1 database from scratch.
  full_title: Query D1 using Prisma ORM · Cloudflare D1 docs
  head_html: <title>Query D1 using Prisma ORM · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial shows you how to set up and deploy a Cloudflare Worker that is accessing a D1 database from scratch."><link rel="canonical" href="https://developers.cloudflare.com/d1/tutorials/d1-and-prisma-orm/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/tutorials/d1-and-prisma-orm/index.md"><meta property="og:title" content="Query D1 using Prisma ORM · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial shows you how to set up and deploy a Cloudflare Worker that is accessing a D1 database from scratch."><meta property="og:url" content="https://developers.cloudflare.com/d1/tutorials/d1-and-prisma-orm/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="TypeScript,SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/tutorials/d1-and-prisma-orm/#page","headline":"Query D1 using Prisma ORM \u00b7 Cloudflare D1 docs","description":"This tutorial shows you how to set up and deploy a Cloudflare Worker that is accessing a D1 database from scratch.","url":"https://developers.cloudflare.com/d1/tutorials/d1-and-prisma-orm/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TypeScript","SQL"]}</script>
  markdown: true
  noindex: false
  route: /d1/tutorials/d1-and-prisma-orm/
  schema: 1
---
<h2 id="what-is-prisma-orm">What is Prisma ORM?</h2>
<p><a href="https://www.prisma.io/orm">Prisma ORM</a> is a next-generation JavaScript and TypeScript ORM that unlocks a new level of developer experience when working with databases thanks to its intuitive data model, automated migrations, type-safety and auto-completion.</p>
<p>To learn more about Prisma ORM, refer to the <a href="https://www.prisma.io/docs">Prisma documentation</a>.</p>
<h2 id="query-d1-from-a-cloudflare-worker-using-prisma-orm">Query D1 from a Cloudflare Worker using Prisma ORM</h2>
<p>This tutorial shows you how to set up and deploy a Cloudflare Worker that is accessing a D1 database from scratch.</p>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the steps and get started quickly, select <strong>Deploy to Cloudflare</strong> below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/d1-prisma/d1/query-d1-using-prisma"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers. Use this option if you are familiar with Cloudflare Workers, and wish to skip the step-by-step guidance.</p>
<p>You may wish to manually follow the steps if you are new to Cloudflare Workers.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="https://nodejs.org/en/"><code>Node.js</code></a> and <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a> installed on your machine.</li>
<li>A <a href="https://dash.cloudflare.com">Cloudflare account</a>.</li>
</ul>
<h2 id="1-create-a-cloudflare-worker"><ol>
<li>Create a Cloudflare Worker</li>
</ol></h2>
<p>Open your terminal, and run the following command to create a Cloudflare Worker using Cloudflare's <a href="https://github.com/cloudflare/workers-sdk/tree/4fdd8987772d914cf50725e9fa8cb91a82a6870d/packages/create-cloudflare/templates/hello-world"><code>hello-world</code></a> template:</p>
<pre tabindex="0"><code class="language-sh">npm create cloudflare@latest prisma-d1-example -- --type hello-world&#10;</code></pre>
<p>In your terminal, you will be asked a series of questions related your project:</p>
<ol>
<li>Answer <code>yes</code> to using TypeScript.</li>
<li>Answer <code>no</code> to deploying your Worker.</li>
</ol>
<h2 id="2-initialize-prisma-orm"><ol start="2">
<li>Initialize Prisma ORM</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7282.md")
</aside>
<p>To set up Prisma ORM, go into your project directory, and install the Prisma CLI:</p>
<pre tabindex="0"><code class="language-sh">cd prisma-d1-example&#10;</code></pre>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add prisma" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Next, install the Prisma Client package and the driver adapter for D1:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @prisma/client @prisma/adapter-d1</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @prisma/client @prisma/adapter-d1" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @prisma/client @prisma/adapter-d1</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @prisma/client @prisma/adapter-d1" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @prisma/client @prisma/adapter-d1</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @prisma/client @prisma/adapter-d1" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @prisma/client @prisma/adapter-d1</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @prisma/client @prisma/adapter-d1" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Finally, bootstrap the files required by Prisma ORM using the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx prisma init --datasource-provider sqlite</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx prisma init --datasource-provider sqlite" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn prisma init --datasource-provider sqlite</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn prisma init --datasource-provider sqlite" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm prisma init --datasource-provider sqlite</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm prisma init --datasource-provider sqlite" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The command above:</p>
<ol>
<li>Creates a new directory called <code>prisma</code> that contains your <a href="https://www.prisma.io/docs/orm/prisma-schema/overview">Prisma schema</a> file.</li>
<li>Creates a <code>.env</code> file used to configure environment variables that will be read by the Prisma CLI.</li>
</ol>
<p>In this tutorial, you will not need the <code>.env</code> file since the connection between Prisma ORM and D1 will happen through a <a href="/workers/runtime-apis/bindings/">binding</a>. The next steps will instruct you through setting up this binding.</p>
<p>Since you will use the <a href="https://www.prisma.io/docs/orm/overview/databases/database-drivers#driver-adapters">driver adapter</a> feature which is currently in Preview, you need to explicitly enable it via the <code>previewFeatures</code> field on the <code>generator</code> block.</p>
<p>Open your <code>schema.prisma</code> file and adjust the <code>generator</code> block to reflect as follows:</p>
<pre tabindex="0"><code class="language-prisma">generator client {&#10;  provider        = &quot;prisma-client-js&quot;&#10;  output          = &quot;../src/generated/prisma&quot;&#10;  previewFeatures = [&quot;driverAdapters&quot;]&#10;}&#10;</code></pre>
<h2 id="3-create-your-d1-database"><ol start="3">
<li>Create your D1 database</li>
</ol></h2>
<p>In this step, you will set up your D1 database. You can create a D1 database via the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, or via <code>wrangler</code>. This tutorial will use the <code>wrangler</code> CLI.</p>
<p>Open your terminal and run the following command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 create prisma-demo-db&#10;</code></pre>
<p>You should receive the following output on your terminal:</p>
<pre tabindex="0"><code>✅ Successfully created DB &#x27;prisma-demo-db&#x27; in region WEUR&#10;Created your new D1 database.&#10;&#10;{&#10;  &quot;d1_databases&quot;: [&#10;    {&#10;      &quot;binding&quot;: &quot;DB&quot;,&#10;      &quot;database_name&quot;: &quot;prisma-demo-db&quot;,&#10;      &quot;database_id&quot;: &quot;&lt;D1_DATABASE_ID&gt;&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>You now have a D1 database in your Cloudflare account with a binding to your Cloudflare Worker.</p>
<p>Copy the last part of the command output and paste it into your Wrangler file. It should look similar to this:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7283.md")
</div>
<p>Replace <code>&lt;D1_DATABASE_ID&gt;</code> with the database ID of your D1 instance. If you were not able to fetch this ID from the terminal output, you can also find it in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, or by running <code>npx wrangler d1 info prisma-demo-db</code> in your terminal.</p>
<p>Next, you will create a database table in the database to send queries to D1 using Prisma ORM.</p>
<h2 id="4-create-a-table-in-the-database"><ol start="4">
<li>Create a table in the database</li>
</ol></h2>
<p><a href="https://www.prisma.io/docs/orm/prisma-migrate/understanding-prisma-migrate/overview">Prisma Migrate</a> does not support D1 yet, so you cannot follow the default migration workflows using <code>prisma migrate dev</code> or <code>prisma db push</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7281.md")
</aside>
<p>D1 uses <a href="/d1/reference/migrations">migrations</a> for managing schema changes, and the Prisma CLI can help generate the necessary SQL for those updates. In the steps below, you will use both tools to create and apply a migration to your database.</p>
<p>First, create a new migration using <code>wrangler</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler d1 migrations create prisma-demo-db create_user_table&#10;</code></pre>
<p>Answer <code>yes</code> to creating a new folder called <code>migrations</code>.</p>
<p>The command has now created a new directory called <code>migrations</code> and an empty file called <code>0001_create_user_table.sql</code> inside of it:</p>
<pre tabindex="0" class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/7284.md")&#10;&#10;&#10;</pre>
<p>Next, you need to add the SQL statement that will create a <code>User</code> table to that file.</p>
<p>Open the <code>schema.prisma</code> file and add the following <code>User</code> model to your schema:</p>
<pre tabindex="0"><code class="language-prisma">model User {&#10;  id    Int     @id @default(autoincrement())&#10;  email String  @unique&#10;  name  String?&#10;}&#10;</code></pre>
<p>Now, run the following command in your terminal to generate the SQL statement that creates a <code>User</code> table equivalent to the <code>User</code> model above:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="prisma"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7287.md")
</div></div>
<p>This stores a SQL statement to create a new <code>User</code> table in your migration file from before, here is what it looks like:</p>
<pre tabindex="0"><code class="language-sql">&#45;- CreateTable&#10;CREATE TABLE &quot;User&quot; (&#10;    &quot;id&quot; INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,&#10;    &quot;email&quot; TEXT NOT NULL,&#10;    &quot;name&quot; TEXT&#10;);&#10;&#10;&#45;- CreateIndex&#10;CREATE UNIQUE INDEX &quot;User_email_key&quot; ON &quot;User&quot;(&quot;email&quot;);&#10;</code></pre>
<p><code>UNIQUE INDEX</code> on <code>email</code> was created because the <code>User</code> model in your Prisma schema is using the <a href="https://www.prisma.io/docs/orm/reference/prisma-schema-reference#unique"><code>@unique</code></a> attribute on its <code>email</code> field.</p>
<p>You now need to use the <code>wrangler d1 migrations apply</code> command to send this SQL statement to D1. This command accepts two options:</p>
<ul>
<li><code>--local</code>: Executes the statement against a <em>local</em> version of D1. This local version of D1 is a SQLite database file that will be located in the <code>.wrangler/state</code> directory of your project. Use this approach when you want to develop and test your Worker on your local machine. Refer to <a href="/d1/best-practices/local-development/">Local development</a> to learn more.</li>
<li><code>--remote</code>: Executes the statement against your <em>remote</em> version of D1. This version is used by your <em>deployed</em> Cloudflare Workers. Refer to <a href="/d1/best-practices/remote-development/">Remote development</a> to learn more.</li>
</ul>
<p>In this tutorial, you will do both local and remote development. You will test the Worker locally, then deploy your Worker afterwards.</p>
<p>Open your terminal, and run both commands:</p>
<pre tabindex="0"><code class="language-sh">&#35; For the local database&#10;npx wrangler d1 migrations apply prisma-demo-db --local&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; For the remote database&#10;npx wrangler d1 migrations apply prisma-demo-db --remote&#10;</code></pre>
<p>Choose <code>Yes</code> both times when you are prompted to confirm that the migration should be applied.</p>
<p>Next, create some data that you can query once the Worker is running. This time, you will run the SQL statement without storing it in a file:</p>
<pre tabindex="0"><code class="language-sh">&#35; For the local database&#10;npx wrangler d1 execute prisma-demo-db --command &quot;INSERT INTO  \&quot;User\&quot; (\&quot;email\&quot;, \&quot;name\&quot;) VALUES&#10;(&#x27;jane@prisma.io&#x27;, &#x27;Jane Doe (Local)&#x27;);&quot; --local&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; For the remote database&#10;npx wrangler d1 execute prisma-demo-db --command &quot;INSERT INTO  \&quot;User\&quot; (\&quot;email\&quot;, \&quot;name\&quot;) VALUES&#10;(&#x27;jane@prisma.io&#x27;, &#x27;Jane Doe (Remote)&#x27;);&quot; --remote&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7280.md")
</aside>
<h2 id="5-query-your-database-from-the-worker"><ol start="5">
<li>Query your database from the Worker</li>
</ol></h2>
<p>To query your database from the Worker using Prisma ORM, you need to:</p>
<ol>
<li>Add <code>DB</code> to the <code>Env</code> interface.</li>
<li>Instantiate <code>PrismaClient</code> using the <code>PrismaD1</code> driver adapter.</li>
<li>Send a query using Prisma Client and return the result.</li>
</ol>
<p>Open <code>src/index.ts</code> and replace the entire content with the following:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7288.md")
</div>
<p>Before running the Worker, generate Prisma Client with the following command:</p>
<pre tabindex="0"><code class="language-sh">npx prisma generate&#10;</code></pre>
<h2 id="6-run-the-worker-locally"><ol start="6">
<li>Run the Worker locally</li>
</ol></h2>
<p>Now that you have the database query in place and Prisma Client generated, run the Worker locally:</p>
<pre tabindex="0"><code class="language-sh">npm run dev&#10;</code></pre>
<p>Open your browser at <a href="http://localhost:8787/"><code>http://localhost:8787</code></a> to check the result of the database query:</p>
<pre tabindex="0"><code class="language-json">[{ &quot;id&quot;: 1, &quot;email&quot;: &quot;jane@prisma.io&quot;, &quot;name&quot;: &quot;Jane Doe (Local)&quot; }]&#10;</code></pre>
<h2 id="7-deploy-the-worker"><ol start="7">
<li>Deploy the Worker</li>
</ol></h2>
<p>To deploy the Worker, run the following command:</p>
<pre tabindex="0"><code class="language-sh">npm run deploy&#10;</code></pre>
<p>Access your Worker at <code>https://prisma-d1-example.USERNAME.workers.dev</code>. Your browser should display the following data queried from your remote D1 database:</p>
<pre tabindex="0"><code class="language-json">[{ &quot;id&quot;: 1, &quot;email&quot;: &quot;jane@prisma.io&quot;, &quot;name&quot;: &quot;Jane Doe (Remote)&quot; }]&#10;</code></pre>
<p>By finishing this tutorial, you have deployed a Cloudflare Worker using D1 as a database and querying it via Prisma ORM.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://www.prisma.io/docs/getting-started">Prisma documentation</a>.</li>
<li>To get help, open a new <a href="https://github.com/prisma/prisma/discussions/">GitHub Discussion</a>, or <a href="https://www.prisma.io/docs">ask the AI bot in the Prisma docs</a>.</li>
<li><a href="https://github.com/prisma/prisma-examples/">Ready-to-run examples using Prisma ORM</a>.</li>
<li>Check out the <a href="https://www.prisma.io/community">Prisma community</a>, follow <a href="https://www.x.com/prisma">Prisma on X</a> and join the <a href="https://pris.ly/discord">Prisma Discord</a>.</li>
<li><a href="https://www.prisma.io/blog/cloudflare-partnership-qerefgvwirjq">Developer Experience Redefined: Prisma &amp; Cloudflare Lead the Way to Data DX</a>.</li>
</ul>
