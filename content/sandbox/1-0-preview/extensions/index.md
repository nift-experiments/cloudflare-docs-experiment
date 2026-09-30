---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/1-0-preview/extensions/
  description: Attach optional Sandbox capabilities on @cloudflare/sandbox@next.
  full_title: Extensions · Cloudflare Sandbox SDK docs
  head_html: <title>Extensions · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Attach optional Sandbox capabilities on @cloudflare/sandbox@next."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/1-0-preview/extensions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/1-0-preview/extensions/index.md"><meta property="og:title" content="Extensions · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Attach optional Sandbox capabilities on @cloudflare/sandbox@next."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/1-0-preview/extensions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/1-0-preview/extensions/#page","headline":"Extensions \u00b7 Cloudflare Sandbox SDK docs","description":"Attach optional Sandbox capabilities on @cloudflare/sandbox@next.","url":"https://developers.cloudflare.com/sandbox/1-0-preview/extensions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/1-0-preview/extensions/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="path-to-sandbox-sdk-1-0">Path to Sandbox SDK 1.0</h3>
@markup("md", "content/.markup/bodies/13748.md")
</aside>
<p>Extensions add optional capabilities to your <code>Sandbox</code> subclass as nested namespaces (for example <code>sandbox.interpreter.*</code>). They are not free-floating globals on every app.</p>
<h2 id="attach-pattern">Attach pattern</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13749.md")
</div>
<p>Export that class from your Worker. Call extension methods through the nested property from application code.</p>
<h2 id="first-party-extensions">First-party extensions</h2>
<p>The following first-party extensions are available on the preview package:</p>
<table>
<thead>
<tr>
<th>Extension</th>
<th>Package</th>
<th>Docs</th>
</tr>
</thead>
<tbody>
<tr>
<td>Code interpreter</td>
<td><code>@cloudflare/sandbox/interpreter</code></td>
<td><a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a>, <a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a></td>
</tr>
<tr>
<td>OpenCode</td>
<td><code>@cloudflare/sandbox/opencode</code></td>
<td>Confirm exports in your installed <code>@next</code> version (for example <code>withOpenCode</code> and client/proxy helpers).</td>
</tr>
</tbody>
</table>
<p>For the interpreter, attach once, then use the same method names as the stable package (<code>createCodeContext</code>, <code>runCode</code>, and related calls) on <code>sandbox.interpreter</code>. Python needs the <strong><code>-python</code></strong> image variant. For the full how-to, refer to <a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a>.</p>
<h2 id="custom-extensions">Custom extensions</h2>
<p>Application-defined extensions are experimental. Helpers exist under <code>@cloudflare/sandbox/extensions</code>, but preview documentation does not yet cover authoring or publishing a custom extension. Prefer the first-party extensions in the table, or keep any custom code inside your application until a supported authoring guide ships.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/1-0-preview/interpreter/">Code interpreter</a></li>
<li><a href="/sandbox/1-0-preview/api/interpreter/">Interpreter API</a></li>
<li><a href="/sandbox/1-0-preview/api/">API reference</a></li>
<li><a href="/sandbox/1-0-preview/migrate/">Migrate</a></li>
</ul>
