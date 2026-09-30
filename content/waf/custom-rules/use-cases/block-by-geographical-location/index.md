---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/
  description: Block traffic based on geographic location.
  full_title: Block traffic by geographical location · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Block traffic by geographical location · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Block traffic based on geographic location."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/index.md"><meta property="og:title" content="Block traffic by geographical location · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block traffic based on geographic location."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/#page","headline":"Block traffic by geographical location \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Block traffic based on geographic location.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Geolocation"]}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/block-by-geographical-location/
  schema: 1
---
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests by autonomous system number (ASN), continent, or country of origin.</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>AS Num</td>
<td>equals</td>
<td><code>131279</code></td>
<td>Or</td>
</tr>
<tr>
<td>Continent</td>
<td>equals</td>
<td><code>Asia</code></td>
<td>Or</td>
</tr>
<tr>
<td>Country</td>
<td>equals</td>
<td><code>Korea, North</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.asnum eq 131279) or (ip.src.continent eq &quot;AS&quot;) or (ip.src.country eq &quot;KP&quot;)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/block-traffic-from-specific-countries/">Use case: Block traffic from specific countries</a></li>
<li><a href="/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/">Use case: Allow traffic from specific countries only</a></li>
<li><a href="/ruleset-engine/rules-language/fields/reference/?field-category=Geolocation">Fields reference: Geolocation</a></li>
</ul>
