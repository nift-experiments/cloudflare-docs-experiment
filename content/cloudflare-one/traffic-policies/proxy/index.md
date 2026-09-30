---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/
  description: How Proxy works in Gateway.
  full_title: Proxy · Cloudflare One docs
  head_html: <title>Proxy · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Proxy works in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/index.md"><meta property="og:title" content="Proxy · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Proxy works in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="TCP,UDP,ICMP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/#page","headline":"Proxy \u00b7 Cloudflare One docs","description":"How Proxy works in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/proxy/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TCP","UDP","ICMP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/proxy/
  schema: 1
---
<p>You can forward <a href="/cloudflare-one/traffic-policies/get-started/http/">HTTP</a> and <a href="/cloudflare-one/traffic-policies/get-started/network/">network</a> traffic to Gateway for logging and filtering. Gateway can proxy both outbound traffic and traffic directed to resources connected via a Cloudflare Tunnel, Generic Routing Encapsulation (GRE) tunnel, or IPsec tunnel. When a user connects to the Gateway proxy, Gateway will accept the connection and establish a new, separate connection to the origin server.</p>
<p>The Gateway proxy is required for filtering HTTP and network traffic via the Cloudflare One Client in Traffic and DNS mode. To proxy HTTP traffic without deploying the Cloudflare One Client, you can configure <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC files</a> on your devices.</p>
<h2 id="proxy-algorithm">Proxy algorithm</h2>
<p>Gateway uses the <a href="https://datatracker.ietf.org/doc/html/rfc6555">Happy Eyeballs algorithm</a>, which tries IPv4 and IPv6 connections with a staggered fallback and uses whichever address family responds first, to proxy traffic in the following order:</p>
<ol>
<li>The user's browser initiates the TCP handshake by sending Gateway a TCP SYN segment.</li>
<li>Gateway sends a SYN segment to the origin server.</li>
<li>If the origin server sends a SYN-ACK segment back, Gateway establishes separate TCP connections between the user and Gateway and between Gateway and the origin server.</li>
<li>Gateway inspects and filters traffic received from the user.</li>
<li>If the traffic passes inspection, Gateway proxies traffic bidirectionally between the user and the origin server.</li>
</ol>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;    %% Accessibility&#10;    accTitle: How Gateway proxy works&#10;    accDescr: Flowchart describing how the Gateway proxy uses the Happy Eyeballs algorithm to establish TCP connections and proxy user traffic.&#10;&#10;    %% Flowchart&#10;    A[User&#x27;s device sends TCP SYN to Gateway] --&gt; B[Gateway sends TCP SYN to origin server]&#10;    B --&gt; C{{Origin server responds with TCP SYN-ACK?}}&#10;    C --&gt;|Yes| E[TCP handshakes completed]&#10;    C --&gt;|No| D[Connection fails]&#10;    E --&gt; F{{Connection allowed?}}&#10;    F --&gt;|Allow policy| G[Gateway proxies traffic bidirectionally]&#10;    F --&gt;|Block policy| H[Connection blocked by firewall policies]&#10;&#10;    %% Styling&#10;    style D stroke:#D50000&#10;    style G stroke:#00C853&#10;    style H stroke:#D50000&#10;</code></pre>
<h2 id="supported-protocols">Supported protocols</h2>
<p>Gateway supports proxying TCP, UDP, and ICMP traffic.</p>
<h3 id="tcp">TCP</h3>
<p>When the proxy is enabled, Gateway will always forward TCP traffic.</p>
<p>By default, TCP connection attempts will timeout after 30 seconds and idle connections will disconnect after 8 hours.</p>
<h3 id="udp">UDP</h3>
<p>The UDP proxy forwards UDP traffic such as VoIP, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/private-dns/">internal DNS requests</a>, and thick client applications.</p>
<p>HTTP/3 uses the QUIC protocol over UDP. To inspect HTTP/3 traffic, turn on both TLS decryption and the UDP proxy. Gateway will then intercept the HTTP/3 connection and connect to the origin server over HTTP/2. Otherwise, HTTP/3 traffic will bypass inspection. For more information on browser-specific behavior, refer to <a href="/cloudflare-one/traffic-policies/http-policies/http3/">HTTP/3 inspection</a>.</p>
<h3 id="icmp-internet-control-message-protocol">ICMP (Internet Control Message Protocol)</h3>
<p>The ICMP proxy allows ICMP traffic to reach your private network through Gateway. For example, this would allow a Cloudflare One Client user to run diagnostic commands such as <code>ping</code> and <code>traceroute</code> to an internal server IP.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="limitation">Limitation</h3>
@markup("md", "content/.markup/bodies/4392.md")
</aside>
<h4 id="allow-icmp-traffic-through-cloudflared">Allow ICMP traffic through <code>cloudflared</code></h4>
<p>To use the ICMP proxy with Cloudflare Tunnel, you may need to configure the <code>cloudflared</code> host to allow ICMP traffic through <code>cloudflared</code>.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4395.md")
</div></div>
<h2 id="turn-on-the-gateway-proxy">Turn on the Gateway proxy</h2>
<p>The Gateway proxy toggle only applies to traffic from Cloudflare One Client devices. Gateway will always proxy traffic sent with <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">PAC files</a> or <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> regardless of this setting.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>In <strong>Proxy and inspection settings</strong>, turn on <strong>Allow Secure Web Gateway to proxy traffic</strong>.</li>
<li>Select <strong>TCP</strong>.</li>
<li>(Optional) Depending on your use case, you can select <strong>UDP</strong> and/or <strong>ICMP</strong>.</li>
</ol>
