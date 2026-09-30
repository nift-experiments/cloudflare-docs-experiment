---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/
  description: Learn how Cloudflare 1.1.1.1 supports Oblivious DNS over HTTPS (ODoH) to enhance privacy by separating HTTP request contents from requester IP addresses.
  full_title: Oblivious DNS over HTTPS · Cloudflare 1.1.1.1 docs
  head_html: <title>Oblivious DNS over HTTPS · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how Cloudflare 1.1.1.1 supports Oblivious DNS over HTTPS (ODoH) to enhance privacy by separating HTTP request contents from requester IP addresses."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/index.md"><meta property="og:title" content="Oblivious DNS over HTTPS · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how Cloudflare 1.1.1.1 supports Oblivious DNS over HTTPS (ODoH) to enhance privacy by separating HTTP request contents from requester IP addresses."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_tags" content="Privacy,Proxying"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/#page","headline":"Oblivious DNS over HTTPS \u00b7 Cloudflare 1.1.1.1 docs","description":"Learn how Cloudflare 1.1.1.1 supports Oblivious DNS over HTTPS (ODoH) to enhance privacy by separating HTTP request contents from requester IP addresses.","url":"https://developers.cloudflare.com/1.1.1.1/encryption/oblivious-dns-over-https/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Privacy","Proxying"]}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/encryption/oblivious-dns-over-https/
  schema: 1
---
<p>With standard <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS (DoH)</a>, your DNS queries are encrypted, but the resolver still sees both your IP address and the domain you are looking up. Oblivious DNS over HTTPS (ODoH) adds a privacy layer so that no single entity can see both pieces of information at the same time.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1815.md")
</aside>
<h2 id="how-odoh-works">How ODoH works</h2>
<p>ODoH introduces two roles between your device and the DNS resolver:</p>
<ul>
<li><strong>Proxy</strong> — Forwards your encrypted DNS query to the target. The proxy can see your IP address but cannot read the query because it is encrypted.</li>
<li><strong>Target</strong> — Receives and decrypts the DNS query, then sends it to the upstream resolver. The target can read the query but only sees the proxy's IP address, not yours.</li>
</ul>
<p>Because the query is encrypted before it reaches the proxy, and the target never learns your IP address:</p>
<ul>
<li>The proxy has no visibility into the DNS messages, with no ability to identify, read, or modify either the query being sent by the client or the answer being returned by the target.</li>
<li>The target only has access to the encrypted query and the proxy's IP address, while not having visibility over the client's IP address.</li>
<li>Only the intended target can read the content of the query and produce a response, which is also encrypted.</li>
</ul>
<p>This means that, as long as the proxy and the target do not collude, no single entity can have access to both the DNS messages and the client IP address at the same time. Clients are in complete control of proxy and target selection, so you can choose a proxy and target operated by different organizations to reduce collusion risk.</p>
<p>Clients encrypt their query for the target using Hybrid Public Key Encryption (<a href="https://blog.cloudflare.com/hybrid-public-key-encryption/">HPKE</a>), a standard for encrypting messages to a recipient using their public key. A target's public key is obtained via DNS, where it is bundled into an HTTPS resource record and protected by DNSSEC.</p>
<h2 id="cloudflare-and-third-party-products">Cloudflare and third-party products</h2>
<p>Cloudflare 1.1.1.1 supports ODoH by acting as a target that can be reached at <code>odoh.cloudflare-dns.com</code>.</p>
<p>To make ODoH queries you can use open source clients such as <a href="https://github.com/DNSCrypt/dnscrypt-proxy">dnscrypt-proxy</a>.</p>
<p><a href="https://support.apple.com/102602">iCloud Private Relay</a> uses similar privacy-separation principles and uses <a href="https://blog.cloudflare.com/icloud-private-relay/">Cloudflare as one of their partners</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/hybrid-public-key-encryption/">HPKE: Standardizing public-key encryption</a> blog post</li>
<li><a href="/privacy-gateway/">Privacy Gateway</a></li>
</ul>
