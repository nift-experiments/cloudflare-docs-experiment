---
cp9:
  canonical: https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/
  description: Additional module types that can be imported in your Worker
  full_title: Non-JavaScript modules · Cloudflare Workers docs
  head_html: <title>Non-JavaScript modules · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Additional module types that can be imported in your Worker"><link rel="canonical" href="https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/index.md"><meta property="og:title" content="Non-JavaScript modules · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Additional module types that can be imported in your Worker"><meta property="og:url" content="https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/#page","headline":"Non-JavaScript modules \u00b7 Cloudflare Workers docs","description":"Additional module types that can be imported in your Worker","url":"https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/vite-plugin/reference/non-javascript-modules/
  schema: 1
---
<p>In addition to TypeScript and JavaScript, the following module types are automatically configured to be importable in your Worker code.</p>
<table>
<thead>
<tr>
<th>Module extension</th>
<th>Imported type</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.txt</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.html</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.sql</code></td>
<td><code>string</code></td>
</tr>
<tr>
<td><code>.bin</code></td>
<td><code>ArrayBuffer</code></td>
</tr>
<tr>
<td><code>.wasm</code>, <code>.wasm?module</code></td>
<td><code>WebAssembly.Module</code></td>
</tr>
</tbody>
</table>
<p>For example, with the following import, <code>text</code> will be a string containing the contents of <code>example.txt</code>:</p>
<pre tabindex="0"><code class="language-js">import text from &quot;./example.txt&quot;;&#10;</code></pre>
<p>This is also the basis for importing Wasm, as in the following example:</p>
<pre tabindex="0"><code class="language-ts">import wasm from &quot;./example.wasm&quot;;&#10;&#10;// Instantiate Wasm modules in the module scope&#10;const instance = await WebAssembly.instantiate(wasm);&#10;&#10;export default {&#10;	fetch() {&#10;		const result = instance.exports.exported_func();&#10;&#10;		return new Response(result);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17390.md")
</aside>
