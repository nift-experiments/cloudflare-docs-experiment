---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/
  description: Regionalize proxied hostnames by assigning a region through the dashboard or Regional Hostnames API.
  full_title: Regional Hostnames · Cloudflare Data Localization Suite docs
  head_html: <title>Regional Hostnames · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Regionalize proxied hostnames by assigning a region through the dashboard or Regional Hostnames API."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/index.md"><meta property="og:title" content="Regional Hostnames · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Regionalize proxied hostnames by assigning a region through the dashboard or Regional Hostnames API."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Data Localization Suite"><meta name="pcx_tags" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/#page","headline":"Regional Hostnames \u00b7 Cloudflare Data Localization Suite docs","description":"Regionalize proxied hostnames by assigning a region through the dashboard or Regional Hostnames API.","url":"https://developers.cloudflare.com/data-localization/regional-services/regional-hostnames/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Terraform"]}</script>
  markdown: true
  noindex: false
  route: /data-localization/regional-services/regional-hostnames/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7414.md")
</aside>
<p>Regional Hostnames are the most common way to use <a href="/data-localization/regional-services/">Regional Services</a>: you assign a region to a proxied hostname, and Cloudflare steers traffic for that hostname — using its shared anycast IP addresses — to in-region data centers for TLS termination and processing. For other ways to regionalize traffic, refer to <a href="/data-localization/regional-services/#ways-to-use-regional-services">Ways to use Regional Services</a>.</p>
<p>Regional Hostnames support <a href="/data-localization/region-support/#region-types">managed regions</a>. If you need a custom region, use <a href="/data-localization/regional-services/spectrum-applications/">Regionalized Spectrum Applications</a> or <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a> instead.</p>
<p>You can configure Regional Hostnames through the dashboard or via API.</p>
<h2 id="configure-regional-services-in-the-dashboard">Configure Regional Services in the dashboard</h2>
<p>To use Regional Services, you need to first create a DNS record in the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Records</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Follow these steps to <a href="/dns/manage-dns-records/how-to/create-dns-records/">create a DNS record</a>.</li>
<li>From the <strong>Region</strong> dropdown, select the region you would like to use on your domain. This value will be applied to all DNS records on the same hostname. This means that if you have two DNS records of the same hostname and change the region for one of them, both records will have the same region.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7413.md")
</aside>
<p>Refer to the table on <a href="/data-localization/region-support/">Available regions and product support</a> for the complete list of available regions, their definitions and product support</p>
<h2 id="configure-regional-services-via-api">Configure Regional Services via API</h2>
<p>You can also use Regional Services via API.</p>
<p>Users with the Super Administrator, Administrator, or Domain Administrator roles can edit Regional Services configurations. The Domain Administrator Read Only role does not currently include read access to Regional Services configurations. Use the <strong>DNS: Read/Write</strong> API permission for the <code>/addressing/</code> endpoints to read or write Regional Services configurations.</p>
<p>These are some examples of API requests.</p>
<details class="nb-details"><summary>List all the available regions</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7415.md")
</div></details>
<details class="nb-details"><summary>Create a new regional hostname entry</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7416.md")
</div></details>
<details class="nb-details"><summary>List all regional hostnames for a zone or get a specific one</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7417.md")
</div></details>
<details class="nb-details"><summary>List all regional hostnames for a specific zone</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7418.md")
</div></details>
<details class="nb-details"><summary>Patch the region for a specific hostname</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7419.md")
</div></details>
<details class="nb-details"><summary>Delete the region configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7420.md")
</div></details>
<h2 id="verify-regional-map-for-zero-trust">Verify regional map for Zero Trust</h2>
<p>To verify that your regional map is being applied correctly, check the <code>IngressColoName</code> field in your <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#ingresscoloname">Zero Trust Network Session logs</a>. This field shows the name of the Cloudflare data center where traffic ingressed. Since regionalization is applied upstream from Gateway, the ingress data center will be located within your configured regional map, confirming that traffic is being processed in the correct region.</p>
<h2 id="terraform-support">Terraform support</h2>
<p>You can also configure Regional Services using Terraform. For more details, refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/regional_hostname"><code>cloudflare_regional_hostname</code> resource</a> in the Terraform documentation.</p>
