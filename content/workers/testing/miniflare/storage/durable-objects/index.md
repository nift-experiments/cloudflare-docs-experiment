<ul>
<li><a href="/durable-objects/api/">Durable Objects Reference</a></li>
<li><a href="/durable-objects/">Using Durable Objects</a></li>
</ul>
<h2 id="objects">Objects</h2>
<p>Specify Durable Objects to add to your environment as follows:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	modules: true,&#10;	script: `&#10;  export class Object1 {&#10;    async fetch(request) {&#10;      ...&#10;    }&#10;  }&#10;  export default {&#10;    fetch(request) {&#10;      ...&#10;    }&#10;  }&#10;  `,&#10;	durableObjects: {&#10;		// Note Object1 is exported from main (string) script&#10;		OBJECT1: &quot;Object1&quot;,&#10;	},&#10;});&#10;</code></pre>
<h2 id="persistence">Persistence</h2>
<p>By default, Durable Object data is stored in memory. It will persist between
reloads, but not different <code>Miniflare</code> instances. To enable persistence to the
file system, specify the Durable Object persistence option:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	durableObjectsPersist: true, // Defaults to ./.mf/do&#10;	durableObjectsPersist: &quot;./data&quot;, // Custom path&#10;});&#10;</code></pre>
<h2 id="manipulating-outside-workers">Manipulating Outside Workers</h2>
<p>For testing, it can be useful to make requests to your Durable Objects from
outside a worker. You can do this with the <code>getDurableObjectNamespace</code> method.</p>
<pre><code class="language-js">import { Miniflare } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	durableObjects: { TEST_OBJECT: &quot;TestObject&quot; },&#10;	script: `&#10;  export class TestObject {&#10;    constructor(state) {&#10;      this.storage = state.storage;&#10;    }&#10;&#10;    async fetch(request) {&#10;      const url = new URL(request.url);&#10;      if (url.pathname === &quot;/put&quot;) await this.storage.put(&quot;key&quot;, 1);&#10;      return new Response((await this.storage.get(&quot;key&quot;)).toString());&#10;    }&#10;  }&#10;&#10;  export default {&#10;    async fetch(request, env) {&#10;      const stub = env.TEST_OBJECT.getByName(&quot;test&quot;);&#10;      return stub.fetch(request);&#10;    }&#10;  }&#10;  `,&#10;});&#10;&#10;const ns = await mf.getDurableObjectNamespace(&quot;TEST_OBJECT&quot;);&#10;const stub = ns.getByName(&quot;test&quot;);&#10;const doRes = await stub.fetch(&quot;http://localhost:8787/put&quot;);&#10;console.log(await doRes.text()); // &quot;1&quot;&#10;&#10;const res = await mf.dispatchFetch(&quot;http://localhost:8787/&quot;);&#10;console.log(await res.text()); // &quot;1&quot;&#10;</code></pre>
<h2 id="using-a-class-exported-by-another-script">Using a Class Exported by Another Script</h2>
<p>Miniflare supports the <code>script_name</code> option for accessing Durable Objects
exported by other scripts. This requires mounting the other worker as described
in <a href="/workers/testing/miniflare/core/multiple-workers">🔌 Multiple Workers</a>.</p>
