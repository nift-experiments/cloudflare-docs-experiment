<p>Hyperdrive supports PostgreSQL and PostgreSQL-compatible databases, <a href="#supported-drivers">popular drivers</a> and Object Relational Mapper (ORM) libraries that use those drivers.</p>
<h2 id="create-a-hyperdrive">Create a Hyperdrive</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9117.md")
</aside>
<p>To create a Hyperdrive that connects to an existing PostgreSQL database, use the <a href="/workers/wrangler/install-and-update/">wrangler</a> CLI or the <a href="https://dash.cloudflare.com/?to=/:account/workers/hyperdrive">Cloudflare dashboard</a>.</p>
<p>When using wrangler, replace the placeholder value provided to <code>--connection-string</code> with the connection string for your database:</p>
<pre><code class="language-sh">&#35; wrangler v3.11 and above required&#10;npx wrangler hyperdrive create my-first-hyperdrive --connection-string=&quot;postgres://user:password@database.host.example.com:5432/databasenamehere&quot;&#10;</code></pre>
<p>The command above will output the ID of your Hyperdrive, which you will need to set in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for your Workers project:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9118.md")
</div>
<p>This will allow Hyperdrive to generate a dynamic connection string within your Worker that you can pass to your existing database driver. Refer to <a href="#driver-examples">Driver examples</a> to learn how to set up a database driver with Hyperdrive.</p>
<p>Refer to the <a href="/hyperdrive/examples/">Examples documentation</a> for step-by-step guides on how to set up Hyperdrive with several popular database providers.</p>
<h2 id="supported-drivers">Supported drivers</h2>
<p>Hyperdrive uses Workers <a href="/workers/runtime-apis/tcp-sockets/#connect">TCP socket support</a> to support TCP connections to databases. The following table lists the supported database drivers and the minimum version that works with Hyperdrive:</p>
<table>
<thead>
<tr>
<th>Driver</th>
<th>Documentation</th>
<th>Minimum Version Required</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>node-postgres - <code>pg</code> (recommended)</td>
<td><a href="https://node-postgres.com/">node-postgres - <code>pg</code> documentation</a></td>
<td><code>pg@8.13.0</code></td>
<td><code>8.11.4</code> introduced a bug with URL parsing and will not work. <code>8.11.5</code> fixes this. Requires <code>compatibility_flags = [&quot;nodejs_compat&quot;]</code> and <code>compatibility_date = &quot;2024-09-23&quot;</code> - refer to <a href="/workers/runtime-apis/nodejs">Node.js compatibility</a>. Requires wrangler <code>3.78.7</code> or later.</td>
</tr>
<tr>
<td>Postgres.js</td>
<td><a href="https://github.com/porsager/postgres">Postgres.js documentation</a></td>
<td><code>postgres@3.4.4</code></td>
<td>Supported in both Workers &amp; Pages.</td>
</tr>
<tr>
<td>Drizzle</td>
<td><a href="https://orm.drizzle.team/">Drizzle documentation</a></td>
<td><code>0.26.2</code>^</td>
<td></td>
</tr>
<tr>
<td>Kysely</td>
<td><a href="https://kysely.dev/">Kysely documentation</a></td>
<td><code>0.26.3</code>^</td>
<td></td>
</tr>
<tr>
<td><a href="https://github.com/sfackler/rust-postgres">rust-postgres</a></td>
<td><a href="https://docs.rs/postgres/latest/postgres/">rust-postgres documentation</a></td>
<td><code>v0.19.8</code></td>
<td>Use the <a href="https://docs.rs/postgres/latest/postgres/struct.Client.html#method.query_typed"><code>query_typed</code></a> method for best performance.</td>
</tr>
</tbody>
</table>
<p>^ <em>The marked libraries use <code>node-postgres</code> as a dependency.</em></p>
<p>Other drivers and ORMs not listed may also be supported: this list is not exhaustive.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommended-driver">Recommended driver</h3>
@markup("md", "content/.markup/bodies/9116.md")
</aside>
<h3 id="database-drivers-and-node-js-compatibility">Database drivers and Node.js compatibility</h3>
<p><a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> is required for database drivers, including Postgres.js, and needs to be configured for your Workers project.</p>
<p>For compatibility dates of <code>2026-08-04</code> or later, Workers and Pages projects enable both <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> by default. Built-in runtime APIs and polyfills are available without additional configuration. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date.</p>
<p>If your compatibility date is before <code>2026-08-04</code>, add the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code></a> <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">compatibility flag</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to opt in:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9119.md")
</div>
<p>To turn off <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> completely for a compatibility date of <code>2026-08-04</code> or later, remove the positive flags if present. Then add both <code>no_nodejs_compat</code> and <code>no_nodejs_compat_v2</code>. For configuration examples, refer to the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>.</p>
<h2 id="driver-examples">Driver examples</h2>
<p>The following examples show you how to:</p>
<ol>
<li>Create a database client with a database driver.</li>
<li>Pass the Hyperdrive connection string and connect to the database.</li>
<li>Query your database via Hyperdrive.</li>
</ol>
<h3 id="node-postgres-pg">node-postgres / pg</h3>
<p>Install the <code>node-postgres</code> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add pg@&gt;8.16.3</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add pg@&gt;8.16.3" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9115.md")
</aside>
<p>If using TypeScript, install the types package:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @types/pg" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9120.md")
</div>
<p>Create a new <code>Client</code> instance and pass the Hyperdrive <code>connectionString</code>:</p>
<pre><code class="language-ts">// filepath: src/index.ts&#10;import { Client } from &quot;pg&quot;;&#10;&#10;export default {&#10;	async fetch(&#10;		request: Request,&#10;		env: Env,&#10;		ctx: ExecutionContext,&#10;	): Promise&lt;Response&gt; {&#10;		// Create a new client instance for each request. Hyperdrive maintains the&#10;		// underlying database connection pool, so creating a new client is fast.&#10;		const client = new Client({&#10;			connectionString: env.HYPERDRIVE.connectionString,&#10;		});&#10;&#10;		try {&#10;			// Connect to the database&#10;			await client.connect();&#10;&#10;			// Perform a simple query&#10;			const result = await client.query(&quot;SELECT * FROM pg_tables&quot;);&#10;&#10;			return Response.json({&#10;				success: true,&#10;				result: result.rows,&#10;			});&#10;		} catch (error: any) {&#10;			console.error(&quot;Database error:&quot;, error.message);&#10;&#10;			return new Response(&quot;Internal error occurred&quot;, { status: 500 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h3 id="postgres-js">Postgres.js</h3>
<p>Install <a href="https://github.com/porsager/postgres">Postgres.js</a>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i postgres@&gt;3.4.5</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i postgres@&gt;3.4.5" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add postgres@&gt;3.4.5</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add postgres@&gt;3.4.5" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add postgres@&gt;3.4.5</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add postgres@&gt;3.4.5" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add postgres@&gt;3.4.5</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add postgres@&gt;3.4.5" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9114.md")
</aside>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9121.md")
</div>
<p>Create a Worker that connects to your PostgreSQL database via Hyperdrive:</p>
<pre><code class="language-ts">// filepath: src/index.ts&#10;import postgres from &quot;postgres&quot;;&#10;&#10;export default {&#10;	async fetch(&#10;		request: Request,&#10;		env: Env,&#10;		ctx: ExecutionContext,&#10;	): Promise&lt;Response&gt; {&#10;		// Create a database client that connects to your database via Hyperdrive.&#10;		// Hyperdrive maintains the underlying database connection pool,&#10;		// so creating a new client on each request is fast and recommended.&#10;		const sql = postgres(env.HYPERDRIVE.connectionString, {&#10;			// Limit the connections for the Worker request to 5 due to Workers&#x27; limits on concurrent external connections&#10;			max: 5,&#10;			// If you are not using array types in your Postgres schema, disable `fetch_types` to avoid an additional round-trip (unnecessary latency)&#10;			fetch_types: false,&#10;&#10;			// This is set to true by default, but certain query generators such as Kysely or queries using sql.unsafe() will set this to false. Hyperdrive will not cache prepared statements when this option is set to false and will require additional round-trips.  &#10;			prepare: true,&#10;		});&#10;&#10;		try {&#10;			// A very simple test query&#10;			const result = await sql`select * from pg_tables`;&#10;&#10;			// Return result rows as JSON&#10;			return Response.json({ success: true, result: result });&#10;		} catch (e: any) {&#10;			console.error(&quot;Database error:&quot;, e.message);&#10;&#10;			return Response.error();&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="identify-connections-from-hyperdrive">Identify connections from Hyperdrive</h2>
<p>To identify active connections to your Postgres database server from Hyperdrive:</p>
<ul>
<li>Hyperdrive's connections to your database will show up with <code>Cloudflare Hyperdrive</code> as the <code>application_name</code> in the <code>pg_stat_activity</code> table.</li>
<li>Run <code>SELECT DISTINCT usename, application_name FROM pg_stat_activity WHERE application_name = 'Cloudflare Hyperdrive'</code> to show whether Hyperdrive is currently holding a connection (or connections) open to your database.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Refer to the list of <a href="/workers/databases/connecting-to-databases/">supported database integrations</a> to understand other ways to connect to existing databases.</li>
<li>Learn more about how to use the <a href="/workers/runtime-apis/tcp-sockets">Socket API</a> in a Worker.</li>
<li>Understand the <a href="/workers/reference/protocols/">protocols supported by Workers</a>.</li>
</ul>
