---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/
  description: Issue individual certificates for every proxied subdomain.
  full_title: Total TLS · Cloudflare SSL/TLS docs
  head_html: <title>Total TLS · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Issue individual certificates for every proxied subdomain."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/index.md"><meta property="og:title" content="Total TLS · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Issue individual certificates for every proxied subdomain."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/#page","headline":"Total TLS \u00b7 Cloudflare SSL/TLS docs","description":"Issue individual certificates for every proxied subdomain.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/total-tls/
  schema: 1
---
<p>Total TLS allows Cloudflare to issue individual certificates for your proxied hostnames. These certificates will protect proxied hostnames not covered by <a href="/ssl/edge-certificates/universal-ssl/">Universal certificates</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14156.md")
</aside>
<p>When issued, these certificates will have a type of <strong>Advanced - Total TLS</strong>, and their default validity period is 90 days.</p>
<h2 id="reference">Reference</h2>
<ul class="directory-listing"><li><a href="/ssl/edge-certificates/additional-options/total-tls/enable/">Enable</a></li><li><a href="/ssl/edge-certificates/additional-options/total-tls/error-messages/">Error messages</a></li></ul>
<h2 id="availability">Availability</h2>
<p>Total TLS is available for domains that have purchased <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> and are currently using a <a href="/dns/zone-setups/full-setup/">full DNS setup</a>.</p>
<h2 id="limitations">Limitations</h2>
<h3 id="hostnames-used-with-other-cloudflare-products">Hostnames used with other Cloudflare products</h3>
<p>Total TLS does not issue certificates for any hostnames used with:</p>
<ul>
<li><a href="/load-balancing/">Cloudflare Load Balancing</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">Cloudflare Tunnel</a></li>
<li><a href="/spectrum/">Cloudflare Spectrum</a></li>
</ul>
<p>You can use other types of certificates or manually <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate">order advanced certificates</a> for these hostnames.</p>
<h3 id="deleting-certificates">Deleting certificates</h3>
<p>Once you <a href="/ssl/edge-certificates/additional-options/total-tls/enable/">enable Total TLS</a>, be careful deleting any Total TLS certificates associated with proxied hostnames.</p>
<p>If you do, our system assumes you want to opt that hostname out of Total TLS certificate and will not order new certificates for the hostname in the future. This behavior applies even if you delete and re-create the hostname's DNS record.</p>
