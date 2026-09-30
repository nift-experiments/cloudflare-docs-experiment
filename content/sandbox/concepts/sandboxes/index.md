---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/concepts/sandboxes/
  description: Sandbox SDK sandboxes transition through running, sleeping, and destroyed states based on activity.
  full_title: Sandbox lifecycle · Cloudflare Sandbox SDK docs
  head_html: <title>Sandbox lifecycle · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Sandbox SDK sandboxes transition through running, sleeping, and destroyed states based on activity."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/concepts/sandboxes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/concepts/sandboxes/index.md"><meta property="og:title" content="Sandbox lifecycle · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Sandbox SDK sandboxes transition through running, sleeping, and destroyed states based on activity."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/concepts/sandboxes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/concepts/sandboxes/#page","headline":"Sandbox lifecycle \u00b7 Cloudflare Sandbox SDK docs","description":"Sandbox SDK sandboxes transition through running, sleeping, and destroyed states based on activity.","url":"https://developers.cloudflare.com/sandbox/concepts/sandboxes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/concepts/sandboxes/
  schema: 1
---
<p>A sandbox is an isolated execution environment where your code runs. Each sandbox:</p>
<ul>
<li>Has a unique identifier (sandbox ID)</li>
<li>Contains an isolated filesystem</li>
<li>Runs in a dedicated Linux container</li>
<li>Maintains state while the container is active</li>
<li>Exists as a Cloudflare Durable Object</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13569.md")
</aside>
<h2 id="lifecycle-states">Lifecycle states</h2>
<h3 id="creation">Creation</h3>
<p>A sandbox is created the first time you reference its ID:</p>
<pre tabindex="0"><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, &quot;user-123&quot;);&#10;await sandbox.exec(&#x27;echo &quot;Hello&quot;&#x27;); // First request creates sandbox&#10;</code></pre>
<h3 id="active">Active</h3>
<p>The sandbox container is running and processing requests. All state remains available: files, running processes, shell sessions, and environment variables.</p>
<h3 id="idle">Idle</h3>
<p>After a period of inactivity (10 minutes by default, configurable via <a href="/sandbox/configuration/sandbox-options/"><code>sleepAfter</code></a>), the container stops to free resources. When the next request arrives, a fresh container starts. All previous state is lost and the environment resets to its initial state.</p>
<p><strong>Note</strong>: Containers with <a href="/sandbox/configuration/sandbox-options/#keepalive"><code>keepAlive: true</code></a> never enter the idle state. They automatically send heartbeat pings every 30 seconds to prevent eviction.</p>
<h3 id="destruction">Destruction</h3>
<p>Sandboxes are explicitly destroyed or automatically cleaned up:</p>
<pre tabindex="0"><code class="language-typescript">await sandbox.destroy();&#10;// All files, processes, and state deleted permanently&#10;</code></pre>
<h2 id="container-lifetime-and-state">Container lifetime and state</h2>
<p>Sandbox state exists only while the container is active. Understanding this is critical for building reliable applications.</p>
<p><strong>While the container is active</strong> (typically minutes to hours of activity):</p>
<ul>
<li>Files written to <code>/workspace</code>, <code>/tmp</code>, <code>/home</code> remain available</li>
<li>Background processes continue running</li>
<li>Shell sessions maintain their working directory and environment</li>
<li>Code interpreter contexts retain variables and imports</li>
</ul>
<p><strong>When the container stops</strong> (due to inactivity or explicit destruction):</p>
<ul>
<li>All files are deleted</li>
<li>All processes terminate</li>
<li>All shell state resets</li>
<li>All code interpreter contexts are cleared</li>
</ul>
<p>The next request creates a fresh container with a clean environment.</p>
<h2 id="naming-strategies">Naming strategies</h2>
<h3 id="per-user-sandboxes">Per-user sandboxes</h3>
<pre tabindex="0"><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, `user-${userId}`);&#10;</code></pre>
<p>Use this pattern for interactive environments, playgrounds, and notebooks where each user returns to their own active workspace.</p>
<h3 id="per-session-sandboxes">Per-session sandboxes</h3>
<pre tabindex="0"><code class="language-typescript">const sessionId = `session-${Date.now()}-${Math.random()}`;&#10;const sandbox = getSandbox(env.Sandbox, sessionId);&#10;// Later:&#10;await sandbox.destroy();&#10;</code></pre>
<p>Use this pattern for one-time execution, CI/CD, and tests that need a clean environment.</p>
<h3 id="per-task-sandboxes">Per-task sandboxes</h3>
<pre tabindex="0"><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, `build-${repoName}-${commit}`);&#10;</code></pre>
<p>Idempotent operations with clear task-to-sandbox mapping. Good for builds, pipelines, and background jobs.</p>
<h2 id="request-routing">Request routing</h2>
<p>The first request to a sandbox determines its geographic location. Subsequent requests route to the same location.</p>
<p><strong>For global apps</strong>:</p>
<ul>
<li>Option 1: Multiple sandboxes per user with region suffix (<code>user-123-us</code>, <code>user-123-eu</code>)</li>
<li>Option 2: Single sandbox per user (simpler, but some users see higher latency)</li>
</ul>
<h2 id="lifecycle-management">Lifecycle management</h2>
<h3 id="when-to-destroy">When to destroy</h3>
<pre tabindex="0"><code class="language-typescript">try {&#10;	const sandbox = getSandbox(env.Sandbox, sessionId);&#10;	await sandbox.exec(&quot;npm run build&quot;);&#10;} finally {&#10;	await sandbox.destroy(); // Clean up temporary sandboxes&#10;}&#10;</code></pre>
<p><strong>Destroy when</strong>: Session ends, task completes, resources no longer needed</p>
<p><strong>Do not destroy</strong>: Personal environments, long-running services</p>
<h3 id="managing-keepalive-containers">Managing keepAlive containers</h3>
<p>Containers with <a href="/sandbox/configuration/sandbox-options/#keepalive"><code>keepAlive: true</code></a> require explicit management since they do not timeout automatically:</p>
<pre tabindex="0"><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, &#x27;persistent-task&#x27;, {&#10;  keepAlive: true&#10;});&#10;&#10;// Later, when done with long-running work&#10;await sandbox.setKeepAlive(false); // Allow normal timeout behavior&#10;// Or explicitly destroy:&#10;await sandbox.destroy();&#10;</code></pre>
<h3 id="handling-container-restarts">Handling container restarts</h3>
<p>Containers restart after inactivity or failures. Design your application to handle state loss:</p>
<pre tabindex="0"><code class="language-typescript">// Check if required files exist before using them&#10;const files = await sandbox.listFiles(&quot;/workspace&quot;);&#10;if (!files.includes(&quot;data.json&quot;)) {&#10;	// Reinitialize: container restarted and lost previous state&#10;	await sandbox.writeFile(&quot;/workspace/data.json&quot;, initialData);&#10;}&#10;&#10;await sandbox.exec(&quot;python process.py&quot;);&#10;</code></pre>
<h2 id="version-compatibility">Version compatibility</h2>
<p>The SDK automatically checks that your npm package version matches the Docker container image version. <strong>Version mismatches can cause features to break or behave unexpectedly.</strong></p>
<p><strong>What happens</strong>:</p>
<ul>
<li>On sandbox startup, the SDK queries the container's version</li>
<li>If versions do not match, a warning is logged</li>
<li>Some features may not work correctly if versions are incompatible</li>
</ul>
<p><strong>When you might see warnings</strong>:</p>
<ul>
<li>You updated the npm package (<code>npm install @cloudflare/sandbox@latest</code>) but forgot to update the <code>FROM</code> line in your Dockerfile</li>
</ul>
<p><strong>How to fix</strong>:
Update your Dockerfile to match your npm package version. For example, if using <code>@cloudflare/sandbox@0.7.0</code>:</p>
<pre tabindex="0"><code class="language-dockerfile">&#35; Default image (JavaScript/TypeScript)&#10;FROM docker.io/cloudflare/sandbox:0.7.0&#10;&#10;&#35; Or Python image if you need Python support&#10;FROM docker.io/cloudflare/sandbox:0.7.0-python&#10;</code></pre>
<p>See <a href="/sandbox/configuration/dockerfile/">Dockerfile reference</a> for details on image variants and extending the base image.</p>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Name consistently</strong> - Use clear, predictable naming schemes</li>
<li><strong>Clean up temporary sandboxes</strong> - Always destroy when done</li>
<li><strong>Reuse user workspaces</strong> - One long-lived sandbox per user is often sufficient</li>
<li><strong>Batch operations</strong> - Combine commands: <code>npm install &amp;&amp; npm test &amp;&amp; npm build</code></li>
<li><strong>Design for ephemeral state</strong> - Containers restart after inactivity, losing all state</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/concepts/architecture/">Architecture</a> - How sandboxes fit in the system</li>
<li><a href="/sandbox/concepts/containers/">Container runtime</a> - What runs inside sandboxes</li>
<li><a href="/sandbox/concepts/sessions/">Session management</a> - Advanced state isolation</li>
<li><a href="/sandbox/concepts/backup-restore/">Directory backups</a> - Why restored files do not survive sleep unless you restore again</li>
<li><a href="/sandbox/api/lifecycle/">Lifecycle API</a> - Create and manage sandboxes</li>
<li><a href="/sandbox/api/sessions/">Sessions API</a> - Create and manage execution sessions</li>
</ul>
