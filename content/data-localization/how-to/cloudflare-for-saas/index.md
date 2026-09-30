---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/how-to/cloudflare-for-saas/
  description: Configure Cloudflare for SaaS with Regional Services and Customer Metadata Boundary.
  full_title: Cloudflare for SaaS · Cloudflare Data Localization Suite docs
  head_html: <title>Cloudflare for SaaS · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Cloudflare for SaaS with Regional Services and Customer Metadata Boundary."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/how-to/cloudflare-for-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/how-to/cloudflare-for-saas/index.md"><meta property="og:title" content="Cloudflare for SaaS · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Cloudflare for SaaS with Regional Services and Customer Metadata Boundary."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/how-to/cloudflare-for-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Data Localization Suite,Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/how-to/cloudflare-for-saas/#page","headline":"Cloudflare for SaaS \u00b7 Cloudflare Data Localization Suite docs","description":"Configure Cloudflare for SaaS with Regional Services and Customer Metadata Boundary.","url":"https://developers.cloudflare.com/data-localization/how-to/cloudflare-for-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /data-localization/how-to/cloudflare-for-saas/
  schema: 1
---
<p>The following sections describe how to configure Cloudflare for SaaS with Regional Services and Customer Metadata Boundary to control where your custom hostnames are processed and where logs are stored.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for both hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare) through Cloudflare and the fallback origin, follow these steps for the dashboard or API configuration:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7448.md")
</div></div>
<p>The Regional Services functionality can be extended to Custom Hostnames and this is dependent on the target of the alias.</p>
<p>Consider the following example.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7445.md")
</aside>
<p>Below you can find a breakdown of the different ways that you might configure Cloudflare for SaaS and the corresponding processing regions:</p>
<ul>
<li>No processing region: <code>fallback.saasprovider.com</code></li>
<li>Processing region is the <code>US</code>: <code>us.saasprovider.com</code></li>
<li>User location: <code>UK</code> (closest datacenter: <code>LHR</code>)</li>
</ul>
<table>
<thead>
<tr>
<th>Test</th>
<th>Custom Hostname</th>
<th>Target</th>
<th>Origin</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>​​<code>regionalservices-default.example.com</code></td>
<td><code>fallback.saasprovider.com</code></td>
<td>default (fallback)</td>
<td><code>LHR</code></td>
</tr>
<tr>
<td>2</td>
<td><code>regionalservices-default2.example.com</code></td>
<td><code>us.saasprovider.com</code></td>
<td>default (fallback)</td>
<td><code>EWR</code></td>
</tr>
<tr>
<td>3</td>
<td><code>regionalservices-custom.example.com</code></td>
<td><code>fallback.saasprovider.com</code></td>
<td><code>us.saasprovider.com</code> (custom)</td>
<td><code>LHR</code></td>
</tr>
<tr>
<td>4</td>
<td><code>regionalservices-custom2.example.com</code></td>
<td><code>us.saasprovider.com</code></td>
<td><code>us.saasprovider.com</code> (custom)</td>
<td><code>EWR</code></td>
</tr>
</tbody>
</table>
<ul>
<li>
<p>In order to set a processing region for the fallback record to any of the available regions for Regional Services, create a new regional hostname entry for the fallback via a <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">POST</a> request.</p>
</li>
<li>
<p>To update the existing region (for example, from <code>EU</code> to <code>US</code>), make a <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">PATCH</a> request for the fallback to update the processing region accordingly.</p>
</li>
<li>
<p>To remove the regional services processing region and set it back to <code>Earth</code>, make a <a href="/data-localization/regional-services/regional-hostnames/#configure-regional-services-via-api">DELETE</a> request to delete the region configuration.</p>
</li>
</ul>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>Cloudflare for SaaS <a href="/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/">Analytics</a> based on <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests</a> are fully supported by Customer Metadata Boundary.</p>
<p>Refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS documentation</a> for more information.</p>
