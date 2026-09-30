---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/reference/analytics/
  description: View DDoS attack analytics in Security Analytics, Network Analytics, or the GraphQL API.
  full_title: DDoS analytics · Cloudflare DDoS Protection docs
  head_html: <title>DDoS analytics · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="View DDoS attack analytics in Security Analytics, Network Analytics, or the GraphQL API."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/reference/analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/reference/analytics/index.md"><meta property="og:title" content="DDoS analytics · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View DDoS attack analytics in Security Analytics, Network Analytics, or the GraphQL API."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/reference/analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="DDoS Protection"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/reference/analytics/#page","headline":"DDoS analytics \u00b7 Cloudflare DDoS Protection docs","description":"View DDoS attack analytics in Security Analytics, Network Analytics, or the GraphQL API.","url":"https://developers.cloudflare.com/ddos-protection/reference/analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/reference/analytics/
  schema: 1
---
<p>You can view DDoS analytics in different dashboards, depending on your service and plan:</p>
<ul>
<li>
<p>The <a href="/waf/analytics/security-events/">Security Events dashboard</a> provides you with visibility into L7 security events that target your zone, including HTTP DDoS attacks and TCP attacks. The dashboard displays mitigations of HTTP DDoS attacks as HTTP DDoS events. These events are also available via <a href="/logs/">Cloudflare Logs</a>.</p>
</li>
<li>
<p>The <a href="/analytics/network-analytics/">Network Analytics dashboard</a> provides you with visibility into L3/4 traffic and DDoS attacks that target your IP ranges or Spectrum applications.</p>
</li>
</ul>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th>Service</th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>WAF/CDN</td>
<td>Sampled logs only</td>
<td>Security Events</td>
<td>Security Events</td>
<td>Security Events</td>
</tr>
<tr>
<td>Spectrum/BYOIP</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>Network Analytics</td>
</tr>
<tr>
<td>Magic Transit</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>Network Analytics</td>
</tr>
</tbody>
</table>
<h2 id="remarks">Remarks</h2>
<p>In some situations, the analytics dashboards will not show you the ID of the DDoS managed rule that handled a packet/request. This means that an internal DDoS rule, which Cloudflare does not currently expose publicly, applied an action to the packet/request. These internal DDoS rules have a very low false positive rate and should always be enabled to protect your properties against DDoS attacks. For the same reason, DDoS rule IDs may also be unavailable in Cloudflare logs and API responses.</p>
