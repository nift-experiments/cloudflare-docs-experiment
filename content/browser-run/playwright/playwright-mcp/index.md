<p><a href="https://github.com/cloudflare/playwright-mcp"><code>@cloudflare/playwright-mcp</code></a> is a <a href="https://github.com/microsoft/playwright-mcp">Playwright MCP</a> server fork that provides browser automation capabilities using Playwright and Browser Run.</p>
<p>This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models. Its key features are:</p>
<ul>
<li>Fast and lightweight. Uses Playwright's accessibility tree, not pixel-based input.</li>
<li>LLM-friendly. No vision models needed, operates purely on structured data.</li>
<li>Deterministic tool application. Avoids ambiguity common with screenshot-based approaches.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3656.md")
</aside>
<h2 id="quick-start">Quick start</h2>
<p>If you are already familiar with Cloudflare Workers and you want to get started with Playwright MCP right away, select this button:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/playwright-mcp/tree/main/cloudflare/example"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>This creates a repository in your GitHub account and deploys the application to Cloudflare Workers. Use this option if you are familiar with Cloudflare Workers, and wish to skip the step-by-step guidance.</p>
<p>Check our <a href="https://github.com/cloudflare/playwright-mcp">GitHub page</a> for more information on how to build and deploy Playwright MCP.</p>
<h2 id="deploying">Deploying</h2>
<p>Follow these steps to deploy <code>@cloudflare/playwright-mcp</code>:</p>
<ol>
<li>Install the Playwright MCP <a href="https://www.npmjs.com/package/@cloudflare/playwright-mcp">npm package</a>.</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/playwright-mcp</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/playwright-mcp" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li>Make sure you have the <a href="/browser-run/">Browser Run</a> and <a href="/durable-objects/">Durable Object</a> bindings and <a href="/durable-objects/reference/durable-objects-migrations/">migrations</a> in your Wrangler configuration file.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3655.md")
</aside>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/3657.md")
</div>
<ol start="3">
<li>Edit the code.</li>
</ol>
<pre><code class="language-ts">import { env } from &quot;cloudflare:workers&quot;;&#10;import { createMcpAgent } from &quot;@cloudflare/playwright-mcp&quot;;&#10;&#10;export const PlaywrightMCP = createMcpAgent(env.BROWSER);&#10;&#10;export default {&#10;	fetch(request: Request, env: Env, ctx: ExecutionContext) {&#10;		const { pathname } = new URL(request.url);&#10;&#10;		switch (pathname) {&#10;			case &quot;/sse&quot;:&#10;			case &quot;/sse/message&quot;:&#10;				return PlaywrightMCP.serveSSE(&quot;/sse&quot;).fetch(request, env, ctx);&#10;			case &quot;/mcp&quot;:&#10;				return PlaywrightMCP.serve(&quot;/mcp&quot;).fetch(request, env, ctx);&#10;			default:&#10;				return new Response(&quot;Not Found&quot;, { status: 404 });&#10;		}&#10;	},&#10;};&#10;</code></pre>
<ol start="4">
<li>Deploy the server.</li>
</ol>
<pre><code class="language-bash">npx wrangler deploy&#10;</code></pre>
<p>The server is now available at <code>https://[my-mcp-url].workers.dev/sse</code> and you can use it with any MCP client.</p>
<h2 id="using-playwright-mcp">Using Playwright MCP</h2>
<p><img src="/assets/upstream/images/browser-run/playground-ai-screenshot.png" alt="Screenshot of the AI Playground" /></p>
<p><a href="https://playground.ai.cloudflare.com/">Cloudflare AI Playground</a> is a great way to test MCP servers using LLM models available in Workers AI.</p>
<ol>
<li>Go to <a href="https://playground.ai.cloudflare.com/">https://playground.ai.cloudflare.com/</a>.</li>
<li>Ensure that the model is set to <code>llama-3.3-70b-instruct-fp8-fast</code>.</li>
<li>In <strong>MCP Servers</strong>, set <strong>URL</strong> to <code>https://[my-mcp-url].workers.dev/sse</code>.</li>
<li>Click <strong>Connect</strong>.</li>
<li>Status should update to <strong>Connected</strong> and it should list 23 available tools.</li>
</ol>
<p>You can now start to interact with the model, and it will run necessary the tools to accomplish what was requested.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3654.md")
</aside>
<p>Try this sequence of instructions to see Playwright MCP in action:</p>
<ol>
<li>&quot;Go to demo.playwright.dev/todomvc&quot;</li>
<li>&quot;Create some todo entry&quot;</li>
<li>&quot;Nice. Now create a todo in parrot style&quot;</li>
<li>&quot;And create another todo in Yoda style&quot;</li>
<li>&quot;Take a screenshot&quot;</li>
</ol>
<p>You can also use other MCP clients like <a href="https://github.com/cloudflare/playwright-mcp/blob/main/cloudflare/example/README.md#use-with-claude-desktop">Claude Desktop</a>.</p>
<p>Check our <a href="https://github.com/cloudflare/playwright-mcp">GitHub page</a> for more examples and MCP client configuration options, and refer to the developer documentation on how to <a href="/agents/">build Agents on Cloudflare</a>.</p>
