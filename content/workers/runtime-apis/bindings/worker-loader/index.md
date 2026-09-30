<aside class="nb-aside note">
<h3 class="nb-aside-title" id="dynamic-worker-loading-is-in-closed-beta">Dynamic Worker Loading is in closed beta</h3>
@markup("md", "content/.markup/bodies/17180.md")
</aside>
<p>A Worker Loader binding allows you to load additional Workers containing arbitrary code at runtime.</p>
<p>An isolate is like a lightweight container. <a href="/workers/reference/how-workers-works/">The Workers platform uses isolates instead of containers or VMs</a>, so every Worker runs in an isolate already. But, a Worker Loader binding allows your Worker to create additional isolates that load arbitrary code on-demand.</p>
<p>Isolates are much cheaper than containers. You can start an isolate in milliseconds, and it's fine to start one just to run a snippet of code and immediately throw away. There's no need to worry about pooling isolates or trying to reuse already-warm isolates, as you would need to do with containers.</p>
<p>Worker Loaders also enable <strong>sandboxing</strong> of code, meaning that you can strictly limit what the code is allowed to do. In particular:</p>
<ul>
<li>You can arrange to intercept or simply block all network requests made by the Worker within.</li>
<li>You can supply the sandboxed Worker with custom bindings to represent specific resources which it should be allowed to access.</li>
</ul>
<p>With proper sandboxing configured, you can safely run code you do not trust in a dynamic isolate.</p>
<h2 id="code-mode">Code Mode</h2>
<p>A primary use case for Dynamic Worker Loaders is <a href="/agents/tools/codemode/">Code Mode</a> in the <a href="/agents/">Agents SDK</a>. Code Mode converts your tools into typed TypeScript APIs and gives the LLM a single &quot;write code&quot; tool. The generated code runs in an isolated Worker sandbox, which lets AI agents chain multiple tool calls in one execution and reduces round-trips through the model.</p>
<p>Code Mode makes <a href="/agents/tools/codemode/ai-sdk/">AI SDK tools</a>, tools from an <a href="/agents/tools/codemode/mcp/">MCP client connection</a>, and <a href="/agents/tools/codemode/openapi/">OpenAPI operations</a> available to model-written code.</p>
<h2 id="basic-usage">Basic usage</h2>
<p>A Worker Loader is a binding with just one method, <code>get()</code>, which loads an isolate. Example usage:</p>
<pre><code class="language-js">let id = &quot;foo&quot;;&#10;&#10;// Get the isolate with the given ID, creating it if no such isolate exists yet.&#10;let worker = env.LOADER.get(id, async () =&gt; {&#10;	// If the isolate does not already exist, this callback is invoked to fetch&#10;	// the isolate&#x27;s Worker code.&#10;&#10;	return {&#10;		compatibilityDate: &quot;2025-06-01&quot;,&#10;&#10;		// Specify the worker&#x27;s code (module files).&#10;		mainModule: &quot;foo.js&quot;,&#10;		modules: {&#10;			&quot;foo.js&quot;:&#10;				&quot;export default {\n&quot; +&#10;				&quot;  fetch(req, env, ctx) { return new Response(&#x27;Hello&#x27;); }\n&quot; +&#10;				&quot;}\n&quot;,&#10;		},&#10;&#10;		// Specify the dynamic Worker&#x27;s environment (`env`). This is specified&#10;		// as a JavaScript object, exactly as you want it to appear to the&#10;		// child Worker. It can contain basic serializable types as well as&#10;		// Service Bindings (see below).&#10;		env: {&#10;			SOME_ENV_VAR: 123,&#10;		},&#10;&#10;		// To block the worker from talking to the internet using `fetch()` or&#10;		// `connect()`, set `globalOutbound` to `null`. You can also set this&#10;		// to any service binding, to have calls be intercepted and redirected&#10;		// to that binding.&#10;		globalOutbound: null,&#10;	};&#10;});&#10;&#10;// Now you can get the Worker&#x27;s entrypoint and send requests to it.&#10;let defaultEntrypoint = worker.getEntrypoint();&#10;await defaultEntrypoint.fetch(&quot;http://example.com&quot;);&#10;&#10;// You can get non-default entrypoints as well, and specify the&#10;// `ctx.props` value to be delivered to the entrypoint.&#10;let someEntrypoint = worker.getEntrypoint(&quot;SomeEntrypointClass&quot;, {&#10;	props: { someProp: 123 },&#10;});&#10;</code></pre>
<h2 id="configuration">Configuration</h2>
<p>To add a dynamic worker loader binding to your worker, add it to your Wrangler config like so:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17181.md")
</div>
<h2 id="api-reference">API Reference</h2>
<h3 id="get"><code>get</code></h3>
<p><code>get(id <span class="nb-type">string</span>, getCodeCallback <span class="nb-type">() =&gt; Promise&lt;WorkerCode&gt;</span> ): <span class="nb-type">WorkerStub</span></code></p>
<p>Loads a Worker with the given ID, returning a <code>WorkerStub</code> which may be used to invoke the Worker.</p>
<p>As a convenience, the loader implements caching of isolates. When a new ID is seen the first time, a new isolate is loaded. But, the isolate may be kept warm in memory for a while. If later invocations of the loader request the same ID, the existing isolate may be returned again, rather than create a new one. But there is no guarantee: a later call with the same ID may instead start a new isolate from scratch.</p>
<p>Whenever the system determines it needs to start a new isolate, and it does not already have a copy of the code cached, it will invoke <code>codeCallback</code> to get the Worker's code. This is an async callback, so the application can load the code from remote storage if desired. The callback returns a <code>WorkerCode</code> object (described below).</p>
<p>Because of the caching, you should ensure that the callback always returns exactly the same content, when called for the same ID. If anything about the content changes, you must use a new ID. But if the content hasn't changed, it's best to reuse the same ID in order to take advantage of caching. If the <code>WorkerCode</code> is different every time, you can pass a random ID.</p>
<p>You could, for example, use IDs of the form <code>&lt;worker-name&gt;:&lt;version-number&gt;</code>, where the version number increments every time the code changes. Or, you could compute IDs based on a hash of the code and config, so that any change results in a new ID.</p>
<p><code>get()</code> returns a <code>WorkerStub</code>, which can be used to send requests to the loaded Worker. Note that the stub is returned synchronously—you do not have to await it. If the Worker is not loaded yet, requests made to the stub will wait for the Worker to load before being delivered. If loading fails, the request will throw an exception.</p>
<p>It is never guaranteed that two requests will go to the same isolate. Even if you use the same <code>WorkerStub</code> to make multiple requests, they could execute in different isolates. The callback passed to <code>loader.get()</code> could be called any number of times (although it is unusual for it to be called more than once).</p>
<h3 id="workercode"><code>WorkerCode</code></h3>
<p>This is the structure returned by <code>getCodeCallback</code> to represent a worker.</p>
<h4 id="compatibilitydate"><code>compatibilityDate <span class="nb-type">string</span></code></h4>
<p>The <a href="/workers/configuration/compatibility-dates/">compatibility date</a> for the Worker. This has the same meaning as the <code>compatibility_date</code> setting in a Wrangler config file.</p>
<h4 id="compatibilityflags"><code>compatibilityFlags <span class="nb-type">string[]</span> <span class="nb-metainfo">Optional</span></code></h4>
<p>An optional list of <a href="/workers/configuration/compatibility-flags">compatibility flags</a> augmenting the compatibility date. This has the same meaning as the <code>compatibility_flags</code> setting in a Wrangler config file.</p>
<h4 id="allowexperimental"><code>allowExperimental <span class="nb-type">boolean</span> <span class="nb-metainfo">Optional</span></code></h4>
<p>If true, then experimental compatibility flags will be permitted in <code>compatibilityFlags</code>. In order to set this, the worker calling the loader must itself have the compatibility flag <code>&quot;experimental&quot;</code> set. Experimental flags cannot be enabled in production.</p>
<h4 id="mainmodule"><code>mainModule <span class="nb-type">string</span></code></h4>
<p>The name of the Worker's main module. This must be one of the modules listed in <code>modules</code>.</p>
<h4 id="modules"><code>modules <span class="nb-type">Record&lt;string, string | Module&gt;</span></code></h4>
<p>A dictionary object mapping module names to their string contents. If the module content is a plain string, then the module name must have a file extension indicating its type: either <code>.js</code> or <code>.py</code>.</p>
<p>A module's content can also be specified as an object, in order to specify its type independent from the name. The allowed objects are:</p>
<ul>
<li><code>{js: string}</code>: A JavaScript module, using ES modules syntax for imports and exports.</li>
<li><code>{cjs: string}</code>: A CommonJS module, using <code>require()</code> syntax for imports.</li>
<li><code>{py: string}</code>: A <a href="/workers/languages/python/">Python module</a>, but see the warning below.</li>
<li><code>{text: string}</code>: An importable string value.</li>
<li><code>{data: ArrayBuffer}</code>: An importable <code>ArrayBuffer</code> value.</li>
<li><code>{json: object}</code>: An importable object. The value must be JSON-serializable. However, note that value is provided as a parsed object, and is delivered as a parsed object; neither side actually sees the JSON serialization.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/17179.md")
</aside>
<h4 id="globaloutbound-optional"><code>globalOutbound <span class="nb-type">ServiceStub | null</span> Optional</code></h4>
<p>Controls whether the dynamic Worker has access to the network. The global <code>fetch()</code> and <code>connect()</code> functions (for making HTTP requests and TCP connections, respectively) can be blocked or redirected to isolate the Worker.</p>
<p>If <code>globalOutbound</code> is not specified, the default is to inherit the parent's network access, which usually means the dynamic Worker will have full access to the public Internet.</p>
<p>If <code>globalOutbound</code> is <code>null</code>, then the dynamic Worker will be totally cut off from the network. Both <code>fetch()</code> and <code>connect()</code> will throw exceptions.</p>
<p><code>globalOutbound</code> can also be set to any service binding, including service bindings in the parent worker's <code>env</code> as well as <a href="/workers/runtime-apis/context/#exports">loopback bindings from <code>ctx.exports</code></a>.</p>
<p>Using <code>ctx.exports</code> is particularly useful as it allows you to customize the binding further for the specific sandbox, by setting the value of <code>ctx.props</code> that should be passed back to it. The <code>props</code> can contain information to identify the specific dynamic Worker that made the request.</p>
<p>For example:</p>
<pre><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Greeter extends WorkerEntrypoint {&#10;	fetch(request) {&#10;		return new Response(`Hello, ${this.ctx.props.name}!`);&#10;	}&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		let worker = env.LOADER.get(&quot;alice&quot;, () =&gt; {&#10;			return {&#10;				// Redirect the worker&#x27;s global outbound to send all requests&#10;				// to the `Greeter` class, filling in `ctx.props.name` with&#10;				// the name &quot;Alice&quot;, so that it always responds &quot;Hello, Alice!&quot;.&#10;				globalOutbound: ctx.exports.Greeter({ props: { name: &quot;Alice&quot; } }),&#10;&#10;				// ... code ...&#10;			};&#10;		});&#10;&#10;		return worker.getEntrypoint().fetch(request);&#10;	},&#10;};&#10;</code></pre>
<h4 id="env"><code>env <span class="nb-type">object</span></code></h4>
<p>The environment object to provide to the dynamic Worker.</p>
<p>Using this, you can provide custom bindings to the Worker.</p>
<p><code>env</code> is serialized and transferred into the dynamic Worker, where it is used directly as the value of <code>env</code> there. It may contain:</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm">Structured cloneable types</a>.</li>
<li><a href="/workers/runtime-apis/bindings/service-bindings">Service Bindings</a>, including <a href="/workers/runtime-apis/context/#exports">loopback bindings from <code>ctx.exports</code></a>.</li>
</ul>
<p>The second point is the key to creating custom bindings: you can define a binding with any arbitrary API, by defining a <a href="/workers/runtime-apis/bindings/service-bindings/rpc"><code>WorkerEntrypoint</code> class</a> implementing an RPC API, and then giving it to the dynamic Worker as a Service Binding.</p>
<p>Moreover, by using <code>ctx.exports</code> loopback bindings, you can further customize the bindings for the specific dynamic Worker by setting <code>ctx.props</code>, just as described for <code>globalOutbound</code>, above.</p>
<pre><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;// Implement a binding which can be called by the dynamic Worker.&#10;export class Greeter extends WorkerEntrypoint {&#10;	greet() {&#10;		return `Hello, ${this.ctx.props.name}!`;&#10;	}&#10;}&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		let worker = env.LOADER.get(&quot;alice&quot;, () =&gt; {&#10;			return {&#10;				env: {&#10;					// Provide a binding which has a method greet() which can be called&#10;					// to receive a greeting. The binding knows the Worker&#x27;s name.&#10;					GREETER: ctx.exports.Greeter({ props: { name: &quot;Alice&quot; } }),&#10;				},&#10;&#10;				// ... code ...&#10;			};&#10;		});&#10;&#10;		return worker.getEntrypoint().fetch(request);&#10;	},&#10;};&#10;</code></pre>
<h4 id="tails-optional"><code>tails <span class="nb-type">ServiceStub[]</span> Optional</code></h4>
<p>You may specify one or more <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> which will observe console logs, errors, and other details about the dynamically-loaded worker's execution. A tail event will be delivered to the Tail Worker upon completion of a request to the dynamically-loaded Worker. As always, you can implement the Tail Worker as an alternative entrypoint in your parent Worker, referring to it using <code>ctx.exports</code>:</p>
<pre><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		let worker = env.LOADER.get(&quot;alice&quot;, () =&gt; {&#10;			return {&#10;				// Send logs, errors, etc. to `LogTailer`. We pass `name` in the&#10;				// `ctx.props` so that `LogTailer` knows what generated the logs.&#10;				// (You can pass anything you want in `props`.)&#10;				tails: [ctx.exports.LogTailer({ props: { name: &quot;alice&quot; } })],&#10;&#10;				// ... code ...&#10;			};&#10;		});&#10;&#10;		return worker.getEntrypoint().fetch(request);&#10;	},&#10;};&#10;&#10;export class LogTailer extends WorkerEntrypoint {&#10;	async tail(events) {&#10;		let name = this.ctx.props.name;&#10;&#10;		// Send the logs off to our log endpoint, specifying the worker name in&#10;		// the URL.&#10;		//&#10;		// Note that `events` will always be an array of size 1 in this scenario,&#10;		// describing the event delivered to the dynamically-loaded Worker.&#10;		await fetch(`https://example.com/submit-logs/${name}`, {&#10;			method: &quot;POST&quot;,&#10;			body: JSON.stringify(events),&#10;		});&#10;	}&#10;}&#10;</code></pre>
