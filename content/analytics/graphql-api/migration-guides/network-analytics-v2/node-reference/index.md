---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/
  description: Reference for Network Analytics v2 GraphQL nodes.
  full_title: NAv2 node reference · Cloudflare Analytics docs
  head_html: <title>NAv2 node reference · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for Network Analytics v2 GraphQL nodes."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/index.md"><meta property="og:title" content="NAv2 node reference · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for Network Analytics v2 GraphQL nodes."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/#page","headline":"NAv2 node reference \u00b7 Cloudflare Analytics docs","description":"Reference for Network Analytics v2 GraphQL nodes.","url":"https://developers.cloudflare.com/analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/migration-guides/network-analytics-v2/node-reference/
  schema: 1
---
<h2 id="main-nodes">Main nodes</h2>
<p>Main nodes provide deep packet-level information about traffic and attacks for Spectrum customers and Magic Transit customers.</p>
<p>Use the main node to query traffic and attacks at a high level, as seen at the Cloudflare edge:</p>
<table>
<thead>
<tr>
<th>Product</th>
<th>Main node</th>
</tr>
</thead>
<tbody>
<tr>
<td>Spectrum</td>
<td><code>spectrumNetworkAnalyticsAdaptiveGroups</code></td>
</tr>
<tr>
<td>Magic Transit</td>
<td><code>magicTransitNetworkAnalyticsAdaptiveGroups</code></td>
</tr>
</tbody>
</table>
<p>To query more specific details about attacks, use the <a href="#attack-nodes">attack nodes</a>.</p>
<p>Each row represents a packet sample. The sample rate of main nodes is 1/10,000 packets.</p>
<p>If you are using both Magic Transit and Spectrum for IP addresses that overlap, you can use only the Magic Transit node.</p>
<h2 id="attack-nodes">Attack nodes</h2>
<h3 id="dosdattackanalyticsgroups"><code>dosdAttackAnalyticsGroups</code></h3>
<p>This node provides information about DDoS attacks detected and mitigated by Cloudflare's main DDoS protection system, the denial of service daemon (<code>dosd</code>). This node includes attack metadata such as:</p>
<ul>
<li><code>startDatetime</code></li>
<li><code>endDatetime</code></li>
<li><code>attackType</code></li>
<li><code>sourceIp</code></li>
</ul>
<p>Each row represents an attack event. Each attack has a unique ID.</p>
<p>The sample rate is dynamic and based on the volume of packets, ranging from 1/100 to 1/10,000 packets.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="adjusting-attack-mitigation">Adjusting attack mitigation</h3>
@markup("md", "content/.markup/bodies/3178.md")
</aside>
<h3 id="dosdnetworkanalyticsadaptivegroups"><code>dosdNetworkAnalyticsAdaptiveGroups</code></h3>
<p>This node complements the information in the <code>dosdAttackAnalyticsGroups</code> node. Provides deep packet-level information about DDoS attack packets mitigated by <code>dosd</code>, including fields such as:</p>
<ul>
<li><code>ipProtocol</code></li>
<li><code>ipv4Checksum</code></li>
<li><code>ipv4Options</code></li>
<li><code>tcpSequenceNumber</code></li>
<li><code>tcpChecksum</code></li>
<li><code>icmpCode</code></li>
<li><code>ruleId</code></li>
<li><code>ruleName</code></li>
<li><code>attackVector</code></li>
</ul>
<p>Each row represents a packet sample. The sample rate is 1/10,000 packets.</p>
<h3 id="advancedtcpprotectionnetworkanalyticsadaptivegroups"><code>advancedTcpProtectionNetworkAnalyticsAdaptiveGroups</code></h3>
<p>This node is only available to Magic Transit customers. Provides metadata about out-of-state TCP DDoS attacks mitigated by Cloudflare's <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a> system.</p>
<p>Advanced TCP Protection does not use the following ID fields: attack ID, rule ID, and ruleset ID.</p>
<p>The sample rate is 1/1,000 packets.</p>
<h3 id="advanceddnsprotectionnetworkanalyticsadaptivegroups"><code>advancedDnsProtectionNetworkAnalyticsAdaptiveGroups</code></h3>
<p>This node is only available to Magic Transit customers. Provides metadata about DNS-based DDoS attacks mitigated by Cloudflare's <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a> system.</p>
<p>Samples include information about the following DNS header fields:</p>
<ul>
<li><code>dnsQueryName</code></li>
<li><code>dnsQueryType</code></li>
</ul>
<p>Advanced DNS Protection does not use the following ID fields: attack ID, rule ID, and ruleset ID.</p>
<p>The sample rate is 1/1,000 packets.</p>
<h3 id="magicfirewallnetworkanalyticsadaptivegroups"><code>magicFirewallNetworkAnalyticsAdaptiveGroups</code></h3>
<p>This node is only available to Magic Transit customers. Provides information about packets that were matched against customer-configured <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> rules.</p>
<p>Each row represents a packet sample that matches a Cloudflare Network Firewall rule.</p>
<p>Cloudflare Network Firewall does not use attack IDs, only rule IDs and ruleset IDs.</p>
<p>The sample rate is dynamic and based on the volume of packets, ranging from 1/100 to 1/1,000,000 packets.</p>
