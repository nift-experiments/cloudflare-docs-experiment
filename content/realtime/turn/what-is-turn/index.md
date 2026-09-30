---
cp9:
  canonical: https://developers.cloudflare.com/realtime/turn/what-is-turn/
  description: TURN relays traffic through NATs and firewalls to enable peer-to-peer WebRTC communication.
  full_title: What is TURN? · Cloudflare Realtime docs
  head_html: <title>What is TURN? · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="TURN relays traffic through NATs and firewalls to enable peer-to-peer WebRTC communication."><link rel="canonical" href="https://developers.cloudflare.com/realtime/turn/what-is-turn/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/turn/what-is-turn/index.md"><meta property="og:title" content="What is TURN? · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="TURN relays traffic through NATs and firewalls to enable peer-to-peer WebRTC communication."><meta property="og:url" content="https://developers.cloudflare.com/realtime/turn/what-is-turn/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/turn/what-is-turn/#page","headline":"What is TURN? \u00b7 Cloudflare Realtime docs","description":"TURN relays traffic through NATs and firewalls to enable peer-to-peer WebRTC communication.","url":"https://developers.cloudflare.com/realtime/turn/what-is-turn/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/turn/what-is-turn/
  schema: 1
---
<h2 id="what-is-turn">What is TURN?</h2>
<p>TURN (Traversal Using Relays around NAT) is a protocol that assists in traversing Network Address Translators (NATs) or firewalls in order to facilitate peer-to-peer communications. It is an extension of the STUN (Session Traversal Utilities for NAT) protocol and is defined in <a href="https://datatracker.ietf.org/doc/html/rfc8656">RFC 8656</a>.</p>
<h2 id="how-do-i-use-turn">How do I use TURN?</h2>
<p>Just like you would use a web browser or cURL to use the HTTP protocol, you need to use a tool or a library to use TURN protocol in your application.</p>
<p>Most users of TURN will use it as part of a WebRTC library, such as the one in their browser or part of <a href="https://github.com/pion/webrtc">Pion</a>, <a href="https://github.com/webrtc-rs/webrtc">webrtc-rs</a> or <a href="https://webrtc.googlesource.com/src/">libwebrtc</a>.</p>
<p>You can use TURN directly in your application too. <a href="https://github.com/pion/turn">Pion</a> offers a TURN client library in Golang, so does <a href="https://github.com/webrtc-rs/webrtc/tree/master/turn">webrtc-rs</a> in Rust.</p>
<h2 id="key-concepts-to-know-when-understanding-turn">Key concepts to know when understanding TURN</h2>
<ol>
<li>
<p><strong>NAT (Network Address Translation)</strong>: A method used by routers to map multiple private IP addresses to a single public IP address. This is commonly done by home internet routers so multiple computers in the same network can share a single public IP address.</p>
</li>
<li>
<p><strong>TURN Server</strong>: A relay server that acts as an intermediary for traffic between clients behind NATs. Cloudflare Realtime TURN service is an example of a TURN server.</p>
</li>
<li>
<p><strong>TURN Client</strong>: An application or device that uses the TURN protocol to communicate through a TURN server. This is your application. It can be a web application using the WebRTC APIs or a native application running on mobile or desktop.</p>
</li>
<li>
<p><strong>Allocation</strong>: When a TURN server creates an allocation, the TURN server reserves an IP and a port unique to that client.</p>
</li>
<li>
<p><strong>Relayed Transport Address</strong>: The IP address and port reserved on the TURN server that others on the Internet can use to send data to the TURN client.</p>
</li>
</ol>
<h2 id="how-turn-works">How TURN Works</h2>
<ol>
<li>A TURN client sends an Allocate request to a TURN server.</li>
<li>The TURN server creates an allocation and returns a relayed transport address to the client.</li>
<li>The client can then give this relayed address to its peers.</li>
<li>When a peer sends data to the relayed address, the TURN server forwards it to the client.</li>
<li>When the client wants to send data to a peer, it sends it through the TURN server, which then forwards it to the peer.</li>
</ol>
<h2 id="turn-vs-vpn">TURN vs VPN</h2>
<p>TURN works similar to a VPN (Virtual Private Network). However TURN servers and VPNs serve different purposes and operate in distinct ways.</p>
<p>A VPN is a general-purpose tool that encrypts all internet traffic from a device, routing it through a VPN server to enhance privacy, security, and anonymity. It operates at the network layer, affects all internet activities, and is often used to bypass geographical restrictions or secure connections on public Wi-Fi.</p>
<p>A TURN server is a specialized tool used by specific applications, particularly for real-time communication. It operates at the application layer, only affecting traffic for applications that use it, and serves as a relay to traverse NATs and firewalls when direct connections between peers are not possible. While a VPN impacts overall internet speed and provides anonymity, a TURN server only affects the performance of specific applications using it.</p>
<h2 id="why-is-turn-useful">Why is TURN Useful?</h2>
<p>TURN is often valuable in scenarios where direct peer-to-peer communication is impossible due to NAT or firewall restrictions. Here are some key benefits:</p>
<ol>
<li>
<p><strong>NAT Traversal</strong>: TURN provides a way to establish connections between peers that are both behind NATs, which would otherwise be challenging or impossible.</p>
</li>
<li>
<p><strong>Firewall Bypassing</strong>: In environments with strict firewall policies, TURN can enable communication that would otherwise be blocked.</p>
</li>
<li>
<p><strong>Consistent Connectivity</strong>: TURN offers a reliable fallback method when direct or NAT-assisted connections fail.</p>
</li>
<li>
<p><strong>Privacy</strong>: By relaying traffic through a TURN server, the actual IP addresses of the communicating parties can be hidden from each other.</p>
</li>
<li>
<p><strong>VoIP and Video Conferencing</strong>: TURN is crucial for applications like Voice over IP (VoIP) and video conferencing, ensuring reliable connections regardless of network configuration.</p>
</li>
<li>
<p><strong>Online Gaming</strong>: TURN can help online games establish peer-to-peer connections between players behind different types of NATs.</p>
</li>
<li>
<p><strong>IoT Device Communication</strong>: Internet of Things (IoT) devices can use TURN to communicate when they're behind NATs or firewalls.</p>
</li>
</ol>
