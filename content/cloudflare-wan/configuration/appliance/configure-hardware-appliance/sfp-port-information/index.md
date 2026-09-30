---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/
  description: SFP+ port specifications for the hardware Appliance.
  full_title: SFP+ port information · Cloudflare WAN docs
  head_html: <title>SFP+ port information · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="SFP+ port specifications for the hardware Appliance."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/index.md"><meta property="og:title" content="SFP+ port information · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="SFP+ port specifications for the hardware Appliance."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/#page","headline":"SFP+ port information \u00b7 Cloudflare WAN docs","description":"SFP+ port specifications for the hardware Appliance.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/
  schema: 1
---
<p>The hardware version of Cloudflare One Appliance (formerly Magic WAN Connector) includes two <a href="https://en.wikipedia.org/wiki/Small_Form-factor_Pluggable">SFP+ ports</a> that support 10G throughput. These ports can be configured as either a WAN or a LAN port, like all of the 1G RJ45 ports in the machine. Because a 10G WAN uplink will often be bottlenecked by IPsec tunnel speeds, the SFP+ ports are most useful for configuring high speed LANs, and for using fiber connections.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="virtual-appliance-and-sfp-ports">Virtual Appliance and SFP+ ports</h3>
@markup("md", "content/.markup/bodies/6998.md")
</aside>
<h2 id="port-configuration">Port configuration</h2>
<p>SFP+ ports are next to the regular LAN ports. They are represented as follows in the dashboard:</p>
<ul>
<li>SFP+ <strong>port 1</strong> is represented by <strong>port 7</strong> in the dashboard</li>
<li>SFP+ <strong>port 2</strong> is represented by <strong>port 8</strong> in the dashboard</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-wan/connector/sfp-ports.png" alt="The left port, SFP+ 1, is port 7. The right port, SFP+ 2, is port 8." /></p>
<p><em>The left port, SFP+ 1, is port 7. The right port, SFP+ 2, is port 8.</em></p>
<h2 id="sfp-module-compatibility">SFP+ module compatibility</h2>
<p>Cloudflare One Appliance only supports 10Gbps SFP+ modules, including RJ45, DAC, and fiber, among others. Many 1 Gbps modules are incompatible with the Intel driver used internally, and thus are not supported.</p>
<p>Cloudflare supports the following SFP+ inputs:</p>
<ul>
<li>10 Gbps Intel-compatible optics using 10GBase-SR, LR, ER. This includes Intel-compatible active optical cables (AOC) cables at 10 Gbps.</li>
<li>10 Gbps DAC Twinax cables, compatible with SFF-8431 v4.1 and SFF-8472 v10.4</li>
<li>10GBASE-T RJ45 converter modules</li>
</ul>
<p>Cloudflare successfully deployed commonly available 10G modules that are also compatible across many vendors:</p>
<ul>
<li>StarTech Dell EMC Twinax SFP+ DAC</li>
<li>Ubiquiti multi-mode, duplex, 10 Gbps fiber transceiver modules</li>
</ul>
<p>Keep in mind that SFP+ modules/cables have to be compatible at both ends, that is, both sides of the connection should be 10 Gbps, and it should really be the same module/cable that is compatible with both hardware stacks. The choice of module/optic/cable ultimately depends on your specific interoperability needs, and it is much less of a &quot;plug and play&quot; situation as one expects from RJ45.</p>
<h2 id="recover-from-unsupported-sfp-inputs">Recover from unsupported SFP+ inputs</h2>
<p>SFP+ modules should be installed and tested prior to deploying Cloudflare One Appliance into production usage.</p>
<p>An unsupported SFP+ input is indicated by the interface failing to come up (that is, the Cloudflare One Appliance has no status lights), and also by the port (7 or 8) going offline until the hardware is rebooted.</p>
<p>When an unsupported module is plugged, the module should be removed and then the Cloudflare One Appliance rebooted by removing power for five seconds. The module should not remain plugged during reboot, or the Cloudflare One Appliance will have to be rebooted again after the module is removed.</p>
