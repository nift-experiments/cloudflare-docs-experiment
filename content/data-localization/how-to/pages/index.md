---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/how-to/pages/
  description: Configure Pages with Regional Services and Customer Metadata Boundary.
  full_title: Pages · Cloudflare Data Localization Suite docs
  head_html: <title>Pages · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Pages with Regional Services and Customer Metadata Boundary."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/how-to/pages/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/how-to/pages/index.md"><meta property="og:title" content="Pages · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Pages with Regional Services and Customer Metadata Boundary."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/how-to/pages/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Data Localization Suite,Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/how-to/pages/#page","headline":"Pages \u00b7 Cloudflare Data Localization Suite docs","description":"Configure Pages with Regional Services and Customer Metadata Boundary.","url":"https://developers.cloudflare.com/data-localization/how-to/pages/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /data-localization/how-to/pages/
  schema: 1
---
<p>The following sections describe how to configure Cloudflare Pages with Regional Services and Customer Metadata Boundary to control where your Pages project is processed and where logs are stored.</p>
<h2 id="regional-services">Regional Services</h2>
<p>To configure Regional Services for hostnames <a href="/dns/proxy-status/">proxied</a> (meaning traffic routes through Cloudflare) through Cloudflare and ensure that processing of a Pages project occurs only in-region, follow these steps for the dashboard or API configuration:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7441.md")
</div></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7438.md")
</aside>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>Customer Metadata Boundary applies to the Custom Domain configured, as well as the <a href="/pages/configuration/preview-deployments/">*.pages.dev</a> subdomain. You also have the option to disable access to the <a href="/pages/configuration/custom-domains/#disable-access-to-pagesdev-subdomain"><code>.dev</code> domain</a>.</p>
<p>For information on available Analytics and Metrics, review the <a href="/data-localization/compatibility/">Cloudflare product compatibility</a> page.</p>
<p>It is recommended not to store any Personally Identifiable Information (PII) in the Pages project's static assets.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7437.md")
</aside>
<p>Refer to the <a href="/pages">Pages documentation</a> for more information.</p>
