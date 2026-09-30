---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/
  description: Full list of cipher suites supported by Cloudflare edge certificates.
  full_title: Supported cipher suites · Cloudflare SSL/TLS docs
  head_html: <title>Supported cipher suites · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Full list of cipher suites supported by Cloudflare edge certificates."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/index.md"><meta property="og:title" content="Supported cipher suites · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Full list of cipher suites supported by Cloudflare edge certificates."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/#page","headline":"Supported cipher suites \u00b7 Cloudflare SSL/TLS docs","description":"Full list of cipher suites supported by Cloudflare edge certificates.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/
  schema: 1
---
<p>Cloudflare supports the following cipher suites by default. If needed, you can <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">restrict your website or application</a> to only use specific cipher suites.</p>
<table>
<thead>
<tr>
<th>Cipher name</th>
<th>Minimum protocol</th>
<th><a href="/ssl/edge-certificates/additional-options/cipher-suites/recommendations/">Security recommendation</a></th>
<th>Cipher suite</th>
<th>IANA name</th>
</tr>
</thead>
<tbody>
<tr>
<td>ECDHE-ECDSA-AES128-GCM-SHA256</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xc02b]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</td>
</tr>
<tr>
<td>ECDHE-ECDSA-CHACHA20-POLY1305</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xcca9]</td>
<td>TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-GCM-SHA256</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xc02f]</td>
<td>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</td>
</tr>
<tr>
<td>ECDHE-RSA-CHACHA20-POLY1305</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xcca8]</td>
<td>TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES128-SHA256</td>
<td>TLS 1.2</td>
<td>Compatible, Legacy</td>
<td>[0xc023]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES128-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0xc009]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-SHA256</td>
<td>TLS 1.2</td>
<td>Compatible, Legacy</td>
<td>[0xc027]</td>
<td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256</td>
</tr>
<tr>
<td>ECDHE-RSA-AES128-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0xc013]</td>
<td>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA</td>
</tr>
<tr>
<td>AES128-GCM-SHA256</td>
<td>TLS 1.2</td>
<td>Legacy</td>
<td>[0x9c]</td>
<td>TLS_RSA_WITH_AES_128_GCM_SHA256</td>
</tr>
<tr>
<td>AES128-SHA256</td>
<td>TLS 1.2</td>
<td>Legacy</td>
<td>[0x3c]</td>
<td>TLS_RSA_WITH_AES_128_CBC_SHA256</td>
</tr>
<tr>
<td>AES128-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0x2f]</td>
<td>TLS_RSA_WITH_AES_128_CBC_SHA</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES256-GCM-SHA384</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xc02c]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</td>
</tr>
<tr>
<td>ECDHE-ECDSA-AES256-SHA384</td>
<td>TLS 1.2</td>
<td>Compatible, Legacy</td>
<td>[0xc024]</td>
<td>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-GCM-SHA384</td>
<td>TLS 1.2</td>
<td>Modern, Compatible, Legacy</td>
<td>[0xc030]</td>
<td>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-SHA384</td>
<td>TLS 1.2</td>
<td>Compatible, Legacy</td>
<td>[0xc028]</td>
<td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384</td>
</tr>
<tr>
<td>ECDHE-RSA-AES256-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0xc014]</td>
<td>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA</td>
</tr>
<tr>
<td>AES256-GCM-SHA384</td>
<td>TLS 1.2</td>
<td>Legacy</td>
<td>[0x9d]</td>
<td>TLS_RSA_WITH_AES_256_GCM_SHA384</td>
</tr>
<tr>
<td>AES256-SHA256</td>
<td>TLS 1.2</td>
<td>Legacy</td>
<td>[0x3d]</td>
<td>TLS_RSA_WITH_AES_256_CBC_SHA256</td>
</tr>
<tr>
<td>AES256-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0x35]</td>
<td>TLS_RSA_WITH_AES_256_CBC_SHA</td>
</tr>
<tr>
<td>DES-CBC3-SHA</td>
<td>TLS 1.0</td>
<td>Legacy</td>
<td>[0x0a]</td>
<td>TLS_RSA_WITH_3DES_EDE_CBC_SHA</td>
</tr>
<tr>
<td>AEAD-AES128-GCM-SHA256 *</td>
<td>TLS 1.3</td>
<td>Modern, Compatible, Legacy</td>
<td>{0x13,0x01}</td>
<td>TLS_AES_128_GCM_SHA256</td>
</tr>
<tr>
<td>AEAD-AES256-GCM-SHA384 *</td>
<td>TLS 1.3</td>
<td>Modern, Compatible, Legacy</td>
<td>{0x13,0x02}</td>
<td>TLS_AES_256_GCM_SHA384</td>
</tr>
<tr>
<td>AEAD-CHACHA20-POLY1305-SHA256 *</td>
<td>TLS 1.3</td>
<td>Modern, Compatible, Legacy</td>
<td>{0x13,0x03}</td>
<td>TLS_CHACHA20_POLY1305_SHA256</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tls-1-3-minimum-protocol">* TLS 1.3 minimum protocol</h3>
@markup("md", "content/.markup/bodies/14162.md")
</aside>
