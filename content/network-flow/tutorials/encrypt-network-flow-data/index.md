---
cp9:
  canonical: https://developers.cloudflare.com/network-flow/tutorials/encrypt-network-flow-data/
  description: Encrypt the network flowData sent from your router to Cloudflare by routing your network traffic through a device running the Cloudflare One Client.
  full_title: Network Flow encrypt network flow data · Cloudflare Network Flow docs
  head_html: <title>Network Flow encrypt network flow data · Cloudflare Network Flow docs</title><meta name="generator" content="Nift"><meta name="description" content="Encrypt the network flowData sent from your router to Cloudflare by routing your network traffic through a device running the Cloudflare One Client."><link rel="canonical" href="https://developers.cloudflare.com/network-flow/tutorials/encrypt-network-flow-data/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-flow/tutorials/encrypt-network-flow-data/index.md"><meta property="og:title" content="Network Flow encrypt network flow data · Cloudflare Network Flow docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Encrypt the network flowData sent from your router to Cloudflare by routing your network traffic through a device running the Cloudflare One Client."><meta property="og:url" content="https://developers.cloudflare.com/network-flow/tutorials/encrypt-network-flow-data/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Flow"><meta name="algolia_product_filter" content="Network Flow"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Network Flow"><meta name="pcx_tags" content="Shell,CLI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-flow/tutorials/encrypt-network-flow-data/#page","headline":"Network Flow encrypt network flow data \u00b7 Cloudflare Network Flow docs","description":"Encrypt the network flowData sent from your router to Cloudflare by routing your network traffic through a device running the Cloudflare One Client.","url":"https://developers.cloudflare.com/network-flow/tutorials/encrypt-network-flow-data/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Shell","CLI"]}</script>
  markdown: true
  noindex: false
  route: /network-flow/tutorials/encrypt-network-flow-data/
  schema: 1
---
<p>You can encrypt the network flow data sent from your router to Cloudflare by <a href="https://www.cloudflare.com/learning/network-layer/what-is-routing/">routing</a> your network flow traffic through a device running the Cloudflare One Client. Encrypted network flow traffic is then forwarded from the Cloudflare One Client device to Cloudflare's network flow endpoints.</p>
<p>To learn more about the Cloudflare One Client, and to install it on Linux, macOS, or Windows, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client documentation</a>.</p>
<h2 id="1-configure-your-devices"><ol>
<li>Configure your devices</li>
</ol></h2>
<p>Follow the instructions in the <a href="/api/resources/magic_network_monitoring/subresources/configs/methods/edit/">Network Flow (formerly Magic Network Monitoring) API</a> to configure your devices.</p>
<p>The <code>warp_devices</code> array at the account level is a list of WARP devices through which you can send encrypted flows. Each WARP device must have:</p>
<ul>
<li>The Cloudflare One Client UUID. You can obtain the UUID in the UI or through the following command:</li>
</ul>
<pre tabindex="0"><code class="language-sh">warp-cli registration show&#10;</code></pre>
<ul>
<li>A name.</li>
<li>A <code>router_ip</code> that belongs to one of your configured router IP addresses.</li>
</ul>
<p>For example:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/mnm/config \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;warp_devices&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;&lt;YOUR_WARP_DEVICE_UNIQUE_IDENTIFIER&gt;&quot;,&#10;      &quot;name&quot;: &quot;&lt;NAME_OF_WARP_DEVICE&gt;&quot;,&#10;      &quot;router_ip&quot;: &quot;YOUR_ROUTER_IP&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h2 id="2-route-network-flow-traffic-through-the-cloudflare-one-client"><ol start="2">
<li>Route Network Flow traffic through the Cloudflare One Client</li>
</ol></h2>
<p>Depending on where you installed the Cloudflare One Client, you may need to configure other devices on the subnet to route traffic through the Cloudflare One Client. If you have access to your router and it runs a version/OS supported by the Cloudflare One Client, Cloudflare recommends <a href="#option-1-default-gateway">Option 1</a>. This also applies if you use a software-based flow exporter (such as <code>softflowd</code>) instead of a physical router to collect and export flows.</p>
<h3 id="option-1-default-gateway">Option 1: Default gateway</h3>
<p>If you installed the Cloudflare One Client on your router or machine collector (a computer, virtual machine, or server that collects flow information), no additional configuration is necessary. All traffic uses the router as the default gateway. Configure your flow export to send data to IP address <code>162.159.65.1</code> and port <code>2055</code> for NetFlow, or <code>162.159.65.1</code> and port <code>6343</code> for sFlow.</p>
<h3 id="option-2-alternate-gateway">Option 2: Alternate gateway</h3>
<p>If you have access to the router but installed the Cloudflare One Client on another machine, you can configure the router to export flow traffic to the machine running the Cloudflare One Client. To do this:</p>
<ol>
<li>Set the machine's IP address as the export destination on the router.</li>
<li>Configure the export port on the router to match the listening port on the Cloudflare One Client machine.</li>
<li>Redirect traffic that arrives at your machine running the Cloudflare One Client to the following Cloudflare destination IPs and ports:
<ul>
<li><strong>For NetFlow</strong>: IP address <code>162.159.65.1</code> and port <code>2055</code>.</li>
<li><strong>For sFlow</strong>: IP <code>162.159.65.1</code> and port <code>6343</code>. <br />
For example, if WARP is running on a machine in your network with the IP <code>10.10.10.10</code>, and you configured it to accept traffic on port <code>2055</code> or <code>6343</code>, you need to configure your flow export-capable router to send data to <code>10.10.10.10</code> and port <code>2055</code> or <code>6343</code>.</li>
</ul>
</li>
</ol>
<p>In the machine running the Cloudflare One Client, you can redirect this traffic to Cloudflare using a proxy or redirect tool of your choice. Options include:</p>
<ul>
<li>Using <code>socat</code>, listen on the desired port for UDP traffic. Then, proxy that traffic to Network Flow's destination and port.
<ul>
<li><code>socat UDP-LISTEN:2055,reuseaddr,fork UDP:162.159.65.1:2055</code></li>
<li><code>socat UDP-LISTEN:6343,reuseaddr,fork UDP:162.159.65.1:6343</code></li>
</ul>
</li>
<li>Using any other proxy or port forwarding tool, such as <code>netcat</code>, <code>uredir</code> or <code>iptables</code>.</li>
</ul>
<h2 id="3-optional-configure-split-tunnels"><ol start="3">
<li>(Optional) Configure split tunnels</li>
</ol></h2>
<p>If you do not want all traffic on your device to route through the Cloudflare One Client, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">configure split tunnels/proxy mode</a> to either only allow Network Flow traffic towards <code>162.159.65.1</code> or exclude everything else.</p>
