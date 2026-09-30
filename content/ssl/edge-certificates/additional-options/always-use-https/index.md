---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/
  description: Redirect all HTTP requests to HTTPS for your domain.
  full_title: Always Use HTTPS · Cloudflare SSL/TLS docs
  head_html: <title>Always Use HTTPS · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Redirect all HTTP requests to HTTPS for your domain."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/index.md"><meta property="og:title" content="Always Use HTTPS · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Redirect all HTTP requests to HTTPS for your domain."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="Redirects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/#page","headline":"Always Use HTTPS \u00b7 Cloudflare SSL/TLS docs","description":"Redirect all HTTP requests to HTTPS for your domain.","url":"https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/additional-options/always-use-https/
  schema: 1
---
<p>Always Use HTTPS redirects all your visitor requests from <code>http</code> to <code>https</code>, for all subdomains and hosts in your application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14152.md")
</aside>
<p>Cloudflare recommends not performing redirects at your origin web server, as this can cause <a href="/ssl/troubleshooting/too-many-redirects/">redirect loop errors</a>.</p>
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
<h2 id="encrypt-all-visitor-traffic">Encrypt all visitor traffic</h2>
<p>To redirect traffic for all subdomains and hosts in your application, you can enable <strong>Always Use HTTPS</strong>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14151.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14155.md")
</div></div>
<h2 id="limitations">Limitations</h2>
<p>Forcing HTTPS does not resolve issues with <a href="/ssl/troubleshooting/mixed-content-errors/">mixed content</a>, as browsers check the protocol of included resources before making a request. You will need to use only relative links or HTTPS links on pages that you force to HTTPS. Cloudflare can automatically resolve some mixed-content links using our <a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a> functionality.</p>
