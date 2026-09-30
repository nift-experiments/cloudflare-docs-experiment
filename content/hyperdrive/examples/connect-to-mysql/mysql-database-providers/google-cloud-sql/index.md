---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/google-cloud-sql/
  description: Connect Hyperdrive to a Google Cloud SQL database instance.
  full_title: Google Cloud SQL · Cloudflare Hyperdrive docs
  head_html: <title>Google Cloud SQL · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Hyperdrive to a Google Cloud SQL database instance."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/google-cloud-sql/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/google-cloud-sql/index.md"><meta property="og:title" content="Google Cloud SQL · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Hyperdrive to a Google Cloud SQL database instance."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/google-cloud-sql/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/google-cloud-sql/#page","headline":"Google Cloud SQL \u00b7 Cloudflare Hyperdrive docs","description":"Connect Hyperdrive to a Google Cloud SQL database instance.","url":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/google-cloud-sql/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/examples/connect-to-mysql/mysql-database-providers/google-cloud-sql/
  schema: 1
---
<p class="article-summary">Connect Hyperdrive to a Google Cloud SQL database instance.</p>
<p>This example shows you how to connect Hyperdrive to a Google Cloud SQL MySQL database instance.</p>
<h2 id="1-allow-hyperdrive-access"><ol>
<li>Allow Hyperdrive access</li>
</ol></h2>
<p>To allow Hyperdrive to connect to your database, you will need to ensure that Hyperdrive has valid user credentials and network access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9147.md")
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
<li>Provide a name (for example, <code>hyperdrive-user</code>), then select <strong>Generate</strong> to generate a password.</li>
<li>Copy this password to your clipboard before selecting <strong>Add</strong> to create the user.</li>
</ol>
<p>With the username, password, public IP address and (optional) database name (default: <code>mysql</code>), you can now create a Hyperdrive database configuration.</p>
<h2 id="2-create-a-database-configuration"><ol start="2">
<li>Create a database configuration</li>
</ol></h2>
<p>To configure Hyperdrive, you will need:</p>
<ul>
<li>The IP address (or hostname) and port of your database.</li>
<li>The database username (for example, <code>hyperdrive-demo</code>) you configured in a previous step.</li>
<li>The password associated with that username.</li>
<li>The name of the database you want Hyperdrive to connect to. For example, <code>mysql</code>.</li>
</ul>
<p>Hyperdrive accepts the combination of these parameters in the common connection string format used by database drivers:</p>
<pre tabindex="0"><code class="language-txt">mysql://USERNAME:PASSWORD@HOSTNAME_OR_IP_ADDRESS:PORT/database_name&#10;</code></pre>
<p>Most database providers will provide a connection string you can copy-and-paste directly into Hyperdrive.</p>
<p>To create a Hyperdrive configuration with the <a href="/workers/wrangler/install-and-update/">Wrangler CLI</a>, open your terminal and run the following command.</p>
<ul>
<li>Replace &lt;NAME_OF_HYPERDRIVE_CONFIG&gt; with a name for your Hyperdrive configuration and paste the connection string provided from your database host, or,</li>
<li>Replace <code>user</code>, <code>password</code>, <code>HOSTNAME_OR_IP_ADDRESS</code>, <code>port</code>, and <code>database_name</code> placeholders with those specific to your database:</li>
</ul>
<pre tabindex="0"><code class="language-sh">npx wrangler hyperdrive create &lt;NAME_OF_HYPERDRIVE_CONFIG&gt; --connection-string=&quot;mysql://user:password@HOSTNAME_OR_IP_ADDRESS:PORT/database_name&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9146.md")
</aside>
<p>This command outputs a binding for the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9148.md")
</div>
<h2 id="3-use-hyperdrive-from-your-worker"><ol start="3">
<li>Use Hyperdrive from your Worker</li>
</ol></h2>
<p>Install the <a href="https://github.com/sidorares/node-mysql2">mysql2</a> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9145.md")
</aside>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9149.md")
</div>
<p>Create a new <code>connection</code> instance and pass the Hyperdrive parameters:</p>
<pre tabindex="0"><code class="language-ts">// mysql2 v3.13.0 or later is required&#10;import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new connection on each request. Hyperdrive maintains the underlying&#10;		// database connection pool, so creating a new connection is fast.&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;&#10;			// Required to enable mysql2 compatibility for Workers&#10;			disableEval: true,&#10;		});&#10;&#10;		try {&#10;			// Sample query&#10;			const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;			// Return result rows as JSON&#10;			return Response.json({ results, fields });&#10;		} catch (e) {&#10;			console.error(e);&#10;			return Response.json(&#10;				{ error: e instanceof Error ? e.message : e },&#10;				{ status: 500 },&#10;			);&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9144.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
