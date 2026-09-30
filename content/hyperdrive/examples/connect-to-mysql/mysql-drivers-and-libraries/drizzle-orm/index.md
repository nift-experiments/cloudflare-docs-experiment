<p><a href="https://orm.drizzle.team/">Drizzle ORM</a> is a lightweight TypeScript ORM with a focus on type safety. This example demonstrates how to use Drizzle ORM with MySQL via Cloudflare Hyperdrive in a Workers application.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A Cloudflare account with Workers access</li>
<li>A MySQL database</li>
<li>A <a href="/hyperdrive/get-started/#3-connect-hyperdrive-to-a-database">Hyperdrive configuration to your MySQL database</a></li>
</ul>
<h2 id="1-install-drizzle"><ol>
<li>Install Drizzle</li>
</ol></h2>
<p>Install the Drizzle ORM and its dependencies such as the <a href="https://github.com/sidorares/node-mysql2">mysql2</a> driver:</p>
<pre><code class="language-sh">&#35; mysql2 v3.13.0 or later is required&#10;npm i drizzle-orm mysql2 dotenv&#10;npm i -D drizzle-kit tsx @types/node&#10;</code></pre>
<p>Add the required Node.js compatibility flags and Hyperdrive binding to your <code>wrangler.jsonc</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9134.md")
</div>
<h2 id="2-configure-drizzle"><ol start="2">
<li>Configure Drizzle</li>
</ol></h2>
<h3 id="2-1-define-a-schema">2.1. Define a schema</h3>
<p>With Drizzle ORM, we define the schema in TypeScript rather than writing raw SQL.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9135.md")
</div>
<h3 id="2-2-connect-drizzle-orm-to-the-database-with-hyperdrive">2.2. Connect Drizzle ORM to the database with Hyperdrive</h3>
<p>Use your the credentials of your Hyperdrive configuration for your database when using the Drizzle ORM.</p>
<p>Populate your <code>index.ts</code> file as shown below.</p>
<pre><code class="language-ts">// src/index.ts&#10;&#10;import { drizzle } from &quot;drizzle-orm/mysql2&quot;;&#10;import { createConnection } from &quot;mysql2/promise&quot;;&#10;import { users } from &quot;./db/schema&quot;;&#10;&#10;export interface Env {&#10;	HYPERDRIVE: Hyperdrive;&#10;  }&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a connection using the mysql2 driver with the Hyperdrive credentials (only accessible from your Worker).&#10;		const connection = await createConnection({&#10;			host: env.HYPERDRIVE.host,&#10;			user: env.HYPERDRIVE.user,&#10;			password: env.HYPERDRIVE.password,&#10;			database: env.HYPERDRIVE.database,&#10;			port: env.HYPERDRIVE.port,&#10;&#10;			// Required to enable mysql2 compatibility for Workers&#10;			disableEval: true,&#10;		});&#10;&#10;		// Create the Drizzle client with the mysql2 driver connection&#10;		const db = drizzle(connection);&#10;&#10;		// Sample query to get all users&#10;		const allUsers = await db.select().from(users);&#10;&#10;		return Response.json(allUsers);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h3 id="2-3-configure-drizzle-kit-for-migrations-optional">2.3. Configure Drizzle-Kit for migrations (optional)</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9133.md")
</aside>
<p>You can generate and run SQL migrations on your database based on your schema using Drizzle Kit CLI. Refer to <a href="https://orm.drizzle.team/docs/get-started/mysql-new">Drizzle ORM docs</a> for additional guidance.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/9136.md")
</div>
<h2 id="3-deploy-your-worker"><ol start="3">
<li>Deploy your Worker</li>
</ol></h2>
<p>Deploy your Worker.</p>
<pre><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
<li>Understand more about other <a href="/workers/platform/storage-options/">storage options</a> available to Cloudflare Workers.</li>
</ul>
