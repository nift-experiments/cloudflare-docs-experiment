---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/
  description: Create a Code Mode runtime with connectors, direct host APIs, durable approvals, rollback, execution history, and reusable snippets.
  full_title: Create a durable Code Mode runtime · Cloudflare Agents docs
  head_html: <title>Create a durable Code Mode runtime · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a Code Mode runtime with connectors, direct host APIs, durable approvals, rollback, execution history, and reusable snippets."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/index.md"><meta property="og:title" content="Create a durable Code Mode runtime · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a Code Mode runtime with connectors, direct host APIs, durable approvals, rollback, execution history, and reusable snippets."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/#page","headline":"Create a durable Code Mode runtime \u00b7 Cloudflare Agents docs","description":"Create a Code Mode runtime with connectors, direct host APIs, durable approvals, rollback, execution history, and reusable snippets.","url":"https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/codemode/durable-runtime/
  schema: 1
---
<p>This guide adds a durable Code Mode runtime to an Agents SDK application. The runtime stores execution history, pending approvals, and snippets across Durable Object hibernation.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2679.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need an existing Agents SDK application with a Durable Object and Vite. The example uses <code>AIChatAgent</code> and the AI SDK.</p>
<h2 id="integrate-code-mode">Integrate Code Mode</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2684.md")
</div>
<h2 id="use-the-runtime-without-the-ai-sdk">Use the runtime without the AI SDK</h2>
<p>Use <code>execute()</code>, <code>search()</code>, and <code>describe()</code> when an MCP server or another host invokes Code Mode without an AI SDK tool adapter:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2685.md")
</div>
<p><code>search()</code> and <code>describe()</code> do not run sandbox code. Their results include <code>requiresApproval: true</code> for connector methods that pause before execution.</p>
<p><code>execute()</code> returns the same durable result as the model-facing tool. A result can complete, pause, or contain an execution error. Resolve a paused result with <code>approve()</code> or <code>reject()</code>.</p>
<h2 id="verify-the-integration">Verify the integration</h2>
<p>Ask the model to list saved notes. The model receives one <code>codemode</code> tool and can discover connector methods inside the sandbox:</p>
<pre tabindex="0"><code class="language-js">async () =&gt; {&#10;	const matches = await codemode.search(&quot;list saved notes&quot;);&#10;	const docs = await codemode.describe(matches.results[0].path);&#10;	const savedNotes = await notes.listNotes();&#10;&#10;	return { docs, savedNotes };&#10;};&#10;</code></pre>
<p>When the model calls <code>notes.createNote()</code>, the execution pauses. Use <code>pendingApprovals()</code> to show the pending action. Pass its <code>executionId</code> to <code>approveExecution()</code>, or pass both <code>executionId</code> and <code>seq</code> to <code>rejectExecution()</code>.</p>
<p>Approval resumes the same script through replay. Completed calls return recorded results instead of running again. Rejection ends the paused execution without undoing earlier actions.</p>
<p>Call <code>rollbackExecution()</code> to compensate for applied calls whose currently configured connector provides <code>revert</code>. Save only completed executions as snippets.</p>
