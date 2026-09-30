---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/
  description: DNS over TLS (DoT) in Zero Trust networking.
  full_title: DNS over TLS (DoT) · Cloudflare One docs
  head_html: <title>DNS over TLS (DoT) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="DNS over TLS (DoT) in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/index.md"><meta property="og:title" content="DNS over TLS (DoT) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="DNS over TLS (DoT) in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS,TLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/#page","headline":"DNS over TLS (DoT) \u00b7 Cloudflare One docs","description":"DNS over TLS (DoT) in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS","TLS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/resolvers-and-proxies/dns/dns-over-tls/
  schema: 1
---
<p>By default, DNS is sent over a plaintext connection. DNS over TLS (DoT) is a standard for encrypting DNS queries to keep them secure and private. DoT uses the same security protocol, TLS, that HTTPS websites use to encrypt and authenticate communications.</p>
<p>Cloudflare supports DoT on standard port <code>853</code> over TLS 1.2 and TLS 1.3 in compliance with <a href="https://tools.ietf.org/html/rfc7858">RFC7858</a>.</p>
<h2 id="configure-dot-queries">Configure DoT queries</h2>
<h3 id="1-obtain-your-dot-hostname"><ol>
<li>Obtain your DoT hostname</li>
</ol></h3>
<p>Each Gateway DNS location has a unique DoT hostname. DNS locations and corresponding DoT hostnames have policies associated with them.</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong>.</li>
<li>Under <strong>DNS locations</strong>, <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">add a new location</a> or select an existing location from the list.</li>
<li>Under <strong>DoT endpoint</strong>, copy the value in <strong>DoT addresses</strong>.</li>
</ol>
<p>The DoT hostname contains your unique location name. For example, if the DoT hostname is <code>9y65g5srsm.cloudflare-gateway.com</code>, the location name is <code>9y65g5srsm</code>.</p>
<h3 id="2-configure-your-dot-client"><ol start="2">
<li>Configure your DoT client</li>
</ol></h3>
<p>To configure a DoT client such as <code>dig</code>, specify the IP address and the DoT hostname for your location in your query. For example:</p>
<pre tabindex="0"><code class="language-txt">Hostname: 9y65g5srsm.cloudflare-gateway.com&#10;IP address: 162.159.36.5&#10;</code></pre>
<p>Alternatively, you can use the generic DoT endpoint (<code>dns.cloudflare-gateway.com</code>) and include an <code>OPT</code> record with code <code>65011</code>. You can select a specific location for the value of the <code>OPT</code> record. For example:</p>
<pre tabindex="0"><code class="language-txt">Hostname: dns.cloudflare-gateway.com&#10;IP address: 162.159.36.5&#10;OPT Record:&#10;  &#45; Code: 65011&#10;  &#45; Value: 9y65g5srsm&#10;</code></pre>
<p>Some stub resolvers support DoT natively. For example, you can configure Unbound to send a DoT query:</p>
<pre tabindex="0"><code class="language-txt">&#35; Unbound TLS Config&#10;tls-cert-bundle: &quot;/etc/ssl/cert.pem&quot;&#10;&#35; Forwarding Config&#10;forward-zone:&#10; name: &quot;.&quot;&#10; forward-tls-upstream: yes&#10; forward-addr: 162.159.36.5@853#9y65g5srsm.cloudflare-gateway.com&#10; forward-addr: 2001:db8:abcd::1234#9y65g5srsm.cloudflare-gateway.com&#10;</code></pre>
