---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/
  description: Error messages you may encounter with Total TLS.
  full_title: Total TLS error messages · Cloudflare SSL/TLS docs
  head_html: <title>Total TLS error messages · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Error messages you may encounter with Total TLS."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/index.md"><meta property="og:title" content="Total TLS error messages · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Error messages you may encounter with Total TLS."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/#page","headline":"Total TLS error messages \u00b7 Cloudflare SSL/TLS docs","description":"Error messages you may encounter with Total TLS.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/total-tls/error-messages/
  schema: 1
---
<p>To help avoid <a href="/ssl/troubleshooting/version-cipher-mismatch/"><code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code></a> errors, Cloudflare automatically shows an error message - <code>This hostname is not covered by a certificate</code> - on proxied DNS records not covered by a TLS certificate.</p>
<h2 id="pending-domains">Pending domains</h2>
<p>If you recently <a href="/fundamentals/manage-domains/add-site/">added your domain</a> to Cloudflare - meaning that your zone is in a <a href="/dns/zone-setups/reference/domain-status/">pending state</a> - you can often ignore this warning.</p>
<p>Once most domains becomes <strong>Active</strong>, Cloudflare will automatically issue a Universal SSL certificate, which will provide SSL/TLS coverage and remove the warning message.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14157.md")
</aside>
<h2 id="active-domains">Active domains</h2>
<p>If your zone is already active on Cloudflare, this warning identifies subdomains that are not covered by your current SSL/TLS certificate.</p>
<p>By default, Cloudflare <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificates</a> only cover your apex domain and one level of subdomain.</p>
<table>
<thead>
<tr>
<th>Hostname</th>
<th>Covered by Universal certificate?</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>www.example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>docs.example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>dev.docs.example.com</code></td>
<td>No</td>
</tr>
<tr>
<td><code>test.dev.api.example.com</code></td>
<td>No</td>
</tr>
</tbody>
</table>
<p>To prevent insecure connections on a multi-level subdomain, do one of the following:</p>
<ul>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a>, which automatically issues individual certificates to your proxied hostnames not covered by a Universal certificate.</li>
<li>Order an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">Advanced Certificate</a> covering the subdomain.</li>
<li>Upload a <a href="/ssl/edge-certificates/custom-certificates/">Custom Certificate</a> covering the subdomain.</li>
</ul>
<p>If none of these solutions work, you could also remove the multi-level subdomain.</p>
