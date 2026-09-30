<p>In this tutorial, you will learn how to create a Cloudflare Workers application and connect it to a PostgreSQL database using <a href="/workers/runtime-apis/tcp-sockets/">TCP Sockets</a> and <a href="/hyperdrive/">Hyperdrive</a>. The Workers application you create in this tutorial will interact with a product database inside of PostgreSQL.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To continue:</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> if you have not already.</li>
<li>Install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>.</li>
<li>Install <a href="https://nodejs.org/en/"><code>Node.js</code></a>. Use a Node version manager like <a href="https://volta.sh/">Volta</a> or <a href="https://github.com/nvm-sh/nvm">nvm</a> to avoid permission issues and change Node.js versions. <a href="/workers/wrangler/install-and-update/">Wrangler</a> requires a Node version of <code>16.17.0</code> or later.</li>
<li>Make sure you have access to a PostgreSQL database.</li>
</ol>
<h2 id="1-create-a-worker-application"><ol>
<li>Create a Worker application</li>
</ol></h2>
<p>First, use the <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare"><code>create-cloudflare</code> CLI</a> to create a new Worker application. To do this, open a terminal window and run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- postgres-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- postgres-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare postgres-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare postgres-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest postgres-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest postgres-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
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
<pre><code class="language-sh">cd postgres-tutorial&#10;</code></pre>
<h3 id="enable-node-js-compatibility">Enable Node.js compatibility</h3>
<p><a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> is required for database drivers, including Postgres.js, and needs to be configured for your Workers project.</p>
<p>For compatibility dates of <code>2026-08-04</code> or later, Workers and Pages projects enable both <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> by default. Built-in runtime APIs and polyfills are available without additional configuration. These flags are not used for these compatibility dates. Existing projects do not need to remove them when updating their compatibility date.</p>
<p>If your compatibility date is before <code>2026-08-04</code>, add the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag"><code>nodejs_compat</code></a> <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">compatibility flag</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to opt in:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16056.md")
</div>
<p>To turn off <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> completely for a compatibility date of <code>2026-08-04</code> or later, remove the positive flags if present. Then add both <code>no_nodejs_compat</code> and <code>no_nodejs_compat_v2</code>. For configuration examples, refer to the <a href="/workers/configuration/compatibility-flags/#nodejs-compatibility-flag">Node.js compatibility flag</a>.</p>
<h2 id="2-add-the-postgresql-connection-library"><ol start="2">
<li>Add the PostgreSQL connection library</li>
</ol></h2>
<p>To connect to a PostgreSQL database, you will need the <code>pg</code> library. In your Worker application directory, run the following command to install the library:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add pg" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Next, install the TypeScript types for the <code>pg</code> library to enable type checking and autocompletion in your TypeScript code:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @types/pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @types/pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @types/pg" aria-label="Copy to clipboard">Copy</button></div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16055.md")
</aside>
<h2 id="3-configure-the-connection-to-the-postgresql-database"><ol start="3">
<li>Configure the connection to the PostgreSQL database</li>
</ol></h2>
<p>Choose one of the two methods to connect to your PostgreSQL database:</p>
<ol>
<li><a href="#use-a-connection-string">Use a connection string</a>.</li>
<li><a href="#set-explicit-parameters">Set explicit parameters</a>.</li>
</ol>
<h3 id="use-a-connection-string">Use a connection string</h3>
<p>A connection string contains all the information needed to connect to a database. It is a URL that contains the following information:</p>
<pre><code>postgresql://username:password@host:port/database&#10;</code></pre>
<p>Replace <code>username</code>, <code>password</code>, <code>host</code>, <code>port</code>, and <code>database</code> with the appropriate values for your PostgreSQL database.</p>
<p>Set your connection string as a <a href="/workers/configuration/secrets/">secret</a> so that it is not stored as plain text. Use <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret put</code></a> with the example variable name <code>DB_URL</code>:</p>
<pre><code class="language-sh">npx wrangler secret put DB_URL&#10;</code></pre>
<pre><code class="language-sh">➜  wrangler secret put DB_URL&#10;&#45;------------------------------------------------------&#10;? Enter a secret value: › ********************&#10;✨ Success! Uploaded secret DB_URL&#10;</code></pre>
<p>Set your <code>DB_URL</code> secret locally in a <code>.dev.vars</code> file as documented in <a href="/workers/configuration/secrets/">Local Development with Secrets</a>.</p>
<pre><code class="language-toml">DB_URL=&quot;&lt;ENTER YOUR POSTGRESQL CONNECTION STRING&gt;&quot;&#10;</code></pre>
<h3 id="set-explicit-parameters">Set explicit parameters</h3>
<p>Configure each database parameter as an <a href="/workers/configuration/environment-variables/">environment variable</a> via the <a href="/workers/configuration/environment-variables/#add-environment-variables-via-the-dashboard">Cloudflare dashboard</a> or in your Wrangler file. Refer to an example of a Wrangler file configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16057.md")
</div>
<p>To set your password as a <a href="/workers/configuration/secrets/">secret</a> so that it is not stored as plain text, use <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret put</code></a>. <code>DB_PASSWORD</code> is an example variable name for this secret to be accessed in your Worker:</p>
<pre><code class="language-sh">npx wrangler secret put DB_PASSWORD&#10;</code></pre>
<pre><code class="language-sh">&#45;------------------------------------------------------&#10;? Enter a secret value: › ********************&#10;✨ Success! Uploaded secret DB_PASSWORD&#10;</code></pre>
<h2 id="4-connect-to-the-postgresql-database-in-the-worker"><ol start="4">
<li>Connect to the PostgreSQL database in the Worker</li>
</ol></h2>
<p>Open your Worker's main file (for example, <code>worker.ts</code>) and import the <code>Client</code> class from the <code>pg</code> library:</p>
<pre><code class="language-typescript">import { Client } from &quot;pg&quot;;&#10;</code></pre>
<p>In the <code>fetch</code> event handler, connect to the PostgreSQL database using your chosen method, either the connection string or the explicit parameters.</p>
<h3 id="use-a-connection-string-1">Use a connection string</h3>
<pre><code class="language-typescript">// create a new Client instance using the connection string&#10;const sql = new Client({ connectionString: env.DB_URL });&#10;// connect to the PostgreSQL database&#10;await sql.connect();&#10;</code></pre>
<h3 id="set-explicit-parameters-1">Set explicit parameters</h3>
<pre><code class="language-typescript">// create a new Client instance using explicit parameters&#10;const sql = new Client({&#10;	username: env.DB_USERNAME,&#10;	password: env.DB_PASSWORD,&#10;	host: env.DB_HOST,&#10;	port: env.DB_PORT,&#10;	database: env.DB_NAME,&#10;	ssl: true, // Enable SSL for secure connections&#10;});&#10;// connect to the PostgreSQL database&#10;await sql.connect();&#10;</code></pre>
<h2 id="5-interact-with-the-products-database"><ol start="5">
<li>Interact with the products database</li>
</ol></h2>
<p>To demonstrate how to interact with the products database, you will fetch data from the <code>products</code> table by querying the table when a request is received.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16054.md")
</aside>
<p>Replace the existing code in your <code>worker.ts</code> file with the following code:</p>
<pre><code class="language-typescript">import { Client } from &quot;pg&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new Client instance using the connection string&#10;		// or explicit parameters as shown in the previous steps.&#10;		// Here, we are using the connection string method.&#10;		const sql = new Client({&#10;			connectionString: env.DB_URL,&#10;		});&#10;        // Connect to the PostgreSQL database&#10;        await sql.connect();&#10;&#10;        // Query the products table&#10;        const result = await sql.query(&quot;SELECT * FROM products&quot;);&#10;&#10;        // Return the result as JSON&#10;        return new Response(JSON.stringify(result.rows), {&#10;            headers: {&#10;                &quot;Content-Type&quot;: &quot;application/json&quot;,&#10;            },&#10;        });&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>This code establishes a connection to the PostgreSQL database within your Worker application and queries the <code>products</code> table, returning the results as a JSON response.</p>
<h2 id="6-deploy-your-worker"><ol start="6">
<li>Deploy your Worker</li>
</ol></h2>
<p>Run the following command to deploy your Worker:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your application is now live and accessible at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<p>After deploying, you can interact with your PostgreSQL products database using your Cloudflare Worker. Whenever a request is made to your Worker's URL, it will fetch data from the <code>products</code> table and return it as a JSON response. You can modify the query as needed to retrieve the desired data from your products database.</p>
<h2 id="7-insert-a-new-row-into-the-products-database"><ol start="7">
<li>Insert a new row into the products database</li>
</ol></h2>
<p>To insert a new row into the <code>products</code> table, create a new API endpoint in your Worker that handles a <code>POST</code> request. When a <code>POST</code> request is received with a JSON payload, the Worker will insert a new row into the <code>products</code> table with the provided data.</p>
<p>Assume the <code>products</code> table has the following columns: <code>id</code>, <code>name</code>, <code>description</code>, and <code>price</code>.</p>
<p>Add the following code snippet inside the <code>fetch</code> event handler in your <code>worker.ts</code> file, before the existing query code:</p>
<pre><code class="language-typescript">import { Client } from &quot;pg&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new Client instance using the connection string&#10;		// or explicit parameters as shown in the previous steps.&#10;		// Here, we are using the connection string method.&#10;		const sql = new Client({&#10;			connectionString: env.DB_URL,&#10;		});&#10;        // Connect to the PostgreSQL database&#10;        await sql.connect();&#10;&#10;        const url = new URL(request.url);&#10;        if (request.method === &quot;POST&quot; &amp;&amp; url.pathname === &quot;/products&quot;) {&#10;            // Parse the request&#x27;s JSON payload&#10;            const productData = (await request.json()) as {&#10;                name: string;&#10;                description: string;&#10;                price: number;&#10;            };&#10;&#10;            const name = productData.name,&#10;                description = productData.description,&#10;                price = productData.price;&#10;&#10;            // Insert the new product into the products table&#10;            const insertResult = await sql.query(&#10;                `INSERT INTO products(name, description, price) VALUES($1, $2, $3)&#10;    RETURNING *`,&#10;                [name, description, price],&#10;            );&#10;&#10;            // Return the inserted row as JSON&#10;            return new Response(JSON.stringify(insertResult.rows), {&#10;                headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;            });&#10;        }&#10;&#10;        // Query the products table&#10;        const result = await sql.query(&quot;SELECT * FROM products&quot;);&#10;&#10;        // Return the result as JSON&#10;        return new Response(JSON.stringify(result.rows), {&#10;            headers: {&#10;                &quot;Content-Type&quot;: &quot;application/json&quot;,&#10;            },&#10;        });&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>This code snippet does the following:</p>
<ol>
<li>Checks if the request is a <code>POST</code> request and the URL path is <code>/products</code>.</li>
<li>Parses the JSON payload from the request.</li>
<li>Constructs an <code>INSERT</code> SQL query using the provided product data.</li>
<li>Executes the query, inserting the new row into the <code>products</code> table.</li>
<li>Returns the inserted row as a JSON response.</li>
</ol>
<p>Now, when you send a <code>POST</code> request to your Worker's URL with the <code>/products</code> path and a JSON payload, the Worker will insert a new row into the <code>products</code> table with the provided data. When a request to <code>/</code> is made, the Worker will return all products in the database.</p>
<p>After making these changes, deploy the Worker again by running:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>You can now use your Cloudflare Worker to insert new rows into the <code>products</code> table. To test this functionality, send a <code>POST</code> request to your Worker's URL with the <code>/products</code> path, along with a JSON payload containing the new product data:</p>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;Sample Product&quot;,&#10;	&quot;description&quot;: &quot;This is a sample product&quot;,&#10;	&quot;price&quot;: 19.99&#10;}&#10;</code></pre>
<p>You have successfully created a Cloudflare Worker that connects to a PostgreSQL database and handles fetching data and inserting new rows into a products table.</p>
<h2 id="8-use-hyperdrive-to-accelerate-queries"><ol start="8">
<li>Use Hyperdrive to accelerate queries</li>
</ol></h2>
<p>Create a Hyperdrive configuration using the connection string for your PostgreSQL database.</p>
<pre><code class="language-bash">npx wrangler hyperdrive create &lt;NAME_OF_HYPERDRIVE_CONFIG&gt; --connection-string=&quot;postgres://user:password@HOSTNAME_OR_IP_ADDRESS:PORT/database_name&quot; --caching-disabled&#10;</code></pre>
<p>This command outputs the Hyperdrive configuration <code>id</code> that will be used for your Hyperdrive <a href="/workers/runtime-apis/bindings/">binding</a>. Set up your binding by specifying the <code>id</code> in the Wrangler file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16058.md")
</div>
<p>Create the types for your Hyperdrive binding using the following command:</p>
<pre><code class="language-bash">npx wrangler types&#10;</code></pre>
<p>Replace your existing connection string in your Worker code with the Hyperdrive connection string.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const sql = new Client({connectionString: env.HYPERDRIVE.connectionString})&#10;&#10;		const url = new URL(request.url);&#10;&#10;		//rest of the routes and database queries&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="9-redeploy-your-worker"><ol start="9">
<li>Redeploy your Worker</li>
</ol></h2>
<p>Run the following command to deploy your Worker:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your Worker application is now live and accessible at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>, using Hyperdrive. Hyperdrive accelerates database queries by pooling your connections and caching your requests across the globe.</p>
<h2 id="next-steps">Next steps</h2>
<p>To build more with databases and Workers, refer to <a href="/workers/tutorials">Tutorials</a> and explore the <a href="/workers/databases">Databases documentation</a>.</p>
<p>If you have any questions, need assistance, or would like to share your project, join the Cloudflare Developer community on <a href="https://discord.cloudflare.com">Discord</a> to connect with fellow developers and the Cloudflare team.</p>
