---
cp9:
  canonical: https://developers.cloudflare.com/support/third-party-software/others/reduce-data-transfer-egress-costs-between-azure-and-cloudflare/
  description: Lower Azure egress costs using Microsoft Routing Preference.
  full_title: Reduce data transfer (egress costs) between Azure and Cloudflare · Cloudflare Support docs
  head_html: <title>Reduce data transfer (egress costs) between Azure and Cloudflare · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Lower Azure egress costs using Microsoft Routing Preference."><link rel="canonical" href="https://developers.cloudflare.com/support/third-party-software/others/reduce-data-transfer-egress-costs-between-azure-and-cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/third-party-software/others/reduce-data-transfer-egress-costs-between-azure-and-cloudflare/index.md"><meta property="og:title" content="Reduce data transfer (egress costs) between Azure and Cloudflare · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Lower Azure egress costs using Microsoft Routing Preference."><meta property="og:url" content="https://developers.cloudflare.com/support/third-party-software/others/reduce-data-transfer-egress-costs-between-azure-and-cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/third-party-software/others/reduce-data-transfer-egress-costs-between-azure-and-cloudflare/#page","headline":"Reduce data transfer (egress costs) between Azure and Cloudflare \u00b7 Cloudflare Support docs","description":"Lower Azure egress costs using Microsoft Routing Preference.","url":"https://developers.cloudflare.com/support/third-party-software/others/reduce-data-transfer-egress-costs-between-azure-and-cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/third-party-software/others/reduce-data-transfer-egress-costs-between-azure-and-cloudflare/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>Cloudflare launched Bandwidth Alliance in 2018 – a group of forward-looking cloud and storage providers who have agreed to waive or steeply discount egress costs for mutual customers. </p>
<p>Cloudflare customers using Azure can lower their egress bills between Cloudflare and Azure via <a href="https://docs.microsoft.com/en-us/azure/virtual-network/routing-preference-overview">Microsoft Routing Preference</a>.</p>
<hr />
<h2 id="how-to">How to</h2>
<p>To lower your data transfer costs from Azure and Cloudflare: </p>
<ol>
<li>In the Azure portal, go to your storage account. </li>
<li>Navigate to <strong>Network Routing &gt; Firewalls and virtual networks</strong>.</li>
<li>For <strong>Routing preference</strong>, choose <strong>Internet routing</strong>.</li>
<li>Publish route-specific endpoint to <strong>Internet routing</strong>.</li>
<li>Navigate to <strong>Properties</strong>.</li>
<li>Locate the endpoint values for <strong>Internet Routing</strong>.</li>
<li>Enter these endpoint values in your Cloudflare Dashboard.</li>
</ol>
<p><img src="/assets/upstream/images/support/bandwidth-alliance.png" alt="Example of where to enter endpoint URLs from Microsoft Azure into your Cloudflare dashboard." /></p>
<p>For additional details, refer to <a href="https://docs.microsoft.com/en-us/azure/storage/common/configure-network-routing-preference?tabs=azure-portal">Configure network routing preference for Azure Storage</a> and <a href="https://docs.microsoft.com/en-us/azure/storage/common/network-routing-preference">Microsoft Routing Preference</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/discounted-egress-for-cloudflare-customers-from-microsoft-azure-is-now-available/">Microsoft Azure data transfer announcement</a> (blog)</li>
<li><a href="https://www.cloudflare.com/bandwidth-alliance/">Bandwidth Alliance</a></li>
</ul>
