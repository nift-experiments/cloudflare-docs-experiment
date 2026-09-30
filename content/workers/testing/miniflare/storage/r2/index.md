<ul>
<li><a href="/r2/api/workers/workers-api-reference/">R2 Reference</a></li>
</ul>
<h2 id="buckets">Buckets</h2>
<p>Specify R2 Buckets to add to your environment as follows:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	r2Buckets: [&quot;BUCKET1&quot;, &quot;BUCKET2&quot;],&#10;});&#10;</code></pre>
<h2 id="manipulating-outside-workers">Manipulating Outside Workers</h2>
<p>For testing, it can be useful to put/get data from R2 storage
outside a worker. You can do this with the <code>getR2Bucket</code> method:</p>
<pre><code class="language-js">import { Miniflare } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	script: `&#10;  export default {&#10;    async fetch(request, env, ctx) {&#10;      const object = await env.BUCKET.get(&quot;count&quot;);&#10;      const value = parseInt(await object.text()) + 1;&#10;      await env.BUCKET.put(&quot;count&quot;, value.toString());&#10;      return new Response(value.toString());&#10;    }&#10;  }&#10;  `,&#10;	r2Buckets: [&quot;BUCKET&quot;],&#10;});&#10;&#10;const bucket = await mf.getR2Bucket(&quot;BUCKET&quot;);&#10;await bucket.put(&quot;count&quot;, &quot;1&quot;);&#10;&#10;const res = await mf.dispatchFetch(&quot;http://localhost:8787/&quot;);&#10;console.log(await res.text()); // 2&#10;console.log(await (await bucket.get(&quot;count&quot;)).text()); // 2&#10;</code></pre>
