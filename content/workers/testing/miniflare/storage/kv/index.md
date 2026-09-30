<ul>
<li><a href="/kv/api/">KV Reference</a></li>
</ul>
<h2 id="namespaces">Namespaces</h2>
<p>Specify KV namespaces to add to your environment as follows:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	kvNamespaces: [&quot;TEST_NAMESPACE1&quot;, &quot;TEST_NAMESPACE2&quot;],&#10;});&#10;</code></pre>
<p>You can now access KV namespaces in your workers:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		return new Response(await env.TEST_NAMESPACE1.get(&quot;key&quot;));&#10;	},&#10;};&#10;</code></pre>
<p>Miniflare supports all KV operations and data types.</p>
<h2 id="manipulating-outside-workers">Manipulating Outside Workers</h2>
<p>For testing, it can be useful to put/get data from KV outside a worker. You can
do this with the <code>getKVNamespace</code> method:</p>
<pre><code class="language-js">import { Miniflare } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	script: `&#10;  export default {&#10;    async fetch(request, env, ctx) {&#10;      const value = parseInt(await env.TEST_NAMESPACE.get(&quot;count&quot;)) + 1;&#10;      await env.TEST_NAMESPACE.put(&quot;count&quot;, value.toString());&#10;      return new Response(value.toString());&#10;    },&#10;  }&#10;  `,&#10;	kvNamespaces: [&quot;TEST_NAMESPACE&quot;],&#10;});&#10;&#10;const ns = await mf.getKVNamespace(&quot;TEST_NAMESPACE&quot;);&#10;await ns.put(&quot;count&quot;, &quot;1&quot;);&#10;&#10;const res = await mf.dispatchFetch(&quot;http://localhost:8787/&quot;);&#10;console.log(await res.text()); // 2&#10;console.log(await ns.get(&quot;count&quot;)); // 2&#10;</code></pre>
