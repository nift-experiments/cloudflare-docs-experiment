<p>This guide shows you how to connect a browser-based terminal to a sandbox shell. You can use the <code>SandboxAddon</code> with xterm.js, or connect directly over WebSockets.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13484.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need an existing Cloudflare Worker with a sandbox binding. Refer to <a href="/sandbox/get-started/">Getting started</a> if you do not have one.</p>
<p>Install the terminal dependencies in your frontend project:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun install @xterm/xterm @xterm/addon-fit @cloudflare/sandbox" aria-label="Copy to clipboard">Copy</button></div></div>
<p>If you are not using xterm.js, you only need <code>@cloudflare/sandbox</code> for types.</p>
<h2 id="handle-websocket-upgrades-in-the-worker">Handle WebSocket upgrades in the Worker</h2>
<p>Add a route that proxies WebSocket connections to the sandbox terminal. The example below supports both the default session and named sessions via a query parameter:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13485.md")
</div>
<h2 id="connect-with-xterm-js-and-sandboxaddon">Connect with xterm.js and SandboxAddon</h2>
<p>Create the terminal in your browser code and attach the <code>SandboxAddon</code>. The addon manages the WebSocket connection, automatic reconnection, and resize forwarding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13486.md")
</div>
<p>For the full addon API, refer to the <a href="/sandbox/api/terminal/">Terminal API reference</a>.</p>
<h2 id="connect-without-xterm-js">Connect without xterm.js</h2>
<p>If you are building a custom terminal UI or running in an environment without xterm.js, connect directly over WebSockets. The protocol uses binary frames for terminal data and JSON text frames for control messages.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13487.md")
</div>
<p>Key protocol details:</p>
<ul>
<li>Set <code>binaryType</code> to <code>arraybuffer</code> before connecting.</li>
<li>Buffered output from a previous connection arrives as binary frames before the <code>ready</code> message.</li>
<li>Send keystrokes as binary (UTF-8). Send control messages (<code>resize</code>) as JSON text.</li>
<li>The PTY stays alive when a client disconnects. Reconnecting replays buffered output.</li>
</ul>
<p>For the full protocol specification, refer to the <a href="/sandbox/api/terminal/#websocket-protocol">WebSocket protocol section</a> in the API reference.</p>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Always use FitAddon</strong> — Without it, terminal dimensions do not match the container and text wraps incorrectly.</li>
<li><strong>Handle resize events</strong> — Call <code>fitAddon.fit()</code> on window resize so the terminal and PTY stay in sync.</li>
<li><strong>Clean up on unmount</strong> — Call <code>addon.disconnect()</code> when removing the terminal from the page.</li>
<li><strong>Scope terminals to a user sandbox</strong> — Use sessions for multiple terminal contexts in the same workspace. Use separate sandboxes for separate users.</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/terminal/">Terminal API reference</a> — Method signatures, addon API, and WebSocket protocol</li>
<li><a href="/sandbox/concepts/terminal/">Terminal connections</a> — How terminal connections work</li>
<li><a href="/sandbox/concepts/sessions/">Session management</a> — How sessions work</li>
</ul>
