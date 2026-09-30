---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/
  description: Learn how renewal and expiration work when using Cloudflare Custom SSL certificates.
  full_title: Renewal and expiration · Cloudflare SSL/TLS docs
  head_html: <title>Renewal and expiration · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how renewal and expiration work when using Cloudflare Custom SSL certificates."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/index.md"><meta property="og:title" content="Renewal and expiration · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how renewal and expiration work when using Cloudflare Custom SSL certificates."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/#page","headline":"Renewal and expiration \u00b7 Cloudflare SSL/TLS docs","description":"Learn how renewal and expiration work when using Cloudflare Custom SSL certificates.","url":"https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/custom-certificates/renewing/
  schema: 1
---
<h2 id="renew-custom-certificates">Renew custom certificates</h2>
<p>Since Cloudflare cannot renew uploaded certificates, you should ensure that you replace or <a href="/ssl/edge-certificates/custom-certificates/uploading/#update-or-renew-an-existing-custom-certificate">update</a> an expiring custom certificate before it expires, otherwise your visitors may not be able to connect.</p>
<p>Cloudflare automatically sends email notifications 30 and 14 days before your custom certificate expires. The email is sent to users who have the SSL/TLS, Administrator, or Super Administrator <a href="/fundamentals/manage-members/roles/">roles</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14089.md")
</aside>
<h2 id="expired-certificates">Expired certificates</h2>
<p>If a valid replacement - covering some or all of the <span class="nb-glossary-tooltip" title="Subject Alternative Names (SANs)">SANs</span> in the expiring custom certificate - is already available, Cloudflare will remove the expiring custom certificate in the 24 hours before expiration. There is no expected downtime due to certificate transition.</p>
<p>If no valid replacement is available, Cloudflare will remove the custom certificate after it expires.</p>
<p>Affected domains and subdomains will fall back to any other active certificate covering the hostnames on the expiring certificate.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14088.md")
</aside>
<h2 id="migrate-to-other-certificate-types">Migrate to other certificate types</h2>
<p>If you no longer want to use your custom certificate but still want your website or application to be covered with SSL/TLS, you can do the following:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Edge Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Make sure there is already an active <a href="/ssl/edge-certificates/universal-ssl/">universal</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced</a> certificate covering the same hostnames.</li>
<li>Delete your custom certificate.</li>
</ol>
