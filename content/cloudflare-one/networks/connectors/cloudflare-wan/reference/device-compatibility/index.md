---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/reference/device-compatibility/
  description: Reference information for Device compatibility in Zero Trust networking.
  full_title: Device compatibility · Cloudflare One docs
  head_html: <title>Device compatibility · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Device compatibility in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/reference/device-compatibility/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/reference/device-compatibility/index.md"><meta property="og:title" content="Device compatibility · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Device compatibility in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/reference/device-compatibility/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPsec"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/reference/device-compatibility/#page","headline":"Device compatibility \u00b7 Cloudflare One docs","description":"Reference information for Device compatibility in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/reference/device-compatibility/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPsec"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/reference/device-compatibility/
  schema: 1
---
<p>Cloudflare WAN (formerly Magic WAN) is compatible with any device that supports <span class="nb-glossary-tooltip" title="IPsec tunnel">IPsec</span> with the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters">supported configuration parameters</a> or supports <span class="nb-glossary-tooltip" title="GRE tunnel">GRE</span>.</p>
<p>The matrix below includes example devices and links to the integration guides.</p>
<table>
<thead>
<tr>
<th>Appliance</th>
<th>GRE tunnel</th>
<th>IPsec tunnel</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aruba-edgeconnect/">Aruba EdgeConnect</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Cisco ASA</td>
<td>Compatibility on roadmap</td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/">Cisco IOS XE</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-meraki-static/">Cisco Meraki MX (static routing)</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/viptela/">Cisco SD-WAN</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/fortinet/">Fortinet</a></td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/fitelnet/">Furukawa Electric FITELnet</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/juniper/">HPE Juniper Networking SRX Series Firewalls</a></td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/palo-alto/">Palo Alto Networks Next-Generation Firewall</a></td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/pfsense/">pfSense</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Prisma SD-WAN (Palo Alto)</td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td>Riverbed</td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/sonicwall/">SonicWall</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/sophos-firewall/">Sophos Firewall</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/strongswan/">strongSwan</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/ubiquiti/">Ubiquiti</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/velocloud/">Velocloud</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td>Versa</td>
<td>Specifications compatible<sup><a href="#footnote-1">1</a></sup></td>
<td>Compatibility on roadmap</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/vyos/">VyOS</a></td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/yamaha/">Yamaha RTX Router</a></td>
<td>-</td>
<td>✅</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>VPN</th>
<th>GRE tunnel</th>
<th>IPsec tunnel</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/alibaba-cloud/">Alibaba Cloud VPN Gateway</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aws/">Amazon AWS Transit Gateway</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/azure/">Azure VPN Gateway</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/google/">GCP Cloud VPN</a></td>
<td>-</td>
<td>✅</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/oracle/">Oracle Cloud</a></td>
<td>-</td>
<td>✅</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Specifications compatible per vendor documentation</li></ol></section>
