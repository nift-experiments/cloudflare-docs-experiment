---
cp9:
  canonical: https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/troubleshooting/
  description: Troubleshoot issues like NET::ERR_CERT_AUTHORITY_INVALID when using Cloudflare origin CA.
  full_title: Troubleshooting Cloudflare origin CA · Cloudflare SSL/TLS docs
  head_html: <title>Troubleshooting Cloudflare origin CA · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot issues like NET::ERR_CERT_AUTHORITY_INVALID when using Cloudflare origin CA."><link rel="canonical" href="https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting Cloudflare origin CA · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot issues like NET::ERR_CERT_AUTHORITY_INVALID when using Cloudflare origin CA."><meta property="og:url" content="https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/troubleshooting/#page","headline":"Troubleshooting Cloudflare origin CA \u00b7 Cloudflare SSL/TLS docs","description":"Troubleshoot issues like NET::ERRCERTAUTHORITYINVALID when using Cloudflare origin CA.","url":"https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/origin-configuration/origin-ca/troubleshooting/
  schema: 1
---
<p>Consider the following common issues and troubleshooting steps when using <a href="/ssl/origin-configuration/origin-ca/">Cloudflare origin CA</a>.</p>
<h2 id="net-err-cert-authority-invalid">NET::ERR_CERT_AUTHORITY_INVALID</h2>
<h3 id="cause">Cause</h3>
<p>Site visitors may see untrusted certificate errors if you <a href="/fundamentals/manage-domains/pause-cloudflare/">pause Cloudflare</a> or <span class="nb-glossary-tooltip" title="proxy status">disable proxying</span> on subdomains that use Cloudflare origin CA certificates. These certificates only encrypt traffic between Cloudflare and your origin server, not traffic from client browsers to your origin.</p>
<p>This also means that SSL Labs or similar SSL validators are expected to flag the certificate as invalid.</p>
<h3 id="solutions">Solutions</h3>
<ul>
<li>Make sure the <a href="/dns/proxy-status/">proxy status</a> of your DNS records and any <a href="/rules/page-rules/">page rules</a> (if existing) are set up correctly. If so, you can try to turn proxying off and then on again and wait a few minutes.</li>
<li>If you must have direct connections between clients and your origin server, consider installing a publicly trusted certificate at your origin instead. This process is done outside of Cloudflare, where you should issue the certificate directly from a <span class="nb-glossary-tooltip" title="Certificate Authority (CA)">certificate authority (CA)</span> of your choice. You can still use Full (strict) <a href="/ssl/origin-configuration/ssl-modes/">encryption mode</a>, as long as the CA is listed on the <a href="https://github.com/cloudflare/cfssl_trust">Cloudflare trust store</a>.</li>
</ul>
<h2 id="the-issuer-of-this-certificate-could-not-be-found">The issuer of this certificate could not be found</h2>
<h3 id="cause-1">Cause</h3>
<p>Some origin web servers require that you upload the Cloudflare origin CA root certificate or certificate chain.</p>
<h3 id="solution">Solution</h3>
<p>Use the following links to download either an ECC or an RSA version and upload to your origin web server:</p>
<ul>
<li><a href="/ssl/static/origin_ca_ecc_root.pem">Cloudflare Origin ECC PEM</a> (do not use with Apache cPanel)</li>
<li><a href="/ssl/static/origin_ca_rsa_root.pem">Cloudflare Origin RSA PEM</a></li>
</ul>
<h2 id="the-certificate-is-not-trusted-in-all-web-browsers">The certificate is not trusted in all web browsers</h2>
<h3 id="cause-2">Cause</h3>
<p>Apache cPanel requires that you upload the Cloudflare origin CA root certificate or certificate chain.</p>
<h3 id="solution-1">Solution</h3>
<p>Use the following link to download an RSA version of the root certificate and upload it to your origin web server:</p>
<ul>
<li><a href="/ssl/static/origin_ca_rsa_root.pem">Cloudflare Origin RSA PEM</a></li>
</ul>
<h2 id="this-zone-is-either-not-part-of-your-account-or-you-do-not-have-access-to-it">This zone is either not part of your account, or you do not have access to it</h2>
<p>When trying to generate an Origin CA on the dashboard, you find the error <code>Failed to validate requested hostname &lt;hostname&gt;: This zone is either not part of your account, or you do not have access to it</code>.</p>
<h3 id="cause-3">Cause</h3>
<p>This is a known issue where, whilst being created on the Cloudflare dashboard, Origin CA requires API access for the user creating the origin certificate.
If the user does not have <strong>API Access</strong>, this error is returned.</p>
<h3 id="solution-2">Solution</h3>
<p>Make sure that the user creating the certificate has access to the API. You can check in the account <strong>Members</strong> page.</p>
<div class="nb-dash-button"></div>
<ul>
<li>The default setting for the account is specified in the card <strong>Enable API Access</strong>.</li>
<li>Specific user API Access (which can override the default setting) is presented after selecting the user in the list of members.</li>
</ul>
