<p>The Context API provides methods to manage the lifecycle of your Worker or Durable Object.</p>
<p>Context is exposed via the following places:</p>
<ul>
<li>As the third parameter in all <a href="/workers/runtime-apis/handlers/">handlers</a>, including the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a>. (<code>fetch(request, env, ctx)</code>)</li>
<li>As a class property of the <a href="/workers/runtime-apis/bindings/service-bindings/rpc"><code>WorkerEntrypoint</code> class</a> (<code>this.ctx</code>)</li>
</ul>
<p>Note that the Context API is available strictly in stateless contexts, that is, not <a href="/durable-objects/">Durable Objects</a>. However, Durable Objects have a different object, the <a href="/durable-objects/api/state/">Durable Object State</a>, which is available as <code>this.ctx</code> inside a Durable Object class, and provides some of the same functionality as the Context API.</p>
<h2 id="props"><code>props</code></h2>
<p><code>ctx.props</code> provides a way to pass additional configuration to a worker based on the context in which it was invoked. For example, when your Worker is called by another Worker, <code>ctx.props</code> can provide information about the calling worker.</p>
<p>For example, imagine that you are configuring a Worker called &quot;frontend-worker&quot;, which must talk to another Worker called &quot;doc-worker&quot; in order to manipulate documents. You might configure &quot;frontend-worker&quot; with a <a href="/workers/runtime-apis/bindings/service-bindings">Service Binding</a> like:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16157.md")
</div>
<p>Now frontend-worker can make calls to doc-worker with code like <code>env.DOC_SERVICE.getDoc(id)</code>. This will make a <a href="/workers/runtime-apis/rpc/">Remote Procedure Call</a> invoking the method <code>getDoc()</code> of the class <code>DocServiceApi</code>, a <a href="/workers/runtime-apis/bindings/service-bindings/rpc"><code>WorkerEntrypoint</code> class</a> exported by doc-worker.</p>
<p>The configuration contains a <code>props</code> value. This in an arbitrary JSON value. When the <code>DOC_SERVICE</code> binding is used, the <code>DocServiceApi</code> instance receiving the call will be able to access this <code>props</code> value as <code>this.ctx.props</code>. Here, we've configured <code>props</code> to specify that the call comes from frontend-worker, and that it should be allowed to read and write documents. However, the contents of <code>props</code> can be anything you want.</p>
<p>The Workers platform is designed to ensure that <code>ctx.props</code> can only be set by someone who has permission to edit and deploy the worker to which it is being delivered. This means that you can trust that the content of <code>ctx.props</code> is authentic. There is no need to use secret keys or cryptographic signatures in a <code>ctx.props</code> value.</p>
<p><code>ctx.props</code> can also be used to configure an RPC interface to represent a <em>specific</em> resource, thus creating a &quot;custom binding&quot;. For example, we could configure a Service Binding to our &quot;doc-worker&quot; which grants access only to a specific document:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16158.md")
</div>
<p>Here, we've placed a <code>docId</code> property in <code>ctx.props</code>. The <code>DocumentApi</code> class could be designed to provide an API to the specific document identified by <code>ctx.props.docId</code>, and enforcing the given permissions.</p>
<h2 id="exports"><code>exports</code></h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="compatibility-flag-required">Compatibility flag required</h3>
@markup("md", "content/.markup/bodies/16156.md")
</aside>
<p><code>ctx.exports</code> provides automatically-configured &quot;loopback&quot; bindings for all of your top-level exports.</p>
<ul>
<li>For each top-level export that <code>extends WorkerEntrypoint</code> (or simply implements a fetch handler), <code>ctx.exports</code> automatically contains a <a href="/workers/runtime-apis/bindings/service-bindings">Service Binding</a>.</li>
<li>For each top-level export that <code>extends DurableObject</code> (and which has been configured with storage via a <a href="/durable-objects/reference/durable-objects-migrations/">migration</a>), <code>ctx.exports</code> automatically contains a <a href="/durable-objects/api/namespace/">Durable Object namespace binding</a>.</li>
</ul>
<p>For example:</p>
<pre><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Greeter extends WorkerEntrypoint {&#10;	greet(name) {&#10;		return `Hello, ${name}!`;&#10;	}&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		let greeting = await ctx.exports.Greeter.greet(&quot;World&quot;);&#10;		return new Response(greeting);&#10;	},&#10;};&#10;</code></pre>
<p>In this example, the default fetch handler calls the <code>Greeter</code> class over RPC, like how you'd use a Service Binding. However, there is no external configuration required. <code>ctx.exports</code> is populated <em>automatically</em> from your top-level imports.</p>
<h3 id="specifying-ctx-props-when-using-ctx-exports">Specifying <code>ctx.props</code> when using <code>ctx.exports</code></h3>
<p>Loopback Service Bindings in <code>ctx.exports</code> have an extra capability that regular Service Bindings do not: the caller can specify the value of <code>ctx.props</code> that should be delivered to the callee.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16161.md")
</div></div>
<p>Specifying props dynamically is permitted in this case because the caller is the same Worker, and thus can be presumed to be trusted to specify any props. The ability to customize props is particularly useful when the resulting binding is to be passed to another Worker over RPC or used in the <code>env</code> of a <a href="/workers/runtime-apis/bindings/worker-loader/">dynamically-loaded worker</a>.</p>
<p>Note that <code>props</code> values specified in this way are allowed to contain any &quot;persistently&quot; serializable type. This includes all basic <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm">structured cloneable data types</a>. It also includes Service Bindings themselves: you can place a Service Binding into the <code>props</code> of another Service Binding.</p>
<h3 id="typescript-types-for-ctx-exports-and-ctx-props">TypeScript types for <code>ctx.exports</code> and <code>ctx.props</code></h3>
<p>If using TypeScript, you should use <a href="/workers/wrangler/commands/general/#types">the <code>wrangler types</code> command</a> to auto-generate types for your project. The generated types will ensure <code>ctx.exports</code> is typed correctly.</p>
<p>When declaring an entrypoint class that accepts <code>props</code>, make sure to declare it as <code>extends WorkerEntrypoint&lt;Env, Props&gt;</code>, where <code>Props</code> is the type of <code>ctx.props</code>. See the example above.</p>
<h2 id="tracing"><code>tracing</code></h2>
<p><code>ctx.tracing</code> provides access to the <a href="/workers/observability/traces/custom-spans/">custom spans API</a> for creating user-defined trace spans. This is the same object available via <code>import { tracing } from &quot;cloudflare:workers&quot;</code>.</p>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> on your Worker for spans to be recorded.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return ctx.tracing.enterSpan(&quot;handleRequest&quot;, async (span) =&gt; {&#10;			span.setAttribute(&quot;url.path&quot;, new URL(request.url).pathname);&#10;			const data = await env.MY_KV.get(&quot;key&quot;);&#10;			return new Response(data);&#10;		});&#10;	},&#10;};&#10;</code></pre>
<p>For full API details, refer to <a href="/workers/observability/traces/custom-spans/">Custom spans</a>.</p>
<h2 id="waituntil"><code>waitUntil</code></h2>
<p><code>ctx.waitUntil()</code> extends the lifetime of your Worker, allowing you to perform work without blocking returning a response, and that may continue after a response is returned. It accepts a <code>Promise</code>, which the Workers runtime will continue executing, even after a response has been returned by the Worker's <a href="/workers/runtime-apis/handlers/">handler</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="background-work-needs-await-or-waituntil">Background work needs `await` or `waitUntil()`</h3>
@markup("md", "content/.markup/bodies/16155.md")
</aside>
<p>Use <code>ctx.waitUntil()</code> for work that can run after the response is sent, such as logging, analytics, or cache writes, as long as the work can finish within the <code>waitUntil()</code> time limit. If the client is still receiving the response, including a streamed response body, the Worker invocation remains active without <code>ctx.waitUntil()</code>. If your response depends on the work, <code>await</code> the work before returning the response or stream the response as the work completes.</p>
<p><code>waitUntil</code> is commonly used to:</p>
<ul>
<li>Fire off events to external analytics providers. (note that when you use <a href="/analytics/analytics-engine/">Workers Analytics Engine</a>, you do not need to use <code>waitUntil</code>)</li>
<li>Put items into cache using the <a href="/workers/runtime-apis/cache/">Cache API</a></li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="waituntil-has-a-30-second-time-limit-after-invocation-end">`waitUntil` has a 30-second time limit after invocation end</h3>
@markup("md", "content/.markup/bodies/16154.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="alternatives-to-waituntil">Alternatives to waitUntil</h3>
@markup("md", "content/.markup/bodies/16153.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="waituntil-in-durable-objects">`waitUntil` in Durable Objects</h3>
@markup("md", "content/.markup/bodies/16152.md")
</aside>
<p>You can call <code>waitUntil()</code> multiple times. Similar to <code>Promise.allSettled</code>, even if a promise passed to one <code>waitUntil</code> call is rejected, promises passed to other <code>waitUntil()</code> calls will still continue to execute.</p>
<p>For example:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// Forward / proxy original request&#10;		let res = await fetch(request);&#10;&#10;		// Add custom header(s)&#10;		res = new Response(res.body, res);&#10;		res.headers.set(&quot;x-foo&quot;, &quot;bar&quot;);&#10;&#10;		// Cache the response&#10;		// NOTE: Does NOT block / wait&#10;		ctx.waitUntil(caches.default.put(request, res.clone()));&#10;&#10;		// Done&#10;		return res;&#10;	},&#10;};&#10;</code></pre>
<h2 id="passthroughonexception"><code>passThroughOnException</code></h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="reuse-of-body">Reuse of body</h3>
@markup("md", "content/.markup/bodies/16151.md")
</aside>
<p>The <code>passThroughOnException</code> method allows a Worker to <a href="https://community.microfocus.com/cyberres/b/sws-22/posts/security-fundamentals-part-1-fail-open-vs-fail-closed">fail open</a>, and pass a request through to an origin server when a Worker throws an unhandled exception. This can be useful when using Workers as a layer in front of an existing service, allowing the service behind the Worker to handle any unexpected error cases that arise in your Worker.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		ctx.passThroughOnException();&#10;&#10;		try {&#10;			return await fetch(request);&#10;		} catch (error) {&#10;			console.error(&quot;Origin fetch failed&quot;, error);&#10;			return new Response(&quot;Bad Gateway&quot;, { status: 502 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
