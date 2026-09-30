---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/
  description: Validate domain control with a TXT DNS record.
  full_title: TXT method — Domain Control Validation — SSL/TLS · Cloudflare SSL/TLS docs
  head_html: <title>TXT method — Domain Control Validation — SSL/TLS · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Validate domain control with a TXT DNS record."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/index.md"><meta property="og:title" content="TXT method — Domain Control Validation — SSL/TLS · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Validate domain control with a TXT DNS record."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/#page","headline":"TXT method \u2014 Domain Control Validation \u2014 SSL/TLS \u00b7 Cloudflare SSL/TLS docs","description":"Validate domain control with a TXT DNS record.","url":"https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/changing-dcv-method/methods/txt/
  schema: 1
---
<p>TXT record validation requires the creation of a TXT record in the hostname's authoritative DNS.
<br /></p>
<hr />
<h2 id="when-to-use">When to use</h2>
<p>Generally, you need to perform TXT-based DCV when your certificate <a href="/ssl/edge-certificates/changing-dcv-method/">requires DCV</a> and you cannot perform <a href="/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/">Delegated DCV</a>.</p>
<hr />
<h2 id="setup">Setup</h2>
<h3 id="specify-dcv-method">Specify DCV method</h3>
<p>If you want to use a <a href="/ssl/edge-certificates/universal-ssl/enable-universal-ssl/">Universal SSL certificate</a>, you will need to edit the <code>validation_method</code> <a href="/api/resources/ssl/subresources/verification/methods/edit/">via the API</a> and specify your chosen validation method.</p>
<p>Alternatively, you could <a href="/ssl/edge-certificates/advanced-certificate-manager/">order an advanced certificate</a> via the dashboard or the API.</p>
<h3 id="get-dcv-values">Get DCV values</h3>
<p>Once you <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/#create-a-certificate">create a new certificate</a> and choose the validation method of <strong>TXT</strong>, your tokens will be ready after a few seconds.</p>
<p>These tokens can be fetched through the API or the dashboard when the certificates are in a <a href="/ssl/reference/certificate-statuses/#new-certificates">pending validation</a> state during custom hostname creation or during certificate renewals.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14188.md")
</div></div>
<h3 id="update-dns-records">Update DNS records</h3>
<p>At your authoritative DNS provider, create a TXT record named the <code>txt_name</code> and containing the <code>txt_value</code>.</p>
<p>Repeat this process for all the DCV records returned in the <code>validation_records</code> field to your Authoritative DNS provider.</p>
<p>If one or more of the hostnames on the certificate fail to validate, the certificate will not be issued or renewed.</p>
<p>This means that a wildcard certificate covering <code>example.com</code> and <code>*.example.com</code> will require two DCV tokens to be placed at the authoritative DNS provider. Similarly, a certificate with five hostnames in the SAN (including a wildcard) will require five DCV tokens to be placed at the authoritative DNS provider.
Certificates with several packs (RSA and ECDSA for example) may also require several DCV tokens.</p>
<h3 id="complete-dcv">Complete DCV</h3>
<p>Once you update your DNS records, you can either <a href="/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/">wait for the next retry</a> or request an immediate recheck.</p>
<p>To request an immediate recheck, send another <a href="/api/resources/ssl/subresources/verification/methods/edit/">PATCH request</a> with the same <code>validation_method</code> as your current validation method.</p>
<p>TXT records used for DCV can be removed from your authoritative DNS provider as soon as the certificate is issued.</p>
<h2 id="renewal">Renewal</h2>
<p>Even if you manually handle DCV when issuing certificates in a <a href="/dns/zone-setups/partial-setup/">partial DNS setup</a>, at certificate renewal, Cloudflare will attempt to automatically perform DCV via HTTP.</p>
<p>If all of the following conditions are confirmed at the first attempt, the renewal happens automatically via <a href="/ssl/edge-certificates/changing-dcv-method/methods/http/">HTTP</a>.</p>
<ul>
<li>Hostnames are proxied.</li>
<li>Hostnames on the certificate resolve to the IPs assigned to the zone.</li>
<li>The certificate does not contain wildcards.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14185.md")
</aside>
<p>If any one of the conditions is not met, the certificate renewal falls back to your chosen method and you will need to <a href="/ssl/edge-certificates/changing-dcv-method/methods/txt/#get-dcv-values">repeat the DCV process</a> manually.</p>
<p>Cloudflare generates renewal tokens 30 days before certificate expiration.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-2">Meaning that another DNS provider - not Cloudflare - maintains your Authoritative DNS.</li></ol></section>
