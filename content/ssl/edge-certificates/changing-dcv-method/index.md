---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/
  description: Understand when domain control validation is required and when Cloudflare handles it automatically.
  full_title: Domain control validation (DCV) · Cloudflare SSL/TLS docs
  head_html: <title>Domain control validation (DCV) · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand when domain control validation is required and when Cloudflare handles it automatically."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/index.md"><meta property="og:title" content="Domain control validation (DCV) · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand when domain control validation is required and when Cloudflare handles it automatically."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/#page","headline":"Domain control validation (DCV) \u00b7 Cloudflare SSL/TLS docs","description":"Understand when domain control validation is required and when Cloudflare handles it automatically.","url":"https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/changing-dcv-method/
  schema: 1
---
<p>Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).</p>
<p>If DCV is not completed, the CA cannot issue or renew the certificate, and visitors to your site will see SSL/TLS errors.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14106.md")
</aside>
<p>For <a href="/ssl/edge-certificates/custom-certificates/">custom certificates</a>, you handle DCV directly with the CA when requesting or renewing the certificate.</p>
<p>For certificates issued through Cloudflare, whether DCV is automatic depends on your DNS setup.</p>
<hr />
<h2 id="full-dns-setup-no-action-required">Full DNS setup - no action required</h2>
<p>If your domain is on a <a href="/dns/zone-setups/full-setup/"><strong>full setup</strong></a> — meaning that Cloudflare runs your authoritative nameservers — Cloudflare handles DCV automatically on your behalf using a TXT record. For more details, refer to <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/#full-dns-setup">Enable Universal SSL</a>.</p>
<hr />
<h2 id="partial-dns-setup-action-sometimes-required">Partial DNS setup - action sometimes required</h2>
<p>If your application is on a <a href="/dns/zone-setups/partial-setup/">partial DNS setup</a> — meaning that Cloudflare does not run your authoritative nameservers — you may need to perform additional steps to complete DCV.</p>
<h3 id="non-wildcard-certificates">Non-wildcard certificates</h3>
<p>If every hostname on a non-wildcard certificate is <span class="nb-glossary-tooltip" title="proxy status">proxying traffic</span> through Cloudflare and the DCV method is <a href="/ssl/edge-certificates/changing-dcv-method/methods/http/">HTTP</a>, Cloudflare can automatically complete DCV on your behalf.</p>
<p>This applies to customers using <a href="/ssl/edge-certificates/universal-ssl/">Universal</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced certificates</a>.</p>
<p>If one of the hostnames on the certificate is not proxying traffic through Cloudflare, certificate issuance and renewal will vary based on the type of certificate you are using:</p>
<ul>
<li><strong>Universal</strong>: Perform DCV using one of the available <a href="/ssl/edge-certificates/changing-dcv-method/methods/">methods</a>.</li>
<li><strong>Advanced</strong>: In most cases, you can opt for <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a>, which greatly simplifies certificate management.</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/14105.md")
</aside>
<h3 id="wildcard-certificates">Wildcard certificates</h3>
<p>For wildcard hostname certificates, certificate issuance and renewal varies based on the type of certificate you are using:</p>
<ul>
<li><strong>Universal</strong>: Perform DCV using <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">TXT validation method</a>.</li>
<li><strong>Advanced</strong>: In most cases, you can opt for <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a>, which greatly simplifies certificate management.</li>
</ul>
<p>If you cannot use Delegated DCV, you need to use <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/">TXT based DCV</a> for certificate issuance and renewal. This means you will need to place one TXT DCV token for every hostname on the certificate. If one or more of the hostnames on the certificate fails to validate, the certificate will not be issued or renewed.</p>
<p>This means that a wildcard certificate covering <code>example.com</code> and <code>*.example.com</code> will require two DCV tokens to be placed at the authoritative DNS provider. Similarly, a certificate with five hostnames in the SAN (including a wildcard) will require five DCV tokens to be placed at the authoritative DNS provider.</p>
