<p class="article-summary">Publish to a queue from within a Durable Object.</p>
<p>The following example shows you how to write a Worker script to publish to <a href="/queues/">Cloudflare Queues</a> from within a <a href="/durable-objects/">Durable Object</a>.</p>
<p>Prerequisites:</p>
<ul>
<li>A <a href="/queues/get-started/#3-create-a-queue">queue created</a> via the Cloudflare dashboard or the <a href="/workers/wrangler/install-and-update/">wrangler CLI</a>.</li>
<li>A <a href="/queues/configuration/configure-queues/#producer-worker-configuration">configured <strong>producer</strong> binding</a> in the Cloudflare dashboard or Wrangler file.</li>
<li>A <a href="/workers/wrangler/configuration/#durable-objects">Durable Object namespace binding</a>.</li>
</ul>
<p>Configure your Wrangler file as follows:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11243.md")
</div>
<p>The following Worker script:</p>
<ol>
<li>Creates a Durable Object stub, or retrieves an existing one based on a userId.</li>
<li>Passes request data to the Durable Object.</li>
<li>Publishes to a queue from within the Durable Object.</li>
</ol>
<p>Extending the <code>DurableObject</code> base class makes your <code>Env</code> available on <code>this.env</code> and the Durable Object state available on <code>this.ctx</code> within the <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/"><code>fetch()</code> handler</a> in the Durable Object.</p>
<pre><code class="language-ts">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;interface Env {&#10;  YOUR_QUEUE: Queue;&#10;  YOUR_DO_CLASS: DurableObjectNamespace&lt;YourDurableObject&gt;;&#10;}&#10;&#10;export default {&#10;  async fetch(req, env, ctx): Promise&lt;Response&gt; {&#10;    // Assume each Durable Object is mapped to a userId in a query parameter&#10;    // In a production application, this will be a userId defined by your application&#10;    // that you validate (and/or authenticate) first.&#10;    const url = new URL(req.url);&#10;    const userIdParam = url.searchParams.get(&quot;userId&quot;);&#10;&#10;    if (userIdParam) {&#10;      // Get a stub that allows you to call that Durable Object&#10;      const durableObjectStub = env.YOUR_DO_CLASS.getByName(userIdParam);&#10;&#10;      // Pass the request to that Durable Object and await the response&#10;      // This invokes the constructor once on your Durable Object class (defined further down)&#10;      // on the first initialization, and the fetch method on each request.&#10;      // We pass the original Request to the Durable Object&#x27;s fetch method&#10;      const response = await durableObjectStub.fetch(req);&#10;&#10;      // This would return &quot;wrote to queue&quot;, but you could return any response.&#10;      return response;&#10;    }&#10;    return new Response(&quot;userId must be provided&quot;, { status: 400 });&#10;  },&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;&#10;export class YourDurableObject extends DurableObject&lt;Env&gt; {&#10;  async fetch(req: Request): Promise&lt;Response&gt; {&#10;    // Error handling elided for brevity.&#10;    // Publish to your queue&#10;    await this.env.YOUR_QUEUE.send({&#10;      id: this.ctx.id.toString(), // Write the ID of the Durable Object to your queue&#10;      // Write any other properties to your queue&#10;    });&#10;&#10;    return new Response(&quot;wrote to queue&quot;);&#10;  }&#10;}&#10;</code></pre>
