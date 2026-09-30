<p>This example shows how to use Workers VPC to create a centralized gateway that routes requests based on URL paths, provides authentication and rate limiting, and load balances across internal services.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Multiple private APIs or services running in your VPC/virtual network (we'll use a user service and orders service)</li>
<li>Cloudflare Tunnel configured and running (follow the <a href="/workers-vpc/get-started/#2-set-up-cloudflare-tunnel">Get Started guide</a> to set up or <a href="https://dash.cloudflare.com/?to=/:account/workers/vpc/tunnels">create a tunnel from the dashboard</a>)</li>
<li>Workers account with Workers VPC access</li>
</ul>
<h2 id="1-create-the-vpc-services"><ol>
<li>Create the VPC Services</li>
</ol></h2>
<p>First, create services for your internal APIs using hostnames:</p>
<pre><code class="language-bash">&#35; Create user service&#10;npx wrangler vpc service create user-service \&#10;  &#45;-type http \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-hostname user-api.internal.example.com&#10;&#10;&#35; Create orders service&#10;npx wrangler vpc service create order-service \&#10;  &#45;-type http \&#10;  &#45;-tunnel-id &lt;YOUR_TUNNEL_ID&gt; \&#10;  &#45;-hostname orders-api.internal.example.com&#10;</code></pre>
<p>Note the service IDs returned for the next step.</p>
<h2 id="2-configure-your-worker"><ol start="2">
<li>Configure your Worker</li>
</ol></h2>
<p>Update your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15874.md")
</div>
<h2 id="3-implement-the-worker"><ol start="3">
<li>Implement the Worker</li>
</ol></h2>
<p>In your Workers code, use the VPC Service bindings to route requests to the appropriate services:</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		const url = new URL(request.url);&#10;&#10;		// Route to internal services&#10;		if (url.pathname.startsWith(&#x27;/api/users&#x27;)) {&#10;			const response = await env.USER_SERVICE.fetch(&quot;https://user-api.internal.example.com&quot; + url.pathname);&#10;			return response;&#10;		} else if (url.pathname.startsWith(&#x27;/api/orders&#x27;)) {&#10;			const response = await env.ORDER_SERVICE.fetch(&quot;https://orders-api.internal.example.com&quot; + url.pathname);&#10;			return response;&#10;		}&#10;&#10;		return new Response(&#x27;Not Found&#x27;, { status: 404 });&#10;	},&#10;};&#10;</code></pre>
<h2 id="4-deploy-and-test"><ol start="4">
<li>Deploy and test</li>
</ol></h2>
<p>Now, you can deploy and test your Worker:</p>
<pre><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<pre><code class="language-bash">&#35; Test user service requests&#10;curl https://api-gateway.workers.dev/api/users&#10;&#10;&#35; Test orders service requests&#10;curl https://api-gateway.workers.dev/api/orders&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Add <a href="/workers/examples/auth-with-headers/">authentication and authorization</a></li>
<li>Implement <a href="/durable-objects/api/">rate limiting</a></li>
<li>Set up <a href="/analytics/analytics-engine/">monitoring and alerting</a></li>
<li>Explore <a href="/workers-vpc/examples/">other examples</a></li>
</ul>
