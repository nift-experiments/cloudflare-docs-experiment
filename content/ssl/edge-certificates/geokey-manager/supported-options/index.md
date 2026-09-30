---
cp9:
  canonical: https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/supported-options/
  description: Learn which options are supported for Geo Key Manager.
  full_title: Supported options - Geo Key Manager · Cloudflare SSL/TLS docs
  head_html: <title>Supported options - Geo Key Manager · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn which options are supported for Geo Key Manager."><link rel="canonical" href="https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/supported-options/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/supported-options/index.md"><meta property="og:title" content="Supported options - Geo Key Manager · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn which options are supported for Geo Key Manager."><meta property="og:url" content="https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/supported-options/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Geo Key Manager"><meta name="pcx_tags" content="Geolocation,Compliance"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/supported-options/#page","headline":"Supported options - Geo Key Manager \u00b7 Cloudflare SSL/TLS docs","description":"Learn which options are supported for Geo Key Manager.","url":"https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/supported-options/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Geolocation","Compliance"]}</script>
  markdown: true
  noindex: false
  route: /ssl/edge-certificates/geokey-manager/supported-options/
  schema: 1
---
<h2 id="available-regions">Available regions</h2>
<p>For customers with Geo Key Manager v2, you can use the <code>policy</code> parameter to specify following regions using the <strong>Region code</strong>:</p>
<table>
<thead>
<tr>
<th>Region code</th>
<th>Region name</th>
</tr>
</thead>
<tbody>
<tr>
<td>AFR</td>
<td>Africa</td>
</tr>
<tr>
<td>APAC</td>
<td>Asia Pacific</td>
</tr>
<tr>
<td>EEUR</td>
<td>Eastern Europe</td>
</tr>
<tr>
<td>ENAM</td>
<td>Eastern North America</td>
</tr>
<tr>
<td>EU</td>
<td>European Union</td>
</tr>
<tr>
<td>ME</td>
<td>Middle East</td>
</tr>
<tr>
<td>OC</td>
<td>Oceania</td>
</tr>
<tr>
<td>SAM</td>
<td>South America</td>
</tr>
<tr>
<td>WEUR</td>
<td>Western Europe</td>
</tr>
<tr>
<td>WNAM</td>
<td>Western North America</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="available-countries">Available countries</h2>
<p>For customers with Geo Key Manager v2, you can use the <code>policy</code> parameter to specify individual countries as well. Cloudflare is constantly expanding the number of supported countries. To indicate a country, specify the two-letter (ISO 3166) country code.</p>
<p>Examples of supported countries are Japan, Canada, India, and Australia.</p>
<hr />
<h2 id="highest-security-data-centers">Highest security data centers</h2>
<p>For customers with both Geo Key Manager v1 and v2, you can use the <code>geo_restrictions</code> parameter to only choose Cloudflare's highest security data centers.</p>
<p>The following aspects are unique to our highest security data centers, but the baseline security requirements for all data centers are also detailed in <a href="https://blog.cloudflare.com/introducing-cloudflare-geo-key-manager/">our blog</a>.</p>
<h3 id="pre-scheduled-and-biometric-controlled-facility-access">Pre-scheduled and biometric controlled facility access</h3>
<p>Employees of Cloudflare permitted to access the facility must have previously scheduled a visit before access will be granted.</p>
<p>Access to the entrance of the facility is controlled through the use of a biometric hand reader combined with an assigned access code.</p>
<h3 id="private-cages-with-biometric-readers">Private cages with biometric readers</h3>
<p>All equipment is in private cages with physical access controlled via biometrics and recorded in audit logs.
Entrants have to pass through five separate readers before they can access the cage.</p>
<h3 id="exterior-security-controls-and-monitoring">Exterior security controls and monitoring</h3>
<p>All points of ingress/egress are monitored by an intrusion detection system (IDS), with authorized users and access events archived for historical review.</p>
<h3 id="interior-security-controls-and-monitoring">Interior security controls and monitoring</h3>
<p>Interior points of ingress/egress are controlled by the access control subsystem, with entry routed through a mantrap. All areas are monitored and recorded with closed-circuit television, with data kept for a minimum of thirty days.</p>
<p>Exterior walls are airtight and may incorporate additional security measures such as reinforced concrete, Kevlar bullet board, vapor barriers, or bullet-proof front doors.</p>
