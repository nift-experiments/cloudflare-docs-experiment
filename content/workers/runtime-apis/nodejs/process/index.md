<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17139.md")
</aside>
<p>The <a href="https://nodejs.org/docs/latest/api/process.html"><code>process</code></a> module in Node.js provides a number of useful APIs related to the current process.</p>
<p>Initially Workers only supported <code>nextTick</code>, <code>env</code>, <code>exit</code>, <code>getBuiltinModule</code>, <code>platform</code> and <code>features</code> on process,
which was then updated with the <a href="/workers/configuration/compatibility-flags/#enable-process-v2-implementation"><code>enable_nodejs_process_v2</code></a> flag to include most Node.js process features.</p>
<p>Refer to the <a href="https://nodejs.org/docs/latest/api/process.html">Node.js documentation for <code>process</code></a> for more information.</p>
<p>Workers-specific implementation details apply when adapting Node.js process support for a serverless environment, which are described in more detail below.</p>
<h2 id="process-env"><code>process.env</code></h2>
<p>In the Node.js implementation of <code>process.env</code>, the <code>env</code> object is a copy of the environment variables at the time the process was started. In the Workers implementation, there is no process-level environment, so by default <code>env</code> is an empty object. You can still set and get values from <code>env</code>, and those will be globally persistent for all Workers running in the same isolate and context (for example, the same Workers entry point).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17138.md")
</aside>
<p>When <a href="/workers/runtime-apis/nodejs/">Node.js compatibility</a> is enabled and the <a href="/workers/configuration/compatibility-flags/#enable-auto-populating-processenv"><code>nodejs_compat_populate_process_env</code></a> compatibility flag is set (enabled by default for compatibility dates on or after 2025-04-01), <code>process.env</code> will contain any <a href="/workers/configuration/environment-variables/">environment variables</a>,
<a href="/workers/configuration/secrets/">secrets</a>, or <a href="/workers/runtime-apis/bindings/version-metadata/">version metadata</a> metadata that has been configured on your Worker.</p>
<p>Setting any value on <code>process.env</code> will coerce that value into a string.</p>
<h3 id="alternative-import-env-from-cloudflare-workers">Alternative: Import <code>env</code> from <code>cloudflare:workers</code></h3>
<p>Instead of using <code>process.env</code>, you can <a href="/workers/runtime-apis/bindings/#importing-env-as-a-global">import <code>env</code> from <code>cloudflare:workers</code></a> to access environment variables and all other bindings from anywhere in your code.</p>
<pre><code class="language-js">import * as process from &quot;node:process&quot;;&#10;&#10;export default {&#10;	fetch(req, env) {&#10;		// Set process.env.FOO to the value of env.FOO if process.env.FOO is not already set&#10;		// and env.FOO is a string.&#10;		process.env.FOO ??= (() =&gt; {&#10;			if (typeof env.FOO === &quot;string&quot;) {&#10;				return env.FOO;&#10;			}&#10;		})();&#10;	},&#10;};&#10;</code></pre>
<p>It is strongly recommended that you <em>do not</em> replace the entire <code>process.env</code> object with
the cloudflare <code>env</code> object. Doing so will cause you to lose any environment variables that
were set previously and will cause unexpected behavior for other Workers running in the
same isolate. Specifically, it would cause inconsistency with the <code>process.env</code> object when
accessed via named imports.</p>
<pre><code class="language-js">import * as process from &quot;node:process&quot;;&#10;import { env } from &quot;node:process&quot;;&#10;&#10;process.env === env; // true! they are the same object&#10;process.env = {}; // replace the object! Do not do this!&#10;process.env === env; // false! they are no longer the same object&#10;&#10;// From this point forward, any changes to process.env will not be reflected in env,&#10;// and vice versa!&#10;</code></pre>
<h2 id="process-nexttick"><code>process.nextTick()</code></h2>
<p>The Workers implementation of <code>process.nextTick()</code> is a wrapper for the standard Web Platform API <a href="https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask"><code>queueMicrotask()</code></a>.</p>
<pre><code class="language-js">import { env, nextTick } from &quot;node:process&quot;;&#10;&#10;env[&quot;FOO&quot;] = &quot;bar&quot;;&#10;console.log(env[&quot;FOO&quot;]); // Prints: bar&#10;&#10;nextTick(() =&gt; {&#10;	console.log(&quot;next tick&quot;);&#10;});&#10;</code></pre>
<h2 id="stdio">Stdio</h2>
<p><a href="https://nodejs.org/docs/latest/api/process.html#processstdout"><code>process.stdout</code></a>, <a href="https://nodejs.org/docs/latest/api/process.html#processstderr"><code>process.stderr</code></a> and <a href="https://nodejs.org/docs/latest/api/process.html#processstdin"><code>process.stdin</code></a> are supported as streams. <code>stdin</code> is treated as an empty readable stream.
<code>stdout</code> and <code>stderr</code> are non-TTY writable streams, which output to normal logging output only with <code>stdout: </code> and <code>stderr: </code> prefixing.</p>
<p>The line buffer works by storing writes to stdout or stderr until either a newline character <code>\n</code> is encountered or until the next microtask, when the log is then flushed to the output.</p>
<p>This ensures compatibility with inspector and structured logging outputs.</p>
<h2 id="current-working-directory">Current Working Directory</h2>
<p><a href="https://nodejs.org/docs/latest/api/process.html#processcwd"><code>process.cwd()</code></a> is the <em>current working directory</em>, used as the default path for all filesystem operations, and is initialized to <code>/bundle</code>.</p>
<p><a href="https://nodejs.org/docs/latest/api/process.html#processchdirdirectory"><code>process.chdir()</code></a> allows modifying the <code>cwd</code> and is respected by FS operations when using <code>enable_nodejs_fs_module</code>.</p>
<h2 id="hrtime">Hrtime</h2>
<p>While <a href="https://nodejs.org/docs/latest/api/process.html#processhrtimetime"><code>process.hrtime</code></a> high-resolution timer is available, it provides an inaccurate timer for compatibility only.</p>
