---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/examples/private-database/
  description: This example demonstrates how to query a private PostgreSQL database from a Worker using Workers VPC and Hyperdrive. The Worker connects to a database that is not exposed to the public Internet, with Hyperdrive providing connection pooling and query acceleration.
  full_title: Connect to a private database · Cloudflare Workers VPC
  head_html: <title>Connect to a private database · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="This example demonstrates how to query a private PostgreSQL database from a Worker using Workers VPC and Hyperdrive. The Worker connects to a database that is not exposed to the public Internet, with Hyperdrive providing connection pooling and query acceleration."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/examples/private-database/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/examples/private-database/index.md"><meta property="og:title" content="Connect to a private database · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This example demonstrates how to query a private PostgreSQL database from a Worker using Workers VPC and Hyperdrive. The Worker connects to a database that is not exposed to the public Internet, with Hyperdrive providing connection pooling and query acceleration."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/examples/private-database/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/examples/private-database/#page","headline":"Connect to a private database \u00b7 Cloudflare Workers VPC","description":"This example demonstrates how to query a private PostgreSQL database from a Worker using Workers VPC and Hyperdrive. The Worker connects to a database that is not exposed to the public Internet, with Hyperdrive providing connection pooling and query acceleration.","url":"https://developers.cloudflare.com/workers-vpc/examples/private-database/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/examples/private-database/
  schema: 1
---
<p>This example demonstrates how to query a private PostgreSQL database from a Worker using <a href="/workers-vpc/">Workers VPC</a> and <a href="/hyperdrive/">Hyperdrive</a>. The Worker connects to a database that is not exposed to the public Internet, with Hyperdrive providing connection pooling and query acceleration.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A PostgreSQL database running in your private network (for example, on port 5432)</li>
<li>A <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel</a> connected to the private network where your database runs</li>
<li>A Cloudflare account with Workers VPC access</li>
</ul>
<h2 id="1-set-up-a-cloudflare-tunnel"><ol>
<li>Set up a Cloudflare Tunnel</li>
</ol></h2>
<p>If you do not already have a tunnel running in the same network as your database, create one.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15879.md")
</div>
<p>The tunnel must be able to reach your database host and port from within the private network. For full tunnel documentation, refer to <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel for Workers VPC</a>.</p>
<h2 id="2-create-a-tcp-vpc-service"><ol start="2">
<li>Create a TCP VPC Service</li>
</ol></h2>
<p>Create a VPC Service of type <code>tcp</code> that points to your database:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler vpc service create my-postgres-db \&#10;  &#45;-type tcp \&#10;  &#45;-tcp-port 5432 \&#10;  &#45;-app-protocol postgresql \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-ipv4 &lt;YOUR_DATABASE_IP&gt;&#10;</code></pre>
<p>Replace <code>&lt;YOUR_TUNNEL_ID&gt;</code> with the tunnel ID from step 1 and <code>&lt;YOUR_DATABASE_IP&gt;</code> with the private IP address of your database (for example, <code>10.0.0.5</code>).</p>
<p>The command returns a service ID. Save this value for the next step.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15878.md")
</aside>
<h2 id="3-create-a-hyperdrive-configuration"><ol start="3">
<li>Create a Hyperdrive configuration</li>
</ol></h2>
<p>Use the <code>--service-id</code> flag to point Hyperdrive at the VPC Service you created:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler hyperdrive create my-vpc-database \&#10;  &#45;-service-id &lt;YOUR_VPC_SERVICE_ID&gt; \&#10;  &#45;-database &lt;DATABASE_NAME&gt; \&#10;  &#45;-user &lt;DATABASE_USER&gt; \&#10;  &#45;-password &lt;DATABASE_PASSWORD&gt; \&#10;  &#45;-scheme postgresql&#10;</code></pre>
<p>Replace <code>&lt;YOUR_VPC_SERVICE_ID&gt;</code> with the service ID from step 2, and provide your database name, user, and password.</p>
<p>The command outputs a Hyperdrive configuration ID. Copy this for the next step.</p>
<h2 id="4-bind-hyperdrive-to-a-worker"><ol start="4">
<li>Bind Hyperdrive to a Worker</li>
</ol></h2>
<p>You must create a binding in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for your Worker to connect to your Hyperdrive configuration. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to access resources, like Hyperdrive, on the Cloudflare developer platform.</p>
<p>To bind your Hyperdrive configuration to your Worker, add the following to the end of your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15880.md")
</div>
<p>Specifically:</p>
<ul>
<li>The value (string) you set for the <code>binding</code> (binding name) will be used to reference this database in your Worker. In this tutorial, name your binding <code>HYPERDRIVE</code>.</li>
<li>The binding must be <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables">a valid JavaScript variable name</a>. For example, <code>binding = &quot;hyperdrive&quot;</code> or <code>binding = &quot;productionDB&quot;</code> would both be valid names for the binding.</li>
<li>Your binding is available in your Worker at <code>env.&lt;BINDING_NAME&gt;</code>.</li>
</ul>
<p>If you wish to use a local database during development, you can add a <code>localConnectionString</code> to your  Hyperdrive configuration with the connection string of your database:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15881.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15877.md")
</aside>
<h2 id="5-query-the-database"><ol start="5">
<li>Query the database</li>
</ol></h2>
<p>Install the <code>node-postgres</code> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15876.md")
</aside>
<p>If using TypeScript, install the types package:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @types/pg" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15882.md")
</div>
<p>Create a new <code>Client</code> instance and pass the Hyperdrive <code>connectionString</code>:</p>
<pre tabindex="0"><code class="language-ts">// filepath: src/index.ts&#10;import { Client } from &quot;pg&quot;;&#10;&#10;export default {&#10;	async fetch(&#10;		request: Request,&#10;		env: Env,&#10;		ctx: ExecutionContext,&#10;	): Promise&lt;Response&gt; {&#10;		// Create a new client instance for each request. Hyperdrive maintains the&#10;		// underlying database connection pool, so creating a new client is fast.&#10;		const client = new Client({&#10;			connectionString: env.HYPERDRIVE.connectionString,&#10;		});&#10;&#10;		try {&#10;			// Connect to the database&#10;			await client.connect();&#10;&#10;			// Perform a simple query&#10;			const result = await client.query(&quot;SELECT * FROM pg_tables&quot;);&#10;&#10;			return Response.json({&#10;				success: true,&#10;				result: result.rows,&#10;			});&#10;		} catch (error: any) {&#10;			console.error(&quot;Database error:&quot;, error.message);&#10;&#10;			return new Response(&quot;Internal error occurred&quot;, { status: 500 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="6-deploy-and-test"><ol start="6">
<li>Deploy and test</li>
</ol></h2>
<p>Deploy your Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Send a request to verify the connection:</p>
<pre tabindex="0"><code class="language-sh">curl https://&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev&#10;</code></pre>
<p>A successful response returns a JSON array of rows from your database.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">how Hyperdrive works</a></li>
<li>Configure <a href="/hyperdrive/concepts/query-caching/">query caching</a> for Hyperdrive</li>
<li>Review <a href="/workers-vpc/configuration/vpc-services/">VPC Service configuration options</a> including TLS certificate verification</li>
<li>Explore <a href="/workers-vpc/examples/">other examples</a></li>
</ul>
