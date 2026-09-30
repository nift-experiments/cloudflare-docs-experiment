---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/sandbox/
  description: Give agents isolated Linux environments for running code, managing files, and executing commands.
  full_title: Sandbox · Cloudflare Agents docs
  head_html: <title>Sandbox · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Give agents isolated Linux environments for running code, managing files, and executing commands."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/sandbox/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/sandbox/index.md"><meta property="og:title" content="Sandbox · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Give agents isolated Linux environments for running code, managing files, and executing commands."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/sandbox/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/sandbox/#page","headline":"Sandbox \u00b7 Cloudflare Agents docs","description":"Give agents isolated Linux environments for running code, managing files, and executing commands.","url":"https://developers.cloudflare.com/agents/tools/sandbox/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/sandbox/
  schema: 1
---
<p>Agents can use <a href="/sandbox/">Sandbox</a> to run code in isolated container environments. Use Sandbox when an agent needs a real filesystem, shell commands, language runtimes, package installation, or long-lived project state that should not run inside the agent's own Worker isolate.</p>
<p>Sandbox is built on <a href="/containers/">Cloudflare Containers</a> and exposes a TypeScript API for command execution, file operations, background processes, and service previews.</p>
<h2 id="when-to-use-sandbox">When to use Sandbox</h2>
<p>Use Sandbox for agents that need to:</p>
<ul>
<li>Run untrusted or model-generated code in isolation.</li>
<li>Execute Python, Node.js, shell commands, or package managers.</li>
<li>Read, write, and manage project files.</li>
<li>Run tests, linters, build tools, or data analysis scripts.</li>
<li>Maintain a workspace across multiple agent turns.</li>
</ul>
<h2 id="basic-pattern">Basic pattern</h2>
<p>Bind the Sandbox Durable Object to your Worker, then access a sandbox from your agent methods with <code>getSandbox()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1841.md")
</div>
<h2 id="configuration">Configuration</h2>
<p>Configure the Sandbox container, Durable Object binding, and migration in <code>wrangler.jsonc</code>.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/1842.md")
</div>
<h2 id="sandbox-and-agent-state">Sandbox and agent state</h2>
<p>Use agent state for user-visible progress and small metadata. Use the sandbox filesystem for workspace files, generated code, package installs, logs, and artifacts.</p>
<p>For long-running sandbox work, pair Sandbox with <a href="/agents/runtime/execution/durable-execution/">durable execution with fibers</a> or <a href="/agents/runtime/execution/run-workflows/">Workflows</a> so the agent can recover or report progress if work outlives a single request.</p>
<h2 id="related-resources">Related resources</h2>
<div class="nb-card nb-link-card"><h3 id="card-sandbox-sdk-sandbox"><a href="/sandbox/">Sandbox SDK</a></h3><p>Full Sandbox documentation for commands, files, sessions, and deployment.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-execute-commands-sandbox-guides-execute-commands"><a href="/sandbox/guides/execute-commands/">Execute commands</a></h3><p>Run shell commands in a sandbox environment.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-manage-files-sandbox-guides-manage-files"><a href="/sandbox/guides/manage-files/">Manage files</a></h3><p>Read, write, upload, and download sandbox files.</p></div>
