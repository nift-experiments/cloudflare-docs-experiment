---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/yamaha/
  description: Integrate Yamaha RTX Router with Zero Trust networking.
  full_title: Yamaha RTX Router · Cloudflare One docs
  head_html: <title>Yamaha RTX Router · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Yamaha RTX Router with Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/yamaha/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/yamaha/index.md"><meta property="og:title" content="Yamaha RTX Router · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Yamaha RTX Router with Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/yamaha/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPsec"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/yamaha/#page","headline":"Yamaha RTX Router \u00b7 Cloudflare One docs","description":"Integrate Yamaha RTX Router with Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/yamaha/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPsec"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/yamaha/
  schema: 1
---
<p>This tutorial describes how to configure the Yamaha RTX840 and RTX1300 series router to connect to Cloudflare WAN (formerly Magic WAN) via IPsec tunnels.</p>
<h2 id="testing-environment">Testing environment</h2>
<p>These configurations were tested on the Yamaha RTX840 and RTX1300 series with the following firmware versions:</p>
<ul>
<li><strong>RTX840 series</strong>: 23.02.02</li>
<li><strong>RTX1300 series</strong>: 23.00.17</li>
</ul>
<h2 id="cloudflare-wan-configuration">Cloudflare WAN configuration</h2>
<p>You need to add IPsec tunnels and static routes to your Cloudflare account via the Cloudflare dashboard.</p>
<p>Before proceeding, ensure that you have the anycast IPs assigned to your account. You can find them in the Cloudflare dashboard under <strong>Address Space</strong> &gt; <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Leased IPs</strong></a>.</p>
<h3 id="ipsec-tunnels">IPsec tunnels</h3>
<ol>
<li>
<p>Follow the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> instructions to create the required IPsec tunnel. When creating your IPsec tunnel, make sure you define the following settings:</p>
<ul>
<li><strong>Tunnel name</strong>: Enter your tunnel name. In this example, it is <code>RTX840-vpn01</code>.</li>
<li><strong>Interface address</strong>: Enter the internal tunnel IP on the Cloudflare side of the IPsec tunnel. In this example, it is <code>172.30.223.2/31</code>.</li>
<li><strong>Customer endpoint</strong>: Enter the WAN IP address of your RTX router. In our example, this is <code>194.xx.xx.xx</code>. This is the fixed public IPv4 address you get from your ISP for your internet service.</li>
<li><strong>Cloudflare endpoint</strong>: One of the Cloudflare anycast IP addresses assigned to your account.</li>
<li><strong>Health check rate</strong>: <em>Medium</em>.</li>
<li><strong>Health check type</strong>: <em>Request</em>.</li>
<li><strong>Health check direction</strong>: <em>Bidirectional</em>.</li>
<li><strong>Health check target</strong>: <em>Default</em>.</li>
<li><strong>Pre-shared key</strong>: Select <strong>Use my own pre-shared key</strong> and paste a secure key of your own.</li>
<li><strong>Replay protection</strong>: Do not check the box, to keep this disabled.</li>
</ul>
</li>
<li>
<p>After you create your tunnel, the Cloudflare dashboard will load a list of tunnels set up for your account. Select the IPsec tunnel you have just created, and check the following setting:</p>
<ul>
<li><strong>FQDN ID</strong>: Copy this ID and save it. You will need it when configuring the IPsec tunnel on your RTX router.</li>
</ul>
</li>
</ol>
<h3 id="static-routes">Static routes</h3>
<p>Static routes are required for any networks that will be reached via the IPsec tunnel. In our example, there is one network: <code>172.16.2.0/24</code>.</p>
<p>Follow the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/">Configure static routes</a> instructions to create a static route (settings not mentioned here can be left with their default values):</p>
<ul>
<li><strong>Description</strong>: <code>RTX840-lan01</code></li>
<li><strong>Prefix</strong>: <code>172.16.2.0/24</code></li>
<li><strong>Tunnel/Next hop</strong>: <em>RTX840-vpn01</em></li>
</ul>
<h2 id="rtx-router-configuration">RTX router configuration</h2>
<p>Use the CLI to configure these settings.</p>
<h3 id="route-settings">Route settings</h3>
<pre tabindex="0"><code class="language-txt">ip route default gateway tunnel 1&#10;&#10;ip route &lt;Cloudflare Anycast IP&gt; gateway &lt;ISP provided Gateway IP&gt;&#10;&#10;ip route &lt; ISP&#x27;s DNS server IP &gt; gateway &lt;ISP provided Gateway IP&gt;&#10;</code></pre>
<h3 id="lan-settings">LAN settings</h3>
<pre tabindex="0"><code class="language-txt">ip lan1 address 172.16.2.254/24&#10;</code></pre>
<h3 id="wired-wan-settings">Wired WAN settings</h3>
<pre tabindex="0"><code class="language-txt">ip lan2 address 194.xx.xx.xx/29&#10;&#10;ip lan2 nat descriptor 1000&#10;</code></pre>
<h3 id="ipsec-vpn-main-side-settings">IPsec VPN main side settings</h3>
<pre tabindex="0"><code class="language-txt">tunnel select 1&#10;&#10;ipsec tunnel 1&#10;&#10;ipsec sa policy 1 1 esp aes256-cbc sha256-hmac anti-replay-check=off&#10;&#10;ipsec ike version 1 2&#10;&#10;ipsec ike duration ipsec-sa 1 3600&#10;&#10;ipsec ike duration isakmp-sa 1 28800&#10;&#10;ipsec ike encryption 1 aes256-cbc&#10;&#10;ipsec ike group 1 modp2048&#10;&#10;ipsec ike hash 1 sha256&#10;&#10;ipsec ike keepalive log 1 off&#10;&#10;ipsec ike keepalive use 1 on rfc4306 10 6&#10;&#10;ipsec ike local address 1 194.xx.xx.xx&#10;&#10;ipsec ike log 1 key-info message-info payload-info&#10;&#10;ipsec ike local name 1 &lt;Cloudflare Magic IPsec Tunnel FQDN IP&gt; fqdn&#10;&#10;ipsec ike pfs 1 on&#10;&#10;ipsec ike proposal-limitation 1 on&#10;&#10;ipsec ike pre-shared-key 1 text &lt;Pre-shared key&gt;&#10;&#10;ipsec ike remote address 1 &lt;Cloudflare Anycast IP&gt;&#10;&#10;ipsec ike remote name 1 &lt;Cloudflare Anycast IP&gt; ipv4-addr&#10;&#10;ip tunnel address 172.30.223.3/31&#10;&#10;ip tunnel tcp mss limit auto&#10;&#10;tunnel enable 1&#10;&#10;ipsec auto refresh on&#10;&#10;! Note: 172.30.223.3/31 is internal tunnel IP on the RTX side.&#10;</code></pre>
<h3 id="nat-settings">NAT settings</h3>
<pre tabindex="0"><code class="language-txt">nat descriptor type 1000 masquerade&#10;&#10;nat descriptor address outer 1000 primary&#10;&#10;nat descriptor masquerade static 1000 1 194.xx.xx.xx udp 500&#10;&#10;nat descriptor masquerade static 1000 2 194.xx.xx.xx esp&#10;</code></pre>
<h3 id="dhcp-settings">DHCP settings</h3>
<pre tabindex="0"><code class="language-txt">dhcp service server&#10;&#10;dhcp server rfc2131 compliant except remain-silent&#10;&#10;dhcp scope 1 172.16.2.2-172.16.2.191/24&#10;</code></pre>
<h3 id="dns-settings">DNS settings</h3>
<pre tabindex="0"><code class="language-txt">dns host lan1&#10;&#10;dns server select 1 &lt;ISP&#x27;s DNS server IP&gt; any .&#10;&#10;dns private address spoof on&#10;</code></pre>
<h2 id="connection-test">Connection test</h2>
<p>In the Yamaha RTX router CLI, you can run <code>show ipsec sa</code> and <code>show status tunnel</code> to check the status of the IPsec VPN.</p>
<h3 id="show-ipsec-sa"><code>show ipsec sa</code></h3>
<pre tabindex="0"><code class="language-txt">Total: isakmp:1 send:1 recv:1&#10;&#10;sa    sgw   isakmp        connection    	dir 	 life[s] 	           remote-id&#10;&#10;&#45;-----------------------------------------------------------------------------------------&#10;&#10;1     1    	     -     		ike         	  -   	 27384         （Cloudflare Anycast IP）&#10;&#10;2     1         1    		 tun[0001]esp  send 	 2185           （Cloudflare Anycast IP）&#10;&#10;3     1         1    		 tun[0001]esp  recv 	 2185           （Cloudflare Anycast IP）&#10;</code></pre>
<h3 id="show-status-tunnel-1"><code>show status tunnel 1</code></h3>
<pre tabindex="0"><code class="language-txt">TUNNEL[1]:&#10;&#10;Description:&#10;&#10;Interface type: IPsec&#10;&#10;Current status is Online.&#10;&#10;from 2025/12/08 13:14:20.&#10;&#10;20 minutes 56 seconds  connection.&#10;&#10;Maximum Transmission Unit(MTU):&#10;&#10;IPv4: 1280 octets&#10;&#10;IPv6: 1280 octets&#10;&#10;Received:    (IPv4) 171847 packets [58823472 octets]&#10;&#10;(IPv6) 0 packet [0 octet]&#10;&#10;Transmitted: (IPv4) 154224 packets [19191955 octets]&#10;&#10;(IPv6) 0 packet [0 octet]&#10;&#10;IKE keepalive:&#10;&#10;[Type]: rfc4306&#10;&#10;[Status]: OK&#10;&#10;[Next send]: 1 sec after&#10;</code></pre>
