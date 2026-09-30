---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers-vpc/
  description: '2026-06-16'
  full_title: workers-vpc changelog | Cloudflare Docs
  head_html: <title>workers-vpc changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-16"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers-vpc/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers-vpc changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-16"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers-vpc/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers-vpc/#page","headline":"workers-vpc changelog | Cloudflare Docs","description":"2026-06-16","url":"https://developers.cloudflare.com/changelog/product/workers-vpc/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers-vpc/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="tcp-connections-via-connect-over-vpc-networks"><a href="/changelog/post/2026-06-16-tcp-connect-vpc-networks/">TCP connections via connect() over VPC Networks</a></h2>
<p><em>2026-06-16</em></p>
<p><a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings now support the <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> Socket API for raw TCP connections to private destinations, in addition to HTTP traffic via <code>fetch()</code>.</p>
<p>This means Workers can now open TCP sockets to any private service reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp — Redis, Memcached, MQTT, custom binary protocols, or any other TCP-based service.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17828.md")</div>
<p>At runtime, use <code>connect()</code> on the binding to open a TCP socket to a private destination:</p>
<pre tabindex="0"><code class="language-ts">export default {&#10;	async fetch(request: Request, env: Env) {&#10;		// Open a TCP connection to a private Redis instance&#10;		const socket = await env.PRIVATE_NETWORK.connect(&quot;10.0.1.50:6379&quot;);&#10;&#10;		// Write a Redis PING command&#10;		const writer = socket.writable.getWriter();&#10;		await writer.write(new TextEncoder().encode(&quot;PING\r\n&quot;));&#10;		await writer.close();&#10;&#10;		return new Response(socket.readable);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17827.md")</aside>
<p>For more details, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> and the <a href="/workers-vpc/api/">Workers Binding API</a>.</p>


<h2 id="filter-workers-public-internet-traffic-using-gateway-policies"><a href="/changelog/post/2026-06-05-gateway-egress/">Filter Workers' public Internet traffic using Gateway policies</a></h2>
<p><em>2026-06-05</em></p>
<p>Workers using a <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> binding with <code>network_id: &quot;cf1:network&quot;</code> now egress to public Internet destinations through <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>. This means your existing Zero Trust traffic policies — DNS, HTTP, Network, and egress — extend to traffic that originates from your Workers, the same way they do for WARP users today.</p>
<div class="nb-interactive-component" data-cf-component="WorkersVPCEgressDiagram"></div>
<p>What you get by default:</p>
<ul>
<li><strong>Visibility.</strong> Worker egress shows up in Gateway <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> logs alongside your other traffic, so you can audit what your Workers are calling and when.</li>
<li><strong>Enforcement.</strong> Any existing Gateway policy whose selectors match a Worker request will apply — including allow / block lists, DNS category filtering, and HTTP destination rules. If you have already blocked a category for your workforce, your Workers inherit that block.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17825.md")</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17826.md")</div>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>. For policy authoring, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway traffic policies</a>.</p>


<h2 id="reach-cloudflare-wan-destinations-from-workers-vpc"><a href="/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/">Reach Cloudflare WAN destinations from Workers VPC</a></h2>
<p><em>2026-05-21</em></p>
<p>You can now use <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings with <code>network_id: &quot;cf1:network&quot;</code> to reach your full private network from Workers, including:</p>
<ul>
<li><a href="/mesh/">Cloudflare Mesh</a> nodes and client devices</li>
<li>Subnet routes and hostname routes announced through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or Cloudflare Mesh</li>
<li>Destinations connected through <a href="/cloudflare-wan/">Cloudflare WAN</a> on-ramps — GRE, IPsec, and CNI</li>
</ul>
<p>This means a single VPC Network binding can route Worker requests to private services regardless of how those services are connected to Cloudflare: through a Cloudflare Tunnel from a cloud VPC, a Mesh node on a private subnet, or a Cloudflare WAN on-ramp from your data center or branch site.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17824.md")</div>
<p>At runtime, the URL you pass to <code>fetch()</code> determines the destination:</p>
<pre tabindex="0"><code class="language-js">// Reach a service behind a Cloudflare WAN IPsec on-ramp&#10;const response = await env.PRIVATE_NETWORK.fetch(&quot;http://10.50.0.100:8080/api&quot;);&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17823.md")</aside>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>.</p>


<h2 id="vpc-networks-and-cloudflare-mesh-support-now-in-public-beta"><a href="/changelog/post/2026-04-14-vpc-networks/">VPC Networks and Cloudflare Mesh support now in public beta</a></h2>
<p><em>2026-04-14</em></p>
<p><a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings now give your Workers access to any service in your private network without pre-registering individual hosts or ports. This complements existing <a href="/workers-vpc/configuration/vpc-services/">VPC Service</a> bindings, which scope each binding to a specific host and port.</p>
<p>You can bind to a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> by <code>tunnel_id</code> to reach any service on the network where that tunnel is running, or bind to your <a href="/mesh/">Cloudflare Mesh</a> network using <code>cf1:network</code> to reach any Mesh node, client device, or subnet route in your account:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17822.md")</div>
<p>At runtime, <code>fetch()</code> routes through the network to reach the service at the IP and port you specify:</p>
<pre tabindex="0"><code class="language-js">const response = await env.MESH.fetch(&quot;http://10.0.1.50:8080/api/data&quot;);&#10;</code></pre>
<p>For configuration options and examples, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> and <a href="/workers-vpc/examples/connect-to-cloudflare-mesh/">Connect Workers to Cloudflare Mesh</a>.</p>


<h2 id="observability-for-workers-vpc-services"><a href="/changelog/post/2026-03-20-metrics-and-settings-dashboard/">Observability for Workers VPC Services</a></h2>
<p><em>2026-03-20</em></p>
<p>Each VPC Service now has a <strong>Metrics</strong> tab so you can monitor connection health and debug failures without leaving the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers-vpc/2026-03-20-metrics-dashboard.png" alt="Workers VPC Metrics dashboard showing connections, latency, and errors charts" /></p>
<ul>
<li><strong>Connections</strong> — See successful and failed connections over time, broken down by what is responsible: your origin (Bad Upstream), your configuration (Client), or Cloudflare (Internal).</li>
<li><strong>Latency</strong> — Track connection and DNS resolution latency trends.</li>
<li><strong>Errors</strong> — Drill into specific error codes grouped by category, with filters to isolate upstream, client, or internal failures.</li>
</ul>
<p>You can also view and edit your VPC Service configuration, host details, and port assignments from the <strong>Settings</strong> tab.</p>
<p>For a full list of error codes and what they mean, refer to <a href="/workers-vpc/reference/troubleshooting/">Troubleshooting</a>.</p>


<h2 id="origin-ca-certificate-support-for-workers-vpc"><a href="/changelog/post/2026-02-13-origin-ca-certificate-support/">Origin CA certificate support for Workers VPC</a></h2>
<p><em>2026-02-13</em></p>
<p>Workers VPC now supports <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificates</a> when connecting to your private services over HTTPS. Previously, Workers VPC only trusted certificates issued by publicly trusted certificate authorities (for example, Let's Encrypt, DigiCert).</p>
<p>With this change, you can use free Cloudflare Origin CA certificates on your origin servers within private networks and connect to them from Workers VPC using the <code>https</code> scheme. This is useful for encrypting traffic between the tunnel and your service without needing to provision certificates from a public CA.</p>
<p>For more information, refer to <a href="/workers-vpc/configuration/vpc-services/#supported-tls-certificates">Supported TLS certificates</a>.</p>


<h2 id="announcing-workers-vpc-services-beta"><a href="/changelog/post/2025-09-25-workers-vpc/">Announcing Workers VPC Services (Beta)</a></h2>
<p><em>2025-11-05</em></p>
<p><strong>Workers VPC Services</strong> is now available, enabling your Workers to securely access resources in your private networks, without having to expose them on the public Internet.</p>
<h4 id="2025-09-25-workers-vpc-what-s-new">What's new</h4>
<ul>
<li><strong>VPC Services</strong>: Create secure connections to internal APIs, databases, and services using familiar Worker binding syntax</li>
<li><strong>Multi-cloud Support</strong>: Connect to resources in private networks in any external cloud (AWS, Azure, GCP, etc.) or on-premise using Cloudflare Tunnels</li>
</ul>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// Perform application logic in Workers here&#10;&#10;		// Sample call to an internal API running on ECS in AWS using the binding&#10;		const response = await env.AWS_VPC_ECS_API.fetch(&quot;https://internal-host.example.com&quot;);&#10;&#10;		// Additional application logic in Workers&#10;		return new Response();&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-09-25-workers-vpc-getting-started">Getting started</h4>
<p>Set up a Cloudflare Tunnel, create a VPC Service, add service bindings to your Worker, and access private resources securely. <a href="/workers-vpc/">Refer to the documentation</a> to get started.</p>



