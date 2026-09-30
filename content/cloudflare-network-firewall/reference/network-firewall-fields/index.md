---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/
  description: Fields available in Network Firewall rule expressions.
  full_title: Cloudflare Network Firewall fields · Cloudflare Network Firewall docs
  head_html: <title>Cloudflare Network Firewall fields · Cloudflare Network Firewall docs</title><meta name="generator" content="Nift"><meta name="description" content="Fields available in Network Firewall rule expressions."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/index.md"><meta property="og:title" content="Cloudflare Network Firewall fields · Cloudflare Network Firewall docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fields available in Network Firewall rule expressions."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Network Firewall"><meta name="algolia_product_filter" content="Cloudflare Network Firewall"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Network Firewall"><meta name="pcx_tags" content="TCP,UDP,ICMP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/#page","headline":"Cloudflare Network Firewall fields \u00b7 Cloudflare Network Firewall docs","description":"Fields available in Network Firewall rule expressions.","url":"https://developers.cloudflare.com/cloudflare-network-firewall/reference/network-firewall-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["TCP","UDP","ICMP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-network-firewall/reference/network-firewall-fields/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4235.md")
</aside>
<h2 id="cf-colo-name"><code>cf.colo.name</code></h2>
<p><code>cf.colo.name</code> <span class="nb-type">String</span></p>
<p>The data center that is handling this traffic.</p>
<p>Example value: <code>sfo06</code></p>
<hr />
<h2 id="cf-colo-region"><code>cf.colo.region</code></h2>
<p><code>cf.colo.region</code> <span class="nb-type">String</span></p>
<p>Region of the data center that is handling this traffic.</p>
<p>Example value: <code>WNAM</code></p>
<hr />
<h2 id="icmp"><code>icmp</code></h2>
<p><code>icmp</code> <span class="nb-type">String</span></p>
<p>The raw ICMP packet as a list of bytes. It should be used in conjunction with the bit_slice function when other structured fields are lacking.</p>
<hr />
<h2 id="icmp-type"><code>icmp.type</code></h2>
<p><code>icmp.type</code> <span class="nb-type">Number</span></p>
<p>The <a href="https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#header_type">ICMP type</a>. Only applies to ICMP packets.</p>
<p>Example value: <code>8</code></p>
<hr />
<h2 id="icmp-code"><code>icmp.code</code></h2>
<p><code>icmp.code</code> <span class="nb-type">Number</span></p>
<p>The <a href="https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#header_code">ICMP code</a>. Only applies to ICMP packets.</p>
<p>Example value: <code>2</code></p>
<hr />
<h2 id="ip"><code>ip</code></h2>
<p><code>ip</code> <span class="nb-type">String</span></p>
<p>The raw IP packet as a list of bytes. It should be used in conjunction with the bit_slice function when other structured fields are lacking.</p>
<hr />
<h2 id="ip-dst"><code>ip.dst</code></h2>
<p><code>ip.dst</code> <span class="nb-type">IP address</span></p>
<p>The destination address as specified in the IP packet.</p>
<p>Example value: <code>192.0.2.2</code></p>
<hr />
<h2 id="ip-dst-country"><code>ip.dst.country</code></h2>
<p><code>ip.dst.country</code> <span class="nb-type">String</span></p>
<p>Represents the 2-letter country code associated with the server IP address in <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> format.</p>
<p>Example value: <code>GB</code></p>
<p>For more information on the ISO 3166-1 Alpha 2 format, refer to <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 Alpha 2</a> on Wikipedia.</p>
<hr />
<h2 id="ip-src-country"><code>ip.src.country</code></h2>
<p><code>ip.src.country</code> <span class="nb-type">String</span></p>
<p>Represents the 2-letter country code associated with the client IP address in <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> format.</p>
<p>Example value: <code>GB</code></p>
<p>For more information on the ISO 3166-1 Alpha 2 format, refer to <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 Alpha 2</a> on Wikipedia.</p>
<p>For Cloudflare Network Firewall, the <code>ip.geoip.country</code> field (which is deprecated) will match on either source or destination address. The <code>ip.geoip.country</code> field is still available for new and existing rules, but you should use the <code>ip.src.country</code> and/or <code>ip.dst.country</code> fields instead.</p>
<hr />
<h2 id="ip-hdr-len"><code>ip.hdr_len</code></h2>
<p><code>ip.hdr_len</code> <span class="nb-type">Number</span></p>
<p>The length of the IPv4 header in bytes.</p>
<p>Example value: <code>5</code></p>
<hr />
<h2 id="ip-len"><code>ip.len</code></h2>
<p><code>ip.len</code> <span class="nb-type">Number</span></p>
<p>The length of the packet including the header.</p>
<p>Example value: <code>60</code></p>
<hr />
<h2 id="ip-opt-type"><code>ip.opt.type</code></h2>
<p><code>ip.opt.type</code> <span class="nb-type">Number</span></p>
<p>The first byte of <a href="https://en.wikipedia.org/wiki/IPv4#Options">IP options field</a>, if the options field is set.</p>
<p>Example value: <code>25</code></p>
<hr />
<h2 id="ip-proto"><code>ip.proto</code></h2>
<p><code>ip.proto</code> <span class="nb-type">String</span></p>
<p>The transport layer for the packet, if it can be determined.</p>
<p>Example values: <code>icmp</code>, <code>tcp</code></p>
<hr />
<h2 id="ip-src"><code>ip.src</code></h2>
<p><code>ip.src</code> <span class="nb-type">IP address</span></p>
<p>The source address of the IP Packet.</p>
<hr />
<h2 id="ip-src-country-1"><code>ip.src.country</code></h2>
<p><code>ip.src.country</code> <span class="nb-type">String</span></p>
<p>Represents the 2-letter country code associated with the client IP address in <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> format.</p>
<p>Example value: <code>GB</code></p>
<p>For more information on the ISO 3166-1 Alpha 2 format, refer to <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 Alpha 2</a> on Wikipedia.</p>
<hr />
<h2 id="ip-ttl"><code>ip.ttl</code></h2>
<p><code>ip.ttl</code> <span class="nb-type">Number</span></p>
<p>The time-to-live of the IP Packet.</p>
<p>Example values: <code>54</code></p>
<hr />
<h2 id="sip"><code>sip</code></h2>
<p><code>sip</code> <span class="nb-type">Boolean</span></p>
<p>Determines if packets are valid L7 protocol <a href="https://datatracker.ietf.org/doc/html/rfc2543">SIP</a>. Requires UDP packets to operate.</p>
<p>Use a guard clause as shown below to ensure the packet is UDP (wirefilter):</p>
<p><code>ip.proto == &quot;udp&quot;</code></p>
<hr />
<h2 id="ip-src-asnum"><code>ip.src.asnum</code></h2>
<p><code>ip.src.asnum</code> <span class="nb-type">Number</span></p>
<p>Autonomous System (AS) number associated with the source IP address.</p>
<p>Example values: <code>13335</code></p>
<hr />
<h2 id="ip-dst-asnum"><code>ip.dst.asnum</code></h2>
<p><code>ip.dst.asnum</code> <span class="nb-type">Number</span></p>
<p>Autonomous System (AS) number associated with the destination IP address.</p>
<p>Example value: <code>15169</code></p>
<hr />
<h2 id="tcp"><code>tcp</code></h2>
<p><code>tcp</code> <span class="nb-type">String</span></p>
<p>The raw TCP packet as a list of bytes. It should be used in conjunction with the bit_slice function when other structured fields are lacking.</p>
<hr />
<h2 id="tcp-flags"><code>tcp.flags</code></h2>
<p><code>tcp.flags</code> <span class="nb-type">Number</span></p>
<p>The numeric value of the TCP flags byte.</p>
<hr />
<h2 id="tcp-flags-ack"><code>tcp.flags.ack</code></h2>
<p><code>tcp.flags.ack</code> <span class="nb-type">Boolean</span></p>
<p>TCP acknowledgment flag.</p>
<hr />
<h2 id="tcp-flags-cwr"><code>tcp.flags.cwr</code></h2>
<p><code>tcp.flags.cwr</code> <span class="nb-type">Boolean</span></p>
<p>TCP congestion window reduced flag.</p>
<hr />
<h2 id="tcp-flags-ecn"><code>tcp.flags.ecn</code></h2>
<p><code>tcp.flags.ecn</code> <span class="nb-type">Boolean</span></p>
<p>TCP ECN-Echo flag.</p>
<hr />
<h2 id="tcp-flags-fin"><code>tcp.flags.fin</code></h2>
<p><code>tcp.flags.fin</code> <span class="nb-type">Boolean</span></p>
<p>TCP flag indicating this is the last packet from sender.</p>
<hr />
<h2 id="tcp-flags-push"><code>tcp.flags.push</code></h2>
<p><code>tcp.flags.push</code> <span class="nb-type">Boolean</span></p>
<p>TCP push flag.</p>
<hr />
<h2 id="tcp-flags-reset"><code>tcp.flags.reset</code></h2>
<p><code>tcp.flags.reset</code> <span class="nb-type">Boolean</span></p>
<p>TCP reset flag.</p>
<hr />
<h2 id="tcp-flags-syn"><code>tcp.flags.syn</code></h2>
<p><code>tcp.flags.syn</code> <span class="nb-type">Boolean</span></p>
<p>TCP synchronize flag.</p>
<hr />
<h2 id="tcp-flags-urg"><code>tcp.flags.urg</code></h2>
<p><code>tcp.flags.urg</code> <span class="nb-type">Boolean</span></p>
<p>TCP urgent flag.</p>
<hr />
<h2 id="tcp-srcport"><code>tcp.srcport</code></h2>
<p><code>tcp.srcport</code> <span class="nb-type">Number</span></p>
<p>Source port number of the IP packet. Only applies to TCP packets.</p>
<hr />
<h2 id="tcp-dstport"><code>tcp.dstport</code></h2>
<p><code>tcp.dstport</code> <span class="nb-type">Number</span></p>
<p>Destination port number of the IP packet. Only applies to TCP packets.</p>
<hr />
<h2 id="udp"><code>udp</code></h2>
<p><code>udp</code> <span class="nb-type">String</span></p>
<p>The raw UDP packet as a list of bytes. It should be used in conjunction with the bit_slice function when other structured fields are lacking.</p>
<hr />
<h2 id="udp-dstport"><code>udp.dstport</code></h2>
<p><code>udp.dstport</code> <span class="nb-type">Number</span></p>
<p>Destination port number of the IP packet. Only applies to UDP packets.</p>
<hr />
<h2 id="udp-srcport"><code>udp.srcport</code></h2>
<p><code>udp.srcport</code> <span class="nb-type">Number</span></p>
<p>Source port number of the IP packet. Only applies to UDP packets.</p>
<hr />
<p><em>GeoIP is the registered trademark of MaxMind, Inc.</em></p>
