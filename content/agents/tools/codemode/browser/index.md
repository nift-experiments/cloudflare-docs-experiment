<p>Use <code>@cloudflare/codemode/browser</code> when your browser owns the tools that the model must orchestrate. For example, these tools might read page state, access browser APIs, or update data held by your application.</p>
<p>Code Mode is useful when the model must call several client tools with loops, conditions, or intermediate results. For a single browser action, use a standard client-side tool instead.</p>
<p>Code Mode presents those tools to the model as typed functions. The model writes one JavaScript async arrow function that can call several tools, combine their results, and apply control flow. <code>IframeSandboxExecutor</code> runs that generated code in a sandboxed iframe on the page.</p>
<p>This integration does not give an agent control of a remote browser. To inspect websites, capture screenshots, or automate pages with the Chrome DevTools Protocol (CDP), refer to <a href="/agents/tools/browser/">Browser tools</a>.</p>
<h2 id="install-code-mode">Install Code Mode</h2>
<p>Install the package in your client application:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/codemode</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/codemode" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/codemode</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/codemode" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/codemode</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/codemode" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/codemode</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/codemode" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The <code>@cloudflare/codemode/browser</code> entry point uses JSON Schema and browser APIs. It does not require the AI SDK or Zod peer dependencies used by <code>@cloudflare/codemode/ai</code>.</p>
<h2 id="add-code-mode-to-an-agent-chat-ui">Add Code Mode to an Agent chat UI</h2>
<p>The browser creates the Code Mode tool and registers it as a dynamic client tool. The Agent receives the tool schema, but the tool implementation remains in the browser.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2691.md")
</div>
<p>If your browser tool set changes at runtime, create a new Code Mode descriptor and register the updated descriptor with your client tool layer.</p>
<h2 id="iframe-execution-and-security">Iframe execution and security</h2>
<p><code>IframeSandboxExecutor</code> creates a hidden iframe for each execution. The iframe uses <code>sandbox=&quot;allow-scripts&quot;</code> and receives the generated code through <code>postMessage</code>. Tool calls return to the parent page, which runs the matching browser-owned <code>execute</code> function.</p>
<p>Messages are scoped to the current iframe and an execution nonce. The executor removes the iframe and message listener after completion, failure, or timeout.</p>
<p>The executor accepts these options:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td><code>30000</code></td>
<td>Ends an execution after the specified number of milliseconds.</td>
</tr>
<tr>
<td><code>csp</code></td>
<td><code>string</code></td>
<td><code>default-src 'none'; script-src 'unsafe-inline' 'unsafe-eval';</code></td>
<td>Sets the Content Security Policy (CSP) for the iframe document.</td>
</tr>
</tbody>
</table>
<p>The default CSP blocks resources except the inline and evaluated scripts required to execute generated code. Pass a custom policy only when your generated code needs additional iframe capabilities.</p>
<p>Relaxing directives such as <code>connect-src</code>, <code>img-src</code>, or <code>form-action</code> can let generated iframe code communicate with external systems. That code could expose values returned by browser tools. Keep outbound destinations narrow, and do not place secrets in tool results. Browser-owned tools execute separately in the parent page with the capabilities their implementations provide.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2686.md")
</aside>
<h2 id="approval-constraints">Approval constraints</h2>
<p><code>createBrowserCodeTool()</code> excludes any tool whose <code>needsApproval</code> value is <code>true</code> or a function. Code Mode does not pause iframe execution to request approval for those tools.</p>
<p>Keep approval-gated actions outside the Code Mode descriptor. Register them as standard tools and use the <a href="/agents/communication-channels/chat/chat-agents/#tool-approval-human-in-the-loop"><code>useAgentChat()</code> approval flow</a> instead.</p>
