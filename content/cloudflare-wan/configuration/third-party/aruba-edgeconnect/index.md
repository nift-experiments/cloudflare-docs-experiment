---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/aruba-edgeconnect/
  description: Connect Aruba EdgeConnect to Cloudflare WAN.
  full_title: Aruba EdgeConnect Enterprise · Cloudflare WAN docs
  head_html: <title>Aruba EdgeConnect Enterprise · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Aruba EdgeConnect to Cloudflare WAN."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/aruba-edgeconnect/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/aruba-edgeconnect/index.md"><meta property="og:title" content="Aruba EdgeConnect Enterprise · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Aruba EdgeConnect to Cloudflare WAN."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/aruba-edgeconnect/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/aruba-edgeconnect/#page","headline":"Aruba EdgeConnect Enterprise \u00b7 Cloudflare WAN docs","description":"Connect Aruba EdgeConnect to Cloudflare WAN.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/aruba-edgeconnect/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/third-party/aruba-edgeconnect/
  schema: 1
---
<p>Cloudflare partners with Aruba's EdgeConnect SD-WAN solution to provide users with an integrated solution. The EdgeConnect appliances manage subnets associated with branch offices or retail locations. Anycast tunnels are set up between the EdgeConnect appliances and Cloudflare to securely route traffic.</p>
<p>This tutorial describes how to configure the EdgeConnect device for both east-west (branch to branch) and north-south (Internet-bound) use cases.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6867.md")
</aside>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before setting up a connection between EdgeConnect and Cloudflare, you must have:</p>
<ul>
<li>A contract that includes Cloudflare WAN (formerly Magic WAN) and Secure Web Gateway.</li>
<li>Received two Cloudflare endpoints (anycast IP addresses), available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>.</li>
<li>Determined a private static /31 IP pair to use with each tunnel. The /31 pairs should be from a different private subnet, separate from the private subnets used behind each EdgeConnect appliance.</li>
<li>The EdgeConnect devices used in this tutorial and on v9.0.</li>
</ul>
<h2 id="example-scenario">Example scenario</h2>
<details class="nb-details"><summary>GRE tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6868.md")
</div></details>
<details class="nb-details"><summary>IPsec tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6869.md")
</div></details>
<h2 id="1-define-a-common-site-on-the-orchestrator"><ol>
<li>Define a common site on the Orchestrator</li>
</ol></h2>
<p>For all EdgeConnect devices using Cloudflare, modify the devices to put them on the same site. This disables automatic IPsec tunnel creation between the EdgeConnect devices using the same labels for the WAN interfaces in use.</p>
<p>This step is only required if Cloudflare is used for east-west traffic routing.</p>
<h2 id="2-configure-overlay-policies"><ol start="2">
<li>Configure overlay policies</li>
</ol></h2>
<p>Aruba Orchestrator's Business Intent Overlays create intuitive policies which automatically identify and steer application traffic to Cloudflare. This example creates two Business Intent Overlay (BIO) policies.</p>
<details class="nb-details"><summary>GRE tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6870.md")
</div></details>
<details class="nb-details"><summary>IPsec tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6871.md")
</div></details>
<h2 id="3-create-tunnels-on-cloudflare-and-edgeconnect"><ol start="3">
<li>Create tunnels on Cloudflare and EdgeConnect</li>
</ol></h2>
<details class="nb-details"><summary>GRE tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6872.md")
</div></details>
<details class="nb-details"><summary>IPsec tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6873.md")
</div></details>
<h2 id="4-create-static-routes-on-cloudflare-and-edgeconnect"><ol start="4">
<li>Create static routes on Cloudflare and EdgeConnect</li>
</ol></h2>
<details class="nb-details"><summary>GRE tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6874.md")
</div></details>
<details class="nb-details"><summary>IPsec tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6875.md")
</div></details>
<h2 id="5-validate-traffic-flow"><ol start="5">
<li>Validate traffic flow</li>
</ol></h2>
<details class="nb-details"><summary>GRE tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6876.md")
</div></details>
<details class="nb-details"><summary>IPsec tunnel configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6877.md")
</div></details>
<h2 id="6-cloudflare-policies"><ol start="6">
<li>Cloudflare policies</li>
</ol></h2>
<p>At this point, the GRE or IPsec tunnels should be connected from the EdgeConnect appliances to Cloudflare's global network, and traffic is scoped to route over the tunnels using the EdgeConnect Business Intent Overlays.</p>
<p>To begin filtering traffic and gathering analytics, refer to the <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall documentation</a> to learn how to create filters for east-west inter-branch traffic and the <a href="/cloudflare-one/traffic-policies/">Secure Web Gateway documentation</a> to learn how to configure Gateway policies if you decide to send traffic from your local private subnets to the Internet through Cloudflare Gateway.</p>
