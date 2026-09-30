---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/
  description: Custom Origin Trust Store allows you to upload certificate authorities (CAs) that Cloudflare will use to authenticate connections to your origin server.
  full_title: Custom Origin Trust Store · Cloudflare SSL/TLS docs
  head_html: <title>Custom Origin Trust Store · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Custom Origin Trust Store allows you to upload certificate authorities (CAs) that Cloudflare will use to authenticate connections to your origin server."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/index.md"><meta property="og:title" content="Custom Origin Trust Store · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Custom Origin Trust Store allows you to upload certificate authorities (CAs) that Cloudflare will use to authenticate connections to your origin server."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/#page","headline":"Custom Origin Trust Store \u00b7 Cloudflare SSL/TLS docs","description":"Custom Origin Trust Store allows you to upload certificate authorities (CAs) that Cloudflare will use to authenticate connections to your origin server.","url":"https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/custom-origin-trust-store/
  schema: 1
---
<p>By default, Cloudflare's global network maintains <a href="https://github.com/cloudflare/cfssl_trust">a list of publicly trusted certificate authorities</a>. This means that when using <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) encryption mode</a>, Cloudflare will only trust origin server certificates issued by a CA included in this trust store.</p>
<p>Custom Origin Trust Store allows you to upload certificate authorities (CAs) that Cloudflare will use to authenticate connections to your origin server. Use this feature to override the default trust store with your preferred CA or CAs.
<br /></p>
<p>When a CA has been uploaded to Custom Origin Trust Store, Cloudflare will ignore all default publicly trusted CAs and exclusively use the CA or CAs that have been uploaded to authenticate the origin server.</p>
<h2 id="availability">Availability</h2>
<p>To get access to Custom Origin Trust Store, <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> must be enabled on the zone.</p>
<h2 id="post-quantum-certificate-authorities">Post-quantum certificate authorities</h2>
<p>Custom Origin Trust Store accepts ML-DSA (FIPS 204) post-quantum certificate authorities. Refer to <a href="/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures">Post-quantum signatures</a> for certificate generation and upload guidance.</p>
<h2 id="how-to">How to</h2>
<p>To manage origin trust stores in the dashboard:</p>
<ol>
<li>Go to the <strong>Origin Server</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Custom Origin Trust Store</strong> tab.</li>
<li>Select <strong>Upload trust store</strong> to add a CA certificate, or use the table to manage existing trust stores.</li>
</ol>
<p>To manage origin trust stores using the API, refer to the <a href="#api-commands">API commands</a>.</p>
<h2 id="limitations">Limitations</h2>
<p>With <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) encryption mode</a> enabled, if your uploaded CA expires and no alternative CAs are valid within the trust store, Cloudflare will not be able to properly authenticate connections to the origin server.</p>
<h2 id="api-commands">API commands</h2>
<h4 id="list-custom-origin-trust-store-details">List Custom Origin Trust Store Details</h4>
<ul>
<li>API documentation: <a href="/api/resources/acm/subresources/custom_trust_store/methods/list/">List Custom Origin Trust Store Details</a></li>
<li>Method: <code>GET</code></li>
<li>Endpoint: <code>/zones/$ZONE_ID/acm/custom_trust_store</code></li>
</ul>
<h4 id="custom-origin-trust-store-details">Custom Origin Trust Store Details</h4>
<ul>
<li>API documentation: <a href="/api/resources/acm/subresources/custom_trust_store/methods/get/">Custom Origin Trust Store Details</a></li>
<li>Method: <code>GET</code></li>
<li>Endpoint: <code>/zones/$ZONE_ID/acm/custom_trust_store/$CUSTOM_ORIGIN_TRUST_STORE_ID</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13999.md")
</aside>
<h4 id="upload-custom-origin-trust-store">Upload Custom Origin Trust Store</h4>
<ul>
<li>API documentation: <a href="/api/resources/acm/subresources/custom_trust_store/methods/create/">Upload Custom Origin Trust Store</a></li>
<li>Method: <code>POST</code></li>
<li>Endpoint: <code>/zones/$ZONE_ID/acm/custom_trust_store</code></li>
</ul>
<h4 id="delete-custom-origin-trust-store">Delete Custom Origin Trust Store</h4>
<ul>
<li>API documentation: <a href="/api/resources/acm/subresources/custom_trust_store/methods/delete/">Delete Custom Origin Trust Store</a></li>
<li>Method: <code>DELETE</code></li>
<li>Endpoint: <code>/zones/$ZONE_ID/acm/custom_trust_store/$CUSTOM_ORIGIN_TRUST_STORE_ID</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13998.md")
</aside>
