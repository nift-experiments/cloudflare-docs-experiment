---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/
  description: Enable user roles for Network Firewall management.
  full_title: Enable user roles · Cloudflare Network Firewall docs
  head_html: <title>Enable user roles · Cloudflare Network Firewall docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable user roles for Network Firewall management."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/index.md"><meta property="og:title" content="Enable user roles · Cloudflare Network Firewall docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable user roles for Network Firewall management."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Network Firewall"><meta name="algolia_product_filter" content="Cloudflare Network Firewall"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Network Firewall"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/#page","headline":"Enable user roles \u00b7 Cloudflare Network Firewall docs","description":"Enable user roles for Network Firewall management.","url":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/enable-roles/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-network-firewall/how-to/enable-roles/
  schema: 1
---
<p>You can determine which users have, or do not have, configuration edit access for Magic products, including Magic Transit, Cloudflare WAN (formerly Magic WAN), and Cloudflare Network Firewall.</p>
<p>For example, if multiple teams manage different Cloudflare products on the same account, you can provide select users with edit access and other users with read-only access.</p>
<h2 id="assign-permissions">Assign permissions</h2>
<ol>
<li>Go to the <strong>Members</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Members</strong>, enter an existing user's name and select <strong>Search</strong>.</li>
<li>Expand the menu at the end of the user row.</li>
<li>From the list, locate <strong>Network Services (Magic)</strong>.</li>
<li>Select one of two options:
<ul>
<li><strong>Network Services (Magic)</strong> - Enables users to view and edit Magic configurations.</li>
<li><strong>Network Services (Magic, Read-Only)</strong> - Enables users to view but not modify Magic configurations.</li>
</ul>
</li>
</ol>
