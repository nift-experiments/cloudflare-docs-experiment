<p>Containers can access <a href="/workers/runtime-apis/bindings/">Workers bindings</a> — KV, R2, D1, Durable Objects, and others — through <a href="/containers/guides/outbound-traffic/#define-outbound-handlers">outbound handlers</a>. An outbound handler intercepts HTTP requests from the container and runs inside the Workers runtime, where all of your configured bindings are available.</p>
<p>The container makes a plain HTTP request to a virtual hostname (for example, <code>http://my.kv/some-key</code>), and the outbound handler resolves it using the bound resource. No SDK or client library is required inside the container.</p>
<h2 id="use-bindings-in-outbound-handlers">Use bindings in outbound handlers</h2>
<p>Define an <code>outboundByHost</code> handler for each virtual hostname. The <code>env</code> argument gives you access to every binding declared in your Wrangler configuration.</p>
<pre><code class="language-js">export class MyContainer extends Container {}&#10;&#10;MyContainer.outboundByHost = {&#10;	&quot;my.kv&quot;: async (request, env, ctx) =&gt; {&#10;		const url = new URL(request.url);&#10;		const key = url.pathname.slice(1);&#10;		const value = await env.KV.get(key);&#10;		return new Response(value);&#10;	},&#10;	&quot;my.r2&quot;: async (request, env, ctx) =&gt; {&#10;		const url = new URL(request.url);&#10;		// Scope access to this container&#x27;s ID&#10;		const path = `${ctx.containerId}${url.pathname}`;&#10;		const object = await env.R2.get(path);&#10;		return new Response(object?.body ?? null, { status: object ? 200 : 404 });&#10;	},&#10;};&#10;</code></pre>
<p>The container calls <code>http://my.kv/some-key</code> and the handler resolves it using the KV binding. A call to <code>http://my.r2/file.png</code> reads from R2, scoped to the current container instance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7149.md")
</aside>
<h2 id="access-durable-object-state">Access Durable Object state</h2>
<p>The <code>ctx</code> argument exposes <code>containerId</code>, which lets you interact with the container's own Durable Object from an outbound handler.</p>
<pre><code class="language-js">&quot;get-state.do&quot;: async (request, env, ctx) =&gt; {&#10;  const id = env.MY_CONTAINER.idFromString(ctx.containerId);&#10;  const stub = env.MY_CONTAINER.get(id);&#10;  // Assumes getStateForKey is defined on your DO&#10;  return stub.getStateForKey(request.body);&#10;},&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/containers/guides/outbound-traffic/">Handle outbound traffic</a> — Block, allow, and intercept all outbound HTTP from a container</li>
<li><a href="/containers/configuration/environment-variables/">Environment variables and secrets</a> — Configure secrets and environment variables</li>
<li><a href="/durable-objects/api/container/">Durable Object interface</a> — Full <code>ctx.container</code> API reference</li>
</ul>
