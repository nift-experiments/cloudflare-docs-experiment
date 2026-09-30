---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/configuration/wrangler/
  description: Set up Wrangler bindings, Durable Objects, and container settings for Sandbox SDK.
  full_title: Wrangler configuration · Cloudflare Sandbox SDK docs
  head_html: <title>Wrangler configuration · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Wrangler bindings, Durable Objects, and container settings for Sandbox SDK."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/configuration/wrangler/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/configuration/wrangler/index.md"><meta property="og:title" content="Wrangler configuration · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Wrangler bindings, Durable Objects, and container settings for Sandbox SDK."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/configuration/wrangler/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Sandbox SDK,Durable Objects,Containers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/configuration/wrangler/#page","headline":"Wrangler configuration \u00b7 Cloudflare Sandbox SDK docs","description":"Set up Wrangler bindings, Durable Objects, and container settings for Sandbox SDK.","url":"https://developers.cloudflare.com/sandbox/configuration/wrangler/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/configuration/wrangler/
  schema: 1
---
<h2 id="minimal-configuration">Minimal configuration</h2>
<p>The minimum required configuration for using Sandbox SDK:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13528.md")
</div>
<h2 id="required-settings">Required settings</h2>
<p>The Sandbox SDK is built on Cloudflare Containers. Your configuration requires three sections:</p>
<ol>
<li><strong>containers</strong> - Define the container image (your runtime environment)</li>
<li><strong>durable_objects.bindings</strong> - Bind the Sandbox Durable Object to your Worker</li>
<li><strong>migrations</strong> - Initialize the Durable Object class</li>
</ol>
<p>The minimal configuration shown above includes all required settings. For detailed configuration options, refer to the <a href="/workers/wrangler/configuration/#containers">Containers configuration documentation</a>.</p>
<h2 id="backup-storage">Backup storage</h2>
<p>To use the <a href="/sandbox/api/backups/">backup and restore API</a>, you need an R2 bucket binding and presigned URL credentials. The container uploads and downloads backup archives directly to/from R2 using presigned URLs, which requires R2 API token credentials.</p>
<h3 id="1-create-the-r2-bucket"><ol>
<li>Create the R2 bucket</li>
</ol></h3>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket create my-backup-bucket&#10;</code></pre>
<h3 id="2-add-the-binding-and-environment-variables"><ol start="2">
<li>Add the binding and environment variables</li>
</ol></h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13529.md")
</div>
<h3 id="3-set-r2-api-credentials-as-secrets"><ol start="3">
<li>Set R2 API credentials as secrets</li>
</ol></h3>
<pre tabindex="0"><code class="language-sh">npx wrangler secret put R2_ACCESS_KEY_ID&#10;npx wrangler secret put R2_SECRET_ACCESS_KEY&#10;</code></pre>
<p>Create an R2 API token in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>R2</strong> &gt; <strong>Overview</strong> &gt; <strong>Manage R2 API Tokens</strong>. The token needs <strong>Object Read &amp; Write</strong> permissions for your backup bucket.</p>
<p>The SDK uses these credentials to generate presigned URLs that allow the container to transfer backup archives directly to and from R2. For a complete setup walkthrough, refer to the <a href="/sandbox/guides/backup-restore/">backup and restore guide</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="binding-not-found">Binding not found</h3>
<p><strong>Error</strong>: <code>TypeError: env.Sandbox is undefined</code></p>
<p><strong>Solution</strong>: Ensure your <code>wrangler.jsonc</code> includes the Durable Objects binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13530.md")
</div>
<h3 id="missing-migrations">Missing migrations</h3>
<p><strong>Error</strong>: Durable Object not initialized</p>
<p><strong>Solution</strong>: Add migrations for the Sandbox class:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13531.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a> - Deploy and keep package and image aligned</li>
<li><a href="/containers/guides/deploy/">Deploy Containers</a> - Containers deploy path</li>
<li><a href="/sandbox/configuration/transport/">Transport modes</a> - Configure HTTP, WebSocket, and RPC transport</li>
<li><a href="/workers/wrangler/">Wrangler documentation</a> - Complete Wrangler reference</li>
<li><a href="/durable-objects/get-started/">Durable Objects setup</a> - DO-specific configuration</li>
<li><a href="/sandbox/configuration/dockerfile/">Dockerfile reference</a> - Custom container images</li>
<li><a href="/sandbox/configuration/environment-variables/">Environment variables</a> - Passing configuration to sandboxes</li>
<li><a href="/sandbox/get-started/">Get Started guide</a> - Initial setup walkthrough</li>
</ul>
