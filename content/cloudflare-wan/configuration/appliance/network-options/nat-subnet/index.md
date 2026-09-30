---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/
  description: Enable static NAT for subnets in Cloudflare One Appliance to re-use address spaces locally.
  full_title: Enable NAT for a subnet · Cloudflare WAN docs
  head_html: <title>Enable NAT for a subnet · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable static NAT for subnets in Cloudflare One Appliance to re-use address spaces locally."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/index.md"><meta property="og:title" content="Enable NAT for a subnet · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable static NAT for subnets in Cloudflare One Appliance to re-use address spaces locally."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/#page","headline":"Enable NAT for a subnet \u00b7 Cloudflare WAN docs","description":"Enable static NAT for subnets in Cloudflare One Appliance to re-use address spaces locally.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/nat-subnet/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/network-options/nat-subnet/
  schema: 1
---
<h2 id="overview">Overview</h2>
<p>Every subnet in the Cloudflare WAN (formerly Magic WAN) overlay must have a unique address space — otherwise, Cloudflare cannot determine which site should receive traffic for a given IP address. In practice, many organizations reuse the same private address ranges (for example, <code>192.168.1.0/24</code>) at multiple sites. Rather than renumbering those subnets, you can enable static network address translation (NAT) for a subnet on a Cloudflare One Appliance (formerly Magic WAN Connector). NAT assigns each site a unique overlay-facing prefix while preserving the existing local addressing.</p>
<p>With subnet NAT, the Appliance performs a static, 1:1 translation between:</p>
<ul>
<li>The <strong>local prefix</strong> used inside the site.</li>
<li>A <strong>NAT prefix</strong> that is advertised into the Cloudflare WAN overlay.</li>
</ul>
<p>Because the mapping is static, the Appliance supports both outbound connections from the site and inbound connections from Cloudflare WAN to the site. Connections do not have to be initiated by hosts behind the Cloudflare One Appliance.</p>
<h2 id="how-subnet-nat-works-in-cloudflare-wan">How subnet NAT works in Cloudflare WAN</h2>
<p>NAT is static and 1:1 between equal-sized prefixes. When you enable NAT for a subnet on an Appliance:</p>
<ul>
<li>The <strong>local prefix</strong> is the subnet on the LAN side of the Appliance.</li>
<li>The <strong>NAT prefix</strong> is a WAN-facing prefix of the same size.</li>
<li>The Appliance translates addresses 1:1 between the two prefixes:
<ul>
<li>For traffic leaving the site towards Cloudflare WAN, it replaces local addresses with the corresponding NAT addresses.</li>
<li>For traffic arriving at the site from Cloudflare WAN, it replaces NAT addresses with the corresponding local addresses.</li>
</ul>
</li>
</ul>
<h2 id="addressing-rules">Addressing rules</h2>
<p>To avoid overlapping addresses in the overlay, Cloudflare WAN enforces the following rules:</p>
<ul>
<li>
<p><strong>Uniqueness within a LAN</strong></p>
<ul>
<li>The local prefix for each subnet must be unique within that LAN on the Appliance.</li>
<li>You can reuse the same local prefix on a different LAN or on a different site.</li>
</ul>
</li>
<li>
<p><strong>Uniqueness in the Cloudflare WAN overlay</strong></p>
<ul>
<li>Every <strong>overlay-facing prefix</strong> must be unique across all sites in your Cloudflare WAN deployment.</li>
<li>For a subnet <strong>with NAT enabled</strong>, the overlay-facing prefix is the <strong>NAT prefix</strong>.</li>
<li>For a subnet <strong>without NAT</strong>, the overlay-facing prefix is the <strong>local prefix</strong>.</li>
</ul>
</li>
</ul>
<p>These rules allow you to reuse local space at multiple sites, as long as each subnet in the Cloudflare WAN overlay has a unique overlay-facing prefix.</p>
<h2 id="example">Example</h2>
<p>Consider a subnet that uses the following prefixes:</p>
<ul>
<li><strong>Local prefix</strong>: <code>192.168.100.0/24</code></li>
<li><strong>NAT prefix</strong>: <code>10.10.100.0/24</code></li>
</ul>
<p>In this case:</p>
<ul>
<li>When a host inside the site with address <code>192.168.100.13</code> sends traffic into the Cloudflare WAN overlay, the Appliance translates the address to <code>10.10.100.13</code>.</li>
<li>When traffic from another site, or from the Internet via Cloudflare WAN, targets <code>10.10.100.13</code>, the Appliance translates the address back to <code>192.168.100.13</code>.</li>
</ul>
<h2 id="configure-nat-for-subnets">Configure NAT for subnets</h2>
<p>You configure subnet NAT when you create or edit a LAN on a Cloudflare One Appliance. In the Appliance configuration:</p>
<ul>
<li>You define the <strong>local prefix</strong> for the subnet on the LAN side.</li>
<li>You optionally define a <strong>static NAT prefix</strong> of the same size. When present, this prefix becomes the overlay-facing prefix for that subnet.</li>
</ul>
<p>For step-by-step instructions to configure a LAN and supply a static NAT prefix, refer to:</p>
<ul>
<li><a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#create-a-lan">Configure hardware Appliance</a></li>
<li><a href="/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#create-a-lan">Configure Virtual Appliance</a></li>
</ul>
