---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/routing-and-bgp/
  description: Troubleshoot Troubleshoot routing and BGP issues in Zero Trust networking.
  full_title: Troubleshoot routing and BGP · Cloudflare One docs
  head_html: <title>Troubleshoot routing and BGP · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Troubleshoot routing and BGP issues in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/routing-and-bgp/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/routing-and-bgp/index.md"><meta property="og:title" content="Troubleshoot routing and BGP · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Troubleshoot routing and BGP issues in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/routing-and-bgp/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/routing-and-bgp/#page","headline":"Troubleshoot routing and BGP \u00b7 Cloudflare One docs","description":"Troubleshoot Troubleshoot routing and BGP issues in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/routing-and-bgp/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/routing-and-bgp/
  schema: 1
---
<p>This guide helps you diagnose and resolve common routing and BGP issues with Cloudflare WAN. These issues can affect traffic delivery, cause unexpected latency, or result in connectivity loss.</p>
<h2 id="quick-diagnostic-checklist">Quick diagnostic checklist</h2>
<p>If you are experiencing routing or BGP issues, check these items first:</p>
<ol>
<li><strong>BGP session state</strong>: Verify session is <strong>Established</strong>, not stuck in <strong>Connect</strong> or <strong>Active</strong>.</li>
<li><strong>Firewall rules</strong>: Ensure TCP port <code>179</code> is permitted bidirectionally between your router and Cloudflare.</li>
<li><strong>Tunnel or CNI health</strong>: Check that underlying connectivity is healthy. Degraded tunnels affect route priority.</li>
<li><strong>Static route conflicts</strong>: Static routes take precedence over BGP routes at equal priority.</li>
</ol>
<h2 id="resolve-common-issues">Resolve common issues</h2>
<h3 id="bgp-session-not-establishing">BGP session not establishing</h3>
<p>This section covers BGP peering sessions (beta) between your network and Cloudflare, established over <a href="/network-interconnect/">CNI</a> or tunnels.</p>
<h4 id="symptoms">Symptoms</h4>
<ul>
<li>BGP session never reaches <strong>Established</strong> state</li>
<li>No routes being advertised or received</li>
<li>Router logs show repeated connection attempts</li>
</ul>
<h4 id="bgp-session-states">BGP session states</h4>
<table>
<thead>
<tr>
<th align="left">State</th>
<th align="left">Meaning</th>
<th align="left">Action</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Established</strong></td>
<td align="left">Session up, exchanging routes</td>
<td align="left">Normal operation</td>
</tr>
<tr>
<td align="left"><strong>Active</strong></td>
<td align="left">Attempting to initiate connection</td>
<td align="left">Check firewall rules, verify neighbor IP</td>
</tr>
<tr>
<td align="left"><strong>Connect</strong></td>
<td align="left">TCP connection in progress</td>
<td align="left">Check port <code>179</code> access, verify peering IP</td>
</tr>
<tr>
<td align="left"><strong>Idle</strong></td>
<td align="left">Session down, no connection attempts</td>
<td align="left">Check configuration, verify BGP is enabled</td>
</tr>
</tbody>
</table>
<h4 id="solution">Solution</h4>
<ol>
<li>Verify your firewall permits TCP port <code>179</code> bidirectionally between your router and the Cloudflare peering address.</li>
<li>Confirm the neighbor IP matches the Cloudflare-provided peering address exactly.</li>
<li>Verify your ASN configuration matches the dashboard settings. Only eBGP is supported, so your ASN must differ from the Cloudflare account ASN.</li>
<li>If using MD5 authentication, verify the password matches on both sides.</li>
</ol>
<h3 id="unexpected-traffic-routing-or-latency">Unexpected traffic routing or latency</h3>
<h4 id="symptoms-1">Symptoms</h4>
<ul>
<li>Traffic from specific regions routed through distant data centers</li>
<li>Higher than expected latency for regional users</li>
<li>Traffic not using the closest tunnel or CNI</li>
</ul>
<h4 id="causes">Causes</h4>
<ul>
<li>Tunnel health degradation causing route deprioritization</li>
<li>Regional route scoping misconfiguration</li>
<li>BGP route priorities not set as expected</li>
<li>Static routes overriding BGP routes</li>
</ul>
<h4 id="solution-1">Solution</h4>
<ol>
<li>
<p><strong>Check tunnel health</strong>: Degraded tunnels have 500,000 added to their route priority. Down tunnels have 1,000,000 added. Traffic shifts to healthier paths, which may be in different regions. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a> for diagnostic steps.</p>
</li>
<li>
<p><strong>Review route priorities</strong>: Lower priority values indicate higher preference. Verify your routes have the expected priority configuration.</p>
<ul>
<li>Default BGP route priority: <code>100</code></li>
<li>Static routes at priority <code>100</code> take precedence over BGP routes at <code>100</code></li>
</ul>
</li>
<li>
<p><strong>Check regional scoping</strong>: If you use region-scoped routes, ensure all regions have route coverage. Traffic arriving at a region without a matching route is dropped.</p>
</li>
<li>
<p><strong>Use Network Analytics</strong>: Review traffic patterns to identify where traffic is landing and which paths it follows. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/analytics/network-analytics/">Network Analytics</a> for usage instructions.</p>
</li>
</ol>
<h3 id="cni-link-failures">CNI link failures</h3>
<h4 id="symptoms-2">Symptoms</h4>
<ul>
<li>CNI shows down in dashboard</li>
<li>BGP session over CNI drops</li>
<li>Traffic fails over to tunnels or alternate CNIs</li>
</ul>
<h4 id="cni-issue-layers">CNI issue layers</h4>
<p>CNI issues can occur at multiple layers:</p>
<table>
<thead>
<tr>
<th align="left">Issue type</th>
<th align="left">Impact</th>
<th align="left">What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Physical link down</td>
<td align="left">All traffic over that CNI affected</td>
<td align="left">Light levels, cross-connect status</td>
</tr>
<tr>
<td align="left">BGP session down</td>
<td align="left">Dynamic routes withdrawn</td>
<td align="left">BGP neighbor state on your router</td>
</tr>
<tr>
<td align="left">Prefixes withdrawn</td>
<td align="left">Specific routes unavailable</td>
<td align="left">BGP advertised and received routes</td>
</tr>
</tbody>
</table>
<p>A healthy physical link can still have BGP issues. A healthy BGP session can exist while specific prefixes are withdrawn.</p>
<h4 id="solution-2">Solution</h4>
<p><strong>Check physical layer (your side):</strong></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5541.md")
</aside>
<ol>
<li>Verify the interface is administratively up on your router.</li>
<li>Check optical light levels (Tx/Rx dBm). Abnormal readings indicate fiber or transceiver issues.</li>
<li>If light levels are low or absent on your receive side, contact your data center to verify cross-connect status.</li>
</ol>
<p><strong>Check BGP session:</strong></p>
<ol>
<li>Verify BGP neighbor state on your router shows <strong>Established</strong>.</li>
<li>Check for MD5 authentication mismatches if authentication is configured.</li>
<li>Review BGP logs for error messages indicating why the session may have dropped.</li>
</ol>
<p><strong>Check for maintenance:</strong></p>
<ol>
<li>Review <a href="https://www.cloudflarestatus.com/">Cloudflare Status</a> for scheduled maintenance affecting your CNI location.</li>
<li>Some maintenance events may temporarily affect CNI connectivity even when marked as non-disruptive.</li>
</ol>
<p>Refer to <a href="/network-interconnect/">Network Interconnect</a> for CNI configuration and setup information.</p>
<h3 id="static-and-bgp-route-conflicts">Static and BGP route conflicts</h3>
<h4 id="symptoms-3">Symptoms</h4>
<ul>
<li>BGP routes not being used despite being learned</li>
<li>Traffic not following expected BGP path</li>
<li>Route changes not taking effect as expected</li>
</ul>
<h4 id="cause">Cause</h4>
<p>Cloudflare prefers static routes when static and BGP routes share the same prefix and priority. This ensures manually configured routes take precedence unless explicitly deprioritized.</p>
<h4 id="solution-3">Solution</h4>
<p>Adjust route priorities based on your preference:</p>
<ul>
<li><strong>To prefer BGP routes</strong>: Set static route priority to a higher number (for example, <code>150</code> or <code>200</code>). Higher numbers indicate lower preference.</li>
<li><strong>To prefer static routes</strong>: Keep static route priority at or below <code>100</code>. BGP routes default to priority <code>100</code>.</li>
</ul>
<table>
<thead>
<tr>
<th align="left">Route type</th>
<th align="left">Prefix</th>
<th align="left">Priority</th>
<th align="left">Selected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Static</td>
<td align="left"><code>10.0.0.0/24</code></td>
<td align="left"><code>100</code></td>
<td align="left">Yes (static wins ties)</td>
</tr>
<tr>
<td align="left">BGP</td>
<td align="left"><code>10.0.0.0/24</code></td>
<td align="left"><code>100</code></td>
<td align="left">No</td>
</tr>
</tbody>
</table>
<p>To make the BGP route preferred in this example, change the static route priority to <code>150</code> or higher, or remove the static route entirely.</p>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#route-prioritization">Route prioritization</a> for detailed information on how priorities work.</p>
<h2 id="cni-tunnel-and-bgp-health">CNI, tunnel, and BGP health</h2>
<p>Understanding the relationship between these components helps diagnose routing issues:</p>
<table>
<thead>
<tr>
<th align="left">Component</th>
<th align="left">What it monitors</th>
<th align="left">Impact when unhealthy</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>CNI health</strong></td>
<td align="left">Physical or virtual interconnect link status</td>
<td align="left">BGP session may drop. All traffic over that CNI is affected.</td>
</tr>
<tr>
<td align="left"><strong>Tunnel health</strong></td>
<td align="left">Logical GRE or IPsec tunnel through health check probes</td>
<td align="left">Route priority penalized. Traffic steers to healthier tunnels.</td>
</tr>
<tr>
<td align="left"><strong>BGP session</strong></td>
<td align="left">Control plane connectivity for dynamic routing</td>
<td align="left">Dynamic routes withdrawn. Static routes remain unaffected.</td>
</tr>
</tbody>
</table>
<p>A healthy CNI can have an unhealthy tunnel if health check probes are blocked or misconfigured. BGP routes can be withdrawn even when the underlying physical link is operational.</p>
<h2 id="gather-information-for-support">Gather information for support</h2>
<p>If you have worked through this guide and still experience routing issues, gather the following information before contacting Cloudflare support.</p>
<h3 id="required-information">Required information</h3>
<ol>
<li><strong>Account ID</strong> and affected prefix(es), tunnel name(s), or CNI identifier(s)</li>
<li><strong>Timestamps</strong> (in UTC) when the issue occurred</li>
<li><strong>BGP configuration details:</strong>
<ul>
<li>Your ASN and Cloudflare peering ASN</li>
<li>Neighbor IP addresses</li>
<li>Sanitized router configuration (remove passwords and keys)</li>
</ul>
</li>
<li><strong>Current state information:</strong>
<ul>
<li>BGP session state from your router</li>
<li>Dashboard screenshots showing prefix, route, or tunnel status</li>
</ul>
</li>
</ol>
<h3 id="helpful-diagnostic-data">Helpful diagnostic data</h3>
<ul>
<li><strong>Router logs</strong>: BGP neighbor logs covering the incident timeframe</li>
<li><strong>Traceroute results</strong>: From affected source networks to your prefix</li>
<li><strong>For CNI issues</strong>: Optical light level readings from your equipment</li>
</ul>
<h3 id="router-diagnostic-commands">Router diagnostic commands</h3>
<p>Collect output from these commands (syntax varies by vendor):</p>
<pre tabindex="0"><code class="language-sh">&#35; Show BGP neighbor status&#10;show bgp neighbors&#10;&#10;&#35; Show BGP summary&#10;show bgp ipv4 unicast summary&#10;&#10;&#35; Show specific prefix in BGP table&#10;show bgp ipv4 unicast &lt;YOUR_PREFIX&gt;&#10;&#10;&#35; Show interface status (for CNI)&#10;show interface &lt;YOUR_INTERFACE_NAME&gt;&#10;&#10;&#35; Show received and advertised routes&#10;show bgp ipv4 unicast neighbors &lt;YOUR_NEIGHBOR_IP&gt; routes&#10;show bgp ipv4 unicast neighbors &lt;YOUR_NEIGHBOR_IP&gt; advertised-routes&#10;</code></pre>
<h2 id="resources">Resources</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#route-prioritization">Traffic steering</a>: Route prioritization, BGP communities, and ECMP behavior</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/">Configure routes</a>: Static route configuration</li>
<li><a href="/network-interconnect/">Network Interconnect</a>: CNI setup and BGP peering</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a>: Tunnel-specific diagnostic steps</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/analytics/network-analytics/">Network Analytics</a>: Traffic analysis and monitoring</li>
<li><a href="https://www.cloudflarestatus.com/">Cloudflare Status</a>: Maintenance and incident notifications</li>
</ul>
