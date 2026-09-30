<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13724.md")
</aside>
<p>Your app addresses a sandbox with a <strong>sandbox ID</strong>. The Linux environment that runs commands and holds local files is a <strong>container</strong>. The ID can outlive any one container.</p>
<p>That distinction matters for processes, terminals, files, and recovery after idle stop or replace.</p>
<h2 id="sandbox-id-and-container">Sandbox ID and container</h2>
<p>Most apps use one sandbox per user or task:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13725.md")
</div>
<table>
<thead>
<tr>
<th></th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Sandbox ID</strong></td>
<td>The string you pass to <code>getSandbox</code> (for example <code>&quot;user-123&quot;</code>). Use the same ID to reach the same sandbox later.</td>
</tr>
<tr>
<td><strong>Durable Object</strong></td>
<td>The coordinator behind that ID. The same ID maps to the same Durable Object identity.</td>
</tr>
<tr>
<td><strong>Container</strong></td>
<td>The current <a href="/containers/">Containers</a> instance that runs Linux work for the sandbox.</td>
</tr>
<tr>
<td><strong>Process or terminal</strong></td>
<td>A program or interactive PTY inside the <strong>current</strong> container.</td>
</tr>
<tr>
<td><strong>Local files</strong></td>
<td>Files on that container’s disk (for example under <code>/workspace</code>).</td>
</tr>
</tbody>
</table>
<p><strong>Same sandbox ID does not mean the same container.</strong> After the container stops or is replaced, the next work for that ID may run in a new container.</p>
<h2 id="when-the-container-starts">When the container starts</h2>
<p><code>getSandbox()</code> returns immediately. It does not start a container by itself.</p>
<p>The container starts when an operation needs it — for example <code>exec()</code>, <code>createTerminal()</code>, or writing a file. The first start after deploy or idle can take longer than a warm call. If the container is not ready yet, the SDK may throw <code>ContainerUnavailableError</code>. That error means the operation did not start inside the container. Refer to <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<h2 id="while-the-container-is-running">While the container is running</h2>
<p>While a container is up for a sandbox ID:</p>
<ul>
<li>Processes and terminals keep running until they exit or you stop them.</li>
<li>Local files stay available in that container.</li>
<li>Later Worker requests can call <code>getProcess</code> or <code>getTerminal</code> and continue, as long as <strong>that</strong> container still has the resource.</li>
</ul>
<p>Process detail: <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>. Terminals: <a href="/sandbox/1-0-preview/terminals/">Terminals</a>.</p>
<h2 id="when-the-container-stops-or-is-replaced">When the container stops or is replaced</h2>
<p>A container is not permanent. Cloudflare may stop it after idle time. It can also stop after failures, or when the platform replaces it during normal operations (for example after some deploys).</p>
<p>When that happens:</p>
<ul>
<li>Your app still uses the same sandbox ID.</li>
<li>Processes and terminals from the old container are gone, including their IDs and live log buffers.</li>
<li>Local files from the old container are gone unless your app restored them (for example with a <a href="/sandbox/guides/backup-restore/">backup</a> or a mounted bucket).</li>
<li>The next real work may start a <strong>new</strong> container for the same sandbox ID.</li>
<li>Handles from the previous container fail closed. <code>getProcess</code> and <code>getTerminal</code> return <code>null</code> when the resource is not in the current container. Those lookups do not start a container only to answer the question.</li>
</ul>
<p>To continue work later, store the <strong>job</strong> (what to run, <code>cwd</code>, <code>env</code>, and any app checkpoint), not only a process or terminal ID.</p>
<h2 id="idle-stop-replace-and-destroy">Idle stop, replace, and destroy</h2>
<table>
<thead>
<tr>
<th>Event</th>
<th>What stays</th>
<th>What is gone</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Idle stop</strong></td>
<td>Sandbox ID and Durable Object identity</td>
<td>Processes, terminals, local files from the stopped container</td>
</tr>
<tr>
<td><strong>Replace</strong> (failure, deploy, or other replacement)</td>
<td>Sandbox ID and Durable Object identity</td>
<td>Same as idle stop for the previous container</td>
</tr>
<tr>
<td><strong><code>destroy()</code></strong></td>
<td>The sandbox ID string can be used again later</td>
<td>Treat prior work for that generation as finished</td>
</tr>
</tbody>
</table>
<p>After idle stop or replace, the next real work may start a <strong>new</strong> container for the same sandbox ID. Old process and terminal handles are invalid. Recovery procedures: <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>.</p>
<p><code>keepAlive</code> and <code>sleepAfter</code> change idle behavior. They do not keep one container instance forever. Refer to the stable <a href="/sandbox/api/lifecycle/">Lifecycle API</a> and <a href="/sandbox/configuration/sandbox-options/">Sandbox options</a> (ignore transport and default-session options on <code>@next</code>).</p>
<h2 id="state-that-outlives-a-container">State that outlives a container</h2>
<p>Only what <strong>your app</strong> keeps (or restores) survives a new container:</p>
<table>
<thead>
<tr>
<th>Need</th>
<th>What must live outside the container</th>
</tr>
</thead>
<tbody>
<tr>
<td>Find the sandbox again</td>
<td>The <strong>sandbox ID</strong></td>
</tr>
<tr>
<td>Continue work on a later request</td>
<td>Resource ID <strong>while</strong> the current container still has it, plus enough job context to start again if it does not</td>
</tr>
<tr>
<td>Survive stop or replace</td>
<td>The <strong>job</strong>: command or terminal setup, <code>cwd</code>, <code>env</code>, checkpoint</td>
</tr>
<tr>
<td>Keep files after a new container</td>
<td>Backup metadata, mount configuration, or another durable store</td>
</tr>
</tbody>
</table>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/processes/">Process execution</a></li>
<li><a href="/sandbox/1-0-preview/terminals/">Terminals</a></li>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a></li>
<li><a href="/containers/concepts/architecture/">Lifecycle of a Container</a></li>
<li>Stable: <a href="/sandbox/concepts/sandboxes/">Sandbox lifecycle</a></li>
</ul>
