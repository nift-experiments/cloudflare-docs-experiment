---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/private-network/
  description: Use Private Network Load Balancing to load balance traffic between servers within a data center or between private applications, and eliminate the need for hardware appliances.
  full_title: Private Network Load Balancing · Cloudflare Load Balancing docs
  head_html: <title>Private Network Load Balancing · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Private Network Load Balancing to load balance traffic between servers within a data center or between private applications, and eliminate the need for hardware appliances."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/private-network/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/private-network/index.md"><meta property="og:title" content="Private Network Load Balancing · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Private Network Load Balancing to load balance traffic between servers within a data center or between private applications, and eliminate the need for hardware appliances."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/private-network/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/private-network/#page","headline":"Private Network Load Balancing \u00b7 Cloudflare Load Balancing docs","description":"Use Private Network Load Balancing to load balance traffic between servers within a data center or between private applications, and eliminate the need for hardware appliances.","url":"https://developers.cloudflare.com/load-balancing/private-network/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /load-balancing/private-network/
  schema: 1
---
<p>Private Network Load Balancing enables you to load balance traffic between servers within a data center (<a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/">endpoint steering</a>) and between private applications. This helps you eliminate the need for hardware appliances and facilitates the migration of your infrastructure to the cloud, providing advantages such as elastic scalability and enhanced reliability.</p>
<p>Private Network Load Balancing supports not only public IPs but also virtual IPs and private IPs as endpoint values.</p>
<hr />
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10350.md")
</aside>
<hr />
<hr />
<h2 id="off-ramps">Off-ramps</h2>
<p>Off-ramps create a direct and secure way for Cloudflare to connect into your networks that are not publicly available.</p>
<p>Since traffic steering decisions or failover mechanisms rely on the health information of pools and endpoints, being able to input your virtual or private IPs directly as endpoints within your load balancer means you can better leverage existing health monitoring.</p>
<h3 id="tunnel">Tunnel</h3>
<p>Currently, to be able to connect to private IP origins, Cloudflare load balancers require a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare tunnel</a> with an associated <a href="/cloudflare-one/networks/virtual-networks/">virtual network (VNet)</a>. If you are connecting to your endpoints using a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers">published application route</a> a VNet is not necessary.</p>
<p>Once the endpoint and virtual network (VNet) tunnel association is configured, Cloudflare can determine not only the tunnel health but also the health of the corresponding virtual or private IP targets.</p>
<p>Refer to <a href="/load-balancing/private-network/public-to-tunnel/">Set up Private Network Load Balancing for Public traffic to Tunnel</a> for a detailed guide.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10349.md")
</aside>
<h3 id="cloudflare-wan">Cloudflare WAN</h3>
<p>Private Network Load Balancing supports off-ramping traffic for Cloudflare WAN (formerly Magic WAN) tunnels, such as GRE, IPSec or CNI tunnels. For more information refer to the <a href="/load-balancing/private-network/cloudflare-wan/">Set up Private Network Load Balancing with Cloudflare WAN</a>.</p>
<hr />
<h2 id="on-ramps">On-ramps</h2>
<p>Private Network Load Balancing on-ramps, on the other hand, refer to secure paths between the end-user request and the Cloudflare network. Cloudflare Load Balancing supports traffic from <a href="/cache/">CDN</a>, <a href="/spectrum/">Spectrum</a>, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> and <a href="/cloudflare-wan/">Cloudflare WAN</a> and forward that traffic to a load balancer, and then egress to an endpoint behind any off-ramp (CDN/CNI/IPSec/GRE/Tunnel). Your traffic can ingress and egress by any on-ramp/off-ramp combination.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10348.md")
</aside>
<hr />
<h2 id="use-cases">Use cases</h2>
<ul>
<li>
<p><strong>Requests originating from the public Internet and directed to a private/internal service</strong>: You can route requests from the Internet to your internal services on internal IPs - such as accounting or production automation systems - using <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>
</li>
<li>
<p><strong>Intelligent traffic routing</strong>: Benefit from failover for your private traffic and have the ability to monitor the health of these IP targets directly, rather than load balancing to a tunnel and only monitoring the health of the tunnel itself.</p>
</li>
<li>
<p><strong>Host applications on non-standard ports</strong>: Easily specify and route traffic to applications hosted on private IP addresses using non-standard ports, allowing greater flexibility in service configuration without requiring changes to existing infrastructure.</p>
</li>
<li>
<p><strong>Public and Private Load Balancers</strong>: Public LBs can direct Internet traffic to private IP addresses, supporting all L7 products like WAF and API Shield. Private LBs direct traffic originating from private networks to private IP addresses and require an on-ramp like the Cloudflare One Client or Cloudflare WAN.</p>
</li>
</ul>
