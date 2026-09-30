<p>Worker A that declares a Service binding to Worker B can forward a <a href="/workers/runtime-apis/request/"><code>Request</code></a> object to Worker B, by calling the <code>fetch()</code> method that is exposed on the binding object.</p>
<p>For example, consider the following Worker that implements a <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17267.md")
</div>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    return new Response(&quot;Hello World!&quot;);&#10;  }&#10;}&#10;</code></pre>
<p>The following Worker declares a binding to the Worker above:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17268.md")
</div>
<p>And then can forward a request to it:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		return await env.WORKER_B.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17266.md")
</aside>
