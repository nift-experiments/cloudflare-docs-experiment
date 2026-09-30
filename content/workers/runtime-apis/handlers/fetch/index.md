<h2 id="background">Background</h2>
<p>Incoming HTTP requests to a Worker are passed to the <code>fetch()</code> handler as a <a href="/workers/runtime-apis/request/"><code>Request</code></a> object. To respond to the request with a response, return a <a href="/workers/runtime-apis/response/"><code>Response</code></a> object:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		return new Response(&#x27;Hello World!&#x27;);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17178.md")
</aside>
<h3 id="parameters">Parameters</h3>
<ul>
<li>
<p><code>request</code> Request</p>
<ul>
<li>The incoming HTTP request.</li>
</ul>
</li>
<li>
<p><code>env</code> object</p>
<ul>
<li>The <a href="/workers/runtime-apis/bindings/">bindings</a> available to the Worker. As long as the <a href="/workers/wrangler/environments/">environment</a> has not changed, the same object (equal by identity) may be passed to multiple requests. You can also <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global">import <code>env</code> from <code>cloudflare:workers</code></a> to access bindings from anywhere in your code.</li>
</ul>
</li>
<li>
<p><code>ctx.waitUntil(promisePromise)</code> : void</p>
<ul>
<li>Refer to <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil</code></a>.</li>
</ul>
</li>
<li>
<p><code>ctx.passThroughOnException()</code> : void</p>
<ul>
<li>Refer to <a href="/workers/runtime-apis/context/#passthroughonexception"><code>passThroughOnException</code></a>.</li>
</ul>
</li>
</ul>
