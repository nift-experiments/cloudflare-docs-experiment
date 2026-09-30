---
cp9:
  canonical: https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/
  description: Use the Node.js crypto module in Cloudflare Workers for hashing, encryption, signing, and verification.
  full_title: crypto · Cloudflare Workers docs
  head_html: <title>crypto · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Use the Node.js crypto module in Cloudflare Workers for hashing, encryption, signing, and verification."><link rel="canonical" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/index.md"><meta property="og:title" content="crypto · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use the Node.js crypto module in Cloudflare Workers for hashing, encryption, signing, and verification."><meta property="og:url" content="https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/#page","headline":"crypto \u00b7 Cloudflare Workers docs","description":"Use the Node.js crypto module in Cloudflare Workers for hashing, encryption, signing, and verification.","url":"https://developers.cloudflare.com/workers/runtime-apis/nodejs/crypto/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/runtime-apis/nodejs/crypto/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17157.md")
</aside>
<p>The <a href="https://nodejs.org/docs/latest/api/crypto.html"><code>node:crypto</code></a> module provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.</p>
<p>All <code>node:crypto</code> APIs are fully supported in Workers with the following exceptions:</p>
<ul>
<li>The functions <a href="https://nodejs.org/api/crypto.html#cryptogeneratekeypairtype-options-callback">generateKeyPair</a> and <a href="https://nodejs.org/api/crypto.html#cryptogeneratekeypairsynctype-options">generateKeyPairSync</a>
do not support DSA or DH key pairs.</li>
<li><code>argon2</code> and <code>argon2Sync</code> are not supported.</li>
<li><code>ed448</code> and <code>x448</code> curves are not supported.</li>
<li>It is not possible to manually enable or disable <a href="https://nodejs.org/docs/latest/api/crypto.html#fips-mode">FIPS mode</a>.</li>
</ul>
<p>The full <code>node:crypto</code> API is documented in the <a href="https://nodejs.org/api/crypto.html">Node.js documentation for <code>node:crypto</code></a>.</p>
<p>The <a href="/workers/runtime-apis/web-crypto/">WebCrypto API</a> is also available within Cloudflare Workers. This does not
require the <code>nodejs_compat</code> compatibility flag.</p>
