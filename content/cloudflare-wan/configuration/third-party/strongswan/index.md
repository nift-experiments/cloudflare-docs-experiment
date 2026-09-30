---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/strongswan/
  description: Connect strongSwan to Cloudflare WAN.
  full_title: strongSwan · Cloudflare WAN docs
  head_html: <title>strongSwan · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect strongSwan to Cloudflare WAN."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/strongswan/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/strongswan/index.md"><meta property="og:title" content="strongSwan · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect strongSwan to Cloudflare WAN."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/strongswan/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/strongswan/#page","headline":"strongSwan \u00b7 Cloudflare WAN docs","description":"Connect strongSwan to Cloudflare WAN.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/strongswan/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/third-party/strongswan/
  schema: 1
---
<p>This tutorial explains how to set up strongSwan along with Cloudflare WAN (formerly Magic WAN). You will learn how to configure strongSwan, configure an IPsec tunnel, and create Policy-Based Routing (PBR).</p>
<h2 id="1-configure-health-checks"><ol>
<li>Configure health checks</li>
</ol></h2>
<p>Configure the <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">bidirectional health checks</a> target for Cloudflare WAN. For this tutorial, use <code>172.64.240.252</code> as the target IP address, and <code>type</code> as the request.</p>
<p>This can be set up <a href="/api/resources/magic_transit/subresources/ipsec_tunnels/methods/update/">with the API</a>. For example:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/ipsec_tunnels/{tunnel_id} \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;health_check&quot;: {&#10;    &quot;enabled&quot;: true,&#10;    &quot;target&quot;: &quot;172.64.240.252&quot;,&#10;    &quot;type&quot;: &quot;request&quot;,&#10;    &quot;rate&quot;: &quot;mid&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<h2 id="2-configure-strongswan"><ol start="2">
<li>Configure strongSwan</li>
</ol></h2>
<ol>
<li><a href="https://docs.strongswan.org/docs/5.9/install/install.html">Install strongSwan</a>. For example, open the console and run:</li>
</ol>
<pre tabindex="0"><code class="language-sh">sudo apt-get install strongswan -y&#10;</code></pre>
<ol start="2">
<li>Open <code>/etc/strongswan.conf</code> and add the following settings:</li>
</ol>
<pre tabindex="0"><code class="language-txt">charon {&#10;    load_modular = yes&#10;    install_routes = no&#10;    install_virtual_ip = no&#10;&#10;    plugins {&#10;        include strongswan.d/charon/*.conf&#10;    }&#10;}&#10;&#10;include strongswan.d/*.conf&#10;</code></pre>
<h2 id="3-configure-the-ipsec-file"><ol start="3">
<li>Configure the IPsec file</li>
</ol></h2>
<ol>
<li>Open <code>/etc/ipsec.conf</code> and add the following settings:</li>
</ol>
<pre tabindex="0"><code class="language-txt">&#35; ipsec.conf - strongSwan IPsec configuration file&#10;config setup&#10;    charondebug=&quot;all&quot;&#10;    uniqueids = yes&#10;&#10;conn %default&#10;    ikelifetime=24h&#10;    rekey=yes&#10;    reauth=no&#10;    keyexchange=ikev2&#10;    authby=secret&#10;    dpdaction=restart&#10;    closeaction=restart&#10;&#10;&#35; Sample VPN connections&#10;conn cloudflare-ipsec&#10;    auto=start&#10;    type=tunnel&#10;    fragmentation=no&#10;    leftauth=psk&#10;    &#35; Private IP of the VM&#10;    left=%any&#10;    &#35; Tunnel ID from dashboard, in this example FQDN is used&#10;    leftid=&lt;YOUR_TUNNEL_ID&gt;.&lt;YOUR_ACCOUNT_ID&gt;.ipsec.cloudflare.com&#10;    leftsubnet=0.0.0.0/0&#10;    &#35; Cloudflare Anycast IP&#10;    right=&lt;YOUR_CLOUDFLARE_ANYCAST_IP&gt;&#10;    rightid=&lt;YOUR_CLOUDFLARE_ANYCAST_IP&gt;&#10;    rightsubnet=0.0.0.0/0&#10;    rightauth=psk&#10;    ike=aes256-sha256-ecp384!&#10;    esp=aes256-sha256-ecp384!&#10;    replay_window=0&#10;    mark_in=42&#10;    mark_out=42&#10;    leftupdown=/etc/strongswan.d/ipsec-vti.sh&#10;</code></pre>
<ol start="2">
<li>
<p>Create a virtual tunnel interface (VTI) with the IP configured as the target for Cloudflare's health checks (<code>172.64.240.252</code>) to route IPsec packets. Open <code>/etc/strongswan.d/</code>.</p>
</li>
<li>
<p>Create a script called <code>ipsec-vti.sh</code> and add the following:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">&#35;!/bin/bash&#10;&#10;set -o nounset&#10;set -o errexit&#10;&#10;VTI_IF=&quot;vti0&quot;&#10;&#10;case &quot;${PLUTO_VERB}&quot; in&#10;    up-client)&#10;        ip tunnel add &quot;${VTI_IF}&quot; local &quot;${PLUTO_ME}&quot; remote &quot;${PLUTO_PEER}&quot; mode vti \&#10;        key &quot;${PLUTO_MARK_OUT%%/*}&quot;&#10;        ip link set &quot;${VTI_IF}&quot; up&#10;        ip addr add 172.64.240.252/32 dev vti0&#10;        sysctl -w &quot;net.ipv4.conf.${VTI_IF}.disable_policy=1&quot;&#10;        sysctl -w &quot;net.ipv4.conf.${VTI_IF}.rp_filter=0&quot;&#10;        sysctl -w &quot;net.ipv4.conf.all.rp_filter=0&quot;&#10;        ip rule add from 172.64.240.252 lookup viatunicmp&#10;        ip route add default dev vti0 table viatunicmp&#10;        ;;&#10;    down-client)&#10;        ip tunnel del &quot;${VTI_IF}&quot;&#10;        ip rule del from 172.64.240.252 lookup viatunicmp&#10;        ip route del default dev vti0 table viatunicmp&#10;        ;;&#10;esac&#10;echo &quot;executed&quot;&#10;</code></pre>
<h2 id="4-add-policy-based-routing"><ol start="4">
<li>Add policy-based routing</li>
</ol></h2>
<p>Create Policy-Based Routing (PBR) to redirect returning traffic through the IPsec tunnel. Without it, the ICMP replies to the health probes sent by Cloudflare will be returned through the Internet, instead of the same IPsec tunnel.</p>
<p>This tutorial uses <a href="https://en.wikipedia.org/wiki/Iproute2">iproute2</a> to route IP packets from <code>172.64.240.252</code> to the tunnel interface.</p>
<ol>
<li>
<p>Open <code>/etc/iproute2/</code>.</p>
</li>
<li>
<p>Edit the <code>rt_tables</code> file to add a routing table number and name. In this example, use <code>viatunicmp</code> as the name and <code>200</code> as the number for the routing table.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">&#35;&#10;&#35; reserved values&#10;&#35;&#10;255 local&#10;254 main&#10;253 default&#10;0   unspec&#10;200 viatunicmp&#10;&#35;&#10;&#35; local&#10;&#35;&#10;&#35;1  inr.ruhep&#10;</code></pre>
<ol start="3">
<li>Add a rule to match the routing table. This rule instructs the system to use routing table <code>viatunicmp</code> if the packet's source address is <code>172.64.240.252</code>:</li>
</ol>
<pre tabindex="0"><code class="language-sh">ip rule add from 172.64.240.252 lookup viatunicmp&#10;</code></pre>
<ol start="4">
<li>Add a route to the <code>viatunicmp</code> routing table. This is the default route through the interface <code>vti0</code> in the <code>viatunicmp</code> table.</li>
</ol>
<pre tabindex="0"><code class="language-sh">ip route add default dev vti0 table viatunicmp&#10;</code></pre>
<ol start="5">
<li>Start IPsec. You can also <code>stop</code>, <code>restart</code>, and show the <code>status</code> for the IPsec connection:</li>
</ol>
<pre tabindex="0"><code class="language-bash">ipsec start&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">Security Associations (1 up, 0 connecting):&#10;cloudflare-ipsec[1]: ESTABLISHED 96 minutes ago, &lt;IPSEC_TUNNEL_IDENTIFIER&gt;.ipsec.cloudflare.com]...162.159.67.88[162.159.67.88]&#10;cloudflare-ipsec{4}:  INSTALLED, TUNNEL, reqid 1, ESP SPIs: c4e20a95_i c5373d00_o&#10;cloudflare-ipsec{4}:   0.0.0.0/0 === 0.0.0.0/0&#10;</code></pre>
<h2 id="5-check-connection-status"><ol start="5">
<li>Check connection status</li>
</ol></h2>
<p>Use tcpdump to investigate the status of health checks originated from Cloudflare.</p>
<pre tabindex="0"><code class="language-sh">sudo tcpdump -i &lt;OUTGOING_INTERFACE&gt; esp and host &lt;TUNNEL_CLOUDFLARE_ENDPOINT_IP&gt;&#10;</code></pre>
<p>In this example, the outgoing Internet interface shows that the IPsec encrypted packets (ESP) from Cloudflare's health check probes (both the request and response) are going through the IPsec tunnel.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/strongswan/ipsec.png" alt="tcpdump shows the IPsec encrypted packets from Cloudflare's health probes" /></p>
<p>Run tcpdump on <code>vti0</code> to check the decrypted packets.</p>
<pre tabindex="0"><code class="language-sh">sudo tcpdump -i vti0 host 172.64.240.252&#10;</code></pre>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/strongswan/tcpdump.png" alt="If you run tcpdump on vti0 you can check for decrypted packets" /></p>
