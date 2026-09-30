---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/ip-addresses/
  description: Get IPv4 and IPv6 addresses for Cloudflare DNS resolvers, 1.1.1.1 and 1.1.1.1 for Families.
  full_title: IP addresses · Cloudflare 1.1.1.1 docs
  head_html: <title>IP addresses · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Get IPv4 and IPv6 addresses for Cloudflare DNS resolvers, 1.1.1.1 and 1.1.1.1 for Families."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/ip-addresses/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/ip-addresses/index.md"><meta property="og:title" content="IP addresses · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Get IPv4 and IPv6 addresses for Cloudflare DNS resolvers, 1.1.1.1 and 1.1.1.1 for Families."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/ip-addresses/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/ip-addresses/#page","headline":"IP addresses \u00b7 Cloudflare 1.1.1.1 docs","description":"Get IPv4 and IPv6 addresses for Cloudflare DNS resolvers, 1.1.1.1 and 1.1.1.1 for Families.","url":"https://developers.cloudflare.com/1.1.1.1/ip-addresses/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/ip-addresses/
  schema: 1
---
<p>Use the addresses below to configure your device or router. Two addresses are provided for each resolver for redundancy.</p>
<p>For step-by-step instructions, refer to <a href="/1.1.1.1/setup/">Set up</a>.</p>
<hr />
<h2 id="1-1-1-1">1.1.1.1</h2>
<p>The standard resolver provides fast, private DNS lookups with no content filtering.</p>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1.1.1.1</code> <br/><code>1.0.0.1</code></td>
<td><code>2606:4700:4700::1111</code> <br/><code>2606:4700:4700::1001</code></td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/1.1.1.1/encryption/">Encryption</a> to learn how to encrypt your DNS queries.</p>
<hr />
<h2 id="1-1-1-1-for-families">1.1.1.1 for Families</h2>
<p>1.1.1.1 for Families adds automatic filtering to block known malware, phishing, and (optionally) adult content.</p>
<p>For more information, refer to <a href="/1.1.1.1/setup/#1111-for-families">1.1.1.1 for Families set up</a>.</p>
<h3 id="block-malware">Block malware</h3>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1.1.1.2</code> <br/><code>1.0.0.2</code></td>
<td><code>2606:4700:4700::1112</code> <br/><code>2606:4700:4700::1002</code></td>
</tr>
</tbody>
</table>
<h3 id="block-malware-and-adult-content">Block malware and adult content</h3>
<table>
<thead>
<tr>
<th>IPv4</th>
<th>IPv6</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1.1.1.3</code> <br/><code>1.0.0.3</code></td>
<td><code>2606:4700:4700::1113</code> <br/><code>2606:4700:4700::1003</code></td>
</tr>
</tbody>
</table>
