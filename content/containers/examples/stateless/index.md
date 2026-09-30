<p class="article-summary">Run multiple instances across Cloudflare&#x27;s network</p>
<p>To simply proxy requests to one of multiple instances of a container, you can use the <code>getRandom</code> function:</p>
<pre><code class="language-ts">import { Container, getRandom } from &quot;@cloudflare/containers&quot;;&#10;&#10;const INSTANCE_COUNT = 3;&#10;&#10;class Backend extends Container {&#10;	defaultPort = 8080;&#10;	sleepAfter = &quot;2h&quot;;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const containerInstance = await getRandom(env.BACKEND, INSTANCE_COUNT);&#10;		return containerInstance.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7138.md")
</aside>
