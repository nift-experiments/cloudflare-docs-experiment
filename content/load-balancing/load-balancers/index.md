---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/load-balancers/
  description: Configure load balancers to distribute traffic across pools.
  full_title: Load balancers · Cloudflare Load Balancing docs
  head_html: <title>Load balancers · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure load balancers to distribute traffic across pools."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/load-balancers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/load-balancers/index.md"><meta property="og:title" content="Load balancers · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure load balancers to distribute traffic across pools."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/load-balancers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/load-balancers/#page","headline":"Load balancers \u00b7 Cloudflare Load Balancing docs","description":"Configure load balancers to distribute traffic across pools.","url":"https://developers.cloudflare.com/load-balancing/load-balancers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/load-balancers/
  schema: 1
---
<p>A load balancer distributes traffic among pools according to <a href="/load-balancing/understand-basics/health-details/">pool health</a> and <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">traffic steering policies</a>. Each load balancer is identified by its DNS hostname (<code>lb.example.com</code>, <code>dev.example.com</code>, etc.) or IP address.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10388.md")
</aside>
<hr />
<h2 id="common-configurations">Common configurations</h2>
<p>For suggestions, refer to <a href="/load-balancing/load-balancers/common-configurations/">Common load balancer configurations</a>.</p>
<h2 id="public-vs-private-load-balancers">Public vs. Private Load Balancers</h2>
<p>Public Load Balancers are designed to handle traffic from the public Internet. When deployed, they automatically receive a hostname, making them immediately accessible. These load balancers can direct traffic to a range of destinations, including public hostnames, public IP addresses, and private IP addresses.</p>
<p>Private Load Balancers, in contrast, are meant for internal use within private networks. They do not automatically receive a hostname, but one can be assigned via Gateway Firewall Policies or through an internal DNS system. Private Load Balancers only accept traffic over a private network on-ramp, such as <a href="/warp-client/">the Cloudflare One Client</a> or <a href="/cloudflare-wan/">Cloudflare WAN</a>. They are capable of forwarding traffic exclusively to private IP addresses.</p>
<h2 id="load-balancing-and-existing-dns-records">Load balancing and existing DNS records</h2>
<p>For details about DNS records, refer to <a href="/load-balancing/load-balancers/dns-records/">DNS records for load balancing</a>.</p>
<h2 id="http-keep-alive-persistent-http-connection">HTTP keep-alive (persistent HTTP connection)</h2>
<p>Cloudflare maintains keep-alive connections to improve performance and reduce cost of recurring TCP connects in the request transaction as Cloudflare proxies customer traffic from its edge network to the site's origin.</p>
<p>Ensure HTTP Keep-Alive connections are enabled on your origin. Cloudflare reuses open TCP connections for up to 15 minutes (900 seconds) after the last HTTP request. Origin web servers close TCP connections if too many are open. HTTP Keep-Alive helps avoid premature reset of connections for requests proxied by Cloudflare.</p>
<h3 id="session-cookies">Session cookies</h3>
<p><strong>When using HTTP cookies to track and bind user sessions to a specific server</strong>, configure <a href="/load-balancing/understand-basics/session-affinity/">Session Affinity</a> to parse HTTP requests by cookie header. Doing so directs each request to the correct application server even when HTTP requests share the same TCP connection due to keep-alive.</p>
<p><strong>For example, F5 BIG-IP load balancers set a session cookie at the beginning of a TCP connection</strong> (if none exists) and then ignore all cookies from subsequent HTTP requests on the same TCP connection. This tends to break session affinity because Cloudflare sends multiple HTTP sessions on the same TCP connection. Configuring the load balancer to parse HTTP requests by cookie headers avoids this issue.</p>
<hr />
<h2 id="create-load-balancers">Create load balancers</h2>
<p>For step-by-step guidance, refer to <a href="/load-balancing/load-balancers/create-load-balancer/">Create a load balancer</a>.</p>
<hr />
<h2 id="properties">Properties</h2>
<p>For an up-to-date list of load balancer properties, refer to <a href="/api/resources/load_balancers/methods/get/">Load balancer properties</a> in the Cloudflare API documentation.</p>
<hr />
<h2 id="api-commands">API commands</h2>
<p>The Cloudflare API supports the following commands for load balancers.</p>
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
<td><a href="/api/resources/load_balancers/methods/create/">Create Load Balancer</a></td>
<td><code>POST</code></td>
<td><code>/zones/:zone_id/load_balancers</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/methods/delete/">Delete Load Balancer</a></td>
<td><code>DELETE</code></td>
<td><code>/zones/:zone_id/load_balancers/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/methods/list/">List Load Balancers</a></td>
<td><code>GET</code></td>
<td><code>/zones/:zone_id/load_balancers</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/methods/get/">Load Balancer Details</a></td>
<td><code>GET</code></td>
<td><code>/zones/:zone_id/load_balancers/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/methods/edit/">Overwrite specific properties</a></td>
<td><code>PATCH</code></td>
<td><code>/zones/:zone_id/load_balancers/:id</code></td>
</tr>
<tr>
<td><a href="/api/resources/load_balancers/methods/update/">Overwrite entire Load Balancer</a></td>
<td><code>PUT</code></td>
<td><code>/zones/:zone_id/load_balancers/:id</code></td>
</tr>
</tbody>
</table>
