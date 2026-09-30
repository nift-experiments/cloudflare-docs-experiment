---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/troubleshooting/
  description: Learn how to diagnose and report issues with Cloudflare's DNS Resolver
  full_title: Troubleshooting DNS Resolver · Cloudflare 1.1.1.1 docs
  head_html: <title>Troubleshooting DNS Resolver · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to diagnose and report issues with Cloudflare&#x27;s DNS Resolver"><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting DNS Resolver · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to diagnose and report issues with Cloudflare&#x27;s DNS Resolver"><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_tags" content="Debugging,CLI"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/troubleshooting/#page","headline":"Troubleshooting DNS Resolver \u00b7 Cloudflare 1.1.1.1 docs","description":"Learn how to diagnose and report issues with Cloudflare's DNS Resolver","url":"https://developers.cloudflare.com/1.1.1.1/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging","CLI"]}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/troubleshooting/
  schema: 1
---
<p>This guide helps you diagnose and resolve common issues with Cloudflare's DNS Resolver. Before proceeding with manual troubleshooting steps, <a href="/1.1.1.1/check/">verify your connection</a> to automatically gather relevant information.</p>
<h2 id="name-resolution-issues">Name resolution issues</h2>
<p>If a domain name is not resolving correctly, test DNS resolution against 1.1.1.1 and compare the result to another resolver (such as <code>8.8.8.8</code>). The CHAOS TXT queries (<code>id.server</code>) identify which Cloudflare server handled your request, which is useful when reporting issues.</p>
<h3 id="linux-macos">Linux/macOS</h3>
<pre tabindex="0"><code class="language-sh">&#35; Test DNS resolution&#10;dig example.com @1.1.1.1&#10;dig example.com @1.0.0.1&#10;dig example.com @8.8.8.8&#10;&#10;&#35; Check connected nameserver&#10;dig +short CHAOS TXT id.server @1.1.1.1&#10;dig +short CHAOS TXT id.server @1.0.0.1&#10;&#10;&#35; Optional: Network information&#10;dig @ns3.cloudflare.com whoami.cloudflare.com txt +short&#10;</code></pre>
<h3 id="windows">Windows</h3>
<pre tabindex="0"><code class="language-sh">&#35; Test DNS resolution&#10;nslookup example.com 1.1.1.1&#10;nslookup example.com 1.0.0.1&#10;nslookup example.com 8.8.8.8&#10;&#10;&#35; Check connected nameserver&#10;nslookup -class=chaos -type=txt id.server 1.1.1.1&#10;nslookup -class=chaos -type=txt id.server 1.0.0.1&#10;&#10;&#35; Optional: Network information&#10;nslookup -type=txt whoami.cloudflare.com ns3.cloudflare.com&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1738.md")
</aside>
<p>For additional analysis, you can generate a <a href="http://dnsviz.net/">DNSViz</a> report for the domain in question.</p>
<h2 id="connectivity-and-routing-issues">Connectivity and routing issues</h2>
<p>If DNS queries time out or you cannot reach 1.1.1.1 at all, the problem may be a network routing issue between your device and Cloudflare. Run traceroutes to both resolver addresses to identify where packets are being dropped.</p>
<p>Before reporting connectivity issues:</p>
<ol>
<li>Search for existing reports from your country and ISP.</li>
<li>Run traceroutes to both Cloudflare DNS resolvers.</li>
</ol>
<h3 id="linux-macos-1">Linux/macOS</h3>
<pre tabindex="0"><code class="language-sh">&#35; Basic connectivity tests&#10;traceroute 1.1.1.1&#10;traceroute 1.0.0.1&#10;&#10;&#35; If reachable, check nameserver identity&#10;dig +short CHAOS TXT id.server @1.1.1.1&#10;dig +short CHAOS TXT id.server @1.0.0.1&#10;&#10;&#35; TCP connection tests&#10;dig +tcp @1.1.1.1 id.server CH TXT&#10;dig +tcp @1.0.0.1 id.server CH TXT&#10;</code></pre>
<h3 id="windows-1">Windows</h3>
<pre tabindex="0"><code class="language-sh">&#35; Basic connectivity tests&#10;tracert 1.1.1.1&#10;tracert 1.0.0.1&#10;&#10;&#35; If reachable, check nameserver identity&#10;nslookup -class=chaos -type=txt id.server 1.1.1.1&#10;nslookup -class=chaos -type=txt id.server 1.0.0.1&#10;&#10;&#35; TCP connection tests&#10;nslookup -vc -class=chaos -type=txt id.server 1.1.1.1&#10;nslookup -vc -class=chaos -type=txt id.server 1.0.0.1&#10;</code></pre>
<h2 id="dns-over-tls-dot-troubleshooting">DNS-over-TLS (DoT) troubleshooting</h2>
<p>DNS over TLS encrypts DNS queries using TLS on port <code>853</code>. If your DoT connection is not working, test TLS connectivity and then DNS resolution over TLS.</p>
<h3 id="linux-macos-2">Linux/macOS</h3>
<pre tabindex="0"><code class="language-sh">&#35; Test TLS connectivity&#10;openssl s_client -connect 1.1.1.1:853&#10;openssl s_client -connect 1.0.0.1:853&#10;&#10;&#35; Test DNS resolution over TLS&#10;kdig +tls @1.1.1.1 id.server CH TXT&#10;kdig +tls @1.0.0.1 id.server CH TXT&#10;</code></pre>
<h3 id="windows-2">Windows</h3>
<p>Windows does not include a standalone DoT client. You can test TLS connectivity using OpenSSL after installing it manually.</p>
<h2 id="dns-over-https-doh-troubleshooting">DNS-over-HTTPS (DoH) troubleshooting</h2>
<p>DNS over HTTPS sends DNS queries as HTTPS requests. If your DoH connection is not working, test it by querying the Cloudflare DNS endpoint directly.</p>
<h3 id="linux-macos-3">Linux/macOS</h3>
<pre tabindex="0"><code class="language-sh">curl -H &#x27;accept: application/dns-json&#x27; &#x27;https://cloudflare-dns.com/dns-query?name=cloudflare.com&amp;type=AAAA&#x27;&#10;</code></pre>
<h3 id="windows-3">Windows</h3>
<pre tabindex="0"><code class="language-powershell">(Invoke-WebRequest -Uri &#x27;https://cloudflare-dns.com/dns-query?name=cloudflare.com&amp;type=AAAA&#x27;).RawContent&#10;</code></pre>
<h2 id="common-issues">Common issues</h2>
<h3 id="first-hop-failures">First hop failures</h3>
<p>If your traceroute fails at the first hop (the first network device after your computer, usually your router), the issue is likely hardware-related. Your router may have a hardcoded route for <code>1.1.1.1</code> that conflicts with using it as a DNS resolver. When reporting this issue, include:</p>
<ul>
<li>Router make and model</li>
<li>ISP name</li>
<li>Any relevant router configuration details</li>
</ul>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li><a href="https://1.1.1.1">1.1.1.1 DNS Resolver homepage</a></li>
<li><a href="/1.1.1.1/encryption/dns-over-tls/">DNS over TLS documentation</a></li>
<li><a href="https://one.one.one.one/help/">Diagnostic tool</a></li>
</ul>
