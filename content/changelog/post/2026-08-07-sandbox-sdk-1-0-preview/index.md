<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 7, 2026</time><h2 id="post-title">Sandbox SDK 1.0 preview on @next</h2>
<div class="changelog-badges"><span>sandbox</span></div><div class="changelog-body"><p><strong>Sandbox SDK 1.0</strong> is available to preview under the npm <code>@next</code> tag. For existing applications, the current stable package remains published on the 0.12.x line.</p>
<p>Sandbox SDK first shipped to provide a rich library for running untrusted and agent-driven work on <a href="/containers/">Cloudflare Containers</a>. Since then, both Sandbox and Containers have matured. This preview is a thinner SDK built on a richer Cloudflare Containers foundation.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="what-this-preview-is">What this preview is</h4>
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
<h4 id="timeline-for-1-0">Timeline for 1.0</h4>
<p>Further Cloudflare Containers features will let us keep reducing the size of the Sandbox SDK. We aim to ship Sandbox SDK 1.0 once those are in. In the meantime we continue to support and maintain the 1.0 preview (<code>@next</code>) alongside the current stable release.</p>
</div></article></div>
