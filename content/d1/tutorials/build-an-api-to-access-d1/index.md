<p>In this tutorial, you will learn how to create an API that allows you to securely run queries against a D1 database.</p>
<p>This is useful if you want to access a D1 database outside of a Worker or Pages project, customize access controls and/or limit what tables can be queried.</p>
<p>D1's built-in <a href="/api/resources/d1/subresources/database/methods/create/">REST API</a> is best suited for administrative use as the global <a href="/fundamentals/api/reference/limits">Cloudflare API rate limit</a> applies.</p>
<p>To access a D1 database outside of a Worker project, you need to create an API using a Worker. Your application can then securely interact with this API to run D1 queries.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7291.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
<li>Have an existing D1 database. Refer to <a href="/d1/get-started/">Get started tutorial for D1</a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7292.md")
</div></details>
<h2 id="1-create-a-new-project"><ol>
<li>Create a new project</li>
</ol></h2>
<p>Create a new Worker to create and deploy your API.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7293.md")
</div>
<h2 id="2-install-hono"><ol start="2">
<li>Install Hono</li>
</ol></h2>
<p>In this tutorial, you will use <a href="https://github.com/honojs/hono">Hono</a>, an Express.js-style framework, to build the API.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7294.md")
</div>
<h2 id="3-add-an-api-key"><ol start="3">
<li>Add an API_KEY</li>
</ol></h2>
<p>You need an API key to make authenticated calls to the API. To ensure that the API key is secure, add it as a <a href="/workers/configuration/secrets">secret</a>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7295.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7290.md")
</aside>
<h2 id="4-initialize-the-application"><ol start="4">
<li>Initialize the application</li>
</ol></h2>
<p>To initialize the application, you need to import the required packages, initialize a new Hono application, and configure the following middleware:</p>
<ul>
<li><a href="https://hono.dev/docs/middleware/builtin/bearer-auth">Bearer Auth</a>: Adds authentication to the API.</li>
<li><a href="https://hono.dev/docs/middleware/builtin/logger">Logger</a>: Allows monitoring the flow of requests and responses.</li>
<li><a href="https://hono.dev/docs/middleware/builtin/pretty-json">Pretty JSON</a>: Enables &quot;JSON pretty print&quot; for JSON response bodies.</li>
</ul>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7296.md")
</div>
<h2 id="5-add-api-endpoints"><ol start="5">
<li>Add API endpoints</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7297.md")
</div>
<p>The Hono application is now set up. You can test the other endpoints and add more endpoints if needed. The API does not yet return any information from your database. In the next steps, you will create a database, add its bindings, and update the endpoints to interact with the database.</p>
<h2 id="6-create-a-database"><ol start="6">
<li>Create a database</li>
</ol></h2>
<p>If you do not have a D1 database already, you can create a new database with <code>wrangler d1 create</code>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7298.md")
</div>
<p>Make a note of the displayed <code>database_name</code> and <code>database_id</code>. You will use this to reference the database by creating a <a href="/workers/runtime-apis/bindings/">binding</a>.</p>
<h2 id="7-add-a-binding"><ol start="7">
<li>Add a binding</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7300.md")
</div>
<p>You can now access the database in the Hono application.</p>
<h2 id="8-create-a-table"><ol start="8">
<li>Create a table</li>
</ol></h2>
<p>To create a table in your newly created database:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7301.md")
</div>
<p>Upon successful execution, a new table will be added to your database.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7289.md")
</aside>
<h2 id="9-query-the-database"><ol start="9">
<li>Query the database</li>
</ol></h2>
<p>Your application can now access the D1 database. In this step, you will update the API endpoints to query the database and return the result.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7302.md")
</div>
<p>In the above code, the endpoints are updated to receive <code>query</code> and <code>params</code>. These queries and parameters are passed to the respective functions to interact with the database.</p>
<ul>
<li>If the query is successful, you receive the result from the database.</li>
<li>If there is an error, the error message is returned.</li>
</ul>
<h2 id="10-test-the-api"><ol start="10">
<li>Test the API</li>
</ol></h2>
<p>Now that the API can query the database, you can test it locally.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7303.md")
</div>
<p>If everything is implemented correctly, the above commands should result successful outputs.</p>
<h2 id="11-deploy-the-api"><ol start="11">
<li>Deploy the API</li>
</ol></h2>
<p>Now that everything is working as expected, the last step is to deploy it to the Cloudflare network. You will use Wrangler to deploy the API.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7304.md")
</div>
<h2 id="summary">Summary</h2>
<p>In this tutorial, you have:</p>
<ol>
<li>Created an API that interacts with your D1 database.</li>
<li>Deployed this API to the Workers. You can use this API in your external application to execute queries against your D1 database. The full code for this tutorial can be found on <a href="https://github.com/harshil1712/d1-http-example/tree/main">GitHub</a>.</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p>You can check out a similar implementation that uses Zod for validation in <a href="https://github.com/elithrar/http-api-d1-example">this GitHub repository</a>. If you want to build an OpenAPI compliant API for your D1 database, you should use the <a href="https://github.com/cloudflare/workers-sdk/tree/main/templates/worker-openapi">Cloudflare Workers OpenAPI 3.1 template</a>.</p>
