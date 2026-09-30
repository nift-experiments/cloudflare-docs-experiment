---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/monitors/
  description: Health monitors that check origin server availability.
  full_title: Monitors · Cloudflare Load Balancing docs
  head_html: <title>Monitors · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Health monitors that check origin server availability."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/monitors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/monitors/index.md"><meta property="og:title" content="Monitors · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Health monitors that check origin server availability."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/monitors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/monitors/#page","headline":"Monitors \u00b7 Cloudflare Load Balancing docs","description":"Health monitors that check origin server availability.","url":"https://developers.cloudflare.com/load-balancing/monitors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/monitors/
  schema: 1
---
<div class="nb-glossary-definition"><p>A monitor issues health monitor requests at regular intervals to evaluate the health of each endpoint within a <a href="/load-balancing/pools/">pool</a>.</p>
<p>When a pool <a href="/load-balancing/understand-basics/health-details/">becomes unhealthy</a>, your load balancer takes that pool out of the endpoint rotation.</p></div>
<pre tabindex="0"><code class="language-mermaid">    flowchart RL&#10;      accTitle: Load balancing monitor flow&#10;      accDescr: Monitors issue health monitor requests, which validate the current status of servers within each pool.&#10;      Monitor -- Health Monitor ----&gt; Endpoint2&#10;      Endpoint2 -- Response ----&gt; Monitor&#10;      subgraph Pool&#10;      Endpoint1((Endpoint 1))&#10;      Endpoint2((Endpoint 2))&#10;      end&#10;</code></pre>
<p>Health monitor requests that result in a status change for an endpoint are recorded as events in the Load Balancing event logs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10375.md")
</aside>
<hr />
<h2 id="properties">Properties</h2>
<p>For an up-to-date list of monitor properties, refer to <a href="/api/resources/load_balancers/subresources/monitors/methods/list/">Monitor properties</a> in our API documentation.</p>
<hr />
<h2 id="create-monitors">Create monitors</h2>
<p>For step-by-step guidance, refer to <a href="/load-balancing/monitors/create-monitor/">Create monitors</a>.</p>
<h3 id="monitor-groups">Monitor Groups</h3>
<p>Monitor Groups let you combine multiple health monitors into a single logical group to create more accurate, intelligent health checks for your applications. By aggregating results from several monitors, you can better reflect real application health and improve traffic steering resilience. For more details, refer to the <a href="/load-balancing/monitors/monitor-groups/">Monitor Groups</a> documentation page.</p>
<hr />
<h2 id="health-monitor-regions">Health monitor regions</h2>
<p>When you <a href="/load-balancing/monitors/create-monitor/#create-a-monitor">attach a monitor to a pool</a>, you can select multiple regions to increase reporting accuracy.</p>
<p>For each option selected in a pool's <strong>Health Monitor Regions</strong>, Cloudflare sends health monitor requests from three separate data centers in that region.</p>
<p><img src="/assets/upstream/images/load-balancing/health-check-component.png" alt="Health monitor requests come from three data centers within each selected region." /></p>
<p>If the majority of data centers for that region pass the health monitor requests, that region is considered healthy. If the majority of regions is healthy, then the endpoint itself will be considered healthy.</p>
<h3 id="configurations">Configurations</h3>
<p><strong>All Data Centers (Enterprise only)</strong></p>
<p>Health monitor probes are sent from every single data center in Cloudflare’s network to the endpoints within the associated pool. This allows probes to hit each endpoint during intervals set by the customer.</p>
<p><strong>All Regions (Enterprise only)</strong></p>
<p>Three health monitor probes per region are sent to each endpoint in the associated pool. There are a total of 13 regions, resulting in 39 probes.</p>
<p><strong>Regional</strong></p>
<p>Three health monitor probes are sent from each specified region within the pool configuration.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10374.md")
</aside>
<hr />
<h2 id="ipv4-and-ipv6-probe-behavior">IPv4 and IPv6 probe behavior</h2>
<p>Health monitor probes use IPv4 by default. IPv6 probes are only sent if the endpoint address has no <code>A</code> records (only <code>AAAA</code>). Each endpoint receives one probe per interval — Cloudflare does not probe both IPv4 and IPv6 for the same endpoint.</p>
<p>To enforce probing over IPv6, set the endpoint address to either a raw IPv6 address or a hostname that only has <code>AAAA</code> records.</p>
<hr />
<h2 id="host-header-prioritization">Host header prioritization</h2>
<p>The host headers used on health monitor requests can be configured either <a href="/load-balancing/monitors/create-monitor/">on the monitor itself</a> or on the <a href="/load-balancing/pools/create-pool/">endpoints within a pool</a>.</p>
<p>When a host header is specified both on the monitor and on the endpoint, the host header configured on the endpoint takes precedence over the host header configured on the monitor.</p>
<p>When no host header is specified, Cloudflare uses the <strong>Endpoint Address</strong> configured on the endpoints as the host header for the health monitor requests.</p>
<p>For more details, refer to <a href="/load-balancing/additional-options/override-http-host-headers/">Override HTTP Host headers</a>.</p>
<hr />
<h2 id="api-commands">API commands</h2>
<p>The Cloudflare API supports the following commands for monitors. Examples are given for user-level endpoint but apply to the account-level endpoint as well.</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Method</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/load_balancers/subresources/monitors/methods/create/">Create Monitor</a></td>
<td><code>POST</code></td>
<td><code>accounts/:account_id/load_balancers/monitors</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/monitors/methods/delete/">Delete Monitor</a></td>
<td><code>DELETE</code></td>
<td><code>accounts/:account_id/load_balancers/monitors/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/monitors/methods/list/">List Monitors</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/load_balancers/monitors</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/monitors/methods/get/">Monitor Details</a></td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/load_balancers/monitors/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/monitors/methods/edit/">Overwrite specific properties</a></td>
<td><code>PATCH</code></td>
<td><code>accounts/:account_id/load_balancers/monitors/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/monitors/methods/update/">Overwrite existing monitor</a></td>
<td><code>PUT</code></td>
<td><code>accounts/:account_id/load_balancers/monitors/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/subresources/monitors/subresources/previews/methods/create/">Preview Monitor</a></td>
<td><code>POST</code></td>
<td><code>accounts/:account_id/load_balancers/monitors/:id/preview</code></td>
</tr>
</tbody>
</table>
<h2 id="supported-protocols">Supported protocols</h2>
<p>The following table summarizes the different types of monitors available in Cloudflare Load Balancing, their monitoring types, and how each health check process evaluates the success criteria to determine endpoint health:</p>
<table>
<thead>
<tr>
<th>Monitor type</th>
<th>Monitoring type</th>
<th>Description</th>
<th>Health check process</th>
<th>Success criteria</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP/HTTPS</td>
<td>Public and private</td>
<td>Used for HTTP and HTTPS endpoints with specific protocol attributes.</td>
<td>The probe is configured with settings and success criteria such as Method, Simulate Zone, Follow Redirects, Request Headers, and Response Body. The probe then evaluates the configured success criteria using the HTTP protocol. Throughout the configured timeout period, the TCP connection is kept active using <a href="/fundamentals/reference/tcp-connections/#tcp-connections-and-keep-alives">keep-alives</a>, even if no response is received.</td>
<td>Success is based on meeting the configured HTTP success criteria. No response within the configured timeout and retries is considered unhealthy.</td>
</tr>
<tr>
<td>TCP</td>
<td>Public and private</td>
<td>Checks TCP connectivity by attempting to open a connection to the endpoint.</td>
<td>The monitor sends a TCP SYN message to the specified port. A successful health check requires receiving a SYN/ACK message to establish the connection. The connection is closed by sending a FIN or RST packet, or by receiving a FIN packet from the endpoint.</td>
<td>Failure to establish a TCP connection within the configured timeout and retries is considered unhealthy.</td>
</tr>
<tr>
<td>ICMP Ping</td>
<td>Public and Tunnel</td>
<td>Confirms basic Layer 3 (L3) connectivity to the endpoint using ICMP. The endpoints need to be allowed to reply to ICMP packets and any intervening networking equipment must support ICMP.</td>
<td>The monitor sends an ICMP/ICMPv6 echo request (ping) and expects an ICMP/ICMPv6 echo reply from the endpoint.</td>
<td>The endpoint must reply to the ICMP ping within the configured timeout and retries to be considered healthy.</td>
</tr>
<tr>
<td>UDP-ICMP</td>
<td>Public and Tunnel</td>
<td>UDP-ICMP monitor works by sending a UDP probe packet after ICMP Ping monitor completes as healthy.</td>
<td>After receiving a successful ICMP reply, the monitor sends a UDP probe packet to the endpoint. If no ICMP Port Unreachable message is received, the endpoint is considered healthy.</td>
<td>If the monitor receives an ICMP Port Unreachable message within the configured timeout and retries, the endpoint is considered unhealthy.</td>
</tr>
<tr>
<td>SMTP</td>
<td>Public</td>
<td>Verifies SMTP availability at the application layer.</td>
<td>The monitor establishes a TCP connection and sends an SMTP HELO command. It expects a reply with code 250. The monitor then sends an SMTP QUIT command, expecting a reply with code 221. At the end of each interval, the TCP connection is closed by sending a TCP FIN packet.</td>
<td>The endpoint must respond with correct SMTP codes (250 for HELO, 221 for QUIT) within the configured timeout and retries to be considered healthy.</td>
</tr>
</tbody>
</table>
