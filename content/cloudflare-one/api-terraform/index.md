---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/api-terraform/
  description: How API and Terraform works in Cloudflare One.
  full_title: API and Terraform · Cloudflare One docs
  head_html: <title>API and Terraform · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How API and Terraform works in Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/api-terraform/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/api-terraform/index.md"><meta property="og:title" content="API and Terraform · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How API and Terraform works in Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/api-terraform/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Terraform,REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/api-terraform/#page","headline":"API and Terraform \u00b7 Cloudflare One docs","description":"How API and Terraform works in Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/api-terraform/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Terraform","REST API"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/api-terraform/
  schema: 1
---
<p>You can manage your Cloudflare Zero Trust configuration using the API or Terraform. For more information, refer to the following links:</p>
<ul>
<li><a href="/api/">API reference</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider reference</a></li>
<li><a href="/terraform/">Terraform how-to documentation</a></li>
</ul>
<p>Detailed API and Terraform examples for Cloudflare Zero Trust are available in our <a href="/cloudflare-one/implementation-guides/">implementation guides</a> and throughout the Cloudflare Zero Trust documentation.</p>
<h2 id="set-dashboard-to-read-only">Set dashboard to read-only</h2>
<p>Super Administrators can lock all settings as read-only in the Cloudflare One dashboard. Read-only mode ensures that all updates for the account are made through the API or Terraform.</p>
<p>To enable read-only mode:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Settings</strong> &gt; <strong>Admin controls</strong>.</li>
<li>Enable <strong>Set dashboard to read-only</strong>.</li>
</ol>
<p>All users, regardless of <a href="/cloudflare-one/roles-permissions/">user permissions</a>, will be prevented from making configuration changes through the UI.</p>
<h2 id="scoped-api-tokens">Scoped API tokens</h2>
<p>The administrators managing policies and groups in Cloudflare Zero Trust might be different from those responsible for configuring WAF custom rules or other Cloudflare settings. You can configure scoped API tokens so that team members and automated systems can manage Cloudflare Zero Trust settings without having permission to modify other configurations in Cloudflare.</p>
<p>You can create a scoped API token <a href="/fundamentals/api/get-started/create-token/">via the dashboard</a> or <a href="/fundamentals/api/how-to/create-via-api/">via the API</a>. For a list of available token permissions, refer to <a href="/fundamentals/api/reference/permissions/">API token permissions</a>.</p>
