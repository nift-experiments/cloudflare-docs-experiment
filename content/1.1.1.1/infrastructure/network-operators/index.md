---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/infrastructure/network-operators/
  description: Information for network operators peering with 1.1.1.1.
  full_title: Network operators · Cloudflare 1.1.1.1 docs
  head_html: <title>Network operators · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Information for network operators peering with 1.1.1.1."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/infrastructure/network-operators/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/infrastructure/network-operators/index.md"><meta property="og:title" content="Network operators · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Information for network operators peering with 1.1.1.1."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/infrastructure/network-operators/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/infrastructure/network-operators/#page","headline":"Network operators \u00b7 Cloudflare 1.1.1.1 docs","description":"Information for network operators peering with 1.1.1.1.","url":"https://developers.cloudflare.com/1.1.1.1/infrastructure/network-operators/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/infrastructure/network-operators/
  schema: 1
---
<p>Network operators, including Internet Service Providers (ISPs), device manufacturers, public Wi-Fi networks, municipal broadband providers, and security scanning services can use <a href="/1.1.1.1/setup/">1.1.1.1</a> in place of operating their own recursive DNS infrastructure — DNS servers that resolve queries on behalf of clients by querying authoritative nameservers across the internet.</p>
<p>Cloudflare also partners with ISPs and network equipment providers to make <a href="/1.1.1.1/setup/#1111-for-families">1.1.1.1 for Families</a> available within their offerings. Refer to our <a href="https://blog.cloudflare.com/safer-resolver/">blog post</a> for details.</p>
<p>Using 1.1.1.1 can improve performance for end-users due to Cloudflare's extensive <a href="https://www.cloudflare.com/network/">global network</a>, as well as provide higher overall cache hit rates (the percentage of DNS queries answered from cache rather than requiring a new upstream lookup) due to our regional caches.</p>
<p>The 1.1.1.1 resolver was designed with a privacy-first approach. Refer to our <a href="/1.1.1.1/privacy/public-dns-resolver/">data and privacy policies</a> for what is logged and retained by 1.1.1.1.</p>
<h2 id="configuring-1-1-1-1">Configuring 1.1.1.1</h2>
<p>There are multiple ways to use 1.1.1.1 as an operator:</p>
<ul>
<li>Including a <a href="/1.1.1.1/encryption/dns-over-https/">DNS over HTTPS</a> or <a href="/1.1.1.1/encryption/dns-over-tls/">DNS over TLS</a> proxy on end-user routers or devices (best for privacy).</li>
<li>Pushing 1.1.1.1 to devices via DHCP/PPP (the protocols operators use to automatically assign network settings, including DNS servers, to devices) within an operator network (recommended; most practical).</li>
<li>Having a DNS proxy on an edge router make requests to 1.1.1.1 on behalf of all connected devices.</li>
</ul>
<p>Where possible, we recommend using encrypted transports (DNS over HTTPS or TLS) for queries, as this provides the highest degree of privacy for users over last-mile networks (the final segment of connectivity between the operator and the end user).</p>
<h2 id="available-endpoints">Available Endpoints</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1813.md")
</aside>
<p>The publicly available endpoints for 1.1.1.1 are detailed in the following table. Each resolver variant serves a different filtering level: the unfiltered resolver performs standard DNS resolution with no content blocking, the Malware variant blocks queries to domains associated with malware and phishing, and the Adult Content + Malware variant blocks adult content in addition to malware and phishing.</p>
<table>
<thead>
<tr>
<th>Resolver</th>
<th>IPv4 address</th>
<th>IPv6 <br /> address</th>
<th>DNS over <br /> HTTPS endpoint</th>
<th>DNS over <br /> TLS endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>1.1.1.1 <br />(unfiltered)</td>
<td><code>1.1.1.1</code> <br /> <code>1.0.0.1</code></td>
<td><code>2606:4700:4700::1111</code> <br /> <code>2606:4700:4700::1001</code></td>
<td><code>https://cloudflare-dns.com/dns-query</code></td>
<td><code>one.one.one.one</code></td>
</tr>
<tr>
<td>Families <br />(Malware)</td>
<td><code>1.1.1.2</code> <br /> <code>1.0.0.2</code></td>
<td><code>2606:4700:4700::1112</code> <br /> <code>2606:4700:4700::1002</code></td>
<td><code>https://security.cloudflare-dns.com/dns-query</code></td>
<td><code>security.cloudflare-dns.com</code></td>
</tr>
<tr>
<td>Families <br />(Adult Content + Malware)</td>
<td><code>1.1.1.3</code> <br /> <code>1.0.0.3</code></td>
<td><code>2606:4700:4700::1113</code> <br /> <code>2606:4700:4700::1003</code></td>
<td><code>https://family.cloudflare-dns.com/dns-query</code></td>
<td><code>family.cloudflare-dns.com</code></td>
</tr>
</tbody>
</table>
<p>You may wish to provide end users with options to change from the default 1.1.1.1 resolver to one of the <a href="/1.1.1.1/setup/#1111-for-families">1.1.1.1 for Families</a> endpoints.</p>
<h2 id="rate-limiting">Rate Limiting</h2>
<p>Operators using 1.1.1.1 for typical Internet-facing applications and/or users should not encounter any rate limiting for their users. In some rare cases, security scanning use-cases or proxied traffic may be rate limited to protect our infrastructure as well as upstream DNS infrastructure from potential abuse.</p>
<p>Best practices include:</p>
<ul>
<li>Avoiding tunneling or proxying all queries from a single IP address at high rates. Distributing queries across multiple public IPs will improve this without impacting cache hit rates (caches are regional).</li>
<li>A high rate of &quot;uncacheable&quot; responses (such as <code>SERVFAIL</code>, a DNS response code indicating the server failed to complete the query) against the same domain may be rate limited to protect upstream, authoritative nameservers (the DNS servers that hold the official records for a domain). Many authoritative nameservers enforce their own rate limits, and we strive to avoid overloading third party infrastructure where possible.</li>
</ul>
<h2 id="help">Help</h2>
<p>If you are a network operator and still have outstanding questions, contact <code>resolver@cloudflare.com</code> with your use case, so it can be discussed further. Make sure to visit <a href="https://one.one.one.one/help">1.1.1.1/help</a> from within your network and share the resulting report when contacting Cloudflare.</p>
