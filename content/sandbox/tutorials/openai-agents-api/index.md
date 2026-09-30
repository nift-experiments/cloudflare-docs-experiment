<p><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">OpenAI Agents API</a> gives your application access to the Codex harness through an OpenAI-managed API. OpenAI manages sessions, orchestration, context compaction, and recovery while your application provides tools and Cloudflare Containers can provide the execution environment.</p>
<p>Run self-hosted OpenAI Agents API sessions in Cloudflare Containers. Each session has a Durable Object backed by a container running <code>codex exec-server</code>. Signed OpenAI webhooks manage session orchestration.</p>
<p><img src="/assets/upstream/images/sandbox/openai-agents-api-arch.jpg" alt="Architecture showing an application creating an OpenAI task, webhooks starting a Cloudflare container, and the application fetching the result" /></p>
<p>The <a href="https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api">Cloudflare executor template</a> includes the worker and container image used in this guide.</p>
<h2 id="how-it-works">How it works</h2>
<ul>
<li><strong>Cloudflare Worker:</strong> Receives signed OpenAI webhooks and manages one container for each agent session.</li>
<li><strong>Cloudflare Container:</strong> Runs <code>codex exec-server</code> and agent-generated code against files in <code>/workspace</code>.</li>
<li><strong>Codex executor:</strong> Connects outbound to OpenAI with a restricted API key while the workspace remains in your Cloudflare account.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need:</p>
<ul>
<li>A Cloudflare account with Containers access</li>
<li>OpenAI Agents API access and an OpenAI API key</li>
<li>curl</li>
<li>For manual deployment, Node.js 24 or newer, npm, <a href="https://www.docker.com/">Docker</a>, and Wrangler</li>
</ul>
<p>Create a restricted OpenAI API key, referred to in this guide as the &quot;executor key&quot;, for use by <code>codex exec-server</code>. It requires <code>api.model.read</code> and <code>api.agents.environments.connect</code>. The application key used by the Worker requires <code>api.agents.read</code>. Both keys must belong to the same organization, project, and user or service-account owner.</p>
<h2 id="quick-start">Quick start</h2>
<p>The quickest setup uses the <strong>Deploy to Cloudflare</strong> button. These steps create an OpenAI agent, deploy its execution environment, register the webhook, and run a test task in <code>/workspace</code>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13311.md")
</div>
<details class="nb-details"><summary>Deploy manually</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13313.md")
</div></details>
<details class="nb-details"><summary>Reconnect an existing session</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13314.md")
</div></details>
<h2 id="agents-api-on-cloudflare-workers">Agents API on Cloudflare Workers</h2>
<p>For a complete TypeScript application with an HTTP interface, refer to the <a href="https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api/basic">basic Agents API example</a> in the Cloudflare Sandbox SDK repository.</p>
<p>The example uses the OpenAI Agents API TypeScript SDK to create self-hosted sessions backed by the deployed executor Worker. It includes endpoints for initial input, follow-up input, and cleanup. Its <code>POST /demo</code> endpoint runs the complete workflow: create a session, write and read a file in the container, send a follow-up message, then delete the OpenAI session and Cloudflare executor.</p>
<h2 id="clean-up">Clean up</h2>
<p>Delete the OpenAI session:</p>
<pre><code class="language-bash">curl --request DELETE --url https://api.openai.com/v1/agents/sessions/$SESSION_ID</code></pre>
<p>To stop its Cloudflare Container immediately, use the shared secret saved during deployment:</p>
<pre><code class="language-bash">export WORKER_URL=&quot;https://&lt;YOUR_WORKER&gt;.workers.dev&quot;&#10;export EXECUTOR_CLIENT_SECRET=&quot;&lt;EXECUTOR_CLIENT_SECRET&gt;&quot;&#10;&#10;curl --fail-with-body \&#10;  &#45;-request DELETE \&#10;  &#45;-header &quot;Authorization: Bearer $EXECUTOR_CLIENT_SECRET&quot; \&#10;  &quot;$WORKER_URL/executors/$SESSION_ID&quot;&#10;</code></pre>
<p>Deleting an OpenAI session does not send a container cleanup webhook. Without explicit cleanup, an idle session keeps its snapshot for the next environment connection. A failed-session webhook or a session lookup that returns <code>404 Not Found</code> releases the container and clears its saved snapshot.</p>
<h2 id="execution-lifecycle">Execution lifecycle</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/13315.md")
</div>
<p><img src="/assets/upstream/images/sandbox/openai-agents-api-lifecycle.jpg" alt="Lifecycle showing an application creating an Agents API session, OpenAI sending webhooks to Cloudflare, and the container connecting its Codex executor to OpenAI" /></p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="failure-and-cleanup">Failure and cleanup</h3>
@markup("md", "content/.markup/bodies/13310.md")
</aside>
<h3 id="workspace-restoration">Workspace restoration</h3>
<p>Container snapshots are currently in private beta. If you would like to enable the feature on your Cloudflare account please contact your Cloudflare representative.</p>
<p>When <code>EXECUTOR_SNAPSHOTS_ENABLED</code> is <code>true</code>, a confirmed idle session creates a whole-container snapshot before its container stops. The next environment connection restores that snapshot, including <code>/workspace</code>. If snapshot creation fails, the Worker leaves the current container running and schedules another lifecycle check.</p>
<p>Snapshots are best-effort session recovery, not durable backup. Failed or deleted sessions and explicit cleanup clear the saved snapshot. When snapshots are disabled or unavailable, the next executor receives a fresh <code>/workspace</code>. For durable files, adapt the container image to use an <a href="/containers/examples/r2-fuse-mount/">R2 FUSE mount</a>.</p>
<h2 id="add-tools-to-the-container">Add tools to the container</h2>
<p>The executor image is defined in <code>openai/agents-api/Dockerfile</code> in the Cloudflare executor template. Add Debian packages to its existing <code>apt-get install</code> command. For example, add <code>jq</code> and Python:</p>
<pre><code class="language-text">RUN apt-get update \&#10;    &amp;&amp; apt-get install --yes --no-install-recommends \&#10;      ca-certificates \&#10;      curl \&#10;      git \&#10;      jq \&#10;      python3 \&#10;      ripgrep \&#10;    &amp;&amp; rm -rf /var/lib/apt/lists/*&#10;</code></pre>
<p>You can also install language-specific tools in the image, such as global npm packages. Do not store API keys or other secrets in the Dockerfile. Pass runtime secrets through Worker bindings or container environment variables.</p>
<p>Run <code>npm run deploy</code> from <code>openai/agents-api</code> to build and deploy the updated image.</p>
<h2 id="security-considerations">Security considerations</h2>
<p>The runnable example is intentionally minimal. Review these defaults before adapting it for production:</p>
<ul>
<li><strong>Secrets:</strong> The controller key, webhook secret, and <code>EXECUTOR_CLIENT_SECRET</code> remain Worker secrets. The restricted executor key is passed into the container as <code>CODEX_API_KEY</code>, where processes inside the container can read it. Refer to <a href="/containers/examples/env-vars-and-secrets/">Container environment variables and secrets</a> for other ways to configure container instances.</li>
<li><strong>Network access:</strong> The example enables outbound Internet access so <code>codex exec-server</code> can reach OpenAI. Use <a href="/containers/platform-details/outbound-traffic/">Container outbound traffic controls</a> to restrict destinations or inject credentials for other services.</li>
<li><strong>Files:</strong> <code>/workspace</code> uses ephemeral container storage. Use a <a href="/containers/examples/r2-fuse-mount/#mounting-buckets-as-read-only">read-only R2 FUSE mount</a> when an agent needs durable source files that it should not modify.</li>
<li><strong>Worker access:</strong> OpenAI must be able to reach <code>/webhook</code> without an interactive Access login. The Worker verifies OpenAI's webhook signature, and the manual cleanup endpoint requires <code>EXECUTOR_CLIENT_SECRET</code>. If you protect other routes with Cloudflare Access, use <a href="/cloudflare-one/access-controls/policies/app-paths/">path-specific policies</a> that leave <code>/webhook</code> reachable.</li>
</ul>
<p>For more information, refer to <a href="/containers/platform-details/architecture/">Containers architecture</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api">Cloudflare reference worker</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">OpenAI Agents API documentation</a></li>
<li><a href="https://github.com/OpenAI/agents-api-python-preview/tree/main/examples/self_hosted_sandbox/webhook_managed/cloudflare">OpenAI Python Cloudflare webhook example</a></li>
<li><a href="https://github.com/OpenAI/agents-api-typescript-preview/tree/main/examples/self_hosted_sandbox/webhook_managed/cloudflare">OpenAI TypeScript Cloudflare webhook example</a></li>
<li><a href="/containers/">Cloudflare Containers</a></li>
</ul>
