<p class="article-summary">Connect Hyperdrive to an Azure Database for MySQL instance.</p>
<p>This example shows you how to connect Hyperdrive to an Azure Database for MySQL instance.</p>
<h2 id="1-allow-hyperdrive-access"><ol>
<li>Allow Hyperdrive access</li>
</ol></h2>
<p>To allow Hyperdrive to connect to your database, you will need to ensure that Hyperdrive has valid credentials and network access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9153.md")
</aside>
<h3 id="azure-portal">Azure Portal</h3>
<h4 id="public-access-networking">Public access networking</h4>
<p>To connect to your Azure Database for MySQL instance using public Internet connectivity:</p>
<ol>
<li>In the <a href="https://portal.azure.com/">Azure Portal</a>, select the instance you want Hyperdrive to connect to.</li>
<li>Expand <strong>Settings</strong> &gt; <strong>Networking</strong> &gt; ensure <strong>Public access</strong> is enabled &gt; in <strong>Firewall rules</strong> add <code>0.0.0.0</code> as <strong>Start IP address</strong> and <code>255.255.255.255</code> as <strong>End IP address</strong>.</li>
<li>Select <strong>Save</strong> to persist your changes.</li>
<li>Select <strong>Overview</strong> from the sidebar and note down the <strong>Server name</strong> of your instance.</li>
</ol>
<p>With the username, password, server name, and database name (default: <code>mysql</code>), you can now create a Hyperdrive database configuration.</p>
<h4 id="private-access-networking">Private access networking</h4>
<p>To connect to a private Azure Database for MySQL instance, refer to <a href="/hyperdrive/configuration/connect-to-private-database/">Connect to a private database using Tunnel</a>.</p>
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
<pre><code class="language-txt">mysql://USERNAME:PASSWORD@HOSTNAME_OR_IP_ADDRESS:PORT/database_name&#10;</code></pre>
<p>Most database providers will provide a connection string you can copy-and-paste directly into Hyperdrive.</p>
<p>To create a Hyperdrive configuration with the <a href="/workers/wrangler/install-and-update/">Wrangler CLI</a>, open your terminal and run the following command.</p>
<ul>
<li>Replace &lt;NAME_OF_HYPERDRIVE_CONFIG&gt; with a name for your Hyperdrive configuration and paste the connection string provided from your database host, or,</li>
<li>Replace <code>user</code>, <code>password</code>, <code>HOSTNAME_OR_IP_ADDRESS</code>, <code>port</code>, and <code>database_name</code> placeholders with those specific to your database:</li>
</ul>
<pre><code class="language-sh">npx wrangler hyperdrive create &lt;NAME_OF_HYPERDRIVE_CONFIG&gt; --connection-string=&quot;mysql://user:password@HOSTNAME_OR_IP_ADDRESS:PORT/database_name&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9152.md")
</aside>
<p>This command outputs a binding for the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9154.md")
</div>
<h2 id="3-use-hyperdrive-from-your-worker"><ol start="3">
<li>Use Hyperdrive from your Worker</li>
</ol></h2>
<p>Install the <a href="https://github.com/sidorares/node-mysql2">mysql2</a> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9151.md")
</aside>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9155.md")
</div>
<p>Create a new <code>connection</code> instance and pass the Hyperdrive parameters:</p>
<pre><code class="language-ts">// mysql2 v3.13.0 or later is required&#10;import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new connection on each request. Hyperdrive maintains the underlying&#10;		// database connection pool, so creating a new connection is fast.&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;&#10;			// Required to enable mysql2 compatibility for Workers&#10;			disableEval: true,&#10;		});&#10;&#10;		try {&#10;			// Sample query&#10;			const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;			// Return result rows as JSON&#10;			return Response.json({ results, fields });&#10;		} catch (e) {&#10;			console.error(e);&#10;			return Response.json(&#10;				{ error: e instanceof Error ? e.message : e },&#10;				{ status: 500 },&#10;			);&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9150.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
