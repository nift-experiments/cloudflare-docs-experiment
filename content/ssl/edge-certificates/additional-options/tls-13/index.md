---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/
  description: Enable TLS 1.3 for improved performance and security.
  full_title: TLS 1.3 · Cloudflare SSL/TLS docs
  head_html: <title>TLS 1.3 · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable TLS 1.3 for improved performance and security."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/index.md"><meta property="og:title" content="TLS 1.3 · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable TLS 1.3 for improved performance and security."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/#page","headline":"TLS 1.3 \u00b7 Cloudflare SSL/TLS docs","description":"Enable TLS 1.3 for improved performance and security.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/tls-13/
  schema: 1
---
<p>TLS 1.3 enables the latest version of the TLS protocol (when supported) for improved security and performance.</p>
<h2 id="what-is-tls-1-3">What is TLS 1.3?</h2>
<p>TLS 1.3 is the newest, fastest, and most secure version of the <a href="/ssl/reference/protocols/">TLS protocol</a>.</p>
<p>By turning on the TLS 1.3 feature, traffic to and from your website will be served over the TLS 1.3 protocol when supported by clients. TLS 1.3 protocol has improved latency over older versions, has several new features, and is currently supported in all updated major browsers.</p>
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
</tbody>
</table>
<h2 id="enable-tls-1-3">Enable TLS 1.3</h2>
<p>TLS 1.3 can be activated in the Cloudflare dashboard or through the API:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14125.md")
</div></div>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>Since TLS 1.3 implementations are relatively new, some failures may occur. If you experience errors, submit a Cloudflare Support ticket with the following information:</p>
<ul>
<li>Steps to replicate the issue (if possible)</li>
<li>Client build version</li>
<li>Client diagnostic information</li>
<li>Packet captures</li>
</ul>
<p>Chrome users should submit a <a href="https://dev.chromium.org/for-testers/providing-network-details">net-internals trace</a> to Google. Firefox users should <a href="https://bugzilla.mozilla.org/home">report bugs to Mozilla</a>.</p>
<h2 id="limitations">Limitations</h2>
<div class="nb-data-component" data-cf-component="Render"></div>
