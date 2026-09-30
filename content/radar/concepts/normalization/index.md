---
cp9:
  canonical: https://developers.cloudflare.com/radar/concepts/normalization/
  description: Understand how Cloudflare Radar normalizes data using percentages, min-max scaling, and other methods applied to API responses.
  full_title: Normalization methods · Cloudflare Radar docs
  head_html: <title>Normalization methods · Cloudflare Radar docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how Cloudflare Radar normalizes data using percentages, min-max scaling, and other methods applied to API responses."><link rel="canonical" href="https://developers.cloudflare.com/radar/concepts/normalization/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/radar/concepts/normalization/index.md"><meta property="og:title" content="Normalization methods · Cloudflare Radar docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how Cloudflare Radar normalizes data using percentages, min-max scaling, and other methods applied to API responses."><meta property="og:url" content="https://developers.cloudflare.com/radar/concepts/normalization/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Radar"><meta name="algolia_product_filter" content="Radar"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Radar"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/radar/concepts/normalization/#page","headline":"Normalization methods \u00b7 Cloudflare Radar docs","description":"Understand how Cloudflare Radar normalizes data using percentages, min-max scaling, and other methods applied to API responses.","url":"https://developers.cloudflare.com/radar/concepts/normalization/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /radar/concepts/normalization/
  schema: 1
---
<p>Cloudflare Radar does not normally return raw values. Instead, values are returned as percentages or normalized using min-max.</p>
<p>Refer to the <code>result.meta.normalization</code> property in the response to check which post-processing method was applied to the raw values, if any.</p>
<h2 id="method">Method</h2>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>PERCENTAGE</code></td>
<td>Values represent percentages.</td>
</tr>
<tr>
<td><code>PERCENTAGE_CHANGE</code></td>
<td>Values represent a <a href="https://en.wikipedia.org/wiki/Relative_change_and_difference#Percentage_change">percentage change</a> from a baseline period.</td>
</tr>
<tr>
<td><code>OVERLAPPED_PERCENTAGE</code></td>
<td>Values represent percentages that exceed 100% due to overlap.</td>
</tr>
<tr>
<td><code>MIN_MAX</code></td>
<td>Values have been normalized using <a href="https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)">min-max</a>.</td>
</tr>
<tr>
<td><code>MIN0_MAX</code></td>
<td>Values have been normalized using min-max, but setting the minimum value to <code>0</code>. Equivalent to a proportion of the maximum value in the entire response, scaled between 0 and 1.</td>
</tr>
<tr>
<td><code>RAW_VALUES</code></td>
<td>Values are raw and have not been changed.</td>
</tr>
</tbody>
</table>
<p>If you want to compare values across locations/time ranges/etc., in endpoints that normalize values using min-max, you must do so in the same request. This is done by asking for multiple series. All values will then be normalized using the same minimum and maximum value and can safely be compared against each other. Refer to <a href="/radar/get-started/making-comparisons/">Make comparisons</a> for more information.</p>
