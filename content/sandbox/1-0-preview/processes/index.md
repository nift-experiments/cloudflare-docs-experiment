<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13710.md")
</aside>
<p>In the 1.0 preview, treat the sandbox as a computer you drive with explicit programs.</p>
<p>Each <code>exec()</code> starts a <strong>new supervised process</strong> from <strong>argv</strong>. The call resolves when launch succeeds (you receive a process handle with <code>id</code> and <code>pid</code> properties), not when the process exits. Each launch is independent: pass <code>cwd</code> and <code>env</code> when the process needs them, or put multi-step shell syntax in one explicit shell argv. For an interactive PTY, use the <a href="/sandbox/1-0-preview/terminals/">terminal</a> API.</p>
<p>Long-running work often spans many short Worker requests. A process ID is enough only while the <strong>same container</strong> still has that process. Across idle stop, failure, or replace, store the full launch (command, options, and any app checkpoint) so you can start again. Refer to <a href="#continue-work-across-requests">Continue work across requests</a>.</p>
<h2 id="sandbox-id-container-and-process">Sandbox ID, container, and process</h2>
<p>Most applications use <strong>one sandbox per user or task</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13711.md")
</div>
<p>Three different things are in play:</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Sandbox ID</strong></td>
<td>The stable string your app uses to find that sandbox again (for example <code>&quot;user-123&quot;</code>).</td>
</tr>
<tr>
<td><strong>Container</strong></td>
<td>The <a href="/containers/">Containers</a> instance currently running work for that sandbox. Sandboxes run on containers. The sandbox ID is stable. The container instance behind it is not always the same one.</td>
</tr>
<tr>
<td><strong>Process</strong></td>
<td>A program you start with <code>exec()</code> <strong>inside the current container</strong>. The handle and <code>process.id</code> mean “this program in this container,” not “this sandbox ID forever.”</td>
</tr>
</tbody>
</table>
<p><strong>Same sandbox ID does not mean the same container.</strong> Processes live only in the container that started them. After a new container serves that ID, start new processes — you do not resume the old ones. Full sandbox model: <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a>.</p>
<h2 id="command-model">Command model</h2>
<p>The command model changes in the 1.0 preview compared with the current stable package:</p>
<table>
<thead>
<tr>
<th>Current stable package</th>
<th>1.0 preview</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>exec(string)</code> resolves when the command finishes</td>
<td><code>exec(argv)</code> resolves when the process starts</td>
</tr>
<tr>
<td>Default session can preserve <code>cd</code> / <code>export</code></td>
<td>Each launch is independent</td>
</tr>
<tr>
<td><code>startProcess</code> / <code>execStream</code> for other shapes</td>
<td>One process handle covers short and long-running work</td>
</tr>
</tbody>
</table>
<p>Use argv for a single binary:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13712.md")
</div>
<p>Use an explicit shell when you need shell syntax:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13713.md")
</div>
<p>Or pass <code>cwd</code> and <code>env</code> on the launch instead of relying on a previous command:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13714.md")
</div>
<p>Sandbox-wide values use <code>setEnvVars</code>. Refer to <a href="/sandbox/1-0-preview/environment/">Environment variables</a>.</p>
<h2 id="process-handles">Process handles</h2>
<p><code>await sandbox.exec(argv)</code> returns a <strong>process handle</strong>:</p>
<table>
<thead>
<tr>
<th>Capability</th>
<th>Members</th>
</tr>
</thead>
<tbody>
<tr>
<td>Identity</td>
<td><code>id</code>, <code>pid</code></td>
</tr>
<tr>
<td>Observe</td>
<td><code>status()</code>, <code>logs()</code>, <code>output()</code>, <code>waitForExit()</code>, <code>waitForLog()</code>, <code>waitForPort()</code>, <code>exitCode</code></td>
</tr>
<tr>
<td>Control</td>
<td><code>kill(signal?)</code> with a numeric signal (default <code>15</code>)</td>
</tr>
</tbody>
</table>
<p>Observation timeouts and <code>AbortSignal</code> values cancel <strong>only that wait or stream</strong>. They do not stop the process. Call <code>kill()</code> when you intend to stop it.</p>
<p><code>exec(argv, { timeout })</code> sets a <strong>remote lifetime</strong> deadline. When the supervisor stops the process for that deadline, completion can report <code>timedOut: true</code>.</p>
<p>For short commands, <code>output()</code> is enough. For large or long-running output, prefer <code>logs({ since, replay, follow })</code> and keep the latest <strong>cursor</strong> so a later request can resume the stream while the process is still in the current container. API details: <a href="/sandbox/1-0-preview/api/processes/">Processes API</a>.</p>
<h2 id="how-long-a-process-lives">How long a process lives</h2>
<p>A process lives only as long as it keeps running <strong>in the current container</strong> for that sandbox. After the container stops, old process IDs are not valid on a later container that serves the same sandbox ID.</p>
<h3 id="when-the-container-stops">When the container stops</h3>
<p>The container for a sandbox is not meant to run forever. After a period with nothing to do, Cloudflare may stop it. The container can also stop after failures, or when the platform replaces it during normal operations (for example after some deploys).</p>
<p>When that happens:</p>
<ul>
<li>Your app still uses the same sandbox ID (<code>user-123</code>).</li>
<li>Processes that were running in the old container have exited. Their process IDs and live log buffers from that container are gone.</li>
<li>The next time you use the sandbox for real work, Cloudflare may start a <strong>new</strong> container for the same sandbox ID. You start new processes there. You do not reconnect to process IDs from the previous container. Files from the old container are not still there unless your app restored them (for example from a backup or a mounted bucket).</li>
</ul>
<p>Container stop and replace are not new in 1.0. The preview makes process handles fail closed after the container that owned them is gone: the SDK does not retarget an old process ID at a new container for the same sandbox ID.</p>
<h3 id="what-you-see-in-the-api">What you see in the API</h3>
<table>
<thead>
<tr>
<th>What you try</th>
<th>What happens</th>
</tr>
</thead>
<tbody>
<tr>
<td>The process is still running in the current container</td>
<td><code>getProcess(id)</code> returns it; you can read logs and wait as usual</td>
</tr>
<tr>
<td>No container is running for the sandbox yet</td>
<td><code>getProcess</code> and <code>listProcesses</code> return <code>null</code> / <code>[]</code>. They do <strong>not</strong> start a container just to answer the lookup</td>
</tr>
<tr>
<td>You still hold a handle from before the container stopped</td>
<td>Calls on that handle fail with <code>StaleProcessHandleError</code></td>
</tr>
<tr>
<td>You need the same <em>job</em> after a stop</td>
<td>Start a new <code>exec()</code> from the launch and checkpoint your app stored</td>
</tr>
</tbody>
</table>
<p>Recovery procedures: <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<h3 id="keep-the-container-running">Keep the container running</h3>
<p>While a process or terminal is active, the container can stay running so work continues across requests. When nothing is active, the container may stop again after idle time. Long-running product flows should either keep meaningful work active or rely on checkpoints and relaunch.</p>
<h2 id="continue-work-across-requests">Continue work across requests</h2>
<p>Worker requests are short. Sandbox processes often are not. Design the job so a later request can either <strong>resume the same process</strong> or <strong>start the job again</strong>.</p>
<h3 id="what-to-store">What to store</h3>
<table>
<thead>
<tr>
<th>Always useful</th>
<th>When you stream logs</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sandbox ID</td>
<td>Latest log <strong>cursor</strong> from delivered events</td>
</tr>
<tr>
<td>Full <code>exec</code> argv</td>
<td></td>
</tr>
<tr>
<td><code>cwd</code> and <code>env</code> if the launch needs them</td>
<td></td>
</tr>
<tr>
<td>Application checkpoint (repo path, step, agent state)</td>
<td></td>
</tr>
</tbody>
</table>
<p>A process ID is a resume key for the <strong>current</strong> container only. It is not enough to restart the job after the container may have stopped.</p>
<h3 id="case-1-the-container-still-has-the-process">Case 1: The container still has the process</h3>
<p>Use this path when the work is still running and the container has not been replaced — for example another request arrives seconds later while a build or server is up.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13715.md")
</div>
<p>You can also call <code>status()</code>, <code>waitForPort()</code>, <code>waitForExit()</code>, or <code>kill()</code> on that handle. Log cursors apply only while this process still exists in this container.</p>
<h3 id="case-2-the-process-is-gone-start-from-the-stored-job">Case 2: The process is gone — start from the stored job</h3>
<p>Use this path when <code>getProcess</code> returns <code>null</code>, a call throws <code>StaleProcessHandleError</code>, or enough time has passed that the container may have stopped or been replaced.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13716.md")
</div>
<p>If the job also depends on files that lived only in the previous container, <a href="/sandbox/guides/backup-restore/">back up and restore</a> those directories or mount durable storage before relying on the tree again. Backup and restore replace filesystem state. They do not bring back old process IDs or log buffers.</p>
<p>If the container is not ready yet, you may get <code>ContainerUnavailableError</code> — back off and run the same unit of work again. Refer to <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<h3 id="choose-a-path">Choose a path</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13717.md")
</div>
<p>If you still hold a handle object from before the container stopped, calls on that handle throw <code>StaleProcessHandleError</code>. Prefer <code>getProcess(id)</code> on each new request instead of reusing an old handle across requests.</p>
<h2 id="processes-and-terminals">Processes and terminals</h2>
<table>
<thead>
<tr>
<th></th>
<th>Process (<code>exec</code>)</th>
<th>Terminal</th>
</tr>
</thead>
<tbody>
<tr>
<td>Role</td>
<td>Supervised argv process</td>
<td>Interactive PTY</td>
</tr>
<tr>
<td>Input</td>
<td>Launch-time argv</td>
<td>PTY input (<code>write</code> / browser <code>connect</code>)</td>
</tr>
<tr>
<td>Stop</td>
<td><code>kill(signal?)</code></td>
<td><code>interrupt()</code> / <code>terminate()</code></td>
</tr>
<tr>
<td>Lookup</td>
<td><code>getProcess</code> / <code>listProcesses</code></td>
<td><code>getTerminal</code> / <code>listTerminals</code></td>
</tr>
</tbody>
</table>
<p>Both follow the same <a href="#how-long-a-process-lives">container lifetime rules</a>. Terminal docs: <a href="/sandbox/1-0-preview/terminals/">Terminals</a>. API: <a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a>.</p>
<h2 id="logs-and-large-output">Logs and large output</h2>
<p><code>output()</code> buffers stdout and stderr and may set <code>truncated: true</code>. Prefer <code>logs()</code> when output may be large or the process runs longer than one Worker request.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13718.md")
</div>
<p>On a later request against the <strong>same still-running container</strong>, call <code>getProcess(id)</code> and resume with <code>logs({ since: cursor, replay: true, follow: true })</code>. After a new container starts for the sandbox, start a new process; the old cursor does not apply.</p>
<p>Event shapes, wait options, and readiness checks: <a href="/sandbox/1-0-preview/api/processes/">Processes API</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a></li>
<li><a href="/sandbox/1-0-preview/api/processes/">Processes API</a></li>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a></li>
<li><a href="/sandbox/1-0-preview/api/errors/">Errors API</a></li>
<li><a href="/sandbox/1-0-preview/terminals/">Terminals</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li><a href="/sandbox/1-0-preview/get-started/">Get started</a></li>
<li><a href="/sandbox/1-0-preview/">1.0 preview overview</a></li>
</ul>
