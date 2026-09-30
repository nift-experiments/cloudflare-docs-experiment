<p>You can build, run, and test your Worker code on your own local machine before deploying it to Cloudflare's network. This is made possible through <a href="/workers/testing/miniflare/">Miniflare</a>, a simulator that executes your Worker code using the same runtime used in production, <a href="https://github.com/cloudflare/workerd"><code>workerd</code></a>.</p>
<p><a href="/workers/local-development/#defaults">By default</a>, your Worker's bindings <a href="/workers/local-development/#bindings-during-local-development">connect to locally simulated resources</a>, but can be configured to interact with the real, production resource with <a href="/workers/local-development/#remote-bindings">remote bindings</a>.</p>
<h2 id="core-concepts">Core concepts</h2>
<h3 id="worker-execution-vs-bindings">Worker execution vs Bindings</h3>
<p>When developing Workers, it's important to understand two distinct concepts:</p>
<ul>
<li>
<p><strong>Worker execution</strong>: Where your Worker code actually runs (on your local machine vs on Cloudflare's infrastructure).</p>
</li>
<li>
<p><a href="/workers/runtime-apis/bindings/"><strong>Bindings</strong></a>: How your Worker interacts with Cloudflare resources (like <a href="/kv">KV namespaces</a>, <a href="/r2">R2 buckets</a>, <a href="/d1">D1 databases</a>, <a href="/queues/">Queues</a>, <a href="/durable-objects/">Durable Objects</a>, etc). In your Worker code, these are accessed via the <code>env</code> object (such as <code>env.MY_KV</code>).</p>
</li>
</ul>
<h2 id="start-a-local-development-server">Start a local development server</h2>
<p>You can start a local development server using:</p>
<ol>
<li>The Cloudflare Workers CLI <a href="/workers/wrangler/"><strong>Wrangler</strong></a>, using the built-in <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a> command.</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler dev" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li><a href="https://vite.dev/"><strong>Vite</strong></a>, using the <a href="/workers/vite-plugin/"><strong>Cloudflare Vite plugin</strong></a>.</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx vite dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx vite dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn vite dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn vite dev" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm vite dev</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm vite dev" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Both Wrangler and the Cloudflare Vite plugin use <a href="/workers/testing/miniflare/">Miniflare</a> under the hood, and are developed and maintained by the Cloudflare team. For guidance on choosing when to use Wrangler versus Vite, see our guide <a href="/workers/local-development/wrangler-vs-vite/">Choosing between Wrangler &amp; Vite</a>.</p>
<ul>
<li><a href="/workers/wrangler/install-and-update/">Get started with Wrangler</a></li>
<li><a href="/workers/vite-plugin/get-started/">Get started with the Cloudflare Vite plugin</a></li>
</ul>
<h3 id="defaults">Defaults</h3>
<p>By default, running <code>wrangler dev</code> / <code>vite dev</code> (when using the <a href="/workers/vite-plugin/get-started/">Vite plugin</a>) means that:</p>
<ul>
<li>Your Worker code runs on your local machine.</li>
<li>All resources your Worker is bound to in your <a href="/workers/wrangler/configuration/">Wrangler configuration</a> are simulated locally.</li>
<li>The local <code>workerd</code> runtime runs with <code>TZ=UTC</code> so that <code>Date</code> and <code>Intl</code> APIs inside your Worker observe UTC, matching the production Cloudflare runtime regardless of your machine's timezone.</li>
</ul>
<h3 id="bindings-during-local-development">Bindings during local development</h3>
<p><a href="/workers/runtime-apis/bindings/">Bindings</a> are interfaces that allow your Worker to interact with various Cloudflare resources (like <a href="/kv">KV namespaces</a>, <a href="/r2">R2 buckets</a>, <a href="/d1">D1 databases</a>, <a href="/queues/">Queues</a>, <a href="/durable-objects/">Durable Objects</a>, etc). In your Worker code, these are accessed via the <code>env</code> object (such as <code>env.MY_KV</code>).</p>
<p>During local development, your Worker code interacts with these bindings using the exact same API calls (such as <code>env.MY_KV.put()</code>) as it would in a deployed environment. These local resources are initially empty, but you can populate them with data, as documented in <a href="/workers/local-development/local-data/">Adding local data</a>.</p>
<ul>
<li>By default, bindings connect to <strong>local resource simulations</strong> (except for <a href="/workers-ai/configuration/bindings/">AI bindings</a>, as AI models always run remotely).</li>
<li>You can override this default behavior and <strong>connect to the remote resource</strong> on a per-binding basis with <a href="/workers/local-development/#remote-bindings">remote bindings</a>. This lets you connect to real, production resources while still running your Worker code locally.</li>
<li>When using <code>wrangler dev</code>, you can temporarily disable all <a href="/workers/local-development/#remote-bindings">remote bindings</a> (and connect only to local resources) by providing the <code>--local</code> flag (i.e. <code>wrangler dev --local</code>)</li>
</ul>
<h2 id="remote-bindings">Remote bindings</h2>
<p><strong>Remote bindings</strong> are bindings that are configured to connect to the deployed, remote resource during local development <em>instead</em> of the locally simulated resource. Remote bindings are supported by <a href="/workers/wrangler/"><strong>Wrangler</strong></a>, the <a href="/workers/vite-plugin/"><strong>Cloudflare Vite plugin</strong></a>, and the <code>@cloudflare/vitest-plugin</code> package. You can configure remote bindings by setting <code>remote: true</code> in the binding definition.</p>
<h3 id="example-configuration">Example configuration</h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16277.md")
</div>
<p>When remote bindings are configured, your Worker still <strong>executes locally</strong>, only the underlying resources your bindings connect to change. For all bindings marked with <code>remote: true</code>, Miniflare will route its operations (such as <code>env.MY_KV.put()</code>) to the deployed resource. All other bindings not explicitly configured with <code>remote: true</code> continue to use their default local simulations.</p>
<h3 id="integration-with-environments">Integration with environments</h3>
<p>Remote Bindings work well together with <a href="/workers/wrangler/environments">Workers Environments</a>. To protect production data, you can create a development or staging environment and specify different resources in your <a href="/workers/wrangler/configuration/">Wrangler configuration</a> than you would use for production.</p>
<p><strong>For example:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16278.md")
</div>
<p>Running <code>wrangler dev -e staging</code> (or <code>CLOUDFLARE_ENV=staging vite dev</code>) with the above configuration means that:</p>
<ul>
<li>Your Worker code runs locally</li>
<li>All calls made to <code>env.screenshots_bucket</code> will use the <code>preview-screenshots-bucket</code> resource, rather than the production <code>screenshots-bucket</code>.</li>
</ul>
<h3 id="recommended-remote-bindings">Recommended remote bindings</h3>
<p>We recommend configuring specific bindings to connect to their remote counterparts. These services often rely on Cloudflare's network infrastructure or have complex backends that are not fully simulated locally.</p>
<p>The following bindings are recommended to have <code>remote: true</code> in your Wrangler configuration:</p>
<h4 id="browser-run-workers-wrangler-configuration-browser-run"><a href="/workers/wrangler/configuration/#browser-run">Browser Run</a>:</h4>
<p>To interact with a real headless browser for rendering. There is no current local simulation for Browser Run.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16279.md")
</div>
<h4 id="workers-ai-workers-wrangler-configuration-workers-ai"><a href="/workers/wrangler/configuration/#workers-ai">Workers AI</a>:</h4>
<p>To utilize actual AI models deployed on Cloudflare's network for inference. There is no current local simulation for Workers AI.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16280.md")
</div>
<h4 id="vectorize-workers-wrangler-configuration-vectorize-indexes"><a href="/workers/wrangler/configuration/#vectorize-indexes">Vectorize</a>:</h4>
<p>To connect to your production Vectorize indexes for accurate vector search and similarity operations. There is no current local simulation for Vectorize.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16281.md")
</div>
<h4 id="mtls-workers-wrangler-configuration-mtls-certificates"><a href="/workers/wrangler/configuration/#mtls-certificates">mTLS</a>:</h4>
<p>To verify that the certificate exchange and validation process work as expected. There is no current local simulation for mTLS bindings.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16282.md")
</div>
<h4 id="images-workers-wrangler-configuration-images"><a href="/workers/wrangler/configuration/#images">Images</a>:</h4>
<p>To connect to a high-fidelity version of the Images API, and verify that all transformations work as expected. Local simulation for Cloudflare Images is <a href="/images/optimization/binding/#interact-with-your-images-binding-locally">limited with only a subset of features</a>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16283.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16276.md")
</aside>
<h4 id="dispatch-namespaces-cloudflare-for-platforms-workers-for-platforms-reference-local-development"><a href="/cloudflare-for-platforms/workers-for-platforms/reference/local-development/">Dispatch Namespaces</a>:</h4>
<p>Workers for Platforms users can configure <code>remote: true</code> in dispatch namespace binding definitions:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16284.md")
</div>
<p>This allows you to run your <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dynamic dispatch Worker</a> locally, while connecting it to your remote dispatch namespace binding. This allows you to test changes to your core dispatching logic against real, deployed <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers">user Workers</a>.</p>
<h3 id="unsupported-remote-bindings">Unsupported remote bindings</h3>
<p>Certain bindings are not supported for remote connections (i.e. with <code>remote: true</code>) during local development. These will always use local simulations or local values.</p>
<p>If <code>remote: true</code> is specified in Wrangler configuration for any of the following unsupported binding types, Cloudflare <strong>will issue an error</strong>. See <a href="/workers/local-development/bindings-per-env/">all supported and unsupported bindings for remote bindings</a>.</p>
<ul>
<li>
<p><a href="/workers/wrangler/configuration/#durable-objects"><strong>Durable Objects</strong></a>: Enabling remote connections for Durable Objects may be supported in the future, but currently will always run locally. However, using Durable Objects in combination with remote bindings is possible. Refer to <a href="#using-remote-resources-with-durable-objects-and-workflows">Using remote resources with Durable Objects and Workflows</a> below.</p>
</li>
<li>
<p><a href="/workflows/"><strong>Workflows</strong></a>: Enabling remote connections for Workflows may be supported in the future, but currently will only run locally. However, using Workflows in combination with remote bindings is possible. Refer to <a href="#using-remote-resources-with-durable-objects-and-workflows">Using remote resources with Durable Objects and Workflows</a> below.</p>
</li>
<li>
<p><a href="/workers/wrangler/configuration/#environment-variables"><strong>Environment Variables (<code>vars</code>)</strong></a>: Environment variables are intended to be distinct between local development and deployed environments. They are easily configurable locally (such as in a <code>.dev.vars</code> file or directly in Wrangler configuration).</p>
</li>
<li>
<p><a href="/workers/wrangler/configuration/#secrets"><strong>Secrets</strong></a>: Like environment variables, secrets are expected to have different values in local development versus deployed environments for security reasons. Use <code>.dev.vars</code> for local secret management.</p>
</li>
<li>
<p><a href="/workers/wrangler/configuration/#assets"><strong>Static Assets</strong></a> Static assets are always served from your local disk during development for speed and direct feedback on changes.</p>
</li>
<li>
<p><a href="/workers/runtime-apis/bindings/version-metadata/"><strong>Version Metadata</strong></a>: Since your Worker code is running locally, version metadata (like commit hash, version tags) associated with a specific deployed version is not applicable or accurate.</p>
</li>
<li>
<p><a href="/analytics/analytics-engine/"><strong>Analytics Engine</strong></a>: Local development sessions typically don't contribute data directly to production Analytics Engine.</p>
</li>
<li>
<p><a href="/workers/wrangler/configuration/#hyperdrive"><strong>Hyperdrive</strong></a>: This is being actively worked on, but is currently unsupported.</p>
</li>
<li>
<p><a href="/workers/runtime-apis/bindings/rate-limit/#configuration"><strong>Rate Limiting</strong></a>: Local development sessions typically should not share or affect rate limits of your deployed Workers. Rate limiting logic should be tested against local simulations.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16275.md")
</aside>
<h4 id="using-remote-resources-with-durable-objects-and-workflows">Using remote resources with Durable Objects and Workflows</h4>
<p>While Durable Object and Workflow bindings cannot currently be remote, you can still use them during local development and have them interact with remote resources.</p>
<p>There are two recommended patterns for this:</p>
<ul>
<li>
<p><strong>Local Durable Objects/Workflows with remote bindings:</strong></p>
<p>When you enable remote bindings in your <a href="/workers/wrangler/configuration">Wrangler configuration</a>, your locally running Durable Objects and Workflows can access remote resources. This allows such bindings, although run locally, to interact with remote resources during local development.</p>
</li>
<li>
<p><strong>Accessing remote Durable Objects/Workflows via service bindings:</strong></p>
<p>To interact with remote Durable Object or Workflow instances, deploy a Worker that defines those. Then, in your local Worker, configure a remote <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> pointing to the deployed Worker.
Your local Worker will be then able to interact with the remote deployed Worker, which in turn can communicate with the remote Durable Objects/Workflows. Using this method, you can create a communication channel via the remote service binding, effectively using the deployed Worker as a proxy interface to the remote bindings during local development.</p>
</li>
</ul>
<h3 id="important-considerations">Important Considerations</h3>
<ul>
<li>
<p><a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>: If your Worker is protected by Cloudflare Access, Wrangler must authenticate with Access when connecting to remote bindings. Refer to <a href="#connect-to-access-protected-workers">Connect to Access-protected Workers</a>.</p>
</li>
<li>
<p><strong>Data modification</strong>: Operations (writes, deletes, updates) on bindings connected remotely will affect your actual data in the targeted Cloudflare resource (be it preview or production).</p>
</li>
<li>
<p><strong>Billing</strong>: Interactions with remote Cloudflare services through these connections will incur standard operational costs for those services (such as KV operations, R2 storage/operations, AI requests, D1 usage).</p>
</li>
<li>
<p><strong>Network latency</strong>: Expect network latency for operations on these remotely connected bindings, as they involve communication over the internet.</p>
</li>
</ul>
<h3 id="connect-to-access-protected-workers">Connect to Access-protected Workers</h3>
<p>If your Worker is protected by <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>, Wrangler must authenticate with Access when connecting to your remote bindings. This applies whether Access protects the Worker itself, all Workers in the account, a <code>workers.dev</code> hostname, a Custom Domain, or another hostname or path that routes to the Worker.</p>
<p>There are two ways you can authenticate against Access:</p>
<ul>
<li>
<p><strong>Interactive login</strong> (local development): If you have a policy defined that accepts user login, then Wrangler launches the interactive <code>cloudflared access login</code> flow in your browser. No additional setup is required beyond being signed in to the correct account. If the policy only allows service token authentication, Wrangler will skip the interactive flow and throw an error indicating that service token credentials are required.</p>
</li>
<li>
<p><strong>Service token</strong> (CI / non-interactive environments): In CI/CD pipelines and other non-interactive contexts, or where the policy only allows service token authentication, Wrangler cannot trigger the interactive flow via the browser. Authentication must be via a <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Cloudflare Access service token</a> instead. If you do not configure a service token in a non-interactive environment, Wrangler will throw an error rather than attempting the interactive flow.</p>
</li>
</ul>
<p>To set up service token authentication:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16285.md")
</div>
<h3 id="api">API</h3>
<p>Wrangler provides programmatic utilities to help tooling authors support remote binding connections when running Workers code with <a href="/workers/testing/miniflare/">Miniflare</a>.</p>
<p><strong>Key APIs include:</strong></p>
<ul>
<li><a href="#startRemoteProxySession"><code>startRemoteProxySession</code></a>: Starts a proxy session that allows interaction with remote bindings.</li>
<li><a href="#unstable_convertconfigbindingstostartworkerbindings"><code>unstable_convertConfigBindingsToStartWorkerBindings</code></a>: Utility for converting binding definitions.</li>
<li><a href="#experimental_maybestartorupdatemixedmodesession"><code>experimental_maybeStartOrUpdateProxySession</code></a>: Convenience function to easily start or update a proxy session.</li>
</ul>
<h4 id="startremoteproxysession"><code>startRemoteProxySession</code></h4>
<p>This function starts a proxy session for a given set of bindings. It accepts options to control session behavior, including an <code>auth</code> option with your Cloudflare account ID and API token for remote binding access.</p>
<p>It returns an object with:</p>
<ul>
<li><code>ready</code> <span class="nb-type">Promise&lt;void&gt;</span>: Resolves when the session is ready.</li>
<li><code>dispose</code> <span class="nb-type">() =&gt; Promise&lt;void&gt;</span>: Stops the session.</li>
<li><code>updateBindings</code> <span class="nb-type">(bindings: StartDevWorkerInput['bindings']) =&gt; Promise&lt;void&gt;</span>: Updates session bindings.</li>
<li><code>remoteProxyConnectionString</code> <span class="nb-type">remoteProxyConnectionString</span>: String to pass to Miniflare for remote binding access.</li>
</ul>
<h4 id="unstable-convertconfigbindingstostartworkerbindings"><code>unstable_convertConfigBindingsToStartWorkerBindings</code></h4>
<p>The <code>unstable_readConfig</code> utility returns an <code>Unstable_Config</code> object which includes the definition of the bindings included in the configuration file. These bindings definitions
are however not directly compatible with <code>startRemoteProxySession</code>. It can be quite convenient to however read the binding declarations with <code>unstable_readConfig</code> and then
pass them to <code>startRemoteProxySession</code>, so for this wrangler exposes <code>unstable_convertConfigBindingsToStartWorkerBindings</code> which is a simple utility to convert
the bindings in an <code>Unstable_Config</code> object into a structure that can be passed to <code>startRemoteProxySession</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16273.md")
</aside>
<h4 id="maybestartorupdateremoteproxysession"><code>maybeStartOrUpdateRemoteProxySession</code></h4>
<p>This wrapper simplifies proxy session management. It takes:</p>
<ul>
<li>An object that contains either:
<ul>
<li>the path to a Wrangler configuration and a potential target environment</li>
<li>the name of the Worker and the bindings it is using</li>
</ul>
</li>
<li>The current proxy session details (this parameter can be set to <code>null</code> or not being provided if none).</li>
<li>Potentially the auth data to use for the remote proxy session.</li>
</ul>
<p>It returns an object with the proxy session details if started or updated, or <code>null</code> if no proxy session is needed.</p>
<p>The function:</p>
<ul>
<li>Based on the first argument prepares the input arguments for the proxy session.</li>
<li>If there are no remote bindings to be used (nor a pre-existing proxy session) it returns null, signaling that no proxy session is needed.</li>
<li>If the details of an existing proxy session have been provided it updates the proxy session accordingly.</li>
<li>Otherwise if starts a new proxy session.</li>
<li>Returns the proxy session details (that can later be passed as the second argument to <code>maybeStartOrUpdateRemoteProxySession</code>).</li>
</ul>
<h4 id="example">Example</h4>
<p>Here's a basic example of using Miniflare with <code>maybeStartOrUpdateRemoteProxySession</code> to provide a local dev session with remote bindings. This example uses a single hardcoded KV binding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/16286.md")
</div>
<h2 id="wrangler-dev-remote-legacy"><code>wrangler dev --remote</code> (Legacy)</h2>
<p>Separate from Miniflare-powered local development, Wrangler also offers a fully remote development mode via <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev --remote</code></a>. Remote development is <a href="/workers/local-development/wrangler-vs-vite/"><strong>not</strong> supported in the Vite plugin</a>.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx wrangler dev --remote</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx wrangler dev --remote" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn wrangler dev --remote</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn wrangler dev --remote" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm wrangler dev --remote</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm wrangler dev --remote" aria-label="Copy to clipboard">Copy</button></div></div>
<p>During <strong>remote development</strong>, all of your Worker code is uploaded to a temporary preview environment on Cloudflare's infrastructure, and changes to your code are automatically uploaded as you save.</p>
<p>When using remote development, all bindings automatically connect to their remote resources. Unlike local development, you cannot configure bindings to use local simulations - they will always use the deployed resources on Cloudflare's network.</p>
<h3 id="when-to-use-remote-development">When to use Remote development</h3>
<ul>
<li>For most development tasks, the most efficient and productive experience will be local development along with <a href="/workers/local-development/#remote-bindings">remote bindings</a> when needed.</li>
<li>You may want to use <code>wrangler dev --remote</code> for testing features or behaviors that are highly specific to Cloudflare's network and cannot be adequately simulated locally or tested via remote bindings.</li>
</ul>
<h3 id="considerations">Considerations</h3>
<ul>
<li>Iteration is significantly slower than local development due to the upload/deployment step for each change.</li>
</ul>
<h3 id="limitations">Limitations</h3>
<ul>
<li>When you run a remote development session using the <code>--remote</code> flag, a limit of 50 <a href="/workers/configuration/routing/routes/">routes</a> per zone is enforced. Learn more in<a href="/workers/platform/limits/#routes-and-domains-when-using-wrangler-dev---remote"> Workers platform limits</a>.</li>
</ul>
