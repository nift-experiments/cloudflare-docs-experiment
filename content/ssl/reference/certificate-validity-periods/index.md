---
cp9:
  canonical: https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/
  description: Learn about Cloudflare SSL certificate validity periods, auto renewal processes, and the benefits of shorter validity periods for enhanced security.
  full_title: Validity periods and renewal · Cloudflare SSL/TLS docs
  head_html: <title>Validity periods and renewal · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about Cloudflare SSL certificate validity periods, auto renewal processes, and the benefits of shorter validity periods for enhanced security."><link rel="canonical" href="https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/index.md"><meta property="og:title" content="Validity periods and renewal · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about Cloudflare SSL certificate validity periods, auto renewal processes, and the benefits of shorter validity periods for enhanced security."><meta property="og:url" content="https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/#page","headline":"Validity periods and renewal \u00b7 Cloudflare SSL/TLS docs","description":"Learn about Cloudflare SSL certificate validity periods, auto renewal processes, and the benefits of shorter validity periods for enhanced security.","url":"https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/reference/certificate-validity-periods/
  schema: 1
---
<p>For certificates managed by Cloudflare, attempts to renew start at the auto renewal period and continue up until 24 hours before expiration. The auto renewal period varies according to the certificate validity period, as explained in the sections below.</p>
<p>If a certificate fails to renew and another valid certificate exists for the hostname, Cloudflare will deploy the valid certificate within the last 24 hours before expiration.</p>
<h2 id="certificate-types">Certificate types</h2>
<h3 id="universal-ssl">Universal SSL</h3>
<p>For Universal certificates, Cloudflare controls the validity periods and certificate authorities (CAs), making sure that renewal always occur.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="partial-setup-and-dcv">Partial setup and DCV</h3>
@markup("md", "content/.markup/bodies/13969.md")
</aside>
<p>Universal certificates have a 90-day validity period. The auto renewal period starts 30 days before expiration.</p>
<h3 id="advanced-certificates">Advanced certificates</h3>
<p>When you order an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">advanced certificate</a>, you can select different certificate validity periods. Each certificate validity period has a corresponding auto renewal period, when <a href="/ssl/reference/certificate-validity-periods/">attempts to renew</a> will start.</p>
<table>
<thead>
<tr>
<th>Certificate validity period</th>
<th>Auto renewal period</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 year</td>
<td>30 days</td>
<td>Limited to Enterprise customers using <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a> with <a href="/ssl/reference/certificate-authorities/#sslcom">SSL.com</a></td>
</tr>
<tr>
<td>3 months</td>
<td>30 days</td>
<td></td>
</tr>
<tr>
<td>1 month</td>
<td>7 days</td>
<td>Not supported by <a href="/ssl/reference/certificate-authorities/#lets-encrypt">Let's Encrypt</a></td>
</tr>
<tr>
<td>2 weeks</td>
<td>3 days</td>
<td>Not supported by <a href="/ssl/reference/certificate-authorities/#lets-encrypt">Let's Encrypt</a></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13968.md")
</aside>
<h3 id="custom-certificates">Custom certificates</h3>
<p>For information regarding custom certificates (managed by you), consider this other page on <a href="/ssl/edge-certificates/custom-certificates/renewing/">renewal and expiration</a>.</p>
<h3 id="ssl-for-saas">SSL for SaaS</h3>
<p>For SSL for SaaS certificates, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/">Renew certificates</a>.</p>
<h2 id="domain-control-validation-dcv">Domain control validation (DCV)</h2>
<p>Before a certificate authority (CA) will issue a certificate for a domain, the requester must prove they have control over that domain. This process is known as domain control validation (DCV).</p>
<p><a href="/ssl/edge-certificates/changing-dcv-method/methods/http/">HTTP validation</a> is attempted on renewals but will fall back to TXT validation depending on the certificate validity period:</p>
<ul>
<li>90-days certificates: after failing for 15 days</li>
<li>30-days certificates: after failing for 7 days</li>
<li>14-days certificates: after failing for 3 days</li>
</ul>
<h2 id="benefits-of-shorter-validity-periods">Benefits of shorter validity periods</h2>
<p>Cloudflare only issues certificates with validity periods of three months or less for two reasons.</p>
<p>First, shorter-lived certificates limit the damage from key compromise and mistaken issuance. Any compromised key material will be valid for a shorter period of time.</p>
<p>Second, shorter certificates encourage automation. The more frequently you have to do a task, the more likely you will want to automate it. Automation also means that you are less likely to let a certificate expire in production or give a person access to key material.</p>
<p>For more details on the benefits of shorter validity periods, refer to our <a href="https://blog.cloudflare.com/advanced-certificate-manager/">blog post introducing Advanced Certificate Manager</a>.</p>
