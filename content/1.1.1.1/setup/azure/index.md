---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/azure/
  description: Configure 1.1.1.1 on Microsoft Azure virtual networks.
  full_title: Set up 1.1.1.1 on Azure · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up 1.1.1.1 on Azure · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure 1.1.1.1 on Microsoft Azure virtual networks."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/azure/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/azure/index.md"><meta property="og:title" content="Set up 1.1.1.1 on Azure · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure 1.1.1.1 on Microsoft Azure virtual networks."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/azure/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_tags" content="Azure"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/azure/#page","headline":"Set up 1.1.1.1 on Azure \u00b7 Cloudflare 1.1.1.1 docs","description":"Configure 1.1.1.1 on Microsoft Azure virtual networks.","url":"https://developers.cloudflare.com/1.1.1.1/setup/azure/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Azure"]}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/azure/
  schema: 1
---
<p>These steps configure 1.1.1.1 as the DNS resolver for an Azure Virtual Network (VNet). This applies to all resources in the VNet, including virtual machines.</p>
<ol>
<li>Log in to your Azure portal.</li>
<li>From the Azure portal side menu, select <strong>Virtual Networks</strong>.</li>
<li>Select the virtual network you want to configure.</li>
<li>Select <strong>DNS Servers</strong> &gt; <strong>Custom</strong>, and add two entries:</li>
</ol>
<pre tabindex="0"><code class="language-txt">1.1.1.1&#10;1.0.0.1&#10;</code></pre>
<ol start="5">
<li>Select <strong>Save</strong>.</li>
</ol>
