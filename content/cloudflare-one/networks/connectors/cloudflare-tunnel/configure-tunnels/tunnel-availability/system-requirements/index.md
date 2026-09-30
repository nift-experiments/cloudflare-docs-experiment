---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/
  description: How System requirements works in Zero Trust networking.
  full_title: System requirements · Cloudflare One docs
  head_html: <title>System requirements · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How System requirements works in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/index.md"><meta property="og:title" content="System requirements · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How System requirements works in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TCP,UDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/#page","headline":"System requirements \u00b7 Cloudflare One docs","description":"How System requirements works in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TCP","UDP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/
  schema: 1
---
<p>Our connector, <code>cloudflared</code>, was designed to be lightweight and flexible enough to be effectively deployed on Raspberry Pi, your laptop or a server in a data center.
Unlike legacy VPNs where throughput is determined by the server's memory, CPU and other hardware specifications, Cloudflare Tunnel throughput is primarily limited by the number of ports configured in system software. Therefore, when sizing your <code>cloudflared</code> server, the most important element is sizing the available ports on the machine to reflect the expected throughput of TCP and UDP traffic.</p>
<h2 id="recommendations">Recommendations</h2>
<p>For most use cases, we recommend the following baseline configuration:</p>
<ul>
<li>Run a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflared-replicas"><code>cloudflared</code> replica</a> on two dedicated host machines per network location. Using two hosts enables server-side redundancy.</li>
<li>Size each host with minimum 4GB of RAM and 4 CPU cores.</li>
<li>Allocate 50,000 <a href="#number-of-ports">ports</a> to the <code>cloudflared</code> process on each host.</li>
</ul>
<p>This setup is usually sufficient to handle traffic from 8,000 Cloudflare One Client users (4,000 per host). The actual amount of resources used by <code>cloudflared</code> will depend on many variables, including the number of requests per second, bandwidth, network path and hardware. As additional users are onboarded, or if network traffic increases beyond your existing <a href="#estimated-throughput">tunnel capacity</a>, you can scale your tunnel by adding an additional <code>cloudflared</code> host in that location.</p>
<h3 id="number-of-ports">Number of ports</h3>
<p>When <code>cloudflared</code> receives a request from a device, it uses the ports on the host machine to evaluate and forward the request to your origin service. Every machine by system design is hardware-limited to a maximum 65,535 ports. Additionally, each service on the machine has a limited number of ports that it can consume. For this reason, we recommend the following deployment model:</p>
<ul>
<li><code>cloudflared</code> should be deployed on a dedicated host machine. This model is typically appropriate, but there may be serverless or clustered workflows where a dedicated host is not possible.</li>
<li>The host machine should allocate 50,000 ports to be available for use by the <code>cloudflared</code> service. The remaining ports are reserved for system administrative processes.</li>
</ul>
<hr />
<hr />
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5376.md")
</div></div>
<h3 id="private-dns">Private DNS</h3>
<p>DNS queries utilize <a href="#estimated-throughput">more system resources</a> compared to TCP and non-DNS UDP requests. To optimize service availability, Cloudflare recommends splitting <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/">private DNS traffic</a> into its own Cloudflare Tunnel. The tunnel should run on a dedicated host and only include routes for your internal DNS resolver IPs.</p>
<h3 id="ulimits">ulimits</h3>
<hr />
<hr />
<p>On Linux and macOS, <code>ulimit</code> settings determine the system resources available to a logged-in user. We recommend configuring the following ulimits on the <code>cloudflared</code> server:</p>
<table>
<thead>
<tr>
<th>ulimit</th>
<th>Description</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>-n</code></td>
<td>Maximum number of open files or file descriptors</td>
<td>≥ 70,000</td>
</tr>
</tbody>
</table>
<p>To view your current ulimits, open a terminal and run:</p>
<pre tabindex="0"><code class="language-sh">ulimit -a&#10;</code></pre>
<p>To set the open files <code>ulimit</code>:</p>
<pre tabindex="0"><code class="language-sh">ulimit -n 70000&#10;</code></pre>
<p>The command above sets the open files limit only for the current terminal session and will not persist after a reboot or new login. To apply this limit permanently, configure it using the persistent method appropriate for your operating system.</p>
<h2 id="estimated-throughput">Estimated throughput</h2>
<p>Most private network traffic proxied by <code>cloudflared</code> falls in one of two categories:</p>
<ul>
<li>TCP requests (more common, less resource intensive)</li>
<li>UDP requests (less common, more resource intensive)</li>
</ul>
<p>TCP traffic uses and releases ports almost instantaneously. This means that in order to overload a <code>cloudflared</code> instance with 50,000 available ports, your organization would need to continuously generate 50,001 TCP requests per second.</p>
<p>UDP traffic is more unique. DNS queries - usually the bulk of UDP traffic - are held by ports in <code>cloudflared</code> for five seconds. Non-DNS UDP traffic holds each port for the duration of the connection, which can be any amount of time. This means that in order to overload a <code>cloudflared</code> instance with 50,000 available ports, you would need to continuously generate either 10,000 DNS queries to your private resolver per second, or a cumulative 50,000 non-DNS UDP requests over a shorter time than your connection reset rate.</p>
<h3 id="calculate-your-tunnel-capacity">Calculate your tunnel capacity</h3>
<p>Our <a href="#recommendations">baseline recommendations</a> serve as a starting point for a Cloudflare Tunnel deployment. Once you have a representative population of users engaging with your network for at least a week, you can customize tunnel sizing according to your own traffic patterns.</p>
<p>To calculate your tunnel capacity:</p>
<ol>
<li>Set up a <a href="/cloudflare-one/tutorials/grafana/">metrics service</a> when you run the tunnel.</li>
<li>After a week or so, query the following <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/#cloudflared-metrics">tunnel metrics</a>:
<ul>
<li><code>cloudflared_tcp_total_sessions</code></li>
<li><code>cloudflared_udp_total_sessions</code></li>
</ul>
</li>
<li>Compute the average <strong>TCP requests per second</strong> and <strong>Non-DNS UDP requests per second</strong> by dividing total sessions by total time.</li>
<li>In your private DNS resolver, obtain the average <strong>Private DNS requests per second</strong>.</li>
<li>Input your values into our sizing calculator:</li>
</ol>
<div class="nb-interactive-component" data-cf-component="TunnelCalculator"><h3 id="system-configuration">System configuration</h3><p>Enter the number of cloudflared replicas and available processor cores.</p><h3 id="metrics">Metrics</h3><p>Provide expected requests, bandwidth, and concurrent connections.</p><h3 id="result">Result</h3><p>Use the estimated throughput to calculate your tunnel capacity.</p></div>
<p>You can use these results to determine if your tunnel is appropriately sized. To increase your tunnel capacity, add identical host machines running <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/#cloudflared-replicas"><code>cloudflared</code> replicas</a>.</p>
