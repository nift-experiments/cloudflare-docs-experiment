---
cp9:
  canonical: https://developers.cloudflare.com/magic-transit/analytics/
  description: Use Magic Transit analytics to monitor network performance and troubleshoot potential issues.
  full_title: Analytics · Cloudflare Magic Transit docs
  head_html: <title>Analytics · Cloudflare Magic Transit docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Magic Transit analytics to monitor network performance and troubleshoot potential issues."><link rel="canonical" href="https://developers.cloudflare.com/magic-transit/analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/magic-transit/analytics/index.md"><meta property="og:title" content="Analytics · Cloudflare Magic Transit docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Magic Transit analytics to monitor network performance and troubleshoot potential issues."><meta property="og:url" content="https://developers.cloudflare.com/magic-transit/analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Magic Transit"><meta name="algolia_product_filter" content="Magic Transit"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Magic Transit"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/magic-transit/analytics/#page","headline":"Analytics \u00b7 Cloudflare Magic Transit docs","description":"Use Magic Transit analytics to monitor network performance and troubleshoot potential issues.","url":"https://developers.cloudflare.com/magic-transit/analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /magic-transit/analytics/
  schema: 1
---
<p>Use these options to gather information at the start of your troubleshooting workflow. Then, use more detailed network data collection and analysis to identify the root cause.</p>
<ul>
<li>Analyze network traffic over time in <a href="#network-analytics">Network Analytics</a></li>
<li>Perform more detailed troubleshooting with:
<ul>
<li><a href="#traceroutes">Traceroutes</a></li>
<li><a href="#packet-captures">Packet captures</a></li>
</ul>
</li>
</ul>
<h2 id="network-analytics">Network Analytics</h2>
<p>Network Analytics provides detailed analytics on your Magic Transit traffic over time. You can filter data by traffic characteristics and review traffic trends over time.</p>
<p>For details, refer to <a href="/magic-transit/analytics/network-analytics/">Magic Transit Network Analytics</a>.</p>
<h2 id="traceroutes">Traceroutes</h2>
<p>Traceroutes provide a hop-by-hop breakdown of the Internet path network traffic follows from Cloudflare's network to your network.</p>
<p>For details, refer to <a href="/magic-transit/analytics/traceroutes/">Traceroutes</a>.</p>
<h2 id="packet-captures">Packet captures</h2>
<p>Packet captures allow you to analyze the raw packet data your network sends to and receives from Cloudflare's network.</p>
<p>For details, refer to <a href="/cloudflare-network-firewall/packet-captures/">packet captures</a>.</p>
<h2 id="query-analytics-with-graphql">Query analytics with GraphQL</h2>
<p>GraphQL Analytics provides a GraphQL API to query raw JSON data for your Magic Transit traffic analytics. You can ingest this data into a Security Information and Event Management (SIEM) tool or another platform for further analysis.</p>
<ul>
<li><a href="/magic-transit/analytics/query-bandwidth/">Querying Magic Transit tunnel bandwidth analytics with GraphQL</a></li>
<li><a href="/magic-transit/analytics/query-tunnel-health/">Querying Magic Transit tunnel health check results with GraphQL</a></li>
</ul>
