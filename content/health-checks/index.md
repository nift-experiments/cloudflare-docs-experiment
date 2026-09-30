---
cp9:
  canonical: https://developers.cloudflare.com/health-checks/
  description: Monitor origin server availability and get notified of status changes.
  full_title: Health Checks · Cloudflare Health Checks docs
  head_html: <title>Health Checks · Cloudflare Health Checks docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor origin server availability and get notified of status changes."><link rel="canonical" href="https://developers.cloudflare.com/health-checks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/health-checks/index.md"><meta property="og:title" content="Health Checks · Cloudflare Health Checks docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor origin server availability and get notified of status changes."><meta property="og:url" content="https://developers.cloudflare.com/health-checks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Health Checks"><meta name="algolia_product_filter" content="Health Checks"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Health Checks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/health-checks/#page","headline":"Health Checks \u00b7 Cloudflare Health Checks docs","description":"Monitor origin server availability and get notified of status changes.","url":"https://developers.cloudflare.com/health-checks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /health-checks/
  schema: 1
---
<hr />
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield">Smart Shield</h3>
@markup("md", "content/.markup/bodies/988.md")
</aside>
<p>Standalone Health Checks monitors an IP address or hostname for origin servers or applications and notifies you in near real-time if there happens to be a problem.</p>
<p>A health check is a service that runs on Cloudflare's edge network to monitor whether an origin server is online. This allows you to view the health of your origin servers even if there is only one origin or you do not yet need to balance traffic across your infrastructure.</p>
<p>Health Checks support various configurations to hone in on what you can check, including response codes, protocol types, and intervals. You can specify a particular path if an origin server serves multiple applications or check a larger subset of response codes for your staging environment. All of these options allow you to properly target your Health Check, providing a precise picture of what is wrong with an origin server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/987.md")
</aside>
<hr />
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/989.md")
</div>
<hr />
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/991.md")
</div>
<hr />
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
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Number of checks</td>
<td>0</td>
<td>10</td>
<td>50</td>
<td>1,000</td>
</tr>
<tr>
<td>Analytics</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<hr />
