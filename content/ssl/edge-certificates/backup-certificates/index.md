---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/
  description: How Cloudflare issues backup certificates for redundancy.
  full_title: Backup certificates · Cloudflare SSL/TLS docs
  head_html: <title>Backup certificates · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="How Cloudflare issues backup certificates for redundancy."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/index.md"><meta property="og:title" content="Backup certificates · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Cloudflare issues backup certificates for redundancy."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/#page","headline":"Backup certificates \u00b7 Cloudflare SSL/TLS docs","description":"How Cloudflare issues backup certificates for redundancy.","url":"https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/backup-certificates/
  schema: 1
---
<p>If Cloudflare is providing <a href="/dns/zone-setups/full-setup/">authoritative DNS</a> for your domain, Cloudflare will issue a backup <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificate</a> for every standard Universal certificate issued.</p>
<p>Backup certificates are wrapped with a different private key and issued from a different Certificate Authority — either Google Trust Services, Let's Encrypt, Sectigo, or SSL.com — than your domain's primary Universal SSL certificate.</p>
<p>These backup certificates are not normally deployed, but they will be deployed automatically by Cloudflare in the event of a certificate revocation or key compromise.</p>
<p>For additional details, refer to the <a href="https://blog.cloudflare.com/introducing-backup-certificates/">introductory blog post</a>.</p>
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
<tr>
<td>Can opt out?</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="opt-out">Opt out</h2>
<p>Enterprise customers can request to opt out of backup certificates by opening a support case. Opting out removes the backup-certificate redundancy for your domain.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="backup-certificate-deleted-after-turning-universal-ssl-back-on">Backup certificate deleted after turning Universal SSL back on</h3>
<p>After you turn off and quickly turn Universal SSL back on, your domain may end up without a backup certificate.</p>
<p>When Universal SSL is toggled off and on in quick succession, certificate processing jobs are not guaranteed to run in the order they were submitted. This race condition can cause a newly issued backup certificate to be deleted before it becomes active.</p>
<p>To recover your backup certificate:</p>
<ol>
<li>Turn Universal SSL off again.</li>
<li>Wait several minutes.</li>
<li>Turn Universal SSL back on, then allow time for Cloudflare to issue a new backup certificate.</li>
</ol>
<p>If you need uninterrupted certificate coverage, consider ordering an <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate Manager</a> certificate before toggling Universal SSL.</p>
<p>For more troubleshooting help, refer to <a href="/ssl/troubleshooting/">Troubleshooting SSL errors</a>.</p>
