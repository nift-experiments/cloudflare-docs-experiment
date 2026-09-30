---
cp9:
  canonical: https://developers.cloudflare.com/magic-transit/analytics/network-analytics/
  description: Analyze Magic Transit traffic with Network Analytics.
  full_title: Magic Transit Network Analytics · Cloudflare Magic Transit docs
  head_html: <title>Magic Transit Network Analytics · Cloudflare Magic Transit docs</title><meta name="generator" content="Nift"><meta name="description" content="Analyze Magic Transit traffic with Network Analytics."><link rel="canonical" href="https://developers.cloudflare.com/magic-transit/analytics/network-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/magic-transit/analytics/network-analytics/index.md"><meta property="og:title" content="Magic Transit Network Analytics · Cloudflare Magic Transit docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Analyze Magic Transit traffic with Network Analytics."><meta property="og:url" content="https://developers.cloudflare.com/magic-transit/analytics/network-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Magic Transit"><meta name="algolia_product_filter" content="Magic Transit"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Magic Transit"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/magic-transit/analytics/network-analytics/#page","headline":"Magic Transit Network Analytics \u00b7 Cloudflare Magic Transit docs","description":"Analyze Magic Transit traffic with Network Analytics.","url":"https://developers.cloudflare.com/magic-transit/analytics/network-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /magic-transit/analytics/network-analytics/
  schema: 1
---
<p><a href="/analytics/network-analytics/">Network Analytics</a> provides real-time insights into Magic Transit traffic that enters and leaves Cloudflare's network through GRE or IPsec tunnels.</p>
<p>Data is aggregated into time intervals that vary based on the selected zoom level. For example, a daily view shows 24-hour averages, which can flatten short-term traffic spikes. As a result, longer time intervals display lower peak bandwidth values compared to more granular views like five-minute intervals.</p>
<p>For details, refer to the <a href="/analytics/network-analytics/">Network Analytics</a> documentation.</p>
<h2 id="network-traffic-data-filters">Network traffic data filters</h2>
<p>With Magic Transit, you can account for traffic flows that enter Cloudflare's network, are blocked by DDoS rules or Cloudflare Network Firewall, and leave Cloudflare's network. This insight lets you track the total packets and bytes that traverse Cloudflare's network and are ultimately destined for your network. It also provides increased insight into traffic flows that are unaccounted for.</p>
<p>The complete list of filters includes:</p>
<ul>
<li>A list of your top tunnels by traffic volume.</li>
<li>Traffic source and destination by traffic type, on-ramps and off-ramps, <span class="nb-glossary-tooltip" title="IP address">IP addresses</span>, and ports.</li>
<li>Destination IP ranges and ASNs.</li>
<li>Protocols and packet sizes.</li>
<li>Samples of all GRE or IPsec tunnel traffic entering or leaving Cloudflare's network.</li>
<li>Mitigations applied (such as DDoS and Cloudflare Network Firewall) to traffic entering Cloudflare's network.</li>
</ul>
<p>For instructions, refer to <a href="#access-tunnel-traffic-analytics">Access tunnel traffic analytics</a>.</p>
<h2 id="access-tunnel-traffic-analytics">Access tunnel traffic analytics</h2>
<ol>
<li>Go to the <strong>Network Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>All Traffic</strong> tab, scroll to <strong>Top Insights</strong> to access network traffic filters. By default, the dashboard displays five items, but you can display up to 25 items at once. To change the number of items, select the drop-down menu.</li>
<li>(Optional) Hover over a traffic type. You can then filter for that traffic or exclude it from the results.</li>
<li>To adjust the scope of information, scroll to <strong>All traffic</strong> &gt; <strong>Add filter</strong>.</li>
<li>In the <strong>New filter</strong> popover, select the data type from the left drop-down menu, an operator from the middle drop-down menu, and an action from the right drop-down menu. For example:</li>
</ol>
<pre tabindex="0"><code class="language-txt">&lt;DESTINATION_TUNNELS&gt; | _equals_ | &lt;NAME_OF_YOUR_TUNNEL&gt;&#10;</code></pre>
<p>This lets you examine traffic from specific Source tunnels and/or Destination tunnels.</p>
<h2 id="feature-notes">Feature notes</h2>
<ul>
<li>For Magic Transit, <code>Non-Tunnel traffic</code> often represents traffic from the public Internet or traffic via <a href="/network-interconnect/">CNIs</a>.</li>
</ul>
<p>The label <code>Non-Tunnel traffic</code> is a placeholder, and Cloudflare will apply more specific labels to this category of traffic in the future.</p>
