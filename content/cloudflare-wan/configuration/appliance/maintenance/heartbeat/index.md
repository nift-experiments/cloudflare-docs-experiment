---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/heartbeat/
  description: Monitor Appliance heartbeat status.
  full_title: Heartbeat · Cloudflare WAN docs
  head_html: <title>Heartbeat · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor Appliance heartbeat status."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/heartbeat/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/heartbeat/index.md"><meta property="og:title" content="Heartbeat · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor Appliance heartbeat status."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/heartbeat/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/heartbeat/#page","headline":"Heartbeat \u00b7 Cloudflare WAN docs","description":"Monitor Appliance heartbeat status.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/maintenance/heartbeat/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/maintenance/heartbeat/
  schema: 1
---
<p>Cloudflare One Appliance (formerly Magic WAN Connector) communicates periodically with Cloudflare via HTTPS. This is also known as a heartbeat, and lets Cloudflare know that the Cloudflare One Appliance in question is connected to the Internet and reachable.</p>
<p>The heartbeat calls are made to <code>api.cloudflare.com</code>. Each Cloudflare One Appliance has a heartbeat frequency of 10 seconds, independently of the number of WAN interfaces you have running on your device.</p>
<p>There are three symbols for the heartbeat signal that allow you to quickly check the status of Cloudflare One Appliance:</p>
<ul>
<li><strong>Blue <code>i</code></strong>: Cloudflare One Appliance is contacting Cloudflare as expected.</li>
<li><strong>Yellow triangle</strong>: Cloudflare One Appliance has not yet connected to Cloudflare.</li>
<li><strong>Red triangle</strong>: There is a potential problem with Cloudflare One Appliance.</li>
</ul>
<h3 id="access-cloudflare-one-appliance-s-heartbeat">Access Cloudflare One Appliance's heartbeat</h3>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>.</li>
<li>From the list, find your Cloudflare One Appliance, and place your cursor over the icon on the <strong>Status</strong> column to check the timestamp. The timestamp displays the last time Cloudflare One Appliance successfully contacted Cloudflare.</li>
</ol>
