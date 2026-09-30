---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/
  description: Map geographic regions to pools using the API.
  full_title: Cloudflare Load Balancing Regions API · Cloudflare Load Balancing docs
  head_html: <title>Cloudflare Load Balancing Regions API · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Map geographic regions to pools using the API."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/index.md"><meta property="og:title" content="Cloudflare Load Balancing Regions API · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Map geographic regions to pools using the API."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/#page","headline":"Cloudflare Load Balancing Regions API \u00b7 Cloudflare Load Balancing docs","description":"Map geographic regions to pools using the API.","url":"https://developers.cloudflare.com/load-balancing/reference/region-mapping-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/reference/region-mapping-api/
  schema: 1
---
<p>Cloudflare’s Load Balancing Regions API has several uses:</p>
<ul>
<li>Identify which countries/areas (states/provinces in the case of the U.S. and Canada) are part of a specific Cloudflare Load Balancer region.</li>
<li>Identify the Cloudflare Load Balancer region for a particular country/area (states/provinces in the case of the U.S. and Canada).</li>
</ul>
<p>The Region API uses 2-letter <a href="https://www.iso.org/iso-3166-country-codes.html">ISO-3166-1 alpha-2 codes</a> for countries/areas and, in the case of the U.S. and Canada, ISO-3166-2 subdivision codes for states/provinces. Only the U.S. and Canada are provided with these subdivisions.</p>
<p>There are two main optional parameters for the Region API:</p>
<ul>
<li>country_code is a string containing a two-letter alpha-2 country code per ISO 3166-1. For example: /load_balancers/regions?country_code=US</li>
<li>subdivision_code is a string containing a two-letter subdivision code for the U.S. and Canada per ISO 3166-2. For example: /load_balancers/regions?subdivision_code=CA</li>
</ul>
<p>For additional details and examples on using the Region Mapping API, see <a href="/api/resources/load_balancers/subresources/regions/methods/list/">Cloudflare’s API documentation</a>.</p>
<h2 id="list-of-load-balancer-regions">List of Load Balancer regions</h2>
<table>
<thead>
<tr>
<th>Region code</th>
<th>Region name</th>
</tr>
</thead>
<tbody>
<tr>
<td>EEU</td>
<td>Eastern Europe</td>
</tr>
<tr>
<td>ENAM</td>
<td>Eastern North America</td>
</tr>
<tr>
<td>ME</td>
<td>Middle East</td>
</tr>
<tr>
<td>NAF</td>
<td>Northern Africa</td>
</tr>
<tr>
<td>NEAS</td>
<td>Northeast Asia</td>
</tr>
<tr>
<td>NSAM</td>
<td>Northern South America</td>
</tr>
<tr>
<td>OC</td>
<td>Oceania</td>
</tr>
<tr>
<td>SAF</td>
<td>Southern Africa</td>
</tr>
<tr>
<td>SAS</td>
<td>Southern Asia</td>
</tr>
<tr>
<td>SEAS</td>
<td>Southeast Asia</td>
</tr>
<tr>
<td>SSAM</td>
<td>Southern South America</td>
</tr>
<tr>
<td>WEU</td>
<td>Western Europe</td>
</tr>
<tr>
<td>WNAM</td>
<td>Western North America</td>
</tr>
</tbody>
</table>
