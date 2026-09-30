---
cp9:
  canonical: https://developers.cloudflare.com/agents/examples/browser-agent/
  description: Build an agent that uses Browser Run tools to inspect pages, capture screenshots, scrape rendered content, and debug frontend issues.
  full_title: Browser agent · Cloudflare Agents docs
  head_html: <title>Browser agent · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Build an agent that uses Browser Run tools to inspect pages, capture screenshots, scrape rendered content, and debug frontend issues."><link rel="canonical" href="https://developers.cloudflare.com/agents/examples/browser-agent/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/examples/browser-agent/index.md"><meta property="og:title" content="Browser agent · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build an agent that uses Browser Run tools to inspect pages, capture screenshots, scrape rendered content, and debug frontend issues."><meta property="og:url" content="https://developers.cloudflare.com/agents/examples/browser-agent/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/examples/browser-agent/#page","headline":"Browser agent \u00b7 Cloudflare Agents docs","description":"Build an agent that uses Browser Run tools to inspect pages, capture screenshots, scrape rendered content, and debug frontend issues.","url":"https://developers.cloudflare.com/agents/examples/browser-agent/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/examples/browser-agent/
  schema: 1
---
<p>Build an agent that can browse the web, inspect pages, capture screenshots, and debug frontend issues with <a href="/browser-run/">Browser Run</a> tools. <span class="nb-badge">Beta</span></p>
<p>Instead of a fixed set of browser actions (click, screenshot, navigate), the LLM writes JavaScript code that runs CDP commands against a live browser session — accessing all domains, commands, events, and types in the protocol.</p>
<p>Two tools are provided:</p>
<table>
<thead>
<tr>
<th>Tool</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>browser_search</code></td>
<td>Query the CDP spec to discover commands, events, and types. The spec is fetched dynamically from the browser's CDP endpoint and cached.</td>
</tr>
<tr>
<td><code>browser_execute</code></td>
<td>Run CDP commands against a live browser via a <code>cdp</code> helper. Each call opens a fresh browser session, executes the code, and closes it.</td>
</tr>
</tbody>
</table>
<h2 id="when-to-use-browser-tools">When to use browser tools</h2>
<p>Browser tools are useful when your agent needs to:</p>
<ul>
<li><strong>Inspect web pages</strong> — DOM structure, computed styles, accessibility tree</li>
<li><strong>Debug frontend issues</strong> — network waterfalls, console errors, performance traces</li>
<li><strong>Scrape structured data</strong> — extract content from rendered pages</li>
<li><strong>Capture screenshots or PDFs</strong> — visual snapshots of web content</li>
<li><strong>Profile performance</strong> — Core Web Vitals, JavaScript profiling, memory analysis</li>
</ul>
<p>For basic page fetches that do not need a rendered DOM, use <code>fetch()</code> instead.</p>
<h2 id="install">Install</h2>
<p>Browser tools require the Agents SDK and <code>@cloudflare/codemode</code>:</p>
<pre tabindex="0"><code class="language-sh">npm install agents @cloudflare/codemode ai zod&#10;</code></pre>
<h2 id="quick-start">Quick start</h2>
<h3 id="1-configure-bindings"><ol>
<li>Configure bindings</li>
</ol></h3>
<p>Add the Browser Run (formerly Browser Rendering) and Worker Loader bindings to your wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1929.md")
</div>
<h3 id="2-create-browser-tools"><ol start="2">
<li>Create browser tools</li>
</ol></h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1930.md")
</div>
<p>To connect to a custom CDP endpoint instead of the Browser Run binding, pass <code>cdpUrl</code>.</p>
<h3 id="3-use-with-streamtext"><ol start="3">
<li>Use with streamText</li>
</ol></h3>
<p>Pass browser tools alongside your other tools. The <code>model</code> can be any AI SDK provider — here using Workers AI:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1931.md")
</div>
<p>Both tools accept a <code>code</code> parameter containing a JavaScript async arrow function. The sandbox injects globals depending on the tool — <code>spec</code> for <code>browser_search</code> and <code>cdp</code> for <code>browser_execute</code>.</p>
<p>When the LLM uses <code>browser_search</code>, the code queries the CDP spec via the injected <code>spec</code> object:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const s = await spec.get();&#10;	return s.domains&#10;		.find((d) =&gt; d.name === &quot;Network&quot;)&#10;		.commands.map((c) =&gt; ({ method: c.method, description: c.description }));&#10;};&#10;</code></pre>
<p>When the LLM uses <code>browser_execute</code>, the code runs CDP commands via the injected <code>cdp</code> helper:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const { targetId } = await cdp.send(&quot;Target.createTarget&quot;, {&#10;		url: &quot;https://example.com&quot;,&#10;	});&#10;	const sessionId = await cdp.attachToTarget(targetId);&#10;	const { root } = await cdp.send(&quot;DOM.getDocument&quot;, {}, { sessionId });&#10;	const { outerHTML } = await cdp.send(&#10;		&quot;DOM.getOuterHTML&quot;,&#10;		{ nodeId: root.nodeId },&#10;		{ sessionId },&#10;	);&#10;	await cdp.send(&quot;Target.closeTarget&quot;, { targetId });&#10;	return outerHTML;&#10;};&#10;</code></pre>
<h2 id="use-with-an-agent">Use with an Agent</h2>
<p>The typical pattern is to create browser tools inside an <a href="/agents/communication-channels/chat/chat-agents/"><code>AIChatAgent</code></a> message handler, which gives you message persistence and streaming:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1932.md")
</div>
<h2 id="tanstack-ai">TanStack AI</h2>
<p>For TanStack AI, use the <code>/tanstack-ai</code> export:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1933.md")
</div>
<h2 id="execution-model">Execution model</h2>
<ul>
<li><code>browser_search</code> fetches the live CDP protocol from the browser's <code>/json/protocol</code> endpoint and caches it briefly.</li>
<li><code>browser_execute</code> opens a fresh browser session for each call, exposes a small <code>cdp</code> helper API to sandboxed code, and closes the session when execution finishes.</li>
<li>LLM-generated code runs in a Worker sandbox. CDP traffic stays in the host Worker.</li>
</ul>
<h2 id="cdp-helper-api">CDP helper API</h2>
<p>Inside <code>browser_execute</code>, the following functions are available to the sandboxed code.</p>
<h3 id="cdp-send-method-params-options"><code>cdp.send(method, params?, options?)</code></h3>
<p>Send a CDP command and wait for the response.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>method</code></td>
<td><code>string</code></td>
<td>CDP method, for example <code>&quot;DOM.getDocument&quot;</code> or <code>&quot;Network.enable&quot;</code></td>
</tr>
<tr>
<td><code>params</code></td>
<td><code>unknown</code></td>
<td>Method parameters</td>
</tr>
<tr>
<td><code>options.timeoutMs</code></td>
<td><code>number</code></td>
<td>Per-command timeout (default: 10 seconds)</td>
</tr>
<tr>
<td><code>options.sessionId</code></td>
<td><code>string</code></td>
<td>Target session ID (required for page-scoped commands)</td>
</tr>
</tbody>
</table>
<h3 id="cdp-attachtotarget-targetid-options"><code>cdp.attachToTarget(targetId, options?)</code></h3>
<p>Attach to a target and get a session ID. Uses <code>Target.attachToTarget</code> with <code>flatten: true</code>.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>targetId</code></td>
<td><code>string</code></td>
<td>The target to attach to</td>
</tr>
<tr>
<td><code>options.timeoutMs</code></td>
<td><code>number</code></td>
<td>Timeout for the attach command</td>
</tr>
</tbody>
</table>
<p>Returns the <code>sessionId</code> string.</p>
<h3 id="cdp-getdebuglog-limit"><code>cdp.getDebugLog(limit?)</code></h3>
<p>Get recent CDP debug log entries (sends, receives, errors). Defaults to the last 50 entries, max 400.</p>
<h3 id="cdp-cleardebuglog"><code>cdp.clearDebugLog()</code></h3>
<p>Clear the debug log buffer.</p>
<h2 id="configuration">Configuration</h2>
<h3 id="createbrowsertools-options"><code>createBrowserTools(options)</code></h3>
<p>Returns AI SDK tools (<code>browser_search</code> and <code>browser_execute</code>).</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Type</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>browser</code></td>
<td><code>Fetcher</code></td>
<td>—</td>
<td>Browser Run binding</td>
</tr>
<tr>
<td><code>cdpUrl</code></td>
<td><code>string</code></td>
<td>—</td>
<td>Optional override for a custom CDP endpoint</td>
</tr>
<tr>
<td><code>cdpHeaders</code></td>
<td><code>Record&lt;string, string&gt;</code></td>
<td>—</td>
<td>Headers for CDP URL discovery (for example, Cloudflare Access)</td>
</tr>
<tr>
<td><code>loader</code></td>
<td><code>WorkerLoader</code></td>
<td>required</td>
<td>Worker Loader binding for sandboxed execution</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td><code>number</code></td>
<td><code>30000</code></td>
<td>Execution timeout in milliseconds</td>
</tr>
</tbody>
</table>
<p>Either <code>browser</code> or <code>cdpUrl</code> must be provided. When both are set, <code>cdpUrl</code> takes priority.</p>
<h3 id="raw-access">Raw access</h3>
<p>For custom integrations, import the building blocks directly:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1934.md")
</div>
<h2 id="local-development">Local development</h2>
<p>Recent Wrangler releases support Browser Run in local development. <code>npx wrangler dev</code> provisions the browser automatically, so the same <code>browser: env.BROWSER</code> setup works locally and when deployed.</p>
<p>Use <code>cdpUrl</code> only when you intentionally want to connect to some other CDP-compatible browser endpoint, such as a tunnel or a manually managed Chrome instance.</p>
<h2 id="security-considerations">Security considerations</h2>
<ul>
<li>LLM-generated code runs in <strong>isolated Worker sandboxes</strong> — each execution gets its own Worker instance</li>
<li>External network access (<code>fetch</code>, <code>connect</code>) is <strong>blocked</strong> in the sandbox at the runtime level</li>
<li>CDP commands are dispatched via Workers RPC — the WebSocket lives in the host, not the sandbox</li>
<li>The CDP spec stays on the server — only query results flow to the LLM</li>
<li>Responses are truncated to approximately 6,000 tokens to prevent context window overflow</li>
</ul>
<h2 id="current-limitations">Current limitations</h2>
<ul>
<li><strong>One session per execute call</strong> — each <code>browser_execute</code> invocation opens a fresh browser session. Multi-step workflows must be completed within a single code block.</li>
<li><strong>No authenticated sessions</strong> — the browser starts without any cookies or login state.</li>
<li>Requires <code>@cloudflare/codemode</code> as a peer dependency.</li>
<li>Limited to JavaScript execution in the sandbox (no TypeScript syntax).</li>
</ul>
<hr />
<h2 id="using-puppeteer-directly">Using Puppeteer directly</h2>
<p>If you prefer to control the browser programmatically without LLM-generated code, you can use Puppeteer with the <a href="/browser-run/">Browser Run</a> API directly.</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1935.md")
</div>
<p>Add the browser binding to your wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1936.md")
</div>
<h2 id="using-browserbase">Using Browserbase</h2>
<p>You can also use <a href="https://docs.browserbase.com/integrations/cloudflare/typescript">Browserbase</a> by using the Browserbase API directly from within your Agent.</p>
<p>Once you have your <a href="https://docs.browserbase.com/integrations/cloudflare/typescript">Browserbase API key</a>, you can add it to your Agent by creating a <a href="/workers/configuration/secrets/">secret</a>:</p>
<pre tabindex="0"><code class="language-sh">cd your-agent-project-folder&#10;npx wrangler@latest secret put BROWSERBASE_API_KEY&#10;</code></pre>
<p>Install the <code>@cloudflare/puppeteer</code> package and use it from within your Agent to call the Browserbase API:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/puppeteer</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/puppeteer" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1937.md")
</div>
