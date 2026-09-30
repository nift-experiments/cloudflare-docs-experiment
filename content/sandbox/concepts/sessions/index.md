---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/concepts/sessions/
  description: Sandbox SDK sessions are shell execution contexts within a single sandbox.
  full_title: Session management · Cloudflare Sandbox SDK docs
  head_html: <title>Session management · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Sandbox SDK sessions are shell execution contexts within a single sandbox."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/concepts/sessions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/concepts/sessions/index.md"><meta property="og:title" content="Session management · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Sandbox SDK sessions are shell execution contexts within a single sandbox."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/concepts/sessions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/concepts/sessions/#page","headline":"Session management \u00b7 Cloudflare Sandbox SDK docs","description":"Sandbox SDK sessions are shell execution contexts within a single sandbox.","url":"https://developers.cloudflare.com/sandbox/concepts/sessions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/concepts/sessions/
  schema: 1
---
<p>Sessions are bash shell execution contexts within a sandbox. Think of them as terminal tabs in the same computer.</p>
<ul>
<li><strong>Sandbox</strong> = A user or task workspace</li>
<li><strong>Session</strong> = A shell in that workspace</li>
</ul>
<p>Sessions are useful for organizing work inside one sandbox. They are not a security boundary between users because sessions share the same filesystem and process space.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13568.md")
</aside>
<h2 id="default-session">Default session</h2>
<p>By default, every sandbox has a default session that maintains shell state between commands while the container is active:</p>
<pre tabindex="0"><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, &#x27;my-sandbox&#x27;);&#10;&#10;// These commands run in the default session&#10;await sandbox.exec(&quot;cd /app&quot;);&#10;await sandbox.exec(&quot;pwd&quot;);  // Output: /app&#10;&#10;await sandbox.exec(&quot;export MY_VAR=hello&quot;);&#10;await sandbox.exec(&quot;echo $MY_VAR&quot;);  // Output: hello&#10;</code></pre>
<p>Working directory, environment variables, and exported variables carry over between commands. This state resets if the container restarts due to inactivity.</p>
<p>If you set <code>enableDefaultSession: false</code> when calling <code>getSandbox()</code>, operations without an explicit <code>sessionId</code> run in isolation instead of using the default session:</p>
<pre tabindex="0"><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, &#x27;my-sandbox&#x27;, {&#10;  enableDefaultSession: false&#10;});&#10;&#10;await sandbox.exec(&quot;cd /app&quot;);&#10;await sandbox.exec(&quot;pwd&quot;);  // Output: /workspace (cd was not inherited)&#10;</code></pre>
<p>Without the default session, the second command does not inherit shell state from the first command. It is recommended that you always apply this setting as it will become the default in a future Sandbox SDK release. Create or retrieve an explicit session when you want commands to share shell state.</p>
<h3 id="automatic-session-creation">Automatic session creation</h3>
<p>The container automatically creates sessions on first use. If you reference a non-existent session ID, the container creates it with default settings:</p>
<pre tabindex="0"><code class="language-typescript">// This session does not exist yet&#10;const result = await sandbox.exec(&#x27;echo hello&#x27;, { sessionId: &#x27;new-session&#x27; });&#10;// Container automatically creates &#x27;new-session&#x27; with defaults:&#10;// - cwd: &#x27;/workspace&#x27;&#10;// - env: {} (empty)&#10;</code></pre>
<p>This behavior is particularly relevant after deleting a session:</p>
<pre tabindex="0"><code class="language-typescript">// Create and configure a session&#10;const session = await sandbox.createSession({&#10;  id: &#x27;temp&#x27;,&#10;  env: { MY_VAR: &#x27;value&#x27; }&#10;});&#10;&#10;// Delete the session&#10;await sandbox.deleteSession(&#x27;temp&#x27;);&#10;&#10;// Using the same session ID again works - auto-created with defaults&#10;const result = await sandbox.exec(&#x27;echo $MY_VAR&#x27;, { sessionId: &#x27;temp&#x27; });&#10;// Output: (empty) - MY_VAR is not set in the freshly created session&#10;</code></pre>
<p>This auto-creation means commands still run when they reference a non-existent session. However, custom configuration (environment variables, working directory) is lost after deletion.</p>
<h2 id="creating-sessions">Creating sessions</h2>
<p>Create additional sessions for separate workflows in the same sandbox:</p>
<pre tabindex="0"><code class="language-typescript">const buildSession = await sandbox.createSession({&#10;  id: &quot;build&quot;,&#10;  env: { NODE_ENV: &quot;production&quot; },&#10;  cwd: &quot;/build&quot;&#10;});&#10;&#10;const testSession = await sandbox.createSession({&#10;  id: &quot;test&quot;,&#10;  env: { NODE_ENV: &quot;test&quot; },&#10;  cwd: &quot;/test&quot;&#10;});&#10;&#10;// Different shell contexts&#10;await buildSession.exec(&quot;npm run build&quot;);&#10;await testSession.exec(&quot;npm test&quot;);&#10;</code></pre>
<p>You can also set a default command timeout for all commands in a session:</p>
<pre tabindex="0"><code class="language-typescript">const session = await sandbox.createSession({&#10;  id: &quot;ci&quot;,&#10;  commandTimeoutMs: 30000 // 30s timeout for all commands&#10;});&#10;&#10;await session.exec(&quot;npm test&quot;); // Times out after 30s if still running&#10;</code></pre>
<p>Individual commands can override the session timeout with the <code>timeout</code> option on <code>exec()</code>. For more details, refer to the <a href="/sandbox/api/sessions/">Sessions API</a> and the <a href="/sandbox/guides/execute-commands/#timeouts">execute commands guide</a>.</p>
<h2 id="what-is-scoped-to-a-session">What is scoped to a session</h2>
<p>Each session has its own:</p>
<p><strong>Shell environment</strong>:</p>
<pre tabindex="0"><code class="language-typescript">await session1.exec(&quot;export MY_VAR=hello&quot;);&#10;await session2.exec(&quot;echo $MY_VAR&quot;);  // Empty - different shell&#10;</code></pre>
<p><strong>Working directory</strong>:</p>
<pre tabindex="0"><code class="language-typescript">await session1.exec(&quot;cd /workspace/project1&quot;);&#10;await session2.exec(&quot;pwd&quot;);  // Different working directory&#10;</code></pre>
<p><strong>Environment variables</strong> (set via <code>createSession</code> options):</p>
<pre tabindex="0"><code class="language-typescript">const session1 = await sandbox.createSession({&#10;  env: { API_KEY: &#x27;key-1&#x27; }&#10;});&#10;const session2 = await sandbox.createSession({&#10;  env: { API_KEY: &#x27;key-2&#x27; }&#10;});&#10;</code></pre>
<h2 id="what-is-shared-across-sessions">What is shared across sessions</h2>
<p>All sessions in a sandbox share:</p>
<p><strong>Filesystem</strong>:</p>
<pre tabindex="0"><code class="language-typescript">await session1.writeFile(&#x27;/workspace/file.txt&#x27;, &#x27;data&#x27;);&#10;await session2.readFile(&#x27;/workspace/file.txt&#x27;);  // Can read it&#10;</code></pre>
<p><strong>Processes</strong>:</p>
<pre tabindex="0"><code class="language-typescript">await session1.startProcess(&#x27;node server.js&#x27;);&#10;await session2.listProcesses();  // Sees the server&#10;</code></pre>
<h2 id="when-to-use-sessions">When to use sessions</h2>
<p><strong>Use sessions when</strong>:</p>
<ul>
<li>You need separate shell state for one user's tasks</li>
<li>Running parallel operations with different environments</li>
<li>Keeping AI agent credentials separate from app runtime</li>
</ul>
<p><strong>Example - separate dev and runtime environments</strong>:</p>
<pre tabindex="0"><code class="language-typescript">// Phase 1: AI agent writes code (with API keys)&#10;const devSession = await sandbox.createSession({&#10;  id: &quot;dev&quot;,&#10;  env: { ANTHROPIC_API_KEY: env.ANTHROPIC_API_KEY }&#10;});&#10;await devSession.exec(&#x27;ai-tool &quot;build a web server&quot;&#x27;);&#10;&#10;// Phase 2: Run the code (without API keys)&#10;const appSession = await sandbox.createSession({&#10;  id: &quot;app&quot;,&#10;  env: { PORT: &quot;3000&quot; }&#10;});&#10;await appSession.exec(&quot;node server.js&quot;);&#10;</code></pre>
<p><strong>Use separate sandboxes when</strong>:</p>
<ul>
<li>You need complete isolation for untrusted code</li>
<li>Different users need separate workspaces</li>
<li>User data must stay separated</li>
<li>Independent resource allocation is needed</li>
</ul>
<h2 id="best-practices">Best practices</h2>
<h3 id="session-cleanup">Session cleanup</h3>
<p><strong>Clean up temporary sessions</strong> to free resources while keeping the sandbox running:</p>
<pre tabindex="0"><code class="language-typescript">try {&#10;  const session = await sandbox.createSession({ id: &#x27;temp&#x27; });&#10;  await session.exec(&#x27;command&#x27;);&#10;} finally {&#10;  await sandbox.deleteSession(&#x27;temp&#x27;);&#10;}&#10;</code></pre>
<p><strong>Default session cannot be deleted</strong>:</p>
<pre tabindex="0"><code class="language-typescript">// This throws an error&#10;await sandbox.deleteSession(&#x27;default&#x27;);&#10;// Error: Cannot delete default session. Use sandbox.destroy() instead.&#10;</code></pre>
<h3 id="filesystem-scope">Filesystem scope</h3>
<p><strong>Sessions share the sandbox filesystem</strong> - file operations affect all sessions:</p>
<pre tabindex="0"><code class="language-typescript">// Bad - affects all sessions&#10;await session.exec(&#x27;rm -rf /workspace/*&#x27;);&#10;&#10;// For user data or untrusted code, use a separate sandbox&#10;const userSandbox = getSandbox(env.Sandbox, `user-${userId}`);&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/sandboxes/">Sandbox lifecycle</a> - Understanding sandbox management</li>
<li><a href="/sandbox/api/sessions/">Sessions API</a> - Complete session API reference</li>
</ul>
