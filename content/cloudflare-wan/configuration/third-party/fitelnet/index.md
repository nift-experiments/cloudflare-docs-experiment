---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/fitelnet/
  description: Connect Furukawa Electric FITELnet to Cloudflare WAN.
  full_title: Furukawa Electric FITELnet · Cloudflare WAN docs
  head_html: <title>Furukawa Electric FITELnet · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Furukawa Electric FITELnet to Cloudflare WAN."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/fitelnet/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/fitelnet/index.md"><meta property="og:title" content="Furukawa Electric FITELnet · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Furukawa Electric FITELnet to Cloudflare WAN."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/fitelnet/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/fitelnet/#page","headline":"Furukawa Electric FITELnet \u00b7 Cloudflare WAN docs","description":"Connect Furukawa Electric FITELnet to Cloudflare WAN.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/fitelnet/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/third-party/fitelnet/
  schema: 1
---
<p>This tutorial describes how to configure the Furukawa Electric's FITELnet F220 and F70 devices to connect to Cloudflare WAN (formerly Magic WAN) via IPsec (Internet Protocol Security) tunnels. The use cases described in this tutorial are for both east-west (branch to branch) and north-south (Internet-bound).</p>
<h2 id="testing-environment">Testing environment</h2>
<p>These configurations were tested on FITELnet F220 and F70 series with the following firmware versions:</p>
<ul>
<li><strong>F220 series</strong>: Version 01.11(00)</li>
<li><strong>F70 series</strong>: Version 01.09(00)</li>
</ul>
<h2 id="ipsec-configuration">IPsec configuration</h2>
<h3 id="cloudflare-wan-configuration">Cloudflare WAN configuration</h3>
<ol>
<li>Follow the <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> instructions to create the required IPsec tunnels.</li>
<li>For the first IPsec tunnel, ensure the following settings are defined:
<ul>
<li><strong>Tunnel name</strong>: <code>FITEL-tunnel-1</code></li>
<li><strong>Interface address</strong>: Enter <code>10.0.0.1/31</code> for your first tunnel.</li>
<li><strong>Customer endpoint</strong>: This setting is not required unless your router is using an IKE ID of <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">type <code>ID_IPV4_ADDR</code></a>.</li>
<li><strong>Cloudflare endpoint</strong>: One of the Cloudflare anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>.</li>
<li><strong>Pre-shared key</strong>: Create a pre-shared key for your first tunnel.</li>
</ul>
</li>
<li>For the second IPsec tunnel, make the same changes as you did for the first tunnel, and ensure these additional settings are defined:
<ul>
<li><strong>Tunnel name</strong>: <code>FITEL-tunnel-2</code></li>
<li><strong>Interface address</strong>: Enter <code>10.0.0.3/31</code> for your second tunnel.</li>
<li><strong>Customer endpoint</strong>: This setting is not required unless your router is using an IKE ID of <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">type <code>ID_IPV4_ADDR</code></a>.</li>
<li><strong>Cloudflare endpoint</strong>: One of the Cloudflare anycast IP addresses assigned to your account.</li>
<li><strong>Pre-shared key</strong>: Create a pre-shared key for your second tunnel.</li>
</ul>
</li>
</ol>
<h3 id="fitelnet-router-configuration">FITELnet router configuration</h3>
<h4 id="router-1-settings">Router 1 settings</h4>
<p>Use the CLI (Command Line Interface) to configure these settings:</p>
<pre tabindex="0"><code class="language-txt">interface Tunnel 1&#10; ip address 10.0.0.0 255.255.255.254&#10; tunnel mode ipsec map MAP1&#10; link-state sync-sa&#10;exit&#10;!&#10;&#10;crypto ipsec policy IPsec_POLICY&#10; set security-association always-up&#10; set security-association lifetime seconds 28800&#10; set security-association transform-keysize aes 256 256 256&#10; set security-association transform esp-aes esp-sha256-hmac&#10; set mtu 1460&#10; set mss 1350&#10; set ip df-bit 0&#10; set ip fragment post&#10; ! if there is a NAT router between Cloudflare and FITELnet,&#10; ! add the two udp-encapsulation options below&#10; set udp-encapsulation nat-t keepalive interval 30 always-send&#10; set udp-encapsulation-force&#10;exit&#10;!&#10;crypto ipsec selector SELECTOR&#10; src 1 ipv4 any&#10; dst 1 ipv4 any&#10;exit&#10;!&#10;crypto isakmp keepalive&#10;crypto isakmp log sa&#10;crypto isakmp log session&#10;crypto isakmp log negotiation-fail&#10;crypto isakmp negotiation always-up-params interval 100 max-initiate 10 max-pending 10 delay 1&#10;crypto ipsec replay-check disable&#10;!&#10;crypto isakmp policy ISAKMP_POLICY&#10; authentication pre-share&#10; encryption aes&#10; encryption-keysize aes 256 256 256&#10; group 20&#10; lifetime 86400&#10; hash sha sha-256&#10; initiate-mode aggressive&#10;exit&#10;!&#10;crypto isakmp profile PROF1&#10; ! set the value of FQDN ID for self-identify&#10; self-identity fqdn &lt;FQDN-ID-TUNNEL01&gt;&#10; set isakmp-policy ISAKMP_POLICY&#10; set ipsec-policy IPsec_POLICY&#10; set peer &lt;CLOUDFLARE-ANYCAST-ADDRESS&gt;&#10; ike-version 2&#10; local-key &lt;PRE-SHARED-KEY-TUNNEL01&gt;&#10;exit&#10;!&#10;crypto map MAP1 ipsec-isakmp&#10; match address SELECTOR&#10; set isakmp-profile PROF1&#10;exit&#10;!&#10;</code></pre>
<h4 id="router-2-settings">Router 2 settings</h4>
<p>Use the CLI to configure these settings:</p>
<pre tabindex="0"><code class="language-txt">interface Tunnel 2&#10; ip address 10.0.0.2 255.255.255.254&#10; tunnel mode ipsec map MAP1&#10; link-state sync-sa&#10;exit&#10;!&#10;&#10;crypto ipsec policy IPsec_POLICY&#10; set security-association always-up&#10; set security-association lifetime seconds 28800&#10; set security-association transform-keysize aes 256 256 256&#10; set security-association transform esp-aes esp-sha256-hmac&#10; set mtu 1460&#10; set mss 1350&#10; set ip df-bit 0&#10; set ip fragment post&#10; ! if there is a NAT router between Cloudflare and FITELnet,&#10; ! add the two udp-encapsulation options below&#10; set udp-encapsulation nat-t keepalive interval 30 always-send&#10; set udp-encapsulation-force&#10;exit&#10;!&#10;crypto ipsec selector SELECTOR&#10; src 1 ipv4 any&#10; dst 1 ipv4 any&#10;exit&#10;!&#10;crypto isakmp keepalive&#10;crypto isakmp log sa&#10;crypto isakmp log session&#10;crypto isakmp log negotiation-fail&#10;crypto isakmp negotiation always-up-params interval 100 max-initiate 10 max-pending 10 delay 1&#10;crypto ipsec replay-check disable&#10;!&#10;crypto isakmp policy ISAKMP_POLICY&#10; authentication pre-share&#10; encryption aes&#10; encryption-keysize aes 256 256 256&#10; group 20&#10; lifetime 86400&#10; hash sha sha-256&#10; initiate-mode aggressive&#10;exit&#10;!&#10;crypto isakmp profile PROF1&#10; ! set the value of FQDN ID for self-identify&#10; self-identity fqdn &lt;FQDN-ID-TUNNEL02&gt;&#10; set isakmp-policy ISAKMP_POLICY&#10; set ipsec-policy IPsec_POLICY&#10; set peer &lt;CLOUDFLARE-ANYCAST-ADDRESS&gt;&#10; ike-version 2&#10; local-key &lt;PRE-SHARED-KEY-TUNNEL02&gt;&#10;exit&#10;!&#10;crypto map MAP1 ipsec-isakmp&#10; match address SELECTOR&#10; set isakmp-profile PROF1&#10;exit&#10;!&#10;</code></pre>
<h2 id="static-route-configuration">Static route configuration</h2>
<p>To configure routes for east-west (branch to branch) connections, refer to the following settings.</p>
<h3 id="cloudflare-wan">Cloudflare WAN</h3>
<ol>
<li>Follow the <a href="/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Configure static routes</a> instructions to create a static route.</li>
<li>For the first route, ensure the following settings are defined:</li>
</ol>
<ul>
<li><strong>Prefix</strong>: <code>192.168.0.0/24</code></li>
<li><strong>Tunnel/Next hop</strong>: <em>FITEL-tunnel-1 / 10.0.0.0</em></li>
</ul>
<ol start="3">
<li>For the second route, ensure the following settings are defined:</li>
</ol>
<ul>
<li><strong>Prefix</strong>: <code>192.168.1.0/24</code></li>
<li><strong>Tunnel/Next hop</strong>: <em>FITEL-tunnel-2 / 10.0.0.2</em></li>
</ul>
<h3 id="fitelnet-router-configuration-1">FITELnet router configuration</h3>
<h4 id="router-1">Router 1</h4>
<p>Use the CLI to configure these settings:</p>
<pre tabindex="0"><code class="language-txt">ip route 192.168.0.0 255.255.255.0 tunnel 1&#10;</code></pre>
<h4 id="router-2">Router 2</h4>
<p>Use the CLI to configure these settings:</p>
<pre tabindex="0"><code class="language-txt">ip route 192.168.1.0 255.255.255.0 tunnel 2&#10;</code></pre>
<h2 id="connection-test">Connection test</h2>
<h3 id="ipsec-status">IPsec status</h3>
<p>In the FITELnet router CLI, you can run <code>show crypto sa</code> to check the status of the IPsec security associations (SAs). <code>Total number of ISAKMP/IPSEC SA</code> shows the number of established SAs.</p>
<pre tabindex="0"><code class="language-txt">show crypto sa&#10;&#10;  IKE_SA&#10;    Mode: &lt;I&gt;&#10;    Local IP : &lt;LOCAL_IP&gt;/500&#10;    Local ID : &lt;LOCAL_ID&gt; (ipv4)&#10;    Remote IP : anycast-address/500&#10;    Remote ID : anycast-address (ipv4)&#10;    Local Authentication method : Pre-shared key&#10;    Remote Authentication method : Pre-shared key&#10;    Encryption algorithm : aes256-cbc&#10;    Hash algorithm : hmac-sha256-128&#10;    Diffie-Hellman group : 20&#10;    Initiator Cookie : aaaaaaaa bbbbbbbb&#10;    Responder Cookie : cccccccc dddddddd&#10;    Life time : 6852/14400 sec&#10;    DPD : on&#10;&#10;  CHILD_SA &lt;I&gt;&#10;    Selector :&#10;      0.0.0.0/0 ALL ALL &lt;---&gt; 0.0.0.0/0 ALL ALL&#10;    Interface : tunnel 1&#10;    Peer IP : anycast-address/500&#10;    Local IP : xxx.xxx.xxx.xxx/500&#10;    Encryption algorithm : AES-CBC/256&#10;    Authentication algorithm : HMAC-SHA2-256&#10;    Life time : 22868/28800 sec&#10;    PFS : off ESN : off&#10;    IN&#10;      SPI : eeeeeeee&#10;      Packets       : 0&#10;      Octets        : 0&#10;      Replay error  : 0&#10;      Auth error    : 0&#10;      Padding error : 0&#10;      Rule error    : 0&#10;    OUT&#10;      SPI : ffffffff&#10;      Packets       : 0&#10;      Octets        : 0&#10;      Seq lapped    : 0&#10;&#10;  Total number of ISAKMP SA 1&#10;  Total number of IPSEC SA 1&#10;</code></pre>
<h3 id="route-status">Route Status</h3>
<p>In the FITELnet router CLI, you can run <code>show ip route</code> to check the route information. A <code>*</code> in the route information indicates that the route information is valid.</p>
<pre tabindex="0"><code class="language-txt">show ip route&#10;&#10;Codes: K - kernel route, C - connected, S - static, R - RIP, O - OSPF,&#10;       B - BGP, T - Tunnel, i - IS-IS, V - VRRP track,&#10;       Iu - ISAKMP SA up, It - ISAKMP tunnel route, Ip - ISAKMP l2tpv2-ppp&#10;       Dc - DHCP-client, L - Local Breakout&#10;       &gt; - selected route, * - FIB route, p - stale info&#10;&#10;&lt;snip&gt;&#10;S &gt; * 192.168.1.0/24 [100/0] is directly connected, Tunnel1&#10;&lt;snip&gt;&#10;&#35;&#10;</code></pre>
