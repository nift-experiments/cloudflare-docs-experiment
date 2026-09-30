---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/
  description: Partner domain TLS in Email Security.
  full_title: Partner domain TLS · Cloudflare One docs
  head_html: <title>Partner domain TLS · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Partner domain TLS in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/index.md"><meta property="og:title" content="Partner domain TLS · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Partner domain TLS in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/#page","headline":"Partner domain TLS \u00b7 Cloudflare One docs","description":"Partner domain TLS in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/pre-delivery-deployment/partner-domain-tls/
  schema: 1
---
<p>To add additional TLS (Transport Layer Security) requirements for emails coming from certain domains, you can enforce higher levels of SSL/TLS inspection. If TLS is required, mail without TLS from the specified domain will be dropped.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4943.md")
</aside>
<p>To set up a partner domain:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and select <strong>Email security</strong>.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Partner domain TLS</strong> &gt; <strong>View</strong>.</li>
<li>Select <strong>Add a domain</strong>.</li>
<li>Enter a valid domain name. You can also exclude subdomains by selecting <strong>Add exclude</strong>.</li>
<li>(Optional) Add an optional note to describe your rule(s).</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To edit a partner domain, select the three dots &gt; <strong>Edit</strong>.</p>
<p>To delete a partner domain, select the three dots &gt; <strong>Delete</strong>.</p>
