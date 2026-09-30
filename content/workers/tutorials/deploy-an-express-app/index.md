<p>In this tutorial, you will learn how to deploy an <a href="https://expressjs.com/">Express.js</a> application on Cloudflare Workers using the <a href="/workers/">Cloudflare Workers platform</a> and <a href="/d1/">D1 database</a>. You will build a Members Registry API with basic Create, Read, Update, and Delete (CRUD) operations. You will use D1 as the database for storing and retrieving member data.</p>
<h2 id="before-you-start">Before you start</h2>
<p>All of the tutorials assume you have already completed the <a href="/workers/get-started/guide/">Get started guide</a>, which gets you set up with a Cloudflare Workers account, <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a>, and <a href="/workers/wrangler/install-and-update/">Wrangler</a>.</p>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the steps and get started quickly, select <strong>Deploy to Cloudflare</strong> below.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/express-on-workers"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers. Use this option if you are familiar with Cloudflare Workers, and wish to skip the step-by-step guidance.</p>
<p>You may wish to manually follow the steps if you are new to Cloudflare Workers.</p>
<h2 id="1-create-a-new-cloudflare-workers-project"><ol>
<li>Create a new Cloudflare Workers project</li>
</ol></h2>
<p>Use <a href="https://developers.cloudflare.com/learning-paths/workers/get-started/c3-and-wrangler/#c3">C3</a>, the command-line tool for Cloudflare's developer products, to create a new directory and initialize a new Worker project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- express-d1-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- express-d1-app" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare express-d1-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare express-d1-app" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest express-d1-app</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest express-d1-app" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Change into your new project directory:</p>
<pre><code class="language-sh">cd express-d1-app&#10;</code></pre>
<h2 id="2-install-express-and-dependencies"><ol start="2">
<li>Install Express and dependencies</li>
</ol></h2>
<p>In this tutorial, you will use <a href="https://expressjs.com/">Express.js</a>, a popular web framework for Node.js. To use Express in a Cloudflare Workers environment, install Express along with the necessary TypeScript types:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i express @types/express</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i express @types/express" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add express @types/express</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add express @types/express" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add express @types/express</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add express @types/express" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add express @types/express</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add express @types/express" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Express.js on Cloudflare Workers requires the <code>nodejs_compat</code> <a href="/workers/configuration/compatibility-flags/">compatibility flag</a>. This flag enables Node.js APIs and allows Express to run on the Workers runtime. Add the following to your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16073.md")
</div>
<h2 id="3-create-a-d1-database"><ol start="3">
<li>Create a D1 database</li>
</ol></h2>
<p>You will now create a D1 database to store member information. Use the <code>wrangler d1 create</code> command to create a new database:</p>
<pre><code class="language-sh">npx wrangler d1 create members-db&#10;</code></pre>
<p>The command will create a new D1 database and ask you the following questions:</p>
<ul>
<li><strong>Would you like Wrangler to add it on your behalf?</strong>: Type <code>Y</code>.</li>
<li><strong>What binding name would you like to use?</strong>: Type <code>DB</code> and press Enter.</li>
<li><strong>For local dev, do you want to connect to the remote resource instead of a local resource?</strong>: Type <code>N</code>.</li>
</ul>
<pre><code class="language-sh"> ⛅️ wrangler 4.44.0&#10;───────────────────&#10;✅ Successfully created DB &#x27;members-db&#x27; in region WNAM&#10;Created your new D1 database.&#10;&#10;To access your new D1 Database in your Worker, add the following snippet to your configuration file:&#10;{&#10;  &quot;d1_databases&quot;: [&#10;    {&#10;      &quot;binding&quot;: &quot;members_db&quot;,&#10;      &quot;database_name&quot;: &quot;members-db&quot;,&#10;      &quot;database_id&quot;: &quot;&lt;unique-ID-for-your-database&gt;&quot;&#10;    }&#10;  ]&#10;}&#10;✔ Would you like Wrangler to add it on your behalf? … yes&#10;✔ What binding name would you like to use? … DB&#10;✔ For local dev, do you want to connect to the remote resource instead of a local resource? … no&#10;</code></pre>
<p>The binding will be added to your Wrangler configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16074.md")
</div>
<h2 id="4-create-database-schema"><ol start="4">
<li>Create database schema</li>
</ol></h2>
<p>Create a directory called <code>schemas</code> in your project root, and inside it, create a file called <code>schema.sql</code>:</p>
<pre><code class="language-sql">DROP TABLE IF EXISTS members;&#10;CREATE TABLE IF NOT EXISTS members (&#10;  id INTEGER PRIMARY KEY AUTOINCREMENT,&#10;  name TEXT NOT NULL,&#10;  email TEXT NOT NULL UNIQUE,&#10;  joined_date TEXT NOT NULL&#10;);&#10;&#10;&#45;- Insert sample data&#10;INSERT INTO members (name, email, joined_date) VALUES&#10;  (&#x27;Alice Johnson&#x27;, &#x27;alice@example.com&#x27;, &#x27;2024-01-15&#x27;),&#10;  (&#x27;Bob Smith&#x27;, &#x27;bob@example.com&#x27;, &#x27;2024-02-20&#x27;),&#10;  (&#x27;Carol Williams&#x27;, &#x27;carol@example.com&#x27;, &#x27;2024-03-10&#x27;);&#10;</code></pre>
<p>This schema creates a <code>members</code> table with an auto-incrementing ID, name, email, and join date fields. It also inserts three sample members.</p>
<p>Execute the schema file against your D1 database:</p>
<pre><code class="language-sh">npx wrangler d1 execute members-db --file=./schemas/schema.sql&#10;</code></pre>
<p>The above command creates the table in your local development database. You will deploy the schema to production later.</p>
<h2 id="5-initialize-express-application"><ol start="5">
<li>Initialize Express application</li>
</ol></h2>
<p>Update your <code>src/index.ts</code> file to set up Express with TypeScript. Replace the file content with the following:</p>
<pre><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { httpServerHandler } from &quot;cloudflare:node&quot;;&#10;import express from &quot;express&quot;;&#10;&#10;const app = express();&#10;&#10;// Middleware to parse JSON bodies&#10;app.use(express.json());&#10;&#10;// Health check endpoint&#10;app.get(&quot;/&quot;, (req, res) =&gt; {&#10;	res.json({ message: &quot;Express.js running on Cloudflare Workers!&quot; });&#10;});&#10;&#10;app.listen(3000);&#10;export default httpServerHandler({ port: 3000 });&#10;</code></pre>
<p>This code initializes Express and creates a basic health check endpoint. The key import <code>import { env } from &quot;cloudflare:workers&quot;</code> allows you to access <a href="/workers/runtime-apis/bindings/">bindings</a> like your D1 database from anywhere in your code. The <a href="/workers/runtime-apis/nodejs/http/#httpserverhandler">httpServerHandler</a> integrates Express with the Workers runtime, enabling your application to handle HTTP requests on Cloudflare's network.</p>
<p>Next, execute the typegen command to generate type definitions for your Worker environment:</p>
<pre><code class="language-sh">npm run cf-typegen&#10;</code></pre>
<h2 id="6-implement-read-operations"><ol start="6">
<li>Implement read operations</li>
</ol></h2>
<p>Add endpoints to retrieve members from the database. Update your <code>src/index.ts</code> file by adding the following routes after the health check endpoint:</p>
<pre><code class="language-ts">// GET all members&#10;app.get(&#x27;/api/members&#x27;, async (req, res) =&gt; {&#10;	try {&#10;		const { results } = await env.DB.prepare(&#x27;SELECT * FROM members ORDER BY joined_date DESC&#x27;).all();&#10;&#10;		res.json({ success: true, members: results });&#10;	} catch (error) {&#10;		res.status(500).json({ success: false, error: &#x27;Failed to fetch members&#x27; });&#10;	}&#10;});&#10;&#10;// GET a single member by ID&#10;app.get(&#x27;/api/members/:id&#x27;, async (req, res) =&gt; {&#10;	try {&#10;		const { id } = req.params;&#10;&#10;		const { results } = await env.DB.prepare(&#x27;SELECT * FROM members WHERE id = ?&#x27;).bind(id).all();&#10;&#10;		if (results.length === 0) {&#10;			return res.status(404).json({ success: false, error: &#x27;Member not found&#x27; });&#10;		}&#10;&#10;		res.json({ success: true, member: results[0] });&#10;	} catch (error) {&#10;		res.status(500).json({ success: false, error: &#x27;Failed to fetch member&#x27; });&#10;	}&#10;});&#10;</code></pre>
<p>These routes use the D1 binding (<code>env.DB</code>) to prepare SQL statements and execute them. Since you imported <code>env</code> from <code>cloudflare:workers</code> at the top of the file, it is accessible throughout your application. The <code>prepare</code>, <code>bind</code>, and <code>all</code> methods on the D1 binding allow you to safely query the database. Refer to <a href="/d1/worker-api/">D1 Workers Binding API</a> for all available methods.</p>
<h2 id="7-implement-create-operation"><ol start="7">
<li>Implement create operation</li>
</ol></h2>
<p>Add an endpoint to create new members. Add the following route to your <code>src/index.ts</code> file:</p>
<pre><code class="language-ts">// POST - Create a new member&#10;app.post(&quot;/api/members&quot;, async (req, res) =&gt; {&#10;  try {&#10;    const { name, email } = req.body;&#10;&#10;    // Validate input&#10;    if (!name || !email) {&#10;      return res.status(400).json({&#10;        success: false,&#10;        error: &quot;Name and email are required&quot;,&#10;      });&#10;    }&#10;&#10;    // Basic email validation (simplified for tutorial purposes)&#10;    // For production, consider using a validation library or more comprehensive checks&#10;    if (!email.includes(&quot;@&quot;) || !email.includes(&quot;.&quot;)) {&#10;      return res.status(400).json({&#10;        success: false,&#10;        error: &quot;Invalid email format&quot;,&#10;      });&#10;    }&#10;&#10;    const joined_date = new Date().toISOString().split(&quot;T&quot;)[0];&#10;&#10;    const result = await env.DB.prepare(&#10;      &quot;INSERT INTO members (name, email, joined_date) VALUES (?, ?, ?)&quot;&#10;    )&#10;      .bind(name, email, joined_date)&#10;      .run();&#10;&#10;    if (result.success) {&#10;      res.status(201).json({&#10;        success: true,&#10;        message: &quot;Member created successfully&quot;,&#10;        id: result.meta.last_row_id,&#10;      });&#10;    } else {&#10;      res&#10;        .status(500)&#10;        .json({ success: false, error: &quot;Failed to create member&quot; });&#10;    }&#10;  } catch (error: any) {&#10;    // Handle unique constraint violation&#10;    if (error.message?.includes(&quot;UNIQUE constraint failed&quot;)) {&#10;      return res.status(409).json({&#10;        success: false,&#10;        error: &quot;Email already exists&quot;,&#10;      });&#10;    }&#10;    res.status(500).json({ success: false, error: &quot;Failed to create member&quot; });&#10;  }&#10;});&#10;</code></pre>
<p>This endpoint validates the input, checks the email format, and inserts a new member into the database. It also handles duplicate email addresses by checking for unique constraint violations.</p>
<h2 id="8-implement-update-operation"><ol start="8">
<li>Implement update operation</li>
</ol></h2>
<p>Add an endpoint to update existing members. Add the following route to your <code>src/index.ts</code> file:</p>
<pre><code class="language-ts">app.put(&quot;/api/members/:id&quot;, async (req, res) =&gt; {&#10;  try {&#10;    const { id } = req.params;&#10;    const { name, email } = req.body;&#10;&#10;    // Validate input&#10;    if (!name &amp;&amp; !email) {&#10;      return res.status(400).json({&#10;        success: false,&#10;        error: &quot;At least one field (name or email) is required&quot;,&#10;      });&#10;    }&#10;&#10;    // Basic email validation if provided (simplified for tutorial purposes)&#10;    // For production, consider using a validation library or more comprehensive checks&#10;    if (email &amp;&amp; (!email.includes(&quot;@&quot;) || !email.includes(&quot;.&quot;))) {&#10;      return res.status(400).json({&#10;        success: false,&#10;        error: &quot;Invalid email format&quot;,&#10;      });&#10;    }&#10;&#10;    // Build dynamic update query&#10;    const updates: string[] = [];&#10;    const values: any[] = [];&#10;&#10;    if (name) {&#10;      updates.push(&quot;name = ?&quot;);&#10;      values.push(name);&#10;    }&#10;    if (email) {&#10;      updates.push(&quot;email = ?&quot;);&#10;      values.push(email);&#10;    }&#10;&#10;    values.push(id);&#10;&#10;    const result = await env.DB.prepare(&#10;      `UPDATE members SET ${updates.join(&quot;, &quot;)} WHERE id = ?`&#10;    )&#10;      .bind(...values)&#10;      .run();&#10;&#10;    if (result.meta.changes === 0) {&#10;      return res&#10;        .status(404)&#10;        .json({ success: false, error: &quot;Member not found&quot; });&#10;    }&#10;&#10;    res.json({ success: true, message: &quot;Member updated successfully&quot; });&#10;  } catch (error: any) {&#10;    if (error.message?.includes(&quot;UNIQUE constraint failed&quot;)) {&#10;      return res.status(409).json({&#10;        success: false,&#10;        error: &quot;Email already exists&quot;,&#10;      });&#10;    }&#10;    res.status(500).json({ success: false, error: &quot;Failed to update member&quot; });&#10;  }&#10;});&#10;</code></pre>
<p>This endpoint allows updating either the name, email, or both fields of an existing member. It builds a dynamic SQL query based on the provided fields.</p>
<h2 id="9-implement-delete-operation"><ol start="9">
<li>Implement delete operation</li>
</ol></h2>
<p>Add an endpoint to delete members. Add the following route to your <code>src/index.ts</code> file:</p>
<pre><code class="language-ts">// DELETE - Delete a member&#10;app.delete(&quot;/api/members/:id&quot;, async (req, res) =&gt; {&#10;  try {&#10;    const { id } = req.params;&#10;&#10;    const result = await env.DB.prepare(&quot;DELETE FROM members WHERE id = ?&quot;)&#10;      .bind(id)&#10;      .run();&#10;&#10;    if (result.meta.changes === 0) {&#10;      return res&#10;        .status(404)&#10;        .json({ success: false, error: &quot;Member not found&quot; });&#10;    }&#10;&#10;    res.json({ success: true, message: &quot;Member deleted successfully&quot; });&#10;  } catch (error) {&#10;    res.status(500).json({ success: false, error: &quot;Failed to delete member&quot; });&#10;  }&#10;});&#10;</code></pre>
<p>This endpoint deletes a member by their ID and returns an error if the member does not exist.</p>
<h2 id="10-test-locally"><ol start="10">
<li>Test locally</li>
</ol></h2>
<p>Start the development server to test your API locally:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<p>The development server will start, and you can access your API at <code>http://localhost:8787</code>.</p>
<p>Open a new terminal window and test the endpoints using <code>curl</code>:</p>
<pre><code class="language-sh">curl http://localhost:8787/api/members&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;members&quot;: [&#10;		{&#10;			&quot;id&quot;: 1,&#10;			&quot;name&quot;: &quot;Alice Johnson&quot;,&#10;			&quot;email&quot;: &quot;alice@example.com&quot;,&#10;			&quot;joined_date&quot;: &quot;2024-01-15&quot;&#10;		},&#10;		{&#10;			&quot;id&quot;: 2,&#10;			&quot;name&quot;: &quot;Bob Smith&quot;,&#10;			&quot;email&quot;: &quot;bob@example.com&quot;,&#10;			&quot;joined_date&quot;: &quot;2024-02-20&quot;&#10;		},&#10;		{&#10;			&quot;id&quot;: 3,&#10;			&quot;name&quot;: &quot;Carol Williams&quot;,&#10;			&quot;email&quot;: &quot;carol@example.com&quot;,&#10;			&quot;joined_date&quot;: &quot;2024-03-10&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Test creating a new member:</p>
<pre><code class="language-sh">curl -X POST http://localhost:8787/api/members \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;name&quot;: &quot;David Brown&quot;, &quot;email&quot;: &quot;david@example.com&quot;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;message&quot;: &quot;Member created successfully&quot;,&#10;	&quot;id&quot;: 4&#10;}&#10;</code></pre>
<p>Test getting a single member:</p>
<pre><code class="language-sh">curl http://localhost:8787/api/members/1&#10;</code></pre>
<p>Test updating a member:</p>
<pre><code class="language-sh">curl -X PUT http://localhost:8787/api/members/1 \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;name&quot;: &quot;Alice Cooper&quot;}&#x27;&#10;</code></pre>
<p>Test deleting a member:</p>
<pre><code class="language-sh">curl -X DELETE http://localhost:8787/api/members/4&#10;</code></pre>
<h2 id="11-deploy-to-cloudflare-workers"><ol start="11">
<li>Deploy to Cloudflare Workers</li>
</ol></h2>
<p>Before deploying to production, execute the schema file against your remote (production) database:</p>
<pre><code class="language-sh">npx wrangler d1 execute members-db --remote --file=./schemas/schema.sql&#10;</code></pre>
<p>Now deploy your application to the Cloudflare network:</p>
<pre><code class="language-sh">npm run deploy&#10;</code></pre>
<pre><code class="language-sh">⛅️ wrangler 4.44.0&#10;───────────────────&#10;Total Upload: 1743.64 KiB / gzip: 498.65 KiB&#10;Worker Startup Time: 48 ms&#10;Your Worker has access to the following bindings:&#10;Binding                  Resource&#10;env.DB (members-db)      D1 Database&#10;&#10;Uploaded express-d1-app (2.99 sec)&#10;Deployed express-d1-app triggers (5.26 sec)&#10;  https://&lt;your-subdomain&gt;.workers.dev&#10;Current Version ID: &lt;version-id&gt;&#10;</code></pre>
<p>After successful deployment, Wrangler will output your Worker's URL.</p>
<h2 id="12-test-production-deployment"><ol start="12">
<li>Test production deployment</li>
</ol></h2>
<p>Test your deployed API using the provided URL. Replace <code>&lt;your-worker-url&gt;</code> with your actual Worker URL:</p>
<pre><code class="language-sh">curl https://&lt;your-worker-url&gt;/api/members&#10;</code></pre>
<p>You should see the same member data you created in the production database.</p>
<p>Create a new member in production:</p>
<pre><code class="language-sh">curl -X POST https://&lt;your-worker-url&gt;/api/members \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;name&quot;: &quot;Eva Martinez&quot;, &quot;email&quot;: &quot;eva@example.com&quot;}&#x27;&#10;</code></pre>
<p>Your Express.js application with D1 database is now running on Cloudflare Workers.</p>
<h2 id="conclusion">Conclusion</h2>
<p>In this tutorial, you built a Members Registry API using Express.js and D1 database, then deployed it to Cloudflare Workers. You implemented full CRUD operations (Create, Read, Update, Delete) and learned how to:</p>
<ul>
<li>Set up an Express.js application for Cloudflare Workers</li>
<li>Create and configure a D1 database with bindings</li>
<li>Implement database operations using D1's prepared statements</li>
<li>Test your API locally and in production</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/d1/">D1 database features</a></li>
<li>Explore <a href="/workers/runtime-apis/">Workers routing and middleware</a></li>
<li>Add authentication to your API using <a href="/workers/runtime-apis/handlers/">Workers authentication</a></li>
<li>Implement pagination for large datasets using <a href="/d1/worker-api/">D1 query optimization</a></li>
</ul>
