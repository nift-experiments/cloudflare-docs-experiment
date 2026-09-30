---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/setup/router/
  description: Configure 1.1.1.1 on your router.
  full_title: Set up 1.1.1.1 on a router · Cloudflare 1.1.1.1 docs
  head_html: <title>Set up 1.1.1.1 on a router · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure 1.1.1.1 on your router."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/setup/router/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/setup/router/index.md"><meta property="og:title" content="Set up 1.1.1.1 on a router · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure 1.1.1.1 on your router."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/setup/router/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/setup/router/#page","headline":"Set up 1.1.1.1 on a router \u00b7 Cloudflare 1.1.1.1 docs","description":"Configure 1.1.1.1 on your router.","url":"https://developers.cloudflare.com/1.1.1.1/setup/router/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/setup/router/
  schema: 1
---
<p>Configuring 1.1.1.1 on your router applies the DNS setting to every device on your network. You do not need to change DNS settings on individual phones, computers, or other devices.</p>
<ol>
<li>
<p>Go to the <strong>IP address</strong> used to access your router's admin console in your browser.</p>
<ul>
<li>Linksys and Asus routers typically use <code>http://192.168.1.1</code> or <code>http://router.asus.com</code> (for ASUS).</li>
<li>Netgear routers typically use <code>http://192.168.1.1</code> or <code>http://routerlogin.net</code>.</li>
<li>D-Link routers typically use <code>http://192.168.0.1</code>.</li>
<li>Ubiquiti routers typically use <code>http://unifi.ubnt.com</code>.</li>
<li>MikroTik routers typically use <code>http://192.168.88.1</code>.</li>
</ul>
</li>
<li>
<p>Enter the router credentials. For consumer routers, the default credentials for the admin console are often found under or behind the device.</p>
</li>
<li>
<p>In the admin console, locate the section where <strong>DNS settings</strong> are configured. This may be contained within categories such as <strong>WAN</strong> and <strong>IPv6</strong> (Asus routers), <strong>IP</strong> (MikroTik routers), or <strong>Internet</strong> (Netgear routers). Consult your router's documentation for details.</p>
</li>
<li>
<p>Take note of any DNS addresses that are currently set and save them in a safe place in case you need to use them later.</p>
</li>
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv4:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1759.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1760.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1761.md")
</div></details>
<ol start="6">
<li></li>
</ol>
<p>Depending on what you want to configure, choose one of the following DNS addresses for IPv6:</p>
<details class="nb-details"><summary>Use 1.1.1.1 resolver</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1762.md")
</div></details>
<details class="nb-details"><summary>Block malware with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1763.md")
</div></details>
<details class="nb-details"><summary>Block malware and adult content with 1.1.1.1 for Families</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/1764.md")
</div></details>
<ol start="7">
<li>Save the updated settings.</li>
</ol>
<h2 id="use-dns-over-tls-on-openwrt">Use DNS over TLS on OpenWrt</h2>
<p>If your router runs OpenWrt, you can encrypt DNS traffic using DNS over TLS. For setup instructions, refer to <a href="https://blog.cloudflare.com/dns-over-tls-for-openwrt/">Adding DNS-Over-TLS support to OpenWrt (LEDE) with Unbound</a>.</p>
<h2 id="fritz-box">FRITZ!Box</h2>
<p>Starting with <a href="https://en.avm.de/press/press-releases/2020/07/fritzos-720-more-performance-convenience-security/">FRITZ!OS 7.20</a>, DNS over TLS is supported. Refer to <a href="https://en.avm.de/service/knowledge-base/dok/FRITZ-Box-7590/165_Configuring-different-DNS-servers-in-the-FRITZ-Box/">Configuring different DNS servers in the FRITZ!Box</a>.</p>
