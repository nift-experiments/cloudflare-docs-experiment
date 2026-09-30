<p>This tutorial explains how to create a TypeScript-based Cloudflare Workers project that can securely access files from and upload files to a <a href="/r2/">Cloudflare R2</a> bucket. Cloudflare R2 allows developers to store large amounts of unstructured data without the costly egress bandwidth fees associated with typical cloud storage services.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To continue:</p>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a> if you have not already.</li>
<li>Install <a href="https://docs.npmjs.com/getting-started"><code>npm</code></a>.</li>
<li>Install <a href="https://nodejs.org/en/"><code>Node.js</code></a>. Use a Node version manager like <a href="https://volta.sh/">Volta</a> or <a href="https://github.com/nvm-sh/nvm">nvm</a> to avoid permission issues and change Node.js versions. <a href="/workers/wrangler/install-and-update/">Wrangler</a> requires a Node version of <code>16.17.0</code> or later.</li>
</ol>
<h2 id="create-a-worker-application">Create a Worker application</h2>
<p>First, use the <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare"><code>create-cloudflare</code> CLI</a> to create a new Worker. To do this, open a terminal window and run the following command:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- upload-r2-assets</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- upload-r2-assets" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare upload-r2-assets</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare upload-r2-assets" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest upload-r2-assets</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest upload-r2-assets" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>Move into your newly created directory:</p>
<pre><code class="language-sh">cd upload-r2-assets&#10;</code></pre>
<h2 id="create-an-r2-bucket">Create an R2 bucket</h2>
<p>Before you integrate R2 bucket access into your Worker application, an R2 bucket must be created:</p>
<pre><code class="language-sh">npx wrangler r2 bucket create &lt;YOUR_BUCKET_NAME&gt;&#10;</code></pre>
<p>Replace <code>&lt;YOUR_BUCKET_NAME&gt;</code> with the name you want to assign to your bucket. List your account's R2 buckets to verify that a new bucket has been added:</p>
<pre><code class="language-sh">npx wrangler r2 bucket list&#10;</code></pre>
<h2 id="configure-access-to-an-r2-bucket">Configure access to an R2 bucket</h2>
<p>After your new R2 bucket is ready, use it inside your Worker application.</p>
<p>Use your R2 bucket inside your Worker project by modifying the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> to include an R2 bucket <a href="/workers/runtime-apis/bindings/">binding</a>. Add the following R2 bucket binding to your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16050.md")
</div>
<p>Give your R2 bucket binding name. Replace <code>&lt;YOUR_BUCKET_NAME&gt;</code> with the name of the R2 bucket you created earlier.</p>
<p>Your Worker application can now access your R2 bucket using the <code>MY_BUCKET</code> variable. You can now perform CRUD (Create, Read, Update, Delete) operations on the contents of the bucket.</p>
<h2 id="fetch-from-an-r2-bucket">Fetch from an R2 bucket</h2>
<p>After setting up an R2 bucket binding, you will implement the functionalities for the Worker to interact with the R2 bucket, such as, fetching files from the bucket and uploading files to the bucket.</p>
<p>To fetch files from the R2 bucket, use the <code>BINDING.get</code> function. In the below example, the R2 bucket binding is called <code>MY_BUCKET</code>. Using <code>.get(key)</code>, you can retrieve an asset based on the URL pathname as the key. In this example, the URL pathname is <code>/image.png</code>, and the asset key is <code>image.png</code>.</p>
<pre><code class="language-ts">interface Env {&#10;	MY_BUCKET: R2Bucket;&#10;}&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		// For example, the request URL my-worker.account.workers.dev/image.png&#10;		const url = new URL(request.url);&#10;		const key = url.pathname.slice(1);&#10;		// Retrieve the key &quot;image.png&quot;&#10;		const object = await env.MY_BUCKET.get(key);&#10;&#10;		if (object === null) {&#10;			return new Response(&quot;Object Not Found&quot;, { status: 404 });&#10;		}&#10;&#10;		const headers = new Headers();&#10;		object.writeHttpMetadata(headers);&#10;		headers.set(&quot;etag&quot;, object.httpEtag);&#10;&#10;		return new Response(object.body, {&#10;			headers,&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>The code written above fetches and returns data from the R2 bucket when a <code>GET</code> request is made to the Worker application using a specific URL path.</p>
<h2 id="upload-securely-to-an-r2-bucket">Upload securely to an R2 bucket</h2>
<p>Next, you will add the ability to upload to your R2 bucket using authentication. To securely authenticate your upload requests, use <a href="/workers/wrangler/commands/general/#secret">Wrangler's secret capability</a>. Wrangler was installed when you ran the <code>create cloudflare@latest</code> command.</p>
<p>Create a secret value of your choice -- for instance, a random string or password. Using the Wrangler CLI, add the secret to your project as <code>AUTH_SECRET</code>:</p>
<pre><code class="language-sh">npx wrangler secret put AUTH_SECRET&#10;</code></pre>
<p>Now, add a new code path that handles a <code>PUT</code> HTTP request. This new code will check that the previously uploaded secret is correctly used for authentication, and then upload to R2 using <code>MY_BUCKET.put(key, data)</code>:</p>
<pre><code class="language-ts">interface Env {&#10;	MY_BUCKET: R2Bucket;&#10;	AUTH_SECRET: string;&#10;}&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		if (request.method === &quot;PUT&quot;) {&#10;			// Note that you could require authentication for all requests&#10;			// by moving this code to the top of the fetch function.&#10;			const auth = request.headers.get(&quot;Authorization&quot;);&#10;			const expectedAuth = `Bearer ${env.AUTH_SECRET}`;&#10;&#10;			if (!auth || auth !== expectedAuth) {&#10;				return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;			}&#10;&#10;			const url = new URL(request.url);&#10;			const key = url.pathname.slice(1);&#10;			await env.MY_BUCKET.put(key, request.body);&#10;			return new Response(`Object ${key} uploaded successfully!`);&#10;		}&#10;&#10;		// include the previous code here...&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>This approach ensures that only clients who provide a valid bearer token, via the <code>Authorization</code> header equal to the <code>AUTH_SECRET</code> value, will be permitted to upload to the R2 bucket. If you used a different binding name than <code>AUTH_SECRET</code>, replace it in the code above.</p>
<h2 id="deploy-your-worker-application">Deploy your Worker application</h2>
<p>After completing your Cloudflare Worker project, deploy it to Cloudflare. Make sure you are in your Worker application directory that you created for this tutorial, then run:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>Your application is now live and accessible at <code>&lt;YOUR_WORKER&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>.</p>
<p>You have successfully created a Cloudflare Worker that allows you to interact with an R2 bucket to accomplish tasks such as uploading and downloading files. You can now use this as a starting point for your own projects.</p>
<h2 id="next-steps">Next steps</h2>
<p>To build more with R2 and Workers, refer to <a href="/workers/tutorials/">Tutorials</a> and the <a href="/r2/">R2 documentation</a>.</p>
<p>If you have any questions, need assistance, or would like to share your project, join the Cloudflare Developer community on <a href="https://discord.cloudflare.com">Discord</a> to connect with fellow developers and the Cloudflare team.</p>
