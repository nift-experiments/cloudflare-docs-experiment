---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/codemode/browser/
  description: Run model-generated code against browser-owned tools with the Code Mode iframe executor and an Agent chat UI.
  full_title: Browser integration · Cloudflare Agents docs
  head_html: <title>Browser integration · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Run model-generated code against browser-owned tools with the Code Mode iframe executor and an Agent chat UI."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/codemode/browser/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/codemode/browser/index.md"><meta property="og:title" content="Browser integration · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run model-generated code against browser-owned tools with the Code Mode iframe executor and an Agent chat UI."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/codemode/browser/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/codemode/browser/#page","headline":"Browser integration \u00b7 Cloudflare Agents docs","description":"Run model-generated code against browser-owned tools with the Code Mode iframe executor and an Agent chat UI.","url":"https://developers.cloudflare.com/agents/tools/codemode/browser/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/codemode/browser/
  schema: 1
---
<p>Use <code>@cloudflare/codemode/browser</code> when your browser owns the tools that the model must orchestrate. For example, these tools might read page state, access browser APIs, or update data held by your application.</p>
<p>Code Mode is useful when the model must call several client tools with loops, conditions, or intermediate results. For a single browser action, use a standard client-side tool instead.</p>
<p>Code Mode presents those tools to the model as typed functions. The model writes one JavaScript async arrow function that can call several tools, combine their results, and apply control flow. <code>IframeSandboxExecutor</code> runs that generated code in a sandboxed iframe on the page.</p>
<p>This integration does not give an agent control of a remote browser. To inspect websites, capture screenshots, or automate pages with the Chrome DevTools Protocol (CDP), refer to <a href="/agents/tools/browser/">Browser tools</a>.</p>
<h2 id="install-code-mode">Install Code Mode</h2>
<p>Install the package in your client application:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @cloudflare/codemode</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/codemode" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @cloudflare/codemode</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/codemode" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @cloudflare/codemode</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/codemode" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @cloudflare/codemode</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/codemode" aria-label="Copy to clipboard">Copy</button></div></div>
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
