---
cp9:
  canonical: https://developers.cloudflare.com/hyperdrive/tutorials/serverless-timeseries-api-with-timescale/
  description: In this tutorial, you will learn to build an API on Workers which will ingest and query time-series data stored in Timescale.
  full_title: Create a serverless, globally distributed time-series API with Timescale · Cloudflare Hyperdrive docs
  head_html: <title>Create a serverless, globally distributed time-series API with Timescale · Cloudflare Hyperdrive docs</title><meta name="generator" content="Nift"><meta name="description" content="In this tutorial, you will learn to build an API on Workers which will ingest and query time-series data stored in Timescale."><link rel="canonical" href="https://developers.cloudflare.com/hyperdrive/tutorials/serverless-timeseries-api-with-timescale/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/hyperdrive/tutorials/serverless-timeseries-api-with-timescale/index.md"><meta property="og:title" content="Create a serverless, globally distributed time-series API with Timescale · Cloudflare Hyperdrive docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="In this tutorial, you will learn to build an API on Workers which will ingest and query time-series data stored in Timescale."><meta property="og:url" content="https://developers.cloudflare.com/hyperdrive/tutorials/serverless-timeseries-api-with-timescale/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Hyperdrive"><meta name="algolia_product_filter" content="Hyperdrive"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="PostgreSQL,TypeScript,SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/hyperdrive/tutorials/serverless-timeseries-api-with-timescale/#page","headline":"Create a serverless, globally distributed time-series API with Timescale \u00b7 Cloudflare Hyperdrive docs","description":"In this tutorial, you will learn to build an API on Workers which will ingest and query time-series data stored in Timescale.","url":"https://developers.cloudflare.com/hyperdrive/tutorials/serverless-timeseries-api-with-timescale/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["PostgreSQL","TypeScript","SQL"]}</script>
  markdown: true
  noindex: false
  route: /hyperdrive/tutorials/serverless-timeseries-api-with-timescale/
  schema: 1
---
<p>In this tutorial, you will learn to build an API on Workers which will ingest and query time-series data stored in <a href="https://www.timescale.com/">Timescale</a> (they make PostgreSQL faster in the cloud).</p>
<p>You will create and deploy a Worker function that exposes API routes for ingesting data, and use <a href="https://developers.cloudflare.com/hyperdrive/">Hyperdrive</a> to proxy your database connection from the edge and maintain a connection pool to prevent us having to make a new database connection on every request.</p>
<p>You will learn how to:</p>
<ul>
<li>Build and deploy a Cloudflare Worker.</li>
<li>Use Worker secrets with the Wrangler CLI.</li>
<li>Deploy a Timescale database service.</li>
<li>Connect your Worker to your Timescale database service with Hyperdrive.</li>
<li>Query your new API.</li>
</ul>
<p>You can learn more about Timescale by reading their <a href="https://docs.timescale.com/getting-started/latest/services/">documentation</a>.</p>
<hr />
<h2 id="1-create-a-worker-project"><ol>
<li>Create a Worker project</li>
</ol></h2>
<p>Run the following command to create a Worker project from the command line:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm create cloudflare@latest -- timescale-api</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- timescale-api" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn create cloudflare timescale-api</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare timescale-api" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm create cloudflare@latest timescale-api</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest timescale-api" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Make note of the URL that your application was deployed to. You will be using it when you configure your GitHub webhook.</p>
<p>Change into the directory you just created for your Worker project:</p>
<pre tabindex="0"><code class="language-sh">cd timescale-api&#10;</code></pre>
<h2 id="2-prepare-your-timescale-service"><ol start="2">
<li>Prepare your Timescale Service</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9017.md")
</aside>
<p>If you are creating a new service, go to the <a href="https://console.cloud.timescale.com/">Timescale Console</a> and follow these steps:</p>
<ol>
<li>Select <strong>Create Service</strong> by selecting the black plus in the upper right.</li>
<li>Choose <strong>Time Series</strong> as the service type.</li>
<li>Choose your desired region and instance size. 1 CPU will be enough for this tutorial.</li>
<li>Set a service name to replace the randomly generated one.</li>
<li>Select <strong>Create Service</strong>.</li>
<li>On the right hand side, expand the <strong>Connection Info</strong> dialog and copy the <strong>Service URL</strong>.</li>
<li>Copy the password which is displayed. You will not be able to retrieve this again.</li>
<li>Select <strong>I stored my password, go to service overview</strong>.</li>
</ol>
<p>If you are using a service you created previously, you can retrieve your service connection information in the <a href="https://console.cloud.timescale.com/">Timescale Console</a>:</p>
<ol>
<li>Select the service (database) you want Hyperdrive to connect to.</li>
<li>Expand <strong>Connection info</strong>.</li>
<li>Copy the <strong>Service URL</strong>. The Service URL is the connection string that Hyperdrive will use to connect. This string includes the database hostname, port number and database name.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9016.md")
</aside>
<p>Insert your password into the <strong>Service URL</strong> as follows (leaving the portion after the @ untouched):</p>
<pre tabindex="0"><code class="language-txt">postgres://tsdbadmin:YOURPASSWORD@...&#10;</code></pre>
<p>This will be referred to as <strong>SERVICEURL</strong> in the following sections.</p>
<h2 id="3-create-your-hypertable"><ol start="3">
<li>Create your Hypertable</li>
</ol></h2>
<p>Timescale allows you to convert regular PostgreSQL tables into <a href="https://docs.timescale.com/use-timescale/latest/hypertables/">hypertables</a>, tables used to deal with time-series, events, or analytics data. Once you have made this change, Timescale will seamlessly manage the hypertable's partitioning, as well as allow you to apply other features like compression or continuous aggregates.</p>
<p>Connect to your Timescale database using the Service URL you copied in the last step (it has the password embedded).</p>
<p>If you are using the default PostgreSQL CLI tool <a href="https://www.timescale.com/blog/how-to-install-psql-on-mac-ubuntu-debian-windows/"><strong>psql</strong></a> to connect, you would run psql like below (substituting your <strong>Service URL</strong> from the previous step). You could also connect using a graphical tool like <a href="https://www.pgadmin.org/">PgAdmin</a>.</p>
<pre tabindex="0"><code class="language-sh">psql &lt;SERVICEURL&gt;&#10;</code></pre>
<p>Once you are connected, create your table by pasting the following SQL:</p>
<pre tabindex="0"><code class="language-sql">CREATE TABLE readings(&#10;  ts timestamptz DEFAULT now() NOT NULL,&#10;  sensor UUID NOT NULL,&#10;  metadata jsonb,&#10;  value numeric NOT NULL&#10; );&#10;&#10;SELECT create_hypertable(&#x27;readings&#x27;, &#x27;ts&#x27;);&#10;</code></pre>
<p>Timescale will manage the rest for you as you ingest and query data.</p>
<h2 id="4-create-a-database-configuration"><ol start="4">
<li>Create a database configuration</li>
</ol></h2>
<p>To create a new Hyperdrive instance you will need:</p>
<ul>
<li>Your <strong>SERVICEURL</strong> from <a href="/hyperdrive/tutorials/serverless-timeseries-api-with-timescale/#2-prepare-your-timescale-service">step 2</a>.</li>
<li>A name for your Hyperdrive service. For this tutorial, you will use <strong>hyperdrive</strong>.</li>
</ul>
<p>Hyperdrive uses the <code>create</code> command with the <code>--connection-string</code> argument to pass this information. Run it as follows:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler hyperdrive create hyperdrive --connection-string=&quot;SERVICEURL&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9015.md")
</aside>
<p>This command outputs your Hyperdrive ID. You can now bind your Hyperdrive configuration to your Worker in your Wrangler configuration by replacing the content with the following:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9018.md")
</div>
<p>Install the Postgres driver into your Worker project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add pg" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add pg</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add pg" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Now copy the below Worker code, and replace the current code in <code>./src/index.ts</code>. The code below:</p>
<ol>
<li>Uses Hyperdrive to connect to Timescale using the connection string generated from <code>env.HYPERDRIVE.connectionString</code> directly to the driver.</li>
<li>Creates a <code>POST</code> route which accepts an array of JSON readings to insert into Timescale in one transaction.</li>
<li>Creates a <code>GET</code> route which takes a <code>limit</code> parameter and returns the most recent readings. This could be adapted to filter by ID or by timestamp.</li>
</ol>
<pre tabindex="0"><code class="language-ts">import { Client } from &quot;pg&quot;;&#10;&#10;export interface Env {&#10;	HYPERDRIVE: Hyperdrive;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx): Promise&lt;Response&gt; {&#10;		// Create a new client on each request. Hyperdrive maintains the underlying&#10;		// database connection pool, so creating a new client is fast.&#10;		const client = new Client({&#10;			connectionString: env.HYPERDRIVE.connectionString,&#10;		});&#10;		await client.connect();&#10;&#10;		const url = new URL(request.url);&#10;		// Create a route for inserting JSON as readings&#10;		if (request.method === &quot;POST&quot; &amp;&amp; url.pathname === &quot;/readings&quot;) {&#10;			// Parse the request&#x27;s JSON payload&#10;			const productData = await request.json();&#10;&#10;			// Write the raw query. You are using jsonb_to_recordset to expand the JSON&#10;			// to PG INSERT format to insert all items at once, and using coalesce to&#10;			// insert with the current timestamp if no ts field exists&#10;			const insertQuery = `&#10;      INSERT INTO readings (ts, sensor, metadata, value)&#10;      SELECT coalesce(ts, now()), sensor, metadata, value FROM jsonb_to_recordset($1::jsonb)&#10;      AS t(ts timestamptz, sensor UUID, metadata jsonb, value numeric)&#10;  `;&#10;&#10;			const insertResult = await client.query(insertQuery, [&#10;				JSON.stringify(productData),&#10;			]);&#10;&#10;			// Collect the raw row count inserted to return&#10;			const resp = new Response(JSON.stringify(insertResult.rowCount), {&#10;				headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;			});&#10;&#10;			return resp;&#10;&#10;			// Create a route for querying within a time-frame&#10;		} else if (request.method === &quot;GET&quot; &amp;&amp; url.pathname === &quot;/readings&quot;) {&#10;			const limit = url.searchParams.get(&quot;limit&quot;);&#10;&#10;			// Query the readings table using the limit param passed&#10;			const result = await client.query(&#10;				&quot;SELECT * FROM readings ORDER BY ts DESC LIMIT $1&quot;,&#10;				[limit],&#10;			);&#10;&#10;			// Return the result as JSON&#10;			const resp = new Response(JSON.stringify(result.rows), {&#10;				headers: { &quot;Content-Type&quot;: &quot;application/json&quot; },&#10;			});&#10;&#10;			return resp;&#10;		}&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="5-deploy-your-worker"><ol start="5">
<li>Deploy your Worker</li>
</ol></h2>
<p>Run the following command to redeploy your Worker:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your application is now live and accessible at <code>timescale-api.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>. The exact URI will be shown in the output of the wrangler command you just ran.</p>
<p>After deploying, you can interact with your Timescale IoT readings database using your Cloudflare Worker. Connection from the edge will be faster because you are using Cloudflare Hyperdrive to connect from the edge.</p>
<p>You can now use your Cloudflare Worker to insert new rows into the <code>readings</code> table. To test this functionality, send a <code>POST</code> request to your Worker’s URL with the <code>/readings</code> path, along with a JSON payload containing the new product data:</p>
<pre tabindex="0"><code class="language-json">[&#10;	{ &quot;sensor&quot;: &quot;6f3e43a4-d1c1-4cb6-b928-0ac0efaf84a5&quot;, &quot;value&quot;: 0.3 },&#10;	{ &quot;sensor&quot;: &quot;d538f9fa-f6de-46e5-9fa2-d7ee9a0f0a68&quot;, &quot;value&quot;: 10.8 },&#10;	{ &quot;sensor&quot;: &quot;5cb674a0-460d-4c80-8113-28927f658f5f&quot;, &quot;value&quot;: 18.8 },&#10;	{ &quot;sensor&quot;: &quot;03307bae-d5b8-42ad-8f17-1c810e0fbe63&quot;, &quot;value&quot;: 20.0 },&#10;	{ &quot;sensor&quot;: &quot;64494acc-4aa5-413c-bd09-2e5b3ece8ad7&quot;, &quot;value&quot;: 13.1 },&#10;	{ &quot;sensor&quot;: &quot;0a361f03-d7ec-4e61-822f-2857b52b74b3&quot;, &quot;value&quot;: 1.1 },&#10;	{ &quot;sensor&quot;: &quot;50f91cdc-fd19-40d2-b2b0-c90db3394981&quot;, &quot;value&quot;: 10.3 }&#10;]&#10;</code></pre>
<p>This tutorial omits the <code>ts</code> (the timestamp) and <code>metadata</code> (the JSON blob) so they will be set to <code>now()</code> and <code>NULL</code> respectively.</p>
<p>Once you have sent the <code>POST</code> request you can also issue a <code>GET</code> request to your Worker’s URL with the <code>/readings</code> path. Set the <code>limit</code> parameter to control the amount of returned records.</p>
<p>If you have <strong>curl</strong> installed you can test with the following commands (replace <code>&lt;YOUR_SUBDOMAIN&gt;</code> with your subdomain from the deploy command above):</p>
<pre tabindex="0"><code class="language-bash">curl --request POST --data @- &#x27;https://timescale-api.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/readings&#x27; &lt;&lt;EOF&#10;[&#10;  { &quot;sensor&quot;: &quot;6f3e43a4-d1c1-4cb6-b928-0ac0efaf84a5&quot;, &quot;value&quot;:0.3},&#10;  { &quot;sensor&quot;: &quot;d538f9fa-f6de-46e5-9fa2-d7ee9a0f0a68&quot;, &quot;value&quot;:10.8},&#10;  { &quot;sensor&quot;: &quot;5cb674a0-460d-4c80-8113-28927f658f5f&quot;, &quot;value&quot;:18.8},&#10;  { &quot;sensor&quot;: &quot;03307bae-d5b8-42ad-8f17-1c810e0fbe63&quot;, &quot;value&quot;:20.0},&#10;  { &quot;sensor&quot;: &quot;64494acc-4aa5-413c-bd09-2e5b3ece8ad7&quot;, &quot;value&quot;:13.1},&#10;  { &quot;sensor&quot;: &quot;0a361f03-d7ec-4e61-822f-2857b52b74b3&quot;, &quot;value&quot;:1.1},&#10;  { &quot;sensor&quot;: &quot;50f91cdc-fd19-40d2-b2b0-c90db3394981&quot;, &quot;metadata&quot;: {&quot;color&quot;: &quot;blue&quot; }, &quot;value&quot;:10.3}&#10;]&#10;EOF&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">curl &quot;https://timescale-api.&lt;YOUR_SUBDOMAIN&gt;.workers.dev/readings?limit=10&quot;&#10;</code></pre>
<p>In this tutorial, you have learned how to create a working example to ingest and query readings from the edge with Timescale, Workers, Hyperdrive, and TypeScript.</p>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Learn more about <a href="/hyperdrive/concepts/how-hyperdrive-works/">How Hyperdrive Works</a>.</li>
<li>Learn more about <a href="https://timescale.com">Timescale</a>.</li>
<li>Refer to the <a href="/hyperdrive/observability/troubleshooting/">troubleshooting guide</a> to debug common issues.</li>
</ul>
