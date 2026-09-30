---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/
  description: How API deployment works in Email Security.
  full_title: API deployment · Cloudflare One docs
  head_html: <title>API deployment · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How API deployment works in Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/index.md"><meta property="og:title" content="API deployment · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How API deployment works in Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/#page","headline":"API deployment \u00b7 Cloudflare One docs","description":"How API deployment works in Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/post-delivery-deployment/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/post-delivery-deployment/api/
  schema: 1
---
<p>When you choose an API deployment, email messages only reach Email security after they have already reached a user's inbox.</p>
<p>Then, through an integration with your email provider, Email security can <a href="/cloudflare-one/email-security/settings/auto-moves/">auto-move messages</a> based on your organization's policies.</p>
<p><img src="/assets/upstream/email-security/M365_API_Deployment_Graph.png" alt="With API deployment, messages travel through Email security's email filter after reaching your users." /></p>
<h2 id="benefits">Benefits</h2>
<p>When you choose API deployment, you get the following benefits:</p>
<ul>
<li>Easy protection for complex email architectures, without requiring any change to mailflow operations.</li>
<li>Agentless deployment for Microsoft 365.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>However, API deployment also has the following disadvantages:</p>
<ul>
<li>Email security is dependent on Microsoft's Graph API, and outages will increase the message dwell time in the inbox.</li>
<li>Your email provider may throttle API requests from Email security.</li>
<li>Email security requires read and write access to mailboxes.</li>
<li>Requires API support from your email provider (does not typically support on-premise providers).</li>
<li>Detection rates may be lower if multiple solutions exist.</li>
<li>Messages cannot be modified or quarantined.</li>
</ul>
