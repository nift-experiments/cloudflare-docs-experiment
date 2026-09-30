---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/
  description: Review a list of cipher suites that Cloudflare presents to origins during an SSL/TLS handshake.
  full_title: Cipher suites — Origin · Cloudflare SSL/TLS docs
  head_html: <title>Cipher suites — Origin · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Review a list of cipher suites that Cloudflare presents to origins during an SSL/TLS handshake."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/index.md"><meta property="og:title" content="Cipher suites — Origin · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review a list of cipher suites that Cloudflare presents to origins during an SSL/TLS handshake."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/#page","headline":"Cipher suites \u2014 Origin \u00b7 Cloudflare SSL/TLS docs","description":"Review a list of cipher suites that Cloudflare presents to origins during an SSL/TLS handshake.","url":"https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/cipher-suites/
  schema: 1
---
<p>Refer to the following list to know what cipher suites Cloudflare presents to origin servers during an SSL/TLS handshake.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14000.md")
</aside>
<p>The list order is based on how the cipher suites appear in the <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/#:~:text=client%20hello">ClientHello</a>, communicating Cloudflare's preference.</p>
<h2 id="supported-cipher-suites-by-protocol">Supported cipher suites by protocol</h2>
<table>
<thead>
<tr>
<th>Cipher name</th>
<th>TLS 1.0</th>
<th>TLS 1.1</th>
<th>TLS 1.2</th>
<th>TLS 1.3</th>
</tr>
</thead>
<tbody>
<tr>
<td>AEAD-AES128-GCM-SHA256 <sup><a href="#footnote-1">1</a></sup></td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>AEAD-AES256-GCM-SHA384 <sup><a href="#footnote-1">1</a></sup></td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>AEAD-CHACHA20-POLY1305-SHA256 <sup><a href="#footnote-1">1</a></sup></td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES128-GCM-SHA256</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-GCM-SHA256</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-SHA</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>AES128-GCM-SHA256</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>AES128-SHA</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES256-GCM-SHA384</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-GCM-SHA384</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-SHA384</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>AES256-SHA</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>DES-CBC3-SHA</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
</tr>
</tbody>
</table>
<h3 id="tls-1-3-cipher-suites">TLS 1.3 cipher suites</h3>
<p>Although TLS 1.3 uses the same cipher suite space as previous versions of TLS, TLS 1.3 cipher suites are defined differently, only specifying the symmetric ciphers, and cannot be used for TLS 1.2 (<a href="https://www.rfc-editor.org/rfc/rfc8446.html">RFC 8446</a>).</p>
<p>Similarly, TLS 1.2 and lower cipher suites cannot be used with TLS 1.3. BoringSSL also hard-codes cipher preferences in the order above for TLS 1.3.</p>
<p>Based on BoringSSL, Cloudflare system will return the names listed above. However, the corresponding names defined in <a href="https://www.rfc-editor.org/rfc/rfc8446.html">RFC 8446</a> are the following:</p>
<ul>
<li><code>TLS_AES_128_GCM_SHA256</code></li>
<li><code>TLS_AES_256_GCM_SHA384</code></li>
<li><code>TLS_CHACHA20_POLY1305_SHA256</code></li>
</ul>
<h2 id="match-on-origin">Match on origin</h2>
<p>Cloudflare will present the cipher suites to your origin and your server will select whichever cipher suite it prefers.</p>
<p>However, if you want to ensure that your origin server supports the same cipher suites that Cloudflare supports at our global network and you use <a href="https://en.wikipedia.org/wiki/Nginx">NGINX</a> for TLS termination on your origin, you can apply the following configuration:</p>
<pre tabindex="0"><code class="language-txt">ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;&#10;ssl_ecdh_curve X25519:P-256:P-384;&#10;ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-CHACHA20-POLY1305:ECDHE+AES128:RSA+AES128:ECDHE+AES256:RSA+AES256:ECDHE+3DES:RSA+3DES;&#10;ssl_prefer_server_ciphers on;&#10;</code></pre>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Refer to [TLS 1.3 cipher suites](#tls-13-cipher-suites) for details.</li></ol></section>
