---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/network-layers/
  description: Map Cloudflare products to OSI model layers, from Layer 7 application services to Layer 1 physical connections.
  full_title: Network Layers · Cloudflare Fundamentals docs
  head_html: <title>Network Layers · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Map Cloudflare products to OSI model layers, from Layer 7 application services to Layer 1 physical connections."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/network-layers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/network-layers/index.md"><meta property="og:title" content="Network Layers · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Map Cloudflare products to OSI model layers, from Layer 7 application services to Layer 1 physical connections."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/network-layers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/network-layers/#page","headline":"Network Layers \u00b7 Cloudflare Fundamentals docs","description":"Map Cloudflare products to OSI model layers, from Layer 7 application services to Layer 1 physical connections.","url":"https://developers.cloudflare.com/fundamentals/reference/network-layers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/network-layers/
  schema: 1
---
<p>Below is a list of the different layers that makes up the <a href="https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/">open systems interconnection (OSI) model</a> and the associated Cloudflare products.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8782.md")
</aside>
<table>
<thead>
<tr>
<th>Network layer</th>
<th>Protocol and related products</th>
</tr>
</thead>
<tbody>
<tr>
<td>7 Application layer</td>
<td><strong>HTTP, DNS</strong><br/> <a href="/dns">Authoritative DNS</a>, <a href="/bots">Bot Management</a>, <a href="/cache/">CDN</a>, <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a>, <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> (outbound only), <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>, <a href="/load-balancing/understand-basics/proxy-modes/">Load Balancing</a>, <a href="/stream/">Stream</a>, <a href="/waf/">WAF</a></td>
</tr>
<tr>
<td>6 Presentation layer</td>
<td></td>
</tr>
<tr>
<td>5 Session layer</td>
<td></td>
</tr>
<tr>
<td>4 Transport layer</td>
<td><strong>TCP/UDP</strong><br/> <a href="/argo-smart-routing/">Argo Smart Routing</a>, <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> (outbound only), <a href="/load-balancing/understand-basics/proxy-modes/">Load Balancing</a>, <a href="/spectrum/">Spectrum</a></td>
</tr>
<tr>
<td>3 Network layer</td>
<td><strong>IP, GRE, any packet/protocol</strong><br/> <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>, <a href="/magic-transit">Magic Transit</a>, <a href="/cloudflare-wan">Cloudflare WAN</a></td>
</tr>
<tr>
<td>2 Datalink layer</td>
<td><strong>Direct connection</strong><br/> <a href="/network-interconnect">Cloudflare Network Interconnect (CNI)</a></td>
</tr>
<tr>
<td>1 Physical layer</td>
<td><strong>Direct connection</strong><br/> <a href="/network-interconnect">Cloudflare Network Interconnect (CNI)</a></td>
</tr>
</tbody>
</table>
