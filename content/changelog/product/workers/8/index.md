<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-sandbox-sdk-adds-streaming-code-interpreter-git-support-process-control-and-more"><a href="/changelog/post/2025-08-05-sandbox-sdk-major-update/">Cloudflare Sandbox SDK adds streaming, code interpreter, Git support, process control and more</a></h2>
<p><em>2025-08-05</em></p>
<p>We’ve shipped a major release for the <a href="https://github.com/cloudflare/sandbox-sdk">@cloudflare/sandbox</a> SDK, turning it into a full-featured, container-based execution platform that runs securely on Cloudflare Workers.</p>
<p>This update adds live streaming of output, persistent Python and JavaScript code interpreters with rich output support (charts, tables, HTML, JSON), file system access, Git operations, full background process control, and the ability to expose running services via public URLs.</p>
<p>This makes it ideal for building AI agents, CI runners, cloud REPLs, data analysis pipelines, or full developer tools — all without managing infrastructure.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-code-interpreter-python-js-ts">Code interpreter (Python, JS, TS)</h4>
<p>Create persistent code contexts with support for rich visual + structured outputs.</p>
<h4 id="2025-08-05-sandbox-sdk-major-update-createcodecontext-options">createCodeContext(options)</h4>
<p>Creates a new code execution context with persistent state.</p>
<pre><code class="language-ts">// Create a Python context&#10;const pythonCtx = await sandbox.createCodeContext({ language: &quot;python&quot; });&#10;&#10;// Create a JavaScript context&#10;const jsCtx = await sandbox.createCodeContext({ language: &quot;javascript&quot; });&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-runcode-code-options">runCode(code, options)</h4>
<p>Executes code with optional streaming callbacks.</p>
<pre><code class="language-ts">// Simple execution&#10;const execution = await sandbox.runCode(&#x27;print(&quot;Hello World&quot;)&#x27;, {&#10;	context: pythonCtx,&#10;});&#10;&#10;// With streaming callbacks&#10;await sandbox.runCode(&#10;	`&#10;for i in range(5):&#10;    print(f&quot;Step {i}&quot;)&#10;    time.sleep(1)&#10;`,&#10;	{&#10;		context: pythonCtx,&#10;		onStdout: (output) =&gt; console.log(&quot;Real-time:&quot;, output.text),&#10;		onResult: (result) =&gt; console.log(&quot;Result:&quot;, result),&#10;	},&#10;);&#10;</code></pre>
<p>Options:</p>
<ul>
<li>language: Programming language ('python' | 'javascript' | 'typescript')</li>
<li>cwd: Working directory (default: /workspace)</li>
<li>envVars: Environment variables for the context</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-real-time-streaming-output">Real-time streaming output</h4>
<p>Returns a streaming response for real-time processing.</p>
<pre><code class="language-ts">const stream = await sandbox.runCodeStream(&#10;	&quot;import time; [print(i) for i in range(10)]&quot;,&#10;);&#10;// Process the stream as needed&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-rich-output-handling">Rich output handling</h4>
<p>Interpreter outputs are auto-formatted and returned in multiple formats:</p>
<ul>
<li>text</li>
<li>html (e.g., Pandas tables)</li>
<li>png, svg (e.g., Matplotlib charts)</li>
<li>json (structured data)</li>
<li>chart (parsed visualizations)</li>
</ul>
<pre><code class="language-ts">const result = await sandbox.runCode(&#10;	`&#10;import seaborn as sns&#10;import matplotlib.pyplot as plt&#10;&#10;data = sns.load_dataset(&quot;flights&quot;)&#10;pivot = data.pivot(&quot;month&quot;, &quot;year&quot;, &quot;passengers&quot;)&#10;sns.heatmap(pivot, annot=True, fmt=&quot;d&quot;)&#10;plt.title(&quot;Flight Passengers&quot;)&#10;plt.show()&#10;&#10;pivot.to_dict()&#10;`,&#10;	{ context: pythonCtx },&#10;);&#10;&#10;if (result.png) {&#10;	console.log(&quot;Chart output:&quot;, result.png);&#10;}&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-preview-urls-from-exposed-ports">Preview URLs from Exposed Ports</h4>
<p>Start background processes and expose them with live URLs.</p>
<pre><code class="language-ts">await sandbox.startProcess(&quot;python -m http.server 8000&quot;);&#10;const preview = await sandbox.exposePort(8000);&#10;&#10;console.log(&quot;Live preview at:&quot;, preview.url);&#10;</code></pre>
<h4 id="2025-08-05-sandbox-sdk-major-update-full-process-lifecycle-control">Full process lifecycle control</h4>
<p>Start, inspect, and terminate long-running background processes.</p>
<pre><code class="language-ts">const process = await sandbox.startProcess(&quot;node server.js&quot;);&#10;console.log(`Started process ${process.id} with PID ${process.pid}`);&#10;&#10;// Monitor the process&#10;const logStream = await sandbox.streamProcessLogs(process.id);&#10;for await (const log of parseSSEStream&lt;LogEvent&gt;(logStream)) {&#10;	console.log(`Server: ${log.data}`);&#10;}&#10;</code></pre>
<ul>
<li>listProcesses() - List all running processes</li>
<li>getProcess(id) - Get detailed process status</li>
<li>killProcess(id, signal) - Terminate specific processes</li>
<li>killAllProcesses() - Kill all processes</li>
<li>streamProcessLogs(id, options) - Stream logs from running processes</li>
<li>getProcessLogs(id) - Get accumulated process output</li>
</ul>
<h4 id="2025-08-05-sandbox-sdk-major-update-git-integration">Git integration</h4>
<p>Clone Git repositories directly into the sandbox.</p>
<pre><code class="language-ts">await sandbox.gitCheckout(&quot;https://github.com/user/repo&quot;, {&#10;	branch: &quot;main&quot;,&#10;	targetDir: &quot;my-project&quot;,&#10;});&#10;</code></pre>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>


<h2 id="increased-disk-space-for-workers-builds"><a href="/changelog/post/2025-08-04-builds-increased-disk-size/">Increased disk space for Workers Builds</a></h2>
<p><em>2025-08-04T01:00:00+00:00</em></p>
<p>As part of the ongoing open beta for <a href="/workers/ci-cd/builds/">Workers Builds</a>, we’ve increased the available disk space for builds from <strong>8 GB</strong> to <strong>20 GB</strong> for both Free and Paid plans.</p>
<p>This provides more space for larger projects, dependencies, and build artifacts while improving overall build reliability.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Free Plan</th>
<th>Paid Plans</th>
</tr>
</thead>
<tbody>
<tr>
<td>Disk Space</td>
<td>20 GB</td>
<td>20 GB</td>
</tr>
</tbody>
</table>
<p>All other <a href="/workers/ci-cd/builds/limits-and-pricing/">build limits</a> — including CPU, memory, build minutes, and timeout remain unchanged.</p>


<h2 id="develop-locally-with-containers-and-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-08-01-containers-in-vite-dev/">Develop locally with Containers and the Cloudflare Vite plugin</a></h2>
<p><em>2025-08-01</em></p>
<p>You can now configure and run <a href="/containers">Containers</a> alongside your <a href="/workers">Worker</a> during local development when using the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. Previously, you could only develop locally when using <a href="/workers/wrangler/">Wrangler</a> as your local development server.</p>
<h4 id="2025-08-01-containers-in-vite-dev-configuration">Configuration</h4>
<p>You can simply configure your Worker and your Container(s) in your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17782.md")</div>
<h4 id="2025-08-01-containers-in-vite-dev-worker-code">Worker Code</h4>
<p>Once your Worker and Containers are configured, you can access the Container instances from your Worker code:</p>
<pre><code class="language-ts">import { Container, getContainer } from &quot;@cloudflare/containers&quot;;&#10;&#10;export class MyContainer extends Container {&#10;  defaultPort = 4000; // Port the container is listening on&#10;  sleepAfter = &quot;10m&quot;; // Stop the instance if requests not sent for 10 minutes&#10;}&#10;&#10;async fetch(request, env) {&#10;  const { &quot;session-id&quot;: sessionId } = await request.json();&#10;  // Get the container instance for the given session ID&#10;  const containerInstance = getContainer(env.MY_CONTAINER, sessionId)&#10;  // Pass the request to the container instance on its default port&#10;  return containerInstance.fetch(request);&#10;}&#10;</code></pre>
<h4 id="2025-08-01-containers-in-vite-dev-local-development">Local development</h4>
<p>To develop your Worker locally, start a local dev server by running</p>
<pre><code class="language-sh">vite dev&#10;</code></pre>
<p>in your terminal.</p>
<h4 id="2025-08-01-containers-in-vite-dev-resources">Resources</h4>
<p>Learn more about <a href="https://developers.cloudflare.com/containers/">Cloudflare Containers</a> or the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a> in our developer docs.</p>


<h2 id="deploy-to-cloudflare-buttons-now-support-worker-environment-variables-secrets-and-secrets-store-secrets"><a href="/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/">Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets</a></h2>
<p><em>2025-07-29T01:00:00+00:00</em></p>
<p>Any template which uses <a href="/workers/configuration/environment-variables/">Worker environment variables</a>, <a href="/workers/configuration/secrets/">secrets</a>, or <a href="/secrets-store/">Secrets Store secrets</a> can now be deployed using a <a href="/workers/platform/deploy-buttons/">Deploy to Cloudflare button</a>.</p>
<p>Define environment variables and secrets store bindings in your Wrangler configuration file as normal:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17781.md")</div>
<p>Add secrets to a <code>.dev.vars.example</code> or <code>.env.example</code> file:</p>
<pre><code class="language-ini">COOKIE_SIGNING_KEY=my-secret # comment&#10;</code></pre>
<p>And optionally, you can add a description for these bindings in your template's <code>package.json</code> to help users understand how to configure each value:</p>
<pre><code class="language-json">{&#10;	&quot;name&quot;: &quot;my-worker&quot;,&#10;	&quot;private&quot;: true,&#10;	&quot;cloudflare&quot;: {&#10;		&quot;bindings&quot;: {&#10;			&quot;API_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Select your company&#x27;s API key for connecting to the example service.&quot;&#10;			},&#10;			&quot;COOKIE_SIGNING_KEY&quot;: {&#10;				&quot;description&quot;: &quot;Generate a random string using `openssl rand -hex 32`.&quot;&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in <a href="/workers/platform/deploy-buttons/">our documentation</a>.</p>


<h2 id="test-out-code-changes-before-shipping-with-per-branch-preview-deployments-for-cloudflare-workers"><a href="/changelog/post/2025-07-23-workers-preview-urls/">Test out code changes before shipping with per-branch preview deployments for Cloudflare Workers</a></h2>
<p><em>2025-07-22T01:00:00+00:00</em></p>
<p>Now, when you connect your Cloudflare Worker to a git repository on GitHub or GitLab, each branch of your repository has its own stable preview URL, that you can use to preview code changes before merging the pull request and deploying to production.</p>
<p>This works the same way that Cloudflare Pages does — every time you create a pull request, you'll automatically get a shareable preview link where you can see your changes running, without affecting production. The link stays the same, even as you add commits to the same branch.
These preview URLs are named after your branch and are posted as a comment to each pull request. The URL stays the same with every commit and always points to the latest version of that branch.</p>
<p><img src="/assets/upstream/images/changelog/workers/preview-urls-comment.png" alt="PR comment preview" /></p>
<h4 id="2025-07-23-workers-preview-urls-preview-url-types">Preview URL types</h4>
<p>Each comment includes <strong>two preview URLs</strong> as shown above:</p>
<ul>
<li><strong>Commit Preview URL</strong>: Unique to the specific version/commit (e.g., <code>&lt;version-prefix&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
<li><strong>Branch Preview URL</strong>: A stable alias based on the branch name (e.g., <code>&lt;branch-name&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
</ul>
<h4 id="2025-07-23-workers-preview-urls-how-it-works">How it works</h4>
<p>When you create a pull request:</p>
<ul>
<li><strong>A preview alias is automatically created</strong> based on the Git branch name (e.g., <code>&lt;branch-name&gt;</code> becomes <code>&lt;branch-name&gt;-&lt;worker-name&gt;.&lt;subdomain&gt;.workers.dev</code>)</li>
<li><strong>No configuration is needed</strong>, the alias is generated for you</li>
<li><strong>The link stays the same</strong> even as you add commits to the same branch</li>
<li><strong>Preview URLs are posted directly to your pull request as comments</strong> (just like they are in Cloudflare Pages)</li>
</ul>
<h4 id="2025-07-23-workers-preview-urls-custom-alias-name">Custom alias name</h4>
<p>You can also assign a custom preview alias using the <a href="/workers/wrangler/">Wrangler CLI</a>, by passing the <code>--preview-alias</code> flag when <a href="/workers/wrangler/commands/general/#versions-upload">uploading a version</a> of your Worker:</p>
<pre><code class="language-bash">wrangler versions upload --preview-alias staging&#10;</code></pre>
<h4 id="2025-07-23-workers-preview-urls-limitations-while-in-beta">Limitations while in beta</h4>
<ul>
<li>Only available on the <strong>workers.dev</strong> subdomain (custom domains not yet supported)</li>
<li>Requires <strong>Wrangler v4.21.0+</strong></li>
<li>Preview URLs are not generated for Workers that use <a href="/durable-objects/">Durable Objects</a></li>
<li>Not yet supported for <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a></li>
</ul>


<h2 id="the-cloudflare-vite-plugin-now-supports-vite-7"><a href="/changelog/post/2025-07-17-vite-plugin-vite-7-support/">The Cloudflare Vite plugin now supports Vite 7</a></h2>
<p><em>2025-07-17T01:00:00+00:00</em></p>
<p><a href="https://vite.dev/blog/announcing-vite7">Vite 7</a> is now supported in the Cloudflare Vite plugin.
See the <a href="https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md#700-2025-06-24">Vite changelog</a> for a list of changes.</p>
<p>Note that the minimum Node.js versions supported by Vite 7 are 20.19 and 22.12.
We continue to support Vite 6 so you do not need to immediately upgrade.</p>


<h2 id="workers-now-supports-javascript-debug-terminals-in-vscode-cursor-and-windsurf-ides"><a href="/changelog/post/2025-07-04-javascript-debug-terminals/">Workers now supports JavaScript debug terminals in VSCode, Cursor and Windsurf IDEs</a></h2>
<p><em>2025-07-04</em></p>
<p>Workers now support breakpoint debugging using VSCode's built-in <a href="https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_javascript-debug-terminal">JavaScript Debug Terminals</a>. All you have to do is open a JS debug terminal (<code>Cmd + Shift + P</code> and then type <code>javascript debug</code>) and run <code>wrangler dev</code> (or <code>vite dev</code>) from within the debug terminal. VSCode will automatically connect to your running Worker (even if you're running multiple Workers at once!) and start a debugging session.</p>
<p>In 2023 we announced <a href="https://blog.cloudflare.com/debugging-cloudflare-workers/">breakpoint debugging support</a> for Workers, which meant that you could easily debug your Worker code in Wrangler's built-in devtools (accessible via the <code>[d]</code> hotkey) as well as multiple other devtools clients, <a href="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/">including VSCode</a>. For most developers, breakpoint debugging via VSCode is the most natural flow, but until now it's required <a href="https://developers.cloudflare.com/workers/observability/dev-tools/breakpoints/#setup-vs-code-to-use-breakpoints">manually configuring a <code>launch.json</code> file</a>, running <code>wrangler dev</code>, and connecting via VSCode's built-in debugger. Now it's much more seamless!</p>


<h2 id="enhanced-support-for-static-assets-with-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/">Enhanced support for static assets with the Cloudflare Vite plugin</a></h2>
<p><em>2025-07-01</em></p>
<p>You can now use any of Vite's <a href="https://vite.dev/guide/assets">static asset handling</a> features in your Worker as well as in your frontend.
These include importing assets as URLs, importing as strings and importing from the <code>public</code> directory as well as inlining assets.</p>
<p>Additionally, assets imported as URLs in your Worker are now automatically moved to the client build output.</p>
<p>Here is an example that fetches an imported asset using the <a href="/workers/static-assets/binding/#binding">assets binding</a> and modifies the response.</p>
<pre><code class="language-ts">// Import the asset URL&#10;// This returns the resolved path in development and production&#10;import myImage from &quot;./my-image.png&quot;;&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		// Fetch the asset using the binding&#10;		const response = await env.ASSETS.fetch(new URL(myImage, request.url));&#10;		// Create a new `Response` object that can be modified&#10;		const modifiedResponse = new Response(response.body, response);&#10;		// Add an additional header&#10;		modifiedResponse.headers.append(&quot;my-header&quot;, &quot;imported-asset&quot;);&#10;&#10;		// Return the modified response&#10;		return modifiedResponse;&#10;	},&#10;};&#10;</code></pre>
<p>Refer to <a href="/workers/vite-plugin/reference/static-assets/">Static Assets</a> in the Cloudflare Vite plugin docs for more info.</p>


<h2 id="remote-bindings-beta-now-works-with-next-js-connect-to-remote-resources-d1-kv-r2-etc-during-local-development"><a href="/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/">Remote bindings (beta) now works with Next.js — connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<p><em>2025-06-30</em></p>
<p>We <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">recently announced</a> our public beta for <a href="/workers/local-development/#remote-bindings">remote bindings</a>, which allow you to connect to deployed resources running on your Cloudflare account (like <a href="/r2">R2 buckets</a> or <a href="/d1">D1 databases</a>) while running a local development session.</p>
<p>Now, you can use remote bindings with your Next.js applications through the <a href="https://opennext.js.org/cloudflare/bindings#remote-bindings"><code>@opennextjs/cloudflare</code> adaptor</a> by enabling the experimental feature in your <code>next.config.ts</code>:</p>
<pre><code class="language-diff">&#45; initOpenNextCloudflareForDev();&#10;&#43; initOpenNextCloudflareForDev({&#10;&#43;  experimental: { remoteBindings: true }&#10;&#43; });&#10;</code></pre>
<p>Then, all you have to do is specify which bindings you want connected to the deployed resource on your Cloudflare account via the <code>experimental_remote</code> flag in your binding definition:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17780.md")</div>
<p>You can then run <code>next dev</code> to start a local development session (or start a preview with <code>opennextjs-cloudflare preview</code>), and all requests to <code>env.MY_BUCKET</code> will be proxied to the remote <code>testing-bucket</code> — rather than the <a href="/workers/local-development/#bindings-during-local-development">default local binding simulations</a>.</p>
<h4 id="2025-06-25-getPlatformProxy-support-remote-bindings-remote-bindings-isr">Remote bindings &amp; ISR</h4>
<p>Remote bindings are also used during the build process, which comes with significant benefits for pages using <a href="https://opennext.js.org/aws/inner_workings/components/server/node#isrssg">Incremental Static Regeneration (ISR)</a>. During the build step for an ISR page, your server executes the page's code just as it would for normal user requests. If a page needs data to display (like fetching user info from <a href="/kv">KV</a>), those requests are actually made. The server then uses this fetched data to render the final HTML.</p>
<p>Data fetching is a critical part of this process, as the finished HTML is only as good as the data it was built with. If the build process can't fetch real data, you end up with a pre-rendered page that's empty or incomplete.</p>
<p><strong>With remote bindings support in OpenNext,</strong> your pre-rendered pages are built with real data from the start. The build process uses any configured remote bindings, and any data fetching occurs against the deployed resources on your Cloudflare account.</p>
<p><strong>Want to learn more?</strong> Get started with <a href="https://opennext.js.org/cloudflare/bindings#remote-bindings">remote bindings and OpenNext</a>.</p>
<p><strong>Have feedback?</strong> Join the discussion in our <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">beta announcement</a> to share feedback or report any issues.</p>


<h2 id="run-and-connect-workers-in-separate-dev-commands-with-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/">Run and connect Workers in separate dev commands with the Cloudflare Vite plugin</a></h2>
<p><em>2025-06-26</em></p>
<p>Workers can now talk to each other across separate dev commands using service bindings and tail consumers, whether started with <code>vite dev</code> or <code>wrangler dev</code>.</p>
<p>Simply start each Worker in its own terminal:</p>
<pre><code class="language-sh">&#35; Terminal 1&#10;vite dev&#10;&#10;&#35; Terminal 2&#10;wrangler dev&#10;</code></pre>
<p>This is useful when different teams maintain different Workers, or when each Worker has its own build setup or tooling.</p>
<p>Check out the <a href="/workers/local-development/multi-workers">Developing with multiple Workers</a> guide to learn more about the different approaches and when to use each one.</p>


<h2 id="run-ai-generated-code-on-demand-with-code-sandboxes-new"><a href="/changelog/post/2025-06-24-announcing-sandboxes/">Run AI-generated code on-demand with Code Sandboxes (new)</a></h2>
<p><em>2025-06-25</em></p>
<p>AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing <a href="https://www.npmjs.com/package/@cloudflare/sandbox">Sandboxes</a>, which let your Worker run actual processes in a secure, container-based environment.</p>
<pre><code class="language-ts">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;		return sandbox.exec(&quot;ls&quot;, [&quot;-la&quot;]);&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-06-24-announcing-sandboxes-methods">Methods</h4>
<ul>
<li><code>exec(command: string, args: string[], options?: { stream?: boolean })</code>:Execute a command in the sandbox.</li>
<li><code>gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })</code>: Checkout a git repository in the sandbox.</li>
<li><code>mkdir(path: string, options: { recursive?: boolean; stream?: boolean })</code>: Create a directory in the sandbox.</li>
<li><code>writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })</code>: Write content to a file in the sandbox.</li>
<li><code>readFile(path: string, options: { encoding?: string; stream?: boolean })</code>: Read content from a file in the sandbox.</li>
<li><code>deleteFile(path: string, options?: { stream?: boolean })</code>: Delete a file from the sandbox.</li>
<li><code>renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })</code>: Rename a file in the sandbox.</li>
<li><code>moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })</code>: Move a file from one location to another in the sandbox.</li>
<li><code>ping()</code>: Ping the sandbox.</li>
</ul>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>
<p>You can try it today from your Worker, with just a few lines of code. Let us know what you build.</p>


<h2 id="cloudflare-actors-library-sdk-for-durable-objects-in-beta"><a href="/changelog/post/2025-06-25-actors-package-alpha/">@cloudflare/actors library - SDK for Durable Objects in beta</a></h2>
<p><em>2025-06-25</em></p>
<p>The new <a href="https://www.npmjs.com/package/@cloudflare/actors">@cloudflare/actors</a> library is now in beta!</p>
<p>The <code>@cloudflare/actors</code> library is a new SDK for Durable Objects and provides a powerful set of abstractions for building real-time, interactive, and multiplayer applications on top of Durable Objects. With beta usage and feedback, <code>@cloudflare/actors</code> will become the recommended way to build on Durable Objects and draws upon Cloudflare's experience building products/features on Durable Objects.</p>
<p>The name &quot;actors&quot; originates from the <a href="/durable-objects/concepts/what-are-durable-objects/#actor-programming-model">actor programming model</a>, which closely ties to how Durable Objects are modelled.</p>
<p>The <code>@cloudflare/actors</code> library includes:</p>
<ul>
<li>Storage helpers for querying embeddeded, per-object SQLite storage</li>
<li>Storage helpers for managing SQL schema migrations</li>
<li>Alarm helpers for scheduling multiple alarms provided a date, delay in seconds, or cron expression</li>
<li><code>Actor</code> class for using Durable Objects with a defined pattern</li>
<li>Durable Objects <a href="https://developers.cloudflare.com/durable-objects/api/base/">Workers API</a> is always available for your application as needed</li>
</ul>
<p>Storage and alarm helper methods can be combined with <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#storage--alarms-with-durableobject-class">any Javascript class</a> that defines your Durable Object, i.e, ones that extend <code>DurableObject</code> including the <code>Actor</code> class.</p>
<pre><code class="language-js">import { Storage } from &quot;@cloudflare/actors/storage&quot;;&#10;&#10;export class ChatRoom extends DurableObject&lt;Env&gt; {&#10;    storage: Storage;&#10;&#10;    constructor(ctx: DurableObjectState, env: Env) {&#10;        super(ctx, env)&#10;        this.storage = new Storage(ctx.storage);&#10;        this.storage.migrations = [{&#10;            idMonotonicInc: 1,&#10;            description: &quot;Create users table&quot;,&#10;            sql: &quot;CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)&quot;&#10;        }]&#10;    }&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        // Run migrations before executing SQL query&#10;        await this.storage.runMigrations();&#10;&#10;        // Query with SQL template&#10;        let userId = new URL(request.url).searchParams.get(&quot;userId&quot;);&#10;        const query = this.storage.sql`SELECT * FROM users WHERE id = ${userId};`&#10;        return new Response(`${JSON.stringify(query)}`);&#10;    }&#10;}&#10;</code></pre>
<p><code>@cloudflare/actors</code> library introduces the <code>Actor</code> class pattern. <code>Actor</code> lets you access Durable Objects without writing the Worker that communicates with your Durable Object (the Worker is created for you). By default, requests are routed to a Durable Object named &quot;default&quot;.</p>
<pre><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(&#x27;Hello, World!&#x27;)&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>You can <a href="/durable-objects/get-started/#3-instantiate-and-communicate-with-a-durable-object">route</a> to different Durable Objects by name within your <code>Actor</code> class using <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#actor-with-custom-name"><code>nameFromRequest</code></a>.</p>
<pre><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    static nameFromRequest(request: Request): string {&#10;        let url = new URL(request.url);&#10;        return url.searchParams.get(&quot;userId&quot;) ?? &quot;foo&quot;;&#10;    }&#10;&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(`Actor identifier (Durable Object name): ${this.identifier}`);&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>For more examples, check out the library <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#getting-started">README</a>. <code>@cloudflare/actors</code> library is a place for more helpers and built-in patterns, like retry handling and Websocket-based applications, to reduce development overhead for common Durable Objects functionality. Please share feedback and what more you would like to see on our <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord channel</a>.</p>


<h2 id="increased-blob-size-limits-in-workers-analytics-engine"><a href="/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/">Increased blob size limits in Workers Analytics Engine</a></h2>
<p><em>2025-06-20</em></p>
<p>We’ve increased the total allowed size of <a href="/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker"><code>blob</code></a> fields on data points written to <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> from <strong>5 KB to 16 KB</strong>.</p>
<p>This change gives you more flexibility when logging rich observability data — such as base64-encoded payloads, AI inference traces, or custom metadata — without hitting request size limits.</p>
<p>You can find full details on limits for queries, filters, payloads, and more <a href="/analytics/analytics-engine/limits/">here in the Workers Analytics Engine limits documentation</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17779.md")</div>


<h2 id="automate-worker-deployments-with-a-simplified-sdk-and-more-reliable-terraform-provider"><a href="/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/">Automate Worker deployments with a simplified SDK and more reliable Terraform provider</a></h2>
<p><em>2025-06-19</em></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-simplified-worker-deployments-with-our-sdks">Simplified Worker Deployments with our SDKs</h4>
<p>We've simplified the programmatic deployment of Workers via our <a href="/fundamentals/api/reference/sdks/">Cloudflare SDKs</a>. This update abstracts away the low-level complexities of the <code>multipart/form-data</code> upload process, allowing you to focus on your code while we handle the deployment mechanics.</p>
<p>This new interface is available in:</p>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (4.4.1)</li>
<li><a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (4.3.1)</li>
</ul>
<p>For complete examples, see our guide on <a href="/workers/platform/infrastructure-as-code">programmatic Worker deployments</a>.</p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-the-old-way-manual-api-calls">The Old way: Manual API calls</h4>
<p>Previously, deploying a Worker programmatically required manually constructing a <code>multipart/form-data</code> HTTP request, packaging your code and a separate <code>metadata.json</code> file. This was more complicated and verbose, and prone to formatting errors.</p>
<p>For example, here's how you would upload a Worker script previously with cURL:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/workers/scripts/my-hello-world-script \&#10;  &#45;X PUT \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;F &#x27;metadata={&#10;        &quot;main_module&quot;: &quot;my-hello-world-script.mjs&quot;,&#10;        &quot;bindings&quot;: [&#10;          {&#10;            &quot;type&quot;: &quot;plain_text&quot;,&#10;            &quot;name&quot;: &quot;MESSAGE&quot;,&#10;            &quot;text&quot;: &quot;Hello World!&quot;&#10;          }&#10;        ],&#10;        &quot;compatibility_date&quot;: &quot;$today&quot;&#10;      };type=application/json&#x27; \&#10;  &#45;F &#x27;my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module&#x27; &lt;&lt;EOF&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return new Response(env.MESSAGE, { status: 200 });&#10;  }&#10;};&#10;EOF&#10;</code></pre>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-after-sdk-interface">After: SDK interface</h4>
<p>With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.</p>
<p>This approach allows you to specify metadata like <code>main_module</code>, <code>bindings</code>, and <code>compatibility_date</code> as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.</p>
<p>Here's how you can now programmatically deploy a Worker via the <a href="https://github.com/cloudflare/cloudflare-typescript"><code>cloudflare-typescript</code> SDK</a></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17777.md")</div>
<p>View the complete example here: <a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts">https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts</a></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-terraform-provider-improvements">Terraform provider improvements</h4>
<p>We've also made several fixes and enhancements to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform provider</a>:</p>
<ul>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource in Terraform, which previously was producing a diff even when there were no changes. Now, your <code>terraform plan</code> outputs will be cleaner and more reliable.</li>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace"><code>cloudflare_workers_for_platforms_dispatch_namespace</code></a>, where the provider would attempt to recreate the namespace on a <code>terraform apply</code>. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.</li>
<li>The <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route"><code>cloudflare_workers_route</code></a> resource now allows for the <code>script</code> property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes <a href="/workers/configuration/routing/routes">docs</a>). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.</li>
<li>Using <code>primary_location_hint</code> in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database"><code>cloudflare_d1_database</code></a> resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.</li>
</ul>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-api-improvements">API improvements</h4>
<p>We've also properly documented the <a href="/api/resources/workers/subresources/scripts/subresources/script_and_version_settings">Workers Script And Version Settings</a> in our public OpenAPI spec and SDKs.</p>


<h2 id="remote-bindings-public-beta-connect-to-remote-resources-d1-kv-r2-etc-during-local-development"><a href="/changelog/post/2025-06-18-remote-bindings-beta/">Remote bindings public beta - Connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<p><em>2025-06-18</em></p>
<p>Today <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">we announced the public beta</a> of <a href="/workers/local-development/#remote-bindings">remote bindings</a> for local development. With remote bindings, you can now connect to deployed resources like <a href="/r2/">R2 buckets</a> and <a href="/d1/">D1 databases</a> while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.</p>
<h4 id="2025-06-18-remote-bindings-beta-example-configuration">Example configuration</h4>
<p>To enable remote mode, add <code>&quot;experimental_remote&quot; : true</code> to each binding that you want to rely on a remote resource running on Cloudflare:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17778.md")</div>
<p>When remote bindings are configured, your Worker <strong>still executes locally</strong>, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.</p>
<p><strong>You can try out remote bindings for local development today with:</strong></p>
<ul>
<li><a href="/workers/local-development/#remote-bindings">Wrangler v4.20.3</a>: Use the <code>wrangler dev --x-remote-bindings</code> command.</li>
<li>The <a href="/workers/local-development/#remote-bindings">Cloudflare Vite Plugin</a>: Refer to the documentation for how to enable in your Vite config.</li>
<li>The <a href="/workers/local-development/#remote-bindings">Cloudflare Vitest Plugin</a>: Refer to the documentation for how to enable in your Vitest config.</li>
</ul>
<p><strong>Have feedback?</strong>
Join the discussion in our <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">beta announcement</a> to share feedback or report any issues.</p>


<h2 id="control-which-routes-invoke-your-worker-script-for-single-page-applications"><a href="/changelog/post/2025-06-17-advanced-routing/">Control which routes invoke your Worker script for Single Page Applications</a></h2>
<p><em>2025-06-17</em></p>
<p>For those building <a href="/workers/static-assets/routing/single-page-application/#advanced-routing-control">Single Page Applications (SPAs) on Workers</a>, you can now explicitly define which routes invoke your Worker script in Wrangler configuration. The <a href="/workers/static-assets/binding/#run_worker_first"><code>run_worker_first</code> config option</a> has now been expanded to accept an array of route patterns, allowing you to more granularly specify when your Worker script runs.</p>
<p><strong>Configuration example:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17776.md")</div>
<p>This new routing control was done in partnership with our community and customers who provided great feedback on <a href="https://github.com/cloudflare/workers-sdk/discussions/9143">our public proposal</a>. Thank you to everyone who brought forward use-cases and feedback on the design!</p>
<h4 id="2025-06-17-advanced-routing-prerequisites">Prerequisites</h4>
<p>To use advanced routing control with <code>run_worker_first</code>, you'll need:</p>
<ul>
<li><a href="/workers/wrangler/install-and-update/">Wrangler</a> v4.20.0 and above</li>
<li><a href="/workers/vite-plugin/get-started/">Cloudflare Vite plugin</a> v1.7.0 and above</li>
</ul>


<h2 id="ssrf-vulnerability-in-opennextjs-cloudflare-proactively-mitigated-for-all-cloudflare-customers"><a href="/changelog/post/2025-06-17-open-next-ssrf/">SSRF vulnerability in @opennextjs/cloudflare proactively mitigated for all Cloudflare customers</a></h2>
<p><em>2025-06-17</em></p>
<p>Mitigations have been put in place for all existing and future deployments of sites with the Cloudflare adapter for Open Next in response to an identified Server-Side Request Forgery (SSRF) vulnerability in the <code>@opennextjs/cloudflare</code> package.</p>
<p>The vulnerability stemmed from an unimplemented feature in the Cloudflare adapter for Open Next, which allowed users to proxy arbitrary remote content via the <code>/_next/image</code> endpoint.</p>
<p>This issue allowed attackers to load remote resources from arbitrary hosts under the victim site's domain for any site deployed using the Cloudflare adapter for Open Next. For example: <code>https://victim-site.com/_next/image?url=https://attacker.com</code>. In this example, attacker-controlled content from <code>attacker.com</code> is served through the victim site's domain (<code>victim-site.com</code>), violating the same-origin policy and potentially misleading users or other services.</p>
<p>References: <a href="https://www.cve.org/cverecord?id=CVE-2025-6087">https://www.cve.org/cverecord?id=CVE-2025-6087</a>, <a href="https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m">https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m</a></p>
<h4 id="2025-06-17-open-next-ssrf-impact">Impact</h4>
<ul>
<li>SSRF via unrestricted remote URL loading</li>
<li>Arbitrary remote content loading</li>
<li>Potential internal service exposure or phishing risks through domain abuse</li>
</ul>
<h4 id="2025-06-17-open-next-ssrf-mitigation">Mitigation</h4>
<p>The following mitigations have been put in place:</p>
<p><strong>Server side updates</strong> to Cloudflare's platform to restrict the content loaded via the <code>/_next/image</code> endpoint to images. The update automatically mitigates the issue for all existing and any future sites deployed to Cloudflare using the affected version of the Cloudflare adapter for Open Next</p>
<p><strong>Root cause fix:</strong> Pull request <a href="https://github.com/opennextjs/opennextjs-cloudflare/pull/727">#727</a> to the Cloudflare adapter for Open Next. The patched version of the adapter has been released as <code>@opennextjs/cloudflare@1.3.0</code></p>
<p><strong>Package dependency update:</strong> Pull request <a href="https://github.com/cloudflare/workers-sdk/pull/9608">cloudflare/workers-sdk#9608</a> to create-cloudflare (c3) to use the fixed version of the Cloudflare adapter for Open Next. The patched version of create-cloudflare has been published as <code>create-cloudflare@2.49.3</code>.</p>
<p>In addition to the automatic mitigation deployed on Cloudflare's platform, we encourage affected users to upgrade to <code>@opennext/cloudflare</code> v1.3.0 and use the <a href="https://nextjs.org/docs/pages/api-reference/components/image#remotepatterns"><code>remotePatterns</code></a> filter in Next config if they need to allow-list external urls with images assets.</p>


<h2 id="grant-account-members-read-only-access-to-the-workers-platform"><a href="/changelog/post/2025-06-16-workers-platform-admin-role/">Grant account members read-only access to the Workers Platform</a></h2>
<p><em>2025-06-16</em></p>
<p>You can now grant members of your Cloudflare account read-only access to the Workers
Platform.</p>
<p>The new &quot;Workers Platform (Read-only)&quot; role grants read-only access to all products typically used as part of Cloudflare's Developer Platform, including <a href="/workers/">Workers</a>, <a href="/pages/">Pages</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, Zones, <a href="/analytics/account-and-zone-analytics/zone-analytics/">Zone Analytics</a> and <a href="/rules/">Page Rules</a>. When Cloudflare introduces new products to the Workers platform, we will add additional read-only permissions to this role.</p>
<p>Additionally, the role previously named &quot;Workers Admin&quot; has been renamed to &quot;Workers Platform Admin&quot;. This
change ensures that the name more accurately reflects the permissions granted — this
role has always granted access to more than just
Workers — it grants read and write access to the products mentioned above, and similarly, as new products are added to the Workers platform, we will add additional read and write permissions to this role.</p>
<p>You can review the updated roles in the <a href="/fundamentals/manage-members/roles/">developer docs</a>.</p>


<h2 id="access-git-commit-sha-and-branch-name-as-environment-variables-in-workers-builds"><a href="/changelog/post/2025-06-10-default-env-vars/">Access git commit sha and branch name as environment variables in Workers Builds</a></h2>
<p><em>2025-06-10</em></p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> connects your Worker to a <a href="/workers/ci-cd/builds/git-integration/">Git repository</a>, and automates building and deploying your code on each pushed change.</p>
<p>To make CI/CD pipelines even more flexible, Workers Builds now automatically injects <a href="/workers/ci-cd/builds/configuration/#environment-variables">default environment variables</a> into your build process (much like the defaults in <a href="/pages/configuration/build-configuration/#environment-variables">Cloudflare Pages projects</a>). You can use these variables to customize your build process based on the deployment context, such as the branch or commit.</p>
<p>The following environment variables are injected by default:</p>
<table>
<thead>
<tr>
<th>Environment Variable</th>
<th>Injected value</th>
<th>Example use-case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CI</code></td>
<td><code>true</code></td>
<td>Changing build behavior when run on CI versus locally</td>
</tr>
<tr>
<td><code>WORKERS_CI</code></td>
<td><code>1</code></td>
<td>Changing build behavior when run on Workers Builds versus locally</td>
</tr>
<tr>
<td><code>WORKERS_CI_BUILD_UUID</code></td>
<td><code>&lt;build-uuid-of-current-build&gt;</code></td>
<td>Passing the Build UUID along to custom workflows</td>
</tr>
<tr>
<td><code>WORKERS_CI_COMMIT_SHA</code></td>
<td><code>&lt;sha1-hash-of-current-commit&gt;</code></td>
<td>Passing current commit ID to error reporting, for example, Sentry</td>
</tr>
<tr>
<td><code>WORKERS_CI_BRANCH</code></td>
<td><code>&lt;branch-name-from-push-event</code></td>
<td>Customizing build based on branch, for example, disabling debug logging on <code>production</code></td>
</tr>
</tbody>
</table>
<p>You can override these default values and add your own custom environment variables by navigating to <strong>your Worker</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment variables</strong>.</p>
<p>Learn more in the <a href="/workers/ci-cd/builds/configuration/#environment-variables">Build configuration documentation</a>.</p>


<h2 id="workers-native-integrations-were-removed-from-the-cloudflare-dashboard"><a href="/changelog/post/2025-06-09-workers-integrations-changes/">Workers native integrations were removed from the Cloudflare dashboard</a></h2>
<p><em>2025-06-09</em></p>
<p>Workers native integrations were <a href="https://blog.cloudflare.com/announcing-database-integrations/">originally launched in May 2023</a> to connect to popular database and observability providers with your Worker in just a few clicks. We are changing how developers connect Workers to these external services. The <strong>Integrations</strong> tab in the dashboard has been removed in favor of a more direct, command-line-based approach using <a href="/workers/wrangler/commands/general/#secret">Wrangler secrets</a>.</p>
<h4 id="2025-06-09-workers-integrations-changes-what-s-changed">What's changed</h4>
<ul>
<li><strong>Integrations tab removed</strong>: The integrations setup flow is no longer available in the Workers dashboard.</li>
<li><strong>Manual secret configuration</strong>: New connections should be configured by adding credentials as secrets to your Workers using <code>npx wrangler secret put</code> commands.</li>
</ul>
<h4 id="2025-06-09-workers-integrations-changes-impact-on-existing-integrations">Impact on existing integrations</h4>
<p><strong>Existing integrations will continue to work without any changes required.</strong> If you have integrations that were previously created through the dashboard, they will remain functional.</p>
<h4 id="2025-06-09-workers-integrations-changes-updating-existing-integrations">Updating existing integrations</h4>
<p>If you'd like to modify your existing integration, you can update the secrets, environment variables, or <a href="/workers/observability/logs/tail-workers/">Tail Workers</a> that were created from the original integration setup.</p>
<ul>
<li><strong>Update secrets</strong>: Use <code>npx wrangler secret put &lt;SECRET_NAME&gt;</code> to update credential values.</li>
<li><strong>Modify environment variables</strong>: Update variables through the dashboard or Wrangler configuration.</li>
<li><strong>Dashboard management</strong>: Access your Worker's settings in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> to modify connections created by our removed native integrations feature.</li>
</ul>
<p>If you have previously set up an observability integration with <a href="https://sentry.io">Sentry</a>, the following environment variables were set and are still modifiable:</p>
<ul>
<li><code>BLOCKED_HEADERS</code>: headers to exclude sending to Sentry</li>
<li><code>EXCEPTION_SAMPLING_RATE</code>: number from 0 - 100, where 0 = no events go through to Sentry, and 100 = all events go through to Sentry</li>
<li><code>STATUS_CODES_TO_SAMPLING_RATES</code>: a map of status codes -- like 400 or with wildcards like 4xx -- to sampling rates described above</li>
</ul>
<h4 id="2025-06-09-workers-integrations-changes-setting-up-new-database-and-observability-connections">Setting up new database and observability connections</h4>
<p>For new connections, refer to our step-by-step guides on connecting to popular database and observability providers including: <a href="/workers/observability/third-party-integrations/sentry">Sentry</a>, <a href="/workers/databases/third-party-integrations/turso/">Turso</a>, <a href="/workers/databases/third-party-integrations/neon/">Neon</a>, <a href="/workers/databases/third-party-integrations/supabase/">Supabase</a>, <a href="/workers/databases/third-party-integrations/planetscale/">PlanetScale</a>, <a href="/workers/databases/third-party-integrations/upstash/">Upstash</a>, <a href="/workers/databases/third-party-integrations/xata/">Xata</a>.</p>


<h2 id="performance-and-size-optimization-for-the-cloudflare-adapter-for-open-next"><a href="/changelog/post/2025-06-05-open-next-size/">Performance and size optimization for the Cloudflare adapter for Open Next</a></h2>
<p><em>2025-06-05T19:00:00+00:00</em></p>
<p>With the release of the Cloudflare adapter for Open Next v1.0.0 in May 2025, we already had followups plans <a href="https://blog.cloudflare.com/deploying-nextjs-apps-to-cloudflare-workers-with-the-opennext-adapter/#1-0-and-the-road-ahead">to improve performance and size</a>.</p>
<p><code>@opennextjs/cloudflare</code> v1.2 released on June 5, 2025 delivers on these enhancements. By removing <code>babel</code> from the app code and dropping a dependency on <code>@ampproject/toolbox-optimizer</code>, we were able to reduce generated bundle sizes. Additionally, by stopping preloading of all app routes, we were able to improve the cold start time.</p>
<p>This means that users will now see a decrease from 14 to 8MiB (2.3 to 1.6MiB gzipped) in generated bundle size for a Next app created via create-next-app, and typically 100ms faster startup times for their medium-sized apps.</p>
<p>Users only need to update to the latest version of <code>@opennextjs/cloudflare</code> to automatically benefit from these improvements.</p>
<p>Note that we published <a href="https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-rvpw-p7vw-wj3m">CVE-2005-6087</a> for a SSRF vulnerability in the <code>@opennextjs/cloudflare</code> package.
The vulnerability has been fixed from <code>@opennextjs/cloudflare</code> v1.3.0 onwards. Please update to any version after this one.</p>


<h2 id="view-an-architecture-diagram-of-your-worker-directly-in-the-cloudflare-dashboard"><a href="/changelog/post/2025-06-03-visualize-your-worker-architecture/">View an architecture diagram of your Worker directly in the Cloudflare dashboard</a></h2>
<p><em>2025-06-03</em></p>
<p>You can now visualize, explore and modify your Worker’s architecture directly in the Cloudflare dashboard, making it easier to understand how your application connects to Cloudflare resources like <a href="/d1">D1 databases</a>, <a href="/durable-objects">Durable Objects</a>, <a href="/kv">KV namespaces</a>, and <a href="/workers/runtime-apis/bindings/">more</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/bindings-canvas.png" alt="Bindings canvas" /></p>
<p>With this new view, you can easily:</p>
<ul>
<li>Explore existing bindings in a visual, architecture-style diagram</li>
<li>Add and manage bindings directly from the same interface</li>
<li>Discover the full range of compute, storage, AI, and media resources you can attach to your Workers application.</li>
</ul>
<p>To get started, head to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages">Cloudflare dashboard</a> and open the <strong>Bindings</strong> tab of any Workers application.</p>


<h2 id="debug-profile-and-view-logs-for-your-worker-in-chrome-devtools-now-supported-in-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-05-21-vite-plugin-chrome-devtools/">Debug, profile, and view logs for your Worker in Chrome Devtools — now supported in the Cloudflare Vite plugin</a></h2>
<p><em>2025-05-30</em></p>
<p>You can now <a href="https://developers.cloudflare.com/workers/observability/dev-tools/">debug, profile, view logs, and analyze memory usage for your Worker</a> using <a href="https://developer.chrome.com/docs/devtools">Chrome Devtools</a> when your Worker runs locally using the <a href="https://developers.cloudflare.com/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p>Previously, this was only possible if your Worker ran locally using the <a href="https://developers.cloudflare.com/workers/wrangler/">Wrangler CLI</a>, and now you can do all the same things if your Worker uses <a href="https://vite.dev/">Vite</a>.</p>
<p>When you run <code>vite</code>, you'll now see a debug URL in your console:</p>
<pre><code>  VITE v6.3.5  ready in 461 ms&#10;&#10;  ➜  Local:   http://localhost:5173/&#10;  ➜  Network: use --host to expose&#10;  ➜  Debug:   http://localhost:5173/__debug&#10;  ➜  press h + enter to show help&#10;</code></pre>
<p>Open the URL in Chrome, and an instance of Chrome Devtools will open and connect to your Worker running locally. You can then use Chrome Devtools to debug and introspect performance issues. For example, you can navigate to the Performance tab to understand where CPU time is spent in your Worker:</p>
<p><img src="/assets/upstream/images/workers/observability/profile.png" alt="CPU Profile" /></p>
<p>For more information on how to get the most out of Chrome Devtools, refer to the following docs:</p>
<ul>
<li><a href="/workers/observability/dev-tools/breakpoints/">Debug code by setting breakpoints</a></li>
<li><a href="/workers/observability/dev-tools/cpu-usage/">Profile CPU usage</a></li>
<li><a href="/workers/observability/dev-tools/memory-usage/">Observe memory usage and debug memory leaks</a></li>
</ul>


<h2 id="50-500ms-faster-d1-rest-api-requests"><a href="/changelog/post/2025-05-30-d1-rest-api-latency/">50-500ms Faster D1 REST API Requests</a></h2>
<p><em>2025-05-29</em></p>
<p>Users using Cloudflare's <a href="/api/resources/d1/">REST API</a> to query their D1 database can see lower end-to-end request latency now that D1 authentication is performed at the closest Cloudflare network data center that received the request. Previously, authentication required D1 REST API requests to proxy to Cloudflare's core, centralized data centers, which added network round trips and latency.</p>
<p>Latency improvements range from 50-500 ms depending on request location and <a href="/d1/configuration/data-location/">database location</a> and only apply to the REST API. REST API requests and databases outside the United States see a bigger benefit since Cloudflare's primary core data centers reside in the United States.</p>
<p>D1 query endpoints like <code>/query</code> and <code>/raw</code> have the most noticeable improvements since they no longer access Cloudflare's core data centers. D1 control plane endpoints such as those to create and delete databases see smaller improvements, since they still require access to Cloudflare's core data centers for other control plane metadata.</p>


<h2 id="handle-incoming-request-cancellation-in-workers-with-request-signal"><a href="/changelog/post/2025-05-22-handle-request-cancellation/">Handle incoming request cancellation in Workers with Request.signal</a></h2>
<p><em>2025-05-22</em></p>
<p>In Cloudflare Workers, you can now attach an event listener to <a href="/workers/runtime-apis/request/"><code>Request</code></a> objects, using the <a href="https://developer.mozilla.org/en-US/docs/Web/API/Request/signal"><code>signal</code> property</a>. This allows you to perform tasks when the request to your Worker is canceled by the client. To use this feature, you must set the <a href="/workers/configuration/compatibility-flags/#enable-requestsignal-for-incoming-requests"><code>enable_request_signal</code></a> compatibility flag.</p>
<p>You can use a listener to perform cleanup tasks or write to logs before your Worker's invocation ends. For example, if you run the Worker below, and then abort the request from the client, a log will be written:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17775.md")</div>
<p>For more information see the <a href="/workers/runtime-apis/request"><code>Request</code> documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/7/">Previous</a><span>Page 8 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/9/">Next</a></nav>
