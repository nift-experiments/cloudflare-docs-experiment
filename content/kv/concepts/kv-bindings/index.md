<p>KV <a href="/workers/runtime-apis/bindings/">bindings</a> allow for communication between a Worker and a KV namespace.</p>
<p>Configure KV bindings in the <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<h2 id="access-kv-from-workers">Access KV from Workers</h2>
<p>A <a href="/kv/concepts/kv-namespaces/">KV namespace</a> is a key-value database replicated to Cloudflare's global network.</p>
<p>To connect to a KV namespace from within a Worker, you must define a binding that points to the namespace's ID.</p>
<p>The name of your binding does not need to match the KV namespace's name. Instead, the binding should be a valid JavaScript identifier, because the identifier will exist as a global variable within your Worker.</p>
<p>A KV namespace will have a name you choose (for example, <code>My tasks</code>), and an assigned ID (for example, <code>06779da6940b431db6e566b4846d64db</code>).</p>
<p>To execute your Worker, define the binding.</p>
<p>In the following example, the binding is called <code>TODO</code>. In the <code>kv_namespaces</code> portion of your Wrangler configuration file, add:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9525.md")
</div>
<p>With this, the deployed Worker will have a <code>TODO</code> field in their environment object (the second parameter of the <code>fetch()</code> request handler). Any methods on the <code>TODO</code> binding will map to the KV namespace with an ID of <code>06779da6940b431db6e566b4846d64db</code> – which you called <code>My Tasks</code> earlier.</p>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    // Get the value for the &quot;to-do:123&quot; key&#10;    // NOTE: Relies on the `TODO` KV binding that maps to the &quot;My Tasks&quot; namespace.&#10;    let value = await env.TODO.get(&quot;to-do:123&quot;);&#10;&#10;    // Return the value, as is, for the Response&#10;    return new Response(value);&#10;  },&#10;};&#10;</code></pre>
<h2 id="use-kv-bindings-when-developing-locally">Use KV bindings when developing locally</h2>
<p>When you use Wrangler to develop locally with the <code>wrangler dev</code> command, Wrangler will default to using a local version of KV to avoid interfering with any of your live production data in KV. This means that reading keys that you have not written locally will return <code>null</code>.</p>
<p>To have <code>wrangler dev</code> connect to your Workers KV namespace running on Cloudflare's global network, set <code>&quot;remote&quot; : true</code> in the KV binding configuration. Refer to the <a href="/workers/local-development/#remote-bindings">remote bindings documentation</a> for more information.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/9526.md")
</div>
<h2 id="access-kv-from-durable-objects-and-workers-using-es-modules-format">Access KV from Durable Objects and Workers using ES modules format</h2>
<p><a href="/durable-objects/">Durable Objects</a> use ES modules format. Instead of a global variable, bindings are available as properties of the <code>env</code> parameter <a href="/durable-objects/get-started/#2-write-a-durable-object-class">passed to the constructor</a>.</p>
<p>An example might look like:</p>
<pre><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class MyDurableObject extends DurableObject {&#10;  constructor(ctx, env) {&#10;    super(ctx, env);&#10;  }&#10;&#10;  async fetch(request) {&#10;    const valueFromKV = await this.env.NAMESPACE.get(&quot;someKey&quot;);&#10;    return new Response(valueFromKV);&#10;  }&#10;}&#10;</code></pre>
