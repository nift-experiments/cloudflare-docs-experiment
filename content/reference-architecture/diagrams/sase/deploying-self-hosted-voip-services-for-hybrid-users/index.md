---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/
  description: Learn how Cloudflare improves over traditional VPN solutions by leveraging its global network.
  full_title: Deploy self-hosted VoIP services for hybrid users · Cloudflare Reference Architecture docs
  head_html: <title>Deploy self-hosted VoIP services for hybrid users · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Cloudflare improves over traditional VPN solutions by leveraging its global network."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/index.md"><meta property="og:title" content="Deploy self-hosted VoIP services for hybrid users · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Cloudflare improves over traditional VPN solutions by leveraging its global network."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="Access,Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/#page","headline":"Deploy self-hosted VoIP services for hybrid users \u00b7 Cloudflare Reference Architecture docs","description":"Learn how Cloudflare improves over traditional VPN solutions by leveraging its global network.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/sase/deploying-self-hosted-voip-services-for-hybrid-users/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>Traditional VPN solutions create several problems for VoIP deployments, primarily due to their inefficiencies in handling real-time traffic protocols such as <a href="https://en.wikipedia.org/wiki/Session_Initiation_Protocol">SIP</a> and <a href="https://en.wikipedia.org/wiki/Real-time_Transport_Protocol">RTP</a>. Legacy VPN deployments introduce high latency and jitter, which negatively impact voice call quality. Additionally, they often struggle with <a href="https://en.wikipedia.org/wiki/Network_address_translation">NAT</a> traversal, leading to connection issues for VoIP calls.</p>
<p>Cloudflare improves over traditional VPN solutions by leveraging its <a href="https://www.cloudflare.com/network/">global network</a> of data centers in <div class="nb-data-component" data-cf-component="PublicStats"></div> to significantly reduce latency for remote users. When using our device agent, remote users are automatically connected to the nearest Cloudflare data center, thus reducing latency.</p>
<p>This document explains how to architect access to a self-hosted VoIP service using Cloudflare. Note the solution below uses <a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector), a small piece of software deployed on a server in the same subnet as the VoIP servers and creates bi-directional traffic flow through Cloudflare to users.</p>
<h2 id="bi-directional-voip-traffic-flow">Bi-directional VoIP traffic flow</h2>
<p><img src="/assets/upstream/images/reference-architecture/deploying-self-hosted-voip-services-for-hybrid-users/figure1.svg" alt="Figure 1: Cloudflare facilitates secure connectivity from user devices to the network where the SIP server is running." title="Figure 1: Cloudflare facilitates secure connectivity from user devices to the network where the SIP server is running." /></p>
<p>The diagram above shows Cloudflare Mesh and our device agent deployed to establish highly performant, reliable connectivity for private VoIP services. Note that Cloudflare will assign remote users an address from the <span class="nb-glossary-tooltip" title="WARP CGNAT IP">CGNAT range</span>, which is used for the private network created between device agents. Cloudflare Mesh ensures secure, bidirectional communication between remote users and the on-premise SIP server, without exposing the server to the public Internet. This shields the VoIP infrastructure from potential attacks while maintaining a seamless, encrypted connection for real-time communications.</p>
<ol>
<li>VoIP server resides on a private network with no public IP.</li>
<li>Cloudflare Mesh creates a secure tunnel to Cloudflare and is configured as a virtual router in the private network.</li>
<li>Allow traffic from Cloudflare to reach the VoIP server, but also allow private network initiated traffic, such as an outbound VoIP call from the server, to route over the Cloudflare tunnel. In the above diagram, we add a static route on the default gateway of <code>100.96.0.0/12</code> (the WARP CGNAT range) via <code>10.0.50.10</code> (Cloudflare Mesh virtual router).</li>
<li>Traffic passes through our <a href="/cloudflare-one/traffic-policies/">Secure Web Gateway</a> (SWG), which applies network level firewall rules to both inbound and outbound traffic.</li>
<li>A device agent is installed on remote user devices. The agent establishes a secure tunnel to Cloudflare, which allows VoIP software to both receive and make calls.</li>
</ol>
<h2 id="call-flow-examples">Call flow examples</h2>
<p>VoIP software running on the remote user's device registers with the VoIP server using SIP. The Cloudflare device agent will be assigned an address from the CGNAT IP range, <code>100.96.0.0/12</code>. As routing has been established to Cloudflare for <code>100.96.0.0/12</code> and to the on-premise network of <code>10.0.50.0/24</code>, call flows will work as normal – both direct and indirect media are supported.</p>
<h3 id="remote-user-calling-another-remote-user">Remote user calling another remote user</h3>
<p>When calls are made from user to user, some traffic flows from user devices through Cloudflare to the on-premise server, while other traffic flows through Cloudflare directly to the other user. Note that the device agent is creating a secure tunnel through which the CGNAT addresses are routed. Both users in this flow have registered their SIP clients with the server.</p>
<p><img src="/assets/upstream/images/reference-architecture/deploying-self-hosted-voip-services-for-hybrid-users/figure2.svg" alt="Figure 2: For remote user to remote user, not all traffic flows over Cloudflare Mesh to the SIP server." title="Figure 2: For remote user to remote user, not all traffic flows over Cloudflare Mesh to the SIP server." /></p>
<p>The above diagram shows the high level signaling and media paths.</p>
<ol>
<li>Alice registers directly with the SIP server (<code>10.0.50.60</code>) with a Cloudflare assigned CGNAT IP of <code>100.96.0.12</code>.</li>
<li>Bob also registers directly with the SIP server (<code>10.0.50.60</code>) with their CGNAT IP of <code>100.96.0.13</code>.</li>
<li>When Alice calls Bob, the SIP server will send a SIP INVITE message to Bob at <code>100.96.0.13</code>.</li>
<li>The default gateway for the SIP server is <code>10.50.0.1</code>, but we have defined a static route such that for destination <code>100.96.0.0/12</code>, the next hop is the Cloudflare Mesh interface (<code>10.0.50.10</code>).</li>
<li>The SIP INVITE message will be routed across Cloudflare Mesh to the Cloudflare network and then received by Bob.</li>
<li>Bob accepts and the SIP server will send SIP/SDP messages to both Alice and Bob specifying which parameters to use for the RTP (audio) data.</li>
<li>For Direct Media paths where the SIP server is not in the audio path and the RTP streams are directly between Alice and Bob, ensure that <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-all-cloudflare-one-traffic-to-reach-enrolled-devices"><strong>Allow all Cloudflare One traffic to reach enrolled devices</strong></a> has been enabled in Cloudflare. Audio streams in the Direct Media use case will not need to route over Cloudflare Mesh.</li>
</ol>
<h3 id="remote-user-to-on-premise-user">Remote user to on-premise user</h3>
<p>Calls between remote and on-premise users are very similar, but RTP audio will be sent over Cloudflare Mesh in addition to the SIP signaling.</p>
<p><img src="/assets/upstream/images/reference-architecture/deploying-self-hosted-voip-services-for-hybrid-users/figure3.svg" alt="Figure 3: Remote user to on-premise user has all traffic routed via Cloudflare to SIP server and client." title="Figure 3: Remote user to on-premise user has all traffic routed via Cloudflare to SIP server and client." /></p>
<p>The high-level signaling and media paths are shown below:</p>
<p><img src="/assets/upstream/images/reference-architecture/deploying-self-hosted-voip-services-for-hybrid-users/figure4.svg" alt="Figure 4: Both signaling and media (audio, video etc) travel via secured tunnels from remote devices to on-premise clients." title="Figure 4: Both signaling and media (audio, video etc) travel via secured tunnels from remote devices to on-premise clients." /></p>
<ol>
<li>Alice registers directly with the SIP server (<code>10.0.50.60</code>) with her CGNAT IP of <code>100.96.0.12</code>.</li>
<li>Bob also registers directly with the SIP server (<code>10.0.50.60</code>) with their LAN IP of <code>10.0.50.101</code>.</li>
<li>When Alice calls Bob, the SIP server will send a SIP INVITE message to Bob at <code>10.0.50.101</code>.</li>
<li>The default gateway for the SIP server is <code>10.50.0.1</code>, but we have defined a static route such that for destination <code>100.96.0.0/12</code>, the next hop is the Cloudflare Mesh interface (<code>10.0.50.10</code>).</li>
<li>The SIP INVITE message will be sent on the local network to Bob.</li>
<li>Bob accepts and the SIP server will send SIP/SDP messages to both Alice and Bob specifying which parameters to use for the RTP (audio) data.</li>
<li>Bob will send audio to Alice at <code>100.96.0.12</code>, which will be routed across Cloudflare Mesh to Cloudflare, and Alice will send audio to Bob at <code>10.0.50.101</code>, which will be sent from Cloudflare across Cloudflare Mesh to the on-premise local network.</li>
</ol>
<h2 id="summary">Summary</h2>
<p>With Cloudflare Mesh, remote users communicating with other remote users or on-premise users via on-premise SIP servers will have a seamless and secure experience for both ends. Key benefits include:</p>
<ol>
<li>
<p><strong>Bidirectional connectivity</strong>: Cloudflare Mesh supports bidirectional traffic, which is crucial for remote users communicating with on-premise users. Both signaling and media traffic (SIP/RTP) flow securely between the two, regardless of where the user is physically located. This is done via Cloudflare's global network, using an encrypted tunnel, ensuring data integrity and encryption​.</p>
</li>
<li>
<p><strong>Private communication over CGNAT</strong>: Cloudflare Mesh assigns Carrier-Grade NAT (CGNAT) IPs to devices, which allows remote users to securely communicate with on-premise users over private networks. This ensures that communication remains isolated from the public Internet, enhancing security. The CGNAT functionality means that remote and on-premise users can communicate as though they are on the same network​.</p>
</li>
<li>
<p><strong>No NAT traversal issues</strong>: NAT traversal often poses a challenge in VoIP scenarios, but because Cloudflare Mesh preserves source IP addresses and handles bidirectional traffic without additional NAT boundaries, remote and on-premise users can communicate without issues typically caused by firewalls or NAT devices, improving the overall call setup and quality​.</p>
</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/mesh/">Set up Cloudflare Mesh</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-all-cloudflare-one-traffic-to-reach-enrolled-devices">Enable Mesh connectivity</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">About the Cloudflare One Client</a></li>
</ul>
