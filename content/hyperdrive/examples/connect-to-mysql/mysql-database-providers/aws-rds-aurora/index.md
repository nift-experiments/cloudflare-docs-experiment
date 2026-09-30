<p class="article-summary">Connect Hyperdrive to an AWS RDS or AWS Aurora MySQL database instance.</p>
<p>This example shows you how to connect Hyperdrive to an Amazon Relational Database Service (Amazon RDS) or Amazon Aurora MySQL database instance.</p>
<h2 id="1-allow-hyperdrive-access"><ol>
<li>Allow Hyperdrive access</li>
</ol></h2>
<p>To allow Hyperdrive to connect to your database, you will need to ensure that Hyperdrive has valid user credentials and network access.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9160.md")
</aside>
<h3 id="aws-console">AWS Console</h3>
<p>When creating or modifying an instance in the AWS console:</p>
<ol>
<li>Configure a <strong>database cluster</strong> and other settings you wish to customize.</li>
<li>Under <strong>Settings</strong> &gt; <strong>Credential settings</strong>, note down the <strong>Master username</strong> and <strong>Master password</strong> (Aurora only).</li>
<li>Under the <strong>Connectivity</strong> header, ensure <strong>Public access</strong> is set to <strong>Yes</strong>.</li>
<li>Select an <strong>Existing VPC security group</strong> that allows public Internet access from <code>0.0.0.0/0</code> to the port your database instance is configured to listen on (default: <code>3306</code> for MySQL instances).</li>
<li>Select <strong>Create database</strong>.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/9159.md")
</aside>
<h3 id="retrieve-the-database-endpoint-aurora">Retrieve the database endpoint (Aurora)</h3>
<p>To retrieve the database endpoint (hostname) for Hyperdrive to connect to:</p>
<ol>
<li>Go to <strong>Databases</strong> view under <strong>RDS</strong> in the AWS console.</li>
<li>Select the database you want Hyperdrive to connect to.</li>
<li>Under the <strong>Endpoints</strong> header, note down the <strong>Endpoint name</strong> with the type <code>Writer</code> and the <strong>Port</strong>.</li>
</ol>
<h3 id="retrieve-the-database-endpoint-rds-mysql">Retrieve the database endpoint (RDS MySQL)</h3>
<p>For regular RDS instances (non-Aurora), you will need to fetch the endpoint and port of the database:</p>
<ol>
<li>Go to <strong>Databases</strong> view under <strong>RDS</strong> in the AWS console.</li>
<li>Select the database you want Hyperdrive to connect to.</li>
<li>Under the <strong>Connectivity &amp; security</strong> header, note down the <strong>Endpoint</strong> and the <strong>Port</strong>.</li>
</ol>
<p>The endpoint will resemble <code>YOUR_DATABASE_NAME.cpuo5rlli58m.AWS_REGION.rds.amazonaws.com</code>, and the port will default to <code>3306</code>.</p>
<h2 id="2-create-your-user"><ol start="2">
<li>Create your user</li>
</ol></h2>
<p>Once your database is created, you will need to create a user for Hyperdrive to connect as. Although you can use the <strong>Master username</strong> configured during initial database creation, best practice is to create a less privileged user.</p>
<p>To create a new user, log in to the database and use the <code>CREATE USER</code> command:</p>
<pre><code class="language-sh">&#35; Log in to the database&#10;mysql -h ENDPOINT_NAME -P PORT -u MASTER_USERNAME -p database_name&#10;</code></pre>
<p>Run the following SQL statements:</p>
<pre><code class="language-sql">&#45;- Create a role for Hyperdrive&#10;CREATE ROLE hyperdrive;&#10;&#10;&#45;- Allow Hyperdrive to connect&#10;GRANT USAGE ON mysql_db.* TO hyperdrive;&#10;&#10;&#45;- Grant database privileges to the hyperdrive role&#10;GRANT ALL PRIVILEGES ON mysql_db.* to hyperdrive;&#10;&#10;&#45;- Create a specific user for Hyperdrive to log in as&#10;CREATE USER &#x27;hyperdrive_user&#x27;@&#x27;%&#x27; IDENTIFIED WITH caching_sha2_password BY &#x27;sufficientlyRandomPassword&#x27;;&#10;&#10;&#45;- Grant this new user the hyperdrive role privileges&#10;GRANT hyperdrive to &#x27;hyperdrive_user&#x27;@&#x27;%&#x27;;&#10;</code></pre>
<p>Refer to AWS' <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.privilege-model.html">documentation on user roles in MySQL</a> for more details.</p>
<p>With a database user, password, database endpoint (hostname and port), and database name, you can now set up Hyperdrive.</p>
<h2 id="3-create-a-database-configuration"><ol start="3">
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
@markup("md", "content/.markup/bodies/9158.md")
</aside>
<p>This command outputs a binding for the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9161.md")
</div>
<h2 id="3-use-hyperdrive-from-your-worker"><ol start="3">
<li>Use Hyperdrive from your Worker</li>
</ol></h2>
<p>Install the <a href="https://github.com/sidorares/node-mysql2">mysql2</a> driver:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add mysql2@&gt;3.13.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add mysql2@&gt;3.13.0" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9157.md")
</aside>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9162.md")
</div>
<p>Create a new <code>connection</code> instance and pass the Hyperdrive parameters:</p>
<pre><code class="language-ts">// mysql2 v3.13.0 or later is required&#10;import { createConnection } from &quot;mysql2/promise&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new connection on each request. Hyperdrive maintains the underlying&#10;		// database connection pool, so creating a new connection is fast.&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;&#10;			// Required to enable mysql2 compatibility for Workers&#10;			disableEval: true,&#10;		});&#10;&#10;		try {&#10;			// Sample query&#10;			const [results, fields] = await connection.query(&quot;SHOW tables;&quot;);&#10;&#10;			// Return result rows as JSON&#10;			return Response.json({ results, fields });&#10;		} catch (e) {&#10;			console.error(e);&#10;			return Response.json(&#10;				{ error: e instanceof Error ? e.message : e },&#10;				{ status: 500 },&#10;			);&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9156.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
