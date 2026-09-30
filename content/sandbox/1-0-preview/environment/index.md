---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/1-0-preview/environment/
  description: How processes and terminals get environment variables in the Sandbox SDK 1.0 preview.
  full_title: Environment variables · Cloudflare Sandbox SDK docs
  head_html: <title>Environment variables · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="How processes and terminals get environment variables in the Sandbox SDK 1.0 preview."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/1-0-preview/environment/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/1-0-preview/environment/index.md"><meta property="og:title" content="Environment variables · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How processes and terminals get environment variables in the Sandbox SDK 1.0 preview."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/1-0-preview/environment/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/1-0-preview/environment/#page","headline":"Environment variables \u00b7 Cloudflare Sandbox SDK docs","description":"How processes and terminals get environment variables in the Sandbox SDK 1.0 preview.","url":"https://developers.cloudflare.com/sandbox/1-0-preview/environment/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/1-0-preview/environment/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13753.md")
</aside>
<p>Each <code>exec()</code> and <code>createTerminal()</code> starts an independent process. Shell <code>export</code> in one process does not apply to the next launch. Configure process environment with the container image, <code>setEnvVars</code>, and per-launch <code>env</code>.</p>
<p>Use environment variables for <strong>non-secret</strong> configuration (paths, feature flags, <code>NODE_ENV</code>, and similar). Do not put live API keys or other long-lived credentials into the sandbox. To call external services that need credentials, use <a href="/sandbox/guides/outbound-traffic/">outbound traffic handlers</a> so secrets stay in the Worker.</p>
<h2 id="how-a-process-gets-its-environment">How a process gets its environment</h2>
<p>When a process starts, the runtime builds its environment from:</p>
<ol>
<li>The <strong>container</strong> environment (image <code>ENV</code> and defaults).</li>
<li>Names from <strong><code>setEnvVars</code></strong>, when you use <code>exec()</code> (described in the next section).</li>
<li>The <strong><code>env</code> option</strong> on that launch, if you pass one.</li>
</ol>
<p>Later launches do not keep overlays from earlier launches. A command that runs <code>export FOO=bar</code> inside one process does not change the next <code>exec()</code>.</p>
<p>Worker bindings in your <code>fetch</code> handler are not process environment variables. Only values you pass through <code>setEnvVars</code> or launch <code>env</code> appear inside the process (and those should not be long-lived secrets).</p>
<h2 id="setenvvars"><code>setEnvVars()</code></h2>
<pre tabindex="0"><code class="language-ts">setEnvVars(envVars: Record&lt;string, string | undefined&gt;): Promise&lt;void&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Value</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td>string</td>
<td>Set this environment variable for later <code>exec()</code> launches</td>
</tr>
<tr>
<td><code>undefined</code></td>
<td>Remove a previously stored variable</td>
</tr>
</tbody>
</table>
<p>On each <code>exec()</code>, the SDK merges stored names into that process’s environment at launch.</p>
<p>Stored names live in the sandbox Durable Object’s memory. They are not written to the container filesystem and are not part of a backup. After the Durable Object is evicted or replaced, call <code>setEnvVars</code> again if you still need those names, or pass <code>env</code> on each <code>exec()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13754.md")
</div>
<h2 id="env-on-exec"><code>env</code> on <code>exec()</code></h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13755.md")
</div>
<table>
<thead>
<tr>
<th>Behavior</th>
<th>Detail</th>
</tr>
</thead>
<tbody>
<tr>
<td>Scope</td>
<td>This launch only</td>
</tr>
<tr>
<td>Merge order</td>
<td>Container environment, then <code>setEnvVars</code>, then this <code>env</code></td>
</tr>
<tr>
<td>Side effects</td>
<td>Does not update <code>setEnvVars</code> storage</td>
</tr>
</tbody>
</table>
<p>Omit <code>env</code> when sandbox-wide names (and the container environment) are enough.</p>
<h2 id="env-on-createterminal"><code>env</code> on <code>createTerminal()</code></h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13756.md")
</div>
<p>The terminal’s launch <code>env</code> overlays the container environment for that terminal only. Pass the names the terminal needs on <code>createTerminal</code>.</p>
<p>Inside an interactive shell, <code>export</code> applies for the life of that terminal. It does not apply to later <code>exec()</code> calls. Refer to <a href="/sandbox/1-0-preview/terminals/">Terminals</a>.</p>
<h2 id="external-apis-and-credentials">External APIs and credentials</h2>
<p>Code inside the sandbox should not hold live provider credentials. Keep secrets in the Worker and intercept outbound HTTP(S) with <code>outboundByHost</code> (and related policy such as <code>enableInternet</code> / <code>allowedHosts</code>). The sandbox can send ordinary requests—or placeholders client libraries require—while the Worker attaches real credentials before the request leaves your account.</p>
<p>Refer to <a href="/sandbox/guides/outbound-traffic/">Handle outbound traffic</a>, including securely injecting credentials. For Workers bindings (KV, R2, and similar) reached by hostname from the sandbox, refer to <a href="/sandbox/guides/workers-connections/">Connect to Workers bindings</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/guides/outbound-traffic/">Handle outbound traffic</a></li>
<li><a href="/sandbox/guides/workers-connections/">Connect to Workers bindings</a></li>
<li><a href="/sandbox/1-0-preview/processes/">Process execution</a></li>
<li><a href="/sandbox/1-0-preview/api/processes/">Processes API</a></li>
<li><a href="/sandbox/1-0-preview/terminals/">Terminals</a></li>
<li><a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
</ul>
