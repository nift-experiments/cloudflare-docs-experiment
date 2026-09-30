<p><a href="/d1/best-practices/read-replication/">D1 Read Replication</a> is a feature that allows you to replicate your D1 database to multiple regions. This is useful for your e-commerce website, as it reduces read latencies and improves read throughput. In this tutorial, you will learn how to use D1 read replication for your e-commerce website.</p>
<p>While this tutorial uses a fictional e-commerce website, the principles can be applied to any use-case that requires low read latencies and scaling reads, such as a news website, a social media platform, or a marketing website.</p>
<h2 id="quick-start">Quick start</h2>
<p>If you want to skip the steps and get started quickly, click on the below button:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/harshil1712/e-com-d1-hono"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This will create a repository in your GitHub account and deploy the application to Cloudflare Workers. It will also create and bind a D1 database, create the required tables, add some sample data. During deployment, tick the <code>Enable read replication</code> box to activate read replication.</p>
<p>You can then visit the deployed application.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7264.md")
</div></details>
<h2 id="step-1-create-a-workers-project">Step 1: Create a Workers project</h2>
<p>Create a new Workers project by running the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- fast-commerce</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- fast-commerce" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare fast-commerce</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare fast-commerce" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest fast-commerce</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest fast-commerce" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>SSR / full-stack app</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>For creating the API routes, you will use <a href="https://hono.dev/">Hono</a>. You need to install Hono by running the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add hono" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add hono</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add hono" aria-label="Copy to clipboard">Copy</button></div></div>
<h2 id="step-2-update-the-frontend">Step 2: Update the frontend</h2>
<p>The above step creates a new Workers project with a default frontend and installs Hono. You will update the frontend to list the products. You will also add a new page to the frontend to display a single product.</p>
<p>Navigate to the newly created Worker project folder.</p>
<pre><code class="language-sh">cd fast-commerce&#10;</code></pre>
<p>Update the <code>public/index.html</code> file to list the products. Use the below code as a reference.</p>
<details class="nb-details"><summary>public/index.html</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7265.md")
</div></details>
<p>Create a new <code>public/product-details.html</code> file to display a single product.</p>
<details class="nb-details"><summary>public/product-details.html</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7266.md")
</div></details>
<p>You now have a frontend that lists products and displays a single product. However, the frontend is not yet connected to the D1 database. If you start the development server now, you will see no products. In the next steps, you will create a D1 database and create APIs to fetch products and display them on the frontend.</p>
<h2 id="step-3-create-a-d1-database-and-enable-read-replication">Step 3: Create a D1 database and enable read replication</h2>
<p>Create a new D1 database by running the following command:</p>
<pre><code class="language-sh">npx wrangler d1 create fast-commerce&#10;</code></pre>
<p>Add the D1 bindings returned in the terminal to the <code>wrangler</code> file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7267.md")
</div>
<p>Run the following command to update the <code>Env</code> interface in the <code>worker-configuration.d.ts</code> file.</p>
<pre><code class="language-sh">npm run cf-typegen&#10;</code></pre>
<p>Next, enable read replication for the D1 database. Navigate to <a href="https://dash.cloudflare.com/?to=/:account/workers/d1"><strong>Workers &amp; Pages</strong> &gt; <strong>D1</strong></a>, then select an existing database &gt; <strong>Settings</strong> &gt; <strong>Enable Read Replication</strong>.</p>
<h2 id="step-4-create-the-api-routes">Step 4: Create the API routes</h2>
<p>Update the <code>src/index.ts</code> file to import the Hono library and create the API routes.</p>
<pre><code class="language-ts">import { Hono } from &quot;hono&quot;;&#10;// Set db session bookmark in the cookie&#10;import { getCookie, setCookie } from &quot;hono/cookie&quot;;&#10;&#10;const app = new Hono&lt;{ Bindings: Env }&gt;();&#10;&#10;// Get all products&#10;app.get(&quot;/api/products&quot;, async (c) =&gt; {&#10;	return c.json({ message: &quot;get list of products&quot; });&#10;});&#10;&#10;// Get a single product&#10;app.get(&quot;/api/products/:id&quot;, async (c) =&gt; {&#10;	return c.json({ message: &quot;get a single product&quot; });&#10;});&#10;&#10;// Upsert a product&#10;app.post(&quot;/api/product&quot;, async (c) =&gt; {&#10;	return c.json({ message: &quot;create or update a product&quot; });&#10;});&#10;&#10;export default app;&#10;</code></pre>
<p>The above code creates three API routes:</p>
<ul>
<li><code>GET /api/products</code>: Returns a list of products.</li>
<li><code>GET /api/products/:id</code>: Returns a single product.</li>
<li><code>POST /api/product</code>: Creates or updates a product.</li>
</ul>
<p>However, the API routes are not connected to the D1 database yet. In the next steps, you will create a products table in the D1 database, and update the API routes to connect to the D1 database.</p>
<h2 id="step-5-create-local-d1-database-schema">Step 5: Create local D1 database schema</h2>
<p>Create a products table in the D1 database by running the following command:</p>
<pre><code class="language-sh">npx wrangler d1 execute fast-commerce --command &quot;CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT, price DECIMAL(10, 2) NOT NULL, inventory INTEGER NOT NULL DEFAULT 0, category TEXT NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)&quot;&#10;</code></pre>
<p>Next, create an index on the products table by running the following command:</p>
<pre><code class="language-sh">npx wrangler d1 execute fast-commerce --command &quot;CREATE INDEX IF NOT EXISTS idx_products_id ON products (id)&quot;&#10;</code></pre>
<p>For development purposes, you can also execute the insert statements on the local D1 database by running the following command:</p>
<pre><code class="language-sh">npx wrangler d1 execute fast-commerce --command &quot;INSERT INTO products (id, name, description, price, inventory, category) VALUES (1, &#x27;Fast Ergonomic Chair&#x27;, &#x27;A comfortable chair for your home or office&#x27;, 100.00, 10, &#x27;Furniture&#x27;), (2, &#x27;Fast Organic Cotton T-shirt&#x27;, &#x27;A comfortable t-shirt for your home or office&#x27;, 20.00, 100, &#x27;Clothing&#x27;), (3, &#x27;Fast Wooden Desk&#x27;, &#x27;A wooden desk for your home or office&#x27;, 150.00, 5, &#x27;Furniture&#x27;), (4, &#x27;Fast Leather Sofa&#x27;, &#x27;A leather sofa for your home or office&#x27;, 300.00, 3, &#x27;Furniture&#x27;), (5, &#x27;Fast Organic Cotton T-shirt&#x27;, &#x27;A comfortable t-shirt for your home or office&#x27;, 20.00, 100, &#x27;Clothing&#x27;)&quot;&#10;</code></pre>
<h2 id="step-6-add-retry-logic">Step 6: Add retry logic</h2>
<p>To make the application more resilient, you can add retry logic to the API routes. Create a new file called <code>retry.ts</code> in the <code>src</code> directory.</p>
<pre><code class="language-ts">export interface RetryConfig {&#10;	maxRetries: number;&#10;	initialDelay: number;&#10;	maxDelay: number;&#10;	backoffFactor: number;&#10;}&#10;&#10;const shouldRetry = (error: unknown): boolean =&gt; {&#10;	const errMsg = error instanceof Error ? error.message : String(error);&#10;	return (&#10;		errMsg.includes(&quot;Network connection lost&quot;) ||&#10;		errMsg.includes(&quot;storage caused object to be reset&quot;) ||&#10;		errMsg.includes(&quot;reset because its code was updated&quot;)&#10;	);&#10;};&#10;&#10;// Helper function for sleeping&#10;const sleep = (ms: number): Promise&lt;void&gt; =&gt; {&#10;	return new Promise((resolve) =&gt; setTimeout(resolve, ms));&#10;};&#10;&#10;export const defaultRetryConfig: RetryConfig = {&#10;	maxRetries: 3,&#10;	initialDelay: 100,&#10;	maxDelay: 1000,&#10;	backoffFactor: 2,&#10;};&#10;&#10;export async function withRetry&lt;T&gt;(&#10;	operation: () =&gt; Promise&lt;T&gt;,&#10;	config: Partial&lt;RetryConfig&gt; = defaultRetryConfig,&#10;): Promise&lt;T&gt; {&#10;	const maxRetries = config.maxRetries ?? defaultRetryConfig.maxRetries;&#10;	const initialDelay = config.initialDelay ?? defaultRetryConfig.initialDelay;&#10;	const maxDelay = config.maxDelay ?? defaultRetryConfig.maxDelay;&#10;	const backoffFactor =&#10;		config.backoffFactor ?? defaultRetryConfig.backoffFactor;&#10;&#10;	let lastError: Error | unknown;&#10;	let delay = initialDelay;&#10;&#10;	for (let attempt = 0; attempt &lt;= maxRetries; attempt++) {&#10;		try {&#10;			const result = await operation();&#10;			return result;&#10;		} catch (error) {&#10;			lastError = error;&#10;&#10;			if (!shouldRetry(error) || attempt === maxRetries) {&#10;				throw error;&#10;			}&#10;&#10;			// Add randomness to avoid synchronizing retries&#10;			// Wait for a random delay between delay and delay*2&#10;			await sleep(delay * (1 + Math.random()));&#10;&#10;			// Calculate next delay with exponential backoff&#10;			delay = Math.min(delay * backoffFactor, maxDelay);&#10;		}&#10;	}&#10;&#10;	throw lastError;&#10;}&#10;</code></pre>
<p>The <code>withRetry</code> function is a utility function that retries a given operation with exponential backoff. It takes a configuration object as an argument, which allows you to customize the number of retries, initial delay, maximum delay, and backoff factor. It will only retry the operation if the error is due to a network connection loss, storage reset, or code update.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7263.md")
</aside>
<p>Next, update the <code>src/index.ts</code> file to import the <code>withRetry</code> function and use it in the API routes.</p>
<pre><code class="language-ts">import { withRetry } from &quot;./retry&quot;;&#10;</code></pre>
<h2 id="step-7-update-the-api-routes">Step 7: Update the API routes</h2>
<p>Update the API routes to connect to the D1 database.</p>
<h3 id="1-post-api-product"><ol>
<li>POST /api/product</li>
</ol></h3>
<pre><code class="language-ts">app.post(&quot;/api/product&quot;, async (c) =&gt; {&#10;	const product = await c.req.json();&#10;&#10;	if (!product) {&#10;		return c.json({ message: &quot;No data passed&quot; }, 400);&#10;	}&#10;&#10;	const db = c.env.DB;&#10;	const session = db.withSession(&quot;first-primary&quot;);&#10;&#10;	const { id } = product;&#10;&#10;	try {&#10;		return await withRetry(async () =&gt; {&#10;			// Check if the product exists&#10;			const { results } = await session&#10;				.prepare(&quot;SELECT * FROM products where id = ?&quot;)&#10;				.bind(id)&#10;				.run();&#10;			if (results.length === 0) {&#10;				const fields = [...Object.keys(product)];&#10;				const values = [...Object.values(product)];&#10;				// Insert the product&#10;				await session&#10;					.prepare(&#10;						`INSERT INTO products (${fields.join(&quot;, &quot;)}) VALUES (${fields.map(() =&gt; &quot;?&quot;).join(&quot;, &quot;)})`,&#10;					)&#10;					.bind(...values)&#10;					.run();&#10;				const latestBookmark = session.getBookmark();&#10;				latestBookmark &amp;&amp;&#10;					setCookie(c, &quot;product_bookmark&quot;, latestBookmark, {&#10;						maxAge: 60 * 60, // 1 hour&#10;					});&#10;				return c.json({ message: &quot;Product inserted&quot; });&#10;			}&#10;&#10;			// Update the product&#10;			const updates = Object.entries(product)&#10;				.filter(([_, value]) =&gt; value !== undefined)&#10;				.map(([key, _]) =&gt; `${key} = ?`)&#10;				.join(&quot;, &quot;);&#10;&#10;			if (!updates) {&#10;				throw new Error(&quot;No valid fields to update&quot;);&#10;			}&#10;&#10;			const values = Object.entries(product)&#10;				.filter(([_, value]) =&gt; value !== undefined)&#10;				.map(([_, value]) =&gt; value);&#10;&#10;			await session&#10;				.prepare(`UPDATE products SET ${updates} WHERE id = ?`)&#10;				.bind(...[...values, id])&#10;				.run();&#10;			const latestBookmark = session.getBookmark();&#10;			latestBookmark &amp;&amp;&#10;				setCookie(c, &quot;product_bookmark&quot;, latestBookmark, {&#10;					maxAge: 60 * 60, // 1 hour&#10;				});&#10;			return c.json({ message: &quot;Product updated&quot; });&#10;		});&#10;	} catch (e) {&#10;		console.error(e);&#10;		return c.json({ message: &quot;Error upserting product&quot; }, 500);&#10;	}&#10;});&#10;</code></pre>
<p>In the above code:</p>
<ul>
<li>You get the product data from the request body.</li>
<li>You then check if the product exists in the database.
<ul>
<li>If it does, you update the product.</li>
<li>If it doesn't, you insert the product.</li>
</ul>
</li>
<li>You then set the bookmark in the cookie.</li>
<li>Finally, you return the response.</li>
</ul>
<p>Since you want to start the session with the latest data, you use the <code>first-primary</code> constraint. Even if you use the <code>first-unconstrained</code> constraint or pass a bookmark, the write request will always be routed to the primary database.</p>
<p>The bookmark set in the cookie can be used to guarantee that a new session reads a database version that is at least as up-to-date as the provided bookmark.</p>
<p>If you are using an external platform to manage your products, you can connect this API to the external platform, such that, when a product is created or updated in the external platform, the D1 database automatically updates the product details.</p>
<h3 id="2-get-api-products"><ol start="2">
<li>GET /api/products</li>
</ol></h3>
<pre><code class="language-ts">app.get(&quot;/api/products&quot;, async (c) =&gt; {&#10;	const db = c.env.DB;&#10;&#10;	// Get bookmark from the cookie&#10;	const bookmark = getCookie(c, &quot;product_bookmark&quot;) || &quot;first-unconstrained&quot;;&#10;&#10;	const session = db.withSession(bookmark);&#10;&#10;	try {&#10;		return await withRetry(async () =&gt; {&#10;			const { results } = await session.prepare(&quot;SELECT * FROM products&quot;).run();&#10;&#10;			const latestBookmark = session.getBookmark();&#10;&#10;			// Set the bookmark in the cookie&#10;			latestBookmark &amp;&amp;&#10;				setCookie(c, &quot;product_bookmark&quot;, latestBookmark, {&#10;					maxAge: 60 * 60, // 1 hour&#10;				});&#10;&#10;			return c.json(results);&#10;		});&#10;	} catch (e) {&#10;		console.error(e);&#10;		return c.json([]);&#10;	}&#10;});&#10;</code></pre>
<p>In the above code:</p>
<ul>
<li>You get the database session bookmark from the cookie.
<ul>
<li>If the bookmark is not set, you use the <code>first-unconstrained</code> constraint.</li>
</ul>
</li>
<li>You then create a database session with the bookmark.</li>
<li>You fetch all the products from the database and get the latest bookmark.</li>
<li>You then set this bookmark in the cookie.</li>
<li>Finally, you return the results.</li>
</ul>
<h3 id="3-get-api-products-id"><ol start="3">
<li>GET /api/products/:id</li>
</ol></h3>
<pre><code class="language-ts">app.get(&quot;/api/products/:id&quot;, async (c) =&gt; {&#10;	const id = c.req.param(&quot;id&quot;);&#10;&#10;	if (!id) {&#10;		return c.json({ message: &quot;Invalid id&quot; }, 400);&#10;	}&#10;&#10;	const db = c.env.DB;&#10;&#10;	// Get bookmark from the cookie&#10;	const bookmark = getCookie(c, &quot;product_bookmark&quot;) || &quot;first-unconstrained&quot;;&#10;&#10;	const session = db.withSession(bookmark);&#10;&#10;	try {&#10;		return await withRetry(async () =&gt; {&#10;			const { results } = await session&#10;				.prepare(&quot;SELECT * FROM products where id = ?&quot;)&#10;				.bind(id)&#10;				.run();&#10;&#10;			const latestBookmark = session.getBookmark();&#10;&#10;			// Set the bookmark in the cookie&#10;			latestBookmark &amp;&amp;&#10;				setCookie(c, &quot;product_bookmark&quot;, latestBookmark, {&#10;					maxAge: 60 * 60, // 1 hour&#10;				});&#10;&#10;			console.log(results);&#10;&#10;			return c.json(results);&#10;		});&#10;	} catch (e) {&#10;		console.error(e);&#10;		return c.json([]);&#10;	}&#10;});&#10;</code></pre>
<p>In the above code:</p>
<ul>
<li>You get the product ID from the request parameters.</li>
<li>You then create a database session with the bookmark.</li>
<li>You fetch the product from the database and get the latest bookmark.</li>
<li>You then set this bookmark in the cookie.</li>
<li>Finally, you return the results.</li>
</ul>
<h2 id="step-8-test-the-application">Step 8: Test the application</h2>
<p>You have now updated the API routes to connect to the D1 database. You can now test the application by starting the development server and navigating to the frontend.</p>
<pre><code class="language-sh">npm run dev&#10;</code></pre>
<p>Navigate to `<a href="http://localhost:8787">http://localhost:8787</a>. You should see the products listed. Click on a product to view the product details.</p>
<p>To insert a new product, use the following command (while the development server is running):</p>
<pre><code class="language-sh">curl -X POST http://localhost:8787/api/product \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;d &#x27;{&quot;id&quot;: 6, &quot;name&quot;: &quot;Fast Computer&quot;, &quot;description&quot;: &quot;A computer for your home or office&quot;, &quot;price&quot;: 1000.00, &quot;inventory&quot;: 10, &quot;category&quot;: &quot;Electronics&quot;}&#x27;&#10;</code></pre>
<p>Navigate to <code>http://localhost:8787/product-details?id=6</code>. You should see the new product.</p>
<p>Update the product using the following command, and navigate to <code>http://localhost:8787/product-details?id=6</code> again. You will see the updated product.</p>
<pre><code class="language-sh">curl -X POST http://localhost:8787/api/product \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;d &#x27;{&quot;id&quot;: 6, &quot;name&quot;: &quot;Fast Computer&quot;, &quot;description&quot;: &quot;A computer for your home or office&quot;, &quot;price&quot;: 1050.00, &quot;inventory&quot;: 10, &quot;category&quot;: &quot;Electronics&quot;}&#x27;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7262.md")
</aside>
<h2 id="step-9-deploy-the-application">Step 9: Deploy the application</h2>
<p>Since the database you used in the previous steps is local, you need to create the products table in the remote database. Execute the following D1 commands to create the products table in the remote database.</p>
<pre><code class="language-sh">npx wrangler d1 execute fast-commerce --remote --command &quot;CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT, price DECIMAL(10, 2) NOT NULL, inventory INTEGER NOT NULL DEFAULT 0, category TEXT NOT NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)&quot;&#10;</code></pre>
<p>Next, create an index on the products table by running the following command:</p>
<pre><code class="language-sh">npx wrangler d1 execute fast-commerce --remote --command &quot;CREATE INDEX IF NOT EXISTS idx_products_id ON products (id)&quot;&#10;</code></pre>
<p>Optionally, you can insert the products into the remote database by running the following command:</p>
<pre><code class="language-sh">npx wrangler d1 execute fast-commerce --remote --command &quot;INSERT INTO products (id, name, description, price, inventory, category) VALUES (1, &#x27;Fast Ergonomic Chair&#x27;, &#x27;A comfortable chair for your home or office&#x27;, 100.00, 10, &#x27;Furniture&#x27;), (2, &#x27;Fast Organic Cotton T-shirt&#x27;, &#x27;A comfortable t-shirt for your home or office&#x27;, 20.00, 100, &#x27;Clothing&#x27;), (3, &#x27;Fast Wooden Desk&#x27;, &#x27;A wooden desk for your home or office&#x27;, 150.00, 5, &#x27;Furniture&#x27;), (4, &#x27;Fast Leather Sofa&#x27;, &#x27;A leather sofa for your home or office&#x27;, 300.00, 3, &#x27;Furniture&#x27;), (5, &#x27;Fast Organic Cotton T-shirt&#x27;, &#x27;A comfortable t-shirt for your home or office&#x27;, 20.00, 100, &#x27;Clothing&#x27;)&quot;&#10;</code></pre>
<p>Now, you can deploy the application with the following command:</p>
<pre><code class="language-sh">npm run deploy&#10;</code></pre>
<p>This will deploy the application to Workers and the D1 database will be replicated to the remote regions. If a user requests the application from any region, the request will be redirected to the nearest region where the database is replicated.</p>
<h2 id="conclusion">Conclusion</h2>
<p>In this tutorial, you learned how to use D1 Read Replication for your e-commerce website. You created a D1 database and enabled read replication for it. You then created an API to create and update products in the database. You also learned how to use the bookmark to get the latest data from the database.</p>
<p>You then created the products table in the remote database and deployed the application.</p>
<p>You can use the same approach for your existing read heavy application to reduce read latencies and improve read throughput. If you are using an external platform to manage the content, you can connect the external platform to the D1 database, so that the content is automatically updated in the database.</p>
<p>You can find the complete code for this tutorial in the <a href="https://github.com/harshil1712/e-com-d1-hono">GitHub repository</a>.</p>
