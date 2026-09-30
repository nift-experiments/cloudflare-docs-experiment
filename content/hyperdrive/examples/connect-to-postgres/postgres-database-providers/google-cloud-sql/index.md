---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/
  description: Connect Hyperdrive to a Google Cloud SQL for Postgres database instance.
  full_title: Google Cloud SQL · Cloudflare Hyperdrive docs
  head_html: <title>Google Cloud SQL · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Hyperdrive to a Google Cloud SQL for Postgres database instance."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/index.md"><meta property="og:title" content="Google Cloud SQL · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Hyperdrive to a Google Cloud SQL for Postgres database instance."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/#page","headline":"Google Cloud SQL \u00b7 Cloudflare Hyperdrive docs","description":"Connect Hyperdrive to a Google Cloud SQL for Postgres database instance.","url":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/examples/connect-to-postgres/postgres-database-providers/google-cloud-sql/
  schema: 1
---
<p class="article-summary">Connect Hyperdrive to a Google Cloud SQL for Postgres database instance.</p>
<p>This example shows you how to connect Hyperdrive to a Google Cloud SQL Postgres database instance.</p>
<h2 id="1-allow-hyperdrive-access"><ol>
<li>Allow Hyperdrive access</li>
</ol></h2>
<p>To allow Hyperdrive to connect to your database, you will need to ensure that Hyperdrive has valid user credentials and network access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9274.md")
</aside>
<h3 id="cloud-console">Cloud Console</h3>
<p>When creating the instance or when editing an existing instance in the <a href="https://console.cloud.google.com/sql/instances">Google Cloud Console</a>:</p>
<p>To allow Hyperdrive to reach your instance:</p>
<ol>
<li>In the <a href="https://console.cloud.google.com/sql/instances">Cloud Console</a>, select the instance you want Hyperdrive to connect to.</li>
<li>Expand <strong>Connections</strong> &gt; <strong>Networking</strong> &gt; ensure <strong>Public IP</strong> is enabled &gt; <strong>Add a Network</strong> and input <code>0.0.0.0/0</code>.</li>
<li>Select <strong>Done</strong> &gt; <strong>Save</strong> to persist your changes.</li>
<li>Select <strong>Overview</strong> from the sidebar and note down the <strong>Public IP address</strong> of your instance.</li>
</ol>
<p>To create a user for Hyperdrive to connect as:</p>
<ol>
<li>Select <strong>Users</strong> in the sidebar.</li>
<li>Select <strong>Add User Account</strong> &gt; select <strong>Built-in authentication</strong>.</li>
<li>Provide a name (for example, <code>hyperdrive-user</code>) &gt; select <strong>Generate</strong> to generate a password.</li>
<li>Copy this password to your clipboard before selecting <strong>Add</strong> to create the user.</li>
</ol>
<p>With the username, password, public IP address and (optional) database name (default: <code>postgres</code>), you can now create a Hyperdrive database configuration.</p>
<h3 id="gcloud-cli">gcloud CLI</h3>
<p>The <a href="https://cloud.google.com/sdk/docs/install">gcloud CLI</a> allows you to create a new user and enable Hyperdrive to connect to your database.</p>
<p>Use <code>gcloud sql</code> to create a new user (for example, <code>hyperdrive-user</code>) with a strong password:</p>
<pre tabindex="0"><code class="language-sh">gcloud sql users create hyperdrive-user --instance=YOUR_INSTANCE_NAME --password=SUFFICIENTLY_LONG_PASSWORD&#10;</code></pre>
<p>Run the following command to enable <a href="https://cloud.google.com/sql/docs/postgres/configure-ip">Internet access</a> to your database instance:</p>
<pre tabindex="0"><code class="language-sh">&#35; If you have any existing authorized networks, ensure you provide those as a comma separated list.&#10;&#35; The gcloud CLI will replace any existing authorized networks with the list you provide here.&#10;gcloud sql instances patch YOUR_INSTANCE_NAME --authorized-networks=&quot;0.0.0.0/0&quot;&#10;</code></pre>
<p>Refer to <a href="https://cloud.google.com/sql/docs/postgres/create-manage-users">Google Cloud's documentation</a> for additional configuration options.</p>
<h2 id="2-create-a-database-configuration"><ol start="2">
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
@input("content/.markup/bodies/9280.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9273.md")
</aside>
<h2 id="3-use-hyperdrive-from-your-worker"><ol start="3">
<li>Use Hyperdrive from your Worker</li>
</ol></h2>
<p>Install the <code>node-postgres</code> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9272.md")
</aside>
<p>If using TypeScript, install the types package:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @types/pg" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9281.md")
</div>
<p>Create a new <code>Client</code> instance and pass the Hyperdrive <code>connectionString</code>:</p>
<pre tabindex="0"><code class="language-ts">// filepath: src/index.ts&#10;import { Client } from &quot;pg&quot;;&#10;&#10;export default {&#10;	async fetch(&#10;		request: Request,&#10;		env: Env,&#10;		ctx: ExecutionContext,&#10;	): Promise&lt;Response&gt; {&#10;		// Create a new client instance for each request. Hyperdrive maintains the&#10;		// underlying database connection pool, so creating a new client is fast.&#10;		const client = new Client({&#10;			connectionString: env.HYPERDRIVE.connectionString,&#10;		});&#10;&#10;		try {&#10;			// Connect to the database&#10;			await client.connect();&#10;&#10;			// Perform a simple query&#10;			const result = await client.query(&quot;SELECT * FROM pg_tables&quot;);&#10;&#10;			return Response.json({&#10;				success: true,&#10;				result: result.rows,&#10;			});&#10;		} catch (error: any) {&#10;			console.error(&quot;Database error:&quot;, error.message);&#10;&#10;			return new Response(&quot;Internal error occurred&quot;, { status: 500 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
