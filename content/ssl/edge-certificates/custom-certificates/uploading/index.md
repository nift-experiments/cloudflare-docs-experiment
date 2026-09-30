---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/
  description: Upload, update, and delete custom certificates.
  full_title: Manage custom certificates · Cloudflare SSL/TLS docs
  head_html: <title>Manage custom certificates · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload, update, and delete custom certificates."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/index.md"><meta property="og:title" content="Manage custom certificates · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload, update, and delete custom certificates."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/#page","headline":"Manage custom certificates \u00b7 Cloudflare SSL/TLS docs","description":"Upload, update, and delete custom certificates.","url":"https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/custom-certificates/uploading/
  schema: 1
---
<p>This page lists Cloudflare requirements for custom certificates and explains how to upload and update these certificates using Cloudflare dashboard or API.</p>
<h2 id="certificate-requirements">Certificate requirements</h2>
<p>Before accepting custom certificates, Cloudflare parses them and checks for validity according to a list of requirements.</p>
<details class="nb-details"><summary>Full list of requirements</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14079.md")
</div></details>
<hr />
<h2 id="upload-a-custom-certificate">Upload a custom certificate</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14078.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14083.md")
</div></div>
<hr />
<h2 id="update-or-renew-an-existing-custom-certificate">Update or renew an existing custom certificate</h2>
<p>To renew a custom certificate that is approaching expiry, or to replace a certificate with updated key material, follow the steps below. <strong>This is the recommended renewal path</strong> — it does not consume an additional certificate quota slot and avoids downtime.</p>
<p>Before you update an existing custom certificate, you might want to consider having active <a href="/ssl/edge-certificates/universal-ssl/">universal</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced</a> certificates as fallback options. Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page to check a list of hostnames and status of the edge certificates in your zone.</p>
<p>If you are on an Enterprise plan and want to update a custom (modern) certificate, also consider requesting access to <a href="/ssl/edge-certificates/staging-environment/">Staging environment (Beta)</a>.</p>
<p>Replacing a custom certificate following these steps does not lead to any downtime. No connections will be terminated and new connections will use the new certificate. The old certificate will only actually be deleted when the new certificate is uploaded and active.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14086.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14073.md")
</aside>
<hr />
<h2 id="delete-a-custom-certificate">Delete a custom certificate</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Edge Certificates</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Edge Certificates</strong>, locate a custom certificate and select it to expand.</li>
<li>Select the cross button.</li>
<li>Select <strong>Confirm</strong> to delete the certificate.</li>
</ol>
