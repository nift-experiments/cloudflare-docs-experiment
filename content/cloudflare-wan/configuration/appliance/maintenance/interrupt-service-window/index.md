---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/
  description: Learn how to set up when Cloudflare One Appliance can update its systems.
  full_title: Interrupt window · Cloudflare WAN docs
  head_html: <title>Interrupt window · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up when Cloudflare One Appliance can update its systems."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/index.md"><meta property="og:title" content="Interrupt window · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up when Cloudflare One Appliance can update its systems."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/#page","headline":"Interrupt window \u00b7 Cloudflare WAN docs","description":"Learn how to set up when Cloudflare One Appliance can update its systems.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/
  schema: 1
---
<p>The Interrupt window defines when Cloudflare One Appliance (formerly Magic WAN Connector) can update its systems. When Cloudflare One Appliance is updating, this may result in an interruption to existing connections. Set up a time window that minimizes disruption to your sites.</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>.</li>
<li>Find the Cloudflare One Appliance you want to set up the update window for &gt; <strong>Edit</strong>.</li>
<li>In <strong>Interrupt window</strong>, select the most appropriate time for the Cloudflare One Appliance to update its systems:
<ul>
<li><strong>Timezone</strong>: Select the time zone for the Cloudflare One Appliance to update.</li>
<li><strong>Start time</strong>: Choose an hour for the Cloudflare One Appliance to start updating. Cloudflare recommends you choose an hour when there is minimal activity in your network, to avoid potential disruptions.</li>
<li><strong>Duration</strong>: Duration indicates the time window during which the Cloudflare One Appliance is scheduled to update. For example, if you configure your Cloudflare One Appliance to update at <code>22:00</code> and specify a <strong>Duration</strong> of <code>4 hours</code>, the Cloudflare One Appliance will attempt to update within the four-hour period following <code>22:00</code>.</li>
</ul>
</li>
</ol>
