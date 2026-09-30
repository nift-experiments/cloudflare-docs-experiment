---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/1-0-preview/
  description: Install @cloudflare/sandbox@next — a thinner Sandbox SDK on Cloudflare Containers — and migrate when you are ready for Sandbox SDK 1.0.
  full_title: Overview · Cloudflare Sandbox SDK docs
  head_html: <title>Overview · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Install @cloudflare/sandbox@next — a thinner Sandbox SDK on Cloudflare Containers — and migrate when you are ready for Sandbox SDK 1.0."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/1-0-preview/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/1-0-preview/index.md"><meta property="og:title" content="Overview · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Install @cloudflare/sandbox@next — a thinner Sandbox SDK on Cloudflare Containers — and migrate when you are ready for Sandbox SDK 1.0."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/1-0-preview/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/sandbox/1-0-preview/#page","headline":"Overview \u00b7 Cloudflare Sandbox SDK docs","description":"Install @cloudflare/sandbox@next \u2014 a thinner Sandbox SDK on Cloudflare Containers \u2014 and migrate when you are ready for Sandbox SDK 1.0.","url":"https://developers.cloudflare.com/sandbox/1-0-preview/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/1-0-preview/
  schema: 1
---
<p><strong>Sandbox SDK 1.0</strong> is the next major release of the SDK. It is available now as a preview on the npm <code>@next</code> tag. The current stable package remains published for existing apps.</p>
<p>Sandbox still runs isolated work on <a href="/containers/">Cloudflare Containers</a>. The 1.0 preview is a <strong>thinner</strong> SDK on that foundation: one process handle for short and long-running work, no session-based command state, no transport picker, terminals as first-class PTYs, and the code interpreter as an opt-in extension.</p>
<p>We recommend that <strong>new projects</strong> start on <code>@cloudflare/sandbox@next</code> and follow this section. <strong>Existing apps</strong> should migrate when you can, so you are ready when 1.0 becomes the stable release. Follow <a href="/sandbox/1-0-preview/migrate/">Migrate</a>.</p>
<p>The main <a href="/sandbox/">Sandbox documentation</a> still documents today's stable package. Use <strong>this</strong> section for preview APIs and the migration path.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="self-deployed-bridge">Self-deployed bridge</h3>
@markup("md", "content/.markup/bodies/13729.md")
</aside>
<h2 id="install-the-preview">Install the preview</h2>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Deploy the Worker package and the sandbox container image from the <strong>same</strong> preview line. Do not mix a preview Worker package with a stable container image (or the reverse). For ongoing deploys, refer to <a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a>. For a breaking cutover, refer to <a href="/sandbox/1-0-preview/migrate/">Migrate</a>.</p>
<h2 id="what-1-0-is-aiming-at">What 1.0 is aiming at</h2>
<p>The stable package grew several ways to run commands (<code>exec</code>, <code>startProcess</code>, <code>execStream</code>), optional session state across launches, and selectable transports between the Durable Object and the container. That surface worked, but it duplicated ideas and hid how sandboxes actually behave on containers.</p>
<p>The preview collapses that toward a smaller contract:</p>
<table>
<thead>
<tr>
<th>You want…</th>
<th>In the preview</th>
</tr>
</thead>
<tbody>
<tr>
<td>Run a program</td>
<td><code>exec(argv)</code> → process handle when <strong>launch</strong> succeeds</td>
</tr>
<tr>
<td>See output or wait for readiness</td>
<td><code>output()</code>, <code>logs()</code>, <code>waitForExit()</code>, <code>waitForLog()</code>, <code>waitForPort()</code> on the handle</td>
</tr>
<tr>
<td>Stop a process</td>
<td><code>kill(signal?)</code> (numeric signal; default <code>15</code>)</td>
</tr>
<tr>
<td>Keep shell state across many interactive steps</td>
<td>A <a href="/sandbox/1-0-preview/terminals/">terminal</a> (PTY), not a hidden default session</td>
</tr>
<tr>
<td>Run Python / JS cells</td>
<td><a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a> extension on your <code>Sandbox</code> subclass</td>
</tr>
<tr>
<td>Talk to the container control plane</td>
<td>Always RPC — no transport setting</td>
</tr>
</tbody>
</table>
<p>Procedures: <a href="/sandbox/1-0-preview/migrate/">Migrate</a>. Mental model: <a href="/sandbox/1-0-preview/processes/">Process execution</a> and <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a>.</p>
<h2 id="what-changes-from-the-stable-package">What changes from the stable package</h2>
<h3 id="command-execution">Command execution</h3>
<p><strong>Stable:</strong> <code>sandbox.exec(string)</code> resolves when the command <strong>finishes</strong> with buffered output. Long-running services and streaming use separate APIs (<code>startProcess</code>, <code>execStream</code>).</p>
<p><strong>Preview:</strong> <code>sandbox.exec()</code> takes <strong>argv</strong> and resolves when the process <strong>starts</strong>. The same handle covers short commands and long-running services.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13730.md")
</div>
<p>Shell features such as pipes and <code>&amp;&amp;</code> need an explicit shell, for example <code>['/bin/bash', '-lc', 'cd app &amp;&amp; npm test']</code>. Pass <code>cwd</code> and <code>env</code> on each <code>exec()</code> when the process needs them. Details: <a href="/sandbox/1-0-preview/processes/">Process execution</a>, <a href="/sandbox/1-0-preview/api/processes/">Processes API</a>.</p>
<h3 id="sessions">Sessions</h3>
<p><strong>Stable:</strong> a default session can preserve working directory and environment variables across <code>exec()</code> calls. Apps can also create named sessions with <code>createSession()</code>.</p>
<p><strong>Preview:</strong> no session execution on the SDK. Each <code>exec()</code> is independent. Pass <code>cwd</code> and <code>env</code> on each launch, or put multi-step shell syntax in one explicit shell argv. Isolate end users with <strong>separate sandboxes</strong>, not sessions inside one sandbox. Environment model: <a href="/sandbox/1-0-preview/environment/">Environment variables</a>.</p>
<h3 id="terminals">Terminals</h3>
<p><strong>Stable:</strong> browser shells often use <code>sandbox.terminal(request)</code> with session helpers and xterm <code>sessionId</code>.</p>
<p><strong>Preview:</strong> terminals are PTY resources — <code>createTerminal</code>, <code>getTerminal</code>, <code>listTerminals</code>, and <code>terminal.connect(request)</code>. The xterm helper uses <code>terminalId</code>. Refer to <a href="/sandbox/1-0-preview/terminals/">Terminals</a>.</p>
<h3 id="code-interpreter">Code interpreter</h3>
<p><strong>Stable:</strong> interpreter methods live on <code>Sandbox</code>.</p>
<p><strong>Preview:</strong> attach the interpreter on your subclass, then call <code>sandbox.interpreter.*</code>. Refer to <a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a>.</p>
<h3 id="transport-configuration">Transport configuration</h3>
<p><strong>Stable:</strong> apps can select HTTP, WebSocket, or RPC between the Durable Object and the container.</p>
<p><strong>Preview:</strong> the SDK always uses RPC. Remove <code>SANDBOX_TRANSPORT</code>, the <code>transport</code> option on <code>getSandbox()</code>, and <code>setTransport()</code>. No replacement setting is required.</p>
<h2 id="same-platform-model-clearer-handles">Same platform model, clearer handles</h2>
<p>This is <strong>not</strong> a new container product. You still address a sandbox with a stable <strong>sandbox ID</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13731.md")
</div>
<p>That sandbox runs in a <strong>container</strong>. The ID is stable. The container instance behind it is not always the same one. Processes and terminals you start exist only in the <strong>current</strong> container. When that container stops or is replaced, those processes and terminals are gone — old handles fail closed instead of quietly attaching to a new container for the same sandbox ID.</p>
<p>Container stop and replace already happened on the stable line. The preview makes process and terminal APIs honest about that lifetime. Full model: <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a>. Process detail: <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>. Recovery: <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<h2 id="what-usually-stays-the-same">What usually stays the same</h2>
<p>These remain available. Use the main Sandbox documentation for signatures, and ignore session or transport options where those pages still mention them:</p>
<ul>
<li><a href="/sandbox/api/files/">Files</a> and <a href="/sandbox/api/file-watching/">file watching</a></li>
<li><a href="/sandbox/api/storage/">Storage</a> and <a href="/sandbox/api/backups/">backups</a></li>
<li><a href="/sandbox/api/ports/">Ports</a> and <a href="/sandbox/api/tunnels/">tunnels</a></li>
<li><a href="/sandbox/api/lifecycle/">Lifecycle options</a> and <a href="/sandbox/configuration/sandbox-options/">sandbox options</a> (except removed session/transport fields)</li>
<li><a href="/sandbox/guides/outbound-traffic/">Outbound traffic</a> (credential injection and egress policy)</li>
</ul>
<p>For process environment on <code>@next</code>, use <a href="/sandbox/1-0-preview/environment/">Environment variables</a> in this section.</p>
<h2 id="start-here">Start here</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/13743.md")
</div>
<h2 id="coding-agents">Coding agents</h2>
<p>Install <a href="https://github.com/cloudflare/skills">Cloudflare Skills</a> for your agent (<a href="/agent-setup/">Agent setup</a>). Use <strong><code>sandbox-next</code></strong> for work on <code>@next</code> (recommended for new projects). Existing apps on the current stable package should use <strong><code>sandbox-stable</code></strong> until you are ready to move, then <strong><code>sandbox-migrate-to-next</code></strong>. Deprecated-API cleanup while staying on stable is covered in the <a href="/sandbox/guides/2026-deprecation/">2026 deprecation guide</a> and <strong><code>sandbox-stable</code></strong>.</p>
<h2 id="stable-documentation">Stable documentation</h2>
<p>While you remain on the current stable package, use the main docs:</p>
<ul>
<li><a href="/sandbox/get-started/">Get started</a></li>
<li><a href="/sandbox/api/commands/">Commands</a></li>
<li><a href="/sandbox/concepts/sessions/">Sessions</a></li>
<li><a href="/sandbox/guides/2026-deprecation/">2026 deprecation migration</a></li>
</ul>
