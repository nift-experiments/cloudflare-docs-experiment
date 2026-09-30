---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/
  description: Allow Cloudflare IP addresses at your origin server and configure your firewall to prevent accidental blocking of proxied traffic.
  full_title: Cloudflare IP addresses · Cloudflare Fundamentals docs
  head_html: <title>Cloudflare IP addresses · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Allow Cloudflare IP addresses at your origin server and configure your firewall to prevent accidental blocking of proxied traffic."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/index.md"><meta property="og:title" content="Cloudflare IP addresses · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Allow Cloudflare IP addresses at your origin server and configure your firewall to prevent accidental blocking of proxied traffic."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/#page","headline":"Cloudflare IP addresses \u00b7 Cloudflare Fundamentals docs","description":"Allow Cloudflare IP addresses at your origin server and configure your firewall to prevent accidental blocking of proxied traffic.","url":"https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/concepts/cloudflare-ip-addresses/
  schema: 1
---
<p>When you add a domain to Cloudflare and <a href="/dns/proxy-status/">proxy its DNS records</a>, visitors who look up your domain receive a Cloudflare IP address instead of your origin server's real IP address. This hides your origin server's IP address and allows Cloudflare to optimize, cache, and protect all requests before forwarding them to you.</p>
<p>Cloudflare has several <a href="https://www.cloudflare.com/ips/">IP address ranges</a> which are shared by all proxied hostnames. Together, these IP addresses form the backbone of Cloudflare's <span class="nb-glossary-tooltip" title="anycast">anycast network</span> — a routing method where the same IP address is announced from data centers worldwide, so each visitor's request is routed to a nearby data center.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8926.md")
</aside>
<h2 id="allow-cloudflare-ip-addresses">Allow Cloudflare IP addresses</h2>
<p>All traffic to <a href="/dns/proxy-status/">proxied DNS records</a> passes through Cloudflare before reaching your origin server. This means that your origin server will stop receiving traffic from individual visitor IP addresses and instead receive traffic from <a href="https://www.cloudflare.com/ips">Cloudflare IP addresses</a>, which are shared by all proxied hostnames.</p>
<p>To your origin server's firewall, this can look like a limited number of sources sending a high volume of traffic — which may trigger automatic blocking or <span class="nb-glossary-tooltip" title="rate limiting">rate limiting</span>. Because all visitor traffic appears to come from Cloudflare IP addresses, blocking these IPs — even accidentally — will prevent visitor traffic from reaching your application.</p>
<p>The guidance above applies to domains that use Cloudflare's HTTP proxy. <a href="/magic-transit/">Magic Transit</a> works differently — instead of proxying web requests, it protects entire IP networks at the network layer. Cloudflare announces your IP address ranges (prefixes) via BGP so that all traffic destined for your network passes through Cloudflare for inspection and DDoS filtering before being forwarded to your infrastructure.</p>
<h2 id="configure-origin-server">Configure origin server</h2>
<h3 id="allowlist-cloudflare-ip-addresses">Allowlist Cloudflare IP addresses</h3>
<p>To avoid blocking Cloudflare IP addresses unintentionally, you also want to allow Cloudflare IP addresses at your origin web server.</p>
<p>You can explicitly allow these IP addresses with a <a href="https://httpd.apache.org/docs/trunk/mod/mod_authz_core.html#require">.htaccess file</a> or by using <a href="https://www.linode.com/docs/security/firewalls/control-network-traffic-with-iptables/#block-or-allow-traffic-by-port-number-to-create-an-iptables-firewall">iptables</a>.</p>
<p>The following example demonstrates how you could use an iptables rule to allow a Cloudflare IP address range. Replace <code>$ip</code> below with one of the <a href="https://www.cloudflare.com/ips">Cloudflare IP address ranges</a>. You will need to run this command once for each IP range listed on that page.</p>
<pre tabindex="0"><code class="language-bash">&#35; For IPv4 addresses&#10;iptables -I INPUT -p tcp -m multiport --dports http,https -s $ip -j ACCEPT&#10;&#10;&#35; For IPv6 addresses&#10;ip6tables -I INPUT -p tcp -m multiport --dports http,https -s $ip -j ACCEPT&#10;</code></pre>
<p>For more specific guidance, contact your hosting provider or website administrator.</p>
<h3 id="block-other-ip-addresses-recommended">Block other IP addresses (recommended)</h3>
<p>If someone discovers your origin server's IP address — for example, through historical DNS records or mail server configuration — they could send traffic directly to your server, bypassing Cloudflare's security protections entirely. To prevent this, block all traffic that does not come from Cloudflare IP addresses or the IP addresses of your trusted partners, vendors, or applications.</p>
<p>For example, you might <a href="https://www.linode.com/docs/guides/control-network-traffic-with-iptables/#block-or-allow-traffic-by-port-number-to-create-an-iptables-firewall">update your iptables</a> with the following commands:</p>
<pre tabindex="0"><code class="language-sh">&#35; For IPv4 addresses&#10;iptables -A INPUT -p tcp -m multiport --dports http,https -j DROP&#10;&#35; For IPv6 addresses&#10;ip6tables -A INPUT -p tcp -m multiport --dports http,https -j DROP&#10;</code></pre>
<p>For more specific guidance, contact your hosting provider or website administrator.</p>
<h2 id="review-external-tools">Review external tools</h2>
<p>To avoid blocking Cloudflare IP addresses unintentionally, review your external tools to check that:</p>
<ul>
<li>Any security plugins — such as those for WordPress — allow Cloudflare IP addresses.</li>
<li>The <a href="https://github.com/SpiderLabs/ModSecurity">ModSecurity</a> plugin is up to date.</li>
</ul>
<h3 id="further-protection">Further protection</h3>
<p>For further recommendations on securing your origin server, refer to our guide on <a href="/fundamentals/security/protect-your-origin-server/">protecting your origin server</a>.</p>
<h3 id="customize-cloudflare-ip-addresses">Customize Cloudflare IP addresses</h3>
<p>Enterprise customers who do not want to use Cloudflare IP addresses — which are shared by all proxied hostnames — have two potential alternatives:</p>
<ul>
<li><a href="/byoip/"><strong>Bring Your Own IP (BYOIP)</strong></a>: Cloudflare announces your IPs (an IP address range you lease/own) in all of our <a href="https://www.cloudflare.com/network/">locations</a>.</li>
<li><strong>Static IP addresses</strong>: Cloudflare sets static IP addresses for your domain. For more details, contact your account team.</li>
</ul>
<p>Business and Enterprise customers can also reduce the number of Cloudflare IPs that their domain shares with other Cloudflare customer domains by <a href="/ssl/edge-certificates/custom-certificates/">uploading a Custom SSL certificate</a>.</p>
<h3 id="ip-range-updates">IP range updates</h3>
<p>Cloudflare's IP ranges do not change frequently. When they do change, they are added to our <a href="https://www.cloudflare.com/en-in/ips/">list of IP ranges</a> before being put into production. You can also use the Cloudflare API to programmatically keep your configuration updated.</p>
<h2 id="aws-vpc-routing-conflict-with-cloudflare-ip-ranges">AWS VPC routing conflict with Cloudflare IP ranges</h2>
<p>Cloudflare uses <strong>172.64.0.0/13</strong> (172.64.0.0–172.71.255.255) as public egress IP space. This range is <strong>not RFC 1918 private space</strong>. RFC 1918 covers 172.16.0.0/12 (172.16.0.0–172.31.255.255), which does not overlap with 172.64.0.0/13.</p>
<p>AWS VPC route tables sometimes include a route covering <code>172.16.0.0/12</code> (or a broader supernet such as <code>172.16.0.0/8</code>) for Transit Gateway or VPN connectivity. If this route points to an internal target rather than an Internet Gateway, it can capture Cloudflare's 172.64.x.x traffic before it reaches the Internet Gateway, causing connection errors (521, 522) from Cloudflare data centers that use this range.</p>
<p><strong>To resolve:</strong></p>
<ol>
<li>Check your AWS VPC route table for any route covering a <code>172.x.x.x</code> range that routes to an internal target (Transit Gateway, VPN Gateway, NAT Gateway, or VPC peering connection).</li>
<li>Add a more-specific route with destination <code>172.64.0.0/13</code> targeting your Internet Gateway. More-specific routes take precedence in AWS routing.</li>
<li>Alternatively, narrow the broad route to exactly <code>172.16.0.0/12</code> (the RFC 1918 range), which does not include 172.64.0.0/13.</li>
</ol>
<p>This issue does not appear in security group audits because security groups are evaluated at the instance level, not the routing layer.</p>
