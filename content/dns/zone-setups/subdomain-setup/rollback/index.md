---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/
  description: Roll back a subdomain zone setup.
  full_title: Rollback subdomain setup · Cloudflare DNS docs
  head_html: <title>Rollback subdomain setup · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Roll back a subdomain zone setup."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/index.md"><meta property="og:title" content="Rollback subdomain setup · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Roll back a subdomain zone setup."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/#page","headline":"Rollback subdomain setup \u00b7 Cloudflare DNS docs","description":"Roll back a subdomain zone setup.","url":"https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/subdomain-setup/rollback/
  schema: 1
---
<p>Refer to the following process to understand how you can rollback a <a href="/dns/zone-setups/subdomain-setup/">subdomain setup</a> and recreate the corresponding subdomain DNS records in an existing parent zone within Cloudflare.</p>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>This guide assumes both your child domain (<code>blog.example.com</code>) and its parent domain (<code>example.com</code>) are in Cloudflare.</li>
<li>In the child zone, review and <a href="/dns/manage-dns-records/how-to/import-and-export/#export-records">export</a> the DNS records.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/7902.md")
</aside>
<h2 id="steps">Steps</h2>
<ol>
<li>(Optional) In the parent zone, migrate over any settings - <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/">Rules</a>, <a href="/workers/">Workers</a>, and more - that might be needed for the child domain.</li>
<li>(Optional) If necessary, <a href="/ssl/edge-certificates/advanced-certificate-manager/">order an advanced SSL certificate</a> that covers the child domain and any deeper subdomains.</li>
<li>In the parent zone, go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page.</li>
<li>Delete one of the <code>NS</code> records defined for the child domain.</li>
<li>Edit the remaining <code>NS</code> record to create the subdomain address record.</li>
<li><a href="/dns/manage-dns-records/how-to/import-and-export/#import-records">Import</a> the records you had obtained <a href="#before-you-begin">before you began</a>.</li>
</ol>
