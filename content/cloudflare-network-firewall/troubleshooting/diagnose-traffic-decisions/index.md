---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-network-firewall/troubleshooting/diagnose-traffic-decisions/
  description: Diagnose why the Network Firewall allowed or blocked traffic.
  full_title: Diagnose traffic decisions · Cloudflare Network Firewall docs
  head_html: <title>Diagnose traffic decisions · Cloudflare Network Firewall docs</title><meta name="generator" content="Nift"><meta name="description" content="Diagnose why the Network Firewall allowed or blocked traffic."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-network-firewall/troubleshooting/diagnose-traffic-decisions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-network-firewall/troubleshooting/diagnose-traffic-decisions/index.md"><meta property="og:title" content="Diagnose traffic decisions · Cloudflare Network Firewall docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Diagnose why the Network Firewall allowed or blocked traffic."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-network-firewall/troubleshooting/diagnose-traffic-decisions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Network Firewall"><meta name="algolia_product_filter" content="Cloudflare Network Firewall"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare Network Firewall"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-network-firewall/troubleshooting/diagnose-traffic-decisions/#page","headline":"Diagnose traffic decisions \u00b7 Cloudflare Network Firewall docs","description":"Diagnose why the Network Firewall allowed or blocked traffic.","url":"https://developers.cloudflare.com/cloudflare-network-firewall/troubleshooting/diagnose-traffic-decisions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-network-firewall/troubleshooting/diagnose-traffic-decisions/
  schema: 1
---
<p>When traffic is unexpectedly blocked, multiple Cloudflare systems could be responsible. This guide walks you through identifying what is blocking your traffic and how to resolve it.</p>
<p>Traffic passing through Cloudflare's network is evaluated by several independent security systems in the following sequence:</p>
<ol>
<li>Network-layer DDoS protection: This layer manages DDoS rulesets.</li>
<li>Advanced TCP protection: Cloudflare carries a stateful TCP inspection known as (<a href="https://blog.cloudflare.com/announcing-flowtrackd/">flowtrackd</a>).</li>
<li>Network Firewall: Your custom and managed firewall rules.</li>
</ol>
<p>Each system operates independently. Traffic blocked by an earlier system never reaches later systems for evaluation.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4234.md")
</aside>
<p>To diagnose blocked traffic, use <a href="/analytics/network-analytics/">Network Analytics</a> to identify which system is blocking the traffic and why. If Network Analytics does not provide enough information, you can use packet captures for deeper analysis.</p>
<h2 id="quick-triage-checklist">Quick triage checklist</h2>
<p>Before making changes, gather the following information:</p>
<ul>
<li>What traffic is affected? Check source IP, destination IP, ports, and protocols.</li>
<li>When did the issue start?</li>
<li>Were any configuration changes made recently?</li>
<li>Is this affecting all traffic or specific flows?</li>
<li>Check <a href="https://www.cloudflarestatus.com/">Cloudflare Status</a> for any ongoing incidents</li>
</ul>
<h2 id="filter-dropped-traffic">Filter dropped traffic</h2>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Under <strong>Protect &amp; Connect</strong>, go to <strong>Insights</strong> &gt; <strong>Network analytics</strong>.</li>
<li>In the <strong>All Traffic</strong> tab, select <strong>Add filter</strong>.</li>
<li>Configure the filter:
<ul>
<li>Select <strong>Action</strong> &gt; <strong>equals</strong> &gt; <strong>Drop</strong></li>
<li>Select <strong>Apply</strong>.</li>
</ul>
</li>
<li>Filter the time range to when the issue occurred.</li>
<li>Add additional filters if you know the affected traffic characteristics (such as Source IP, Destination IP, and more).</li>
<li>To identify the blocking system:
In the <strong>Packet Summary</strong> graph, select the three dots &gt; <strong>Mitigation system</strong>.
This tells you which Cloudflare system blocked the traffic.</li>
</ol>
<h3 id="if-the-mitigation-system-displays-ddos-managed-ruleset">If the mitigation system displays DDoS Managed Ruleset</h3>
<p>If the mitigation system displays DDoS Managed Ruleset, this means that traffic was blocked by DDoS Managed Ruleset. Note the <strong>Rule ID</strong> and <strong>Rule Name</strong> fields to identify which specific rule triggered.</p>
<ol>
<li>At the top of <strong>Network analytics</strong>, select <strong>DDoS managed rules</strong>.</li>
<li>Make sure to include any relevant filters to identify the traffic and to narrow down the time range to the relevant issue timing.</li>
<li>In the <strong>Packets summary</strong> graph, select the three dots, then choose <strong>Rule</strong>. The dashboard will show you the rules that were acting on your traffic.</li>
<li>To resolve: Adjust the DDoS managed rule sensitivity or <a href="/ddos-protection/managed-rulesets/network/network-overrides/">create an override</a> for the affected traffic pattern.</li>
</ol>
<h3 id="if-the-mitigation-system-displays-tcp-protection">If the mitigation system displays TCP Protection</h3>
<p>If the mitigation system displays TCP Protection, it means that traffic was blocked by <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">TCP Protection</a>. Refer to <a href="/ddos-protection/advanced-ddos-systems/concepts/#mitigation-reasons">Mitigation Reason</a> field to understand why it displays TCP Protection.</p>
<p><strong>To resolve</strong>, create an <a href="/ddos-protection/advanced-ddos-systems/how-to/add-prefix-allowlist/">Advanced TCP Protection allowlist</a> or <a href="/ddos-protection/advanced-ddos-systems/how-to/create-filter/">filter</a> to bypass protection for the affected traffic.</p>
<h3 id="if-the-mitigation-system-displays-firewall-policy">If the mitigation system displays Firewall Policy</h3>
<p>If your traffic was blocked by your Network Firewall configuration:</p>
<ol>
<li>At the top of <strong>Network analytics</strong>, select the <strong>Firewall</strong> tab.</li>
<li>Make sure to include any relevant filters to identify the traffic and to narrow down the time range to the relevant issue timing.</li>
<li>In the <strong>Packets summary</strong> graph, select the three dots, then choose <strong>Rule</strong>. The dashboard will show you the rules that were acting on your traffic.</li>
<li>Review your <a href="/cloudflare-network-firewall/how-to/add-policies/">Network Firewall policies</a> and adjust the rule order or expressions as needed.</li>
</ol>
<h2 id="use-packet-captures-for-deeper-analysis">Use packet captures for deeper analysis</h2>
<p>If you cannot identify the issue from Network Analytics, use <a href="/cloudflare-network-firewall/packet-captures/">packet captures</a> to inspect the actual traffic:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</li>
<li>Under <strong>Protect &amp; Connect</strong>, go to <strong>Insights</strong> &gt; <strong>Network health</strong>.</li>
<li>Go to <strong>Diagnostics</strong>, and configure a packet capture filter matching the affected traffic. Note that the packet capture (pcap) might be empty because packets were dropped.</li>
<li>Analyze the captured packets to understand traffic characteristics.</li>
<li>Compare against your rule configurations.</li>
</ol>
<h2 id="common-scenarios">Common scenarios</h2>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Symptoms</th>
<th>Likely cause</th>
<th>Recommended action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Partner traffic blocked</td>
<td>Specific source IP blocked</td>
<td>DDoS or ATP sensitivity</td>
<td>Allowlist partner IP ranges in both systems</td>
</tr>
<tr>
<td>New rule not working</td>
<td>Traffic still passes</td>
<td>Rule order (earlier rule matches first)</td>
<td>Adjust rule priority or refine the matching criteria</td>
</tr>
<tr>
<td>Traffic blocked after change</td>
<td>Sudden drops after configuration change</td>
<td>Rule misconfiguration</td>
<td>Review recent changes and revert to the last version</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/analytics/network-analytics/">Network Analytics</a></li>
<li><a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a></li>
<li><a href="/cloudflare-network-firewall/how-to/add-policies/">Network Firewall rule configuration</a></li>
<li><a href="/cloudflare-network-firewall/packet-captures/">Packet captures</a></li>
</ul>
