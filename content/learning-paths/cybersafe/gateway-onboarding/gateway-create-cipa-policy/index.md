---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/
  description: Learn about create cipa policy in this guide.
  full_title: Create CIPA policy · Cloudflare Learning Paths
  head_html: <title>Create CIPA policy · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about create cipa policy in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/index.md"><meta property="og:title" content="Create CIPA policy · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about create cipa policy in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Gateway,Email security (formerly Area 1),Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/#page","headline":"Create CIPA policy \u00b7 Cloudflare Learning Paths","description":"Learn about create cipa policy in this guide.","url":"https://developers.cloudflare.com/learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/cybersafe/gateway-onboarding/gateway-create-cipa-policy/
  schema: 1
---
<h2 id="create-cipa-policy">Create CIPA policy</h2>
<ol>
<li>Go to <strong>Traffic policies</strong> &gt; <strong>Firewall policies</strong>.</li>
<li>Create a policy to block using the CIPA filter:</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content Categories</td>
<td>in</td>
<td><em>CIPA Filter</em></td>
<td>Block</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>In <strong>Logs</strong> &gt; <strong>Gateway</strong> &gt; <strong>DNS</strong>, verify that you see the blocked domain.</li>
</ol>
<p>Your environment is now protected against all of the subcategories listed in <a href="/fundamentals/reference/policies-compliances/cybersafe/#configuration">Configuration</a>.</p>
