---
cp9:
  canonical: https://developers.cloudflare.com/r2/examples/ssec/
  description: The following tutorial shows some snippets for how to use Server-Side Encryption with Customer-Provided Keys (SSE-C) on Cloudflare R2.
  full_title: Use SSE-C · Cloudflare R2 docs
  head_html: <title>Use SSE-C · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="The following tutorial shows some snippets for how to use Server-Side Encryption with Customer-Provided Keys (SSE-C) on Cloudflare R2."><link rel="canonical" href="https://developers.cloudflare.com/r2/examples/ssec/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/examples/ssec/index.md"><meta property="og:title" content="Use SSE-C · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="The following tutorial shows some snippets for how to use Server-Side Encryption with Customer-Provided Keys (SSE-C) on Cloudflare R2."><meta property="og:url" content="https://developers.cloudflare.com/r2/examples/ssec/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/examples/ssec/#page","headline":"Use SSE-C \u00b7 Cloudflare R2 docs","description":"The following tutorial shows some snippets for how to use Server-Side Encryption with Customer-Provided Keys (SSE-C) on Cloudflare R2.","url":"https://developers.cloudflare.com/r2/examples/ssec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/examples/ssec/
  schema: 1
---
<p>The following tutorial shows some snippets for how to use Server-Side Encryption with Customer-Provided Keys (SSE-C) on R2.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>When using SSE-C, make sure you store your encryption key(s) in a safe place. In the event you misplace them, Cloudflare will be unable to recover the body of any objects encrypted using those keys.</li>
<li>While SSE-C does provide MD5 hashes, this hash can be used for identification of keys only. The MD5 hash is not used in the encryption process itself.</li>
</ul>
<h2 id="workers">Workers</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11452.md")
</div></div>
<h2 id="s3-api">S3-API</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11454.md")
</div></div>
