---
cp9:
  canonical: https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/
  description: Learn how to bulk delete DNS records in Cloudflare with a script so you can start from zero instead of using the quick scan results.
  full_title: Delete all DNS records · Cloudflare DNS docs
  head_html: <title>Delete all DNS records · Cloudflare DNS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to bulk delete DNS records in Cloudflare with a script so you can start from zero instead of using the quick scan results."><link rel="canonical" href="https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/index.md"><meta property="og:title" content="Delete all DNS records · Cloudflare DNS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to bulk delete DNS records in Cloudflare with a script so you can start from zero instead of using the quick scan results."><meta property="og:url" content="https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DNS"><meta name="algolia_product_filter" content="DNS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/#page","headline":"Delete all DNS records \u00b7 Cloudflare DNS docs","description":"Learn how to bulk delete DNS records in Cloudflare with a script so you can start from zero instead of using the quick scan results.","url":"https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /dns/zone-setups/troubleshooting/delete-all-records/
  schema: 1
---
<p>When you connect your domain to Cloudflare, the <a href="/dns/zone-setups/reference/dns-quick-scan/">DNS records quick scan</a> may automatically add several records to your zone.</p>
<p>If you realize most of them are not applicable and want to bulk delete DNS records, follow the steps below. This method assumes you are familiar with <a href="/fundamentals/api/">API calls fundamentals</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bulk-deletion-available-in-the-dashboard">Bulk deletion available in the dashboard</h3>
@markup("md", "content/.markup/bodies/7900.md")
</aside>
<ol>
<li>Make sure you have <a href="/fundamentals/api/get-started/create-token/">an API token</a> that allows you to edit DNS for your zone.</li>
<li>Get your <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a>.</li>
<li>Run the following script, replacing <code>&lt;ZONE_ID&gt;</code> and <code>&lt;API_TOKEN&gt;</code> with the values you got from the previous steps.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/7901.md")
</div>
