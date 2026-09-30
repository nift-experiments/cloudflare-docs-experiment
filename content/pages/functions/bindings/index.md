<p>A <a href="/workers/runtime-apis/bindings/">binding</a> enables your Pages Functions to interact with resources on the Cloudflare developer platform. Use bindings to integrate your Pages Functions with Cloudflare resources like <a href="/kv/concepts/how-kv-works/">KV</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/r2/">R2</a>, and <a href="/d1/">D1</a>. You can set bindings for both production and preview environments.</p>
<p>This guide will instruct you on configuring a binding for your Pages Function. You must already have a Cloudflare Developer Platform resource set up to continue.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10971.md")
</aside>
<h2 id="kv-namespaces">KV namespaces</h2>
<p><a href="/kv/concepts/kv-namespaces/">Workers KV</a> is Cloudflare's key-value storage solution.</p>
<p>To bind your KV namespace to your Pages Function, you can configure a KV namespace binding in the <a href="/pages/functions/wrangler-configuration/#kv-namespaces">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>To configure a KV namespace binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Bindings** > **Add** > **KV namespace**.
4. Give your binding a name under **Variable name**.
5. Under **KV namespace**, select your desired namespace.
6. Redeploy your project for the binding to take effect.
<p>Below is an example of how to use KV in your Function. In the following example, your KV namespace binding is called <code>TODO_LIST</code> and you can access the binding in your Function code on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10974.md")
</div></div>
<h3 id="interact-with-your-kv-namespaces-locally">Interact with your KV namespaces locally</h3>
<p>You can interact with your KV namespace bindings locally in one of two ways:</p>
<ul>
<li>Configure your Pages project's Wrangler file and run <a href="/workers/wrangler/commands/pages/#pages-dev"><code>npx wrangler pages dev</code></a>.</li>
<li>Pass arguments to <code>wrangler pages dev</code> directly.</li>
</ul>
<p>To interact with your KV namespace binding locally by passing arguments to the Wrangler CLI, add <code>-k &lt;BINDING_NAME&gt;</code> or <code>--kv=&lt;BINDING_NAME&gt;</code> to the <code>wrangler pages dev</code> command. For example, if your KV namespace is bound your Function via the <code>TODO_LIST</code> binding, access the KV namespace in local development by running:</p>
<pre><code class="language-sh">npx wrangler pages dev &lt;OUTPUT_DIR&gt; --kv=TODO_LIST&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10970.md")
</aside>
<h2 id="durable-objects">Durable Objects</h2>
<p><a href="/durable-objects/">Durable Objects</a> (DO) are Cloudflare's strongly consistent data store that power capabilities such as connecting WebSockets and handling state.</p>
<p>You must create a Durable Object Worker and bind it to your Pages project using the Cloudflare dashboard or your Pages project's <a href="/pages/functions/wrangler-configuration/">Wrangler configuration file</a>. You cannot create and deploy a Durable Object within a Pages project.</p>
<p>To bind your Durable Object to your Pages Function, you can configure a Durable Object binding in the <a href="/pages/functions/wrangler-configuration/#kv-namespaces">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>To configure a Durable Object binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Bindings** > **Add** > **Durable Object**.
4. Give your binding a name under **Variable name**.
5. Under **Durable Object namespace**, select your desired namespace.
6. Redeploy your project for the binding to take effect.
<p>Below is an example of how to use Durable Objects in your Function. In the following example, your DO binding is called <code>DURABLE_OBJECT</code> and you can access the binding in your Function code on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10977.md")
</div></div>
<h3 id="interact-with-your-durable-object-namespaces-locally">Interact with your Durable Object namespaces locally</h3>
<p>You can interact with your Durable Object bindings locally in one of two ways:</p>
<ul>
<li>Configure your Pages project's Wrangler file and run <a href="/workers/wrangler/commands/pages/#pages-dev"><code>npx wrangler pages dev</code></a>.</li>
<li>Pass arguments to <code>wrangler pages dev</code> directly.</li>
</ul>
<p>While developing locally, to interact with a Durable Object namespace, run <code>wrangler dev</code> in the directory of the Worker exporting the Durable Object. In another terminal, run <code>wrangler pages dev</code> in the directory of your Pages project.</p>
<p>To interact with your Durable Object namespace locally via the Wrangler CLI, append <code>--do &lt;BINDING_NAME&gt;=&lt;CLASS_NAME&gt;@&lt;SCRIPT_NAME&gt;</code> to <code>wrangler pages dev</code>. <code>CLASS_NAME</code> indicates the Durable Object class name and <code>SCRIPT_NAME</code> the name of your Worker.</p>
<p>For example, if your Worker is called <code>do-worker</code> and it declares a Durable Object class called <code>DurableObjectExample</code>, access this Durable Object by running <code>npx wrangler dev</code> in the <code>do-worker</code> directory. At the same time, run <code>npx wrangler pages dev &lt;OUTPUT_DIR&gt; --do MY_DO=DurableObjectExample@do-worker</code> in your Pages' project directory. Interact with the <code>MY_DO</code> binding in your Function code by using <code>context.env</code> (for example, <code>context.env.MY_DO</code>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10969.md")
</aside>
<h2 id="r2-buckets">R2 buckets</h2>
<p><a href="/r2/">R2</a> is Cloudflare's blob storage solution that allows developers to store large amounts of unstructured data without the egress fees.</p>
<p>To bind your R2 bucket to your Pages Function, you can configure a R2 bucket binding in the <a href="/pages/functions/wrangler-configuration/#r2-buckets">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>To configure a R2 bucket binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Bindings** > **Add** > **R2 bucket**.
4. Give your binding a name under **Variable name**.
5. Under **R2 bucket**, select your desired R2 bucket.
6. Redeploy your project for the binding to take effect.
<p>Below is an example of how to use R2 buckets in your Function. In the following example, your R2 bucket binding is called <code>BUCKET</code> and you can access the binding in your Function code on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10980.md")
</div></div>
<h3 id="interact-with-your-r2-buckets-locally">Interact with your R2 buckets locally</h3>
<p>You can interact with your R2 bucket bindings locally in one of two ways:</p>
<ul>
<li>Configure your Pages project's Wrangler file and run <a href="/workers/wrangler/commands/pages/#pages-dev"><code>npx wrangler pages dev</code></a>.</li>
<li>Pass arguments to <code>wrangler pages dev</code> directly.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10968.md")
</aside>
<p>To interact with an R2 bucket locally via the Wrangler CLI, add <code>--r2=&lt;BINDING_NAME&gt;</code> to the <code>wrangler pages dev</code> command. If your R2 bucket is bound to your Function with the <code>BUCKET</code> binding, access this R2 bucket in local development by running:</p>
<pre><code class="language-sh">npx wrangler pages dev &lt;OUTPUT_DIR&gt; --r2=BUCKET&#10;</code></pre>
<p>Interact with this binding by using <code>context.env</code> (for example, <code>context.env.BUCKET</code>.)</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10967.md")
</aside>
<h2 id="d1-databases">D1 databases</h2>
<p><a href="/d1/">D1</a> is Cloudflare's native serverless database.</p>
<p>To bind your D1 database to your Pages Function, you can configure a D1 database binding in the <a href="/pages/functions/wrangler-configuration/#d1-databases">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>To configure a D1 database binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Bindings** > **Add**> **D1 database bindings**.
4. Give your binding a name under **Variable name**.
5. Under **D1 database**, select your desired D1 database.
6. Redeploy your project for the binding to take effect.
<p>Below is an example of how to use D1 in your Function. In the following example, your D1 database binding is <code>NORTHWIND_DB</code> and you can access the binding in your Function code on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10983.md")
</div></div>
<h3 id="interact-with-your-d1-databases-locally">Interact with your D1 databases locally</h3>
<p>You can interact with your D1 database bindings locally in one of two ways:</p>
<ul>
<li>Configure your Pages project's Wrangler file and run <a href="/workers/wrangler/commands/pages/#pages-dev"><code>npx wrangler pages dev</code></a>.</li>
<li>Pass arguments to <code>wrangler pages dev</code> directly.</li>
</ul>
<p>To interact with a D1 database via the Wrangler CLI while <a href="/d1/best-practices/local-development/#develop-locally-with-pages">developing locally</a>, add <code>--d1 &lt;BINDING_NAME&gt;=&lt;DATABASE_ID&gt;</code> to the <code>wrangler pages dev</code> command.</p>
<p>If your D1 database is bound to your Pages Function via the <code>NORTHWIND_DB</code> binding and the <code>database_id</code> in your Wrangler file is <code>xxxx-xxxx-xxxx-xxxx-xxxx</code>, access this database in local development by running:</p>
<pre><code class="language-sh">npx wrangler pages dev &lt;OUTPUT_DIR&gt; --d1 NORTHWIND_DB=xxxx-xxxx-xxxx-xxxx-xxxx&#10;</code></pre>
<p>Interact with this binding by using <code>context.env</code> (for example, <code>context.env.NORTHWIND_DB</code>.)</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10966.md")
</aside>
<p>Refer to the <a href="/d1/worker-api/">D1 Workers Binding API documentation</a> for the API methods available on your D1 binding.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10965.md")
</aside>
<h2 id="vectorize-indexes">Vectorize indexes</h2>
<p><a href="/vectorize/">Vectorize</a> is Cloudflare’s native vector database.</p>
<p>To bind your Vectorize index to your Pages Function, you can configure a Vectorize index binding in the <a href="/pages/functions/wrangler-configuration/#vectorize-indexes">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>To configure a Vectorize index binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Choose whether you would like to set up the binding in your **Production** or **Preview** environment.
3. Select your Pages project > **Settings**.
4. Go to **Bindings** > **Add** > **Vectorize index**.
5. Give your binding a name under **Variable name**.
6. Under **Vectorize index**, select your desired Vectorize index.
8. Redeploy your project for the binding to take effect.
<h3 id="use-vectorize-index-bindings">Use Vectorize index bindings</h3>
<p>To use Vectorize index in your Pages Function, you can access your Vectorize index binding in your Pages Function code. In the following example, your Vectorize index binding is called <code>VECTORIZE_INDEX</code> and you can access the binding in your Pages Function code on <code>context.env</code>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10986.md")
</div></div>
<h2 id="workers-ai">Workers AI</h2>
<p><a href="/workers-ai/">Workers AI</a> allows you to run machine learning models, powered by serverless GPUs, on Cloudflare’s global network.</p>
<p>To bind Workers AI to your Pages Function, you can configure a Workers AI binding in the <a href="/pages/functions/wrangler-configuration/#workers-ai">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>When developing locally using Wrangler, you can define an AI binding using the <code>--ai</code> flag. Start Wrangler in development mode by running <a href="/workers/wrangler/commands/general/#dev"><code>wrangler pages dev --ai AI</code></a> to expose the <code>context.env.AI</code> binding.</p>
<p>To configure a Workers AI binding via the Cloudflare dashboard:</p>
<ol>
<li>Go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project > **Settings**.
3. Select your Pages environment > **Bindings** > **Add** > **Workers AI**.
4. Give your binding a name under **Variable name**.
5. Redeploy your project for the binding to take effect.
<h3 id="use-workers-ai-bindings">Use Workers AI bindings</h3>
<p>To use Workers AI in your Pages Function, you can access your Workers AI binding in your Pages Function code. In the following example, your Workers AI binding is called <code>AI</code> and you can access the binding in your Pages Function code on <code>context.env</code>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10989.md")
</div></div>
<h3 id="interact-with-your-workers-ai-binding-locally">Interact with your Workers AI binding locally</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-ai-local-development-usage-charges">Workers AI local development usage charges</h3>
@markup("md", "content/.markup/bodies/10964.md")
</aside>
<p>You can interact with your Workers AI bindings locally in one of two ways:</p>
<ul>
<li>Configure your Pages project's Wrangler file and run <a href="/workers/wrangler/commands/pages/#pages-dev"><code>npx wrangler pages dev</code></a>.</li>
<li>Pass arguments to <code>wrangler pages dev</code> directly.</li>
</ul>
<p>To interact with a Workers AI binding via the Wrangler CLI while developing locally, run:</p>
<pre><code class="language-sh">npx wrangler pages dev --ai=&lt;BINDING_NAME&gt;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10963.md")
</aside>
<h2 id="service-bindings">Service bindings</h2>
<p><a href="/workers/runtime-apis/bindings/service-bindings/">Service bindings</a> enable you to call a Worker from within your Pages Function.</p>
<p>To bind your Pages Function to a Worker, configure a Service binding in your Pages Function using the <a href="/pages/functions/wrangler-configuration/#service-bindings">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>To configure a Service binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Bindings** > **Add** > **Service binding**.
4. Give your binding a name under **Variable name**.
5. Under **Service**, select your desired Worker.
6. Redeploy your project for the binding to take effect.
<p>Below is an example of how to use Service bindings in your Function. In the following example, your Service binding is called <code>SERVICE</code> and you can access the binding in your Function code on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10992.md")
</div></div>
<h3 id="interact-with-your-service-bindings-locally">Interact with your Service bindings locally</h3>
<p>You can interact with your Service bindings locally in one of two ways:</p>
<ul>
<li>Configure your Pages project's Wrangler file and run <a href="/workers/wrangler/commands/pages/#pages-dev"><code>npx wrangler pages dev</code></a>.</li>
<li>Pass arguments to <code>wrangler pages dev</code> directly.</li>
</ul>
<p>To interact with a <a href="/workers/runtime-apis/bindings/service-bindings/">Service binding</a> while developing locally, run the Worker you want to bind to via <code>wrangler dev</code> and in parallel, run <code>wrangler pages dev</code> with <code>--service &lt;BINDING_NAME&gt;=&lt;SCRIPT_NAME&gt;</code> where <code>SCRIPT_NAME</code> indicates the name of the Worker. For example, if your Worker is called <code>my-worker</code>, connect with this Worker by running it via <code>npx wrangler dev</code> (in the Worker's directory) alongside <code>npx wrangler pages dev &lt;OUTPUT_DIR&gt; --service MY_SERVICE=my-worker</code> (in the Pages' directory). Interact with this binding by using <code>context.env</code> (for example, <code>context.env.MY_SERVICE</code>).</p>
<p>If you set up the Service binding via the Cloudflare dashboard, you will need to append <code>wrangler pages dev</code> with <code>--service &lt;BINDING_NAME&gt;=&lt;SCRIPT_NAME&gt;</code> where <code>BINDING_NAME</code> is the name of the Service binding and <code>SCRIPT_NAME</code> is the name of the Worker.</p>
<p>For example, to develop locally, if your Worker is called <code>my-worker</code>, run <code>npx wrangler dev</code> in the <code>my-worker</code> directory. In a different terminal, also run <code>npx wrangler pages dev &lt;OUTPUT_DIR&gt; --service MY_SERVICE=my-worker</code> in your Pages project directory. Interact with this Service binding by using <code>context.env</code> (for example, <code>context.env.MY_SERVICE</code>).</p>
<p>Wrangler also supports running your Pages project and bound Workers in the same dev session with one command. To try it out, pass multiple -c flags to Wrangler, like this: <code>wrangler pages dev -c wrangler.jsonc -c ../other-worker/wrangler.jsonc</code>. The first argument must point to your Pages configuration file, and the subsequent configurations will be accessible via a Service binding from your Pages project.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10962.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10961.md")
</aside>
<h2 id="queue-producers">Queue Producers</h2>
<p><a href="/queues/configuration/javascript-apis/#producer">Queue Producers</a> enable you to send messages into a queue within your Pages Function.</p>
<p>To bind a queue to your Pages Function, configure a queue producer binding in your Pages Function using the <a href="/pages/functions/wrangler-configuration/#queues-producers">Wrangler configuration file</a> or the Cloudflare dashboard:</p>
<p>To configure a queue producer binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Bindings** > **Add** > **Queue**.
4. Give your binding a name under **Variable name**.
5. Under **Queue**, select your desired queue.
6. Redeploy your project for the binding to take effect.
<p>Below is an example of how to use a queue producer binding in your Function. In this example, the binding is named <code>MY_QUEUE</code> and you can access the binding in your Function code on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10995.md")
</div></div>
<h3 id="interact-with-your-queue-producer-binding-locally">Interact with your Queue Producer binding locally</h3>
<p>If using a queue producer binding with a Pages Function, you will be able to send events to a queue locally. However, it is not possible to consume events from a queue with a Pages Function. You will have to create a <a href="/queues/get-started/#5-create-your-consumer-worker">separate consumer Worker</a> with a <a href="/queues/configuration/javascript-apis/#consumer">queue consumer handler</a> to consume events from the queue. Wrangler does not yet support running separate producer Functions and consumer Workers bound to the same queue locally.</p>
<h2 id="hyperdrive-configs">Hyperdrive configs</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10960.md")
</aside>
<p><a href="/hyperdrive/">Hyperdrive</a> is a service for connecting to your existing databases from Cloudflare Workers and Pages Functions.</p>
<p>To bind your Hyperdrive config to your Pages Function, you can configure a Hyperdrive binding in the <a href="/pages/functions/wrangler-configuration/#hyperdrive">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>To configure a Hyperdrive binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Bindings** > **Add** > **Hyperdrive**.
4. Give your binding a name under **Variable name**.
5. Under **Hyperdrive configuration**, select your desired configuration.
6. Redeploy your project for the binding to take effect.
<p>Below is an example of how to use Hyperdrive in your Function. In the following example, your Hyperdrive config is named <code>HYPERDRIVE</code> and you can access the binding in your Function code on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10998.md")
</div></div>
<h3 id="interact-with-your-hyperdrive-binding-locally">Interact with your Hyperdrive binding locally</h3>
<p>To interact with your Hyperdrive binding locally, you must provide a local connection string to your database that your Pages project will connect to directly. You can set an environment variable <code>CLOUDFLARE_HYPERDRIVE_LOCAL_CONNECTION_STRING_&lt;BINDING_NAME&gt;</code> with the connection string of the database, or use the Wrangler file to configure your Hyperdrive binding with a <code>localConnectionString</code> as specified in <a href="/hyperdrive/configuration/local-development/">Hyperdrive documentation for local development</a>. Then, run <a href="/workers/wrangler/commands/pages/#pages-dev"><code>npx wrangler pages dev &lt;OUTPUT_DIR&gt;</code></a>.</p>
<h2 id="analytics-engine">Analytics Engine</h2>
<p>The <a href="/analytics/analytics-engine/">Analytics Engine</a> binding enables you to write analytics within your Pages Function.</p>
<p>To bind an Analytics Engine dataset to your Pages Function, you must configure an Analytics Engine binding using the <a href="/pages/functions/wrangler-configuration/#analytics-engine-datasets">Wrangler configuration file</a> or the Cloudflare dashboard:</p>
<p>To configure an Analytics Engine binding via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Bindings** > **Add** > **Analytics engine**.
4. Give your binding a name under **Variable name**.
5. Under **Dataset**, input your desired dataset.
6. Redeploy your project for the binding to take effect.
<p>Below is an example of how to use an Analytics Engine binding in your Function. In the following example, the binding is called <code>ANALYTICS_ENGINE</code> and you can access the binding in your Function code on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11001.md")
</div></div>
<h3 id="interact-with-your-analytics-engine-binding-locally">Interact with your Analytics Engine binding locally</h3>
<p>You cannot use an Analytics Engine binding locally.</p>
<h2 id="environment-variables">Environment variables</h2>
<p>An <a href="/workers/configuration/environment-variables/">environment variable</a> is an injected value that can be accessed by your Functions. Environment variables are a type of binding that allow you to attach text strings or JSON values to your Pages Function. It is stored as plain text. Set your environment variables directly within the Cloudflare dashboard for both your production and preview environments at runtime and build-time.</p>
<p>To add environment variables to your Pages project, you can use the <a href="/pages/functions/wrangler-configuration/#environment-variables">Wrangler configuration file</a> or the Cloudflare dashboard.</p>
<p>To configure an environment variable via the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Variables and Secrets** > **Add** .
4. After setting a variable name and value, select **Save**.
<p>Below is an example of how to use environment variables in your Function. The environment variable in this example is <code>ENVIRONMENT</code> and you can access the environment variable on <code>context.env</code>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11004.md")
</div></div>
<h3 id="interact-with-your-environment-variables-locally">Interact with your environment variables locally</h3>
<p>You can interact with your environment variables locally in one of two ways:</p>
<ul>
<li>Configure your Pages project's Wrangler file and running <code>npx wrangler pages dev</code>.</li>
<li>Pass arguments to <a href="/workers/wrangler/commands/pages/#pages-dev"><code>wrangler pages dev</code></a> directly.</li>
</ul>
<p>To interact with your environment variables locally via the Wrangler CLI, add <code>--binding=&lt;ENVIRONMENT_VARIABLE_NAME&gt;=&lt;ENVIRONMENT_VARIABLE_VALUE&gt;</code> to the <code>wrangler pages dev</code> command:</p>
<pre><code class="language-sh">npx wrangler pages dev --binding=&lt;ENVIRONMENT_VARIABLE_NAME&gt;=&lt;ENVIRONMENT_VARIABLE_VALUE&gt;&#10;</code></pre>
<h2 id="secrets">Secrets</h2>
<p>Secrets are a type of binding that allow you to attach encrypted text values to your Pages Function. You cannot see secrets after you set them and can only access secrets programmatically on <code>context.env</code>. Secrets are used for storing sensitive information like API keys and auth tokens.</p>
<p>To add secrets to your Pages project:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Settings** > **Variables and Secrets** > **Add**.
4. Set a variable name and value.
5. Select **Encrypt** to create your secret.
6. Select **Save**.
<p>You use secrets the same way as environment variables. When setting secrets with Wrangler or in the Cloudflare dashboard, it needs to be done before a deployment that uses those secrets. For more guidance, refer to <a href="#environment-variables">Environment variables</a>.</p>
<h3 id="local-development-with-secrets">Local development with secrets</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10958.md")
</aside>
<p>Put secrets for use in local development in either a <code>.dev.vars</code> file or a <code>.env</code> file, in the same directory as the Wrangler configuration file.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10957.md")
</aside>
<aside class="nb-aside info">
@markup("md", "content/.markup/bodies/10956.md")
</aside>
<p>These files should be formatted using the <a href="https://hexdocs.pm/dotenvy/dotenv-file-format.html">dotenv</a> syntax. For example:</p>
<pre><code class="language-bash">SECRET_KEY=&quot;value&quot;&#10;API_TOKEN=&quot;eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9&quot;&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="do-not-commit-secrets-to-git">Do not commit secrets to git</h3>
@markup("md", "content/.markup/bodies/10955.md")
</aside>
<p>To set different secrets for each Cloudflare environment, create files named <code>.dev.vars.&lt;environment-name&gt;</code> or <code>.env.&lt;environment-name&gt;</code>.</p>
<p>When you select a Cloudflare environment in your local development, the corresponding environment-specific file will be loaded ahead of the generic <code>.dev.vars</code> (or <code>.env</code>) file.</p>
<ul>
<li>When using <code>.dev.vars.&lt;environment-name&gt;</code> files, all secrets must be defined per environment. If <code>.dev.vars.&lt;environment-name&gt;</code> exists then only this will be loaded; the <code>.dev.vars</code> file will not be loaded.</li>
<li>In contrast, all matching <code>.env</code> files are loaded and the values are merged. For each variable, the value from the most specific file is used, with the following precedence:
<ul>
<li><code>.env.&lt;environment-name&gt;.local</code> (most specific)</li>
<li><code>.env.local</code></li>
<li><code>.env.&lt;environment-name&gt;</code></li>
<li><code>.env</code> (least specific)</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="controlling-env-handling">Controlling `.env` handling</h3>
@markup("md", "content/.markup/bodies/10954.md")
</aside>
