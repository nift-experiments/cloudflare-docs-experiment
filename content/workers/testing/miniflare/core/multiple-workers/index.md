<p>Miniflare allows you to run multiple workers in the same instance. All Workers can be defined at the same level, using the <code>workers</code> option.</p>
<p>Here's an example that uses a service binding to increment a value in a shared KV namespace:</p>
<pre><code class="language-js">import { Miniflare, Response } from &quot;miniflare&quot;;&#10;&#10;const message = &quot;The count is &quot;;&#10;const mf = new Miniflare({&#10;	// Options shared between workers such as HTTP and persistence configuration&#10;	// should always be defined at the top level.&#10;	host: &quot;0.0.0.0&quot;,&#10;	port: 8787,&#10;	kvPersist: true,&#10;&#10;	workers: [&#10;		{&#10;			name: &quot;worker&quot;,&#10;			kvNamespaces: { COUNTS: &quot;counts&quot; },&#10;			serviceBindings: {&#10;				INCREMENTER: &quot;incrementer&quot;,&#10;				// Service bindings can also be defined as custom functions, with access&#10;				// to anything defined outside Miniflare.&#10;				async CUSTOM(request) {&#10;					// `request` is the incoming `Request` object.&#10;					return new Response(message);&#10;				},&#10;			},&#10;			modules: true,&#10;			script: `export default {&#10;        async fetch(request, env, ctx) {&#10;          // Get the message defined outside&#10;          const response = await env.CUSTOM.fetch(&quot;http://host/&quot;);&#10;          const message = await response.text();&#10;&#10;          // Increment the count 3 times&#10;          await env.INCREMENTER.fetch(&quot;http://host/&quot;);&#10;          await env.INCREMENTER.fetch(&quot;http://host/&quot;);&#10;          await env.INCREMENTER.fetch(&quot;http://host/&quot;);&#10;          const count = await env.COUNTS.get(&quot;count&quot;);&#10;&#10;          return new Response(message + count);&#10;        }&#10;      }`,&#10;		},&#10;		{&#10;			name: &quot;incrementer&quot;,&#10;			// Note we&#x27;re using the same `COUNTS` namespace as before, but binding it&#10;			// to `NUMBERS` instead.&#10;			kvNamespaces: { NUMBERS: &quot;counts&quot; },&#10;			// Worker formats can be mixed-and-matched&#10;			script: `addEventListener(&quot;fetch&quot;, (event) =&gt; {&#10;        event.respondWith(handleRequest());&#10;      })&#10;      async function handleRequest() {&#10;        const count = parseInt((await NUMBERS.get(&quot;count&quot;)) ?? &quot;0&quot;) + 1;&#10;        await NUMBERS.put(&quot;count&quot;, count.toString());&#10;        return new Response(count.toString());&#10;      }`,&#10;		},&#10;	],&#10;});&#10;const res = await mf.dispatchFetch(&quot;http://localhost&quot;);&#10;console.log(await res.text()); // &quot;The count is 3&quot;&#10;await mf.dispose();&#10;</code></pre>
<h2 id="routing">Routing</h2>
<p>You can enable routing by specifying <code>routes</code> via the API,
using the
<a href="/workers/configuration/routing/routes/#matching-behavior">standard route syntax</a>.
Note port numbers are ignored:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	workers: [&#10;		{&#10;			scriptPath: &quot;./api/worker.js&quot;,&#10;			routes: [&quot;http://127.0.0.1/api*&quot;, &quot;api.mf/*&quot;],&#10;		},&#10;	],&#10;});&#10;</code></pre>
<p>When using hostnames that aren't <code>localhost</code> or <code>127.0.0.1</code>, you
may need to edit your computer's <code>hosts</code> file, so those hostnames resolve to
<code>localhost</code>. On Linux and macOS, this is usually at <code>/etc/hosts</code>. On Windows,
it's at <code>C:\Windows\System32\drivers\etc\hosts</code>. For the routes above, we would
need to append the following entries to the file:</p>
<pre><code>127.0.0.1 miniflare.test&#10;127.0.0.1 api.mf&#10;</code></pre>
<p>Alternatively, you can customise the <code>Host</code> header when sending the request:</p>
<pre><code class="language-sh">&#35; Dispatches to the &quot;api&quot; worker&#10;$ curl &quot;http://localhost:8787/todos/update/1&quot; -H &quot;Host: api.mf&quot;&#10;</code></pre>
<p>When using the API, Miniflare will use the request's URL to determine which
Worker to dispatch to.</p>
<pre><code class="language-js">// Dispatches to the &quot;api&quot; worker&#10;const res = await mf.dispatchFetch(&quot;http://api.mf/todos/update/1&quot;, { ... });&#10;</code></pre>
<h2 id="durable-objects">Durable Objects</h2>
<p>Miniflare supports the <code>script_name</code> option for accessing Durable Objects
exported by other scripts. See
<a href="/workers/testing/miniflare/storage/durable-objects#using-a-class-exported-by-another-script">📌 Durable Objects</a>
for more details.</p>
