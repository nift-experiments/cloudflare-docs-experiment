---
cp9:
  canonical: https://developers.cloudflare.com/style-guide/build-the-page/components/typescript-example/
  description: Show TypeScript and auto-transpiled JavaScript tabs.
  full_title: TypeScript example · Cloudflare Style Guide
  head_html: <title>TypeScript example · Cloudflare Style Guide</title><meta name="generator" content="Nift"><meta name="description" content="Show TypeScript and auto-transpiled JavaScript tabs."><link rel="canonical" href="https://developers.cloudflare.com/style-guide/build-the-page/components/typescript-example/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/style-guide/build-the-page/components/typescript-example/index.md"><meta property="og:title" content="TypeScript example · Cloudflare Style Guide"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Show TypeScript and auto-transpiled JavaScript tabs."><meta property="og:url" content="https://developers.cloudflare.com/style-guide/build-the-page/components/typescript-example/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Style Guide"><meta name="algolia_product_filter" content="Style Guide"><meta name="pcx_additional_products" content="Style Guide"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/style-guide/build-the-page/components/typescript-example/#page","headline":"TypeScript example \u00b7 Cloudflare Style Guide","description":"Show TypeScript and auto-transpiled JavaScript tabs.","url":"https://developers.cloudflare.com/style-guide/build-the-page/components/typescript-example/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /style-guide/build-the-page/components/typescript-example/
  schema: 1
---
<h2 id="typescript-examples">TypeScript examples</h2>
<p>The <code>TypeScriptExample</code> component uses <a href="https://github.com/bloomberg/ts-blank-space"><code>ts-blank-space</code></a> to remove TypeScript-specific syntax from your example and provide a JavaScript tab. This reduces maintenance burden by only having a single example to maintain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14626.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14625.md")
</aside>
<h2 id="component">Component</h2>
<pre tabindex="0"><code class="language-mdx">import { TypeScriptExample } from &quot;~/components&quot;;&#10;&#10;&lt;TypeScriptExample code={{&#10;  collapse: &quot;1-2&quot;&#10;}}&gt;&#10;</code></pre>
<p>// comment to demonstrate
// collapsible sections
interface Environment {
KV: KVNamespace;
}</p>
<p>async fetch(req, env, ctx): Promise<Response> {
if (req !== &quot;POST&quot;) {
return new Response(&quot;Method Not Allowed&quot;, {
status: 405,
headers: {
&quot;Allow&quot;: &quot;POST&quot;
}
});
}</p>
<pre tabindex="0"><code>await env.KV.put(&quot;foo&quot;, &quot;bar&quot;);&#10;&#10;return new Response();&#10;</code></pre>
<p>}
} satisfies ExportedHandler<Environment></p>
<pre tabindex="0"><code>&lt;/TypeScriptExample&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;TypeScriptExample&gt;</code> Props</h2>
<h3 id="filename"><code>filename</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>An optional filename, ending in <code>.ts</code>.</p>
<p><code>.ts</code> will be replaced by <code>.js</code> for the JavaScript tab.</p>
<h3 id="playground"><code>playground</code></h3>
<p><strong>type:</strong> <code>boolean</code></p>
<p>If set to <code>true</code>, a <a href="/style-guide/style-and-grammar/formatting/code-block-guidelines/#workers-playground"><code>Run Worker in Playground</code></a> button will appear on the JavaScript tab.</p>
<h3 id="code"><code>code</code></h3>
<p><strong>type</strong>: <code>object</code></p>
<p>Props to pass to the <a href="https://docs.astro.build/en/reference/api-reference/#code-">Astro <code>Code</code> component</a>.</p>
<p>These props will apply to both code blocks and so options like <code>collapse</code> may not work as expected, as lines may be removed from the TypeScript code.</p>
