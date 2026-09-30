<p>This guide shows you how to execute commands in the sandbox, handle output, and manage errors effectively.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13461.md")
</aside>
<h2 id="choose-the-right-method">Choose the right method</h2>
<p>The SDK provides multiple approaches for running commands:</p>
<ul>
<li><strong><code>exec()</code></strong> - Run a command and wait for complete result. Best for one-time commands like builds, installations, and scripts.</li>
<li><strong><code>execStream()</code></strong> - Stream output in real-time. Best for long-running commands where you need immediate feedback.</li>
<li><strong><code>startProcess()</code></strong> - Start a background process. Best for web servers, databases, and services that need to keep running.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13460.md")
</aside>
<h2 id="execute-basic-commands">Execute basic commands</h2>
<p>Use <code>exec()</code> for simple commands that complete quickly:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13462.md")
</div>
<h2 id="pass-arguments-safely">Pass arguments safely</h2>
<p>When passing user input or dynamic values, avoid string interpolation to prevent injection attacks:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13463.md")
</div>
<h2 id="handle-errors">Handle errors</h2>
<p>Commands can fail in two ways:</p>
<ol>
<li><strong>Non-zero exit code</strong> - Command ran but failed (result.success === false)</li>
<li><strong>Execution error</strong> - Command couldn't start (throws exception)</li>
</ol>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13464.md")
</div>
<h2 id="execute-shell-commands">Execute shell commands</h2>
<p>The sandbox supports shell features like pipes, redirects, and chaining:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13465.md")
</div>
<h2 id="execute-python-scripts">Execute Python scripts</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13466.md")
</div>
<h2 id="timeouts">Timeouts</h2>
<p>Set a maximum execution time for commands to prevent long-running operations from blocking indefinitely.</p>
<h3 id="per-command-timeout">Per-command timeout</h3>
<p>Pass <code>timeout</code> in the options to set a timeout for a single command:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13467.md")
</div>
<h3 id="session-level-timeout">Session-level timeout</h3>
<p>Set a default timeout for all commands in a session with <code>commandTimeoutMs</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13468.md")
</div>
<h3 id="global-timeout">Global timeout</h3>
<p>Set the <code>COMMAND_TIMEOUT_MS</code> <a href="/sandbox/configuration/environment-variables/#command_timeout_ms">environment variable</a> to define a global default timeout for every <code>exec()</code> call across all sessions.</p>
<h3 id="timeout-precedence">Timeout precedence</h3>
<p>When multiple timeouts are configured, the most specific value wins:</p>
<ol>
<li><strong>Per-command</strong> <code>timeout</code> on <code>exec()</code> (highest priority)</li>
<li><strong>Session-level</strong> <code>commandTimeoutMs</code> on <code>createSession()</code></li>
<li><strong>Global</strong> <code>COMMAND_TIMEOUT_MS</code> environment variable (lowest priority)</li>
</ol>
<p>If none are set, commands run without a timeout.</p>
<h3 id="timeout-does-not-kill-the-process">Timeout does not kill the process</h3>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13459.md")
</aside>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Check exit codes</strong> - Always verify <code>result.success</code> and <code>result.exitCode</code></li>
<li><strong>Validate inputs</strong> - Escape or validate user input to prevent injection</li>
<li><strong>Use streaming</strong> - For long operations, use <code>execStream()</code> for real-time feedback</li>
<li><strong>Use background processes</strong> - For services that need to keep running (web servers, databases), use the <a href="/sandbox/guides/background-processes/">Background processes guide</a> instead</li>
<li><strong>Handle errors</strong> - Check stderr for error details</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="command-not-found">Command not found</h3>
<p>Verify the command exists in the container:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13469.md")
</div>
<h3 id="working-directory-issues">Working directory issues</h3>
<p>Use absolute paths or change directory:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13470.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/commands/">Commands API reference</a> - Complete method documentation</li>
<li><a href="/sandbox/guides/background-processes/">Background processes guide</a> - Managing long-running processes</li>
<li><a href="/sandbox/guides/streaming-output/">Streaming output guide</a> - Advanced streaming patterns</li>
<li><a href="/sandbox/guides/code-execution/">Code Interpreter guide</a> - Higher-level code execution</li>
</ul>
