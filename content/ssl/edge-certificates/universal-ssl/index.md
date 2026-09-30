---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/
  description: Free TLS certificates automatically issued for all proxied hostnames.
  full_title: Free Universal SSL/TLS certificates · Cloudflare SSL/TLS docs
  head_html: <title>Free Universal SSL/TLS certificates · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Free TLS certificates automatically issued for all proxied hostnames."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/index.md"><meta property="og:title" content="Free Universal SSL/TLS certificates · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Free TLS certificates automatically issued for all proxied hostnames."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/#page","headline":"Free Universal SSL/TLS certificates \u00b7 Cloudflare SSL/TLS docs","description":"Free TLS certificates automatically issued for all proxied hostnames.","url":"https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/universal-ssl/
  schema: 1
---
<div class="nb-glossary-definition"><p>By default, Cloudflare issues — and <a href="/ssl/reference/certificate-validity-periods/#universal-ssl">renews</a> — free, unshared, publicly trusted SSL certificates to all domains <a href="/fundamentals/manage-domains/add-site/">added to</a> and <a href="/dns/zone-setups/reference/domain-status/">activated on</a> Cloudflare.</p></div>
<p>On a <a href="/dns/zone-setups/full-setup/">full setup</a>, Universal SSL certificates cover your root domain (for example, <code>example.com</code>) and first-level subdomains (for example, <code>www.example.com</code>). On a <a href="/dns/zone-setups/partial-setup/">partial (CNAME) setup</a>, each proxied subdomain receives its own certificate regardless of depth. Cloudflare handles issuance, renewal, and deployment automatically.</p>
<p>For full setup zones that need coverage beyond first-level subdomains, use <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a>.</p>
<p>Universal certificates are <a href="/ssl/concepts/#validation-level">Domain Validated (DV)</a>, which means the certificate authority verifies domain ownership but does not validate organization identity. For setup details, refer to <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/">Enable Universal SSL</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14051.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ssl/edge-certificates/universal-ssl/limitations/">Limitations</a></li>
<li><a href="/ssl/edge-certificates/backup-certificates/">Backup certificates</a></li>
<li><a href="/ssl/reference/certificate-validity-periods/#universal-ssl">Validity period and renewal</a></li>
</ul>
