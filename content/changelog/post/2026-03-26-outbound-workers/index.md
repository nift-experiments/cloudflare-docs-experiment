<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 26, 2026</time><h2 id="post-title">Easily connect Containers and Sandboxes to Workers</h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><a href="/containers/">Containers</a> and <a href="/sandbox/">Sandboxes</a> now support connecting directly to Workers over HTTP. This allows you to call Workers
functions and <a href="/workers/runtime-apis/bindings/">bindings</a>, like <a href="/kv">KV</a> or <a href="/r2/">R2</a>, from within the container at specific hostnames.</p>
<h4 id="run-worker-code">Run Worker code</h4>
<p>Define an <code>outbound</code> handler to capture any HTTP request or use <code>outboundByHost</code> to capture requests to individual hostnames and IPs.</p>
<pre><code class="language-js">export class MyApp extends Sandbox {}&#10;&#10;MyApp.outbound = async (request, env, ctx) =&gt; {&#10;	// you can run arbitrary functions defined in your Worker on any HTTP request&#10;	return await someWorkersFunction(request.body);&#10;};&#10;&#10;MyApp.outboundByHost = {&#10;	&quot;my.worker&quot;: async (request, env, ctx) =&gt; {&#10;		return await anotherFunction(request.body);&#10;	},&#10;};&#10;</code></pre>
<p>In this example, requests from the container to <code>http://my.worker</code> will run the function defined within <code>outboundByHost</code>,
and any other HTTP requests will run the <code>outbound</code> handler. These handlers run entirely inside the Workers runtime,
outside of the container sandbox.</p>
<h4 id="access-workers-bindings">Access Workers bindings</h4>
<p>Each handler has access to <code>env</code>, so it can call any binding set in <a href="/workers/wrangler/configuration/#bindings">Wrangler config</a>.
Code inside the container makes a standard HTTP request to that hostname and the outbound Worker translates it into a binding call.</p>
<pre><code class="language-js">export class MyApp extends Sandbox {}&#10;&#10;MyApp.outboundByHost = {&#10;	&quot;my.kv&quot;: async (request, env, ctx) =&gt; {&#10;		const key = new URL(request.url).pathname.slice(1);&#10;		const value = await env.KV.get(key);&#10;		return new Response(value ?? &quot;&quot;, { status: value ? 200 : 404 });&#10;	},&#10;	&quot;my.r2&quot;: async (request, env, ctx) =&gt; {&#10;		const key = new URL(request.url).pathname.slice(1);&#10;		const object = await env.BUCKET.get(key);&#10;		return new Response(object?.body ?? &quot;&quot;, { status: object ? 200 : 404 });&#10;	},&#10;};&#10;</code></pre>
<p>Now, from inside the container sandbox, <code>curl http://my.kv/some-key</code> will access <a href="/kv">Workers KV</a> and <code>curl http://my.r2/some-object</code> will access <a href="/r2/">R2</a>.</p>
<h4 id="access-durable-object-state">Access Durable Object state</h4>
<p>Use <code>ctx.containerId</code> to reference the container's automatically provisioned <a href="/durable-objects">Durable Object</a>.</p>
<pre><code class="language-js">export class MyContainer extends Container {}&#10;&#10;MyContainer.outboundByHost = {&#10;	&quot;get-state.do&quot;: async (request, env, ctx) =&gt; {&#10;		const id = env.MY_CONTAINER.idFromString(ctx.containerId);&#10;		const stub = env.MY_CONTAINER.get(id);&#10;		return stub.getStateForKey(request.body);&#10;	},&#10;};&#10;</code></pre>
<p>This provides an easy way to associate state with any container instance, and includes a <a href="/durable-objects/get-started/#2-write-a-durable-object-class-using-sql-api">built-in SQLite database</a>.</p>
<h4 id="get-started-today">Get Started Today</h4>
<p>Upgrade to <code>@cloudflare/containers</code> version 0.2.0 or later, or <code>@cloudflare/sandbox</code> version 0.8.0 or later to use outbound Workers.</p>
<p>Refer to <a href="/containers/guides/outbound-traffic/">Containers outbound traffic</a> and <a href="/sandbox/guides/outbound-traffic/">Sandboxes outbound traffic</a> for more details and examples.</p>
</div></article></div>
