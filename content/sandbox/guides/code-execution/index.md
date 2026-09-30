---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/guides/code-execution/
  description: Execute Python and JavaScript code with rich outputs.
  full_title: Use code interpreter · Cloudflare Sandbox SDK docs
  head_html: <title>Use code interpreter · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Execute Python and JavaScript code with rich outputs."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/guides/code-execution/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/guides/code-execution/index.md"><meta property="og:title" content="Use code interpreter · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Execute Python and JavaScript code with rich outputs."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/guides/code-execution/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/guides/code-execution/#page","headline":"Use code interpreter \u00b7 Cloudflare Sandbox SDK docs","description":"Execute Python and JavaScript code with rich outputs.","url":"https://developers.cloudflare.com/sandbox/guides/code-execution/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/guides/code-execution/
  schema: 1
---
<p>This guide shows you how to execute Python and JavaScript code with rich outputs using the Code Interpreter API.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13475.md")
</aside>
<h2 id="when-to-use-code-interpreter">When to use code interpreter</h2>
<p>Use the Code Interpreter API for <strong>simple, direct code execution</strong> with minimal setup:</p>
<ul>
<li><strong>Quick code execution</strong> - Run Python/JS code without environment setup</li>
<li><strong>Rich outputs</strong> - Get charts, tables, images, HTML automatically</li>
<li><strong>AI-generated code</strong> - Execute LLM-generated code with structured results</li>
<li><strong>Persistent state</strong> - Variables preserved between executions in the same context</li>
</ul>
<p>Use <code>exec()</code> for <strong>advanced or custom workflows</strong>:</p>
<ul>
<li><strong>System operations</strong> - Install packages, manage files, run builds</li>
<li><strong>Custom environments</strong> - Configure specific versions, dependencies</li>
<li><strong>Shell commands</strong> - Git operations, system utilities, complex pipelines</li>
<li><strong>Long-running processes</strong> - Background services, servers</li>
</ul>
<h2 id="create-an-execution-context">Create an execution context</h2>
<p>Code contexts maintain state between executions:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13476.md")
</div>
<h2 id="execute-code">Execute code</h2>
<h3 id="simple-execution">Simple execution</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13477.md")
</div>
<h3 id="state-within-a-context">State within a context</h3>
<p>Variables and imports remain available between executions in the same context, as long as the container stays active:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13478.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13474.md")
</aside>
<h2 id="handle-rich-outputs">Handle rich outputs</h2>
<p>The code interpreter returns multiple output formats:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13479.md")
</div>
<h2 id="stream-execution-output">Stream execution output</h2>
<p>For long-running code, stream output in real-time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13480.md")
</div>
<h2 id="execute-ai-generated-code">Execute AI-generated code</h2>
<p>Run LLM-generated code safely in a sandbox:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13481.md")
</div>
<h2 id="manage-contexts">Manage contexts</h2>
<h3 id="list-all-contexts">List all contexts</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13482.md")
</div>
<h3 id="delete-contexts">Delete contexts</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13483.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Clean up contexts</strong> - Delete contexts when done to free resources</li>
<li><strong>Handle errors</strong> - Always check <code>result.success</code> and <code>result.error</code></li>
<li><strong>Stream long operations</strong> - Use streaming for code that takes &gt;2 seconds</li>
<li><strong>Validate AI code</strong> - Review generated code before execution</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/interpreter/">Code Interpreter API reference</a> - Complete API documentation</li>
<li><a href="/sandbox/tutorials/ai-code-executor/">AI code executor tutorial</a> - Build complete AI executor</li>
<li><a href="/sandbox/guides/execute-commands/">Execute commands guide</a> - Lower-level command execution</li>
</ul>
