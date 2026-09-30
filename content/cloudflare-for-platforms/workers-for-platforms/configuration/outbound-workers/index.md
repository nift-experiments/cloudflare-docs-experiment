<p>Outbound Workers sit between your customer's Workers and the public Internet. They give you visibility into all outgoing <code>fetch()</code> requests from user Workers.</p>
<p><img src="/assets/upstream/images/cloudflare-for-platforms/outbound-worker-diagram.png" alt="Outbound Workers diagram information" /></p>
<h2 id="general-use-cases">General Use Cases</h2>
<p>Outbound Workers can be used to:</p>
<ul>
<li>Log all subrequests to identify malicious domains or usage patterns.</li>
<li>Create, allow, or block lists for hostnames requested by user Workers.</li>
<li>Configure authentication to your APIs behind the scenes (without end developers needing to set credentials).</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4218.md")
</aside>
<h2 id="use-outbound-workers">Use Outbound Workers</h2>
<p>To use Outbound Workers:</p>
<ol>
<li>Create a Worker intended to serve as your Outbound Worker.</li>
<li>Outbound Worker can be specified as an optional parameter in the <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">dispatch namespaces</a> binding in a project's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. Optionally, to pass data from your dynamic dispatch Worker to the Outbound Worker, the variable names can be specified under <strong>parameters</strong>.</li>
</ol>
<p>Make sure that you have <code>wrangler@3.3.0</code> or later <a href="/workers/wrangler/install-and-update/">installed</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/4219.md")
</div>
<ol start="3">
<li>Edit your dynamic dispatch Worker to call the Outbound Worker and declare variables to pass on <code>dispatcher.get()</code>.</li>
</ol>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		try {&#10;			// parse the URL, read the subdomain&#10;			let workerName = new URL(request.url).host.split(&quot;.&quot;)[0];&#10;&#10;			let context_from_dispatcher = {&#10;				customer_name: workerName,&#10;				url: request.url,&#10;			};&#10;&#10;			let userWorker = env.dispatcher.get(&#10;				workerName,&#10;				{},&#10;				{&#10;					// outbound arguments. object name must match parameters in the binding&#10;					outbound: {&#10;						params_object: context_from_dispatcher,&#10;					},&#10;				},&#10;			);&#10;			return await userWorker.fetch(request);&#10;		} catch (e) {&#10;			if (e.message.startsWith(&quot;Worker not found&quot;)) {&#10;				// we tried to get a worker that doesn&#x27;t exist in our dispatch namespace&#10;				return new Response(&quot;&quot;, { status: 404 });&#10;			}&#10;			return new Response(e.message, { status: 500 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<ol start="4">
<li>The Outbound Worker will now be invoked on any <code>fetch()</code> requests from a user Worker. The user Worker will trigger a <a href="/workers/runtime-apis/handlers/fetch/">FetchEvent</a> on the Outbound Worker. The variables declared in the binding can be accessed in the Outbound Worker through <code>env.&lt;VAR_NAME&gt;</code>.</li>
</ol>
<p>The following is an example of an Outbound Worker that logs the fetch request from user Worker and creates a JWT if the fetch request matches <code>api.example.com</code>.</p>
<pre><code class="language-js">export default {&#10;	// this event is fired when the dispatched Workers make a subrequest&#10;	async fetch(request, env, ctx) {&#10;		// env contains the values we set in `dispatcher.get()`&#10;		const customer_name = env.customer_name;&#10;		const original_url = env.url;&#10;&#10;		// log the request&#10;		ctx.waitUntil(&#10;			fetch(&quot;https://logs.example.com&quot;, {&#10;				method: &quot;POST&quot;,&#10;				body: JSON.stringify({&#10;					customer_name,&#10;					original_url,&#10;				}),&#10;			}),&#10;		);&#10;&#10;		const url = new URL(original_url);&#10;		if (url.host === &quot;api.example.com&quot;) {&#10;			// pre-auth requests to our API&#10;			const jwt = make_jwt_for_customer(customer_name);&#10;&#10;			let headers = new Headers(request.headers);&#10;			headers.set(&quot;Authorization&quot;, `Bearer ${jwt}`);&#10;&#10;			// clone the request to set new headers using existing body&#10;			let new_request = new Request(request, { headers });&#10;&#10;			return fetch(new_request);&#10;		}&#10;&#10;		return fetch(request);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4217.md")
</aside>
