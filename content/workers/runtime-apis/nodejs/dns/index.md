---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/
  description: Use the Node.js dns module in Cloudflare Workers for DNS name resolution via DNS over HTTPS.
  full_title: dns · Cloudflare Workers docs
  head_html: <title>dns · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Node.js dns module in Cloudflare Workers for DNS name resolution via DNS over HTTPS."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/index.md"><meta property="og:title" content="dns · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Node.js dns module in Cloudflare Workers for DNS name resolution via DNS over HTTPS."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/#page","headline":"dns \u00b7 Cloudflare Workers docs","description":"Use the Node.js dns module in Cloudflare Workers for DNS name resolution via DNS over HTTPS.","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/dns/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/dns/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17154.md")
</aside>
<p>You can use <a href="https://nodejs.org/api/dns.html"><code>node:dns</code></a> for name resolution via <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS</a> using
<a href="https://www.cloudflare.com/application-services/products/dns/">Cloudflare DNS</a> at 1.1.1.1.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17155.md")
</div>
<p>All <code>node:dns</code> functions are available, except <code>lookup</code>, <code>lookupService</code>, and <code>resolve</code> which throw &quot;Not implemented&quot; errors when called.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17153.md")
</aside>
<p>The full <code>node:dns</code> API is documented in the <a href="https://nodejs.org/api/dns.html">Node.js documentation for <code>node:dns</code></a>.</p>
<pre tabindex="0"><code>&#10;</code></pre>
