---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/
  description: Reference information for Traceroute test in Zero Trust analytics.
  full_title: Traceroute test · Cloudflare One docs
  head_html: <title>Traceroute test · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Traceroute test in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/index.md"><meta property="og:title" content="Traceroute test · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Traceroute test in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Windows,MacOS,Android"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/#page","headline":"Traceroute test \u00b7 Cloudflare One docs","description":"Reference information for Traceroute test in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Windows","MacOS","Android"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/tests/traceroute/
  schema: 1
---
<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/4973.md")
</div></details>
<p>A traceroute test measures the network path of an IP packet from an end-user device to a server. The packet passes through a series of intermediate routers — each called a &quot;hop&quot; — and the test records the response time and packet loss at each one. You can use the results to troubleshoot network issues by identifying which hop along the path is causing increased latency or dropped packets.</p>
<h2 id="create-a-test">Create a test</h2>
<p>To set up a traceroute test for an application:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Select <strong>Add a Test</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Name</strong>: Enter any name for the test.</li>
<li><strong>Target</strong>: Enter the IP address of the server you want to test (for example, <code>192.0.2.0</code>). You can test either a public-facing endpoint or a private endpoint you have connected to Cloudflare.</li>
<li><strong>Source device profiles</strong>: (Optional) Select the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a> that you want to run the test on. A device profile defines Cloudflare One Client settings for a specific set of devices in your organization. If no profiles are selected, the test will run on all supported devices connected to your Zero Trust organization.</li>
<li><strong>Test type</strong>: Select <em>Traceroute</em>.</li>
<li><strong>Test frequency</strong>: Specify how often the test will run. Input a minute value between 5 and 60.</li>
</ul>
</li>
<li>Select <strong>Add test</strong>.</li>
</ol>
<p>Next, <a href="/cloudflare-one/insights/dex/tests/view-results/">view the results</a> of your test.</p>
<h2 id="test-results">Test results</h2>
<p>A traceroute test measures the following data:</p>
<table>
<thead>
<tr>
<th>Data</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Network path</td>
<td>IP address, average response time, and packet loss for each hop (router) between the device and the target. This is the core traceroute data — it maps the route your traffic takes.</td>
</tr>
<tr>
<td>Round trip time</td>
<td>Time, in milliseconds, between sending out a packet and receiving a response from the target. This is the end-to-end latency measurement.</td>
</tr>
<tr>
<td>Number of hops</td>
<td>Number of routers encountered between the device and the target.</td>
</tr>
<tr>
<td>Packet loss</td>
<td>Percentage of IP packets that failed to receive a response.</td>
</tr>
<tr>
<td>Availability</td>
<td>Percentage of tests where at least one packet reached the destination. A value below 100% means the destination was completely unreachable during some test runs.</td>
</tr>
<tr>
<td>Last seen ISP</td>
<td>The Internet Service Provider that is managing the connection from the device to Cloudflare. (Only available on macOS and Windows.) <br/> <br/> DEX looks up the IP address of the ISP in a geolocation database and returns the corresponding <a href="https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/">ASO (Autonomous System Organization) and ASN (Autonomous System Number)</a>. If the ASO and ASN are <code>Unknown</code>, it means this information is unavailable in the geolocation data provider.</td>
</tr>
</tbody>
</table>
<h2 id="export-dex-application-test-logs">Export DEX application test logs</h2>
<p>You can use <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> to export <a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX application test</a> data to <a href="/r2/">R2</a> (Cloudflare's object storage), a third-party cloud storage bucket, or a Security Information and Event Management (SIEM) tool. This is useful if you need to retain test data beyond the <a href="/cloudflare-one/insights/logs/#log-retention">7-day log retention period</a> or correlate DEX data with other log sources.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/insights/dex/rules/">DEX rules</a> - Define which users or groups a test applies to, using selectors such as user email, user group, operating system, or managed network.</li>
</ul>
