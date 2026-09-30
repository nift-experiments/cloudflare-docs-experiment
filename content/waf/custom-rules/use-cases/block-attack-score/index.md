---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/
  description: Block requests with high WAF attack scores.
  full_title: Block requests by attack score · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Block requests by attack score · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Block requests with high WAF attack scores."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/index.md"><meta property="og:title" content="Block requests by attack score · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block requests with high WAF attack scores."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><meta name="pcx_tags" content="Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/#page","headline":"Block requests by attack score \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Block requests with high WAF attack scores.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Geolocation"]}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/block-attack-score/
  schema: 1
---
<p>The <a href="/waf/detections/attack-score/">attack score</a> helps identify variations of known attacks and their malicious payloads.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> blocks requests based on country code (<a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> format), from requests with an attack score lower than 20. For more information, refer to <a href="/waf/detections/attack-score/">WAF attack score</a>.</p>
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
<td>Country</td>
<td>is in</td>
<td><code>China</code>, <code>Taiwan</code>, <code>United Kingdom</code>, <code>United States</code></td>
<td>And</td>
</tr>
<tr>
<td>WAF Attack Score</td>
<td>less than</td>
<td><code>20</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(ip.src.country in {&quot;CN&quot; &quot;TW&quot; &quot;US&quot; &quot;GB&quot;} and cf.waf.score lt 20)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
