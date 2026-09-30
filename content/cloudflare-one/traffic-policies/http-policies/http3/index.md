---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/
  description: How HTTP/3 inspection works in Gateway.
  full_title: HTTP/3 inspection · Cloudflare One docs
  head_html: <title>HTTP/3 inspection · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How HTTP/3 inspection works in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/index.md"><meta property="og:title" content="HTTP/3 inspection · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How HTTP/3 inspection works in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="QUIC,UDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/#page","headline":"HTTP/3 inspection \u00b7 Cloudflare One docs","description":"How HTTP/3 inspection works in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/http3/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["QUIC","UDP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/http-policies/http3/
  schema: 1
---
<p>HTTP/3 uses the QUIC protocol over UDP instead of TCP. Because Gateway's default proxy only handles TCP traffic, HTTP/3 inspection requires turning on the UDP proxy. Without it, HTTP/3 traffic bypasses HTTP inspection. <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a> still apply to the underlying UDP traffic.</p>
<p>Gateway applies HTTP policies to HTTP/3 traffic last. For more information, refer to the <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#http3-traffic">order of enforcement</a>.</p>
<h2 id="turn-on-http-3-inspection">Turn on HTTP/3 inspection</h2>
<p>Before you can inspect any HTTPS traffic, you must deploy a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">user-side certificate</a> to your devices and turn on <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">TLS decryption</a>. To inspect HTTP/3 traffic, you must also turn on the <a href="/cloudflare-one/traffic-policies/proxy/">Gateway proxy</a> for UDP.</p>
<p>To turn on the Gateway proxy for UDP and TLS decryption:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>In <strong>Proxy and inspection</strong>, turn on <strong>Allow Secure Web Gateway to proxy traffic</strong>.</li>
<li>Select <strong>TCP</strong> and <strong>UDP</strong>.</li>
<li>Turn on <strong>TLS decryption</strong>.</li>
</ol>
<h3 id="application-limitations">Application limitations</h3>
<p>Gateway can inspect HTTP/3 traffic from Mozilla Firefox and Microsoft Edge by establishing an HTTP/3 proxy connection. Gateway will then terminate the HTTP/3 connection, decrypt and inspect the traffic, and connect to the destination server over HTTP/2. Gateway can also inspect other HTTP applications, such as cURL.</p>
<p>If both the UDP proxy and TLS decryption are turned on, Google Chrome will automatically cancel HTTP/3 connections and retry them over HTTP/2, which Gateway can inspect. If either the UDP proxy or TLS decryption is turned off, HTTP/3 traffic from Chrome bypasses inspection entirely.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6525.md")
</aside>
<h2 id="exempt-http-3-traffic-from-inspection">Exempt HTTP/3 traffic from inspection</h2>
<p>If you require HTTP/3 traffic with end-to-end encryption from the client to the origin while still using the Gateway proxy, you can create a <a href="/cloudflare-one/traffic-policies/http-policies/#do-not-inspect">Do Not Inspect HTTP policy</a> to match the desired traffic. Using a Do Not Inspect policy allows HTTP/3 traffic to preserve proxy performance and end-to-end encryption by bypassing Gateway's TLS decryption and inspection.</p>
<h2 id="force-http-2-traffic">Force HTTP/2 traffic</h2>
<p>To apply Gateway policies to HTTP traffic without turning on the UDP proxy, you must turn off QUIC in your users' browsers to ensure only HTTP/2 traffic reaches Gateway.</p>
<details class="nb-details"><summary>Google Chrome</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6526.md")
</div></details>
<details class="nb-details"><summary>Safari</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6527.md")
</div></details>
<details class="nb-details"><summary>Firefox</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6528.md")
</div></details>
<details class="nb-details"><summary>Microsoft Edge</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6529.md")
</div></details>
