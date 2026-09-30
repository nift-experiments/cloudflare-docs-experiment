---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/
  description: Recommended cipher suite security levels for different use cases.
  full_title: Cipher suite recommendations · Cloudflare SSL/TLS docs
  head_html: <title>Cipher suite recommendations · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Recommended cipher suite security levels for different use cases."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/index.md"><meta property="og:title" content="Cipher suite recommendations · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Recommended cipher suite security levels for different use cases."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/#page","headline":"Cipher suite recommendations \u00b7 Cloudflare SSL/TLS docs","description":"Recommended cipher suite security levels for different use cases.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/cipher-suites/recommendations/
  schema: 1
---
<p>Refer to the sections below for three different security levels and how Cloudflare recommends that you set them up if you need to restrict the <a href="/ssl/edge-certificates/additional-options/cipher-suites/">cipher suites</a> used between Cloudflare and clients that access your website or application.</p>
<p>Refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">Customize cipher suites</a> to learn how to specify cipher suites at zone level or per hostname.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14163.md")
</aside>
<h2 id="modern">Modern</h2>
<p>Offers the best security and performance, limiting your range of clients to modern devices and browsers. Supports TLS 1.2-1.3 cipher suites. All suites are forward-secret and support authenticated encryption (AEAD).</p>
<details class="nb-details"><summary>Cipher suites list</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14164.md")
</div></details>
<p>If you are customizing cipher suites via API, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples">Steps and API examples</a> for a snippet you can copy with the formatted array.</p>
<h2 id="compatible">Compatible</h2>
<p>Provides broader compatibility with somewhat weaker security. Supports TLS 1.2-1.3 cipher suites. All suites are forward-secret.</p>
<details class="nb-details"><summary>Cipher suites list</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14165.md")
</div></details>
<p>If you are customizing cipher suites via API, refer to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/#steps-and-api-examples">Steps and API examples</a> for a snippet you can copy with the formatted array.</p>
<h2 id="legacy-default">Legacy (default)</h2>
<p>Includes all cipher suites that Cloudflare supports today. Broadest compatibility with the weakest security. Supports TLS 1.0-1.3 cipher suites.</p>
<details class="nb-details"><summary>Cipher suites list</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14166.md")
</div></details>
<p>To reset your option to the default, <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/#reset-to-default-values">use an empty array</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Same as `TLS_AES_128_GCM_SHA256`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li>
<li id="footnote-2">Same as `TLS_AES_256_GCM_SHA384`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li>
<li id="footnote-3">Same as `TLS_CHACHA20_POLY1305_SHA256`. Refer to [TLS 1.3 cipher suites](/ssl/edge-certificates/additional-options/cipher-suites/#tls-13) for details.</li>
<li id="footnote-4">Although configured independently, cipher suites interact with **Minimum TLS version** and **TLS 1.3**.</li></ol></section>
