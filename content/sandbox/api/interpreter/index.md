---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/api/interpreter/
  description: Execute Python, JavaScript, and TypeScript code with rich output formats in Sandbox SDK.
  full_title: Code interpreter · Cloudflare Sandbox SDK docs
  head_html: <title>Code interpreter · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Execute Python, JavaScript, and TypeScript code with rich output formats in Sandbox SDK."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/api/interpreter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/api/interpreter/index.md"><meta property="og:title" content="Code interpreter · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Execute Python, JavaScript, and TypeScript code with rich output formats in Sandbox SDK."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/api/interpreter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/api/interpreter/#page","headline":"Code interpreter \u00b7 Cloudflare Sandbox SDK docs","description":"Execute Python, JavaScript, and TypeScript code with rich output formats in Sandbox SDK.","url":"https://developers.cloudflare.com/sandbox/api/interpreter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/api/interpreter/
  schema: 1
---
<p>Execute Python, JavaScript, and TypeScript code with support for data visualizations, tables, and rich output formats. Contexts maintain state (variables, imports, functions) across executions.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13635.md")
</aside>
<h2 id="methods">Methods</h2>
<h3 id="createcodecontext"><code>createCodeContext()</code></h3>
<p>Create a persistent execution context for running code.</p>
<pre tabindex="0"><code class="language-ts">const context = await sandbox.createCodeContext(options?: CreateContextOptions): Promise&lt;CodeContext&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>options</code> (optional):
<ul>
<li><code>language</code> - <code>&quot;python&quot; | &quot;javascript&quot; | &quot;typescript&quot;</code> (default: <code>&quot;python&quot;</code>)</li>
<li><code>cwd</code> - Working directory (default: <code>&quot;/workspace&quot;</code>)</li>
<li><code>envVars</code> - Environment variables</li>
<li><code>timeout</code> - Request timeout in milliseconds (default: 30000)</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;CodeContext&gt;</code> with <code>id</code>, <code>language</code>, <code>cwd</code>, <code>createdAt</code>, <code>lastUsed</code></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13636.md")
</div>
<h3 id="runcode"><code>runCode()</code></h3>
<p>Execute code in a context and return the complete result.</p>
<pre tabindex="0"><code class="language-ts">const result = await sandbox.runCode(code: string, options?: RunCodeOptions): Promise&lt;ExecutionResult&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>code</code> - The code to execute (required)</li>
<li><code>options</code> (optional):
<ul>
<li><code>context</code> - Context to run in (recommended - see below)</li>
<li><code>language</code> - <code>&quot;python&quot; | &quot;javascript&quot; | &quot;typescript&quot;</code> (default: <code>&quot;python&quot;</code>)</li>
<li><code>timeout</code> - Execution timeout in milliseconds (default: 60000)</li>
<li><code>onStdout</code>, <code>onStderr</code>, <code>onResult</code>, <code>onError</code> - Streaming callbacks</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ExecutionResult&gt;</code> with:</p>
<ul>
<li><code>code</code> - The executed code</li>
<li><code>logs</code> - <code>stdout</code> and <code>stderr</code> arrays</li>
<li><code>results</code> - Array of rich outputs (see <a href="#rich-output-formats">Rich Output Formats</a>)</li>
<li><code>error</code> - Execution error if any</li>
<li><code>executionCount</code> - Execution counter</li>
</ul>
<p><strong>Recommended usage - create explicit context</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13637.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="default-context-behavior">Default context behavior</h3>
@markup("md", "content/.markup/bodies/13634.md")
</aside>
<p><strong>Error handling</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13638.md")
</div>
<p><strong>JavaScript and TypeScript features</strong>:</p>
<p>JavaScript and TypeScript code execution supports top-level <code>await</code> and persistent variables across executions within the same context.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13639.md")
</div>
<p>Variables declared with <code>const</code>, <code>let</code>, or <code>var</code> persist across executions, enabling multi-step workflows:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13640.md")
</div>
<h3 id="listcodecontexts"><code>listCodeContexts()</code></h3>
<p>List all active code execution contexts.</p>
<pre tabindex="0"><code class="language-ts">const contexts = await sandbox.listCodeContexts(): Promise&lt;CodeContext[]&gt;&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13641.md")
</div>
<h3 id="deletecodecontext"><code>deleteCodeContext()</code></h3>
<p>Delete a code execution context and free its resources.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.deleteCodeContext(contextId: string): Promise&lt;void&gt;&#10;</code></pre>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13642.md")
</div>
<h2 id="rich-output-formats">Rich Output Formats</h2>
<p>Results include: <code>text</code>, <code>html</code>, <code>png</code>, <code>jpeg</code>, <code>svg</code>, <code>latex</code>, <code>markdown</code>, <code>json</code>, <code>chart</code>, <code>data</code></p>
<p><strong>Charts (matplotlib)</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13643.md")
</div>
<p><strong>Tables (pandas)</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13644.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/tutorials/ai-code-executor/">Build an AI Code Executor</a> - Complete tutorial</li>
<li><a href="/sandbox/api/commands/">Commands API</a> - Lower-level command execution</li>
<li><a href="/sandbox/api/files/">Files API</a> - File operations</li>
</ul>
