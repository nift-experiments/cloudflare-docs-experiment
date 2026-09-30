<p class="article-summary">A simple frontend app with a containerized backend</p>
<p>A common pattern is to serve a static frontend application (e.g., React, Vue, Svelte) using Static Assets,
then pass backend requests to a containerized backend application.</p>
<p>In this example, we'll show an example using a simple <code>index.html</code> file served as a static asset,
but you can select from one of many frontend frameworks. See our <a href="/workers/framework-guides/web-apps/">Workers framework examples</a> for more information.</p>
<p>For a full example, see the <a href="https://github.com/mikenomitch/static-frontend-container-backend">Static Frontend + Container Backend Template</a>.</p>
<h2 id="configure-static-assets-and-a-container">Configure Static Assets and a Container</h2>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7146.md")
</div>
<h2 id="add-a-simple-index-html-file-to-serve">Add a simple index.html file to serve</h2>
<p>Create a simple <code>index.html</code> file in the <code>./dist</code> directory.</p>
<details class="nb-details"><summary>index.html</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7147.md")
</div></details>
<p>In this example, we are using <a href="https://alpinejs.dev/">Alpine.js</a> to fetch a list of widgets from <code>/api/widgets</code>.</p>
<p>This is meant to be a very simple example, but you can get significantly more complex.
See <a href="/workers/framework-guides/web-apps/">examples of Workers integrating with frontend frameworks</a> for more information.</p>
<h2 id="define-a-worker">Define a Worker</h2>
<p>Your Worker needs to be able to both serve static assets and route requests to the containerized backend.</p>
<p>In this case, we will pass requests to one of three container instances if the route starts with <code>/api</code>,
and all other requests will be served as static assets.</p>
<pre><code class="language-javascript">import { Container, getRandom } from &quot;@cloudflare/containers&quot;;&#10;&#10;const INSTANCE_COUNT = 3;&#10;&#10;class Backend extends Container {&#10;	defaultPort = 8080; // pass requests to port 8080 in the container&#10;	sleepAfter = &quot;2h&quot;; // only sleep a container if it hasn&#x27;t gotten requests in 2 hours&#10;}&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		const url = new URL(request.url);&#10;		if (url.pathname.startsWith(&quot;/api&quot;)) {&#10;			const containerInstance = await getRandom(env.BACKEND, INSTANCE_COUNT);&#10;			return containerInstance.fetch(request);&#10;		}&#10;&#10;		return env.ASSETS.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7145.md")
</aside>
<h2 id="define-a-backend-container">Define a backend container</h2>
<p>Your container should be able to handle requests to <code>/api/widgets</code>.</p>
<p>In this case, we'll use a simple Golang backend that returns a hard-coded list of widgets.</p>
<details class="nb-details"><summary>server.go</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7148.md")
</div></details>
