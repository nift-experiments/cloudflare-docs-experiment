---
cp9:
  canonical: https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/
  description: Recommended CPU, memory, and scaling guidelines for cloudflared tunnel hosts.
  full_title: Hardware requirements · Cloudflare Workers VPC
  head_html: <title>Hardware requirements · Cloudflare Workers VPC</title><meta name="generator" content="Nift"><meta name="description" content="Recommended CPU, memory, and scaling guidelines for cloudflared tunnel hosts."><link rel="canonical" href="https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/index.md"><meta property="og:title" content="Hardware requirements · Cloudflare Workers VPC"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Recommended CPU, memory, and scaling guidelines for cloudflared tunnel hosts."><meta property="og:url" content="https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers VPC"><meta name="algolia_product_filter" content="Workers VPC"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers VPC"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/#page","headline":"Hardware requirements \u00b7 Cloudflare Workers VPC","description":"Recommended CPU, memory, and scaling guidelines for cloudflared tunnel hosts.","url":"https://developers.cloudflare.com/workers-vpc/configuration/tunnel/hardware-requirements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers-vpc/configuration/tunnel/hardware-requirements/
  schema: 1
---
<h2 id="recommendations">Recommendations</h2>
<p>For production use cases, we recommend the following baseline configuration:</p>
<ul>
<li>Run a cloudflared replica on two dedicated host machines per network location. Using two hosts enables server-side redundancy. See <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">tunnel availability and replicas</a> for setup instructions.</li>
<li>Size each host with minimum 4GB of RAM and 4 CPU cores.</li>
</ul>
<p>This setup is usually sufficient to handle traffic from small-medium sized applications. The actual amount of resources used by cloudflared will depend on many variables, including the number of requests per second, bandwidth, network path, and hardware. If usage increases beyond your existing tunnel capacity, you can scale your tunnel by increasing the hardware allocated to the cloudflared hosts.</p>
<h2 id="capacity-calculator">Capacity calculator</h2>
<p>To estimate tunnel capacity requirements for your deployment, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/">tunnel capacity calculator in the Zero Trust documentation</a>.</p>
<h2 id="scaling-considerations">Scaling considerations</h2>
<p>Monitor tunnel performance and scale accordingly:</p>
<ul>
<li><strong>CPU utilization</strong>: Keep below 70% average usage</li>
<li><strong>Memory usage</strong>: Maintain headroom for traffic spikes</li>
<li><strong>Network bandwidth</strong>: Ensure adequate throughput for peak loads</li>
<li><strong>Connection count</strong>: Scale cloudflared vertically when approaching capacity limits</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Configure <a href="/workers-vpc/configuration/tunnel/">tunnel deployment</a></li>
<li>Set up <a href="/workers-vpc/configuration/tunnel/">high availability</a> with multiple replicas</li>
</ul>
