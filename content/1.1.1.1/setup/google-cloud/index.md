---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/
  description: Configure 1.1.1.1 on Google Cloud instances.
  full_title: Set up 1.1.1.1 on Google Cloud · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up 1.1.1.1 on Google Cloud · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure 1.1.1.1 on Google Cloud instances."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/index.md"><meta property="og:title" content="Set up 1.1.1.1 on Google Cloud · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure 1.1.1.1 on Google Cloud instances."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_tags" content="GCP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/#page","headline":"Set up 1.1.1.1 on Google Cloud \u00b7 Cloudflare 1.1.1.1 docs","description":"Configure 1.1.1.1 on Google Cloud instances.","url":"https://developers.cloudflare.com/1.1.1.1/setup/google-cloud/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["GCP"]}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/google-cloud/
  schema: 1
---
<p>Google Cloud lets you configure custom DNS servers at the Virtual Private Cloud (VPC) network level using <a href="https://cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-out">outbound server policies</a> in Cloud DNS. When you create an outbound server policy, all resources in that VPC network — including existing virtual machines — use the specified DNS servers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1802.md")
</aside>
<p>To configure 1.1.1.1 for your Google Cloud VPC network:</p>
<ol>
<li>Open the <a href="https://console.cloud.google.com">Google Cloud Console</a>.</li>
<li>Go to <strong>Network Services</strong> &gt; <strong>Cloud DNS</strong> and select <a href="https://console.cloud.google.com/net-services/dns/policies"><strong>DNS Server Policies</strong></a>.</li>
<li>Select <strong>Create Policy</strong>.</li>
<li>Enter a name for your policy (for example, <code>cloudflare-1-1-1-1</code>) and select the VPC networks to apply it to.</li>
<li>Under <strong>Alternate DNS servers</strong>, select <strong>Add Item</strong> and enter:</li>
</ol>
<pre tabindex="0"><code class="language-txt">1.1.1.1&#10;1.0.0.1&#10;</code></pre>
<ol start="6">
<li>Select <strong>Create</strong>.</li>
</ol>
<p>DNS requests within the configured VPC networks will now use 1.1.1.1.</p>
