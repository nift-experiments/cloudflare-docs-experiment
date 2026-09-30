---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/
  description: Review the TLS cipher suites supported by `cloudflared` for secure connections between your origin and Cloudflare's network.
  full_title: Cipher suites · Cloudflare One docs
  head_html: <title>Cipher suites · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Review the TLS cipher suites supported by `cloudflared` for secure connections between your origin and Cloudflare&#x27;s network."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/index.md"><meta property="og:title" content="Cipher suites · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review the TLS cipher suites supported by `cloudflared` for secure connections between your origin and Cloudflare&#x27;s network."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/#page","headline":"Cipher suites \u00b7 Cloudflare One docs","description":"Review the TLS cipher suites supported by cloudflared for secure connections between your origin and Cloudflare's network.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cipher-suites/
  schema: 1
---
<p>Cloudflare Tunnel connections use the cipher suites supported by <code>cloudflared</code>, which relies on the Go TLS library for its TLS implementation. These cipher suites apply to both the TLS connection between Cloudflare's network and <code>cloudflared</code>, and the HTTPS connection between <code>cloudflared</code> and your origin. In both cases, <code>cloudflared</code> negotiates the most secure cipher suite supported by both sides. All tunnel connections use TLS 1.3 and post-quantum encryption by default.</p>
<p>The following table lists the cipher suites supported by <code>cloudflared</code>:</p>
<table>
<thead>
<tr>
<th>Protocol support</th>
<th>Cipher suites</th>
</tr>
</thead>
<tbody>
<tr>
<td>TLS 1.3 only</td>
<td><code>TLS_AES_128_GCM_SHA256</code><br /><code>TLS_AES_256_GCM_SHA384</code><br /><code>TLS_CHACHA20_POLY1305_SHA256</code></td>
</tr>
<tr>
<td>TLS 1.2 only</td>
<td><code>TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256</code><br /><code>TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384</code><br /><code>TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256</code><br /><code>TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384</code><br /><code>TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256</code><br /><code>TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256</code></td>
</tr>
<tr>
<td>Up to and including TLS 1.2</td>
<td><code>TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA</code><br /><code>TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA</code><br /><code>TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA</code><br /><code>TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA</code></td>
</tr>
</tbody>
</table>
