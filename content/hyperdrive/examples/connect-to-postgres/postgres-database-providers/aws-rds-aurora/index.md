---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/
  description: Connect Hyperdrive to an AWS RDS or Aurora Postgres database instance.
  full_title: AWS RDS and Aurora · Cloudflare Hyperdrive docs
  head_html: <title>AWS RDS and Aurora · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Hyperdrive to an AWS RDS or Aurora Postgres database instance."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/index.md"><meta property="og:title" content="AWS RDS and Aurora · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Hyperdrive to an AWS RDS or Aurora Postgres database instance."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/#page","headline":"AWS RDS and Aurora \u00b7 Cloudflare Hyperdrive docs","description":"Connect Hyperdrive to an AWS RDS or Aurora Postgres database instance.","url":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/examples/connect-to-postgres/postgres-database-providers/aws-rds-aurora/
  schema: 1
---
<p class="article-summary">Connect Hyperdrive to an AWS RDS or Aurora Postgres database instance.</p>
<p>This example shows you how to connect Hyperdrive to an Amazon Relational Database Service (Amazon RDS) Postgres or Amazon Aurora database instance.</p>
<h2 id="1-allow-hyperdrive-access"><ol>
<li>Allow Hyperdrive access</li>
</ol></h2>
<p>To allow Hyperdrive to connect to your database, you will need to ensure that Hyperdrive has valid user credentials and network access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9326.md")
</aside>
<h3 id="aws-console">AWS Console</h3>
<p>When creating or modifying an instance in the AWS console:</p>
<ol>
<li>Configure a <strong>DB cluster identifier</strong> and other settings you wish to customize.</li>
<li>Under <strong>Settings</strong> &gt; <strong>Credential settings</strong>, note down the <strong>Master username</strong> and <strong>Master password</strong> (Aurora only).</li>
<li>Under the <strong>Connectivity</strong> header, ensure <strong>Public access</strong> is set to <strong>Yes</strong>.</li>
<li>Select an <strong>Existing VPC security group</strong> that allows public Internet access from <code>0.0.0.0/0</code> to the port your database instance is configured to listen on (default: <code>5432</code> for PostgreSQL instances).</li>
<li>Select <strong>Create database</strong>.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9325.md")
</aside>
<h3 id="retrieve-the-database-endpoint-aurora">Retrieve the database endpoint (Aurora)</h3>
<p>To retrieve the database endpoint (hostname) for Hyperdrive to connect to:</p>
<ol>
<li>Go to <strong>Databases</strong> view under <strong>RDS</strong> in the AWS console.</li>
<li>Select the database you want Hyperdrive to connect to.</li>
<li>Under the <strong>Endpoints</strong> header, note down the <strong>Endpoint name</strong> with the type <code>Writer</code> and the <strong>Port</strong>.</li>
</ol>
<h3 id="retrieve-the-database-endpoint-rds-postgresql">Retrieve the database endpoint (RDS PostgreSQL)</h3>
<p>For regular RDS instances (non-Aurora), you will need to fetch the endpoint and port of the database:</p>
<ol>
<li>Go to <strong>Databases</strong> view under <strong>RDS</strong> in the AWS console.</li>
<li>Select the database you want Hyperdrive to connect to.</li>
<li>Under the <strong>Connectivity &amp; security</strong> header, note down the <strong>Endpoint</strong> and the <strong>Port</strong>.</li>
</ol>
<p>The endpoint will resemble <code>YOUR_DATABASE_NAME.cpuo5rlli58m.AWS_REGION.rds.amazonaws.com</code> and the port will default to <code>5432</code>.</p>
<h2 id="2-create-your-user"><ol start="2">
<li>Create your user</li>
</ol></h2>
<p>Once your database is created, you will need to create a user for Hyperdrive to connect as. Although you can use the <strong>Master username</strong> configured during initial database creation, best practice is to create a less privileged user.</p>
<p>To create a new user, log in to the database and use the <code>CREATE ROLE</code> command:</p>
<pre tabindex="0"><code class="language-sh">&#35; Log in to the database&#10;psql postgresql://MASTER_USERNAME:MASTER_PASSWORD@ENDPOINT_NAME:PORT/database_name&#10;</code></pre>
<p>Run the following SQL statements:</p>
<pre tabindex="0"><code class="language-sql">&#45;- Create a role for Hyperdrive&#10;CREATE ROLE hyperdrive;&#10;&#10;&#45;- Allow Hyperdrive to connect&#10;GRANT CONNECT ON DATABASE postgres TO hyperdrive;&#10;&#10;&#45;- Grant database privileges to the hyperdrive role&#10;GRANT ALL PRIVILEGES ON DATABASE postgres to hyperdrive;&#10;&#10;&#45;- Create a specific user for Hyperdrive to log in as&#10;CREATE ROLE hyperdrive_user LOGIN PASSWORD &#x27;sufficientlyRandomPassword&#x27;;&#10;&#10;&#45;- Grant this new user the hyperdrive role privileges&#10;GRANT hyperdrive to hyperdrive_user;&#10;</code></pre>
<p>Refer to AWS' <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.html">documentation on user roles in PostgreSQL</a> for more details.</p>
<p>With a database user, password, database endpoint (hostname and port) and database name (default: <code>postgres</code>), you can now set up Hyperdrive.</p>
<h2 id="3-create-a-database-configuration"><ol start="3">
<li>Create a database configuration</li>
</ol></h2>
<p>To configure Hyperdrive, you will need:</p>
<ul>
<li>The IP address (or hostname) and port of your database.</li>
<li>The database username (for example, <code>hyperdrive-demo</code>) you configured in a previous step.</li>
<li>The password associated with that username.</li>
<li>The name of the database you want Hyperdrive to connect to. For example, <code>postgres</code>.</li>
</ul>
<p>Hyperdrive accepts the combination of these parameters in the common connection string format used by database drivers:</p>
<pre tabindex="0"><code class="language-txt">postgres://USERNAME:PASSWORD@HOSTNAME_OR_IP_ADDRESS:PORT/database_name&#10;</code></pre>
<p>Most database providers will provide a connection string you can directly copy-and-paste directly into Hyperdrive.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9332.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9324.md")
</aside>
<h2 id="3-use-hyperdrive-from-your-worker"><ol start="3">
<li>Use Hyperdrive from your Worker</li>
</ol></h2>
<p>Install the <code>node-postgres</code> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9323.md")
</aside>
<p>If using TypeScript, install the types package:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @types/pg" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9333.md")
</div>
<p>Create a new <code>Client</code> instance and pass the Hyperdrive <code>connectionString</code>:</p>
<pre tabindex="0"><code class="language-ts">// filepath: src/index.ts&#10;import { Client } from &quot;pg&quot;;&#10;&#10;export default {&#10;	async fetch(&#10;		request: Request,&#10;		env: Env,&#10;		ctx: ExecutionContext,&#10;	): Promise&lt;Response&gt; {&#10;		// Create a new client instance for each request. Hyperdrive maintains the&#10;		// underlying database connection pool, so creating a new client is fast.&#10;		const client = new Client({&#10;			connectionString: env.HYPERDRIVE.connectionString,&#10;		});&#10;&#10;		try {&#10;			// Connect to the database&#10;			await client.connect();&#10;&#10;			// Perform a simple query&#10;			const result = await client.query(&quot;SELECT * FROM pg_tables&quot;);&#10;&#10;			return Response.json({&#10;				success: true,&#10;				result: result.rows,&#10;			});&#10;		} catch (error: any) {&#10;			console.error(&quot;Database error:&quot;, error.message);&#10;&#10;			return new Response(&quot;Internal error occurred&quot;, { status: 500 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
