<p>Build your first application with Sandbox SDK - a secure code execution environment. In this guide, you'll create a Worker that can execute Python code and work with files in isolated containers.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/421.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="what-you-re-building">What you're building</h3>
@markup("md", "content/.markup/bodies/420.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/422.md")
</div></details>
<h3 id="ensure-docker-is-running-locally">Ensure Docker is running locally</h3>
<p>Sandbox SDK uses <a href="https://www.docker.com/">Docker</a> to build container images alongside your Worker.</p>
<p>You must have Docker running locally when you run <code>wrangler deploy</code>. For most people, the best way to install Docker is to follow the <a href="https://docs.docker.com/desktop/">docs for installing Docker Desktop</a>. Other tools like <a href="https://github.com/abiosoft/colima">Colima</a> may also work.</p>
<p>You can check that Docker is running properly by running the <code>docker info</code> command in your terminal. If Docker is running, the command will succeed. If Docker is not running,
the <code>docker info</code> command will hang or return an error including the message &quot;Cannot connect to the Docker daemon&quot;.</p>
<h2 id="1-create-a-new-project"><ol>
<li>Create a new project</li>
</ol></h2>
<p>Create a new Sandbox SDK project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-sandbox --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-sandbox --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-sandbox --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-sandbox --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-sandbox --template=cloudflare/sandbox-sdk/examples/minimal</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-sandbox --template=cloudflare/sandbox-sdk/examples/minimal" aria-label="Copy to clipboard">Copy</button></div></div>
<p>This creates a <code>my-sandbox</code> directory with everything you need:</p>
<ul>
<li><code>src/index.ts</code> - Worker with sandbox integration</li>
<li><code>wrangler.jsonc</code> - Configuration for Workers and Containers</li>
<li><code>Dockerfile</code> - Container environment definition</li>
</ul>
<pre><code class="language-sh">cd my-sandbox&#10;</code></pre>
<h2 id="2-explore-the-template"><ol start="2">
<li>Explore the template</li>
</ol></h2>
<p>The template provides a minimal Worker that demonstrates core sandbox capabilities:</p>
<pre><code class="language-typescript">import { getSandbox, proxyToSandbox, type Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;type Env = {&#10;	Sandbox: DurableObjectNamespace&lt;Sandbox&gt;;&#10;};&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;		const url = new URL(request.url);&#10;&#10;		// Get or create a sandbox instance. For user-facing apps,&#10;		// derive this ID from the authenticated user.&#10;		const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;&#10;		// Execute Python code&#10;		if (url.pathname === &quot;/run&quot;) {&#10;			const result = await sandbox.exec(&#x27;python3 -c &quot;print(2 + 2)&quot;&#x27;);&#10;			return Response.json({&#10;				output: result.stdout,&#10;				error: result.stderr,&#10;				exitCode: result.exitCode,&#10;				success: result.success,&#10;			});&#10;		}&#10;&#10;		// Work with files&#10;		if (url.pathname === &quot;/file&quot;) {&#10;			await sandbox.writeFile(&quot;/workspace/hello.txt&quot;, &quot;Hello, Sandbox!&quot;);&#10;			const file = await sandbox.readFile(&quot;/workspace/hello.txt&quot;);&#10;			return Response.json({&#10;				content: file.content,&#10;			});&#10;		}&#10;&#10;		return new Response(&quot;Try /run or /file&quot;);&#10;	},&#10;};&#10;</code></pre>
<p><strong>Key concepts</strong>:</p>
<ul>
<li><code>getSandbox()</code> - Gets or creates a sandbox instance by ID. Use a stable ID to reconnect to the same sandbox. In user-facing apps, scope IDs to a single user.</li>
<li><code>sandbox.exec()</code> - Execute shell commands in the sandbox and capture stdout, stderr, and exit codes.</li>
<li><code>sandbox.writeFile()</code> / <code>readFile()</code> - Write and read files in the sandbox filesystem.</li>
</ul>
<h2 id="3-test-locally"><ol start="3">
<li>Test locally</li>
</ol></h2>
<p>Start the development server:</p>
<pre><code class="language-sh">npm run dev&#10;&#35; If you expect to have multiple sandbox instances, you can increase `max_instances`.&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/419.md")
</aside>
<p>Test the endpoints:</p>
<pre><code class="language-sh">&#35; Execute Python code&#10;curl http://localhost:8787/run&#10;&#10;&#35; File operations&#10;curl http://localhost:8787/file&#10;</code></pre>
<p>You should see JSON responses with the command output and file contents.</p>
<h2 id="4-deploy-to-production"><ol start="4">
<li>Deploy to production</li>
</ol></h2>
<p>Deploy your Worker and container:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>This will:</p>
<ol>
<li>Build your container image using Docker</li>
<li>Push it to Cloudflare's Container Registry</li>
<li>Deploy your Worker globally</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="wait-for-provisioning">Wait for provisioning</h3>
@markup("md", "content/.markup/bodies/418.md")
</aside>
<p>Check deployment status:</p>
<pre><code class="language-sh">npx wrangler containers list&#10;</code></pre>
<h2 id="5-test-your-deployment"><ol start="5">
<li>Test your deployment</li>
</ol></h2>
<p>Visit your Worker URL (shown in deploy output):</p>
<pre><code class="language-sh">&#35; Replace with your actual URL&#10;curl https://my-sandbox.YOUR_SUBDOMAIN.workers.dev/run&#10;</code></pre>
<p>Your sandbox is now deployed and can execute code in isolated containers.</p>
<h2 id="understanding-the-configuration">Understanding the configuration</h2>
<p>Your <code>wrangler.jsonc</code> connects three pieces together:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/423.md")
</div>
<ul>
<li><strong>containers</strong> - Defines the <a href="/workers/wrangler/configuration/#containers">container image, instance type, and resource limits</a> for your sandbox environment. If you expect to have multiple sandbox instances, you can increase <code>max_instances</code>.</li>
<li><strong>durable_objects</strong> - You need not be familiar with <a href="/durable-objects">Durable Objects</a> to use Sandbox SDK, but if you'd like, you can <a href="/containers/get-started/#each-container-is-backed-by-its-own-durable-object">learn more about Cloudflare Containers and Durable Objects</a>. This configuration creates a <a href="/workers/runtime-apis/bindings#what-is-a-binding">binding</a> that makes the <code>Sandbox</code> Durable Object accessible in your Worker code.</li>
<li><strong>migrations</strong> - Registers the <code>Sandbox</code> class, implemented by the Sandbox SDK, with <a href="/durable-objects/best-practices/access-durable-objects-storage">SQLite storage backend</a> (required once)</li>
</ul>
<p>For detailed configuration options including environment variables, secrets, and custom images, see the <a href="/sandbox/configuration/wrangler/">Wrangler configuration reference</a>.</p>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have a working sandbox, explore more capabilities:</p>
<ul>
<li><a href="/sandbox/tutorials/workers-ai-code-interpreter/">Code interpreter with Workers AI</a> - Build an AI-powered code execution system</li>
<li><a href="/sandbox/guides/execute-commands/">Execute commands</a> - Run shell commands and stream output</li>
<li><a href="/sandbox/guides/manage-files/">Manage files</a> - Work with files and directories</li>
<li><a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a> - Deploy and keep package and image aligned</li>
<li><a href="/sandbox/guides/expose-services/">Expose services</a> - Get public URLs for services running in your sandbox</li>
<li><a href="/sandbox/api/tunnels/">Quick tunnels</a> - Zero-config <code>*.trycloudflare.com</code> URLs for development and <code>.workers.dev</code> deployments</li>
<li><a href="/sandbox/guides/preview-urls-custom-domain/">Configure preview URLs on a custom domain</a> - Wildcard DNS and TLS for <code>exposePort()</code></li>
<li><a href="/sandbox/api/">API reference</a> - Complete API documentation</li>
</ul>
