<p>Get started with Workers for Platforms by deploying a starter kit to your account.</p>
<h2 id="deploy-a-platform">Deploy a platform</h2>
<p>Deploy the <a href="https://github.com/cloudflare/templates/tree/main/worker-publisher-template">Platform Starter Kit</a> to your Cloudflare account. This creates a complete Workers for Platforms setup with one click.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/worker-publisher-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>After deployment completes, open your Worker URL. You now have a platform where you can deploy code snippets.</p>
<h3 id="try-it-out">Try it out</h3>
<ol>
<li>Enter a script name, for example <code>my-worker</code>.</li>
<li>Write or paste Worker code in the editor.</li>
<li>Click <strong>Deploy Worker</strong>.</li>
</ol>
<p>Once deployed, visit <code>/&lt;script-name&gt;</code> on your Worker URL to run your code. For example, if you named your script <code>my-worker</code>, go to <code>https://&lt;your-worker&gt;.&lt;subdomain&gt;.workers.dev/my-worker</code>.</p>
<p>Each script you deploy becomes its own isolated Worker. The platform calls the Cloudflare API to create the Worker and the dispatch Worker routes requests to it based on the URL path.</p>
<h2 id="understand-how-it-works">Understand how it works</h2>
<p>The template you deployed contains three components that work together:</p>
<h3 id="dispatch-namespace">Dispatch namespace</h3>
<p>A dispatch namespace is a collection of user Workers. Think of it as a container that holds all the Workers your platform deploys on behalf of your customers.</p>
<p>When you deployed the template, it created a dispatch namespace automatically. You can view it in the Cloudflare dashboard under <strong>Workers for Platforms</strong>.</p>
<h3 id="dispatch-worker">Dispatch Worker</h3>
<p>The dispatch Worker receives incoming requests and routes them to the correct user Worker. It uses a <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">binding</a> to access the dispatch namespace.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		// Get the user Worker name from the URL path&#10;		const url = new URL(request.url);&#10;		const workerName = url.pathname.split(&quot;/&quot;)[1];&#10;&#10;		// Fetch the user Worker from the dispatch namespace&#10;		const userWorker = env.DISPATCHER.get(workerName);&#10;&#10;		// Forward the request to the user Worker&#10;		return userWorker.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>The <code>env.DISPATCHER.get()</code> method retrieves a user Worker by name from the dispatch namespace.</p>
<h3 id="user-workers">User Workers</h3>
<p>User Workers contain the code your customers write and deploy. They run in isolated environments with no access to other customers' data or code.</p>
<p>In the template, user Workers are deployed programmatically through the API. In production, your platform would call the Cloudflare API or SDK to deploy user Workers when your customers save their code.</p>
<h2 id="build-your-platform">Build your platform</h2>
<p>Now that you understand how the components work together, customize the template for your use case:</p>
<ul>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/">Dynamic dispatch</a> — Route requests by subdomain or hostname</li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/hostname-routing/">Hostname routing</a> — Let customers use <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">custom domains</a> with their applications</li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/">Bindings</a> — Give each customer access to their own <a href="/d1/">database</a>, <a href="/kv/">key-value store</a>, or <a href="/r2/">object storage</a></li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">Outbound Workers</a> — Configure egress policies on outgoing requests from customer code</li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/">Custom limits</a> — Set CPU time and subrequest limits per customer</li>
<li><a href="/cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/">API examples</a> — Examples for deploying and managing customer code programmatically</li>
</ul>
<h2 id="build-an-ai-vibe-coding-platform">Build an AI vibe coding platform</h2>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/vibesdk"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>Build an <a href="/reference-architecture/diagrams/ai/ai-vibe-coding-platform/">AI vibe coding platform</a> where users describe what they want and AI generates and deploys applications.</p>
<p>With <a href="https://github.com/cloudflare/vibesdk">VibeSDK</a>, Cloudflare's open source vibe coding platform, you can get started with an example that handles AI code generation, code execution in secure sandboxes, live previews, and deployment at scale.</p>
<p><a class="nb-link-button" href="https://build.cloudflare.dev">View demo</a>
<a class="nb-link-button" href="https://github.com/cloudflare/vibesdk">View on GitHub</a></p>
<h2 id="deploy-an-internal-static-sites-platform">Deploy an internal static sites platform</h2>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/internal-sites-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>Deploy an internal drag-and-drop static site platform for your company. Employees upload files and get a live URL -- every site is protected behind <a href="/cloudflare-one/">Cloudflare Access</a>.</p>
<p>Uses <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> and <a href="/cloudflare-one/">Access</a> to handle site deployment and company-wide authentication.</p>
<p><a class="nb-link-button" href="https://github.com/cloudflare/templates/tree/main/internal-sites-template">View on GitHub</a></p>
