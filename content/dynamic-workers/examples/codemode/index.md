---
cp9:
  canonical: https://developers.cloudflare.com/dynamic-workers/examples/codemode/
  description: Project management chat app demonstrating code-as-tool. The LLM writes and executes JavaScript to orchestrate multiple tools in a single Dynamic Worker sandbox.
  full_title: Code Mode Example · Cloudflare Dynamic Workers docs
  head_html: <title>Code Mode Example · Cloudflare Dynamic Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Project management chat app demonstrating code-as-tool. The LLM writes and executes JavaScript to orchestrate multiple tools in a single Dynamic Worker sandbox."><link rel="canonical" href="https://developers.cloudflare.com/dynamic-workers/examples/codemode/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dynamic-workers/examples/codemode/index.md"><meta property="og:title" content="Code Mode Example · Cloudflare Dynamic Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Project management chat app demonstrating code-as-tool. The LLM writes and executes JavaScript to orchestrate multiple tools in a single Dynamic Worker sandbox."><meta property="og:url" content="https://developers.cloudflare.com/dynamic-workers/examples/codemode/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Dynamic Workers"><meta name="algolia_product_filter" content="Dynamic Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Dynamic Workers"><meta name="pcx_tags" content="AI,AI Agents,JavaScript,TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dynamic-workers/examples/codemode/#page","headline":"Code Mode Example \u00b7 Cloudflare Dynamic Workers docs","description":"Project management chat app demonstrating code-as-tool. The LLM writes and executes JavaScript to orchestrate multiple tools in a single Dynamic Worker sandbox.","url":"https://developers.cloudflare.com/dynamic-workers/examples/codemode/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","AI Agents","JavaScript","TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /dynamic-workers/examples/codemode/
  schema: 1
---
<p>This example shows how to use the <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> library with the <a href="https://www.npmjs.com/package/agents">Agents SDK</a> to build an agent where the LLM writes code to orchestrate tool calls, instead of calling them one at a time. This approach, called <a href="https://blog.cloudflare.com/code-mode/">Code Mode</a>, reduces tokens spent by up to 80%, returns better results, and avoids bloating the context window.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/codemode"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Workers" /></a></p>
<p>This example shows you how to:</p>
<ul>
<li>Define tools as plain functions with Zod schemas</li>
<li>Use <code>createCodeTool</code> to expose your tools to the LLM as a single &quot;write code&quot; tool</li>
<li>Use <code>DynamicWorkerExecutor</code> to safely run LLM-generated code</li>
<li>Wire it all together with <code>AIChatAgent</code> to handle chat over WebSockets</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>The agent uses three components from the <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> library and the <a href="https://www.npmjs.com/package/agents">Agents SDK</a>:</p>
<ul>
<li><strong><code>AIChatAgent</code> (<code>@cloudflare/ai-chat</code>)</strong>, your agent's base class. Handles chat over WebSockets, persists messages, and calls the LLM.</li>
<li><strong><code>createCodeTool</code> (<code>@cloudflare/codemode/ai</code>)</strong>, wraps your tools into a single <code>codemode</code> tool that accepts <code>{ code: string }</code>.</li>
<li><strong><code>DynamicWorkerExecutor</code> (<code>@cloudflare/codemode</code>)</strong>, runs the LLM-generated code in an isolated <a href="/dynamic-workers/">Dynamic Worker</a>.</li>
</ul>
<p>The flow:</p>
<ol>
<li>User sends a message over WebSocket.</li>
<li><code>AIChatAgent</code> passes it to the LLM with a single tool available: <code>codemode</code>.</li>
<li>The LLM writes JavaScript, for example <code>const projects = await codemode.listProjects()</code>, instead of making individual tool calls.</li>
<li><code>DynamicWorkerExecutor</code> spins up an isolated Worker and runs the code. Inside the sandbox, <code>codemode.listProjects()</code> calls your real <code>listProjects</code> implementation.</li>
<li>The result, any console output, and errors are returned to the LLM.</li>
<li>The LLM uses the result to respond to the user, or writes more code if it needs to.</li>
</ol>
<h3 id="dynamicworkerexecutor"><code>DynamicWorkerExecutor</code></h3>
<p><code>DynamicWorkerExecutor</code> is part of the <code>@cloudflare/codemode</code> library. When the LLM writes code that orchestrates your tools, that code needs to run somewhere safe. <code>DynamicWorkerExecutor</code> spins up an isolated Dynamic Worker for each execution using the Worker Loader binding. Inside the sandbox:</p>
<ul>
<li>A <code>codemode</code> proxy object routes calls like <code>codemode.createTask(...)</code> back to your real tool implementations over Workers RPC</li>
<li>Setting <code>globalOutbound</code> to <code>null</code> blocks <code>fetch()</code>, so the code can only reach the outside world through your tools</li>
<li><code>console.log</code> output is captured and returned alongside the result</li>
<li>Each execution gets its own Worker instance with a 30-second timeout</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8454.md")
</div>
<h3 id="createcodetool"><code>createCodeTool</code></h3>
<p><code>createCodeTool</code> is part of <code>@cloudflare/codemode</code>. It takes your tools and an executor, and returns a single AI SDK <code>tool()</code>. It:</p>
<ul>
<li>Generates TypeScript type declarations from your tools' Zod schemas, so the LLM knows what is available and what the argument shapes look like.</li>
<li>Puts those types in the tool's description, so the LLM sees a single tool with parameter <code>{ code: string }</code> and a description that includes the full typed API surface.</li>
<li>On execution, normalizes the LLM's code (strips markdown fences, wraps bare statements in async functions, auto-returns the last expression), then passes it to the executor.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8455.md")
</div>
<p>The LLM writes an async arrow function. <code>createCodeTool</code> normalizes it and hands it to the executor. The executor builds a Worker module with a <code>codemode</code> proxy, runs the code, and returns <code>{ code, result, logs }</code>.</p>
