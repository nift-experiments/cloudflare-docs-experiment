---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/
  description: How Path MTU Discovery (PMTUD) works in Zero Trust.
  full_title: Path MTU Discovery (PMTUD) · Cloudflare One docs
  head_html: <title>Path MTU Discovery (PMTUD) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Path MTU Discovery (PMTUD) works in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/index.md"><meta property="og:title" content="Path MTU Discovery (PMTUD) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Path MTU Discovery (PMTUD) works in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="MASQUE,IPv6"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#page","headline":"Path MTU Discovery (PMTUD) \u00b7 Cloudflare One docs","description":"How Path MTU Discovery (PMTUD) works in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["MASQUE","IPv6"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6352.md")
</div></details>
<p>The <a href="https://www.cloudflare.com/learning/network-layer/what-is-mtu/">Maximum Transmission Unit (MTU)</a> is the largest data packet size that a device can send over a network without fragmentation. When you connect to services through the Cloudflare One Client (formerly WARP), your data is encapsulated, which adds extra headers and increases the overall packet size. On some networks, especially cellular or guest Wi-Fi networks, the network's MTU may be smaller than the Cloudflare One Client's <a href="#recommended-mtu">default packet size</a>. This mismatch forces packets to be fragmented or dropped entirely, leading to connection instability or complete connection failures.</p>
<p>The Cloudflare One Client's Path MTU Discovery (PMTUD) feature solves this problem by actively probing for the minimum MTU along the entire network path between the device and Cloudflare. The Cloudflare One Client will then dynamically adjust its <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#virtual-interface">tunnel interface</a> MTU based on the probe results. This allows the Cloudflare One Client to maintain a stable connection on low MTU networks and take advantage of higher MTUs when available.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6351.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>The Cloudflare One Client must be configured to use the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE tunnel protocol</a>.</li>
</ul>
<h2 id="enable-path-mtu-discovery">Enable Path MTU Discovery</h2>
<p>PMTUD is disabled by default. To enable PMTUD on your devices, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#windows">deploy an MDM file</a> with the <code>enable_pmtud</code> key set to <code>true</code>. For example:</p>
<pre tabindex="0"><code class="language-xml">&lt;dict&gt;&#10;	&lt;key&gt;organization&lt;/key&gt;&#10;	&lt;string&gt;your-team-name&lt;/string&gt;&#10;	&lt;key&gt;warp_tunnel_protocol&lt;/key&gt;&#10;  &lt;string&gt;masque&lt;/string&gt;&#10;	&lt;key&gt;enable_pmtud&lt;/key&gt;&#10;  &lt;true/&gt;&#10;&lt;/dict&gt;&#10;</code></pre>
<p>This configuration enables the PMTUD feature and explicitly configures the MASQUE tunnel protocol.</p>
<p>The Cloudflare One Client will now send active probes to detect the network path MTU and will update its tunnel interface MTU accordingly. You can expect PMTUD probes to generate an extra 25 Mb/day of traffic coming from the device.</p>
<h2 id="verify-pmtud-is-enabled">Verify PMTUD is enabled</h2>
<p>To check if PMTUD is active on a device, open a terminal and run the following command:</p>
<pre tabindex="0"><code class="language-sh">warp-cli settings | grep -i pmtu&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">(local policy)	PMTUD enabled: true&#10;</code></pre>
<p>If PMTUD is enabled, the output will show <code>PMTUD enabled: true</code>.</p>
<h2 id="minimum-mtus">Minimum MTUs</h2>
<h3 id="recommended-mtu">Recommended MTU</h3>
<p>The Cloudflare One Client requires the following MTUs for full functionality and performance:</p>
<table>
<thead>
<tr>
<th>Device tunnel protocol</th>
<th>IPv4</th>
<th>IPv6</th>
</tr>
</thead>
<tbody>
<tr>
<td>WireGuard</td>
<td>1340 bytes</td>
<td>1360 bytes</td>
</tr>
<tr>
<td>MASQUE</td>
<td>1361 bytes</td>
<td>1381 bytes</td>
</tr>
</tbody>
</table>
<h3 id="path-mtu-discovery">Path MTU Discovery</h3>
<p>For the PMTUD feature to work, the network path must support an MTU of at least 1281 bytes. The 1281 bytes consists of:</p>
<ul>
<li>1200 bytes: Minimum QUIC datagram</li>
<li>53 bytes: WARP MASQUE encapsulation</li>
<li>28 bytes: IP/UDP headers</li>
</ul>
<h3 id="ipv6">IPv6</h3>
<p>To send IPv6 traffic through the Cloudflare One Client, the network path must support an MTU of at least 1361 bytes. The 1361 bytes consists of:</p>
<ul>
<li>1280 bytes: Minimum IPv6 packet size</li>
<li>53 bytes: WARP MASQUE encapsulation</li>
<li>28 bytes: IP/UDP headers</li>
</ul>
<p>If PMTUD is enabled and the MTU is less than 1361 bytes, then the Cloudflare One Client will automatically disable IPv6 on the tunnel interface.</p>
<h3 id="webrtc">WebRTC</h3>
<p>To send WebRTC traffic through the Cloudflare One Client, the network path must support an MTU of at least 1361 bytes. Below 1361 bytes, WebRTC connections will experience progressively degraded performance. This minimum MTU impacts <a href="/cloudflare-one/remote-browser-isolation/">Cloudflare Browser Isolation</a> and any other website that uses WebRTC (such as video conferencing and media streaming services).</p>
<h2 id="check-your-mtu">Check your MTU</h2>
<p>You can check your current network path MTU by collecting <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/">Cloudflare One Client diagnostic logs</a>.</p>
<ol>
<li>Run the <code>warp-diag</code> command on the device or <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#collect-logs-via-the-dashboard">collect logs via the dashboard</a>.</li>
<li>Open the resulting <code>warp-debugging-info-&lt;date&gt;-&lt;time&gt;.zip</code> file.</li>
<li>Open <code>connectivity.txt</code> and search for <code>PMTU</code>.</li>
</ol>
<pre tabindex="0"><code class="language-txt">====================================================================&#10;H3 Quic Connect&#10;====================================================================&#10;&#10;Testing H3 QUIC connectivity to &#x27;https://cloudflare-quic.com/cdn-cgi/l4-stats&#x27; result: Successful&#10;IPv4:&#10;&quot;&#10;Headers:&#10;	server address=104.18.26.14:443&#10;	...&#10;&#10;Body:&#10;	transport=TCP&#10;	...&#10;&#10;PMTU:&#10;	1500 bytes&#10;&quot;&#10;</code></pre>
<p>The example above shows an MTU of 1500 bytes, which meets the <a href="#recommended-mtu">recommended MTU requirements</a> for the Cloudflare One Client. If your MTU falls below the recommended threshold, consider <a href="#enable-path-mtu-discovery">enabling Path MTU Discovery</a> to optimize connection performance.</p>
