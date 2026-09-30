---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/1-0-preview/interpreter/
  description: Run Python, JavaScript, or TypeScript in a sandbox with the interpreter extension on @cloudflare/sandbox@next.
  full_title: Code interpreter · Cloudflare Sandbox SDK docs
  head_html: <title>Code interpreter · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Run Python, JavaScript, or TypeScript in a sandbox with the interpreter extension on @cloudflare/sandbox@next."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/1-0-preview/interpreter/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/1-0-preview/interpreter/index.md"><meta property="og:title" content="Code interpreter · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Run Python, JavaScript, or TypeScript in a sandbox with the interpreter extension on @cloudflare/sandbox@next."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/1-0-preview/interpreter/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/1-0-preview/interpreter/#page","headline":"Code interpreter \u00b7 Cloudflare Sandbox SDK docs","description":"Run Python, JavaScript, or TypeScript in a sandbox with the interpreter extension on @cloudflare/sandbox@next.","url":"https://developers.cloudflare.com/sandbox/1-0-preview/interpreter/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/1-0-preview/interpreter/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13726.md")
</aside>
<p>On <code>@next</code>, the code interpreter is an opt-in extension, not methods on bare <code>Sandbox</code>. Method names match the stable interpreter. You attach once, then call <code>sandbox.interpreter.*</code>. <code>runCode</code> returns plain serializable data across the Worker and Durable Object boundary.</p>
<p>Signatures and types: <a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a>.</p>
<h2 id="attach">Attach</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13727.md")
</div>
<p>Export that class from your Worker. The sidecar provisions on first use.</p>
<h2 id="image">Image</h2>
<table>
<thead>
<tr>
<th>Language</th>
<th>Image</th>
</tr>
</thead>
<tbody>
<tr>
<td>JavaScript / TypeScript</td>
<td>Default sandbox image (or any variant with a JS runtime)</td>
</tr>
<tr>
<td>Python</td>
<td><strong><code>-python</code></strong> image variant</td>
</tr>
</tbody>
</table>
<p>Use the same preview Worker package and container image line. Refer to <a href="/sandbox/configuration/dockerfile/">Dockerfile</a>.</p>
<h2 id="run-code">Run code</h2>
<p>A <strong>context</strong> keeps variables and imports until you delete it or the container is replaced.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13728.md")
</div>
<p>If you omit <code>context</code>, <code>runCode</code> uses a default context for the language (default language: <code>python</code>). Languages: <code>python</code>, <code>javascript</code>, <code>typescript</code>.</p>
<p>For result fields, streaming (<code>runCodeStream</code>), and list/delete context methods, refer to the <a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a>.</p>
<p>Contexts exist only in the <strong>current container</strong>. After stop or replace, create new ones. Refer to <a href="/sandbox/1-0-preview/lifecycle/">Sandbox lifecycle</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a></li>
<li><a href="/sandbox/1-0-preview/extensions/">Extensions</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
<li>Stable guide: <a href="/sandbox/guides/code-execution/">Use code interpreter</a></li>
</ul>
