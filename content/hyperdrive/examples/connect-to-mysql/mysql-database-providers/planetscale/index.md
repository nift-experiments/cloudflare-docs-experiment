---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/
  description: Connect Hyperdrive to a PlanetScale MySQL database.
  full_title: PlanetScale · Cloudflare Hyperdrive docs
  head_html: <title>PlanetScale · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Hyperdrive to a PlanetScale MySQL database."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/index.md"><meta property="og:title" content="PlanetScale · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Hyperdrive to a PlanetScale MySQL database."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Hyperdrive"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/#page","headline":"PlanetScale \u00b7 Cloudflare Hyperdrive docs","description":"Connect Hyperdrive to a PlanetScale MySQL database.","url":"https://developers.cloudflare.com/hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/examples/connect-to-mysql/mysql-database-providers/planetscale/
  schema: 1
---
<p class="article-summary">Connect Hyperdrive to a PlanetScale MySQL database.</p>
<p>This example shows you how to connect Hyperdrive to a <a href="https://planetscale.com/">PlanetScale</a> MySQL database.</p>
<h2 id="1-allow-hyperdrive-access"><ol>
<li>Allow Hyperdrive access</li>
</ol></h2>
<p>You can connect Hyperdrive to any existing PlanetScale MySQL-compatible database by creating a new user and fetching your database connection string.</p>
<h3 id="planetscale-dashboard">PlanetScale Dashboard</h3>
<ol>
<li>Go to the <a href="https://app.planetscale.com/"><strong>PlanetScale dashboard</strong></a> and select the database you wish to connect to.</li>
<li>Click <strong>Connect</strong>. Enter <code>hyperdrive-user</code> as the password name (or your preferred name) and configure the permissions as desired. Select <strong>Create password</strong>. Note the username and password as they will not be displayed again.</li>
<li>Select <strong>Other</strong> as your language or framework. Note down the database host, database name, database username, and password. You will need these to create a database configuration in Hyperdrive.</li>
</ol>
<p>With the host, database name, username and password, you can now create a Hyperdrive database configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9141.md")
</aside>
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
@markup("md", "content/.markup/bodies/9140.md")
</aside>
<p>This command outputs a binding for the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9142.md")
</div>
<h2 id="3-use-hyperdrive-from-your-worker"><ol start="3">
<li>Use Hyperdrive from your Worker</li>
</ol></h2>
<p>Install the <a href="https://github.com/sidorares/node-mysql2">mysql2</a> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9139.md")
</aside>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9143.md")
</div>
<p>Create a new <code>connection</code> instance and pass the Hyperdrive parameters:</p>
<pre tabindex="0"><code class="language-ts">// mysql2 v3.13.0 or later is required&#10;import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new connection on each request. Hyperdrive maintains the underlying&#10;		// database connection pool, so creating a new connection is fast.&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;&#10;			// Required to enable mysql2 compatibility for Workers&#10;			disableEval: true,&#10;		});&#10;&#10;		try {&#10;			// Sample query&#10;			const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;			// Return result rows as JSON&#10;			return Response.json({ results, fields });&#10;		} catch (e) {&#10;			console.error(e);&#10;			return Response.json(&#10;				{ error: e instanceof Error ? e.message : e },&#10;				{ status: 500 },&#10;			);&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9138.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9137.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
