---
cp9:
  canonical: https://developers.cloudflare.com/radar/concepts/confidence-levels/
  description: Interpret Cloudflare Radar confidence levels to assess data quality and reliability for a given location or time range.
  full_title: Confidence levels · Cloudflare Radar docs
  head_html: <title>Confidence levels · Cloudflare Radar docs</title><meta name="generator" content="Nift"><meta name="description" content="Interpret Cloudflare Radar confidence levels to assess data quality and reliability for a given location or time range."><link rel="canonical" href="https://developers.cloudflare.com/radar/concepts/confidence-levels/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/radar/concepts/confidence-levels/index.md"><meta property="og:title" content="Confidence levels · Cloudflare Radar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Interpret Cloudflare Radar confidence levels to assess data quality and reliability for a given location or time range."><meta property="og:url" content="https://developers.cloudflare.com/radar/concepts/confidence-levels/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Radar"><meta name="algolia_product_filter" content="Radar"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Radar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/radar/concepts/confidence-levels/#page","headline":"Confidence levels \u00b7 Cloudflare Radar docs","description":"Interpret Cloudflare Radar confidence levels to assess data quality and reliability for a given location or time range.","url":"https://developers.cloudflare.com/radar/concepts/confidence-levels/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /radar/concepts/confidence-levels/
  schema: 1
---
<p>The <code>result.meta.confidenceInfo.level</code> in the response provides an indication of how much confidence Cloudflare has in the data. Confidence levels can be affected either by internal issues affecting data quality or by not having a lot of data for a given location (like Antarctica) or Autonomous System (AS).</p>
<table>
<thead>
<tr>
<th>Level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td>There is not enough data in this time range and/or for this location or Autonomous System. Data also exhibits an erratic pattern, possibly due to the reasons previously mentioned.</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td>There is not enough data in this timerange and/or in this location or Autonomous System.</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td>Data exhibits an erratic pattern but is not affected by known data issues (like pipeline issues).</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td>Unassigned.</td>
</tr>
<tr>
<td><strong>5</strong></td>
<td>No known data quality issues.</td>
</tr>
</tbody>
</table>
