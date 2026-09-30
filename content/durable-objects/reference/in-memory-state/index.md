<p>In-memory state means that each <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/8095.md")
</div> has one active instance at any particular time. All requests sent to that Durable Object are handled by that same instance. You can store some state in memory.
<p>Variables in a Durable Object will maintain state as long as your Durable Object is not evicted from memory.</p>
<p>A common pattern is to initialize a Durable Object from <a href="/durable-objects/api/sqlite-storage-api/">persistent storage</a> and set instance variables the first time it is accessed. Since future accesses are routed to the same Durable Object, it is then possible to return any initialized values without making further calls to persistent storage.</p>
<pre><code class="language-js">import { DurableObject } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Counter extends DurableObject {&#10;  constructor(ctx, env) {&#10;    super(ctx, env);&#10;    // `blockConcurrencyWhile()` ensures no requests are delivered until&#10;    // initialization completes.&#10;    this.ctx.blockConcurrencyWhile(async () =&gt; {&#10;      let stored = await this.ctx.storage.get(&quot;value&quot;);&#10;      // After initialization, future reads do not need to access storage.&#10;      this.value = stored || 0;&#10;    });&#10;  }&#10;&#10;  // Handle HTTP requests from clients.&#10;  async fetch(request) {&#10;    // use this.value rather than storage&#10;  }&#10;}&#10;</code></pre>
<p>A given instance of a Durable Object may share global memory with other instances defined in the same Worker code.</p>
<p>In the example above, using a global variable <code>value</code> instead of the instance variable <code>this.value</code> would be incorrect. Two different instances of <code>Counter</code> will each have their own separate memory for <code>this.value</code>, but might share memory for the global variable <code>value</code>, leading to unexpected results. Because of this, it is best to avoid global variables.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="built-in-caching">Built-in caching</h3>
@markup("md", "content/.markup/bodies/8094.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="observe-in-memory-state-size">Observe in-memory state size</h3>
@markup("md", "content/.markup/bodies/8093.md")
</aside>
