---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/api/sessions/
  description: Create shell sessions with independent working directories and environment variables within a sandbox.
  full_title: Sessions · Cloudflare Sandbox SDK docs
  head_html: <title>Sessions · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Create shell sessions with independent working directories and environment variables within a sandbox."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/api/sessions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/api/sessions/index.md"><meta property="og:title" content="Sessions · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create shell sessions with independent working directories and environment variables within a sandbox."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/api/sessions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/api/sessions/#page","headline":"Sessions \u00b7 Cloudflare Sandbox SDK docs","description":"Create shell sessions with independent working directories and environment variables within a sandbox.","url":"https://developers.cloudflare.com/sandbox/api/sessions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/api/sessions/
  schema: 1
---
<p>Create shell sessions within a sandbox. Each session maintains its own shell state, environment variables, and working directory, while sharing the sandbox filesystem and process space. For more information, refer to <a href="/sandbox/concepts/sessions/">Session management</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13606.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13605.md")
</aside>
<h2 id="methods">Methods</h2>
<h3 id="createsession"><code>createSession()</code></h3>
<p>Create a new shell session.</p>
<pre tabindex="0"><code class="language-ts">const session = await sandbox.createSession(options?: SessionOptions): Promise&lt;ExecutionSession&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>options</code> (optional):
<ul>
<li><code>id</code> - Custom session ID (auto-generated if not provided)</li>
<li><code>env</code> - Environment variables for this session: <code>Record&lt;string, string | undefined&gt;</code></li>
<li><code>cwd</code> - Working directory (default: <code>&quot;/workspace&quot;</code>)</li>
<li><code>commandTimeoutMs</code> - Maximum time in milliseconds that any command in this session can run before timing out. Individual commands can override this with the <code>timeout</code> option on <code>exec()</code>.</li>
</ul>
</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ExecutionSession&gt;</code> with all sandbox methods bound to this session</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13607.md")
</div>
<h3 id="getsession"><code>getSession()</code></h3>
<p>Retrieve an existing session by ID.</p>
<pre tabindex="0"><code class="language-ts">const session = await sandbox.getSession(sessionId: string): Promise&lt;ExecutionSession&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>sessionId</code> - ID of an existing session</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;ExecutionSession&gt;</code> bound to the specified session</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13608.md")
</div>
<hr />
<h3 id="deletesession"><code>deleteSession()</code></h3>
<p>Delete a session and clean up its resources.</p>
<pre tabindex="0"><code class="language-ts">const result = await sandbox.deleteSession(sessionId: string): Promise&lt;SessionDeleteResult&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>sessionId</code> - ID of the session to delete (cannot be <code>&quot;default&quot;</code>)</li>
</ul>
<p><strong>Returns</strong>: <code>Promise&lt;SessionDeleteResult&gt;</code> containing:</p>
<ul>
<li><code>success</code> - Whether deletion succeeded</li>
<li><code>sessionId</code> - ID of the deleted session</li>
<li><code>timestamp</code> - Deletion timestamp</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13609.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13604.md")
</aside>
<hr />
<h3 id="setenvvars"><code>setEnvVars()</code></h3>
<p>Set environment variables in the sandbox.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.setEnvVars(envVars: Record&lt;string, string | undefined&gt;): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>envVars</code> - Key-value pairs of environment variables to set or unset
<ul>
<li><code>string</code> values: Set the environment variable</li>
<li><code>undefined</code> or <code>null</code> values: Unset the environment variable</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13603.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13610.md")
</div>
<hr />
<h2 id="executionsession-methods">ExecutionSession methods</h2>
<p>The <code>ExecutionSession</code> object has all sandbox methods bound to the specific session:</p>
<table>
<thead>
<tr>
<th>Category</th>
<th>Methods</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Commands</strong></td>
<td><a href="/sandbox/api/commands/#exec"><code>exec()</code></a>, <a href="/sandbox/api/commands/#execstream"><code>execStream()</code></a></td>
</tr>
<tr>
<td><strong>Processes</strong></td>
<td><a href="/sandbox/api/commands/#startprocess"><code>startProcess()</code></a>, <a href="/sandbox/api/commands/#listprocesses"><code>listProcesses()</code></a>, <a href="/sandbox/api/commands/#killprocess"><code>killProcess()</code></a>, <a href="/sandbox/api/commands/#killallprocesses"><code>killAllProcesses()</code></a>, <a href="/sandbox/api/commands/#getprocesslogs"><code>getProcessLogs()</code></a>, <a href="/sandbox/api/commands/#streamprocesslogs"><code>streamProcessLogs()</code></a></td>
</tr>
<tr>
<td><strong>Files</strong></td>
<td><a href="/sandbox/api/files/#writefile"><code>writeFile()</code></a>, <a href="/sandbox/api/files/#readfile"><code>readFile()</code></a>, <a href="/sandbox/api/files/#mkdir"><code>mkdir()</code></a>, <a href="/sandbox/api/files/#deletefile"><code>deleteFile()</code></a>, <a href="/sandbox/api/files/#renamefile"><code>renameFile()</code></a>, <a href="/sandbox/api/files/#movefile"><code>moveFile()</code></a>, <a href="/sandbox/api/files/#gitcheckout"><code>gitCheckout()</code></a></td>
</tr>
<tr>
<td><strong>Environment</strong></td>
<td><a href="/sandbox/api/sessions/#setenvvars"><code>setEnvVars()</code></a></td>
</tr>
<tr>
<td><strong>Terminal</strong></td>
<td><a href="/sandbox/api/terminal/#terminal"><code>terminal()</code></a></td>
</tr>
<tr>
<td><strong>Code Interpreter</strong></td>
<td><a href="/sandbox/api/interpreter/#createcodecontext"><code>createCodeContext()</code></a>, <a href="/sandbox/api/interpreter/#runcode"><code>runCode()</code></a>, <a href="/sandbox/api/interpreter/#listcodecontexts"><code>listCodeContexts()</code></a>, <a href="/sandbox/api/interpreter/#deletecodecontext"><code>deleteCodeContext()</code></a></td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/sessions/">Session management concept</a> - How sessions work</li>
<li><a href="/sandbox/api/commands/">Commands API</a> - Execute commands</li>
</ul>
