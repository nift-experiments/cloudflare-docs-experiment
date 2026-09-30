<p>This guide shows you how to start, monitor, and manage long-running background processes in the sandbox.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13505.md")
</aside>
<h2 id="when-to-use-background-processes">When to use background processes</h2>
<p>Use <code>startProcess()</code> instead of <code>exec()</code> when:</p>
<ul>
<li><strong>Running web servers</strong> - HTTP servers, APIs, WebSocket servers</li>
<li><strong>Long-running services</strong> - Database servers, caches, message queues</li>
<li><strong>Development servers</strong> - Hot-reloading dev servers, watch modes</li>
<li><strong>Continuous monitoring</strong> - Log watchers, health checkers</li>
<li><strong>Parallel execution</strong> - Multiple services running simultaneously</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13504.md")
</aside>
<h2 id="start-a-background-process">Start a background process</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13506.md")
</div>
<h2 id="configure-process-environment">Configure process environment</h2>
<p>Set working directory and environment variables:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13507.md")
</div>
<h2 id="monitor-process-status">Monitor process status</h2>
<p>List and check running processes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13508.md")
</div>
<h2 id="wait-for-process-readiness">Wait for process readiness</h2>
<p>Wait for a process to be ready before proceeding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13509.md")
</div>
<p>Or wait for specific log patterns:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13510.md")
</div>
<h2 id="monitor-process-logs">Monitor process logs</h2>
<p>Stream logs in real-time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13511.md")
</div>
<p>Or get accumulated logs:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13512.md")
</div>
<h2 id="stop-processes">Stop processes</h2>
<p>Stop background processes and their children:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13513.md")
</div>
<p><code>killProcess()</code> terminates the specified process and all child processes it spawned. This ensures that processes running in the background do not leave orphaned child processes when terminated.</p>
<p>For example, if your process spawns multiple worker processes or background tasks, <code>killProcess()</code> will clean up the entire process tree:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13514.md")
</div>
<h2 id="run-multiple-processes">Run multiple processes</h2>
<p>Start services in sequence, waiting for dependencies:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13515.md")
</div>
<h2 id="keep-containers-alive-for-long-running-processes">Keep containers alive for long-running processes</h2>
<p>By default, containers automatically shut down after 10 minutes of inactivity. For long-running processes that may have idle periods (like CI/CD pipelines, batch jobs, or monitoring tasks), use the <a href="/sandbox/configuration/sandbox-options/#keepalive"><code>keepAlive</code> option</a>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13516.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="always-destroy-with-keepalive">Always destroy with keepAlive</h3>
@markup("md", "content/.markup/bodies/13503.md")
</aside>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Wait for readiness</strong> - Use <code>waitForPort()</code> or <code>waitForLog()</code> to detect when services are ready</li>
<li><strong>Clean up</strong> - Always stop processes when done</li>
<li><strong>Handle failures</strong> - Monitor logs for errors and restart if needed</li>
<li><strong>Use try/finally</strong> - Ensure cleanup happens even on errors</li>
<li><strong>Use <code>keepAlive</code> for long-running tasks</strong> - Prevent container shutdown during processes with idle periods</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="process-exits-immediately">Process exits immediately</h3>
<p>Check logs to see why:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13517.md")
</div>
<h3 id="port-already-in-use">Port already in use</h3>
<p>Kill existing processes before starting:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13518.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/commands/">Commands API reference</a> - Complete process management API</li>
<li><a href="/sandbox/configuration/sandbox-options/">Sandbox options configuration</a> - Configure <code>keepAlive</code> and other options</li>
<li><a href="/sandbox/api/lifecycle/">Lifecycle API</a> - Create and manage sandboxes</li>
<li><a href="/sandbox/api/sessions/">Sessions API reference</a> - Create isolated execution contexts</li>
<li><a href="/sandbox/guides/execute-commands/">Execute commands guide</a> - One-time command execution</li>
<li><a href="/sandbox/guides/expose-services/">Expose services guide</a> - Make processes accessible</li>
<li><a href="/sandbox/guides/streaming-output/">Streaming output guide</a> - Monitor process output</li>
</ul>
