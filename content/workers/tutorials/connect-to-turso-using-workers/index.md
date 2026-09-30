---
cp9:
  canonical: https://developers.cloudflare.com/workers/tutorials/connect-to-turso-using-workers/
  description: This tutorial will guide you on how to build globally distributed applications with Cloudflare Workers, and Turso, an edge-hosted distributed database based on libSQL.
  full_title: Connect to and query your Turso database using Workers · Cloudflare Workers docs
  head_html: <title>Connect to and query your Turso database using Workers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="This tutorial will guide you on how to build globally distributed applications with Cloudflare Workers, and Turso, an edge-hosted distributed database based on libSQL."><link rel="canonical" href="https://developers.cloudflare.com/workers/tutorials/connect-to-turso-using-workers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/tutorials/connect-to-turso-using-workers/index.md"><meta property="og:title" content="Connect to and query your Turso database using Workers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This tutorial will guide you on how to build globally distributed applications with Cloudflare Workers, and Turso, an edge-hosted distributed database based on libSQL."><meta property="og:url" content="https://developers.cloudflare.com/workers/tutorials/connect-to-turso-using-workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="TypeScript,SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/tutorials/connect-to-turso-using-workers/#page","headline":"Connect to and query your Turso database using Workers \u00b7 Cloudflare Workers docs","description":"This tutorial will guide you on how to build globally distributed applications with Cloudflare Workers, and Turso, an edge-hosted distributed database based on libSQL.","url":"https://developers.cloudflare.com/workers/tutorials/connect-to-turso-using-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TypeScript","SQL"]}</script>
  markdown: true
  noindex: false
  route: /workers/tutorials/connect-to-turso-using-workers/
  schema: 1
---
<p>This tutorial will guide you on how to build globally distributed applications with Cloudflare Workers, and <a href="https://chiselstrike.com/">Turso</a>, an edge-hosted distributed database based on libSQL. By using Workers and Turso, you can create applications that are close to your end users without having to maintain or operate infrastructure in tens or hundreds of regions.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16080.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before continuing with this tutorial, you should have:</p>
<ul>
<li>Successfully <a href="/workers/get-started/guide/">created up your first Cloudflare Worker</a> and/or have deployed a Cloudflare Worker before.</li>
<li>Installed <a href="/workers/wrangler/install-and-update/">Wrangler</a>, a command-line tool for building Cloudflare Workers.</li>
<li>A <a href="https://github.com/">GitHub account</a>, required for authenticating to Turso.</li>
<li>A basic familiarity with installing and using command-line interface (CLI) applications.</li>
</ul>
<h2 id="install-the-turso-cli">Install the Turso CLI</h2>
<p>You will need the Turso CLI to create and populate a database. Run either of the following two commands in your terminal to install the Turso CLI:</p>
<pre tabindex="0"><code class="language-sh">&#35; On macOS or Linux with Homebrew&#10;brew install chiselstrike/tap/turso&#10;&#10;&#35; Manual scripted installation&#10;curl -sSfL &lt;https://get.tur.so/install.sh&gt; | bash&#10;</code></pre>
<p>After you have installed the Turso CLI, verify that the CLI is in your shell path:</p>
<pre tabindex="0"><code class="language-sh">turso --version&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; This should output your current Turso CLI version (your installed version may be higher):&#10;turso version v0.51.0&#10;</code></pre>
<h2 id="create-and-populate-a-database">Create and populate a database</h2>
<p>Before you create your first Turso database, you need to log in to the CLI using your GitHub account by running:</p>
<pre tabindex="0"><code class="language-sh">turso auth login&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#10;Waiting for authentication...&#10;✔  Success! Logged in as &lt;your GitHub username&gt;&#10;</code></pre>
<p><code>turso auth login</code> will open a browser window and ask you to sign into your GitHub account, if you are not already logged in. The first time you do this, you will need to give the Turso application permission to use your account. Select <strong>Approve</strong> to grant Turso the permissions needed.</p>
<p>After you have authenticated, you can create a database by running <code>turso db create &lt;DATABASE_NAME&gt;</code>. Turso will automatically choose a location closest to you.</p>
<pre tabindex="0"><code class="language-sh">turso db create my-db&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#35; Example:&#10;[===&gt;                ]&#10;Creating database my-db in Los Angeles, California (US) (lax)&#10;&#35; Once succeeded:&#10;Created database my-db in Los Angeles, California (US) (lax) in 34 seconds.&#10;</code></pre>
<p>With your first database created, you can now connect to it directly and execute SQL against it:</p>
<pre tabindex="0"><code class="language-sh">turso db shell my-db&#10;</code></pre>
<p>To get started with your database, create and define a schema for your first table. In this example, you will create a <code>example_users</code> table with one column: <code>email</code> (of type <code>text</code>) and then populate it with one email address.</p>
<p>In the shell you just opened, paste in the following SQL:</p>
<pre tabindex="0"><code class="language-sql">create table example_users (email text);&#10;insert into example_users values (&#x27;foo@bar.com&#x27;);&#10;</code></pre>
<p>If the SQL statements succeeded, there will be no output. Note that the trailing semi-colons (<code>;</code>) are necessary to terminate each SQL statement.</p>
<p>Type <code>.quit</code> to exit the shell.</p>
<h2 id="use-wrangler-to-create-a-workers-project">Use Wrangler to create a Workers project</h2>
<p>The Workers command-line interface, <a href="/workers/wrangler/install-and-update/">Wrangler</a>, allows you to create, locally develop, and deploy your Workers projects.</p>
<p>To create a new Workers project (named <code>worker-turso-ts</code>), run the following:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- worker-turso-ts</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- worker-turso-ts" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare worker-turso-ts</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare worker-turso-ts" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest worker-turso-ts</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest worker-turso-ts" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>To start developing your Worker, <code>cd</code> into your new project directory:</p>
<pre tabindex="0"><code class="language-sh">cd worker-turso-ts&#10;</code></pre>
<p>In your project directory, you now have the following files:</p>
<ul>
<li><code>wrangler.json</code> / <code>wrangler.toml</code>: <a href="/workers/wrangler/configuration/">Wrangler configuration file</a></li>
<li><code>src/index.ts</code>: A minimal Hello World Worker written in TypeScript</li>
<li><code>package.json</code>: A minimal Node dependencies configuration file.</li>
<li><code>tsconfig.json</code>: TypeScript configuration that includes Workers types. Only generated if indicated.</li>
</ul>
<p>For this tutorial, only the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> and <code>src/index.ts</code> file are relevant. You will not need to edit the other files, and they should be left as is.</p>
<h2 id="configure-your-worker-for-your-turso-database">Configure your Worker for your Turso database</h2>
<p>The Turso client library requires two pieces of information to make a connection:</p>
<ol>
<li><code>LIBSQL_DB_URL</code> - The connection string for your Turso database.</li>
<li><code>LIBSQL_DB_AUTH_TOKEN</code> - The authentication token for your Turso database. This should be kept a secret, and not committed to source code.</li>
</ol>
<p>To get the URL for your database, run the following Turso CLI command, and copy the result:</p>
<pre tabindex="0"><code class="language-sh">turso db show my-db --url&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">libsql://my-db-&lt;your-github-username&gt;.turso.io&#10;</code></pre>
<p>Open the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> in your editor and at the bottom of the file, create a new <code>[vars]</code> section representing the <a href="/workers/configuration/environment-variables/">environment variables</a> for your project:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16081.md")
</div>
<p>Save the changes to the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<p>Next, create a long-lived authentication token for your Worker to use when connecting to your database. Run the following Turso CLI command, and copy the output to your clipboard:</p>
<pre tabindex="0"><code class="language-sh">turso db tokens create my-db -e none&#10;&#35; Will output a long text string (an encoded JSON Web Token)&#10;</code></pre>
<p>To keep this token secret:</p>
<ol>
<li>You will create a <code>.dev.vars</code> file for local development. Do not commit this file to source control. You should add <code>.dev.vars to your </code>.gitignore` file if you are using Git.</li>
</ol>
<ul>
<li>You will also create a <a href="/workers/configuration/secrets/">secret</a> to keep your authentication token confidential.</li>
</ul>
<p>First, create a new file called <code>.dev.vars</code> with the following structure. Paste your authentication token in the quotation marks:</p>
<pre tabindex="0"><code>LIBSQL_DB_AUTH_TOKEN=&quot;&lt;YOUR_AUTH_TOKEN&gt;&quot;&#10;</code></pre>
<p>Save your changes to <code>.dev.vars</code>. Next, store the authentication token as a secret for your production Worker to reference. Run the following <code>wrangler secret</code> command to create a Secret with your token:</p>
<pre tabindex="0"><code class="language-sh">&#35; Ensure you specify the secret name exactly: your Worker will need to reference it later.&#10;npx wrangler secret put LIBSQL_DB_AUTH_TOKEN&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">? Enter a secret value: › &lt;paste your token here&gt;&#10;</code></pre>
<p>Select <code>&lt;Enter&gt;</code> on your keyboard to save the token as a secret. Both <code>LIBSQL_DB_URL</code> and <code>LIBSQL_DB_AUTH_TOKEN</code> will be available in your Worker's environment at runtime.</p>
<h2 id="install-extra-libraries">Install extra libraries</h2>
<p>Install the Turso client library and a router:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @libsql/client itty-router</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @libsql/client itty-router" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @libsql/client itty-router</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @libsql/client itty-router" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @libsql/client itty-router</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @libsql/client itty-router" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @libsql/client itty-router</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @libsql/client itty-router" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The <code>@libsql/client</code> library allows you to query a Turso database. The <code>itty-router</code> library is a lightweight router you will use to help handle incoming requests to the worker.</p>
<h2 id="write-your-worker">Write your Worker</h2>
<p>You will now write a Worker that will:</p>
<ol>
<li>Handle an HTTP request.</li>
<li>Route it to a specific handler to either list all users in our database or add a new user.</li>
<li>Return the results and/or success.</li>
</ol>
<p>Open <code>src/index.ts</code> and delete the existing template. Copy the below code exactly as is and paste it into the file:</p>
<pre tabindex="0"><code class="language-ts">import { Client as LibsqlClient, createClient } from &quot;@libsql/client/web&quot;;&#10;import { Router, RouterType } from &quot;itty-router&quot;;&#10;&#10;export interface Env {&#10;	// The environment variable containing your the URL for your Turso database.&#10;	LIBSQL_DB_URL?: string;&#10;	// The Secret that contains the authentication token for your Turso database.&#10;	LIBSQL_DB_AUTH_TOKEN?: string;&#10;&#10;	// These objects are created before first use, then stashed here&#10;	// for future use&#10;	router?: RouterType;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		if (env.router === undefined) {&#10;			env.router = buildRouter(env);&#10;		}&#10;&#10;		return env.router.fetch(request);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;&#10;function buildLibsqlClient(env: Env): LibsqlClient {&#10;	const url = env.LIBSQL_DB_URL?.trim();&#10;	if (url === undefined) {&#10;		throw new Error(&quot;LIBSQL_DB_URL env var is not defined&quot;);&#10;	}&#10;&#10;	const authToken = env.LIBSQL_DB_AUTH_TOKEN?.trim();&#10;	if (authToken === undefined) {&#10;		throw new Error(&quot;LIBSQL_DB_AUTH_TOKEN env var is not defined&quot;);&#10;	}&#10;&#10;	return createClient({ url, authToken });&#10;}&#10;&#10;function buildRouter(env: Env): RouterType {&#10;	const router = Router();&#10;&#10;	router.get(&quot;/users&quot;, async () =&gt; {&#10;		const client = buildLibsqlClient(env);&#10;		const rs = await client.execute(&quot;select * from example_users&quot;);&#10;		return Response.json(rs);&#10;	});&#10;&#10;	router.get(&quot;/add-user&quot;, async (request) =&gt; {&#10;		const client = buildLibsqlClient(env);&#10;		const email = request.query.email;&#10;		if (email === undefined) {&#10;			return new Response(&quot;Missing email&quot;, { status: 400 });&#10;		}&#10;		if (typeof email !== &quot;string&quot;) {&#10;			return new Response(&quot;email must be a single string&quot;, { status: 400 });&#10;		}&#10;		if (email.length === 0) {&#10;			return new Response(&quot;email length must be &gt; 0&quot;, { status: 400 });&#10;		}&#10;&#10;		try {&#10;			await client.execute({&#10;				sql: &quot;insert into example_users values (?)&quot;,&#10;				args: [email],&#10;			});&#10;		} catch (e) {&#10;			console.error(e);&#10;			return new Response(&quot;database insert failed&quot;);&#10;		}&#10;&#10;		return new Response(&quot;Added&quot;);&#10;	});&#10;&#10;	router.all(&quot;*&quot;, () =&gt; new Response(&quot;Not Found.&quot;, { status: 404 }));&#10;&#10;	return router;&#10;}&#10;</code></pre>
<p>Save your <code>src/index.ts</code> file with your changes.</p>
<p>Note:</p>
<ul>
<li>The libSQL client library import '@libsql/client/web' must be imported exactly as shown when working with Cloudflare workers. The non-web import will not work in the Workers environment.</li>
<li>The <code>Env</code> interface contains the environment variable and secret you defined earlier.</li>
<li>The <code>Env</code> interface also caches the libSQL client object and router, which are created on the first request to the Worker.</li>
<li>The <code>/users</code> route fetches all rows from the <code>example_users</code> table you created in the Turso shell. It simply serializes the <code>ResultSet</code> object as JSON directly to the caller.</li>
<li>The <code>/add-user</code> route inserts a new row using a value provided in the query string.</li>
</ul>
<p>With your environment configured and your code ready, you will now test your Worker locally before you deploy.</p>
<h2 id="run-the-worker-locally-with-wrangler">Run the Worker locally with Wrangler</h2>
<p>To run a local instance of our Worker (entirely on your machine), run the following command:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>You should be able to review output similar to the following:</p>
<pre tabindex="0"><code class="language-txt">Your worker has access to the following bindings:&#10;&#45; Vars:&#10;  &#45; LIBSQL_DB_URL: &quot;your-url&quot;&#10;⎔ Starting a local server...&#10;╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮&#10;│ [b] open a browser, [d] open Devtools, [l] turn off local mode, [c] clear console, [x] to exit                                                                  	│&#10;╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯&#10;Debugger listening on ws://127.0.0.1:61918/1064babd-bc9d-4bed-b171-b35dab3b7680&#10;For help, see: https://nodejs.org/en/docs/inspector&#10;Debugger attached.&#10;[mf:inf] Worker reloaded! (40.25KiB)&#10;[mf:inf] Listening on 0.0.0.0:8787&#10;[mf:inf] - http://127.0.0.1:8787&#10;[mf:inf] - http://192.168.1.136:8787&#10;[mf:inf] Updated `Request.cf` object cache!&#10;</code></pre>
<p>The localhost address — the one with <code>127.0.0.1</code> in it — is a web-server running locally on your machine.</p>
<p>Connect to it and validate your Worker returns the email address you inserted when you created your <code>example_users</code> table by visiting the <code>/users</code> route in your browser: <a href="http://127.0.0.1:8787/users">http://127.0.0.1:8787/users</a>.</p>
<p>You should see JSON similar to the following containing the data from the <code>example_users</code> table:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;columns&quot;: [&quot;email&quot;],&#10;	&quot;rows&quot;: [{ &quot;email&quot;: &quot;foo@bar.com&quot; }],&#10;	&quot;rowsAffected&quot;: 0&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16079.md")
</aside>
<p>Test the <code>/add-users</code> route and pass it an email address to insert: <a href="http://127.0.0.1:8787/add-user?email=test@test.com.">http://127.0.0.1:8787/add-user?email=test@test.com</a></p>
<p>You should see the text <code>“Added”</code>. If you load the first URL with the <code>/users</code> route again (<a href="http://127.0.0.1:8787/users">http://127.0.0.1:8787/users</a>), it will show the newly added row. You can repeat this as many times as you like. Note that due to its design, your application will not stop you from adding duplicate email addresses.</p>
<p>Quit Wrangler by typing <code>q</code> into the shell where it was started.</p>
<h2 id="deploy-to-cloudflare">Deploy to Cloudflare</h2>
<p>After you have validated that your Worker can connect to your Turso database, deploy your Worker. Run the following Wrangler command to deploy your Worker to the Cloudflare global network:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>The first time you run this command, it will launch a browser, ask you to sign in with your Cloudflare account, and grant permissions to Wrangler.</p>
<p>The <code>deploy</code> command will output the following:</p>
<pre tabindex="0"><code class="language-txt">Your worker has access to the following bindings:&#10;&#45; Vars:&#10;  &#45; LIBSQL_DB_URL: &quot;your-url&quot;&#10;...&#10;Published worker-turso-ts (0.19 sec)&#10;  https://worker-turso-ts.&lt;your-Workers-subdomain&gt;.workers.dev&#10;Current Deployment ID: f9e6b48f-5aac-40bd-8f44-8a40be2212ff&#10;</code></pre>
<p>You have now deployed a Worker that can connect to your Turso database, query it, and insert new data.</p>
<h2 id="optional-clean-up">Optional: Clean up</h2>
<p>To clean up the resources you created as part of this tutorial:</p>
<ul>
<li>If you do not want to keep this Worker, run <code>npx wrangler delete worker-turso-ts</code> to delete the deployed Worker.</li>
<li>You can also delete your Turso database via <code>turso db destroy my-db</code>.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li>Find the <a href="https://github.com/cloudflare/workers-sdk/tree/main/templates/worker-turso-ts/">complete project source code on GitHub</a>.</li>
<li>Understand how to <a href="/workers/observability/">debug your Cloudflare Worker</a>.</li>
<li>Join the <a href="https://discord.cloudflare.com">Cloudflare Developer Discord</a>.</li>
<li>Join the <a href="https://discord.com/invite/4B5D7hYwub">ChiselStrike (Turso) Discord</a>.</li>
</ul>
