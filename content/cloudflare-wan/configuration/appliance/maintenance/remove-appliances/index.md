---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/
  description: Remove Appliances from your account.
  full_title: Remove appliances · Cloudflare WAN docs
  head_html: <title>Remove appliances · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Remove Appliances from your account."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/index.md"><meta property="og:title" content="Remove appliances · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Remove Appliances from your account."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/#page","headline":"Remove appliances \u00b7 Cloudflare WAN docs","description":"Remove Appliances from your account.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/remove-appliances/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/maintenance/remove-appliances/
  schema: 1
---
<p>When adding or removing Cloudflare One Appliances (formerly Magic WAN Connectors), you need to be aware of the difference between the physical device and its profile.</p>
<ul>
<li>The physical device is the hardware at your site.</li>
<li>The profile contains the configuration that allows the device to connect to Cloudflare, including your WANs, LANs, traffic steering, and LAN policies.</li>
</ul>
<p>You can have more than one Cloudflare One Appliance in one profile if you initially enabled high availability during the configuration of the profile. If you did not enable high availability, you need to delete the profile associated with a site before adding a new Cloudflare One Appliance.</p>
<h2 id="remove-a-profile">Remove a profile</h2>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Appliances</strong> &gt; <strong>Profiles</strong>.</li>
<li>Find the profile that you want to edit &gt; select the three dots next to it &gt; <strong>Delete</strong>.</li>
</ol>
<h2 id="remove-a-physical-device">Remove a physical device</h2>
<p>To remove a Cloudflare One Appliance from your account:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>.</li>
<li>Find the Cloudflare One Appliance that you want to delete &gt; select the three dots next to it &gt; <strong>Delete</strong>.</li>
</ol>
