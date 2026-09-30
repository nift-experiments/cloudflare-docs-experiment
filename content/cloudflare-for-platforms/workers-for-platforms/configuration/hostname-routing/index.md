<p>You can use <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">dynamic dispatch</a> Workers to route millions of vanity domains or subdomains to Workers without hitting traditional <a href="/workers/platform/limits/#routes-and-domains">route limits</a>. These hostnames can be subdomains under your managed domain (e.g. <code>customer1.saas.com</code>) or vanity domains controlled by your end customers (e.g. <code>mystore.com</code>), which can be managed through <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom hostnames</a>.</p>
<h2 id="recommended-wildcard-route-with-a-dispatch-worker">(Recommended) Wildcard route with a dispatch Worker</h2>
<p>Configure a wildcard <a href="/workers/configuration/routing/routes/">Route</a> (<code>*/*</code>) on your SaaS domain (the domain where you configure custom hostnames) to point to your dynamic dispatch Worker. This allows you to:</p>
<ul>
<li><strong>Support both subdomains and vanity domains</strong>: Handle <code>customer1.myplatform.com</code> (subdomain) and <code>shop.customer.com</code> (custom hostname) with the same routing logic.</li>
<li><strong>Avoid route limits</strong>: Instead of creating individual routes for every domain, which can cause you to hit <a href="/workers/platform/limits/#routes-and-domains">Routes limits</a>, you can handle the routing logic in code and proxy millions of domains to individual Workers.</li>
<li><strong>Programmatically control routing logic</strong>: Write custom code to route requests based on hostname, <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">custom metadata</a>, path, or any other properties.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4221.md")
</aside>
<p>If you'd like to exclude certain hostnames from routing to the dispatch Worker, you can either:</p>
<ul>
<li>Add routes without a Worker specification to opt certain hostnames or paths from being executed by the dispatcher Worker (for example, for <code>saas.com</code>, <code>api.saas.com</code>, etc)</li>
<li>Use a <a href="/dns/zone-setups/subdomain-setup/">dedicated domain</a> (for example, <code>customers.saas.com</code>) for custom hostname and dispatch worker management to keep the rest of the traffic for that domain separate.</li>
</ul>
<h3 id="setup">Setup</h3>
<p>To set up hostname routing with a wildcard route:</p>
<ol>
<li><strong>Configure custom hostnames</strong>: Set up your domain and custom hostnames using <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a></li>
<li><strong>Set the fallback origin</strong>: Set up a <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin">fallback origin server</a>, this is where all custom hostnames will be routed to. If you’d like to route them to separate origins, you can use a <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/">custom origin server</a>. Requests will route through the Worker before reaching the origin. If the Worker is the origin then place a dummy DNS record for the fallback origin (e.g., <code>A 192.0.2.0</code>).</li>
<li><strong>Configure DNS</strong>: Point DNS records (subdomains or custom hostname) via <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record">CNAME record to the saas domain</a>. If your customers need to proxy their apex hostname (e.g. <code>example.com</code>) and cannot use CNAME records, check out <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">Apex Proxying</a>.</li>
<li><strong>Create wildcard route</strong>: Add a <code>*/*</code> route on your platform domain (e.g. saas.com) and associate it with your dispatch Worker.</li>
<li><strong>Implement dispatch logic</strong>: Add logic to your dispatch Worker to route based on hostname, lookup mappings stored in <a href="/kv/">Workers KV</a>, or use <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">custom metadata</a> attached to custom hostnames.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4220.md")
</aside>
<h4 id="example-dispatch-worker">Example dispatch Worker</h4>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const hostname = new URL(request.url).hostname;&#10;&#10;		// Get custom hostname metadata for routing decisions&#10;		const hostnameData = await env.KV.get(`hostname:${hostname}`, {&#10;			type: &quot;json&quot;,&#10;		});&#10;&#10;		if (!hostnameData?.workerName) {&#10;			return new Response(&quot;Hostname not configured&quot;, { status: 404 });&#10;		}&#10;&#10;		// Route to the appropriate user Worker&#10;		const userWorker = env.DISPATCHER.get(hostnameData.workerName);&#10;		return await userWorker.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<h2 id="subdomain-routing">Subdomain routing</h2>
<p>If you're only looking to route subdomain records (e.g. <code>customer1.saas.com</code>), you can use a more specific route (<code>*.saas.com/*</code>) to route requests to your dispatch Worker.</p>
<h3 id="setup-1">Setup</h3>
<p>To set up subdomain routing:</p>
<ol>
<li>Create an orange-clouded wildcard DNS record: <code>*.saas.com</code> that points to the origin. If the Worker is the origin then you can use a dummy DNS value (for example, <code>A 192.0.2.0</code>).</li>
<li>Set wildcard route: <code>*.saas.com/*</code> pointing to your dispatch Worker</li>
<li>Add logic to the dispatch Worker to route subdomain requests to the right Worker.</li>
</ol>
<h4 id="example-subdomain-dispatch-worker">Example subdomain dispatch Worker</h4>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		const url = new URL(request.url);&#10;		const subdomain = url.hostname.split(&quot;.&quot;)[0];&#10;&#10;		// Route based on subdomain&#10;		if (subdomain &amp;&amp; subdomain !== &quot;saas&quot;) {&#10;			const userWorker = env.DISPATCHER.get(subdomain);&#10;			return await userWorker.fetch(request);&#10;		}&#10;&#10;		return new Response(&quot;Invalid subdomain&quot;, { status: 400 });&#10;	},&#10;};&#10;</code></pre>
<h3 id="o2o-behavior">O2O Behavior</h3>
<p>When your customers are also using Cloudflare and point their custom domain to your SaaS domain via CNAME (for example, <code>mystore.com</code> → <code>saas.com</code>), Worker routing behavior depends on whether the customer's DNS record is proxied (orange cloud) or DNS-only (grey cloud). Learn more about <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/#with-o2o">O2O setups</a></p>
<p>This can cause inconsistent behavior when using specific hostname routes:</p>
<ul>
<li>If you're routing based on the CNAME target (<code>saas.com</code>), the custom hostname's DNS record must be orange-clouded for the Worker to be invoked.</li>
<li>If you're routing based on the custom hostname (<code>mystore.com</code>), the customer's record must be grey-clouded for the Worker to be invoked.</li>
</ul>
<p>Since you may not have control over your customer's DNS proxy settings, we recommend using <code>*/*</code> wildcard route to ensure routing logic always works as expected, regardless of how DNS is configured.</p>
<h4 id="worker-invocation-across-route-configurations-and-proxy-modes">Worker invocation across route configurations and proxy modes</h4>
<p>The table below shows when Workers are invoked based on your route pattern and the customer's DNS proxy settings:</p>
<table>
<thead>
<tr>
<th>Route Pattern</th>
<th>Custom Hostname (Orange Cloud)</th>
<th>Custom Hostname (Grey Cloud)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*/*</code> (Recommended)</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Target hostname route</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Custom hostname route</td>
<td>❌</td>
<td>✅</td>
</tr>
</tbody>
</table>
