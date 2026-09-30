---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/
  description: Learn how to connect to Cloudflare's 1.1.1.1 using DNS over HTTPS (DoH) clients.
  full_title: Connect to 1.1.1.1 using DoH clients · Cloudflare 1.1.1.1 docs
  head_html: <title>Connect to 1.1.1.1 using DoH clients · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to connect to Cloudflare&#x27;s 1.1.1.1 using DNS over HTTPS (DoH) clients."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/index.md"><meta property="og:title" content="Connect to 1.1.1.1 using DoH clients · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to connect to Cloudflare&#x27;s 1.1.1.1 using DNS over HTTPS (DoH) clients."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/#page","headline":"Connect to 1.1.1.1 using DoH clients \u00b7 Cloudflare 1.1.1.1 docs","description":"Learn how to connect to Cloudflare's 1.1.1.1 using DNS over HTTPS (DoH) clients.","url":"https://developers.cloudflare.com/1.1.1.1/encryption/dns-over-https/dns-over-https-client/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/encryption/dns-over-https/dns-over-https-client/
  schema: 1
---
<p>A DoH client is a software that runs on your device and sends DNS queries to a resolver like 1.1.1.1 over an encrypted HTTPS connection. Once configured, the client handles DNS resolution for your device or network.</p>
<h2 id="cloudflare-warp-client">Cloudflare WARP client</h2>
<p>Refer to <a href="/warp-client/">WARP client</a> for guidance on WARP modes and get-started information for different <a href="/warp-client/get-started/">operating systems</a>.</p>
<h2 id="dnscrypt-proxy">DNSCrypt-Proxy</h2>
<p><a href="https://dnscrypt.info">DNSCrypt-Proxy</a> 2.0+ supports DoH out of the box. It supports both 1.1.1.1 and other services. It also includes more advanced features, such as load balancing and local filtering.</p>
<ol>
<li>
<p><a href="https://github.com/DNSCrypt/dnscrypt-proxy/wiki/installation">Install DNSCrypt-Proxy</a>.</p>
</li>
<li>
<p>Verify that <code>dnscrypt-proxy</code> is installed and the version is 2.0 or later:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">dnscrypt-proxy -version&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">2.0.8&#10;</code></pre>
<ol start="3">
<li>Set up the configuration file using the <a href="https://github.com/DNSCrypt/dnscrypt-proxy/wiki/installation#setting-up-dnscrypt-proxy">official instructions</a>, and add <code>cloudflare</code> and <code>cloudflare-ipv6</code> to the server list in <code>dnscrypt-proxy.toml</code>:</li>
</ol>
<pre tabindex="0"><code class="language-toml">server_names = [&#x27;cloudflare&#x27;, &#x27;cloudflare-ipv6&#x27;]&#10;</code></pre>
<ol start="4">
<li>Make sure that nothing else is running on <code>localhost:53</code> (port <code>53</code> is the standard DNS port on your local machine), and check that everything works as expected:</li>
</ol>
<pre tabindex="0"><code class="language-sh">dnscrypt-proxy -resolve cloudflare-dns.com&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Resolving [cloudflare-dns.com]&#10;&#10;Domain exists:  yes, 3 name servers found&#10;Canonical name: cloudflare-dns.com.&#10;IP addresses:   2400:cb00:2048:1::6810:6f19, 2400:cb00:2048:1::6810:7019, 104.16.111.25, 104.16.112.25&#10;TXT records:    -&#10;Resolver IP:    172.68.140.217&#10;</code></pre>
<ol start="5">
<li>Register it as a system service so that it starts automatically when your device boots. Follow the <a href="https://github.com/DNSCrypt/dnscrypt-proxy/wiki/installation">DNSCrypt-Proxy installation instructions</a>.</li>
</ol>
