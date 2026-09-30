<ul>
<li><a href="/workers/reference/migrate-to-module-workers/">Modules Reference</a></li>
</ul>
<h2 id="enabling-modules">Enabling Modules</h2>
<p>Miniflare supports both the traditional <code>service-worker</code> and the newer <code>modules</code> formats for writing workers. To use the <code>modules</code> format, enable it with:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	modules: true,&#10;});&#10;</code></pre>
<p>You can then use <code>modules</code> worker scripts like the following:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// - `request` is the incoming `Request` instance&#10;		// - `env` contains bindings, KV namespaces, Durable Objects, etc&#10;		// - `ctx` contains `waitUntil` and `passThroughOnException` methods&#10;		return new Response(&quot;Hello Miniflare!&quot;);&#10;	},&#10;	async scheduled(controller, env, ctx) {&#10;		// - `controller` contains `scheduledTime` and `cron` properties&#10;		// - `env` contains bindings, KV namespaces, Durable Objects, etc&#10;		// - `ctx` contains the `waitUntil` method&#10;		console.log(&quot;Doing something scheduled...&quot;);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside warning">
@markup("md", "content/.markup/bodies/17366.md")
</aside>
<h2 id="module-rules">Module Rules</h2>
<p>Miniflare supports all module types: <code>ESModule</code>, <code>CommonJS</code>, <code>Text</code>, <code>Data</code> and
<code>CompiledWasm</code>. You can specify additional module resolution rules as follows:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	modulesRules: [&#10;		{ type: &quot;ESModule&quot;, include: [&quot;**/*.js&quot;], fallthrough: true },&#10;		{ type: &quot;Text&quot;, include: [&quot;**/*.txt&quot;] },&#10;	],&#10;});&#10;</code></pre>
<h3 id="default-rules">Default Rules</h3>
<p>The following rules are automatically added to the end of your modules rules
list. You can override them by specifying rules matching the same <code>globs</code>:</p>
<pre><code class="language-js">[&#10;	{ type: &quot;ESModule&quot;, include: [&quot;**/*.mjs&quot;] },&#10;	{ type: &quot;CommonJS&quot;, include: [&quot;**/*.js&quot;, &quot;**/*.cjs&quot;] },&#10;];&#10;</code></pre>
