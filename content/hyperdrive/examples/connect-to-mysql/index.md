<p>Hyperdrive supports MySQL and MySQL-compatible databases, <a href="#supported-drivers">popular drivers</a>, and Object Relational Mapper (ORM) libraries that use those drivers.</p>
<h2 id="create-a-hyperdrive">Create a Hyperdrive</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9124.md")
</aside>
<p>To create a Hyperdrive that connects to an existing MySQL database, use the <a href="/workers/wrangler/install-and-update/">Wrangler</a> CLI or the <a href="https://dash.cloudflare.com/?to=/:account/workers/hyperdrive">Cloudflare dashboard</a>.</p>
<p>When using Wrangler, replace the placeholder value provided to <code>--connection-string</code> with the connection string for your database:</p>
<pre><code class="language-sh">&#35; wrangler v3.11 and above required&#10;npx wrangler hyperdrive create my-first-hyperdrive --connection-string=&quot;mysql://user:password@database.host.example.com:3306/databasenamehere&quot;&#10;</code></pre>
<p>The command above will output the ID of your Hyperdrive, which you will need to set in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> for your Workers project:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9125.md")
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
<td>mysql2 (<strong>recommended</strong>)</td>
<td><a href="https://github.com/sidorares/node-mysql2">mysql2 documentation</a></td>
<td><code>mysql2@3.13.0</code></td>
<td>Supported in both Workers &amp; Pages. Using the Promise API is recommended.</td>
</tr>
<tr>
<td>mysql</td>
<td><a href="https://github.com/mysqljs/mysql">mysql documentation</a></td>
<td><code>mysql@2.18.0</code></td>
<td>Requires <code>compatibility_flags = [&quot;nodejs_compat&quot;]</code> and <code>compatibility_date = &quot;2024-09-23&quot;</code> - refer to <a href="/workers/runtime-apis/nodejs">Node.js compatibility</a>. Requires wrangler <code>3.78.7</code> or later.</td>
</tr>
<tr>
<td>Drizzle</td>
<td><a href="https://orm.drizzle.team/">Drizzle documentation</a></td>
<td>Requires <code>mysql2@3.13.0</code></td>
<td></td>
</tr>
<tr>
<td>Kysely</td>
<td><a href="https://kysely.dev/">Kysely documentation</a></td>
<td>Requires <code>mysql2@3.13.0</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>^ <em>The marked libraries can use either mysql or mysql2 as a dependency.</em></p>
<p>Other drivers and ORMs not listed may also be supported: this list is not exhaustive.</p>
<h3 id="database-drivers-and-node-js-compatibility">Database drivers and Node.js compatibility</h3>
<p><a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> is required for database drivers, including mysql and mysql2, and needs to be configured for your Workers project.</p>
<p>For compatibility dates of <code>2026-08-04</code> or later, Workers and Pages projects enable both <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> by default. Built-in runtime APIs and polyfills are available without additional configuration. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date.</p>
<p>If your compatibility date is before <code>2026-08-04</code>, add the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code></a> <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">compatibility flag</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to opt in:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9126.md")
</div>
<p>To turn off <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> completely for a compatibility date of <code>2026-08-04</code> or later, remove the positive flags if present. Then add both <code>no_nodejs_compat</code> and <code>no_nodejs_compat_v2</code>. For configuration examples, refer to the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>.</p>
<h2 id="supported-tls-ssl-modes">Supported TLS (SSL) modes</h2>
<p>Hyperdrive supports the following MySQL TLS/SSL connection modes when connecting to your origin database:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Supported</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>DISABLED</code></td>
<td>No</td>
<td>Hyperdrive does not support insecure plain text connections.</td>
</tr>
<tr>
<td><code>PREFERRED</code></td>
<td>No (use <code>REQUIRED</code>)</td>
<td>Hyperdrive will always use TLS.</td>
</tr>
<tr>
<td><code>REQUIRED</code></td>
<td>Yes (default)</td>
<td>TLS is required, and server certificates are validated (based on WebPKI).</td>
</tr>
<tr>
<td><code>VERIFY_CA</code></td>
<td>Yes</td>
<td>Verifies the server's TLS certificate is signed by a root CA on the client.</td>
</tr>
<tr>
<td><code>VERIFY_IDENTITY</code></td>
<td>Yes</td>
<td>In addition to <code>VERIFY_CA</code> checks, Hyperdrive requires the database hostname to match a Subject Alternative Name (SAN) or Common Name (CN) on the certificate.</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">SSL/TLS certificates</a> documentation for details on how to configure <code>VERIFY_CA</code> or <code>VERIFY_IDENTITY</code> TLS (SSL) modes for Hyperdrive.</p>
<h2 id="driver-examples">Driver examples</h2>
<p>The following examples show you how to:</p>
<ol>
<li>Create a database client with a database driver.</li>
<li>Pass the Hyperdrive connection string and connect to the database.</li>
<li>Query your database via Hyperdrive.</li>
</ol>
<h3 id="mysql2"><code>mysql2</code></h3>
<p>The following Workers code shows you how to use <a href="https://github.com/sidorares/node-mysql2">mysql2</a> with Hyperdrive using the Promise API.</p>
<p>Install the <a href="https://github.com/sidorares/node-mysql2">mysql2</a> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9123.md")
</aside>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9127.md")
</div>
<p>Create a new <code>connection</code> instance and pass the Hyperdrive parameters:</p>
<pre><code class="language-ts">// mysql2 v3.13.0 or later is required&#10;import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new connection on each request. Hyperdrive maintains the underlying&#10;		// database connection pool, so creating a new connection is fast.&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;&#10;			// Required to enable mysql2 compatibility for Workers&#10;			disableEval: true,&#10;		});&#10;&#10;		try {&#10;			// Sample query&#10;			const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;			// Return result rows as JSON&#10;			return Response.json({ results, fields });&#10;		} catch (e) {&#10;			console.error(e);&#10;			return Response.json(&#10;				{ error: e instanceof Error ? e.message : e },&#10;				{ status: 500 },&#10;			);&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9122.md")
</aside>
<h3 id="mysql"><code>mysql</code></h3>
<p>The following Workers code shows you how to use <a href="https://github.com/mysqljs/mysql">mysql</a> with Hyperdrive.</p>
<p>Install the <a href="https://github.com/mysqljs/mysql">mysql</a> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i mysql</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i mysql" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add mysql</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add mysql" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add mysql</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add mysql" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add mysql</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add mysql" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9128.md")
</div>
<p>Create a new connection and pass the Hyperdrive parameters:</p>
<pre><code class="language-ts">import { createConnection } from &quot;mysql&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const result = await new Promise&lt;any&gt;((resolve) =&gt; {&#10;			// Create a connection using the mysql driver with the Hyperdrive credentials (only accessible from your Worker).&#10;			const connection = createConnection({&#10;				host: env.HYPERDRIVE.host,&#10;				user: env.HYPERDRIVE.user,&#10;				password: env.HYPERDRIVE.password,&#10;				database: env.HYPERDRIVE.database,&#10;				port: env.HYPERDRIVE.port,&#10;			});&#10;&#10;			connection.connect((error: { message: string }) =&gt; {&#10;				if (error) {&#10;					throw new Error(error.message);&#10;				}&#10;&#10;				// Sample query&#10;				connection.query(&quot;SHOW tables;&quot;, [], (error, rows, fields) =&gt; {&#10;					resolve({ fields, rows });&#10;				});&#10;			});&#10;		});&#10;&#10;		// Return result  as JSON&#10;		return new Response(JSON.stringify(result), {&#10;			headers: {&#10;				&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="identify-connections-from-hyperdrive">Identify connections from Hyperdrive</h2>
<p>To identify active connections to your MySQL database server from Hyperdrive:</p>
<ul>
<li>Hyperdrive's connections to your database will show up with <code>Cloudflare Hyperdrive</code> in the <code>PROGRAM_NAME</code> column in the <code>performance_schema.threads</code> table.</li>
<li>Run <code>SELECT DISTINCT USER, HOST, PROGRAM_NAME FROM performance_schema.threads WHERE PROGRAM_NAME = 'Cloudflare Hyperdrive'</code> to show whether Hyperdrive is currently holding a connection (or connections) open to your database.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Refer to the list of <a href="/workers/databases/connecting-to-databases/">supported database integrations</a> to understand other ways to connect to existing databases.</li>
<li>Learn more about how to use the <a href="/workers/runtime-apis/tcp-sockets">Socket API</a> in a Worker.</li>
<li>Understand the <a href="/workers/reference/protocols/">protocols supported by Workers</a>.</li>
</ul>
