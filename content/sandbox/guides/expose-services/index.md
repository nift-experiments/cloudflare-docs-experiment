---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/guides/expose-services/
  description: Create preview URLs and expose ports for web services.
  full_title: Expose services · Cloudflare Sandbox SDK docs
  head_html: <title>Expose services · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Create preview URLs and expose ports for web services."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/guides/expose-services/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/guides/expose-services/index.md"><meta property="og:title" content="Expose services · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create preview URLs and expose ports for web services."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/guides/expose-services/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/guides/expose-services/#page","headline":"Expose services \u00b7 Cloudflare Sandbox SDK docs","description":"Create preview URLs and expose ports for web services.","url":"https://developers.cloudflare.com/sandbox/guides/expose-services/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/guides/expose-services/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="coming-soon-sandbox-sdk-1-0">Coming soon: Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13446.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="production-requires-custom-domain">Production requires custom domain</h3>
@markup("md", "content/.markup/bodies/13445.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prefer-sandbox-tunnels-for-public-urls">Prefer `sandbox.tunnels` for public URLs</h3>
@markup("md", "content/.markup/bodies/13444.md")
</aside>
<p>This guide shows you how to expose services running in your sandbox to the internet via preview URLs.</p>
<h2 id="when-to-expose-ports">When to expose ports</h2>
<p>Expose ports when you need to:</p>
<ul>
<li><strong>Test web applications</strong> - Preview frontend or backend apps</li>
<li><strong>Share demos</strong> - Give others access to running applications</li>
<li><strong>Develop APIs</strong> - Test endpoints from external tools</li>
<li><strong>Debug services</strong> - Access internal services for troubleshooting</li>
<li><strong>Build dev environments</strong> - Create shareable development workspaces</li>
</ul>
<h2 id="basic-port-exposure">Basic port exposure</h2>
<p>The typical workflow is: start service → wait for ready → expose port → handle requests with <code>proxyToSandbox</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13447.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13443.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="local-development-requirement">Local development requirement</h3>
@markup("md", "content/.markup/bodies/13442.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="uppercase-sandbox-ids-don-t-work-with-preview-urls">Uppercase sandbox IDs don't work with preview URLs</h3>
@markup("md", "content/.markup/bodies/13441.md")
</aside>
<h2 id="stable-urls-with-custom-tokens">Stable URLs with custom tokens</h2>
<p>For production deployments or when sharing URLs with users, use custom tokens to maintain consistent preview URLs across container restarts:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13448.md")
</div>
<p><strong>Token requirements:</strong></p>
<ul>
<li>1-16 characters long</li>
<li>Lowercase letters (a-z), numbers (0-9), hyphens (-), and underscores (_) only</li>
<li>Must be unique within each sandbox</li>
</ul>
<p><strong>Use cases:</strong></p>
<ul>
<li>Production APIs with stable endpoints</li>
<li>Sharing demo URLs with external users</li>
<li>Integration testing with predictable URLs</li>
<li>Documentation with consistent examples</li>
</ul>
<h2 id="name-your-exposed-ports">Name your exposed ports</h2>
<p>When exposing multiple ports, use names to stay organized:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13449.md")
</div>
<h2 id="wait-for-service-readiness">Wait for service readiness</h2>
<p>Always verify a service is ready before exposing. Use a simple delay for most cases:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13450.md")
</div>
<p>For critical services, poll the health endpoint:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13451.md")
</div>
<h2 id="multiple-services">Multiple services</h2>
<p>Expose multiple ports for full-stack applications:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13452.md")
</div>
<h2 id="manage-exposed-ports">Manage exposed ports</h2>
<h3 id="list-currently-exposed-ports">List currently exposed ports</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13453.md")
</div>
<h3 id="unexpose-ports">Unexpose ports</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13454.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Wait for readiness</strong> - Don't expose ports immediately after starting processes</li>
<li><strong>Use named ports</strong> - Easier to track when exposing multiple ports</li>
<li><strong>Clean up</strong> - Unexpose ports when done to prevent abandoned URLs</li>
<li><strong>Add authentication</strong> - Preview URLs are public; protect sensitive services</li>
</ul>
<h2 id="local-development">Local development</h2>
<p>When developing locally with <code>wrangler dev</code>, you must expose ports in your Dockerfile:</p>
<pre tabindex="0"><code class="language-dockerfile">FROM docker.io/cloudflare/sandbox:0.3.3&#10;&#10;&#35; Expose ports you plan to use&#10;EXPOSE 8000&#10;EXPOSE 8080&#10;EXPOSE 5173&#10;</code></pre>
<p>Update <code>wrangler.jsonc</code> to use your Dockerfile:</p>
<pre tabindex="0"><code class="language-jsonc">{&#10;  &quot;containers&quot;: [&#10;    {&#10;      &quot;class_name&quot;: &quot;Sandbox&quot;,&#10;      &quot;image&quot;: &quot;./Dockerfile&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>In production, all ports are available and controlled programmatically via <code>exposePort()</code> / <code>unexposePort()</code>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="port-3000-is-reserved">Port 3000 is reserved</h3>
<p>Port 3000 is used by the internal Bun server and cannot be exposed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13455.md")
</div>
<h3 id="port-not-ready">Port not ready</h3>
<p>Wait for the service to start before exposing:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13456.md")
</div>
<h3 id="port-already-exposed">Port already exposed</h3>
<p>Check before exposing to avoid errors:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13457.md")
</div>
<h3 id="uppercase-sandbox-id-error">Uppercase sandbox ID error</h3>
<p><strong>Error</strong>: <code>Preview URLs require lowercase sandbox IDs</code></p>
<p><strong>Cause</strong>: You created a sandbox with uppercase characters (e.g., <code>&quot;MyProject-123&quot;</code>) but preview URLs always use lowercase in routing, causing a mismatch.</p>
<p><strong>Solution</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13458.md")
</div>
<p>This creates the Durable Object with ID <code>&quot;myproject-123&quot;</code>, matching the preview URL routing.</p>
<p>See <a href="/sandbox/configuration/sandbox-options/#normalizeid">Sandbox options - normalizeId</a> for details.</p>
<h2 id="preview-url-format">Preview URL Format</h2>
<p><strong>Production</strong>: <code>https://{port}-{sandbox-id}-{token}.yourdomain.com</code></p>
<ul>
<li>Auto-generated token: <code>https://8080-abc123-random16chars12.yourdomain.com</code></li>
<li>Custom token: <code>https://8080-abc123-my-api-v1.yourdomain.com</code></li>
</ul>
<p><strong>Local development</strong>: <code>http://localhost:8787/...</code></p>
<p><strong>Note</strong>: Port 3000 is reserved for the internal Bun server and cannot be exposed.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/api/ports/">Ports API reference</a> - Complete port exposure API</li>
<li><a href="/sandbox/guides/background-processes/">Background processes guide</a> - Managing services</li>
<li><a href="/sandbox/guides/execute-commands/">Execute commands guide</a> - Starting services</li>
<li><a href="/sandbox/api/tunnels/">Tunnels API reference</a> - Recommended alternative for most public-URL use cases (quick or named tunnels)</li>
</ul>
