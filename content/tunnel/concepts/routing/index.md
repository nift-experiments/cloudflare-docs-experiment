---
cp9:
  canonical: https://developers.cloudflare.com/tunnel/concepts/routing/
  description: Route traffic to private networks and services through Cloudflare Tunnel.
  full_title: Routing · Cloudflare Docs
  head_html: <title>Routing · Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="Route traffic to private networks and services through Cloudflare Tunnel."><link rel="canonical" href="https://developers.cloudflare.com/tunnel/concepts/routing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/tunnel/concepts/routing/index.md"><meta property="og:title" content="Routing · Cloudflare Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route traffic to private networks and services through Cloudflare Tunnel."><meta property="og:url" content="https://developers.cloudflare.com/tunnel/concepts/routing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Tunnel"><meta name="algolia_product_filter" content="Cloudflare Tunnel"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Tunnel"><meta name="pcx_tags" content="DNS,WebSockets"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/tunnel/concepts/routing/#page","headline":"Routing \u00b7 Cloudflare Docs","description":"Route traffic to private networks and services through Cloudflare Tunnel.","url":"https://developers.cloudflare.com/tunnel/concepts/routing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS","WebSockets"]}</script>
  markdown: true
  noindex: false
  route: /tunnel/concepts/routing/
  schema: 1
---
<p>Cloudflare Tunnel routes traffic from Cloudflare's network to services running behind <code>cloudflared</code>. When you <a href="/tunnel/get-started/#publish-an-application">publish an application</a>, you map a public hostname to a local service — for example, <code>app.example.com</code> to <code>http://localhost:8080</code> — and Cloudflare applies CDN caching, WAF, and DDoS protection before forwarding the request to your origin.</p>
<p><img src="/assets/upstream/images/reference-architecture/cloudflare-one-reference-architecture-images/cf1-ref-arch-7.svg" alt="Multiple outbound connections from cloudflared are spread across Cloudflare data centers for reliability and failover." /></p>
<h2 id="published-applications">Published applications</h2>
<p>A published application is a hostname-to-service mapping defined in your tunnel configuration. Each mapping tells <code>cloudflared</code> which local service should receive traffic for a given public hostname.</p>
<p>You can publish multiple applications on a single tunnel. For each application, specify:</p>
<ul>
<li><strong>Public hostname</strong> — The domain or subdomain that users visit (for example, <code>app.example.com</code>).</li>
<li><strong>Service</strong> — The local address or socket where the application is running (for example, <code>http://localhost:8080</code>).</li>
</ul>
<p>When you add a route through the dashboard, Cloudflare automatically creates a DNS record pointing the hostname to your tunnel subdomain (<code>&lt;UUID&gt;.cfargotunnel.com</code>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14964.md")
</aside>
<h2 id="supported-protocols">Supported protocols</h2>
<p>The table below lists the service types you can route to a public hostname. Non-HTTP services require <a href="/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/">installing <code>cloudflared</code> on the client</a> for end users to connect.</p>
<table>
<thead>
<tr>
<th>Service type</th>
<th>Description</th>
<th>Example <code>service</code> value</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP</td>
<td>Proxies incoming HTTPS requests to your local web service over HTTP.</td>
<td><code>http://localhost:8000</code></td>
</tr>
<tr>
<td>HTTPS</td>
<td>Proxies incoming HTTPS requests directly to your local web service. You can <a href="/tunnel/reference/origin-parameters/#notlsverify">disable TLS verification</a> for self-signed certificates.</td>
<td><code>https://localhost:8000</code></td>
</tr>
<tr>
<td>UNIX</td>
<td>Same as HTTP, but uses a Unix socket.</td>
<td><code>unix:/home/production/echo.sock</code></td>
</tr>
<tr>
<td>UNIX + TLS</td>
<td>Same as HTTPS, but uses a Unix socket.</td>
<td><code>unix+tls:/home/production/echo.sock</code></td>
</tr>
<tr>
<td>TCP</td>
<td>Streams TCP over a WebSocket connection. End users run <code>cloudflared access tcp</code> to <a href="/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/arbitrary-tcp/">connect</a>. For long-lived connections, use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Client-to-Tunnel</a> instead.</td>
<td><code>tcp://localhost:2222</code></td>
</tr>
<tr>
<td>SSH</td>
<td>Streams SSH over a WebSocket connection. End users run <code>cloudflared access ssh</code> to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-cloudflared-authentication/">connect</a>. For long-lived connections, use <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">Client-to-Tunnel</a> instead.</td>
<td><code>ssh://localhost:22</code></td>
</tr>
<tr>
<td>RDP</td>
<td>Streams RDP over a WebSocket connection. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-cloudflared-authentication/">Connect to RDP with client-side cloudflared</a>.</td>
<td><code>rdp://localhost:3389</code></td>
</tr>
<tr>
<td>SMB</td>
<td>Streams SMB over a WebSocket connection. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/smb/#connect-to-smb-server-with-cloudflared-access">Connect to SMB with client-side cloudflared</a>.</td>
<td><code>smb://localhost:445</code></td>
</tr>
<tr>
<td>HTTP_STATUS</td>
<td>Responds to all requests with a fixed HTTP status code.</td>
<td><code>http_status:404</code></td>
</tr>
<tr>
<td>BASTION</td>
<td>Allows <code>cloudflared</code> to act as a jump host, providing access to any local address.</td>
<td><code>bastion</code></td>
</tr>
<tr>
<td>HELLO_WORLD</td>
<td>Test server for validating your Cloudflare Tunnel connection (for <a href="/tunnel/features/locally-managed-tunnels/configuration-file/#file-structure-for-published-applications">locally managed tunnels</a> only).</td>
<td><code>hello_world</code></td>
</tr>
</tbody>
</table>
<h2 id="ipv6-service-addresses">IPv6 service addresses</h2>
<p>When the service value is an IPv6 literal, wrap the address in square brackets as defined by <a href="https://datatracker.ietf.org/doc/html/rfc3986#section-3.2.2">RFC 3986</a>. The brackets are required so that the <code>:</code> characters in the address are not confused with the port separator.</p>
<table>
<thead>
<tr>
<th>Service type</th>
<th>Example <code>service</code> value</th>
</tr>
</thead>
<tbody>
<tr>
<td>HTTP</td>
<td><code>http://[2001:db8::1]:8000</code></td>
</tr>
<tr>
<td>HTTPS</td>
<td><code>https://[2001:db8::1]:443</code></td>
</tr>
<tr>
<td>TCP</td>
<td><code>tcp://[2001:db8::1]:2222</code></td>
</tr>
<tr>
<td>SSH</td>
<td><code>ssh://[2001:db8::1]:22</code></td>
</tr>
<tr>
<td>RDP</td>
<td><code>rdp://[2001:db8::1]:3389</code></td>
</tr>
</tbody>
</table>
<p>Hostnames and IPv4 addresses do not need brackets — <code>http://localhost:8000</code> and <code>http://192.0.2.1:8000</code> are valid as-is.</p>
<h2 id="dns-records">DNS records</h2>
<p>When you create a tunnel, Cloudflare generates a subdomain at <code>&lt;UUID&gt;.cfargotunnel.com</code>. You point a CNAME record at this subdomain to route traffic from your hostname to the tunnel.</p>
<p>The <code>cfargotunnel.com</code> subdomain only proxies traffic for DNS records in the same Cloudflare account. If someone discovers your tunnel UUID, they cannot create a DNS record in another account to proxy traffic through it.</p>
<h3 id="create-a-dns-record">Create a DNS record</h3>
<p>To create a DNS record for a Cloudflare Tunnel:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14967.md")
</div></div>
<p>The DNS record and the tunnel are independent. You can create DNS records that point to a tunnel that is not running. If a tunnel stops, the DNS record is not deleted — visitors will see a <code>1016</code> error.</p>
<p>You can also create multiple DNS records pointing to the same tunnel subdomain. If you route traffic from multiple hostnames to multiple services, create a CNAME entry for each hostname. All entries share the same target.</p>
<h2 id="load-balancing">Load balancing</h2>
<p>Use a <a href="/load-balancing/load-balancers/">public load balancer</a> to distribute traffic across servers running your published applications. This provides health-check-based failover and intelligent traffic steering across regions.</p>
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;    accTitle: Load balancing traffic to applications behind Cloudflare Tunnel&#10;&#10;    A[Internet] --&gt; C{Cloudflare &lt;br&gt; Load Balancer}&#10;    C -- Tunnel 1 --&gt; cf1&#10;    C -- Tunnel 2 --&gt; cf2&#10;    subgraph F[Data center 2]&#10;        cf2[cloudflared]&#10;        S3[App server]&#10;        S4[App server]&#10;        cf2--&gt;S3&#10;        cf2--&gt;S4&#10;    end&#10;    subgraph E[Data center 1]&#10;        cf1[cloudflared]&#10;        S1[App server]&#10;        S2[App server]&#10;        cf1--&gt;S1&#10;        cf1--&gt;S2&#10;    end&#10;</code></pre>
<h3 id="replicas-versus-load-balancers">Replicas versus load balancers</h3>
<p>Running multiple <code>cloudflared</code> <a href="/tunnel/configuration/#replicas-and-high-availability">replicas</a> on the same tunnel UUID provides basic redundancy — if one host fails, other replicas continue serving traffic. However, the load balancer treats all replicas of the same tunnel UUID as a single endpoint.</p>
<p>For granular traffic steering and <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>, connect each host using a different tunnel UUID so the load balancer can address them independently.</p>
<h3 id="add-a-tunnel-to-a-load-balancer-pool">Add a tunnel to a load balancer pool</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/14962.md")
</aside>
<p>To create a load balancer for Cloudflare Tunnel published applications:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create load balancer</strong>, then select <strong>Public load balancer</strong>.</li>
<li>Under <strong>Select website</strong>, select the domain of your published application route.</li>
<li>On the <strong>Hostname</strong> page, enter a hostname for the load balancer (for example, <code>lb.example.com</code>).</li>
<li>On the <strong>Pools</strong> page, select <strong>Create a pool</strong> and enter a descriptive name.</li>
<li>Add a tunnel endpoint with the following values:
<ul>
<li><strong>Endpoint Name</strong>: Name of the server running the application</li>
<li><strong>Endpoint Address</strong>: <code>&lt;UUID&gt;.cfargotunnel.com</code> (find the Tunnel ID in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Networking</strong> &gt; <strong>Tunnels</strong>)</li>
<li><strong>Header value</strong>: Hostname of your published application route (for example, <code>app.example.com</code>)</li>
<li><strong>Weight</strong>: <code>1</code> (if only one endpoint)</li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14961.md")
</aside>
<ol start="7">
<li>Choose a <strong>Fallback pool</strong>. Refer to <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policies</a> for routing options.</li>
<li>(Recommended) On the <strong>Monitors</strong> page, attach a monitor to the endpoint. For an HTTP or HTTPS application, create an HTTPS monitor:
<ul>
<li><strong>Type</strong>: <em>HTTPS</em></li>
<li><strong>Path</strong>: <code>/</code></li>
<li><strong>Port</strong>: <code>443</code></li>
<li><strong>Expected Code(s)</strong>: <code>200</code></li>
<li><strong>Header Name</strong>: <code>Host</code></li>
<li><strong>Value</strong>: <code>app.example.com</code></li>
</ul>
</li>
<li>Save and deploy the load balancer.</li>
</ol>
<p>To test, access your application using the load balancer hostname (<code>lb.example.com</code>).</p>
<details class="nb-details"><summary>Monitor TCP tunnel origins</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14968.md")
</div></details>
<details class="nb-details"><summary>Local connection preference</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14969.md")
</div></details>
<h2 id="cloudflare-settings">Cloudflare settings</h2>
<p>Published applications inherit the Cloudflare settings for their hostname, including <a href="/cache/how-to/cache-rules/">cache rules</a>, <a href="/waf/">WAF rules</a>, and other <a href="/rules/">Rules</a> configurations. You can change these settings for each hostname in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</p>
<p>If you use a load balancer, settings are applied to the load balancer hostname instead.</p>
