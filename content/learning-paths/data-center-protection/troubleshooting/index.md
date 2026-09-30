---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/data-center-protection/troubleshooting/
  description: Learn about troubleshooting connectivity issues after prefix advertisement in this guide.
  full_title: Troubleshooting connectivity issues after prefix advertisement · Cloudflare Learning Paths
  head_html: <title>Troubleshooting connectivity issues after prefix advertisement · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about troubleshooting connectivity issues after prefix advertisement in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/data-center-protection/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/data-center-protection/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting connectivity issues after prefix advertisement · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about troubleshooting connectivity issues after prefix advertisement in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/data-center-protection/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Magic Transit,DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/data-center-protection/troubleshooting/#page","headline":"Troubleshooting connectivity issues after prefix advertisement \u00b7 Cloudflare Learning Paths","description":"Learn about troubleshooting connectivity issues after prefix advertisement in this guide.","url":"https://developers.cloudflare.com/learning-paths/data-center-protection/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/data-center-protection/troubleshooting/
  schema: 1
---
<h2 id="for-magic-transit-ingress-only-with-direct-server-return">For Magic Transit ingress-only with Direct Server Return</h2>
<h3 id="magic-transit-devices-cannot-reach-internet-ips-after-cutover-to-cloudflare">Magic Transit devices cannot reach Internet IPs after cutover to Cloudflare.</h3>
<p><strong>Potential solutions</strong>:</p>
<ul>
<li>Run a traceroute from the Magic Transit prefix out to the destination IP on the Internet.</li>
<li>Verify on your CPE there is no uRPF strict mode or anti-spoofing which would drop this traffic.</li>
<li>Verify that your CPE is not enforcing uRPF strict mode or other anti-spoofing mechanisms that could drop this traffic. If they do, ask them to change this to loose mode.</li>
<li>Other workarounds:
<ul>
<li>If you have a less-specific prefix then you can continue to advertise this to your ISP while Cloudflare advertises a more-specific prefix. For example, Cloudflare advertises a <code>/24</code> to the Internet; you advertise its parent <code>/23</code> to your ISP.</li>
<li>You can continue advertising a <code>/24</code> to your ISP, but this is not recommended, as inbound traffic from your ISP would bypass Cloudflare and therefore not benefit from Magic Transit DDoS protection.</li>
</ul>
</li>
</ul>
<h3 id="devices-connected-to-the-magic-transit-prefix-cannot-access-internet-websites-via-tcp-on-ports-443-or-80-https-http">Devices connected to the Magic Transit prefix cannot access Internet websites via TCP on ports <code>443</code> or <code>80</code> (HTTPS/HTTP)</h3>
<p><strong>Potential solutions</strong>:</p>
<ul>
<li>The MSS clamp is configured on all your CPE egress ports at the location where the Magic Transit prefix is configured.</li>
<li>Confirm the MSS values advertised in the TCP SYN-ACK by capturing packets at both ends of the traffic flow — for example, on the remote Internet IP and on your Magic Transit device.</li>
<li>To quickly test whether the issue is related to MTU or MSS settings, you can temporarily lower the MSS clamp on the LAN interface of a test device within the Magic Transit prefix. If this resolves the issue, it confirms that the MSS clamp setting needs to be fine-tuned for your prefix. Be sure to verify that the correct MSS clamp is applied on all egress interfaces of your edge CPE(s).</li>
</ul>
<h3 id="devices-on-the-internet-cannot-access-a-tcp-service-on-magic-transit-prefix">Devices on the Internet cannot access a TCP service on Magic Transit prefix</h3>
<p>For example, devices cannot browse to a server which is hosted on the Magic Transit prefix.</p>
<p><strong>Potential solutions</strong>:</p>
<ul>
<li>The MSS clamp is configured on all your CPE egress ports at the location where the Magic Transit prefix is configured.</li>
<li>Confirm the MSS values advertised in the TCP SYN-ACK by capturing packets at both ends of the traffic flow — for example, on the remote Internet IP and on your Magic Transit device.</li>
<li>To quickly test whether the issue is related to MTU or MSS settings, you can temporarily lower the MSS clamp on the LAN interface of a test device within the Magic Transit prefix. If this resolves the issue, it confirms that the MSS clamp setting needs to be fine-tuned for your prefix. Be sure to verify that the correct MSS clamp is applied on all egress interfaces of your edge CPE(s).</li>
</ul>
<h3 id="users-report-issues-with-ipsec-or-gre-traffic-between-magic-transit-and-third-parties">Users report issues with IPsec or GRE traffic between Magic Transit and third parties</h3>
<p><strong>Potential solutions</strong>:</p>
<ul>
<li>The MSS clamp is properly applied to traffic traversing the IPsec/GRE tunnel. Use packet captures at both tunnel endpoints to inspect the MSS values advertised in the TCP SYN-ACK.</li>
<li>Verify the MSS setting on your firewall's IPsec internal tunnel interface connected to the Magic Transit prefix. Set it to approximately 1300 bytes to avoid fragmentation of inbound packets traversing the Magic Transit GRE tunnel (MTU 1476 bytes). For GRE tunnels, adjust the MSS by subtracting 24 bytes from the original value to account for GRE encapsulation overhead.</li>
<li>If this does not work, then you can reach out to Cloudflare to ask that we enable the <code>clear don't fragment</code> bit for a specific endpoint IP on your prefix which is having the problem, to see if that resolves the issue.</li>
</ul>
<h3 id="cloudflare-might-be-dropping-valid-traffic-to-your-magic-transit-prefix">Cloudflare might be dropping valid traffic to your Magic Transit prefix</h3>
<p>If you suspect that Cloudflare mitigations might be dropping legitimate traffic to your Magic Transit prefix:</p>
<ol>
<li>Go to the Network analytics page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In the <strong>All traffic</strong> tab select <strong>Add filter</strong> to configure the filters for the traffic-flow in question — like source IP, destination IP and protocol/ports.</li>
<li>Check the analytics results to determine which Cloudflare mitigation system has dropped the traffic — for example, DDoS Managed Rules, Advanced TCP/DNS Protection or Network Firewall.</li>
<li>If the traffic was dropped by DDoS Managed Rules:
<ul>
<li>Check whether the rule that dropped the traffic is customizable. If it is, go to <a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/#create-a-ddos-override">DDoS Overrides</a>. There, you can create/amend an existing override to ensure that this endpoint IP is added to the override with a lower sensitivity applied.</li>
<li>If this rule is not customizable and is part of Cloudflare's always-on standard DDoS mitigations, reach out to Cloudflare support team to request for assistance on this.</li>
</ul>
</li>
<li>If the traffic was dropped by Advanced TCP Protection (ATP):
<ul>
<li>If the mode for the global rule is <strong>Mitigation</strong> you can set up a filter for <code>monitoring</code> so that ATP will not drop traffic for this particular traffic flow.</li>
<li>If you need further assistance, reach out to your Cloudflare support team who can adjust other backend configuration options for this mitigation system.</li>
</ul>
</li>
<li>If the traffic was dropped by Advanced DNS Protection:
<ul>
<li>You can create a rule to apply on traffic received in a region or datacenter with a lower sensitivity setting. Once created, you can change the mode of the rule to <code>monitoring</code>.</li>
<li>Alternatively, you can change the mode for the global rule from <code>mitigation</code> to <code>monitoring</code>.</li>
</ul>
</li>
<li>If the traffic was dropped by Network Firewall:
<ul>
<li>Check which configured Network Firewall rule caused the drop.</li>
<li>You can choose to edit the rule or disable it. You can also add a new rule to permit your traffic and ensure it is placed above the rule that is configured to drop the traffic.</li>
</ul>
</li>
</ol>
<h2 id="for-magic-transit-ingress-egress">For Magic Transit ingress + egress</h2>
<h3 id="devices-using-your-magic-transit-ip-cannot-reach-any-internet-sites-via-tcp-udp-or-icmp">Devices using your Magic Transit IP cannot reach any Internet sites via TCP, UDP, or ICMP</h3>
<p><strong>Potential solutions</strong>:</p>
<ul>
<li>If you are using Cloudflare Magic Transit leased IPs, ensure your CPE is correctly NATing to the Cloudflare leased IP and has policy-based Routing configured properly to forward egress traffic via the Magic Transit IPsec/GRE tunnel.</li>
<li>Check that the Network Firewall rules are configured to allow the egress traffic. As a reminder, Network Firewall is stateless, and configured rules will apply for both ingress and egress traffic.</li>
<li>Check that the egress traffic flow is visible inside Network Analytics. Also, check for the inbound traffic flow returning to the Magic Transit prefix. Verify if any mitigations are applied on the traffic.</li>
</ul>
<p>If the problem is seen for TCP only and UDP/ICMP are successful, check the MSS and MTU configuration on your CPE's GRE/IPsec tunnel. Perform a packet capture on the CPE/end-device to confirm the SYN-ACK values exchanged.</p>
