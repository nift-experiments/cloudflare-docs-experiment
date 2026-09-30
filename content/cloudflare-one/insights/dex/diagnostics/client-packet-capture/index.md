---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/
  description: Feature documentation for Cloudflare One client packet captures.
  full_title: Client packet capture · Cloudflare One docs
  head_html: <title>Client packet capture · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Feature documentation for Cloudflare One client packet captures."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/index.md"><meta property="og:title" content="Client packet capture · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Feature documentation for Cloudflare One client packet captures."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#page","headline":"Client packet capture \u00b7 Cloudflare One docs","description":"Feature documentation for Cloudflare One client packet captures.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/diagnostics/client-packet-capture/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/diagnostics/client-packet-capture/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/4976.md")
</div></details>
<p>Remote captures allow administrators to collect packet captures (PCAPs) and Cloudflare One Client diagnostic logs directly from end user devices. A packet capture is a recording of network traffic at the packet level. This data can be used to troubleshoot network problems, investigate security incidents, and identify performance bottlenecks.</p>
<h2 id="start-a-remote-capture">Start a remote capture</h2>
<div class="nb-data-component" data-cf-component="Render"></div>
<h2 id="check-remote-capture-status">Check remote capture status</h2>
<p>To view a list of captures, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong> &gt; <strong>Diagnostics</strong>. The <strong>Status</strong> column displays one of the following options:</p>
<ul>
<li><strong>Success</strong>: The capture is complete and ready for download. Any partially successful captures will still upload to Cloudflare. For example, there could be a scenario where the PCAP succeeds on the primary network interface but fails on the WARP tunnel interface. You can <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#download-remote-captures">review PCAP results</a> to determine which PCAPs succeeded or failed.</li>
<li><strong>Running</strong>: The capture is in progress on the device.</li>
<li><strong>Pending Upload</strong>: The capture is complete but not yet ready for download.</li>
<li><strong>Failed</strong>: The capture has either timed out or encountered an error. To retry the capture, check the Cloudflare One Client version and <a href="/cloudflare-one/insights/dex/monitoring/#fleet-status">connectivity status</a>, then start a <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/#start-a-remote-capture">new capture</a>.</li>
</ul>
<h2 id="download-remote-captures">Download remote captures</h2>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>DEX</strong> &gt; <strong>Remote captures</strong>.</li>
<li>Find a successful capture.</li>
<li>Select the three-dot menu and select <strong>Download</strong>.</li>
</ol>
<p>This will download a ZIP file to your local machine called <code>&lt;capture-id&gt;.zip</code>. DEX will store capture data according to our <a href="/cloudflare-one/insights/logs/#log-retention">log retention policy</a>.</p>
<h3 id="device-pcap-contents">Device PCAP contents</h3>
<p>The downloaded PCAP folder contains three files:</p>
<ul>
<li><code>capture-default.pcap</code>: Packet captures for the primary network interface.</li>
<li><code>capture-tunnel.pcap</code>: Packet captures for traffic inside of the WARP tunnel.</li>
<li><code>results.json</code>: Reports successful and failed packet captures.</li>
</ul>
<p>You can analyze <code>.pcap</code> files using Wireshark or another third-party packet capture tool.</p>
<h3 id="diagnostic-log-files">Diagnostic log files</h3>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs">Cloudflare One Client diagnostic logs</a> for a description of each file.</p>
<h2 id="diagnostics-analyzer-beta">Diagnostics analyzer (beta)</h2>
<p>The diagnostics analyzer highlights what Cloudflare determines to be the most important detection events in a <code>warp-diag</code> log. You can use the detection report to help parse your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#warp-diag-logs">log files</a> and identify the root cause of client issues. The diagnostics analyzer is only available for logs <a href="#collect-logs-via-the-dashboard">collected via the dashboard</a>.</p>
<p>To access the diagnostics analyzer:</p>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>DEX</strong> &gt; <strong>Remote captures</strong>.</p>
</li>
<li>
<p>Locate an existing <code>warp-diag</code> log from the list or select <strong>Run diagnostics</strong> to generate a new <code>warp-diag</code> log.</p>
</li>
<li>
<p>Select the three dots for the <code>warp-diag</code> log that you want to analyze, then select <strong>View Device Diag</strong>.</p>
<p>The <strong>Overview</strong> tab will display an <a href="/fundamentals/reference/cloudy-ai-agent/">AI-generated summary</a> of the results, a list of detection events, and basic device information.</p>
 <details class="nb-details"><summary>Explanation of the fields</summary><div class="nb-details-body">
</li>
</ol>
@input("content/.markup/bodies/4977.md")
</div></details>
4. Select a detection type for more information about the event and recommended next steps.
<p>Cloudflare DEX will store the <code>warp-diag</code> log and its detection report per our <a href="/cloudflare-one/insights/logs/#log-retention">log retention policy</a>. To save a copy onto your local machine, <a href="#download-remote-captures">download the log file</a> and go to the <strong>JSON file</strong> tab to copy the report in JSON format.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Packet captures are subject to the following limits:</li>
</ul>
<table>
<thead>
<tr>
<th>Limit Type</th>
<th>Maximum Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Time limit</td>
<td>600 seconds</td>
</tr>
<tr>
<td>File size</td>
<td>50 MB</td>
</tr>
<tr>
<td>Packet size</td>
<td>1500 bytes</td>
</tr>
</tbody>
</table>
<ul>
<li>
<p>Cloudflare One Client diagnostic logs have no file size limit, but files larger than 100 MB cannot be uploaded to Cloudflare and must be shared directly with the admin.</p>
</li>
<li>
<p>Windows devices do not support concurrent remote captures. If you start a remote capture while another is in progress, the second capture will fail immediately.</p>
</li>
<li>
<p>PCAPs will fail on Windows if you have another third-party packet capture tool (such as, Packet Monitor <code>pktmon</code>) running.</p>
</li>
<li>
<p>On Windows, packet captures may fail on devices configured with a non-English language due to limitations with the underlying <code>PktMon</code> tool.</p>
</li>
</ul>
