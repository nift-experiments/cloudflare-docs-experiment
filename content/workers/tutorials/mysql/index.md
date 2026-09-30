<p>In this tutorial, you will learn how to create a Cloudflare Workers application and connect it to a MySQL database using <a href="/workers/runtime-apis/tcp-sockets/">TCP Sockets</a> and <a href="/hyperdrive/">Hyperdrive</a>. The Workers application you create in this tutorial will interact with a product database inside of MySQL.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/16061.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>To continue:</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> if you have not already.</li>
<li>Install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>.</li>
<li>Install <a href="https://nodejs.org/en/"><code>Node.js</code></a>. Use a Node version manager like <a href="https://volta.sh/">Volta</a> or <a href="https://github.com/nvm-sh/nvm">nvm</a> to avoid permission issues and change Node.js versions. <a href="/workers/wrangler/install-and-update/">Wrangler</a> requires a Node version of <code>16.17.0</code> or later.</li>
<li>Make sure you have access to a MySQL database.</li>
</ol>
<h2 id="1-create-a-worker-application"><ol>
<li>Create a Worker application</li>
</ol></h2>
<p>First, use the <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare"><code>create-cloudflare</code> CLI</a> to create a new Worker application. To do this, open a terminal window and run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- mysql-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- mysql-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare mysql-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare mysql-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest mysql-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest mysql-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This will prompt you to install the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code></a> package and lead you through a setup wizard.</p>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>If you choose to deploy, you will be asked to authenticate (if not logged in already), and your project will be deployed. If you deploy, you can still modify your Worker code and deploy again at the end of this tutorial.</p>
<p>Now, move into the newly created directory:</p>
<pre><code class="language-sh">cd mysql-tutorial&#10;</code></pre>
<h2 id="2-enable-node-js-compatibility"><ol start="2">
<li>Enable Node.js compatibility</li>
</ol></h2>
<p><a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> is required for database drivers, including mysql2, and needs to be configured for your Workers project.</p>
<p>For compatibility dates of <code>2026-08-04</code> or later, Workers and Pages projects enable both <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> by default. Built-in runtime APIs and polyfills are available without additional configuration. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date.</p>
<p>If your compatibility date is before <code>2026-08-04</code>, add the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code></a> <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">compatibility flag</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to opt in:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16062.md")
</div>
<p>To turn off <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> completely for a compatibility date of <code>2026-08-04</code> or later, remove the positive flags if present. Then add both <code>no_nodejs_compat</code> and <code>no_nodejs_compat_v2</code>. For configuration examples, refer to the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>.</p>
<h2 id="3-create-a-hyperdrive-configuration"><ol start="3">
<li>Create a Hyperdrive configuration</li>
</ol></h2>
<p>Create a Hyperdrive configuration using the connection string for your MySQL database.</p>
<pre><code class="language-bash">npx wrangler hyperdrive create &lt;NAME_OF_HYPERDRIVE_CONFIG&gt; --connection-string=&quot;mysql://user:password@HOSTNAME_OR_IP_ADDRESS:PORT/database_name&quot;&#10;</code></pre>
<p>This command outputs the Hyperdrive configuration <code>id</code> that will be used for your Hyperdrive <a href="/workers/runtime-apis/bindings/">binding</a>. Set up your binding by specifying the <code>id</code> in the Wrangler file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16063.md")
</div>
<h2 id="4-query-your-database-from-your-worker"><ol start="4">
<li>Query your database from your Worker</li>
</ol></h2>
<p>Install the <a href="https://github.com/sidorares/node-mysql2">mysql2</a> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16060.md")
</aside>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16064.md")
</div>
<p>Create a new <code>connection</code> instance and pass the Hyperdrive parameters:</p>
<pre><code class="language-ts">// mysql2 v3.13.0 or later is required&#10;import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new connection on each request. Hyperdrive maintains the underlying&#10;		// database connection pool, so creating a new connection is fast.&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;&#10;			// Required to enable mysql2 compatibility for Workers&#10;			disableEval: true,&#10;		});&#10;&#10;		try {&#10;			// Sample query&#10;			const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;			// Return result rows as JSON&#10;			return Response.json({ results, fields });&#10;		} catch (e) {&#10;			console.error(e);&#10;			return Response.json(&#10;				{ error: e instanceof Error ? e.message : e },&#10;				{ status: 500 },&#10;			);&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16059.md")
</aside>
<h2 id="5-deploy-your-worker"><ol start="5">
<li>Deploy your Worker</li>
</ol></h2>
<p>Run the following command to deploy your Worker:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your application is now live and accessible at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<h2 id="next-steps">Next steps</h2>
<p>To build more with databases and Workers, refer to <a href="/workers/tutorials">Tutorials</a> and explore the <a href="/workers/databases">Databases documentation</a>.</p>
<p>If you have any questions, need assistance, or would like to share your project, join the Cloudflare Developer community on <a href="https://discord.cloudflare.com">Discord</a> to connect with fellow developers and the Cloudflare team.</p>
