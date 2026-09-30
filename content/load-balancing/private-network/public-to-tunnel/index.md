---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/
  description: Load balance public traffic to private origins via Tunnel.
  full_title: Set up Private Network Load Balancing for Public traffic to Tunnel · Cloudflare Load Balancing docs
  head_html: <title>Set up Private Network Load Balancing for Public traffic to Tunnel · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Load balance public traffic to private origins via Tunnel."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/index.md"><meta property="og:title" content="Set up Private Network Load Balancing for Public traffic to Tunnel · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Load balance public traffic to private origins via Tunnel."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Load Balancing"><meta name="pcx_tags" content="Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/#page","headline":"Set up Private Network Load Balancing for Public traffic to Tunnel \u00b7 Cloudflare Load Balancing docs","description":"Load balance public traffic to private origins via Tunnel.","url":"https://developers.cloudflare.com/load-balancing/private-network/public-to-tunnel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Private networks"]}</script>
  markdown: true
  noindex: false
  route: /load-balancing/private-network/public-to-tunnel/
  schema: 1
---
<p>Consider the following steps to learn how to configure Private Network Load Balancing solution, using <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> as the off-ramp to securely connect to your private or internal services.</p>
<h2 id="1-configure-a-cloudflare-tunnel-with-an-assigned-virtual-network"><ol>
<li>Configure a Cloudflare tunnel with an assigned virtual network</li>
</ol></h2>
<p>The specific configuration steps can vary depending on your infrastructure and services you are looking to connect. If you are not familiar with Cloudflare Tunnel, the pages linked on each step provide more guidance.</p>
<ol>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#1-create-a-tunnel">Create a tunnel</a> to connect your data center to Cloudflare.</li>
<li>Create a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual network</a> and assign it to the tunnel you configured in the previous step.</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10347.md")
</div></div>
<h2 id="2-configure-cloudflare-load-balancing"><ol start="2">
<li>Configure Cloudflare Load Balancing</li>
</ol></h2>
<p>Once you have Cloudflare tunnels with associated virtual networks (VNets) configured, the VNets can be specified for each endpoint when you <a href="/load-balancing/pools/create-pool/#create-a-pool">create or edit a pool</a>. This will enable Cloudflare load balancers to use the correct tunnel and securely reach the private IP endpoints.</p>
<p>The specific configuration will vary depending on your use case. Refer to the following steps to understand the workflow.</p>
<ol>
<li><a href="/load-balancing/monitors/create-monitor/">Create the Load Balancing monitor</a> according to your needs.</li>
<li><a href="/load-balancing/pools/create-pool/">Create the pool</a> specifying your private IP addresses and corresponding virtual networks.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10344.md")
</aside>
<ol start="3">
<li><a href="/load-balancing/load-balancers/create-load-balancer/">Create the load balancer</a>, specifying the pool and monitor you created in the previous steps, as well as the desired <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">global traffic steering policies</a> and <a href="/load-balancing/additional-options/load-balancing-rules/">custom rules</a>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="spectrum-limitations">Spectrum limitations</h3>
@markup("md", "content/.markup/bodies/10343.md")
</aside>
