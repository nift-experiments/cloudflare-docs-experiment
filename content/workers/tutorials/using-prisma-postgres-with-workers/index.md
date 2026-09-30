<p><a href="https://www.prisma.io/postgres">Prisma Postgres</a> is a managed, serverless PostgreSQL database. It supports features like connection pooling, caching, real-time subscriptions, and query optimization recommendations.</p>
<p>In this tutorial, you will learn how to:</p>
<ul>
<li>Set up a Cloudflare Workers project with <a href="https://www.prisma.io/docs">Prisma ORM</a>.</li>
<li>Create a Prisma Postgres instance from the Prisma CLI.</li>
<li>Model data and run migrations with Prisma Postgres.</li>
<li>Query the database from Workers.</li>
<li>Deploy the Worker to Cloudflare.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>To follow this guide, ensure you have the following:</p>
<ul>
<li>Node.js <code>v18.18</code> or higher installed.</li>
<li>An active <a href="https://dash.cloudflare.com/">Cloudflare account</a>.</li>
<li>A basic familiarity with installing and using command-line interface (CLI) applications.</li>
</ul>
<h2 id="1-create-a-new-worker-project"><ol>
<li>Create a new Worker project</li>
</ol></h2>
<p>Begin by using <a href="/pages/get-started/c3/">C3</a> to create a Worker project in the command line:</p>
<pre><code class="language-sh">npm create cloudflare@latest prisma-postgres-worker -- --type=hello-world --ts=true --git=true --deploy=false&#10;</code></pre>
<p>Then navigate into your project:</p>
<pre><code class="language-sh">cd ./prisma-postgres-worker&#10;</code></pre>
<p>Your initial <code>src/index.ts</code> file currently contains a simple request handler:</p>
<pre><code class="language-ts">export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		return new Response(&quot;Hello World!&quot;);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="2-setup-prisma-in-your-project"><ol start="2">
<li>Setup Prisma in your project</li>
</ol></h2>
<p>In this step, you will set up Prisma ORM with a Prisma Postgres database using the CLI. Then you will create and execute helper scripts to create tables in the database and generate a Prisma client to query it.</p>
<h3 id="2-1-install-required-dependencies">2.1. Install required dependencies</h3>
<p>Install Prisma CLI as a dev dependency:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add prisma" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add prisma</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add prisma" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Install the <a href="https://www.npmjs.com/package/@prisma/extension-accelerate">Prisma Accelerate client extension</a> as it is required for Prisma Postgres:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @prisma/extension-accelerate</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @prisma/extension-accelerate" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @prisma/extension-accelerate</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @prisma/extension-accelerate" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @prisma/extension-accelerate</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @prisma/extension-accelerate" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @prisma/extension-accelerate</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @prisma/extension-accelerate" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Install the <a href="https://www.npmjs.com/package/dotenv-cli"><code>dotenv-cli</code> package</a> to load environment variables from <code>.dev.vars</code>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i dotenv-cli</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i dotenv-cli" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add dotenv-cli</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add dotenv-cli" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add dotenv-cli</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add dotenv-cli" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add dotenv-cli</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add dotenv-cli" aria-label="Copy to clipboard">Copy</button></div></div>
<h3 id="2-2-create-a-prisma-postgres-database-and-initialize-prisma">2.2. Create a Prisma Postgres database and initialize Prisma</h3>
<p>Initialize Prisma in your application:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx prisma@latest init --db</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx prisma@latest init --db" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn dlx prisma@latest init --db</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn dlx prisma@latest init --db" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpx prisma@latest init --db</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpx prisma@latest init --db" aria-label="Copy to clipboard">Copy</button></div></div>
<p>If you do not have a <a href="https://console.prisma.io/">Prisma Data Platform</a> account yet, or if you are not logged in, the command will prompt you to log in using one of the available authentication providers. A browser window will open so you can log in or create an account. Return to the CLI after you have completed this step.</p>
<p>Once logged in (or if you were already logged in), the CLI will prompt you to select a project name and a database region.</p>
<p>Once the command has terminated, it will have created:</p>
<ul>
<li>A project in your <a href="https://console.prisma.io/">Platform Console</a> containing a Prisma Postgres database instance.</li>
<li>A <code>prisma</code> folder containing <code>schema.prisma</code>, where you will define your database schema.</li>
<li>An <code>.env</code> file in the project root, which will contain the Prisma Postgres database url <code>DATABASE_URL=&lt;your-prisma-postgres-database-url&gt;</code>.</li>
</ul>
<p>Note that Cloudflare Workers do not support <code>.env</code> files. You will use a file called <code>.dev.vars</code> instead of the <code>.env</code> file that was just created.</p>
<h3 id="2-3-prepare-environment-variables">2.3. Prepare environment variables</h3>
<p>Rename the <code>.env</code> file in the root of your application to <code>.dev.vars</code> file:</p>
<pre><code class="language-sh">mv .env .dev.vars&#10;</code></pre>
<h3 id="2-4-apply-database-schema-changes">2.4. Apply database schema changes</h3>
<p>Open the <code>schema.prisma</code> file in the <code>prisma</code> folder and add the following <code>User</code> model to your database:</p>
<pre><code class="language-prisma">generator client {&#10;  provider = &quot;prisma-client-js&quot;&#10;}&#10;&#10;datasource db {&#10;  provider = &quot;postgresql&quot;&#10;  url      = env(&quot;DATABASE_URL&quot;)&#10;}&#10;&#10;model User {&#10;  id  Int @id @default(autoincrement())&#10;  email String&#10;	name 	String&#10;}&#10;</code></pre>
<p>Next, add the following helper scripts to the <code>scripts</code> section of your <code>package.json</code>:</p>
<pre><code class="language-json">&quot;scripts&quot;: {&#10;  &quot;migrate&quot;: &quot;dotenv -e .dev.vars -- npx prisma migrate dev&quot;,&#10;	&quot;generate&quot;: &quot;dotenv -e .dev.vars -- npx prisma generate --no-engine&quot;,&#10;	&quot;studio&quot;: &quot;dotenv -e .dev.vars -- npx prisma studio&quot;,&#10;  // Additional worker scripts...&#10;}&#10;</code></pre>
<p>Run the migration script to apply changes to the database:</p>
<pre><code class="language-sh">npm run migrate&#10;</code></pre>
<p>When prompted, provide a name for the migration (for example, <code>init</code>).</p>
<p>After these steps are complete, Prisma ORM is fully set up and connected to your Prisma Postgres database.</p>
<h2 id="3-develop-the-application"><ol start="3">
<li>Develop the application</li>
</ol></h2>
<p>Modify the <code>src/index.ts</code> file and replace its contents with the following code:</p>
<pre><code class="language-ts">import { PrismaClient } from &quot;@prisma/client/edge&quot;;&#10;import { withAccelerate } from &quot;@prisma/extension-accelerate&quot;;&#10;&#10;export interface Env {&#10;	DATABASE_URL: string;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		const path = new URL(request.url).pathname;&#10;		if (path === &quot;/favicon.ico&quot;)&#10;			return new Response(&quot;Resource not found&quot;, {&#10;				status: 404,&#10;				headers: {&#10;					&quot;Content-Type&quot;: &quot;text/plain&quot;,&#10;				},&#10;			});&#10;&#10;		const prisma = new PrismaClient({&#10;			datasourceUrl: env.DATABASE_URL,&#10;		}).$extends(withAccelerate());&#10;&#10;		const user = await prisma.user.create({&#10;			data: {&#10;				email: `Jon${Math.ceil(Math.random() * 1000)}@gmail.com`,&#10;				name: &quot;Jon Doe&quot;,&#10;			},&#10;		});&#10;&#10;		const userCount = await prisma.user.count();&#10;&#10;		return new Response(`\&#10;Created new user: ${user.name} (${user.email}).&#10;Number of users in the database: ${userCount}.&#10;		`);&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Run the development server:</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<p>Visit <a href="https://localhost:8787"><code>https://localhost:8787</code></a> to see your app display the following output:</p>
<pre><code class="language-sh">Number of users in the database: 1&#10;</code></pre>
<p>Every time you refresh the page, a new user is created. The number displayed will increment by <code>1</code> with each refresh as it returns the total number of users in your database.</p>
<h2 id="4-deploy-the-application-to-cloudflare"><ol start="4">
<li>Deploy the application to Cloudflare</li>
</ol></h2>
<p>When the application is deployed to Cloudflare, it needs access to the <code>DATABASE_URL</code> environment variable that is defined locally in <code>.dev.vars</code>. You can use the <a href="/workers/configuration/secrets/#adding-secrets-to-your-project"><code>npx wrangler secret put</code></a> command to upload the <code>DATABASE_URL</code> to the deployment environment:</p>
<pre><code class="language-sh">npx wrangler secret put DATABASE_URL&#10;</code></pre>
<p>When prompted, paste the <code>DATABASE_URL</code> value (from <code>.dev.vars</code>). If you are logged in via the Wrangler CLI, you will see a prompt asking if you'd like to create a new Worker. Confirm by choosing &quot;yes&quot;:</p>
<pre><code class="language-sh">✔ There doesn&#x27;t seem to be a Worker called &quot;prisma-postgres-worker&quot;. Do you want to create a new Worker with that name and add secrets to it? … yes&#10;</code></pre>
<p>Then execute the following command to deploy your project to Cloudflare Workers:</p>
<pre><code class="language-sh">npm run deploy&#10;</code></pre>
<p>The <code>wrangler</code> CLI will bundle and upload your application.</p>
<p>If you are not already logged in, the <code>wrangler</code> CLI will open a browser window prompting you to log in to the Cloudflare dashboard.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16049.md")
</aside>
<p>Once the deployment completes, verify the deployment by visiting the live URL provided in the deployment output, such as <code>https://{PROJECT_NAME}.workers.dev</code>. If you encounter any issues, ensure the secrets were added correctly and check the deployment logs for errors.</p>
<h2 id="next-steps">Next steps</h2>
<p>Congratulations on building and deploying a simple application with Prisma Postgres and Cloudflare Workers!</p>
<p>To enhance your application further:</p>
<ul>
<li>Add <a href="https://www.prisma.io/docs/postgres/caching">caching</a> to your queries.</li>
<li>Explore the <a href="https://www.prisma.io/docs/postgres/getting-started">Prisma Postgres documentation</a>.</li>
</ul>
<p>To see how to build a real-time application with Cloudflare Workers and Prisma Postgres, read <a href="https://www.prisma.io/docs/guides/prisma-postgres-realtime-on-cloudflare">this</a> guide.</p>
