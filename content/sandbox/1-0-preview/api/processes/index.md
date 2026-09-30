<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13761.md")
</aside>
<p>Launch and observe supervised processes in the current container for a sandbox.</p>
<p>For the mental model, refer to <a href="/sandbox/1-0-preview/processes/">Process execution</a>. For interactive PTY input and browser terminals, refer to <a href="/sandbox/1-0-preview/terminals/">Terminals</a> and the <a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a>.</p>
<p>Process handles have <strong>no standard input</strong>. Use <code>cwd</code>, <code>env</code>, and argv (or an explicit shell script) for non-interactive work. Use a <a href="/sandbox/1-0-preview/terminals/">terminal</a> when you need an interactive PTY.</p>
<h2 id="exec"><code>exec()</code></h2>
<p>Start a process from <strong>argv</strong> (executable, then arguments). Resolves when launch succeeds, not when the process exits. The SDK does not run a shell and does not shell-escape argv — each entry is one process argument.</p>
<pre><code class="language-ts">exec(command: SandboxCommand, options?: ExecOptions): Promise&lt;SandboxProcess&gt;&#10;</code></pre>
<h3 id="sandboxcommand"><code>SandboxCommand</code></h3>
<pre><code class="language-ts">type SandboxCommand = readonly [executable: string, ...args: string[]];&#10;</code></pre>
<ul>
<li><code>command[0]</code> must be a non-empty executable path or name.</li>
<li>Later arguments may be empty strings.</li>
<li>Entries are passed through as-is (no shell escaping of argv).</li>
<li>Shell syntax requires an explicit shell, for example <code>['/bin/bash', '-lc', script]</code>.</li>
</ul>
<h3 id="execoptions"><code>ExecOptions</code></h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cwd</code></td>
<td><code>string</code></td>
<td>Working directory for this launch. Defaults to <code>/workspace</code> when unset.</td>
</tr>
<tr>
<td><code>env</code></td>
<td><code>Record&lt;string, string&gt;</code></td>
<td>Environment overlay for this launch. Does not mutate later launches. Sandbox-level env still applies.</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td>Remote process lifetime in milliseconds. The supervisor may stop the process; completion can report <code>timedOut: true</code>.</td>
</tr>
</tbody>
</table>
<h3 id="returns">Returns</h3>
<p><code>Promise&lt;SandboxProcess&gt;</code></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13762.md")
</div>
<h2 id="getprocess"><code>getProcess()</code></h2>
<p>Return a handle for a process running in the <strong>current container</strong> for this sandbox, or <code>null</code>.</p>
<p>Does not start a container if none is running. Returns <code>null</code> when no container is up, when the process ID is unknown in the current container, or when that process belonged to a previous container for the same sandbox ID.</p>
<pre><code class="language-ts">getProcess(id: string): Promise&lt;SandboxProcess | null&gt;&#10;</code></pre>
<p>Process IDs are not durable across container stop or replace. Refer to <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>.</p>
<h2 id="listprocesses"><code>listProcesses()</code></h2>
<p>List processes in the current container for this sandbox. Does not start a container if none is running. Returns an empty list when no container is up.</p>
<pre><code class="language-ts">listProcesses(): Promise&lt;ProcessStatus[]&gt;&#10;</code></pre>
<p>Each entry is a <a href="#processstatus">ProcessStatus</a> value (the same shape as <code>status()</code>).</p>
<h2 id="sandboxprocess"><code>SandboxProcess</code></h2>
<table>
<thead>
<tr>
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>Process ID in the current container.</td>
</tr>
<tr>
<td><code>pid</code></td>
<td>Container pid at launch.</td>
</tr>
<tr>
<td><code>exitCode</code></td>
<td><code>Promise&lt;number&gt;</code> that resolves when the supervised process group settles.</td>
</tr>
<tr>
<td><code>status()</code></td>
<td>Current discriminated status.</td>
</tr>
<tr>
<td><code>logs(options?)</code></td>
<td>Cursor-based log stream.</td>
</tr>
<tr>
<td><code>output(options?)</code></td>
<td>Buffered stdout and stderr plus exit metadata.</td>
</tr>
<tr>
<td><code>waitForExit(options?)</code></td>
<td>Wait until the supervised process group settles.</td>
</tr>
<tr>
<td><code>waitForLog(pattern, options?)</code></td>
<td>Wait until stdout or stderr matches.</td>
</tr>
<tr>
<td><code>waitForPort(port, options?)</code></td>
<td>Wait until a port is ready or readiness fails.</td>
</tr>
<tr>
<td><code>kill(signal?)</code></td>
<td>Send a numeric signal. Default <code>15</code> (<code>SIGTERM</code>).</td>
</tr>
</tbody>
</table>
<p>There is no process stdin API on this handle.</p>
<h3 id="status"><code>status()</code></h3>
<pre><code class="language-ts">status(): Promise&lt;ProcessStatus&gt;&#10;</code></pre>
<p>Refer to <a href="#processstatus">ProcessStatus</a>. A process stays <code>running</code> until the supervised <strong>process group</strong> has settled, even if the root pid exits while descendants continue.</p>
<h3 id="output"><code>output()</code></h3>
<p>Buffer stdout and stderr until the process completes (or the local wait ends), then return exit metadata.</p>
<pre><code class="language-ts">output(options?: ProcessOutputOptions): Promise&lt;ProcessOutput&lt;Uint8Array&gt;&gt;&#10;output(&#10;	options: ProcessOutputOptions &amp; { encoding: &quot;utf8&quot; },&#10;): Promise&lt;ProcessOutput&lt;string&gt;&gt;&#10;</code></pre>
<h4 id="processoutput"><code>ProcessOutput</code></h4>
<pre><code class="language-ts">interface ProcessOutput&lt;T = Uint8Array&gt; {&#10;	stdout: T;&#10;	stderr: T;&#10;	exitCode: number;&#10;	signal?: number;&#10;	timedOut: boolean;&#10;	truncated: boolean;&#10;}&#10;</code></pre>
<p>Default body encoding is binary (<code>Uint8Array</code>) unless you pass <code>encoding: &quot;utf8&quot;</code>. Prefer <code>logs()</code> when output may exceed what you want to buffer.</p>
<h4 id="processoutputoptions"><code>ProcessOutputOptions</code></h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>encoding</code></td>
<td><code>&quot;utf8&quot;</code></td>
<td>Decode stdout/stderr as strings.</td>
</tr>
<tr>
<td><code>maxBytes</code></td>
<td><code>number</code></td>
<td>Cap buffered bytes per stream side of the result; may set <code>truncated: true</code>. No default cap when omitted.</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td>Local wait deadline in milliseconds only; does not kill the process.</td>
</tr>
<tr>
<td><code>signal</code></td>
<td><code>AbortSignal</code></td>
<td>Cancel this wait only; does not kill the process.</td>
</tr>
</tbody>
</table>
<p><code>maxBytes</code> must be a non-negative finite number when set.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13763.md")
</div>
<h3 id="logs"><code>logs()</code></h3>
<p>Stream replayable log events with an opaque cursor.</p>
<pre><code class="language-ts">logs(options?: ProcessLogsOptions): Promise&lt;ReadableStream&lt;ProcessLogEvent&gt;&gt;&#10;</code></pre>
<h4 id="processlogsoptions"><code>ProcessLogsOptions</code></h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>since</code></td>
<td><code>string</code></td>
<td>Opaque cursor; resume after a previous event.</td>
</tr>
<tr>
<td><code>replay</code></td>
<td><code>boolean</code></td>
<td>Include buffered history when resuming.</td>
</tr>
<tr>
<td><code>follow</code></td>
<td><code>boolean</code></td>
<td>Keep the stream open for live output.</td>
</tr>
<tr>
<td><code>signal</code></td>
<td><code>AbortSignal</code></td>
<td>Cancel this subscription only; the process keeps running.</td>
</tr>
</tbody>
</table>
<h4 id="processlogevent"><code>ProcessLogEvent</code></h4>
<pre><code class="language-ts">type ProcessLogEvent =&#10;	| {&#10;			type: &quot;stdout&quot; | &quot;stderr&quot;;&#10;			cursor: string;&#10;			timestamp: string;&#10;			data: Uint8Array;&#10;	  }&#10;	| {&#10;			type: &quot;terminal&quot;;&#10;			state: &quot;exited&quot;;&#10;			cursor: string;&#10;			timestamp: string;&#10;			exit: ProcessExit;&#10;	  }&#10;	| {&#10;			type: &quot;terminal&quot;;&#10;			state: &quot;error&quot;;&#10;			cursor: string;&#10;			timestamp: string;&#10;			error: ProcessFailure;&#10;	  }&#10;	| {&#10;			type: &quot;truncated&quot;;&#10;			cursor?: string;&#10;			timestamp: string;&#10;	  };&#10;</code></pre>
<p>Retain the latest <code>cursor</code> from delivered events if a later Worker request resumes with <code>logs({ since: cursor, replay: true, follow: true })</code> on the <strong>same</strong> process in the <strong>same</strong> container.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13764.md")
</div>
<h3 id="waitforexit"><code>waitForExit()</code></h3>
<p>Wait until the supervised process group settles.</p>
<pre><code class="language-ts">waitForExit(options?: {&#10;	timeout?: number;&#10;	signal?: AbortSignal;&#10;}): Promise&lt;ProcessExit&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td>Local wait deadline only; does not kill the process.</td>
</tr>
<tr>
<td><code>signal</code></td>
<td><code>AbortSignal</code></td>
<td>Cancel this wait only; does not kill the process.</td>
</tr>
</tbody>
</table>
<p>Returns <a href="#processexit">ProcessExit</a>. Local timeout surfaces as <code>ProcessWaitTimeoutError</code>. Local abort surfaces as <code>ProcessAbortedError</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13765.md")
</div>
<h3 id="waitforlog"><code>waitForLog()</code></h3>
<p>Wait until stdout and/or stderr matches a pattern.</p>
<pre><code class="language-ts">waitForLog(&#10;	pattern: string | RegExp,&#10;	options?: WaitForLogOptions,&#10;): Promise&lt;WaitForLogResult&gt;&#10;</code></pre>
<h4 id="waitforlogoptions"><code>WaitForLogOptions</code></h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>stream</code></td>
<td><code>&quot;stdout&quot; | &quot;stderr&quot; | &quot;both&quot;</code></td>
<td>Which streams to match. Default: <code>&quot;both&quot;</code>.</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td>Local wait deadline only; does not kill the process.</td>
</tr>
<tr>
<td><code>signal</code></td>
<td><code>AbortSignal</code></td>
<td>Cancel this wait only; does not kill the process.</td>
</tr>
</tbody>
</table>
<h4 id="waitforlogresult"><code>WaitForLogResult</code></h4>
<pre><code class="language-ts">interface WaitForLogResult {&#10;	stream: &quot;stdout&quot; | &quot;stderr&quot;;&#10;	text: string;&#10;	match: string;&#10;	cursor?: string;&#10;}&#10;</code></pre>
<ul>
<li><code>text</code> is the matching window of decoded output for that stream.</li>
<li><code>match</code> is the matched substring.</li>
<li><code>cursor</code> is the log cursor at the match when available.</li>
</ul>
<p>If the process exits before a match, the SDK throws <code>ProcessExitedBeforeLogError</code>. A local wait timeout throws <code>ProcessWaitTimeoutError</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13766.md")
</div>
<h3 id="waitforport"><code>waitForPort()</code></h3>
<p>Wait until a port is ready, or fail if the process exits first or the local wait ends.</p>
<pre><code class="language-ts">waitForPort(port: number, options?: WaitForPortOptions): Promise&lt;void&gt;&#10;</code></pre>
<h4 id="waitforportoptions"><code>WaitForPortOptions</code></h4>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>mode</code></td>
<td><code>&quot;tcp&quot; | &quot;http&quot;</code></td>
<td>Readiness check. Default: <code>&quot;tcp&quot;</code> (accepts a TCP connection).</td>
</tr>
<tr>
<td><code>path</code></td>
<td><code>string</code></td>
<td>HTTP path to request when <code>mode</code> is <code>&quot;http&quot;</code>. Default: <code>&quot;/&quot;</code>.</td>
</tr>
<tr>
<td><code>status</code></td>
<td><code>number | { min: number; max: number }</code></td>
<td>Expected HTTP status or inclusive range when <code>mode</code> is <code>&quot;http&quot;</code>. Default: <code>{ min: 200, max: 399 }</code>.</td>
</tr>
<tr>
<td><code>interval</code></td>
<td><code>number</code></td>
<td>Milliseconds between checks. Default: <code>500</code>.</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td>Local wait deadline only; does not kill the process. No default timeout when omitted.</td>
</tr>
<tr>
<td><code>signal</code></td>
<td><code>AbortSignal</code></td>
<td>Cancel this wait only; does not kill the process.</td>
</tr>
</tbody>
</table>
<p><strong>TCP mode</strong> (default) succeeds when the port accepts a connection:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13767.md")
</div>
<p><strong>HTTP mode</strong> issues an HTTP request and checks the response status:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13768.md")
</div>
<p>Typical failures:</p>
<ul>
<li><code>ProcessReadyTimeoutError</code> — port not ready before the local timeout</li>
<li><code>ProcessExitedBeforeReadyError</code> — process exited before the port was ready</li>
<li><code>ProcessAbortedError</code> — local <code>AbortSignal</code> cancelled the wait (process may still run)</li>
</ul>
<h3 id="kill"><code>kill()</code></h3>
<p>Send a numeric signal to the process.</p>
<pre><code class="language-ts">kill(signal?: number): Promise&lt;void&gt;&#10;</code></pre>
<p>Default <code>signal</code> is <code>15</code> (<code>SIGTERM</code>). Pass a numeric signal only (for example <code>9</code> for <code>SIGKILL</code>). String signal names are not accepted.</p>
<p>Stopping the process is separate from cancelling a local wait or log subscription.</p>
<h3 id="exitcode"><code>exitCode</code></h3>
<pre><code class="language-ts">readonly exitCode: Promise&lt;number&gt;&#10;</code></pre>
<p>Resolves to the exit code when the supervised process group has settled (the same completion boundary as <code>waitForExit()</code>). Prefer <code>waitForExit()</code> when you also need <code>signal</code> or <code>timedOut</code>.</p>
<h2 id="processstatus">ProcessStatus</h2>
<pre><code class="language-ts">type ProcessStatus =&#10;	| {&#10;			state: &quot;running&quot;;&#10;			id: string;&#10;			pid: number;&#10;			command: SandboxCommand;&#10;			cwd?: string;&#10;			startedAt: string;&#10;	  }&#10;	| {&#10;			state: &quot;exited&quot;;&#10;			id: string;&#10;			pid: number;&#10;			command: SandboxCommand;&#10;			cwd?: string;&#10;			startedAt: string;&#10;			endedAt: string;&#10;			exit: ProcessExit;&#10;	  }&#10;	| {&#10;			state: &quot;error&quot;;&#10;			id: string;&#10;			pid: number;&#10;			command: SandboxCommand;&#10;			cwd?: string;&#10;			startedAt: string;&#10;			endedAt: string;&#10;			error: ProcessFailure;&#10;	  };&#10;</code></pre>
<p><code>listProcesses()</code> returns <code>ProcessStatus[]</code> using this shape.</p>
<h3 id="processexit"><code>ProcessExit</code></h3>
<p>Outcome observed for the <strong>root</strong> subprocess when the supervised group settles.</p>
<pre><code class="language-ts">interface ProcessExit {&#10;	code: number;&#10;	signal?: number;&#10;	timedOut: boolean;&#10;}&#10;</code></pre>
<p>Signals delivered only to descendants do not rewrite this outcome. Refer to <a href="/sandbox/1-0-preview/processes/">Process execution</a>.</p>
<h3 id="processfailure"><code>ProcessFailure</code></h3>
<pre><code class="language-ts">interface ProcessFailure {&#10;	code: string;&#10;	message: string;&#10;}&#10;</code></pre>
<h2 id="common-errors">Common errors</h2>
<p><code>getProcess</code> and <code>listProcesses</code> do not throw for missing work. They return <code>null</code> or <code>[]</code> when no container is up, the ID is unknown in the current container, or the process belonged to a previous container. The following error classes apply to operations on a process handle (and to launch), not to those lookups.</p>
<table>
<thead>
<tr>
<th>Situation</th>
<th>Class / outcome</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>getProcess</code> / <code>listProcesses</code> while no container is running</td>
<td><code>null</code> / <code>[]</code> (not an error; does not start a container)</td>
</tr>
<tr>
<td><code>getProcess</code> for an unknown ID or a process from a previous container</td>
<td><code>null</code></td>
</tr>
<tr>
<td>Operation on a handle after the container was replaced</td>
<td><code>StaleProcessHandleError</code></td>
</tr>
<tr>
<td>Operation on a handle when the process is gone in the current container</td>
<td><code>ProcessNotFoundError</code></td>
</tr>
<tr>
<td>Local wait timed out (<code>output</code> / <code>waitForExit</code> / <code>waitForLog</code>)</td>
<td><code>ProcessWaitTimeoutError</code></td>
</tr>
<tr>
<td>Local <code>AbortSignal</code> on a wait or stream</td>
<td><code>ProcessAbortedError</code></td>
</tr>
<tr>
<td>Port not ready before local timeout</td>
<td><code>ProcessReadyTimeoutError</code></td>
</tr>
<tr>
<td>Process exited before port readiness</td>
<td><code>ProcessExitedBeforeReadyError</code></td>
</tr>
<tr>
<td>Process exited before a log match</td>
<td><code>ProcessExitedBeforeLogError</code></td>
</tr>
<tr>
<td>Invalid working directory at launch</td>
<td><code>InvalidProcessCwdError</code></td>
</tr>
<tr>
<td>Invalid environment at launch</td>
<td><code>InvalidProcessEnvironmentError</code></td>
</tr>
<tr>
<td>Invalid log cursor</td>
<td><code>InvalidProcessCursorError</code></td>
</tr>
<tr>
<td>Process failed to start</td>
<td><code>ProcessSpawnFailedError</code></td>
</tr>
<tr>
<td>Container not ready; work did not start</td>
<td><code>ContainerUnavailableError</code></td>
</tr>
<tr>
<td>Work interrupted after it may have started</td>
<td><code>OperationInterruptedError</code></td>
</tr>
</tbody>
</table>
<p>Recovery guidance: <a href="/sandbox/1-0-preview/errors/">Errors and recovery</a>. Full catalog: <a href="/sandbox/1-0-preview/api/errors/">Errors API</a>. Lifetime: <a href="/sandbox/1-0-preview/processes/#how-long-a-process-lives">How long a process lives</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/processes/">Process execution</a></li>
<li><a href="/sandbox/1-0-preview/errors/">Errors and recovery</a></li>
<li><a href="/sandbox/1-0-preview/api/errors/">Errors API</a></li>
<li><a href="/sandbox/1-0-preview/api/terminals/">Terminals API</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate from the stable SDK</a></li>
<li>Stable: <a href="/sandbox/api/commands/">Commands</a></li>
</ul>
