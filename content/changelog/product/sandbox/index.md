<h1 id="changelog">Changelog</h1>

<h2 id="run-cursor-cloud-agents-on-cloudflare-via-self-hosted-machines"><a href="/changelog/post/2026-09-02-cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a></h2>
<p><em>2026-09-02</em></p>
<p><a href="https://cursor.com/docs/cloud-agent/self-hosted">Cursor self-hosted machines</a> let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by <a href="/containers/">Cloudflare Containers</a>.</p>
<p><img src="/assets/upstream/images/changelog/sandbox/cursor-cloud-agents-self-hosted-pool.png" alt="Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool" /></p>
<p>Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source <a href="https://github.com/anysphere/cloudflare-workers">Cursor Cloudflare Workers template</a> deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a>.</p>


<h2 id="sandbox-sdk-1-0-preview-on-next"><a href="/changelog/post/2026-08-07-sandbox-sdk-1-0-preview/">Sandbox SDK 1.0 preview on @next</a></h2>
<p><em>2026-08-07</em></p>
<p><strong>Sandbox SDK 1.0</strong> is available to preview under the npm <code>@next</code> tag. For existing applications, the current stable package remains published on the 0.12.x line.</p>
<p>Sandbox SDK first shipped to provide a rich library for running untrusted and agent-driven work on <a href="/containers/">Cloudflare Containers</a>. Since then, both Sandbox and Containers have matured. This preview is a thinner SDK built on a richer Cloudflare Containers foundation.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="2026-08-07-sandbox-sdk-1-0-preview-what-this-preview-is">What this preview is</h4>
<ul>
<li><strong>A single execution interface</strong> — <code>sandbox.exec()</code> takes an argument list, returns when the process <strong>starts</strong>, and gives you a handle for output, logs, waits, and signals. Both short commands and long-running services use the same API.</li>
<li><strong>Removed session execution</strong> — the SDK no longer maintains shell state between executions. Each launch is independent. Pass <code>cwd</code> and <code>env</code> when you need them, or put multi-step shell syntax in one explicit shell command.</li>
<li><strong>RPC as the only transport</strong> — the SDK talks to the container exclusively over RPC. Remove <code>SANDBOX_TRANSPORT</code>, <code>transport</code> on <code>getSandbox()</code>, and <code>setTransport()</code>.</li>
<li><strong>Improved PTY and terminal interface</strong> — interactive PTYs use <code>createTerminal</code> / <code>connect</code>, not the older session-shaped helpers.</li>
<li><strong>Code interpreter as an extension</strong> — configure the code interpreter on your <code>Sandbox</code> subclass so you only ship what you need.</li>
</ul>
<p>Start new projects on <code>@next</code>. Migrate existing apps when you can so you are ready when 1.0 becomes stable. Deploy the Worker package and container image from the <strong>same</strong> <code>@next</code> line.</p>
<p>Coding agents: install <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a> (<a href="/agent-setup/">Agent setup</a>). Use <strong><code>sandbox-next</code></strong> for <code>@next</code> (recommended for new projects), <strong><code>sandbox-stable</code></strong> for the current stable package, and <strong><code>sandbox-migrate-to-next</code></strong> when you are ready to port. Stable-package deprecated-API cleanup is in the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation guide</a>.</p>
<p>The main <a href="/sandbox/">Sandbox documentation</a> still describes today's stable package. Preview docs:</p>
<ul>
<li><a href="/sandbox/1-0-preview/">1.0 preview</a></li>
<li><a href="/sandbox/1-0-preview/get-started/">Get started</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Processes</a> · <a href="/sandbox/1-0-preview/terminals/">Terminals</a> · <a href="/sandbox/1-0-preview/errors/">Errors</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
</ul>
<p>The self-deployed Sandbox bridge is not currently part of this preview. We are working on bringing it in line with the latest code. Until then, use the <a href="/sandbox/bridge/">stable bridge</a> with the matching stable package and container image.</p>
<h4 id="2026-08-07-sandbox-sdk-1-0-preview-timeline-for-1-0">Timeline for 1.0</h4>
<p>Further Cloudflare Containers features will let us keep reducing the size of the Sandbox SDK. We aim to ship Sandbox SDK 1.0 once those are in. In the meantime we continue to support and maintain the 1.0 preview (<code>@next</code>) alongside the current stable release.</p>


<h2 id="run-devin-on-cloudflare-using-devin-outposts"><a href="/changelog/post/2026-07-21-devin-outposts/">Run Devin on Cloudflare using Devin Outposts</a></h2>
<p><em>2026-07-21</em></p>
<p><a href="https://docs.devin.ai/onboard-devin/outposts">Devin Outposts</a> lets you run Devin agents on Cloudflare. Each Devin session runs in its own isolated sandbox backed by <a href="/containers/">Cloudflare Containers</a>, so agents can execute code and use development tooling in an isolated environment.</p>
<p>Use Devin Outposts when you want Devin sessions to run on Cloudflare managed infrastructure, with each session isolated from the others.</p>
<p><img src="/assets/upstream/images/changelog/sandbox/devin-outposts.jpg" alt="Devin interface showing Cloudflare selected as an Outposts virtual environment" /></p>
<p>To get started, refer to <a href="/sandbox/tutorials/devin-outposts/">Run Devin on Cloudflare using Devin Outposts</a>.</p>


<h2 id="deprecating-sandbox-sdk-features"><a href="/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/">Deprecating Sandbox SDK features</a></h2>
<p><em>2026-06-09</em></p>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2026-06-09-deprecating-sandbox-sdk-features-sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h4>
@markup("md", "content/.markup/bodies/17752.md")</aside>
<p>Today we are announcing the deprecation of several features from the Sandbox SDK. The SDK has grown and matured substantially since it first launched. As agent workflows have developed, we have shipped many new features and experiments so developers can easily integrate secure, isolated code execution into their workflows.</p>
<p>We want the SDK to continue providing a stable foundation for agentic workflows while we iterate quickly on the codebase. These deprecated features have either been superseded by newer capabilities or seen low adoption. Do not build new work on them. Migrate using the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration guide</a>, or move to the <a href="/sandbox/1-0-preview/">Sandbox SDK 1.0 preview</a> when you can.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-http-and-websocket-transports">HTTP and WebSocket transports</h4>
<p>In April 2026, we released the new RPC transport and deprecated the WebSocket transport. This setting governs how the sandbox container talks to the Workers ecosystem. The RPC transport removes the limitations of both the HTTP and WebSocket transports. As of this announcement, RPC is the recommended default. HTTP and WebSocket transports are deprecated and will not ship in future Sandbox SDK majors.</p>
<p>To migrate, update the <code>SANDBOX_TRANSPORT</code> variable to <code>rpc</code> or set the <code>transport</code> option when calling <code>getSandbox()</code>. For more information, refer to the <a href="/sandbox/configuration/transport/">transport configuration documentation</a>.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-desktop">Desktop</h4>
<p>The desktop feature ran a full Linux desktop inside the sandbox (display server, desktop environment, and VNC/noVNC) so agents and apps could drive a GUI with screenshots, mouse, and keyboard — the same <em>computer-use</em> shape other sandbox products expose for UI automation. Adoption stayed low, and we removed it in <code>0.10.2</code>. If you need that capability again, you can build it on top of the sandbox with <a href="/sandbox/1-0-preview/extensions/">extensions</a> rather than a built-in <code>sandbox.desktop</code> API.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-expose-ports">Expose ports</h4>
<p>We recently released support for Cloudflare Tunnel in the Sandbox SDK. This provides a robust API for exposing services running in your sandbox to the public internet. It fixes issues many were facing with local development and deployment to <code>workers.dev</code> domains. To migrate from <code>exposePort()</code> to tunnels, refer to the <a href="/sandbox/api/tunnels/">tunnels API documentation</a> and the <a href="/sandbox/guides/expose-services/">expose services guide</a>.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-default-sessions">Default sessions</h4>
<p>By default, the <code>exec()</code> method in the Sandbox SDK maintains a default session across all calls, so a <code>cd</code> in one call is honored in the next. This convenience helped developers writing <code>exec</code> statements by hand, but confused agents and caused hard-to-trace bugs. As of <code>0.10.3</code>, we have introduced the <a href="/sandbox/configuration/sandbox-options/"><code>enableDefaultSession</code></a> flag on the <code>getSandbox()</code> interface to turn this off. Default sessions as a concept — and the flag — will be removed in an upcoming release.</p>
<p>We recommend setting <code>enableDefaultSession: false</code> today and using the <a href="/sandbox/api/sessions/"><code>sandbox.createSession()</code> API</a> when you need the previous behavior.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-other-changes">Other changes</h4>
<p>We are also consolidating all APIs that buffer data to support streaming by default. This includes <a href="/sandbox/api/files/"><code>readFile</code>, <code>writeFile</code></a>, and <a href="/sandbox/api/commands/"><code>exec</code></a>. The stream equivalents will be removed.</p>
<p>We are exploring moving non-core features like the <a href="/sandbox/guides/code-execution/">code interpreter</a>, <a href="/sandbox/api/terminal/">terminal</a>, and <a href="/sandbox/guides/git-workflows/">git APIs</a> into helpers. These features will retain their existing APIs, so migration should be simple.</p>
<h4 id="2026-06-09-deprecating-sandbox-sdk-features-next-steps">Next steps</h4>
<p>If you use any of these features on the <strong>current stable</strong> package, refer to the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration guide</a>. Coding agents can use the <strong><code>sandbox-stable</code></strong> skill for stable-package work and that guide for cleanup (<a href="/agent-setup/">Agent setup</a> · <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a>).</p>
<p>If you are moving to <strong>Sandbox SDK 1.0</strong> (<code>@next</code>), use the <a href="/sandbox/1-0-preview/">1.0 preview</a> and <a href="/sandbox/1-0-preview/migrate/">Migrate</a> guides instead — or the <strong><code>sandbox-migrate-to-next</code></strong> skill after installing Cloudflare Skills. New projects should prefer <strong><code>sandbox-next</code></strong> on <code>@next</code>.</p>
<p>For any questions, ask in the <a href="https://discord.gg/cloudflaredev">Cloudflare Developers Discord</a>.</p>



