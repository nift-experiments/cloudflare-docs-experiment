<h2 id="scale-container-instances-with-explicit-ids">Scale container instances with explicit IDs</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7150.md")
</aside>
<p>Today, Containers are scaled manually by getting containers with a unique ID, then
starting the container. Note that getting a container does not automatically start it.</p>
<pre><code class="language-typescript">// get and start two container instances&#10;const containerOne = getContainer(&#10;	env.MY_CONTAINER,&#10;	idOne,&#10;).startAndWaitForPorts();&#10;&#10;const containerTwo = getContainer(&#10;	env.MY_CONTAINER,&#10;	idTwo,&#10;).startAndWaitForPorts();&#10;</code></pre>
<p>Each instance will run until its <code>sleepAfter</code> time has elapsed, or until it is manually stopped.</p>
<p>This behavior is very useful when you want explicit control over the lifecycle of container instances.
For instance, you may want to spin up a container backend instance for a specific user, or you may briefly
run a code sandbox to isolate AI-generated code, or you may want to run a short-lived batch job.</p>
<h3 id="use-the-getrandom-helper-function">Use the <code>getRandom</code> helper function</h3>
<p>If you want to run multiple instances of a container and route requests between them, use the
<code>getRandom</code> helper function:</p>
<pre><code class="language-javascript">import { Container, getRandom } from &quot;@cloudflare/containers&quot;;&#10;&#10;const INSTANCE_COUNT = 3;&#10;&#10;class Backend extends Container {&#10;	defaultPort = 8080;&#10;	sleepAfter = &quot;2h&quot;;&#10;}&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const containerInstance = await getRandom(env.BACKEND, INSTANCE_COUNT);&#10;		return containerInstance.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>Use <code>getRandom</code> to route to multiple stateless container instances. It randomly selects one of N
instances for each request, which means:</p>
<ul>
<li>It requires that the user set a fixed number of instances to route to.</li>
<li>It will randomly select each instance, regardless of location.</li>
</ul>
<p>We plan to fix these issues with built-in autoscaling and routing features in the near future.</p>
