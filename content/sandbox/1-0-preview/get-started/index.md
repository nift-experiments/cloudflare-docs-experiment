<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13744.md")
</aside>
<h2 id="1-install-the-preview-package"><ol>
<li>Install the preview package</li>
</ol></h2>
<p>In a Workers project that already uses Sandbox, or a new project from the Sandbox template:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/sandbox@next</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/sandbox@next" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Build and deploy the Worker <strong>and</strong> the sandbox container image from the same preview line.</p>
<h2 id="2-export-your-sandbox-class"><ol start="2">
<li>Export your Sandbox class</li>
</ol></h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13745.md")
</div>
<p>Keep your <code>wrangler</code> Durable Object binding and container configuration. Preview-specific transport variables are not required.</p>
<h2 id="3-run-a-process"><ol start="3">
<li>Run a process</li>
</ol></h2>
<p><code>exec()</code> starts a program from <strong>argv</strong> — an array of the executable path or name, then its arguments. It waits until the sandbox can start the process, then returns a <strong>process handle</strong>. It does <strong>not</strong> wait for the process to exit.</p>
<p>Collect results with handle methods such as <code>output()</code>, or stream with <code>logs()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13746.md")
</div>
<p>Each argv entry is one argument to the process. The SDK does <strong>not</strong> run a shell and does <strong>not</strong> shell-escape argv. Spaces and special characters in an entry stay inside that argument.</p>
<p>Shell syntax (<code>&amp;&amp;</code>, pipes, redirects, globs) needs an explicit shell, with the script as its own argument:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13747.md")
</div>
<h2 id="4-how-this-differs-from-the-stable-package"><ol start="4">
<li>How this differs from the stable package</li>
</ol></h2>
<ul>
<li><code>await sandbox.exec(...)</code> creates a process. It does <strong>not</strong> wait for exit. Use <code>output()</code>, <code>waitForExit()</code>, or other handle methods for completion.</li>
<li>Each <code>exec()</code> is independent. A <code>cd</code> or <code>export</code> in one call is not remembered in the next.</li>
<li>Pass <code>cwd</code> and <code>env</code> on each <code>exec()</code> when you need them, or use <code>setEnvVars</code> for sandbox-wide values. Refer to <a href="/sandbox/1-0-preview/environment/">Environment variables</a>.</li>
<li>A process runs only in the <strong>current container</strong> for that sandbox. After the container stops or is replaced, start a new process. Model: <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a>.</li>
<li>Before production traffic, learn which failures are safe to retry: <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</li>
</ul>
<h2 id="next">Next</h2>
<ul>
<li><a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a> — sandbox ID, container, stop, and replace</li>
<li><a href="/sandbox/1-0-preview/processes/">Process execution</a> — <code>exec()</code>, handles, and continuing work across requests</li>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a> — retries, interrupted calls, and stale handles</li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a> — update an existing stable app</li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a> — processes, terminals, and errors</li>
<li><a href="/sandbox/1-0-preview/terminals/">Terminals</a> — interactive PTY and browser connections</li>
<li><a href="/sandbox/1-0-preview/extensions/">Extensions</a></li>
</ul>
