---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/
  description: Turn on Universal SSL certificates for your domain.
  full_title: Enable Universal SSL certificates · Cloudflare SSL/TLS docs
  head_html: <title>Enable Universal SSL certificates · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Turn on Universal SSL certificates for your domain."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/index.md"><meta property="og:title" content="Enable Universal SSL certificates · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Turn on Universal SSL certificates for your domain."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#page","headline":"Enable Universal SSL certificates \u00b7 Cloudflare SSL/TLS docs","description":"Turn on Universal SSL certificates for your domain.","url":"https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/universal-ssl/enable-universal-ssl/
  schema: 1
---
<div class="nb-glossary-definition"><p>By default, Cloudflare issues — and <a href="/ssl/reference/certificate-validity-periods/#universal-ssl">renews</a> — free, unshared, publicly trusted SSL certificates to all domains <a href="/fundamentals/manage-domains/add-site/">added to</a> and <a href="/dns/zone-setups/reference/domain-status/">activated on</a> Cloudflare.</p></div>
<hr />
<p>The process for activating a Universal SSL certificate depends on your domain's DNS setup.</p>
<h2 id="full-dns-setup">Full DNS setup</h2>
<p>For domains on a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a><sup><a href="#footnote-ssl-universal-ssl-enable-full-mdx-1">1</a></sup>, your domain should <strong>automatically</strong> receive its Universal SSL certificate within <strong>15 minutes to 24 hours</strong> of domain activation<sup><a href="#footnote-ssl-universal-ssl-enable-full-mdx-2">2</a></sup>.</p>
<p>This certificate will cover your zone apex (<code>example.com</code>) and all first-level subdomains (<code>subdomain.example.com</code>), and is provisioned even if your records are DNS only. However, the certificate will only be presented if your domain or subdomains are <a href="/dns/proxy-status/">proxied</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-ssl-universal-ssl-enable-full-mdx-1">The most common Cloudflare setup that involves changing your authoritative nameservers.</li>
<li id="footnote-ssl-universal-ssl-enable-full-mdx-2">Provisioning time depends on certain security checks and other requirements mandated by Certificate Authorities (CA).</li></ol></section>
<h3 id="minimize-downtime">Minimize downtime</h3>
<p>If your website or application is already live and cannot be uncovered while the Universal certificate is provisioned, consider the following:</p>
<ul>
<li>Order an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a> before proxying traffic to Cloudflare.</li>
<li>Upload a <a href="/ssl/edge-certificates/custom-certificates/">custom certificate</a> prior to migrating and then delete the certificate after your <a href="#verify-your-certificate-is-active">Universal certificate is active</a>.</li>
<li>Keep DNS records <a href="/dns/proxy-status/"><strong>unproxied</strong></a> until your <a href="#verify-your-certificate-is-active">certificate is active</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14053.md")
</aside>
<h2 id="partial-dns-setup">Partial DNS setup</h2>
<p>For non-authoritative or <a href="/dns/zone-setups/partial-setup/">partial domains</a>, Universal SSL will be:</p>
<ul>
<li>Provisioned once the DNS record is <a href="/dns/zone-setups/partial-setup/setup/#3-add-dns-records">proxied through Cloudflare</a>.</li>
<li>Validated:
<ul>
<li>Immediately if you add <a href="/ssl/edge-certificates/changing-dcv-method/">Domain Control Validation (DCV)</a> records to your authoritative DNS.</li>
<li>After a brief period of downtime if you <strong>do not</strong> add DCV records (once your traffic is proxied).</li>
</ul>
</li>
</ul>
<p>Unless you cover and validate multiple subdomains with an <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificate</a>, you will need to proxy and validate new subdomains as they are added.</p>
<hr />
<h2 id="verify-your-certificate-is-active">Verify your certificate is active</h2>
<p>Once you enable Universal SSL, you can review the <a href="/ssl/reference/certificate-statuses/">activation status</a> on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page or via the API with a <a href="/api/resources/ssl/subresources/certificate_packs/methods/list/">GET request</a>.</p>
<hr />
<h2 id="universal-ssl-renewal">Universal SSL renewal</h2>
<p>For Universal certificates, Cloudflare controls the validity periods and certificate authorities (CAs), making sure that renewal always occur.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="partial-setup-and-dcv">Partial setup and DCV</h3>
@markup("md", "content/.markup/bodies/14052.md")
</aside>
<p>Universal certificates have a 90-day validity period. The auto renewal period starts 30 days before expiration.</p>
<p>For details, refer to <a href="/ssl/reference/certificate-validity-periods/">Validity periods and renewal</a>.</p>
