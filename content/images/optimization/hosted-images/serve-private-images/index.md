---
cp9:
  canonical: https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/
  description: Restrict access to Cloudflare Images by generating signed URL tokens with expiration times.
  full_title: Serve private images · Cloudflare Images docs
  head_html: <title>Serve private images · Cloudflare Images docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict access to Cloudflare Images by generating signed URL tokens with expiration times."><link rel="canonical" href="https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/index.md"><meta property="og:title" content="Serve private images · Cloudflare Images docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict access to Cloudflare Images by generating signed URL tokens with expiration times."><meta property="og:url" content="https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Images"><meta name="algolia_product_filter" content="Cloudflare Images"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Images"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/#page","headline":"Serve private images \u00b7 Cloudflare Images docs","description":"Restrict access to Cloudflare Images by generating signed URL tokens with expiration times.","url":"https://developers.cloudflare.com/images/optimization/hosted-images/serve-private-images/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /images/optimization/hosted-images/serve-private-images/
  schema: 1
---
<p>You can serve private images by using signed URL tokens. When an image requires a signed URL, the image cannot be accessed without a token unless it is being requested for a variant set to always allow public access.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Keys</strong>.</li>
<li>Copy your key and use it to generate an expiring tokenized URL.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9467.md")
</aside>
<h2 id="generate-signed-urls-from-your-backend">Generate signed URLs from your backend</h2>
<p>Signed URLs are generated server-side to protect your signing key. The example below uses a Cloudflare Worker, but the same signing logic can be implemented in any backend environment (Node.js, Python, PHP, Go, etc.).</p>
<p>The Worker accepts a regular Images URL and returns a signed URL that expires after one day. Adjust the <code>EXPIRATION</code> value to set a different expiry period.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9466.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/9468.md")
</div>
