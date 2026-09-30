---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/network/protect-public-networks-with-cloudflare/
  description: This document explains how Cloudflare Magic Transit, Cloudflare Network Firewall, and Gateway work. The products offer in-line, automatic, scalable network protection for all Internet-facing networks. The architecture is designed to protect public networks across multiple clouds and on-premises.
  full_title: Protect public networks with Cloudflare · Cloudflare Reference Architecture docs
  head_html: <title>Protect public networks with Cloudflare · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="This document explains how Cloudflare Magic Transit, Cloudflare Network Firewall, and Gateway work. The products offer in-line, automatic, scalable network protection for all Internet-facing networks. The architecture is designed to protect public networks across multiple clouds and on-premises."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/network/protect-public-networks-with-cloudflare/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/network/protect-public-networks-with-cloudflare/index.md"><meta property="og:title" content="Protect public networks with Cloudflare · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="This document explains how Cloudflare Magic Transit, Cloudflare Network Firewall, and Gateway work. The products offer in-line, automatic, scalable network protection for all Internet-facing networks. The architecture is designed to protect public networks across multiple clouds and on-premises."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/network/protect-public-networks-with-cloudflare/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="DDoS Protection,Gateway,Cloudflare Network Firewall,Magic Transit,Network Interconnect"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/network/protect-public-networks-with-cloudflare/#page","headline":"Protect public networks with Cloudflare \u00b7 Cloudflare Reference Architecture docs","description":"This document explains how Cloudflare Magic Transit, Cloudflare Network Firewall, and Gateway work. The products offer in-line, automatic, scalable network protection for all Internet-facing networks. The architecture is designed to protect public networks across multiple clouds and on-premises.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/network/protect-public-networks-with-cloudflare/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/network/protect-public-networks-with-cloudflare/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>Network security teams have traditionally used various network firewalls or security appliances at the perimeter of their network to protect their public-facing networks against both external and internal threats like DDoS attacks, malware, ransomware, phishing, and leaking of sensitive information. However, these firewalls and security appliances are often expensive, complex to configure and manage, difficult to scale to handle large attacks, and lack the flexibility to quickly incorporate upgrades and patches to defend against newly discovered threats and vulnerabilities.</p>
<p><a href="/magic-transit/">Cloudflare Magic Transit</a>, <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a>, and <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> services running natively on <a href="https://www.cloudflare.com/network/">Cloudflare's massive global network</a> provide solutions to all the shortcomings described above and more. These services offer in-line, automatic, scalable network protection for all your Internet-facing networks, without slowing down performance, regardless of where they are deployed, whether on-premises, in the cloud, or a combination of the two (that is, a hybrid architecture).</p>
<ul>
<li><a href="https://www.cloudflare.com/network-services/products/magic-transit/">Magic Transit</a> provides instant detection and mitigation against network-layer DDoS attacks on your public, Internet-facing networks.</li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> is a cloud-native network firewall service that can be used to filter traffic that is routed to and from your networks that are protected by Magic Transit. It also supports functionalities such as <a href="/cloudflare-network-firewall/about/ids/">Intrusion Detection</a> (IDS) and <a href="/cloudflare-network-firewall/packet-captures/">packet capture</a>.</li>
<li><a href="https://www.cloudflare.com/zero-trust/products/gateway/">Gateway</a> is a secure web gateway (SWG) service that allows you to inspect and control Internet bound traffic originating from your network by proxying this traffic through Cloudflare's global network while applying DNS, network and HTTP based <a href="/cloudflare-one/traffic-policies/">policies</a>.</li>
</ul>
<p>The details of how Magic Transit, Cloudflare Network Firewall, and Gateway work and how these products can be architected for various use cases can be found in the linked resources at the end of the document. This document will focus specifically on the reference architectures of using Cloudflare Magic Transit, Cloudflare Network Firewall, and Cloudflare Gateway services to protect public, Internet-facing network infrastructure.</p>
<p>To illustrate the architecture and how it works, the following diagrams visualize an example corporation with a set of public facing networks. These networks are deployed at 5 distinct locations, both on-premises and across multiple public clouds.</p>
<pre tabindex="0"><code>AWS VPC: 192.0.2.0/24&#10;GCP VPC: 198.51.100.0/24&#10;Azure vNet: 203.0.113.0/26&#10;On-premises data center 1: 203.0.113.64/26&#10;On-premises data center 2: 203.0.113.128/25&#10;</code></pre>
<h2 id="protect-inbound-network-traffic">Protect inbound network traffic</h2>
<p>The reference architecture diagram below illustrates how Cloudflare Magic Transit and Cloudflare Network Firewall can be used to protect the public networks from inbound traffic originating from the Internet.</p>
<p><img src="/assets/upstream/images/reference-architecture/protect-public-networks-with-cloudflare/figure-1.svg" alt="Figure 1: Protect the public networks from inbound traffic originating from the Internet." title="Figure 1: Protect the public networks from inbound traffic originating from the Internet." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>
<p>Using Border Gateway Protocol (<a href="https://www.cloudflare.com/learning/security/glossary/what-is-bgp/">BGP</a>) and <a href="https://www.cloudflare.com/learning/cdn/glossary/anycast-network/">IP anycast</a>, Cloudflare advertises customer's protected IP prefixes to the Internet from all of Cloudflare's global data centers. Internet traffic destined to these protected IP prefixes will always be routed to the Cloudflare data center that is closest to the source of the traffic.</p>
<p>At the same time, on-premises network(s) and cloud provider network(s) would stop advertising the same exact prefixes from their respective on-premises border routers and cloud border routers. This ensures all Internet traffic destined to the Magic Transit protected IP prefixes will be routed through the Cloudflare network.</p>
<p>You can instead advertise less-specific IP prefixes from the border routers to the Internet. This way, in the unlikely event of a Magic Transit service failure, traffic can be quickly re-routed directly to network locations from the Internet.</p>
</li>
<li>
<p>Traffic originating from the Internet and destined to the protected IP prefixes is ingested into the global Cloudflare network.</p>
</li>
<li>
<p>All DDoS attack traffic is mitigated in-line at every Cloudflare data center using advanced and automated <a href="/ddos-protection/">DDoS mitigation</a> technologies.</p>
</li>
<li>
<p>Traffic that passes DDoS mitigation is subjected to additional network firewall filtering using the included <a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a> service.</p>
</li>
<li>
<p>Clean, filtered traffic is routed to the protected networks either through private <a href="/network-interconnect/">Cloudflare Network Interconnect</a> (CNI) connections, or the public Internet using GRE or IPsec tunnels. More specific details on Magic Transit IP tunnels can be found in the <a href="/magic-transit/reference/gre-ipsec-tunnels/">Magic Transit Tunnels and Encapsulation documentation</a>.</p>
</li>
<li>
<p>The server return traffic is routed back through the Cloudflare network to reach the Internet, using <a href="/magic-transit/reference/egress/">Magic Transit Egress</a>. It can be routed to the Cloudflare network via the same CNIs or GRE, IPsec tunnels that the ingress traffic traversed, using routing techniques such as policy-based routing (PBR) at your sites.</p>
</li>
<li>
<p>Magic Transit Egress traffic is subject to Cloudflare Network Firewall filtering before being routed out to the Internet towards the users.</p>
</li>
</ol>
<h2 id="protect-outbound-network-traffic">Protect outbound network traffic</h2>
<p>The reference architecture diagram below illustrates how Cloudflare services - Magic Transit (Egress), Cloudflare Network Firewall and Cloudflare Gateway, can be used to protect outbound Internet traffic originating from the public networks.</p>
<p><img src="/assets/upstream/images/reference-architecture/protect-public-networks-with-cloudflare/figure-2.svg" alt="Figure 2: Protect outbound Internet traffic originating from the public networks." title="Figure 2: Protect outbound Internet traffic originating from the public networks." /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<ol>
<li>Each site network routes outbound Internet traffic originating from the public networks to Cloudflare, via the same CNIs and IP tunnels that inbound traffic traverses. This can be done at your site through routing techniques of your choice, such as policy based routing (PBR).</li>
<li>Upon entering the Cloudflare network, outbound Internet traffic is first routed through Cloudflare Network Firewall where it is subject to any configured network firewall policies.</li>
<li>Outbound Internet traffic is subsequently sent to <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a>, our secure web gateway service where various <a href="/cloudflare-one/traffic-policies/">policies</a> enforce a comprehensive set of security and control measures on the outbound traffic, ensuring the utmost protection for your networks.</li>
<li>Once traffic clears inspection, Gateway proxies the outbound traffic to their destinations on the Internet. The source IP addresses of the outbound traffic are the Cloudflare owned IP addresses associated with the Gateway service.</li>
<li>Return traffic from the Internet, destined to Cloudflare's IP addresses linked to the Gateway service, is routed into Cloudflare's global network.</li>
<li>Traffic is inspected against Gateway policies.</li>
<li>Return traffic that passes Gateway inspection is routed to Cloudflare Network Firewall for further packet filtering, if any.</li>
<li>Return traffic that passes Cloudflare Network Firewall filtering is routed from Cloudflare to your network locations via CNIs or IP Tunnels over the Internet.</li>
</ol>
<h2 id="related-resources">Related Resources</h2>
<ul>
<li><a href="/magic-transit/">Cloudflare Magic Transit</a></li>
<li><a href="/ddos-protection/">Cloudflare DDoS Protection</a></li>
<li><a href="/reference-architecture/architectures/magic-transit/">Magic Transit Reference Architecture</a></li>
<li><a href="/network-interconnect/">Cloudflare Network Interconnect</a></li>
<li><a href="/cloudflare-network-firewall/">Cloudflare Network Firewall</a></li>
<li><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a></li>
<li><a href="/cloudflare-wan/zero-trust/cloudflare-gateway/">Integration of Cloudflare Magic services and Cloudflare Gateway</a></li>
</ul>
